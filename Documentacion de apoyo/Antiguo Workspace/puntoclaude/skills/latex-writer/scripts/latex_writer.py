#!/usr/bin/env python3
"""
LaTeX Writer - Main entry point
Intelligent LaTeX document generator with template management
y bucle de auto-debug: compila, parsea errores, corrige y recompila.
"""

import sys
import json
import subprocess
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Dict, Any, List

# Import modules
from template_manager import TemplateManager, Template
from latex_generator import LaTeXGenerator, DocumentStructure
from pdf_builder import PDFBuilder, BuildResult
from latex_debugger import LaTeXDebugger, debug_tex_file, DebugResult

MAX_DEBUG_ATTEMPTS = 5


class LaTeXWriter:
    """Main LaTeX Writer class con auto-debug loop."""

    def __init__(self):
        self.template_manager = TemplateManager()
        self.pdf_builder: Optional[PDFBuilder] = None
    
    def select_template(
        self,
        user_input: str,
        document_type: Optional[str] = None
    ) -> Optional[Template]:
        """Select best matching template based on user input"""
        matches = self.template_manager.match_template(
            user_input,
            document_type
        )
        
        if matches:
            best_match, confidence = matches[0]
            print(f"Selected template: {best_match.name} (confidence: {confidence:.2f})")
            return best_match
        
        return None
    
    def generate_latex(
        self,
        template: Template,
        document: DocumentStructure
    ) -> str:
        """Generate LaTeX source code"""
        generator = LaTeXGenerator(template)
        return generator.generate(document)
    
    def build_pdf(
        self,
        latex_code: str,
        output_name: str = "document"
    ) -> BuildResult:
        """Compile LaTeX to PDF"""
        if self.pdf_builder is None:
            self.pdf_builder = PDFBuilder()
        
        import asyncio
        return asyncio.run(
            self.pdf_builder.build(latex_code, output_name)
        )
    
    def create_document(
        self,
        user_input: str,
        content: Dict[str, Any],
        document_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """End-to-end document creation pipeline"""
        result = {
            "success": False,
            "latex_code": None,
            "pdf_bytes": None,
            "pdf_path": None,
            "template": None,
            "error_message": ""
        }
        
        try:
            # 1. Select template
            template = self.select_template(user_input, document_type)
            if not template:
                result["error_message"] = "No suitable template found"
                return result
            
            result["template"] = template.id
            
            # 2. Build document structure
            document = self._build_document_structure(content)
            
            # 3. Generate LaTeX
            latex_code = self.generate_latex(template, document)
            result["latex_code"] = latex_code
            
            # 4. Build PDF
            build_result = self.build_pdf(latex_code, "document")
            
            if build_result.success:
                result["success"] = True
                result["pdf_bytes"] = build_result.pdf_bytes
                result["pdf_path"] = str(build_result.pdf_path) if build_result.pdf_path else None
            else:
                result["error_message"] = build_result.error_message
        
        except Exception as e:
            result["error_message"] = f"Error: {str(e)}"
        
        return result
    
    def _build_document_structure(self, content: Dict) -> DocumentStructure:
        """Build DocumentStructure from content dict"""
        return DocumentStructure(
            title=content.get("title", ""),
            subtitle=content.get("subtitle", ""),
            authors=content.get("authors", []),
            abstract=content.get("abstract", ""),
            keywords=content.get("keywords", []),
            sections=content.get("sections", []),
            bibliography=content.get("bibliography", []),
            acknowledgments=content.get("acknowledgments", ""),
            appendices=content.get("appendices", [])
        )

    # ------------------------------------------------------------------ #
    # Auto-debug loop para archivos .tex existentes                        #
    # ------------------------------------------------------------------ #

    def compile_with_selfheal(
        self,
        tex_path: str,
        compiler: str = "pdflatex",
        use_biber: bool = False,
        max_attempts: int = MAX_DEBUG_ATTEMPTS,
    ) -> Dict[str, Any]:
        """
        Compila un archivo .tex existente con bucle de auto-corrección.

        Flujo por iteración:
          1. pdflatex (nonstopmode)
          2. biber/bibtex si use_biber=True
          3. pdflatex x2 para referencias cruzadas
          4. Parsear log → aplicar fixes si hay errores fatales
          5. Repetir hasta éxito o max_attempts agotados

        Devuelve dict con: success, pdf_path, attempts, fixes_applied,
                           remaining_errors, log_final
        """
        tex_path = Path(tex_path)
        work_dir = tex_path.parent
        stem = tex_path.stem

        result = {
            "success": False,
            "pdf_path": None,
            "attempts": 0,
            "fixes_applied": [],
            "remaining_errors": [],
            "log_final": "",
        }

        for attempt in range(1, max_attempts + 1):
            result["attempts"] = attempt
            print(f"\n{'='*50}")
            print(f"  Intento {attempt}/{max_attempts} — compilando {tex_path.name}")
            print(f"{'='*50}")

            # --- Paso 1: pdflatex ---
            log_text, returncode = self._run_compiler(compiler, tex_path, work_dir)
            result["log_final"] = log_text

            if returncode != 0:
                print(f"  ✗ Error en compilación (código {returncode})")
                # Parsear y aplicar fixes
                debug_result = debug_tex_file(str(tex_path), log_text)
                if debug_result.fixes_applied:
                    result["fixes_applied"].extend(debug_result.fixes_applied)
                    print(f"  → Fixes aplicados: {len(debug_result.fixes_applied)}")
                    for fix in debug_result.fixes_applied:
                        print(f"    • {fix}")
                else:
                    # No hay fixes automáticos — informar y salir
                    debugger = LaTeXDebugger(str(tex_path))
                    errors = debugger.parse_log(log_text)
                    result["remaining_errors"] = [
                        f"[L{e.line_number}] {e.message}" for e in errors
                        if e.error_type == "fatal"
                    ]
                    print("  ✗ No hay correcciones automáticas disponibles.")
                    print(debugger.report_unfixed(errors))
                    break
                continue  # reintentar con el tex corregido

            # --- Paso 2: biber / bibtex ---
            if use_biber:
                print(f"  → Ejecutando biber...")
                self._run_biber(stem, work_dir)

            # --- Paso 3: recompilar 2 veces ---
            for _ in range(2):
                log_text, _ = self._run_compiler(compiler, tex_path, work_dir)

            # --- Comprobar PDF generado ---
            pdf_path = work_dir / f"{stem}.pdf"
            if pdf_path.exists():
                result["success"] = True
                result["pdf_path"] = str(pdf_path)
                print(f"  ✓ PDF generado: {pdf_path}")
                if result["fixes_applied"]:
                    print(f"  ✓ Auto-corregido en {attempt} intento(s).")
                    print(f"  Fixes totales aplicados: {len(result['fixes_applied'])}")
                break
            else:
                print("  ✗ No se generó el PDF tras compilación aparentemente exitosa.")
                break

        return result

    @staticmethod
    def _run_compiler(compiler: str, tex_path: Path, work_dir: Path) -> tuple:
        """Ejecuta el compilador LaTeX y devuelve (log_text, returncode)."""
        cmd = [
            compiler,
            "-interaction=nonstopmode",
            "-file-line-error",
            "-halt-on-error",
            str(tex_path.name),
        ]
        proc = subprocess.run(
            cmd,
            cwd=str(work_dir),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return proc.stdout + proc.stderr, proc.returncode

    @staticmethod
    def _run_biber(stem: str, work_dir: Path) -> None:
        """Ejecuta biber para procesar la bibliografía."""
        subprocess.run(
            ["biber", stem],
            cwd=str(work_dir),
            capture_output=True,
        )


def main():
    """Command-line interface for LaTeX Writer"""
    import argparse

    parser = argparse.ArgumentParser(description="LaTeX Writer - Generate & debug documents")
    parser.add_argument("--template", "-t", help="Template ID")
    parser.add_argument("--output", "-o", default="document.pdf", help="Output PDF path")
    parser.add_argument("--content", "-c", help="Content JSON file")
    # Modo auto-debug: compila un .tex existente con bucle de corrección
    parser.add_argument("--file", "-f", help="Archivo .tex existente a compilar/debugear")
    parser.add_argument("--debug-mode", action="store_true",
                        help="Activar bucle de auto-corrección sobre --file")
    parser.add_argument("--biber", action="store_true",
                        help="Usar biber para la bibliografía (biblatex)")
    parser.add_argument("--compiler", default="pdflatex",
                        help="Compilador LaTeX (pdflatex, xelatex, lualatex)")
    parser.add_argument("--max-attempts", type=int, default=MAX_DEBUG_ATTEMPTS,
                        help=f"Máx. intentos de auto-corrección (defecto: {MAX_DEBUG_ATTEMPTS})")

    args = parser.parse_args()
    writer = LaTeXWriter()

    # --- Modo auto-debug sobre archivo existente ---
    if args.file:
        result = writer.compile_with_selfheal(
            tex_path=args.file,
            compiler=args.compiler,
            use_biber=args.biber,
            max_attempts=args.max_attempts,
        )
        if result["success"]:
            status = f"SUCCESS (en {result['attempts']} intento(s))"
            if result["fixes_applied"]:
                status = f"FIXED({result['attempts']}) — {len(result['fixes_applied'])} correcciones"
            print(f"\n✓ {status}")
            print(f"  PDF: {result['pdf_path']}")
        else:
            print(f"\n✗ FAILED tras {result['attempts']} intento(s)")
            if result["remaining_errors"]:
                print("  Errores sin resolver:")
                for err in result["remaining_errors"]:
                    print(f"    • {err}")
        return

    # --- Modo generación desde plantilla ---
    if args.content:
        with open(args.content, 'r', encoding='utf-8') as f:
            content = json.load(f)

        result = writer.create_document(
            user_input=content.get("description", ""),
            content=content,
            document_type=content.get("type")
        )

        if result["success"]:
            with open(args.output, 'wb') as f:
                f.write(result["pdf_bytes"])
            print(f"✓ PDF generated: {args.output}")
            tex_path = args.output.replace('.pdf', '.tex')
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(result["latex_code"])
            print(f"✓ LaTeX source: {tex_path}")
        else:
            print(f"✗ Error: {result['error_message']}")
    else:
        print("LaTeX Writer - Available templates:")
        for template in writer.template_manager.list_templates():
            print(f"  - {template.id}: {template.name}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
LaTeX Debugger — Auto-fix loop
Parsea errores del log de LaTeX y aplica correcciones automáticas.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple


@dataclass
class LaTeXError:
    """Representa un error o advertencia extraído del log."""
    line_number: Optional[int]
    error_type: str          # 'fatal', 'warning', 'info'
    message: str
    context: str = ""        # líneas de contexto del log
    fixable: bool = False
    fix_applied: str = ""


@dataclass
class DebugResult:
    """Resultado de un ciclo de debug."""
    fixed: bool
    errors_found: List[LaTeXError] = field(default_factory=list)
    fixes_applied: List[str] = field(default_factory=list)
    remaining_errors: List[LaTeXError] = field(default_factory=list)
    iterations: int = 0


class LaTeXDebugger:
    """
    Bucle de auto-corrección para archivos LaTeX.
    Parsea el log, identifica errores conocidos y aplica fixes.
    """

    MAX_ATTEMPTS = 5

    # Patrones de error → (regex_en_log, regex_en_tex, reemplazo, descripción)
    KNOWN_FIXES = [
        # Undefined control sequence — intentar eliminar el comando
        {
            "log_pattern": r"Undefined control sequence\.\s*\nl\.(\d+)\s+(.*)",
            "type": "undefined_command",
            "description": "Comando LaTeX no definido",
        },
        # Missing $ inserted
        {
            "log_pattern": r"Missing \$ inserted",
            "type": "missing_math",
            "description": "Expresión matemática fuera de entorno $...$",
        },
        # Multiply defined label
        {
            "log_pattern": r"Label `(.+)' multiply defined",
            "type": "duplicate_label",
            "description": "Label duplicado",
        },
        # Overfull hbox (advertencia, no error fatal)
        {
            "log_pattern": r"Overfull \\hbox",
            "type": "overfull_hbox",
            "description": "Texto desborda la caja horizontal",
        },
        # Citation undefined
        {
            "log_pattern": r"Citation `(.+)' on page \d+ undefined",
            "type": "undefined_citation",
            "description": "Clave de cita no encontrada en .bib",
        },
        # Package not found
        {
            "log_pattern": r"File `(.+\.sty)' not found",
            "type": "missing_package",
            "description": "Paquete LaTeX no instalado",
        },
    ]

    def __init__(self, tex_path: str):
        self.tex_path = Path(tex_path)
        if not self.tex_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {tex_path}")

    # ------------------------------------------------------------------ #
    # Parseo del log                                                       #
    # ------------------------------------------------------------------ #

    def parse_log(self, log_text: str) -> List[LaTeXError]:
        """Extrae errores y advertencias del log de compilación."""
        errors: List[LaTeXError] = []
        lines = log_text.split("\n")

        i = 0
        while i < len(lines):
            line = lines[i]

            # Error fatal: línea que empieza con "!"
            if line.startswith("!"):
                # La siguiente línea con "l.<n>" indica el número de línea
                line_number = None
                context_lines = [line]
                for j in range(i + 1, min(i + 6, len(lines))):
                    context_lines.append(lines[j])
                    m = re.match(r"^l\.(\d+)", lines[j])
                    if m:
                        line_number = int(m.group(1))
                        break

                error = LaTeXError(
                    line_number=line_number,
                    error_type="fatal",
                    message=line.lstrip("! ").strip(),
                    context="\n".join(context_lines),
                    fixable=self._is_fixable(line),
                )
                errors.append(error)

            # Advertencia LaTeX
            elif "LaTeX Warning:" in line or "Package warning:" in line.lower():
                error = LaTeXError(
                    line_number=None,
                    error_type="warning",
                    message=line.strip(),
                    context=line,
                    fixable=False,
                )
                errors.append(error)

            # Overfull/Underfull
            elif line.startswith("Overfull") or line.startswith("Underfull"):
                error = LaTeXError(
                    line_number=None,
                    error_type="warning",
                    message=line.strip(),
                    context=line,
                    fixable=False,
                )
                errors.append(error)

            i += 1

        return errors

    def _is_fixable(self, error_line: str) -> bool:
        """Determina si el error tiene una corrección automática disponible."""
        fixable_patterns = [
            "Undefined control sequence",
            "Missing \\$ inserted",
            "multiply defined",
            "not found",
            "Overfull \\hbox",
        ]
        return any(p in error_line for p in fixable_patterns)

    # ------------------------------------------------------------------ #
    # Aplicar correcciones al .tex                                         #
    # ------------------------------------------------------------------ #

    def apply_fixes(self, errors: List[LaTeXError]) -> List[str]:
        """
        Aplica correcciones automáticas al archivo .tex.
        Devuelve lista de descripciones de los cambios realizados.
        """
        with open(self.tex_path, "r", encoding="utf-8") as f:
            content = f.read()
        lines = content.split("\n")

        fixes_applied = []

        for error in errors:
            if not error.fixable:
                continue

            original_content = "\n".join(lines)

            # --- Undefined control sequence ---
            if "Undefined control sequence" in error.message:
                # Extraer el nombre del comando del contexto
                m = re.search(r"\\(\w+)", error.context.split("\n")[-1] if "\n" in error.context else error.context)
                if m and error.line_number:
                    bad_cmd = "\\" + m.group(1)
                    ln = error.line_number - 1  # 0-indexed
                    if 0 <= ln < len(lines) and bad_cmd in lines[ln]:
                        # Comentar la línea problemática
                        lines[ln] = "% [AUTO-FIX: undefined cmd] " + lines[ln]
                        fix = f"L{error.line_number}: comentada línea con '{bad_cmd}' indefinido"
                        fixes_applied.append(fix)
                        error.fix_applied = fix

            # --- Missing $ inserted ---
            elif "Missing $" in error.message and error.line_number:
                ln = error.line_number - 1
                if 0 <= ln < len(lines):
                    # Buscar posibles expresiones matemáticas sin $
                    # Patrón: letras seguidas de _ o ^ fuera de math
                    new_line = re.sub(
                        r"(?<!\$)([A-Za-z]+[_^][A-Za-z0-9{}]+)(?!\$)",
                        r"$\1$",
                        lines[ln],
                    )
                    if new_line != lines[ln]:
                        lines[ln] = new_line
                        fix = f"L{error.line_number}: añadidos delimitadores $ para expresión matemática"
                        fixes_applied.append(fix)
                        error.fix_applied = fix

            # --- Label multiply defined ---
            elif "multiply defined" in error.message:
                m = re.search(r"Label `(.+)' multiply defined", error.message)
                if m:
                    label = m.group(1)
                    # Encontrar segunda ocurrencia y añadir sufijo
                    count = 0
                    for idx, ln in enumerate(lines):
                        if f"\\label{{{label}}}" in ln:
                            count += 1
                            if count == 2:
                                lines[idx] = ln.replace(
                                    f"\\label{{{label}}}",
                                    f"\\label{{{label}-b}}"
                                )
                                fix = f"Label duplicado '{label}' renombrado a '{label}-b' en L{idx+1}"
                                fixes_applied.append(fix)
                                error.fix_applied = fix
                                break

            # --- Overfull hbox → añadir \sloppy si no existe ---
            elif "Overfull" in error.message:
                has_sloppy = any("\\sloppy" in ln for ln in lines)
                if not has_sloppy:
                    # Insertar \sloppy justo después de \begin{document}
                    for idx, ln in enumerate(lines):
                        if "\\begin{document}" in ln:
                            lines.insert(idx + 1, "\\sloppy  % AUTO-FIX: reduce overfull hbox")
                            fix = "Añadido \\sloppy tras \\begin{document} para reducir overfull"
                            fixes_applied.append(fix)
                            error.fix_applied = fix
                            break

        new_content = "\n".join(lines)
        if new_content != content:
            with open(self.tex_path, "w", encoding="utf-8") as f:
                f.write(new_content)

        return fixes_applied

    # ------------------------------------------------------------------ #
    # Informe de errores no corregibles                                    #
    # ------------------------------------------------------------------ #

    def report_unfixed(self, errors: List[LaTeXError]) -> str:
        """Genera un informe legible de errores que no se pudieron corregir."""
        fatal = [e for e in errors if e.error_type == "fatal" and not e.fix_applied]
        warnings = [e for e in errors if e.error_type == "warning"]

        report = []
        if fatal:
            report.append("=== ERRORES FATALES SIN CORREGIR ===")
            for e in fatal:
                loc = f"L{e.line_number}" if e.line_number else "?"
                report.append(f"  [{loc}] {e.message}")
                if e.context:
                    report.append(f"       Contexto: {e.context[:120]}")

        if warnings:
            report.append(f"\n=== ADVERTENCIAS ({len(warnings)}) ===")
            for w in warnings[:5]:  # mostrar máximo 5
                report.append(f"  {w.message[:100]}")

        return "\n".join(report) if report else "Sin errores pendientes."


# ------------------------------------------------------------------ #
# Función de conveniencia para llamar desde latex_writer.py           #
# ------------------------------------------------------------------ #

def debug_tex_file(tex_path: str, log_text: str) -> DebugResult:
    """
    Parsea el log y aplica correcciones al archivo .tex.
    Devuelve un DebugResult con el resumen.
    """
    debugger = LaTeXDebugger(tex_path)
    errors = debugger.parse_log(log_text)
    fatal_errors = [e for e in errors if e.error_type == "fatal"]

    if not fatal_errors:
        return DebugResult(fixed=True, errors_found=errors)

    fixes = debugger.apply_fixes(fatal_errors)
    remaining = [e for e in fatal_errors if not e.fix_applied]

    return DebugResult(
        fixed=len(remaining) == 0,
        errors_found=errors,
        fixes_applied=fixes,
        remaining_errors=remaining,
    )

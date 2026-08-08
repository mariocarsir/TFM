---
type: concept
title: "claude-obsidian (plugin)"
created: 2026-08-06
updated: 2026-08-06
status: developing
tags:
  - concept
  - claude-obsidian
domain: "Claude Code plugins"
complexity: intermediate
related:
  - "[[claude-obsidian-wiki]]"
  - "[[claude-obsidian-wiki-ingest]]"
  - "[[claude-obsidian-wiki-query]]"
  - "[[claude-obsidian-wiki-retrieve]]"
  - "[[claude-obsidian-wiki-lint]]"
  - "[[claude-obsidian-wiki-fold]]"
  - "[[claude-obsidian-wiki-cli]]"
  - "[[claude-obsidian-wiki-mode]]"
  - "[[claude-obsidian-save]]"
  - "[[claude-obsidian-autoresearch]]"
  - "[[claude-obsidian-canvas]]"
  - "[[claude-obsidian-defuddle]]"
  - "[[claude-obsidian-obsidian-bases]]"
  - "[[claude-obsidian-obsidian-markdown]]"
  - "[[claude-obsidian-think]]"
---

# claude-obsidian

Plugin de Claude Code (`AgriciDaniel/claude-obsidian`, v2.1.0) que convierte un vault de Obsidian en una base de conocimiento local-first con procedencia trazable. Mantiene ledgers de fuentes y afirmaciones, y fuerza un flujo de transacción (`preview → aprobación sha256 → apply`) para toda escritura en el vault, evitando mutaciones silenciosas.

Diseñado para no inyectar contexto automáticamente: `save` guarda solo bajo petición explícita, nunca como transcripción automática de la sesión.

**Instalación:** `C:\Users\Usuario\.claude\plugins\marketplaces\AgriciDaniel-claude-obsidian`
**Skills (caché versionado):** `C:\Users\Usuario\.claude\plugins\cache\agricidaniel-claude-obsidian\claude-obsidian\2.1.0\skills\`
**Requisito:** WSL en Windows para cualquier escritura en el vault (descriptores de directorio POSIX).

## Skills incluidas

- [[claude-obsidian-wiki]] — orquestador: inicializa/adopta el vault y enruta al resto de skills.
- [[claude-obsidian-wiki-ingest]] — ingesta fuentes (archivos, texto, URLs) con procedencia.
- [[claude-obsidian-wiki-query]] — consulta el vault existente, solo lectura.
- [[claude-obsidian-wiki-retrieve]] — índice de recuperación BM25 + reranking opcional.
- [[claude-obsidian-wiki-lint]] — auditoría de salud del vault, solo lectura.
- [[claude-obsidian-wiki-fold]] — resume (rollup) entradas del log sin tocar páginas hijas.
- [[claude-obsidian-wiki-cli]] — transporte de lectura vía el CLI oficial de Obsidian.
- [[claude-obsidian-wiki-mode]] — sugiere rutas de archivado según metodología (PARA, LYT, Zettelkasten...).
- [[claude-obsidian-save]] — guarda una decisión/resultado de sesión de forma explícita.
- [[claude-obsidian-autoresearch]] — investigación web acotada y citada.
- [[claude-obsidian-canvas]] — crea/edita tableros Obsidian Canvas.
- [[claude-obsidian-defuddle]] — limpia páginas web a Markdown legible.
- [[claude-obsidian-obsidian-bases]] — diseña ficheros `.base` (vistas tipo base de datos).
- [[claude-obsidian-obsidian-markdown]] — referencia de sintaxis Obsidian Flavored Markdown.
- [[claude-obsidian-think]] — razonamiento profundo de 10 etapas para decisiones complejas.

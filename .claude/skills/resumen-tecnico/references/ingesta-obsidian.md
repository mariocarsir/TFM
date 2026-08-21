# Referencia: indexar un resumen en el vault de Obsidian (`claude-obsidian`)

Procedimiento verificado y repetible para llevar un `.md` ya generado por esta skill al
vault de `claude-obsidian`. Sin esta referencia el patrón se re-deduce desde cero en cada
invocación (~30-45k tokens perdidos por ingesta).

> **Esta skill NO ingesta por su cuenta.** La ingesta ocurre solo cuando Mario la pide
> explícitamente ("indexa esto en Obsidian"), en cumplimiento de la regla 4 de `SKILL.md`
> y del requisito de mecanismos *pull*, nunca *push*. Este fichero documenta el CÓMO para
> cuando llegue esa petición, no un automatismo.

## 0. Requisitos no negociables

- **La escritura al vault solo funciona desde WSL.** En Windows nativo o Git Bash toda
  mutación (`transaction apply`, `capture apply`, `init`, `adopt`, `migrate`) falla con
  `UNSUPPORTED_PLATFORM`. Es una restricción de diseño del plugin, no una recomendación.
- Desde una sesión Windows se invoca WSL así:

  ```bash
  wsl.exe -e bash -lc '<comando>'
  ```

- El script vive **en el lado Windows**, montado en WSL (no está instalado en el home de WSL):

  ```
  /mnt/c/Users/Usuario/.claude/plugins/cache/agricidaniel-claude-obsidian/claude-obsidian/2.1.0/scripts/claude-obsidian.py
  ```

- El vault es la propia carpeta del TFM:

  ```
  /mnt/c/Users/Usuario/OneDrive - Universidad Politécnica de Madrid/Escritorio/Claudio/TFM
  ```

- **Nunca escribir en `wiki/` con `Write`/`Edit` ni redirigiendo la salida de la shell.**
  Toda mutación pasa por el flujo transaccional; saltárselo desincroniza los ledgers y rompe
  la trazabilidad.

## 1. Flujo completo

```
borradores en el directorio temporal del job
        ↓
bundle JSON (claude-obsidian.transaction.v1)
        ↓
transaction inspect  → devuelve approval_sha256
        ↓
transaction apply --approved-plan-sha256 <hash>
        ↓
lint (verificación)
        ↓
commit en git
```

Los comandos concretos:

```bash
wsl.exe -e bash -lc "python3 '<SCRIPT>' transaction inspect '<BUNDLE>' --vault '<VAULT>'"
wsl.exe -e bash -lc "python3 '<SCRIPT>' transaction apply '<BUNDLE>' --vault '<VAULT>' --approved-plan-sha256 '<HASH>'"
```

## 2. Qué ficheros toca SIEMPRE una ingesta

Una ingesta completa son **7 escrituras**. Omitir cualquiera deja el vault incoherente:

| Fichero | Modo | Qué se hace |
| --- | --- | --- |
| `wiki/sources/<slug-fuente>.md` | `create` | Página fuente nueva |
| `wiki/meta/ledgers/source-ledger.json` | `replace` | Añadir la entrada de la fuente |
| `wiki/meta/ledgers/claim-ledger.json` | `replace` | Añadir las afirmaciones extraídas |
| `wiki/index.md` | `replace` | Añadir la línea en la sección Sources |
| `wiki/log.md` | `replace` | Entrada de bitácora de la ingesta |
| `wiki/hot.md` | `replace` | Cachear las cifras más consultables |
| `wiki/concepts/<nodo-tematico>.md` | `replace` | Enlazar la fuente desde el nodo que la agrupa |

Los ledgers **se reescriben enteros** (no hay parcheo incremental): hay que leerlos, añadir
lo nuevo y volcar el JSON completo.

## 3. El `source_id` NUNCA se inventa a mano

Es determinista. Se calcula invocando la función real del plugin, `stable_source_id` del
módulo `claude_obsidian.ledgers`, con tres argumentos: el `kind` del origen (`file`), el
`locator` (ruta relativa del resumen) y el `content_sha256` del resumen.

Devuelve `src-` seguido de los primeros 20 caracteres hexadecimales del sha256 de esa terna
unida por bytes nulos. Un ID inventado a mano rompe la unión entre el ledger y la página.

El `sha256` del contenido se obtiene con `sha256sum <fichero>`.

## 4. Esquema del bundle

```json
{
  "schema": "claude-obsidian.transaction.v1",
  "operation_id": "ingest-AAAAMMDD-<slug>",
  "operation_type": "ingest",
  "expected_hashes": {
    "wiki/sources/<nuevo>.md": null,
    "wiki/index.md": "<sha256 ACTUAL del fichero antes de tocarlo>"
  },
  "writes": [
    {
      "path": "wiki/sources/<nuevo>.md",
      "mode": "create",
      "content_file": "/mnt/c/.../tmp/<borrador>.md",
      "sha256": "<sha256 del borrador>"
    }
  ],
  "address_requests": [],
  "source_manifest_updates": {}
}
```

Detalles que cuestan tiempo si se olvidan:

- `mode` solo admite `"create"` y `"replace"`. **No existe `"update"`.**
- `expected_hashes` es `null` para ficheros nuevos, y el sha256 **actual** para los que se
  reemplazan. Si no coincide, el apply aborta: es la protección contra escrituras concurrentes.
- `content_file` debe ser una ruta **vista desde WSL** (`/mnt/c/...`).
- Existe la alternativa `content` (cadena en línea, sin `sha256` declarado), pero para
  contenido largo o con tildes es más frágil: usar siempre `content_file`.
- `operation_type: "ingest"` es lo que autoriza a tocar `wiki/sources/` y los ledgers. Para
  notas conceptuales sin fuente nueva, el tipo correcto es `"markdown"`.

## 5. Entrada del `source-ledger.json`

La clave `sources` es una **lista**. Cada entrada:

```json
{
  "origin": { "kind": "file", "locator": "conocimiento fotovoltaico/Referencia/<resumen>.md" },
  "content_kind": "document",
  "title": "<título largo, con autor y año>",
  "authority": "community",
  "content_sha256": "<sha256 del resumen>",
  "ingested_at": null,
  "retrieved_at": "AAAA-MM-DD",
  "refresh_due": "AAAA-MM-DD (un año después)",
  "review_status": "active",
  "independence_key": "<clave que agrupa fuentes no independientes entre sí>",
  "pages": ["wiki/sources/<slug>.md"],
  "supersedes": null
}
```

Ojo: el `source_id` **no** aparece en la entrada del ledger. Vive en el frontmatter de la
página fuente y en el campo `evidence[].source_id` de cada afirmación.

## 6. Entrada del `claim-ledger.json`

La clave `claims` es un **diccionario** indexado por `claim_id` (formato `clm-<autor><año>-<tema>`):

```json
"clm-barrios2023-presupuesto-tramitacion": {
  "text": "<la afirmación, con sus cifras>",
  "risk": "normal",
  "assessment": "accepted",
  "confidence": "high",
  "location": { "path": "wiki/sources/<slug>.md", "anchor": null },
  "reviewed_at": "AAAA-MM-DD",
  "notes": "NO CITABLE. <para qué sirve y para qué no>",
  "supersedes": null,
  "evidence": [
    { "source_id": "src-...", "relation": "supports", "locator": "p.63-64" }
  ]
}
```

## 7. Enums permitidos (inventarse uno hace fallar el apply)

| Campo | Valores |
| --- | --- |
| `review_status` / `review_state` | `unreviewed`, `active`, `superseded`, `rejected` |
| `risk` | `normal`, `high` |
| `authority` | `primary`, `secondary`, `community` |
| `mode` (en `writes`) | `create`, `replace` |

**No existe ningún enum para "no citable".** La no-citabilidad de los TFM de referencia se
expresa con tres cosas a la vez: `authority: community` + `citable: false` en el frontmatter,
el `notes` de cada afirmación empezando por `"NO CITABLE."`, y un aviso visible en el cuerpo
de la página fuente.

## 8. Wikilinks

Se resuelven por **nombre de fichero en kebab-case ASCII**, no por el `title` del frontmatter.
Se escribe `[[resumenes]]`, nunca `[[Resúmenes]]`. Para mostrar un texto distinto:
`[[slug-real|Texto visible]]`.

## 9. Verificación posterior

Pasar el linter del plugin sobre el vault al terminar.

**Ruido conocido:** el linter recorre también los directorios `.claude/worktrees/*`, que
pueden contener copias residuales del vault de otros jobs. Eso genera cientos de hallazgos
falsos. Antes de alarmarse, filtrar por ruta: solo cuentan los hallazgos cuya ruta empieza
directamente por `wiki/`. Lo que debe salir a cero es `dead_links`, `missing_frontmatter` y
`provenance_errors` **dentro de `wiki/`**.

## 10. Cierre

Commitear el resultado (regla 9 de `CLAUDE.md`), **nunca con `git add -A`**: hay otros jobs
trabajando en paralelo sobre el mismo repositorio y sus cambios sin commitear no deben
colarse. Añadir solo las rutas de la ingesta, una a una.

El `.obsidian/graph.json` lo regenera la herramienta automáticamente en cada apply: entra en
el commit, no es un cambio espurio.

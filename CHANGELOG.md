# Changelog

Todas las versiones siguen [SemVer].

## [v1.0.0] - 2025-10-19
### 🆕 Añadido
- **charset_mutator.py**: generador ofensivo de variantes de payloads aplicando **charsets reales** (no transformacionales).
- Modos de mutación: `special_only` (solo especiales críticos) y `full_payload` (todo el payload).
- **100 charsets** de texto + **24 BYTE_CHANGERS** reales (UTF-16/32, UTF-7, EBCDIC…).
- **Compatibilidad automática**: salta charsets que no representen el payload (modo estricto).
- CLI completa con flags: `--payload`, `--input-file`, `--modes`, `--charsets`, `--skip-broken`, `--include-broken`, `--base-charset`, `--report-unsupported`, `--output-dir`.

### ✨ Cambiado
- N/A (versión inicial).

### 🐞 Corregido
- N/A (versión inicial).

### 🧭 Notas
- Objetivo: **cambiar los bytes sin romper la ejecución**, descubriendo bypass binarios contra firmas ASCII de WAF/filtros.
- Formato del proyecto: interfaz web local (HTML/JS) para demo + script `charset_mutator.py`.

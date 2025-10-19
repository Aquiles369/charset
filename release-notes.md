# Release Notes — v1.0.0 (2025-10-19)

## 📦 Resumen
**Charset** introduce `charset_mutator.py`, una herramienta que genera variantes de payloads web usando **charsets reales**, modificando la representación **byte a byte** sin alterar la ejecución. Ideal para laboratorios de **XSS/RCE/inyecciones** y para estudiar **bypasses binarios** contra WAF/parsers.

---

## 🧪 Problema que resuelve
La mayoría de “mutadores” solo usan entidades/URL-encode —no cambian el binario real—. Eso deja vivas las firmas ASCII y muchas heurísticas simples. Este mutador **aplica charsets de verdad** (UTF-16/32, UTF-7, EBCDIC…), generando **bytes diferentes** para los mismos caracteres críticos.

---

## ⚙️ Qué aporta
- 🔬 **Visibilidad de bytes**: cómo `< > ' " …` cambian por charset.
- 🛡️ **Bypass reales**: rompe firmas estáticas y parsers frágiles.
- ⚙️ **Automatización**: miles de variantes válidas sin esfuerzo.
- 🧯 **Modo estricto**: salta charsets no soportados → solo líneas útiles.

---

## 🧰 Características clave
- **2 modos**:  
  - `special_only`: muta solo especiales críticos.  
  - `full_payload`: aplica el charset a todo el payload.
- **Catálogo integrado**: ~100 charsets + **24 BYTE_CHANGERS** (UTF-16/32, UTF-7, EBCDIC cp037, cp500, cp1140…).
- **Compatibilidad automática**: si un charset no puede representar un carácter crítico → **se omite**.
- **CLI completa** con flags (ver más abajo).

---

## ▶️ Uso rápido

### Payload único
```bash
python charset_mutator.py --payload "<body onafterprint=alert(1)>" \
  --modes special_only \
  --charsets utf_16 utf_16_be utf_16_le utf_32 utf_32_be utf_32_le utf_7 cp037 cp500

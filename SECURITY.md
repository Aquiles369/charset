# Política de seguridad

## 🎯 Alcance
Este proyecto y `charset_mutator.py` están pensados **exclusivamente** para:
- Laboratorios controlados.
- Programas de **bug bounty** o VDP con autorización explícita.
- Investigación educativa sobre **bypass binario** y evasión de WAFs mediante charsets reales.

⚠️ **No constituye invitación a probar en sistemas sin permiso.**

---

## ✅ Buenas prácticas
- 📜 **Respeto del alcance**: siempre verificá las políticas del programa antes de usar las variantes generadas.  
- 🧪 **No ejecutes en producción sin permiso**: limita las pruebas a entornos de laboratorio o sandbox oficiales.  
- 🗂️ **Registro detallado**: documentá cada payload, charset aplicado y resultado obtenido.  
- 🔒 **Privacidad ante todo**: nunca publiques información sensible de terceros.

---

## ⚠️ Riesgos y consideraciones
- Algunos charsets (como UTF-16/32 BE/LE, UTF-7 o EBCDIC) pueden **alterar cabeceras, longitudes o rutas de parseo**, lo que puede provocar comportamientos inesperados.  
- Los BYTE_CHANGERS pueden **romper parsers intermedios**; por defecto usá `--skip-broken` para evitarlos.  
- Evitá mezclar estos charsets con codificaciones transformacionales (base64, hex…) si querés analizar solo el efecto del charset en los bytes.

---

## 📬 Reporte de vulnerabilidades en este repositorio
Si encontrás un problema de seguridad **en esta herramienta** (no en sistemas de terceros):

1. Abrí un *issue* sin incluir datos sensibles.  
2. Si el fallo es crítico, solicitá un canal privado para compartir detalles.  
3. No subas PoCs que apunten a dominios reales.

---

## 🧾 Descargo de responsabilidad
El uso de esta herramienta es **responsabilidad del usuario**. Está destinada a **uso ético y autorizado únicamente**.  
Siempre asegurate de contar con **permiso previo y explícito** antes de realizar cualquier prueba.

💡 **Regla de oro:** *Primero el permiso, después los bytes.*

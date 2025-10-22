<h1 align="center"><img height="40" src="https://github.com/Aquiles369/iconos/blob/main/img/lobo1.gif"><img height="40" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWx4YTl1dW9scXlqZDk2cTdyY2VvcXQwMG40OGoxY25rZzV0MDZhcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/peSyJWjNTRfzaWh49M/giphy.gif">"Charset"<img height="40" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWx4YTl1dW9scXlqZDk2cTdyY2VvcXQwMG40OGoxY25rZzV0MDZhcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/peSyJWjNTRfzaWh49M/giphy.gif"><img height="35" src="https://github.com/Aquiles369/iconos/blob/main/img/lobo1.gif"> </h1>	


<br>


<p align="center">
 <img  height="470rem" alt="GIF" src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmQ3bnlwbmY2ZnltajJhbHJwYnhuajFkMmV6bWw4MXlrMDI5cHU4cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/GltC4HZLjJLvq/giphy.gif"/>
</p>

<picture> <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">  </picture>


### <picture> <img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3ZkZmYxMG1uZWdpOWdyd2RnbmZxeW12YTNlbHRhZTFlMWdiZmFiNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/N1n2Z59pZCslW/giphy.gif" width = 75px>  </picture> Charset

<br>

 **charset_mutadorr.py es una herramienta ofensiva diseñada para generar variantes de payloads web aplicando charsets reales (no transformacionales), cambiando su representación binaria sin alterar su ejecución. Permite descubrir bypass efectivos contra WAFs y filtros que dependen de firmas ASCII, analizar cómo cada charset representa caracteres especiales y automatizar pruebas avanzadas de evasión, <a href="https://youtu.be/Rx-z-gV6roI" target="_blank" rel="noopener">demo de la tool Youtube</a>.** 
<br><br> 

<p align="center">
 <img  height="420rem" alt="GIF" src="https://github.com/Aquiles369/iconos/blob/main/demo_charset_100.gif"/>
</p>

<br>
<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXk0OXNnNHk0cDV3aWdwMTh2a3pwbmg3b3lha3dubzc5dmdlb3M5ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/11QU48jrASWMsE/giphy.gif" width = 75px>  </picture> Problema que resuelve<br><br>
**En bypass de WAF, evasión de filtros y pruebas de payloads, la mayoría de scripts solo generan variantes superficiales (entidades, URL encoding, etc.) sin cambiar el binario real. Esta herramienta resuelve ese problema al aplicar charsets reales a los payloads, cambiando su representación byte a byte sin alterar su ejecución, permitiendo descubrir variantes que rompen firmas estáticas, heurísticas simples o parsers frágiles.** 

<br>

### <picture> <img src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3VtZHVwd2V3dWV1OWtkYTR4dmhuZXV3cHd1NzJmcGsxaGV4YnZ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/HHwI031emo0GQ/giphy.gif" width = 75px>  </picture> Qué aporta y cómo beneficia <br><br>
**• Permite detectar cómo cambian los bytes de caracteres especiales (<, >, ', ", etc.) al usar distintos charsets.<br><br>
  • Ayuda a descubrir bypass reales contra WAFs que se basan en firmas ASCII.<br><br>
  • Expone variantes funcionales con codificaciones que alteran el binario (UTF-16, UTF-32, UTF-7, EBCDIC), algo que muchas herramientas no hacen.<br><br>
  • Acelera laboratorios de XSS, RCE o inyecciones al automatizar la mutación por charset.** 

<br>


<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxiOWdscHZ3endqOWM0ZjJ0YTFsdHJwcnZsZXBmZGc3ZWs0ZGZ5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/nrY3TgN3JNbUs/giphy.gif" width = 80px>  </picture> Resumen rápido
<br><br>

charset_mutadorr.py genera variantes de payloads web codificadas con distintos charsets reales (no transformacionales), tanto completas como solo en sus caracteres especiales. Esto permite probar bypass binarios contra WAFs y filtros, detectar inconsistencias de parsing y entender cómo cambian los bytes críticos según el juego de caracteres.<br>


• Formato: interfaz web local (HTML/JS), toda la data se guarda en localStorage por defecto (offline, en tu máquina).<br><br>

• Pasos a seguir:<br>
1. Descarga el repositorio.<br>
2. Abra el archivo Estados_servidor.html en con su navegador preferido.<br>
3. Introduzca el código de estado (ej.: 429) o presione Ctrl + F y busque "429".<br>

<br>

<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXA0bTNlbWYxZGRvcGpqanA3anlqYmdkeWhoaGdwazlpM3VzZzdybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/RlAfYHeJFLO78ChAee/giphy.gif" width = 80px>  </picture> Características
<br><br>

## 2 modos de mutación:<br>

• special_only: solo muta caracteres especiales críticos.

• full_payload: codifica todo el payload.

• 100 charsets de texto disponibles automáticamente.

• 24 BYTE_CHANGERS reales (UTF-16/32, UTF-7, EBCDIC…) que modifican bytes críticos.

• Compatibilidad realista: excluye codecs transformacionales (base64, hex, etc.).

• Modo estricto: solo genera variantes válidas; si un charset no puede representar el payload, se omite.


<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2Fka2xkY2VybmR4YWppNGc0czNsZzdnOXMxa2pjNnRlMThsbWFlNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/dTWgGXLigmTl2f8Dm3/giphy.gif" width = 80px>  </picture> Uso
<br><br>

Payload único:<br>

```yaml
python charset_mutadorr.py --payload "<body onafterprint=alert(1)>" --modes special_only --charsets utf_16 utf_16_be utf_16_le utf_32 utf_32_be utf_32_le utf_7 cp037 cp500


```
<br>

## Archivo con varios payloads:

```yaml
python charset_mutadorr.py --input-file payloads.txt --modes special_only full_payload


```
<br>

## Comando solo charset que cambie el binario del paylodad:

```yaml

python charset_mutadorr.py --payload '<body onafterprint=alert(1)>'  --modes special_only  --charsets utf_16 utf_16_le utf_16_be utf_32 utf_32_le utf_32_be utf_7  cp037 cp273 cp424 cp500 cp875 cp1026  cp1140 cp1141 cp1142 cp1143 cp1144 cp1145 cp1146 cp1147 cp1148 cp1149
```

 <br>

 ## Compatibilidad automática:

- Si un charset no puede representar alguno de los caracteres especiales del payload →  se salta automáticamente.<br><br>

-Si el payload solo contiene SPECIALS soportados por ese charset →  la variante se genera.<br><br>
 Esto garantiza que cada línea del output sea válida en la práctica real, sin bytes falsos ni reemplazos artificiales.<br>


<br><br>

###  Flags disponibles

>  Usa estas opciones con `charset_mutadorr.py` para personalizar cómo se generan las variantes:

| Flag | Descripción |
|------|-------------|
| `--payload "<PAYLOAD>"` | Payload único a mutar |
| `--input-file payloads.txt` | Archivo con lista de payloads |
| `--modes special_only full_payload` | Modos de mutación (`special_only` / `full_payload`) |
| `--output-dir out` | Directorio de salida (por defecto: `out`) |
| `--skip-broken` | Saltar charsets que no soportan los caracteres (default) |
| `--include-broken` | Incluir variantes rotas (rellenando con vacío) |
| `--base-charset utf-8` | Charset base para caracteres no especiales |
| `--charsets utf_16 utf_32 ...` | Lista personalizada de charsets |
| `--report-unsupported` | Solo imprime qué caracteres son soportados por cada charset y termina |

<br>


Flag	Descripción
CWE-79	XSS / DOM XSS por neutralización insuficiente de input/output. Evitar innerHTML/document.write; validar y encodar salida. URL: https://cwe.mitre.org/data/definitions/79.html

CWE-116	Escape/encoding inadecuado (apoya mitigación de XSS). Aplicar encoding contextual en servidor/cliente. URL: https://cwe.mitre.org/data/definitions/116.html

CWE-95	Eval injection — uso de eval/new Function con datos no confiables → ejecución de código. Eliminar evaluadores dinámicos. URL: https://cwe.mitre.org/data/definitions/95.html

CWE-94	Code injection por generación dinámica de código a partir de entrada no controlada. Validar y sanear fuertemente. URL: https://cwe.mitre.org/data/definitions/94.html

CWE-829	Inclusión de funcionalidad desde fuentes no confiables (scripts/CDN comprometidos). Usar SRI, CSP y auditar dependencias. URL: https://cwe.mitre.org/data/definitions/829.html

CWE-798	Credenciales hardcodeadas en JS/frontend. No poner secretos en cliente; usar vault/servidor. URL: https://cwe.mitre.org/data/definitions/798.html

CWE-312 / CWE-200 / CWE-215	Exposición de información sensible (localStorage, logs, comentarios, respuestas). Evitar almacenar/mostrar secretos. URL: https://cwe.mitre.org/

CWE-1336	Template Injection en engines cliente (plantillas que permiten ejecución). No evaluar plantillas con input arbitrario; usar escapes del motor. URL: https://cwe.mitre.org/

CWE-1321	Prototype Pollution en objetos JS (modificación de __proto__ u operaciones merge inseguras). Validar keys, evitar merges inseguros. Referencia técnica: Mend.io y CWE. URL: https://cwe.mitre.org/data/definitions/1321.html

CVE-2020-11022	jQuery — XSS vía ciertos métodos DOM (ejemplo de patrón a cazar). Actualizar jQuery a versiones parcheadas. URL: https://nvd.nist.gov/vuln/detail/CVE-2020-11022

CVE-2020-11023	jQuery — XSS relacionado con <option> al insertar HTML. Parchear y sanitizar. URL: https://nvd.nist.gov/vuln/detail/CVE-2020-11023

CVE-2021-23337	lodash _.template — inyección/ejecución si se usan plantillas con input no controlado. Actualizar lodash. URL: https://nvd.nist.gov/vuln/detail/CVE-2021-23337

CAPEC-63	Cross-Site Scripting — patrón general (incluye DOM XSS). Identificar sinks y aplicar sanitización/encoding. URL: https://capec.mitre.org/data/definitions/63.html

CAPEC-242	Code Injection — vectores eval/Function/plantillas que generan código. Eliminar evaluadores dinámicos. URL: https://capec.mitre.org/data/definitions/242.html

CAPEC-591 / CAPEC-592	Reflected / Stored XSS — clasificación práctica para reportes y priorización. URL: https://capec.mitre.org/

RFC 9110	HTTP Semantics — cabeceras y comportamientos HTTP que afectan parseo, caché y seguridad de recursos usados por JS. Revisar Content-Type, Cache-Control, Vary. URL: https://www.rfc-editor.org/rfc/rfc9110.html

RFC 6454	Web Origin Concept — base de SOP; clave para postMessage, CORS y separación de orígenes en JS. URL: https://www.rfc-editor.org/rfc/rfc6454.html

RFC 6265 / 6265bis	Cookies — atributos HttpOnly, Secure, SameSite para proteger sesiones frente a JS/CSRF. URL: https://www.rfc-editor.org/rfc/rfc6265.html
 / https://httpwg.org/http-extensions/draft-ietf-httpbis-rfc6265bis.html

RFC 3986	URI Syntax — normalización/validación de URIs; importante al construir URLs en JS y discovery de endpoints. URL: https://www.rfc-editor.org/rfc/rfc3986.html

RFC 6455	WebSocket — handshake / Origin header; revisar usos WS desde código cliente. URL: https://www.rfc-editor.org/rfc/rfc6455.html

OWASP Top 10 (2021)	A03 Injection (XSS mapeado aquí). Usar Top10 como checklist de riesgos prioritarios. URL: https://owasp.org/Top10/

NIST SP 800-218 (SSDF)	Secure Software Development Framework — integrar prácticas de ciclo de vida: SCA, SAST, evitar eval, revisar dependencias JS. URL: https://csrc.nist.gov/pubs/sp/800/218/final

NIST SP 800-53 Rev.5	Controles aplicables (ej. SI-10 Input Validation) útiles para mapear requisitos de validación y mitigación. URL: https://csrc.nist.gov/pubs/sp/800/53/r5/final

ASVS v4 / v5 — V5	Validation, Sanitization & Encoding — encode salida y validar entradas usadas por JS/DOM. URL: https://owasp.org/www-project-application-security-verification-standard/

ASVS v4 / v5 — V10	Malicious Code — prohibir eval, Function, setTimeout(string) y libs no confiables. URL: https://owasp.org/www-project-application-security-verification-standard/

ASVS v4 / v5 — V14	Config — CSP estricta y SRI (Subresource Integrity) para <script> externos. URL: https://owasp.org/www-project-application-security-verification-standard/

MITRE ATT&CK — T1190	Exploit Public-Facing Application — si el JS vulnerable está expuesto públicamente puede ser vector de acceso inicial. URL: https://attack.mitre.org/techniques/T1190/

MITRE ATT&CK — T1552	Unsecured Credentials — credenciales expuestas en JS → exfiltración/uso. Escaneo de secretos y rotación. URL: https://attack.mitre.org/techniques/T1552/

MITRE ATT&CK — T1027	Obfuscated Files & Info — ofuscación/packing de JS (mal uso o supply-chain). Analizar ofuscación y comprobar integridad. URL: https://attack.mitre.org/techniques/T1027/

MITRE ATT&CK — T1195	Supply Chain Compromise — dependencias NPM/CDN comprometidas inyectan código en bundles finales. Auditar dependencias/pinear versiones. URL: https://attack.mitre.org/techniques/T1195/

 

<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3YwbG9zbmU1amprdTJsbmxzYnpobzd5eGtnazB6b2FmdnllaTRhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/h8UlsEpqiCISTKUzvz/giphy.gif" width = 80px>  </picture> “Cambia los bytes, no el payload — porque el WAF no puede bloquear lo que ya no reconoce.”
<br>


<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>

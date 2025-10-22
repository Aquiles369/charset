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

 

<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>
<br>

### <picture> <img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3YwbG9zbmU1amprdTJsbmxzYnpobzd5eGtnazB6b2FmdnllaTRhZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/h8UlsEpqiCISTKUzvz/giphy.gif" width = 80px>  </picture> “Cambia los bytes, no el payload — porque el WAF no puede bloquear lo que ya no reconoce.”
<br>


<picture> <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width ="1050" > </picture>

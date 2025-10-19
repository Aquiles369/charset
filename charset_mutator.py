#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
charset_mutator.py
------------------
Genera variantes de payloads aplicando *charsets reales* (Python codecs).
Soporta dos modos:
  - special_only: aplica el charset SOLO a caracteres especiales (mezcla bytes).
  - full_payload: aplica el charset a TODO el payload (bytes homogéneos por línea).
Guarda los resultados en archivos .txt (modo binario), con *una variante por línea*,
sin comentarios ni metadatos, tal como se pidió.

Uso rápido:
  python charset_mutator.py --payload "<img src=x onerror=alert(1)>" --modes special_only full_payload
  python charset_mutator.py --input-file payloads.txt --modes special_only --skip-broken

Notas:
  - Se saltean charsets que no pueden representar los caracteres necesarios si --skip-broken está activo (default).
  - Salida en binario (abre los .txt con editores que muestren bytes crudos si ves símbolos raros).
"""

import os
import argparse
import codecs
from encodings.aliases import aliases as _aliases
from typing import List, Iterable

# === Mejora 1: SPECIALS como set robusto (incluye '-' y espacio; backslash real) ===
SPECIALS_SET = set("<>/=\\'\"+(){}[].,;:%#&?`~^|_- ")

def all_codecs() -> List[str]:
    """
    Unir alias → canonicals y filtrar codecs que NO son charsets de texto.
    === Mejora 2: incluir utf_7 y excluir transformacionales (base64, hex, zlib, quopri, uu, rot_13, idna, punycode) ===
    """
    bad = {
        'base64_codec', 'bz2_codec', 'hex_codec', 'zlib_codec', 'quopri_codec', 'uu_codec', 'rot_13',
        'idna', 'punycode'
    }
    base = set(name.lower().replace('-', '_') for name in _aliases.values())
    base.update({
        'utf_8', 'utf_8_sig', 'latin_1', 'iso8859_1', 'cp1252', 'ascii',
        'utf_16', 'utf_16_be', 'utf_16_le', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_7'
    })
    return sorted(c for c in base if isinstance(c, str) and c.strip() and c not in bad)

def read_payloads(input_file: str=None, payload: str=None) -> List[str]:
    if payload and input_file:
        raise ValueError("Usa --payload o --input-file, no ambos.")
    if not payload and not input_file:
        raise ValueError("Debes proporcionar --payload o --input-file.")
    if payload:
        return [payload]
    # archivo: una por línea (se ignoran líneas vacías)
    out = []
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            s = line.rstrip('\n\r')
            if s.strip():
                out.append(s)
    if not out:
        raise ValueError("El archivo de entrada no contiene payloads válidos.")
    return out

def encode_special_only(s: str, target_charset: str, base_charset: str='utf-8') -> bytes:
    """
    Convierte SOLO caracteres SPECIALS al target_charset.
    El resto se codifica en base_charset (por defecto UTF-8).
    Produce una mezcla de bytes (intencional para laboratorio).
    """
    out_bytes = bytearray()
    for ch in s:
        try:
            if ch in SPECIALS_SET:
                out_bytes += ch.encode(target_charset, errors='strict')
            else:
                out_bytes += ch.encode(base_charset, errors='strict')
        except Exception as e:
            # re-lanza para ser contado como "skipped" según flags
            raise
    return bytes(out_bytes)

def encode_full_payload(s: str, target_charset: str) -> bytes:
    return s.encode(target_charset, errors='strict')

def main():
    parser = argparse.ArgumentParser(description="Mutador de payloads por charset (especiales y completo).")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument('--payload', help='Payload único (cadena).')
    src.add_argument('--input-file', help='Archivo con payloads (uno por línea, UTF-8).')
    parser.add_argument('--modes', nargs='+', choices=['special_only','full_payload'], default=['special_only','full_payload'],
                        help='Modos a ejecutar. Default: ambos.')
    parser.add_argument('--output-dir', default='out', help='Directorio de salida (se crea si no existe).')
    parser.add_argument('--skip-broken', action='store_true', default=True,
                        help='Saltar charsets que no pueden representar los bytes necesarios (default: True).')
    parser.add_argument('--include-broken', action='store_true', default=False,
                        help='Forzar inclusión de charsets rotos (anula --skip-broken).')
    parser.add_argument('--base-charset', default='utf-8', help='Charset base para no especiales en special_only (default utf-8).')
    parser.add_argument('--charsets', nargs='*', help='Lista de charsets a usar (por defecto: todos los disponibles en Python).')
    args = parser.parse_args()

    # Resolver política skip/include
    skip_broken = True
    if args.include_broken:
        skip_broken = False
    elif args.skip_broken:
        skip_broken = True

    # Resolver charsets
    if args.charsets:
        charsets = sorted(set(c.lower().replace('-', '_') for c in args.charsets))
    else:
        charsets = all_codecs()

    payloads = read_payloads(args.input_file, args.payload)

    # Preparar salida
    os.makedirs(args.output_dir, exist_ok=True)
    paths = {}
    if 'special_only' in args.modes:
        paths['special_only'] = os.path.join(args.output_dir, 'encoded_special_only.txt')
    if 'full_payload' in args.modes:
        paths['full_payload'] = os.path.join(args.output_dir, 'encoded_full_payload.txt')

    # Abrimos archivos en binario para escribir bytes reales
    files = {mode: open(p, 'wb') for mode, p in paths.items()}

    total_written = {mode:0 for mode in files}
    total_skipped = {mode:0 for mode in files}

    try:
        for payload in payloads:
            for cs in charsets:
                for mode in files:
                    try:
                        if mode == 'special_only':
                            b = encode_special_only(payload, cs, base_charset=args.base_charset)
                        else:
                            b = encode_full_payload(payload, cs)
                        files[mode].write(b + b'\n')
                        total_written[mode] += 1
                    except Exception:
                        total_skipped[mode] += 1
                        if not skip_broken:
                            # Escribimos una línea vacía para mantener cardinalidad, si se exige incluir rotos
                            files[mode].write(b'' + b'\n')
    finally:
        for f in files.values():
            f.close()

    # Resumen a stdout
    print("Charsets usados:", len(charsets))
    print("Payloads de entrada:", len(payloads))
    for mode in paths:
        print(f"[{mode}] escrito: {total_written[mode]} líneas, salteado: {total_skipped[mode]}")
        print(f"Archivo: {paths[mode]}")

if __name__ == '__main__':
    main()

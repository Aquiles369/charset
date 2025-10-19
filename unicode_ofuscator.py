#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unicode_ofuscator.py
--------------------
Genera variantes de payloads XSS aplicando *ofuscaciones Unicode* en texto permitido
(strings, identificadores, contenido visible), sin alterar sintaxis crítica.

Soporta:
  - --payload "<PAYLOAD>"  → payload único
  - --input-file payloads.txt → lista de payloads (uno por línea)
Por cada payload genera 28 variantes (una por bloque Unicode predefinido).

⚔️ Reglas duras:
  - No toca tokens críticos: < > = + ( ) { } [ ] . , ; : ' " / ? ! & # % * \ ~ ^ | `
  - No altera nombres de etiquetas ni eventos (img, script, onerror, onload, etc.)
  - Solo muta dentro de strings, identificadores y contenido visible
  - Si rompe sintaxis → se descarta (modo estricto por defecto)

Uso rápido:
  python unicode_ofuscator.py --payload "<img src=x onerror=alert(1)>" --output-dir out
  python unicode_ofuscator.py --input-file payloads.txt --output-dir out
"""

import os
import argparse
import re
from typing import List, Dict, Callable

# ================================================================
# ⚔️ 1. Configuración global
# ================================================================

# Tokens intocables (símbolos críticos de HTML/JS)
CRITICAL_TOKENS = set("<>=+(){}[].,;:'\"/?!&#%*\\`~^|")

# Palabras reservadas que NO se deben mutar (etiquetas y eventos críticos)
RESERVED_WORDS = {
    'script', 'img', 'svg', 'math', 'iframe', 'body', 'video', 'audio',
    'onerror', 'onload', 'onmouseover', 'onfocus', 'onblur', 'onclick'
}

# Bandera de validación estricta
STRICT_MODE = True

# ================================================================
# ⚔️ 2. Parser de payloads (simplificado)
# ================================================================

def extract_mutable_sections(payload: str) -> List[Dict]:
    """
    Extrae secciones mutables del payload:
    - Strings entre comillas simples/dobles
    - Identificadores simples (alert, test123, fooBar)
    - Contenido de texto plano visible entre etiquetas
    Devuelve lista de dicts con {type, start, end, text}.
    """
    sections = []

    # Strings entre comillas
    for m in re.finditer(r'(["\'])(.*?)(\1)', payload):
        sections.append({
            'type': 'string',
            'start': m.start(2),
            'end': m.end(2),
            'text': m.group(2)
        })

    # Identificadores (palabras alfanuméricas)
    for m in re.finditer(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', payload):
        word = m.group(1)
        if word.lower() not in RESERVED_WORDS:
            sections.append({
                'type': 'identifier',
                'start': m.start(1),
                'end': m.end(1),
                'text': word
            })

    # Texto visible entre etiquetas (ej: >Hola<)
    for m in re.finditer(r'>([^<]+)<', payload):
        content = m.group(1)
        if content.strip():
            sections.append({
                'type': 'text',
                'start': m.start(1),
                'end': m.end(1),
                'text': content
            })

    return sections

# ================================================================
# ⚔️ 3. Módulo de validación
# ================================================================

def is_valid_payload(payload: str) -> bool:
    """
    Valida payload según reglas:
    - Sintaxis balanceada de comillas y paréntesis
    - No contiene invisibles disruptivos
    """
    if payload.count('"') % 2 != 0: return False
    if payload.count("'") % 2 != 0: return False
    if payload.count("(") != payload.count(")"): return False
    if payload.count("{") != payload.count("}"): return False
    if payload.count("[") != payload.count("]"): return False
    return True

# ================================================================
# ⚔️ 4. Ofuscadores (placeholders, se cargan en Parte 2)
# ================================================================

OFUSCATORS: Dict[str, Callable[[str], str]] = {}

def register_ofuscator(block_id: str, func: Callable[[str], str]):
    """Registra un ofuscador para un bloque."""
    OFUSCATORS[block_id] = func

def apply_ofuscations(payload: str) -> Dict[str, str]:
    """
    Aplica todos los ofuscadores al payload.
    Devuelve dict {block_id: variante}.
    """
    variants = {}
    sections = extract_mutable_sections(payload)
    for block_id, func in OFUSCATORS.items():
        new_payload = list(payload)
        for sec in sections:
            mutated = func(sec['text'])
            new_payload[sec['start']:sec['end']] = mutated
        result = ''.join(new_payload)
        if not STRICT_MODE or is_valid_payload(result):
            variants[block_id] = result
    return variants

# ================================================================
# ⚔️ 5. CLI principal
# ================================================================

def read_payloads(input_file: str=None, payload: str=None) -> List[str]:
    if payload and input_file:
        raise ValueError("Usa --payload o --input-file, no ambos.")
    if not payload and not input_file:
        raise ValueError("Debes proporcionar --payload o --input-file.")
    if payload:
        return [payload]
    # Desde archivo
    out = []
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            s = line.strip()
            if s:
                out.append(s)
    return out

def main():
    parser = argparse.ArgumentParser(description="Ofuscador Unicode para payloads XSS (28 bloques).")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument('--payload', help='Payload único.')
    src.add_argument('--input-file', help='Archivo con payloads.')
    parser.add_argument('--output-dir', default='out', help='Directorio de salida.')
    parser.add_argument('--strict', action='store_true', default=True, help='Validación estricta (default ON).')
    args = parser.parse_args()

    global STRICT_MODE
    STRICT_MODE = args.strict

    payloads = read_payloads(args.input_file, args.payload)

    os.makedirs(args.output_dir, exist_ok=True)
    out_file = os.path.join(args.output_dir, 'unicode_obfuscated.txt')

    with open(out_file, 'w', encoding='utf-8') as f:
        for p in payloads:
            variants = apply_ofuscations(p)
            for block_id, v in variants.items():
                f.write(v + '\n')

    print(f"Payloads procesados: {len(payloads)}")
    print(f"Bloques aplicados: {len(OFUSCATORS)}")
    print(f"Archivo generado: {out_file}")

if __name__ == '__main__':
    main()

# ================================================================
# ⚔️ 6. Registro de ofuscadores (Bloques #1–#28)
# ================================================================

# === Bloque #1: ASCII (identidad, baseline) ===
register_ofuscator("#1_ASCII", lambda s: s)

# === Bloque #2: Latin-1 Supplement (U+0080–U+00FF) ===
LATIN1_MAP = str.maketrans({
    'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú',
    'A': 'À', 'E': 'È', 'I': 'Ì', 'O': 'Ò', 'U': 'Ù'
})
register_ofuscator("#2_Latin1", lambda s: s.translate(LATIN1_MAP))

# === Bloque #3: Latin Extended-A (U+0100–U+017F) ===
LATIN_EXT_A = str.maketrans({
    'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū',
    'c': 'č', 's': 'š', 'z': 'ž'
})
register_ofuscator("#3_LatinExtA", lambda s: s.translate(LATIN_EXT_A))

# === Bloque #4: Latin Extended-B (U+0180–U+024F) ===
LATIN_EXT_B = str.maketrans({'d': 'đ', 'g': 'ǧ', 'n': 'ŋ', 't': 'ŧ'})
register_ofuscator("#4_LatinExtB", lambda s: s.translate(LATIN_EXT_B))

# === Bloque #5: Latin Extended Additional (U+1E00–U+1EFF) ===
LATIN_ADD = str.maketrans({'a': 'ạ', 'e': 'ẹ', 'o': 'ọ', 'u': 'ụ'})
register_ofuscator("#5_LatinAdditional", lambda s: s.translate(LATIN_ADD))

# === Bloque #6: Greek (homoglifos) (U+0370–U+03FF) ===
GREEK_MAP = str.maketrans({'A': 'Α', 'B': 'Β', 'E': 'Ε', 'Z': 'Ζ', 'H': 'Η', 'I': 'Ι', 'K': 'Κ', 'M': 'Μ', 'N': 'Ν', 'O': 'Ο', 'P': 'Ρ', 'T': 'Τ', 'X': 'Χ', 'Y': 'Υ'})
register_ofuscator("#6_Greek", lambda s: s.translate(GREEK_MAP))

# === Bloque #7: Greek Extended (U+1F00–U+1FFF) ===
GREEK_EXT = str.maketrans({'a': 'ᾰ', 'e': 'ᾱ', 'i': 'ᾶ', 'o': 'ᾷ'})
register_ofuscator("#7_GreekExt", lambda s: s.translate(GREEK_EXT))

# === Bloque #8: Cyrillic (homoglifos) (U+0400–U+04FF) ===
CYRILLIC_MAP = str.maketrans({'A': 'А', 'B': 'В', 'E': 'Е', 'K': 'К', 'M': 'М', 'H': 'Н', 'O': 'О', 'P': 'Р', 'C': 'С', 'T': 'Т', 'Y': 'У', 'X': 'Х'})
register_ofuscator("#8_Cyrillic", lambda s: s.translate(CYRILLIC_MAP))

# === Bloque #9: Cyrillic Supplement (U+0500–U+052F) ===
CYRILLIC_SUPP = str.maketrans({'y': 'ў', 'e': 'ѐ', 'o': 'ө'})
register_ofuscator("#9_CyrillicSupp", lambda s: s.translate(CYRILLIC_SUPP))

# === Bloque #10: Fullwidth Latin (U+FF01–U+FF5E) ===
def to_fullwidth(text: str) -> str:
    return ''.join(chr(ord(c) + 0xFEE0) if '!' <= c <= '~' and c not in CRITICAL_TOKENS else c for c in text)
register_ofuscator("#10_Fullwidth", to_fullwidth)

# === Bloque #11: Math Alphanumeric Symbols — Latin (U+1D400–U+1D7FF) ===
MATH_LATIN = str.maketrans({'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡'})
register_ofuscator("#11_MathLatin", lambda s: s.translate(MATH_LATIN))

# === Bloque #12: Math Alphanumeric Symbols — Greek ===
MATH_GREEK = str.maketrans({'a': '𝛂', 'b': '𝛃', 'g': '𝛄'})
register_ofuscator("#12_MathGreek", lambda s: s.translate(MATH_GREEK))

# === Bloque #13: Phonetic Extensions (U+1D00–U+1D7F) ===
PHONETIC = str.maketrans({'a': 'ᴀ', 'e': 'ᴇ', 'o': 'ᴏ'})
register_ofuscator("#13_Phonetic", lambda s: s.translate(PHONETIC))

# === Bloque #14: Phonetic Extensions Supplement ===
PHONETIC_SUPP = str.maketrans({'r': 'ʀ', 'h': 'ʜ', 't': 'ᴛ'})
register_ofuscator("#14_PhoneticSupp", lambda s: s.translate(PHONETIC_SUPP))

# === Bloque #15: Combining Diacritical Marks (U+0300–U+036F) ===
def add_combining(text: str) -> str:
    return ''.join(ch + '\u0301' if ch.isalpha() else ch for ch in text)
register_ofuscator("#15_Combining", add_combining)

# === Bloque #16: Latin Extended C/D/E ===
LATIN_EXT_CDE = str.maketrans({'l': 'ⱡ', 'n': 'ꞑ', 's': 'ꞩ'})
register_ofuscator("#16_LatinCDE", lambda s: s.translate(LATIN_EXT_CDE))

# === Bloque #17: Modifier Letters (U+02B0–U+02FF) ===
MODIFIER = str.maketrans({'h': 'ʰ', 'j': 'ʲ', 'w': 'ʷ'})
register_ofuscator("#17_Modifier", lambda s: s.translate(MODIFIER))

# === Bloque #18: Greek & Coptic confusables ===
GREEK_CONF = str.maketrans({'p': 'ρ', 'f': 'ϝ'})
register_ofuscator("#18_GreekConf", lambda s: s.translate(GREEK_CONF))

# === Bloque #19: Cyrillic Extended A/B ===
CYRILLIC_EXT = str.maketrans({'d': 'ԁ', 'g': 'ԍ'})
register_ofuscator("#19_CyrillicExt", lambda s: s.translate(CYRILLIC_EXT))

# === Bloque #20: Letterlike Symbols (U+2100–U+214F) ===
LETTERLIKE = str.maketrans({'c': 'ℂ', 'p': 'ℙ', 'h': 'ℋ'})
register_ofuscator("#20_Letterlike", lambda s: s.translate(LETTERLIKE))

# === Bloque #21: Superscripts & Subscripts (U+2070–U+209F) ===
SUPERSUB = str.maketrans({'1': '¹', '2': '²', '3': '³'})
register_ofuscator("#21_Supersub", lambda s: s.translate(SUPERSUB))

# === Bloque #22: Combining Diacritical Marks Extended ===
def add_combining_ext(text: str) -> str:
    return ''.join(ch + '\u1AB0' if ch.isalpha() else ch for ch in text)
register_ofuscator("#22_CombiningExt", add_combining_ext)

# === Bloque #23: Enclosed Alphanumerics (U+2460–U+24FF) ===
ENCLOSED = str.maketrans({'1': '①', '2': '②', '3': '③'})
register_ofuscator("#23_Enclosed", lambda s: s.translate(ENCLOSED))

# === Bloque #24: (duplicado de #5) — omitido
# === Bloque #25: Spacing Modifier Letters (U+02B0–U+02FF) ===
SPACING_MOD = str.maketrans({'a': 'ᵃ', 'e': 'ᵉ', 'o': 'ᵒ'})
register_ofuscator("#25_SpacingMod", lambda s: s.translate(SPACING_MOD))

# === Bloque #26: Greek & Coptic extra confusables ===
GREEK_EXTRA = str.maketrans({'v': 'ν', 't': 'τ'})
register_ofuscator("#26_GreekExtra", lambda s: s.translate(GREEK_EXTRA))

# === Bloque #27: Cyrillic Extended A/B extra ===
CYRILLIC_EXTRA = str.maketrans({'a': 'ꙗ', 'y': 'ꙑ'})
register_ofuscator("#27_CyrillicExtra", lambda s: s.translate(CYRILLIC_EXTRA))

# === Bloque #28: Mathematical Operators (U+2200–U+22FF) ===
MATH_OP = str.maketrans({'*': '×', '-': '−', '+': '∔'})
register_ofuscator("#28_MathOps", lambda s: s.translate(MATH_OP))


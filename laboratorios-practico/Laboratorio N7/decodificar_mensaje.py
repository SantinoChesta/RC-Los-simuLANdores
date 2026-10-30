#!/usr/bin/env python3
"""
decodificar_mensaje.py — TP7 Redes de Computadoras.

Lee un archivo de texto con unos y ceros y lo traduce a caracteres ASCII,
tomando los bits de a 7 (por ejemplo, 1000001 -> A).
Cada línea del archivo se decodifica por separado.

Uso:
    python decodificar_mensaje.py                  # lee mensaje.txt
    python decodificar_mensaje.py otro_archivo.txt
"""
import sys

ruta = sys.argv[1] if len(sys.argv) > 1 else "mensaje.txt"

with open(ruta, encoding="utf-8") as f:
    for linea in f:
        bits = linea.strip()
        if bits:
            print("".join(chr(int(bits[k:k + 7], 2)) for k in range(0, len(bits), 7)))

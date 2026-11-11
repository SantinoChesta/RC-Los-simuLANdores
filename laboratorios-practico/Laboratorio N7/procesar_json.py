#!/usr/bin/env python3
"""TP7: analiza el texto JSON, verifica paridades y decodifica los candidatos.

Uso:
    python3 procesar_json.py '{"SIZE":"1,7","PL":"1000000","CHECK":"01000001"}'
    python3 procesar_json.py                 # pegar JSON y terminar con Ctrl+D
    python3 procesar_json.py < paquete.json

Debe estar junto a procesar_captura.py, paridad.py y decodificar_mensaje.py.
No requiere tshark. No modifica el JSON original ni elige candidatos ambiguos.
"""

import argparse
import json
from pathlib import Path
import sys
import tempfile

from procesar_captura import procesar


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("texto", nargs="?", help="Texto JSON entre comillas; si se omite, lee la entrada estándar")
    parser.add_argument("-o", "--salida", type=Path, help="Carpeta nueva para los resultados (no debe existir)")
    args = parser.parse_args()
    try:
        for script in ("paridad.py", "decodificar_mensaje.py"):
            if not (Path(__file__).resolve().parent / script).is_file():
                raise ValueError(f"Falta {script}: debe estar junto a procesar_json.py.")
        if args.texto is None and sys.stdin.isatty():
            print("Pegá el JSON completo y terminá con Enter y Ctrl+D:", file=sys.stderr)
        mensaje = json.loads(args.texto if args.texto is not None else sys.stdin.read())
        if not isinstance(mensaje, dict):
            raise ValueError("La entrada debe ser un objeto JSON con SIZE, PL y CHECK.")
        if args.salida:
            salida = args.salida.expanduser().resolve()
            salida.mkdir(parents=True, exist_ok=False)
        else:
            salida = Path(tempfile.mkdtemp(prefix="json_tp7_", dir=Path.cwd()))
        print(procesar([{"mensaje": mensaje, "paquetes": []}], [], salida))
        print(f"Resultados guardados en: {salida}")
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()

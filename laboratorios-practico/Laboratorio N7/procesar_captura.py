#!/usr/bin/env python3
"""TP7: extrae mensajes UDP JSON de una captura y ejecuta los scripts de la cátedra.

Uso: python3 procesar_captura.py captura.pcapng [-o carpeta_nueva]
Requiere tshark en PATH y paridad.py y decodificar_mensaje.py junto a este archivo.
No abre enlaces ni ejecuta instrucciones contenidas en los paquetes.
"""

import argparse
import itertools
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def paridades(filas):
    por_fila = "".join(str(fila.count("1") % 2) for fila in filas)
    por_columna = "".join(
        str(sum(fila[j] == "1" for fila in filas) % 2)
        for j in range(len(filas[0]))
    )
    return por_fila, por_columna


def analizar(mensaje):
    if not all(isinstance(mensaje.get(k), str) for k in ("SIZE", "PL", "CHECK")):
        raise ValueError("SIZE, PL y CHECK deben ser cadenas de texto.")
    try:
        cantidad, columnas = map(int, mensaje["SIZE"].split(","))
    except ValueError as exc:
        raise ValueError("SIZE debe tener formato FILAS,COLUMNAS.") from exc
    if cantidad <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser positivas.")
    bits, control = mensaje["PL"], mensaje["CHECK"]
    if not bits or set(bits) - {"0", "1"}:
        raise ValueError("PL no contiene exclusivamente unos y ceros; no se decodifica como bits.")
    if not control or set(control) - {"0", "1"}:
        raise ValueError("CHECK no contiene exclusivamente unos y ceros.")
    if len(bits) % cantidad:
        raise ValueError("PL no se puede dividir en la cantidad de filas declarada.")
    ancho = len(bits) // cantidad
    avisos = []
    if ancho != columnas:
        if ancho != columnas * 7:
            raise ValueError("La longitud de PL no coincide con SIZE, ni usando ASCII de 7 bits.")
        avisos.append(
            f"SIZE={mensaje['SIZE']}, pero los datos forman {cantidad} filas de {ancho} bits: "
            f"{columnas} caracteres ASCII por fila. Interpretación inferida de las longitudes."
        )
    if len(control) != cantidad + ancho:
        raise ValueError(f"CHECK tiene {len(control)} bits; se esperaban {cantidad + ancho}.")
    filas = [bits[i:i + ancho] for i in range(0, len(bits), ancho)]
    calculadas_f, calculadas_c = paridades(filas)
    recibidas_f, recibidas_c = control[:cantidad], control[cantidad:]
    fallas_f = [i + 1 for i, (a, b) in enumerate(zip(calculadas_f, recibidas_f)) if a != b]
    fallas_c = [i + 1 for i, (a, b) in enumerate(zip(calculadas_c, recibidas_c)) if a != b]
    if ancho % 7:
        avisos.append(
            "El ancho no es múltiplo de 7. El script de la cátedra interpreta también "
            "el grupo incompleto al final de cada fila: su texto puede ser engañoso."
        )
    candidatos = []
    if not fallas_f and not fallas_c:
        estado = "Paridades consistentes; ciertos errores múltiples pueden pasar inadvertidos."
    elif len(fallas_f) == len(fallas_c) == 1:
        estado = "Corrección única bajo el supuesto de un solo error en los datos."
    elif (len(fallas_f), len(fallas_c)) in ((1, 0), (0, 1)):
        estado = "Posible error de un bit de control. No se modifica ningún dato."
    else:
        estado = "Errores múltiples: no hay una corrección única garantizada."

    # shortcut: solo enumera el modelo de un error por fila/columna fallida; otros patrones requieren otro código.
    if fallas_f and len(fallas_f) == len(fallas_c):
        if len(fallas_f) > 5:
            avisos.append("Hay más de 120 emparejamientos; se omite la enumeración para no generar miles de archivos.")
        else:
            for columnas_error in itertools.permutations(fallas_c):
                matriz = [list(fila) for fila in filas]
                cambios = []
                for fila, columna in zip(fallas_f, columnas_error):
                    antes = matriz[fila - 1][columna - 1]
                    despues = "1" if antes == "0" else "0"
                    matriz[fila - 1][columna - 1] = despues
                    cambios.append({"fila": fila, "columna": columna, "recibido": antes, "corregido": despues})
                matriz = ["".join(fila) for fila in matriz]
                if "".join(paridades(matriz)) != control:
                    raise ValueError("La corrección generada no satisface los controles.")
                candidatos.append({"filas": matriz, "cambios": cambios})
            if len(fallas_f) > 1:
                avisos.append(
                    f"Los {math.factorial(len(fallas_f))} candidatos suponen exactamente "
                    f"{len(fallas_f)} errores en datos, uno en cada fila y columna fallida, "
                    "y controles intactos. Todos cierran las paridades; ninguno se elige automáticamente."
                )
    return {
        "filas": filas, "ancho_bits": ancho, "avisos": avisos, "estado": estado,
        "paridad_filas_recibida": recibidas_f, "paridad_filas_calculada": calculadas_f,
        "paridad_columnas_recibida": recibidas_c, "paridad_columnas_calculada": calculadas_c,
        "filas_fallidas": fallas_f, "columnas_fallidas": fallas_c, "candidatos": candidatos,
    }


def extraer(captura):
    campos = ["frame.number", "frame.time_relative", "ip.src", "ip.dst",
              "udp.srcport", "udp.dstport", "eth.dst", "udp.payload"]
    comando = ["tshark", "-n", "-r", str(captura), "-Y", 'udp && frame contains "SIZE"', "-T", "fields"]
    for campo in campos:
        comando.extend(["-e", campo])
    proceso = subprocess.run(comando, capture_output=True, text=True, encoding="utf-8")
    if proceso.returncode:
        raise ValueError(f"No se pudo leer la captura: {proceso.stderr.strip()}")
    grupos, descartados = {}, []
    for linea in proceso.stdout.splitlines():
        valores = linea.split("\t")
        if len(valores) != len(campos):
            descartados.append("Registro con campos incompletos.")
            continue
        trama, tiempo, origen, destino, puerto_o, puerto_d, mac_destino, carga = valores
        try:
            mensaje = json.loads(bytes.fromhex(carga.replace(":", "")).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            descartados.append(f"Trama {trama}: carga no interpretable como JSON completo.")
            continue
        if not isinstance(mensaje, dict) or not {"SIZE", "PL", "CHECK"} <= mensaje.keys():
            descartados.append(f"Trama {trama}: faltan campos SIZE, PL o CHECK.")
            continue
        clave = json.dumps(mensaje, sort_keys=True)
        grupo = grupos.setdefault(clave, {"mensaje": mensaje, "paquetes": []})
        grupo["paquetes"].append({
            "trama": int(trama), "segundos": tiempo, "ip_origen": origen,
            "ip_destino": destino, "puerto_origen": puerto_o, "puerto_destino": puerto_d,
            "mac_destino": mac_destino,
        })
    return list(grupos.values()), descartados


def ejecutar_scripts(filas, carpeta, nombre):
    archivo = carpeta / f"{nombre}.txt"
    archivo.write_text("\n".join(filas) + "\n", encoding="utf-8")
    salidas = {}
    for script in ("paridad.py", "decodificar_mensaje.py"):
        proceso = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / script), str(archivo)],
            capture_output=True, text=True, encoding="utf-8",
        )
        if proceso.returncode:
            raise ValueError(f"Falló {script}: {proceso.stderr.strip()}")
        salidas[script] = proceso.stdout
    (carpeta / f"{nombre}_paridades.txt").write_text(salidas["paridad.py"], encoding="utf-8")
    (carpeta / f"{nombre}_decodificado.txt").write_text(salidas["decodificar_mensaje.py"], encoding="utf-8")
    # El texto concatenado conserva caracteres de control; la salida del script queda guardada aparte.
    texto = "".join(
        "".join(chr(int(fila[i:i + 7], 2)) for i in range(0, len(fila), 7))
        for fila in filas
    )
    return {"archivo": archivo.name, "texto": texto, "salidas": salidas}


def procesar(grupos, descartados, salida, captura=None):
    resumen = [f"# TP7: {captura.name if captura else 'JSON pegado'}", ""]
    if captura:
        resumen.extend([f"Captura: {captura}", "",
                        f"Paquetes JSON del TP: {sum(len(g['paquetes']) for g in grupos)}. Mensajes diferentes: {len(grupos)}.",
                        "", "Un solo paquete completo alcanza. Las repeticiones idénticas se agrupan.",
                        "El análisis cubre mensajes JSON en UDP, como los observados en este laboratorio.", ""])
    for numero, grupo in enumerate(grupos, 1):
        carpeta = salida / f"mensaje_{numero:02d}"
        carpeta.mkdir()
        (carpeta / "paquete.json").write_text(json.dumps(grupo["mensaje"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        resumen.extend([f"## Mensaje {numero}", ""])
        if grupo["paquetes"]:
            tramas = ", ".join(str(p["trama"]) for p in grupo["paquetes"])
            primero = grupo["paquetes"][0]
            resumen.extend([f"Tramas: {tramas}.",
                            f"UDP {primero['ip_origen']}:{primero['puerto_origen']} -> {primero['ip_destino']}:{primero['puerto_destino']}",
                            f"MAC destino (si la captura la expone como Ethernet): {primero['mac_destino'] or 'no disponible'}", ""])
        try:
            analisis = analizar(grupo["mensaje"])
        except ValueError as exc:
            grupo["error"] = str(exc)
            resumen.extend([f"No procesable: {exc}", f"PL recibido: {json.dumps(grupo['mensaje'].get('PL'), ensure_ascii=False)}", ""])
            continue
        grupo["analisis"] = analisis
        recibido = ejecutar_scripts(analisis["filas"], carpeta, "recibido")
        analisis["recibido"] = recibido
        resumen.extend([analisis["estado"], *analisis["avisos"], "",
                        f"Filas fallidas (desde 1): {analisis['filas_fallidas']}",
                        f"Columnas fallidas (desde 1): {analisis['columnas_fallidas']}",
                        f"Paridad filas recibida: {analisis['paridad_filas_recibida']}",
                        f"Paridad filas calculada: {analisis['paridad_filas_calculada']}",
                        f"Paridad columnas recibida: {analisis['paridad_columnas_recibida']}",
                        f"Paridad columnas calculada: {analisis['paridad_columnas_calculada']}",
                        f"Texto recibido: {json.dumps(recibido['texto'], ensure_ascii=False)}", ""])
        for n, candidato in enumerate(analisis["candidatos"], 1):
            candidato.update(ejecutar_scripts(candidato["filas"], carpeta, f"candidato_{n:03d}"))
            cambios = "; ".join(f"({c['fila']},{c['columna']}): {c['recibido']} -> {c['corregido']}" for c in candidato["cambios"])
            resumen.extend([f"Candidato {n}: {json.dumps(candidato['texto'], ensure_ascii=False)}", f"Cambios: {cambios}", ""])
    if not grupos:
        resumen.extend(["No se encontraron mensajes UDP JSON completos con SIZE, PL y CHECK.",
                        "Revisá la interfaz/red de captura. Más tiempo puede ayudar, pero no se requiere una cantidad mínima de paquetes.", ""])
    if descartados:
        resumen.extend(["## Registros descartados", "", *descartados, ""])
    informe = "\n".join(resumen)
    (salida / "informe.md").write_text(informe, encoding="utf-8")
    (salida / "analisis.json").write_text(json.dumps({"captura": str(captura) if captura else None, "mensajes": grupos, "descartados": descartados}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return informe


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("captura", type=Path, help="Archivo .pcapng o .pcap")
    parser.add_argument("-o", "--salida", type=Path, help="Carpeta nueva para los resultados (no debe existir)")
    args = parser.parse_args()
    try:
        captura = args.captura.expanduser().resolve()
        if not captura.is_file():
            raise ValueError(f"No existe el archivo: {captura}")
        if not shutil.which("tshark"):
            raise ValueError("Falta tshark. Instalalo junto con las herramientas de consola de Wireshark.")
        for script in ("paridad.py", "decodificar_mensaje.py"):
            if not (Path(__file__).resolve().parent / script).is_file():
                raise ValueError(f"Falta {script}: debe estar junto a procesar_captura.py.")
        grupos, descartados = extraer(captura)
        if args.salida:
            salida = args.salida.expanduser().resolve()
            salida.mkdir(parents=True, exist_ok=False)
        else:
            salida = Path(tempfile.mkdtemp(prefix=f"{captura.stem}_decodificado_", dir=captura.parent))
        print(procesar(grupos, descartados, salida, captura))
        print(f"Resultados guardados en: {salida}")
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()

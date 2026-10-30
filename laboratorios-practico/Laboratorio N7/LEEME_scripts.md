# Scripts automáticos del TP7

Ejecutar desde esta carpeta. Requieren Python 3 y los archivos originales
`paridad.py` y `decodificar_mensaje.py`. El procesador de capturas también
requiere `tshark` instalado. El procesador de JSON importa el análisis de
`procesar_captura.py`, pero no requiere tshark.

## Desde una captura

```bash
python3 procesar_captura.py paquetes1.pcapng
```

Busca mensajes JSON UDP con SIZE, PL y CHECK y agrupa las cargas idénticas.
Un solo paquete completo alcanza. No necesita Internet.
La captura queda intacta. Por defecto crea una carpeta nueva junto a ella.

## Desde texto JSON

Para pegar un JSON de cualquier largo:

```bash
python3 procesar_json.py
```

Pegá el JSON completo, presioná Enter y después Ctrl+D.
También podés pasar el JSON entre comillas simples:

```bash
python3 procesar_json.py '{"SIZE":"1,7","PL":"1000000","CHECK":"01000001"}'
```

Ese ejemplo recibe `@`, detecta el error en fila 1, columna 7 y produce `A`.
Si ya lo guardaste en un archivo:

```bash
python3 procesar_json.py < paquete.json
```

Por defecto crea una carpeta `json_tp7_...` en la carpeta actual.
Ambos scripts aceptan `-o carpeta_nueva` para indicar otro destino; se niegan
a sobrescribir una carpeta existente.

## Resultados

- `informe.md`: resumen, paridades, síndrome y cambios de cada candidato.
- `analisis.json`: información completa para reutilizar.
- `mensaje_XX/paquete.json`: JSON recibido.
- `mensaje_XX/recibido.txt`: matriz original, sin controles.
- `mensaje_XX/candidato_NNN.txt`: matriz corregida de cada candidato.
- Archivos `*_paridades.txt` y `*_decodificado.txt`: salidas de los dos
  scripts originales, ejecutados sobre cada matriz.

Las filas y columnas se numeran desde 1. Si SIZE declara columnas como
cantidad de caracteres ASCII de 7 bits, se verifica esa interpretación
contra las longitudes de PL y CHECK y se deja constancia en el informe.

## Límites de la corrección

Una fila y una columna fallida permiten corregir bajo el supuesto de un
único error de datos. Si fallan varias, el programa enumera los emparejamientos
posibles suponiendo controles intactos y exactamente un error en cada fila
y columna fallida. Todos esos candidatos satisfacen los controles; no son
una recuperación garantizada. Se enumeran hasta 120 candidatos (5 errores).
Otros patrones y posibles controles dañados se informan sin inventar cambios.
Que el texto sea legible no demuestra que la corrección sea la original.

No se abren enlaces ni se ejecutan instrucciones recibidas dentro del JSON.
El procesamiento de capturas cubre UDP; no reconstruye streams TCP.

## Pruebas

```bash
python3 -m unittest -v test_procesar_captura.py
```

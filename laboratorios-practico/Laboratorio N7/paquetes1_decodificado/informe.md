# TP7: paquetes1.pcapng

Captura: /home/valentino/Documentos/UNC/3TO AÑO/REDES DE COMPUTADORAS/RC-Los-simuLANdores/laboratorios-practico/Laboratorio N7/paquetes1.pcapng

Paquetes JSON del TP: 9. Mensajes diferentes: 3.

Un solo paquete completo alcanza. Las repeticiones idénticas se agrupan.
El análisis cubre mensajes JSON en UDP, como los observados en este laboratorio.

## Mensaje 1

Tramas: 368, 538, 1364, 1418, 1952.
UDP 192.168.8.150:63573 -> 192.168.8.255:12007
MAC destino (si la captura la expone como Ethernet): ff:ff:ff:ff:ff:ff

Errores múltiples: no hay una corrección única garantizada.
SIZE=8,7, pero los datos forman 8 filas de 49 bits: 7 caracteres ASCII por fila. Interpretación inferida de las longitudes.
Los 6 candidatos suponen exactamente 3 errores en datos, uno en cada fila y columna fallida, y controles intactos. Todos cierran las paridades; ninguno se elige automáticamente.

Filas fallidas (desde 1): [5, 6, 7]
Columnas fallidas (desde 1): [9, 17, 23]
Paridad filas recibida: 01111101
Paridad filas calculada: 01110011
Paridad columnas recibida: 0110111111110110011100101111001100001100110010001
Paridad columnas calculada: 0110111101110110111100001111001100001100110010001
Texto recibido: "https://youtube.com/shorts/q8wgKzJwPa$?featurE=share "

Candidato 1: "https://youtube.com/shorts/q8WgKzJwPa4?feature=share " -- ES ESTE
Cambios: (5,9): 1 -> 0; (6,17): 0 -> 1; (7,23): 0 -> 1

Candidato 2: "https://youtube.com/shorts/q8WgKzJwPa$\u001ffeatubE=share "
Cambios: (5,9): 1 -> 0; (6,23): 1 -> 0; (7,17): 1 -> 0

Candidato 3: "https://youtube.com/shorts/q8wwKzJwPA$?feature=share "
Cambios: (5,17): 0 -> 1; (6,9): 1 -> 0; (7,23): 0 -> 1

Candidato 4: "https://youtube.com/shorts/q8wwKzJwPa$\u001ffeatUrE=share "
Cambios: (5,17): 0 -> 1; (6,23): 1 -> 0; (7,9): 1 -> 0

Candidato 5: "https://youtube.com/shorts/q8wgkzJwPA$?featubE=share "
Cambios: (5,23): 0 -> 1; (6,9): 1 -> 0; (7,17): 1 -> 0

Candidato 6: "https://youtube.com/shorts/q8wgkzJwPa4?featUrE=share "
Cambios: (5,23): 0 -> 1; (6,17): 0 -> 1; (7,9): 1 -> 0

## Mensaje 2

Tramas: 1325, 2853, 3171.
UDP 192.168.8.150:63573 -> 192.168.8.255:12007
MAC destino (si la captura la expone como Ethernet): ff:ff:ff:ff:ff:ff

No procesable: PL no contiene exclusivamente unos y ceros; no se decodifica como bits.
PL recibido: "https://www.youtube.com/watch?v=CsGYh8AacgY"

## Mensaje 3

Tramas: 2042.
UDP 192.168.8.150:63573 -> 192.168.8.255:12007
MAC destino (si la captura la expone como Ethernet): ff:ff:ff:ff:ff:ff

No procesable: PL no contiene exclusivamente unos y ceros; no se decodifica como bits.
PL recibido: "https://www.youtube.com/watch?v=msX4oAXpvUE"

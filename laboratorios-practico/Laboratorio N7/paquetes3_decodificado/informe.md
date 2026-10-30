# TP7: JSON pegado

## Mensaje 1

Errores múltiples: no hay una corrección única garantizada.
SIZE=4,4, pero los datos forman 4 filas de 28 bits: 4 caracteres ASCII por fila. Interpretación inferida de las longitudes.
Los 24 candidatos suponen exactamente 4 errores en datos, uno en cada fila y columna fallida, y controles intactos. Todos cierran las paridades; ninguno se elige automáticamente.

Filas fallidas (desde 1): [1, 2, 3, 4]
Columnas fallidas (desde 1): [7, 11, 15, 20]
Paridad filas recibida: 1000
Paridad filas calculada: 0111
Paridad columnas recibida: 1110100011101010001110100000
Paridad columnas calculada: 1110101011001000001010100000
Texto recibido: "Qr3mi8!:)1p-dIgZ"

Candidato 1: "Pr3mi0!:)10-dIeZ" -- ESTE ES EL CORRECTO
Cambios: (1,7): 1 -> 0; (2,11): 1 -> 0; (3,15): 1 -> 0; (4,20): 1 -> 0

Candidato 2: "Pr3mi0!:)1r-dI'Z"
Cambios: (1,7): 1 -> 0; (2,11): 1 -> 0; (3,20): 0 -> 1; (4,15): 1 -> 0

Candidato 3: "Pr3mi8a:)9p-dIeZ"
Cambios: (1,7): 1 -> 0; (2,15): 0 -> 1; (3,11): 0 -> 1; (4,20): 1 -> 0

Candidato 4: "Pr3mi8a:)1r-dAgZ"
Cambios: (1,7): 1 -> 0; (2,15): 0 -> 1; (3,20): 0 -> 1; (4,11): 1 -> 0

Candidato 5: "Pr3mi8#:)9p-dI'Z"
Cambios: (1,7): 1 -> 0; (2,20): 0 -> 1; (3,11): 0 -> 1; (4,15): 1 -> 0

Candidato 6: "Pr3mi8#:)10-dAgZ"
Cambios: (1,7): 1 -> 0; (2,20): 0 -> 1; (3,15): 1 -> 0; (4,11): 1 -> 0

Candidato 7: "Qz3mh8!:)10-dIeZ"
Cambios: (1,11): 0 -> 1; (2,7): 1 -> 0; (3,15): 1 -> 0; (4,20): 1 -> 0

Candidato 8: "Qz3mh8!:)1r-dI'Z"
Cambios: (1,11): 0 -> 1; (2,7): 1 -> 0; (3,20): 0 -> 1; (4,15): 1 -> 0

Candidato 9: "Qz3mi8a:(1p-dIeZ"
Cambios: (1,11): 0 -> 1; (2,15): 0 -> 1; (3,7): 1 -> 0; (4,20): 1 -> 0

Candidato 10: "Qz3mi8a:)1r-eIgZ"
Cambios: (1,11): 0 -> 1; (2,15): 0 -> 1; (3,20): 0 -> 1; (4,7): 0 -> 1

Candidato 11: "Qz3mi8#:(1p-dI'Z"
Cambios: (1,11): 0 -> 1; (2,20): 0 -> 1; (3,7): 1 -> 0; (4,15): 1 -> 0

Candidato 12: "Qz3mi8#:)10-eIgZ"
Cambios: (1,11): 0 -> 1; (2,20): 0 -> 1; (3,15): 1 -> 0; (4,7): 0 -> 1

Candidato 13: "Qrsmh8!:)9p-dIeZ"
Cambios: (1,15): 0 -> 1; (2,7): 1 -> 0; (3,11): 0 -> 1; (4,20): 1 -> 0

Candidato 14: "Qrsmh8!:)1r-dAgZ"
Cambios: (1,15): 0 -> 1; (2,7): 1 -> 0; (3,20): 0 -> 1; (4,11): 1 -> 0

Candidato 15: "Qrsmi0!:(1p-dIeZ"
Cambios: (1,15): 0 -> 1; (2,11): 1 -> 0; (3,7): 1 -> 0; (4,20): 1 -> 0

Candidato 16: "Qrsmi0!:)1r-eIgZ"
Cambios: (1,15): 0 -> 1; (2,11): 1 -> 0; (3,20): 0 -> 1; (4,7): 0 -> 1

Candidato 17: "Qrsmi8#:(1p-dAgZ"
Cambios: (1,15): 0 -> 1; (2,20): 0 -> 1; (3,7): 1 -> 0; (4,11): 1 -> 0

Candidato 18: "Qrsmi8#:)9p-eIgZ"
Cambios: (1,15): 0 -> 1; (2,20): 0 -> 1; (3,11): 0 -> 1; (4,7): 0 -> 1

Candidato 19: "Qr1mh8!:)9p-dI'Z"
Cambios: (1,20): 1 -> 0; (2,7): 1 -> 0; (3,11): 0 -> 1; (4,15): 1 -> 0

Candidato 20: "Qr1mh8!:)10-dAgZ"
Cambios: (1,20): 1 -> 0; (2,7): 1 -> 0; (3,15): 1 -> 0; (4,11): 1 -> 0

Candidato 21: "Qr1mi0!:(1p-dI'Z"
Cambios: (1,20): 1 -> 0; (2,11): 1 -> 0; (3,7): 1 -> 0; (4,15): 1 -> 0

Candidato 22: "Qr1mi0!:)10-eIgZ"
Cambios: (1,20): 1 -> 0; (2,11): 1 -> 0; (3,15): 1 -> 0; (4,7): 0 -> 1

Candidato 23: "Qr1mi8a:(1p-dAgZ"
Cambios: (1,20): 1 -> 0; (2,15): 0 -> 1; (3,7): 1 -> 0; (4,11): 1 -> 0

Candidato 24: "Qr1mi8a:)9p-eIgZ"
Cambios: (1,20): 1 -> 0; (2,15): 0 -> 1; (3,11): 0 -> 1; (4,7): 0 -> 1

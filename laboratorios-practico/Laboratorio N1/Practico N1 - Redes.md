![][image1]  
UNIVERSIDAD NACIONAL DE CÓRDOBA  
FACULTAD DE CIENCIAS EXACTAS, FÍSICAS Y NATURALES  
CÁTEDRA DE REDES DE COMPUTADORAS

TRABAJO PRÁCTICO Nº 1

**“Repaso de fundamentos esenciales e introducción a Packet Tracer”**

Grupo: “Los simuLANdores”

Alumnos:

Barrio, Rafael

Chesta, Santiago

Garay, Alexis Tomás

Guzmán Gonzalez, Pedro

Vera Gonzalez, Fernando Agustín

Martin, Agostina Rocio

Zucchella Paz, Valentino

Profesor:  
Ing. Santiago Martin Henn

Resolución de consignas:

1) a)Resumen de los fundamentos básicos y esenciales:  
   

**Ondas electromagnéticas:** Se refiere a la representación física de los datos, que permite el transporte e intercambio de información entre un emisor y receptor.  
Sus características principales son:

- **Naturaleza de la señal:** Pueden ser señales analogicas o digitales  
- **Parámetros fundamentales**: amplitud, frecuencia y fase  
- **Propagación**: Se transmiten a través de medios y guiados  
- **Longitud de onda:** Es la distancia física que ocupa un ciclo completo de la onda.   
- **Composición espectral:** Significa que una señal electromagnética está constituida por una serie de frecuencias constituyentes.


	**Modulación:** Es el proceso de codificar los datos o información de la fuente en una señal portadora. Con el objetivo de transmitir los datos hacia un receptor.

	**Demodulación:** Es el proceso en el cual el receptor capta la señal modulada y la transforma de nuevo para recuperar los datos originales de tal manera que los datos puedan ser manejados por el dispositivo de destino.

	**Señales de tiempo continuo:** Se refiere a que una señal no presenta discontinuidad en el tiempo.

	**Señales de tiempo discreto:** Es aquella señal cuya intensidad se mantiene constante en un valor durante un determinado tiempo.

b) Longitud de onda obtenida directamente del gráfico: λ \= 0.06 \[m\] 

Considerando  que la onda viaja a la velocidad de la luz c \= 3 x 108m/s, la frecuencia está dada por:  
f \= c \=(3 x 108m/s) / (0,06 m) \= 5x109 Hz \= 5 GHz

c) El espectro electromagnético se encuentra dividido en regiones (radiofrecuencia, microondas, infrarrojo, visible, ultravioleta, rayos X y rayos gamma, entre otras) y, dentro de estas, en bandas normalizadas según su frecuencia. De acuerdo con la clasificación de bandas de radiofrecuencia establecida por la Unión Internacional de Telecomunicaciones (ITU), una **frecuencia** de **5 GHz** se ubica dentro de la región de las **microondas**, específicamente en la **banda** denominada **SHF (Super High Frequency)**, definida por la ITU en el rango de **3 GHz a 30 GHz.**

d) Dentro de la banda SHF, y específicamente en la sub-banda de 5 GHz, operan numerosos dispositivos de comunicación de datos, como por ejemplo los routers y puntos de acceso WI-FI, comunicaciones satelitales, radar, etc.  
e) La línea roja es la **envolvente decreciente de la amplitud** de la onda a medida que aumenta la distancia. Representa la **atenuación**: la pérdida de energía/potencia de la señal a medida que se propaga por el medio. 

f) El fenómeno de **atenuación** descrito afecta de manera directa al funcionamiento de los routers Wi-Fi mencionados como ejemplo, dado que la intensidad de la señal recibida disminuye a medida que el dispositivo receptor se aleja del punto de acceso. 

Este fenómeno resulta fácilmente reconocible en la experiencia cotidiana: al desplazarse hacia una habitación alejada del router, o al interponer obstáculos como paredes o entrepisos, se observa una notable disminución en la calidad de la señal Wi-Fi, manifestada en menores velocidades de transmisión, mayor latencia o pérdida total de conectividad. Cabe destacar que, además de la atenuación por distancia, los obstáculos físicos introducen pérdidas adicionales por absorción y reflexión, acentuando el efecto observado. 

g)  
**i) Telefonía celular:** Sí, la atenuación afecta significativamente a las transmisiones celulares. Al tratarse de ondas de radio que se propagan por el espacio libre, su intensidad decrece con la distancia a la antena o estación base.

**ii) Cable coaxial:** Sí. Aunque es un medio guiado (no se propaga por el aire libre), el cable coaxial también presenta atenuación de la señal con la distancia recorrida, debido a la resistencia del conductor y las pérdidas dieléctricas. Por este motivo, en redes de cable (por ejemplo, distribución de TV o internet por cable) se instalan amplificadores y repetidores cada cierta distancia para compensar esta pérdida.

**iii) Fibra óptica:** Sí, pero en mucha menor medida. La fibra óptica también sufre atenuación (medida típicamente en dB/km), producto de la absorción del material y la dispersión de la luz dentro del núcleo de la fibra. Sin embargo, sus pérdidas son órdenes de magnitud menores que en cobre o en el aire libre (del orden de 0,2 a 0,5 dB/km en fibra monomodo), razón por la cual es el medio elegido para enlaces de larga distancia y backbones de internet.

2) a)   
   **Direccionalidad (Modo de transmisión):** Es una transmisión simplex (unidireccional) ya que los datos viajan solo en un sentido, desde el Módulo de comunicación emisor hacia el receptor.  
     
   **Características temporales (tipo de transmisión):** La transmisión es sincrónica, dado que junto con la línea de datos se transmite una señal de reloj (*clock*) dedicada, que permite sincronizar emisor y receptor   
   

b) El esquema Simplex representado no resulta adecuado si se busca una comunicación rápida y bidireccional dado que el flujo de datos está fijado en un solo sentido.

c) La cuarta letra de nuestro grupo (Los simuLANdores) es “ “ (espacio en blanco), lo cual en ascii es el número 32, en hexadecimal es 0x20, en binario 0010 0000\.  

<img width="827" height="221" alt="Captura de pantalla 2026-08-19 101707" src="https://github.com/user-attachments/assets/bddb3417-2239-42eb-8338-97a42d8885b4" />

d) Para determinar el valor digital de la señal de manera correcta debemos muestrear en el punto medio de cada intervalo de bit, una vez que la señal se estabilizó en su nivel final y antes de que empiece  la siguiente transición. Esto le da al receptor mayor margen posible frente a pequeñas variaciones de temporización.   
Si muestreamos durante la transición (flanco de subida o de bajada) el valor de tensión es ambiguo, no representa ni un “1” ni un “0” de manera limpia.

3) ¿Por qué no transmitir señales escalonadas por aire?  
   **Ancho de banda infinito:** una señal digital "escalonada" (onda cuadrada) matemáticamente contiene infinitos armónicos (serie de Fourier), lo que exigiría un ancho de banda infinito para transmitirse sin distorsión — inviable en la práctica y en cualquier medio real con ancho de banda limitado. Como consecuencia, al transmitirse, las componentes de alta frecuencia se atenúan y los bordes de la señal se suavizan o distorsionan.   
1)  La técnica de modulación que vemos en el gráfico es una modulación en fase, un cambio de fase representa un cambio de nivel de la señal digital.  
2) La señal 01110110 se vería modulada de la siguiente manera

<img width="942" height="227" alt="Captura de pantalla 2026-08-19 101915" src="https://github.com/user-attachments/assets/3e8b6440-24b4-4377-87cb-8f00c76605e3" />

3)   

**Modulación en fase (PSK \- Phase Shift Keying):** codifica información variando la fase de la portadora, manteniendo amplitud y frecuencia constantes. Técnicas principales:

* **BPSK** (Binary PSK): 2 fases posibles (0° y 180°), 1 bit por símbolo. La más robusta ante ruido, pero baja eficiencia espectral.  
* **QPSK** (Quadrature PSK): 4 fases (separadas 90°), 2 bits por símbolo. Duplica la tasa de transmisión respecto a BPSK con el mismo ancho de banda.  
* **8-PSK**: 8 fases, 3 bits por símbolo. Mayor eficiencia espectral, pero más sensible al ruido (fases más cercanas entre sí).  
* **DPSK** (Differential PSK): la info se codifica en el *cambio* de fase entre símbolos consecutivos, no en la fase absoluta. Evita necesitar una referencia de fase exacta en el receptor.

**Basadas en el mismo principio (combinan fase \+ amplitud):**

* **QAM** (Quadrature Amplitude Modulation): combina PSK con ASK, variando fase y amplitud simultáneamente (ej: 16-QAM, 64-QAM). Permite más bits por símbolo que PSK puro.  
4)  **Bit Error Rate (BER):** relación entre la cantidad de bits recibidos con error y el total de bits transmitidos en un período determinado. Es la métrica principal para medir la calidad/confiabilidad de un enlace digital ante ruido y distorsión.  
     
   BER \= (bits erróneos) / (bits totales transmitidos)

**Comparación:** Para el mismo nivel de SNR (relación señal-ruido) **fase \< frec \< amplitud**

* **PSK (fase)** tiene el mejor desempeño (menor BER) porque usa toda la energía de la señal para transportar información en la fase, y la detección coherente de fase es más inmune al ruido.  
* **FSK (frecuencia)** queda en el medio.  
* **ASK (amplitud)** es el más vulnerable, porque el ruido afecta directamente la amplitud, que es donde está codificada la info (además, en ASK un "0" suele representarse con ausencia de señal, más susceptible a confundirse con ruido).

4) 

<img width="463" height="275" alt="Captura de pantalla 2026-08-19 102744" src="https://github.com/user-attachments/assets/9bb29320-0b66-4717-9451-41ebffbb221e" />

**c)** El router está configurado como un dispositivo Wireless-N Tri-Band (WRT300N), capaz de operar en la banda de 2.4 GHz y 5 GHz. Sin embargo, la red inalámbrica configurada para este trabajo (SSID "wi-fi") opera específicamente en la banda de **2.4 GHz**, canal 1, con una frecuencia central de **2.412 GHz**.   
Esta frecuencia corresponde a la región de **microondas** del espectro electromagnético, dentro de la banda **UHF** (Ultra High Frequency, 300 MHz – 3 GHz según la clasificación de la ITU), específicamente en la sub-banda ISM de 2.4 GHz, de uso libre y ampliamente utilizada para redes Wi-Fi, Bluetooth y otros dispositivos de corto alcance. 

g) Se comprobó la conectividad entre PC1 y Laptop0 mediante el comando *ping*, obteniendo los siguientes resultados: 

| Equipo | Tipo de conexión | Dirección IP |
| :---: | :---: | :---: |
| PC1 | Cableada (FastEthernet, DHCP) | 192.168.0.105 |
| Laptop0 | Inalámbrica (WI-FI, DHCP) | 192.168.0.101 |

**PC1**   
<img width="472" height="215" alt="Captura de pantalla 2026-08-13 012324" src="https://github.com/user-attachments/assets/3bf67055-42fb-4322-9f49-aaa8e7ff24da" />

**Laptop0**  
<img width="468" height="212" alt="Captura de pantalla 2026-08-13 012450" src="https://github.com/user-attachments/assets/1fa3db93-1bf3-4342-999e-ed8bbd4e229b" />


Ambos resultados confirman conectividad plena dentro de la red local, sin pérdida de paquetes (0% en los dos casos) tanto para el enlace cableado como para el inalámbrico en condiciones ideales de cercanía al router.

El enlace cableado (PC1) tuvo un RTT promedio de 8 ms, y el inalámbrico (Laptop0) de 3 ms, ambos con valores bajos y estables al tratarse de una posición cercana al router y sin obstáculos. 

h)  
se ubicó una notebook adicional **(Laptop1, IP 192.168.0.106, conexión Wi-Fi por DHCP)** en tres posiciones distintas respecto del área de cobertura inalámbrica visualizada (círculo de degradado púrpura), realizando un *ping* hacia PC1   
**Posición 1 – Dentro del núcleo de cobertura  (Laptop0, cerca del router).**  
Resultado: 4/4 paquetes recibidos, 0% de pérdida, RTT entre 14 y 35 ms (promedio 20 ms). La conexión fue estable.

<img alt="Captura de pantalla 2026-08-13 022750" src="https://github.com/user-attachments/assets/acc5098f-a8ff-46f1-9ec3-e282eae32b30" width="500" />

Command Prompt Laptop0  
<img width="500" alt="Captura de pantalla 2026-08-13 023308" src="https://github.com/user-attachments/assets/519cad98-0e85-4583-a4c5-1a4f0aa97b12" />

**Posición 2 – Cerca del router, fuera del edificio (Laptop1).**  
Resultado: 4/4 paquetes recibidos, 0% de pérdida, RTT entre 14 y 26 ms (promedio 19 ms). La conexión se mantuvo igualmente sólida.

<img width="500" alt="Captura de pantalla 2026-08-13 013600" src="https://github.com/user-attachments/assets/94111255-7d57-447c-a564-81a1a6faf402" />

Command Prompt Laptop1  
<img width="500" height="206" alt="Captura de pantalla 2026-08-13 014651" src="https://github.com/user-attachments/assets/e940e46b-3431-424d-a8b0-51512e7e2224" />

**Posición 3 – Borde del área cobertura (Laptop1).**    
Resultado: 2/4 paquetes recibidos, 50% de pérdida, RTT entre 4 y 23 ms (promedio 13 ms), con dos solicitudes agotando el tiempo de espera (*Request timed out*). Conexión Intermitente.

<img width="500" height="350" alt="Captura de pantalla 2026-08-13 020703" src="https://github.com/user-attachments/assets/7785d6af-ed04-4664-a5b9-4dc19bb0dcce" />

Command Prompt Laptop1  
<img width="500" height="205" alt="Captura de pantalla 2026-08-13 023745" src="https://github.com/user-attachments/assets/f41b60c7-5348-4e09-a985-42fab81cc400" />

**Posición 4 – Fuera del área de cobertura (Laptop1).**   
Resultado: 0/4 paquetes recibidos, 100% de pérdida, con las cuatro solicitudes agotando el tiempo de espera. La señal Wi-Fi no llegaba con potencia suficiente para establecer comunicación 

<img width="500" height="350" alt="Captura de pantalla 2026-08-13 013738" src="https://github.com/user-attachments/assets/c276a943-e371-450a-9d63-d1d3f163ba74" />

Command Prompt Laptop1  
<img width="500" height="170" alt="image" src="https://github.com/user-attachments/assets/754872ed-cf48-4b3e-baa7-d9c5947c2fa2" />

Resumen de las mediciones realizadas :

| Equipo | Conexión | Ubicación | paquetes recibidos | Pérdida | Estado |
| :---: | :---: | :---: | :---: | :---: | :---: |
| PC1 | Cableada (DHCP)  | \- | 4/4 | 0% | Conexión sólida |
| Laptop0 | WI-FI (DHCP)  | Posición 1 | 4/4 | 0% | Conexión sólida |
| Laptop1 | WI-FI (DHCP)  | Posición 2 | 4/4 | 0% | Conexión Sólida |
| Laptop1 | WI-FI (DHCP)  | Posición 3 | 2/4 | 50% | Conexión intermedia |
| Laptop1 | WI-FI (DHCP)  | Posición 4 | 0/4 | 100% | Sin conexión |

**Conclusión:** En la posición cercana al router, dentro del radio de cobertura wifi, la conexión se mantuvo estable con 0% de pérdida de paquetes y tiempos de respuesta bajos (14-26ms). Al alejar la notebook fuera del alcance de la señal, el 100% de los paquetes se perdió, indicando que la señal wifi no llega a esa distancia — probablemente por atenuación de la potencia de la señal con la distancia y/o la interposición de paredes/obstáculos entre el dispositivo y el router.  


# Trabajo Práctico Nº 5

**Universidad Nacional de Córdoba**
Facultad de Ciencias Exactas, Físicas y Naturales
Cátedra de Redes de Computadoras

**Grupo:** "Los simuLANdores"

**Alumnos:**

- Barrio, Rafael
- Chesta, Santino
- Garay, Alexis Tomás
- Guzmán Gonzalez, Pedro
- Vera Gonzalez, Fernando Agustín
- Martin, Agostina Rocio
- Zucchella Paz, Valentino

**Profesor:** Henn Santiago Martin

---

## 1) ICMP y primer contacto con Wireshark

### a) ¿Qué es ICMP y para qué se usa? ¿Transporta datos de aplicación como lo hacen TCP o UDP?

ICMP es un protocolo de la capa de red (modelo OSI) que sirve para reportar errores y hacer diagnóstico en una red IP. Y no, no transporta datos de aplicación, solo reporta.

### b) ¿Qué relación tiene con el IP? ¿Viaja dentro de IP, al lado de IP o debajo de IP? ¿Cómo sabe el receptor que el contenido de un paquete IP es ICMP?

La relación que tiene con IP es que IP manda paquetes sin garantías y sin avisar si algo sale mal; en cambio, ICMP es lo que le permite a la red avisarle al origen si sucede un error.

ICMP viaja dentro de IP: un mensaje ICMP es el payload de un paquete IP.

El receptor reconoce que el contenido de un paquete IP es ICMP debido a que el encabezado IP trae un campo llamado **Protocol** que dice qué hay adentro del paquete. Si ese campo vale 1, el contenido es ICMP.

### c) ¿Qué hace ping? ¿Qué son un Echo Request y un Echo Reply? ¿Qué campos de ICMP permiten distinguirlos?

Ping lo que hace es verificar si puedo llegar a otro host por la red y cuánto tarda en responder.

Un Echo Request y un Echo Reply son mensajes ICMP. Para distinguirlos se debe mirar el "Tipo" del mensaje.

### d) ¿Qué información mínima contiene un mensaje ICMP de tipo Echo?

La información mínima que contiene un mensaje ICMP de tipo Echo es:

- Tipo (si el mensaje es de pedido o respuesta)
- Identificador (de quién es el mensaje)
- Sequence number
- Checksum
- Data

**Echo Request y sus detalles:**

| Capa | Dirección/identificador origen | Dirección/identificador destino | ¿Qué campo indica qué protocolo viene adentro? |
|---|---|---|---|
| Ethernet II | TPLink_2d:eb:7c (78:20:51:d2:eb:7c) | HuaweiTechno_98:98:42 (b8:85:7b:98:98:42) | El campo Type indica que viene el protocolo IPv4 (0x0800) |
| Internet Protocol Version 4 | 192.168.100.5 | 192.168.100.1 | Protocol: ICMP (1) |
| Internet Control Message Protocol | No tiene | No tiene | El campo Type: 8 (Echo (ping) request) |
| Datos / payload | No aplica | No aplica | No aplica: es el contenido final del mensaje |

---

## Simulación 1

Responder, justificando con la captura (una captura de pantalla con el campo resaltado vale más que el valor copiado):

### A) La MAC destino del Echo Request enviado a 8.8.8.8, ¿es la MAC de 8.8.8.8? ¿De qué equipo es? Compárenla con la MAC destino del ping al gateway. ¿Qué conclusión sacan sobre el alcance de una dirección MAC frente al de una dirección IP?

No, no es la MAC de 8.8.8.8, es la interfaz LAN del router. La MAC de destino es la misma para las 2 solicitudes de ping, y el equipo al que pertenece es el "router". La conclusión con respecto al alcance es que IP me permite enviar una trama a través de internet. En cambio, con MAC, al enviar una trama el destino se encuentra dentro de mi propia red.

```text
Frame 502: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface \Device\NPF_{A53AD2B2-5E40-4D3D-BD...
Ethernet II, Src: TPLink_d2:eb:7c (78:20:51:d2:eb:7c), Dst: HuaweiTechno_98:98:42 (b8:85:7b:98:98:42)
Internet Protocol Version 4, Src: 192.168.100.5, Dst: 8.8.8.8
Internet Control Message Protocol

Frame 363: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface \Device\NPF_{A53AD2B2-5E40-4D3D-BD...
Ethernet II, Src: TPLink_d2:eb:7c (78:20:51:d2:eb:7c), Dst: HuaweiTechno_98:98:42 (b8:85:7b:98:98:42)
Internet Protocol Version 4, Src: 192.168.100.5, Dst: 192.168.100.1
Internet Control Message Protocol
```

### B) Comparen un Echo Request con su Echo Reply (Wireshark los vincula en el campo [Response frame:...]). Hagan una lista de los campos que cambian y de los que se mantienen en Ethernet, IP e ICMP. ¿Por qué tiene sentido cada cambio? ¿Por qué el identificador y el número de secuencia se mantienen?

**Comparación entre Echo Request y Echo Reply:**

| Capa | Cambian | Se mantiene |
|---|---|---|
| Ethernet | Source MAC and destination MAC | Type |
| IP | IP origen e IP destino, identification, time to live (TTL) y header checksum | Version, header length, protocol |
| ICMP | Type, checksum | Identification, sequence number y data |

Tiene sentido que cambien, debido a que un mensaje es de pedido y otro de respuesta.

El identificador y la secuencia se mantienen porque permiten identificar qué respuesta corresponde a tal pedido.

### C) ¿Dónde está el payload de ping? ¿Cuántos bytes tiene y qué contiene? ¿Es igual en el Reply? Si en el grupo hay una computadora con Windows y otra con Linux, compárenlos: ¿qué les sugiere que sean distintos?

El payload del ping se encuentra en la capa ICMP, en el campo Data. Está conformado por 32 bytes y contiene el siguiente texto: `abcdefghijklmnopqrstuvwabcdefghi`.

Sí, es el mismo en el Reply, ya que el protocolo ICMP obliga al que responde a devolver los datos del Echo Request sin modificarlos.

```text
Data (32 bytes)
    Data: 6162636465666768696a6b6c6d6e6f7071727374757677616263646566676869
    [Length: 32]

0000  b8 85 7b 98 98 42 78 20  51 d2 eb 7c 08 00 45 00   ..{..Bx Q..|..E.
0010  00 3c 58 76 00 00 80 01  ad 8d c0 a8 64 05 08 08   .<Xv........d...
0020  08 08 08 00 4d 3c 00 01  00 1f 61 62 63 64 65 66   ....M<....abcdef
0030  67 68 69 6a 6b 6c 6d 6e  6f 70 71 72 73 74 75 76   ghijklmn opqrstuv
0040  77 61 62 63 64 65 66 67  68 69                     wabcdefg hi
```

Al compararlos, cambia la Data, el tamaño de la Data y el TTL. Suponemos que son distintos debido a que cambia el sistema operativo y cada uno elige según sus preferencias por defecto.

### D) ¿Qué valor de TTL tiene el Echo Request que ustedes enviaron? ¿Y el Reply que llegó de 8.8.8.8? ¿Por qué no son iguales? (Pista: investiguen qué hace un router con el TTL.)

El Echo Request tiene TTL igual a 128 (valor inicial que asigna Windows al armar el paquete) y el Echo Reply llegó con TTL igual a 117.

No son iguales porque son paquetes distintos: el Reply lo genera 8.8.8.8 con su propio TTL inicial (asumimos 128, el valor típico inmediatamente superior a 117) y cada router que atraviesa le resta 1 antes de reenviarlo. Entonces 128 − 117 = 11, lo que indica que el Reply atravesó aproximadamente 11 routers hasta llegar a nuestra PC.

| Echo Request | Echo Reply |
|---|---|
| Time to Live: 128 | Time to Live: 117 |
| Protocol: ICMP (1) | Protocol: ICMP (1) |
| Header Checksum: 0xaeaf [validation disabled] | Header Checksum: 0x1104 [validation disabled] |
| [Header checksum status: Unverified] | [Header checksum status: Unverified] |
| Source Address: 192.168.100.5 | Source Address: 8.8.8.8 |
| Destination Address: 8.8.8.8 | Destination Address: 192.168.100.5 |
| [Stream index: 19] | [Stream index: 19] |
| Type: 8 (Echo (ping) request) | Type: 0 (Echo (ping) reply) |

### E) Dibujen la encapsulación del paquete que eligieron como "cajas dentro de cajas", indicando para cada caja qué tamaño en bytes tiene según Wireshark.

**Encapsulación de un Echo**

```text
┌──────────────────────────────── Trama Ethernet II - 74 bytes ────────────────────────────────┐
│ ┌─────────────┐ ┌──────────────────────── Paquete IPv4 - 60 bytes ─────────────────────────┐ │
│ │  Cabecera   │ │ ┌─────────────┐ ┌──────────────── Mensaje ICMP - 40 bytes ─────────────┐ │ │
│ │  Ethernet   │ │ │ Cabecera IP │ │ ┌──────────┐ ┌─────────────────────────────────────┐ │ │ │
│ │  14 bytes   │ │ │  20 bytes   │ │ │ Cabecera │ │           Data (payload)            │ │ │ │
│ │             │ │ │             │ │ │   ICMP   │ │              32 bytes               │ │ │ │
│ │             │ │ │             │ │ │ 8 bytes  │ │                                     │ │ │ │
│ │             │ │ │             │ │ └──────────┘ └─────────────────────────────────────┘ │ │ │
│ └─────────────┘ │ └─────────────┘ └──────────────────────────────────────────────────────┘ │ │
│                 └───────────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Cabecera Ethernet II - 14 bytes**

| MAC destino | MAC origen | EtherType (0x0800) |
|---|---|---|
| 6 bytes | 6 bytes | 2 bytes |

**Cabecera IPv4 - 20 bytes**

| Ver+IHL | DSCP/ECN | Total Length | Identif. | Flags+Frag.off. | TTL | Proto (ICMP) | Header Checksum | IP origen | IP destino |
|---|---|---|---|---|---|---|---|---|---|
| 1 byte | 1 byte | 2 bytes | 2 bytes | 2 bytes | 1 byte | 1 byte | 2 bytes | 4 bytes | 4 bytes |

**Cabecera ICMP - 8 bytes**

| Type (8) | Code | Checksum | Identifier | Seq. number |
|---|---|---|---|---|
| 1 byte | 1 byte | 2 bytes | 2 bytes | 2 bytes |

---

## 2) ARP: de una IP a una dirección MAC

En el punto anterior la trama Ethernet ya tenía una MAC destino. Pero ping solo conoce una IP. ¿De dónde salió esa MAC?

La MAC destino salió del protocolo ARP. Como la PC solo conoce la IP del gateway, envía por broadcast una consulta ARP del tipo "¿A quién pertenece esta IP?", y la respuesta a esa consulta es la MAC destino.

### a) ¿Qué problema resuelve ARP? ¿En qué capa lo ubicarían y por qué es discutible?

El problema que resuelve es que me permite conocer la MAC destino de determinada IP. Lo ubicamos en la capa 2 (enlace), porque viaja dentro de una trama Ethernet y opera dentro de la red local. Es discutible porque maneja direcciones IP y existe para que la capa de red pueda entregar paquetes, por lo que también podría considerarse capa 3 (red).

### b) ¿Qué es un ARP Request y un ARP Reply? ¿A quién se envía cada uno?

Un ARP Request es un pedido para conocer la dirección MAC de destino según su IP. Se envía a todos los equipos de la red.

Un ARP Reply es la respuesta, es decir, que se obtuvo la dirección MAC de destino. Se lo envía solo a quien preguntó por esa determinada IP.

### c) ¿Qué es la caché ARP y por qué existe?

La caché ARP es un espacio de memoria que guarda en cada equipo los pares IP → MAC que fue aprendiendo mediante ARP. Existe para evitar repetir la consulta en cada envío de paquete, lo que mejora la eficiencia y la velocidad.

### d) Traten de responder con sus palabras: "Tengo la IP de una máquina de mi red local. ¿Cómo sé a qué dirección MAC debo enviarle la trama?"

Primero consulto mi caché ARP para ver si ya conozco la MAC de esa IP. Si no está, necesito hacer un pedido ARP Request con la IP de la máquina. Una vez que obtuve la dirección MAC de esa IP mediante ARP Reply, a continuación guardo en caché ese par IP → MAC y me encuentro en condiciones de enviar la trama a esa MAC.

### e) Ver la caché ARP de su computadora y buscar la entrada del gateway

```text
Interfaz: 192.168.56.1 --- 0x3
  Dirección de Internet     Dirección física      Tipo
  192.168.56.255            ff-ff-ff-ff-ff-ff     estático
  224.0.0.22                01-00-5e-00-00-16     estático
  224.0.0.251               01-00-5e-00-00-fb     estático
  224.0.0.252               01-00-5e-00-00-fc     estático
  239.255.255.250           01-00-5e-7f-ff-fa     estático

Interfaz: 192.168.100.5 --- 0xc
  Dirección de Internet     Dirección física      Tipo
  192.168.100.1             b8-85-7b-98-98-42     dinámico
  192.168.100.255           ff-ff-ff-ff-ff-ff     estático
  224.0.0.22                01-00-5e-00-00-16     estático
  224.0.0.251               01-00-5e-00-00-fb     estático
  224.0.0.252               01-00-5e-00-00-fc     estático
  239.255.255.250           01-00-5e-7f-ff-fa     estático
  255.255.255.255           ff-ff-ff-ff-ff-ff     estático
```

Se observa que sí, la MAC asociada al gateway coincide con la MAC de destino visualizada anteriormente.

**Tabla que analiza ARP Request y ARP Reply:**

| Campo | ARP Request | ARP Reply |
|---|---|---|
| MAC destino (Ethernet) | ff:ff:ff:ff:ff:ff | 78:20:51:d2:eb:7c |
| MAC origen (Ethernet) | 78:20:51:d2:eb:7c | be:f5:83:ef:4e:01 |
| Opcode | request (1) | reply (2) |
| Sender MAC address | 78:20:51:d2:eb:7c | 78:20:51:d2:eb:7c |
| Sender IP address | 192.168.100.5 | 192.168.100.26 |
| Target MAC address | 00:00:00:00:00:00 | 78:20:51:d2:eb:7c |
| Target IP address | 192.168.100.253 | 192.168.100.5 |

---

## Simulación 2

### a) ¿Por qué el Request va a una dirección broadcast y el Reply no? ¿Qué valor tiene Target MAC address en el Request y por qué?

El ARP Request se envía por broadcast (MAC destino `ff:ff:ff:ff:ff:ff`) porque el equipo que pregunta no sabe cuál de los equipos de la LAN tiene esa IP ni cuál es su MAC, entonces le consulta a todos y solo responde el dueño de la IP. El ARP Reply, en cambio, se envía por unicast, porque el Request ya incluía la IP y la MAC de quien preguntó, por lo que el que responde sabe a quién entregarle la respuesta. El Target MAC address del Request vale `00:00:00:00:00:00` porque es justamente el dato que se está tratando de averiguar; como todavía no se conoce, se lo rellena con ceros.

### b) En el encabezado Ethernet de la trama ARP, ¿qué valor tiene el campo Type? ¿Hay un encabezado IP? ¿Qué les dice eso sobre dónde "vive" ARP?

El valor del campo Type es `0x0806`. No, no hay un encabezado de IP. Nos dice que ARP va dentro de la trama Ethernet, como si fuera un protocolo del mismo nivel que IP, lo cual sugiere que ARP no depende de la capa de red para viajar y que solo funciona dentro de la red local.

```text
Frame 61: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface \Device\NPF_{A53AD2B2-5E40-4D3D-BDC1-33...
Ethernet II, Src: TPLink_d2:eb:7c (78:20:51:d2:eb:7c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
    Source: TPLink_d2:eb:7c (78:20:51:d2:eb:7c)
    Type: ARP (0x0806)
    [Stream index: 3]
Address Resolution Protocol (request)
    Hardware type: Ethernet (1)
    Protocol type: IPv4 (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: request (1)
    Sender MAC address: TPLink_d2:eb:7c (78:20:51:d2:eb:7c)
    Sender IP address: 192.168.100.5
    Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Target IP address: 192.168.100.253
```

### c) Con la Opción A (IP inexistente): ¿cuántos ARP Request aparecieron? ¿Hubo Reply? ¿Apareció algún ICMP Echo Request en la captura? Expliquen por qué.

La cantidad de ARP Request que aparecieron fueron 4. No, no hubo ningún Reply porque al hacer el pedido a la IP 192.168.100.253 y esta no existir, no se puede obtener una respuesta de esa dirección. No, no apareció ningún ICMP Echo Request en la captura porque para enviarlo se necesita la MAC de destino de la IP 192.168.100.253, que se obtiene mediante ARP.

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 11 | 2.294736 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 21 | 3.296815 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 29 | 4.294951 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 38 | 5.295070 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |

### d) Volvieron a hacer ping al mismo destino un minuto después: ¿apareció ARP de nuevo? Revisen la caché ARP. ¿Qué ventaja tiene la caché y qué problema podría causar si una entrada quedara vieja?

Sí, al repetir el ping a 192.168.100.253 un minuto después volvieron a aparecer ARP Request. Como esa IP no pertenece a ningún equipo, nadie respondió y no se guardó ninguna entrada en la caché ARP, por lo que la PC tuvo que volver a preguntar.

Filtro: `arp`

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 103 | 11.413171 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 108 | 12.415958 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 110 | 13.413379 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 117 | 14.413495 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 375 | 49.289162 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 376 | 49.919458 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 383 | 50.919568 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 390 | 51.921544 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 391 | 52.908320 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |
| 392 | 53.908426 | TPLink_d2:eb:7c | Broadcast | ARP | 42 | Who has 192.168.100.253? Tell 192.168.100.5 |

La ventaja que tiene la caché es que, al repetir el ping a una IP existente, no se repite el broadcast en cada envío, ahorrando tráfico y tiempo.

El problema que podría causar es que, si el equipo de esa IP se reemplaza por otro con otra MAC, las tramas se seguirán enviando a la MAC antigua, perdiendo información.

---

## 3) TCP y UDP "a mano" con ncat

### a) ¿Qué significa "establecer una conexión"? ¿Dónde "existe" una conexión TCP: en los cables, en los routers o en los extremos?

Establecer una conexión significa crear y sincronizar un estado compartido entre los dos extremos de la comunicación. La conexión existe en los extremos.

### b) ¿Qué es un puerto? ¿Qué identifica el par (IP, puerto)?

Un puerto es un número de 16 bits que va en la cabecera de TCP e identifica qué programa dentro de un equipo debe recibir los datos. El par (IP, puerto) identifica un extremo de comunicación (un programa específico, corriendo en un equipo específico).

### c) ¿Qué significa que un proceso esté "escuchando" en un puerto?

Significa que un proceso está asociado a un puerto y listo para aceptar conexiones entrantes. Es decir, que el puerto está esperando una conexión, sin tener ninguna conexión abierta todavía.

---

## Simulación 3

### a) ¿Qué pasó en la red cuando ejecutaron el comando del cliente, antes de escribir el primer mensaje? Compárenlo con TCP.

En TCP, antes de enviar el primer mensaje por la terminal del "Cliente", hubo 3 paquetes en los distintos puertos:

1. Src Port: 50781, Dst Port: 12000, Seq: 0, flags SYN y ACK activado. El "Cliente" propone iniciar la conexión.
2. Src Port: 12000, Dst Port: 50781, Seq: 0, flags SYN y ACK activado. El "Servidor" acepta y propone su propio número de secuencia.
3. Src Port: 50781, Dst Port: 12000, Seq: 1, flag ACK activado. El "Cliente" confirma, y la conexión queda establecida.

Filtro: `tcp.port==12000`

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 117 | 30.502827 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | 50781 → 12000 [SYN] Seq=0 Win=8192 Len=0 MSS=65495 WS=256 SACK_PERM |
| 118 | 30.502859 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | 12000 → 50781 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=65495 WS=256 SA… |
| 119 | 30.502877 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50781 → 12000 [ACK] Seq=1 Ack=1 Win=525568 Len=0 |
| 198 | 52.227670 | 127.0.0.1 | 127.0.0.1 | TCP | 55 | 50781 → 12000 [PSH, ACK] Seq=1 Ack=1 Win=525568 Len=11 |

En cambio, en UDP no se capturó ningún paquete al ejecutar el cliente; solo apareció tráfico cuando se envió un mensaje.

Filtro: `udp.port==12001` → sin paquetes.

Servidor:

```text
C:\Users\Agustin\Downloads\ncat-portable-5.59BETA1\ncat-portable-5.59BETA1>ncat -v -u -l 12001
Ncat: Version 5.59BETA1 ( http://nmap.org/ncat )
Ncat: Listening on 0.0.0.0:12001
```

Cliente:

```text
C:\Users\Agustin\Downloads\ncat-portable-5.59BETA1\ncat-portable-5.59BETA1>ncat -v -u 127.0.0.1 12001
Ncat: Version 5.59BETA1 ( http://nmap.org/ncat )
Ncat: Connected to 127.0.0.1:12001.
```

### b) ¿Cuántos datagramas generó cada mensaje? ¿Hay algo parecido a un ACK?

En UDP se produjo 1 datagrama por cada mensaje. No hay nada parecido a un ACK: el servidor no manda ninguna confirmación.

### C) Comparen el encabezado UDP con el encabezado TCP de un segmento con datos: ¿qué campos tiene cada uno? ¿Cuántos bytes ocupa cada encabezado?

El encabezado de UDP ocupa 8 bytes, sus campos son:

- Source Port
- Destination Port
- Length
- Checksum

El encabezado de UDP ocupa 20 bytes, sus campos son:

- Source Port
- Destination Port
- Sequence Number
- Acknowledgment Number
- Flags
- Window
- Urgent Pointer
- Checksum

### D) ¿Qué pasó en la red al cerrar el cliente con Ctrl+C? ¿Y en TCP?

Al cerrar el cliente en UDP, no apareció ningún paquete nuevo en la captura.

En cambio, en TCP, después de mi último mensaje, apareció 1 paquete en la captura, con los flags "RST y ACK", indicando que la conexión se cerró de forma abrupta.

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 620 | 161.016524 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50759 → 12000 [RST, ACK] Seq=10 Ack=13 Win=0 Len=0 |

### e) Para enviar la misma frase, ¿cuántos paquetes necesitaron en total con TCP y cuántos con UDP? ¿Qué "compran" con los paquetes extra de TCP?

Para enviar la misma frase, en TCP necesitamos en total 2 paquetes: el primer paquete lleva los datos, pero no incluye la confirmación de sí mismo. En el segundo paquete llegó la confirmación de que el receptor recibió ese paquete.

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 198 | 52.227670 | 127.0.0.1 | 127.0.0.1 | TCP | 55 | 50781 → 12000 [PSH, ACK] Seq=1 Ack=1 Win=525568 Len=11 |
| 199 | 52.227701 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50781 [ACK] Seq=1 Ack=12 Win=525568 Len=0 |

En UDP solo se necesita 1 paquete. Ese paquete solo contiene la información del mensaje. El protocolo no informa la confirmación del mismo.

Filtro: `udp.port==12001`

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 828 | 221.157433 | 127.0.0.1 | 127.0.0.1 | LLC | 53 | I P, N(R)=48, N(S)=54; DSAP 0x68 Individual, SSAP 0x6e Response |

Los paquetes extra de TCP me brindan información sobre si el paquete se recibió con éxito o no. Es una ventaja, ya que me permite enterarme si sucede un error; en el caso de que haya sucedido un error, el emisor retransmite el paquete.

### f) ¿Y si nadie escucha? Con Wireshark capturando en loopback y el filtro `tcp.port == 12000 || udp.port == 12001 || icmp`, sin servidores corriendo:

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 69 | 17.870683 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | 50799 → 12000 [SYN] Seq=0 Win=8192 Len=0 MSS=65495 WS=256 SACK_PERM |
| 70 | 17.870699 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50799 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0 |
| 71 | 18.377933 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | [TCP Port numbers reused] 50799 → 12000 [SYN] Seq=0 Win=8192 Len=0 MSS=… |
| 72 | 18.377949 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50799 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0 |
| 77 | 18.877983 | 127.0.0.1 | 127.0.0.1 | TCP | 52 | [TCP Port numbers reused] 50799 → 12000 [SYN] Seq=0 Win=8192 Len=0 MSS=… |
| 78 | 18.877998 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50799 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0 |
| 833 | 222.942223 | 127.0.0.1 | 127.0.0.1 | LLC | 35 | [Malformed Packet] |
| 834 | 222.942242 | 127.0.0.1 | 127.0.0.1 | ICMP | 63 | Destination unreachable (Port unreachable) |

Se observa en TCP que el cliente intenta abrir la conexión, pero no se pudo establecer ya que el destino denegó dicha conexión debido a que no hay ningún puerto "escuchando".

En UDP, al no haber conexión, el cliente no envía nada hasta que se escribe un mensaje. Al enviarlo, en la captura se observa que un datagrama llega a un puerto sin servidor y el sistema destino responde con un mensaje ICMP "Destination unreachable (Port unreachable)". Este aviso pertenece al protocolo ICMP, que informa el error.

---

## 4) Servidor TCP mínimo - TP5 Redes de Computadoras

### C)

Servidor:

```text
[servidor TCP] conexión aceptada desde 127.0.0.1:50961
[servidor TCP] recibido (13 bytes): 'Hola servidor'
[servidor TCP] respuesta enviada: 'Recibido: Hola servidor'
[servidor TCP] el cliente cerró la conexión

C:\Users\Agustin\Downloads>tcp_server.py
[servidor TCP] escuchando en 127.0.0.1:12000 ...
[servidor TCP] conexión aceptada desde 127.0.0.1:50963
[servidor TCP] recibido (13 bytes): 'Hola servidor'
[servidor TCP] respuesta enviada: 'Recibido: Hola servidor'
[servidor TCP] el cliente cerró la conexión

C:\Users\Agustin\Downloads>
```

Cliente:

```text
C:\Users\Agustin\Downloads>tcp_client.py
[cliente TCP] conectado a 127.0.0.1:12000 desde 127.0.0.1:50961
[cliente TCP] enviado: 'Hola servidor'
[cliente TCP] respuesta (23 bytes): 'Recibido: Hola servidor'

C:\Users\Agustin\Downloads>tcp_client.py
[cliente TCP] conectado a 127.0.0.1:12000 desde 127.0.0.1:50963
[cliente TCP] enviado: 'Hola servidor'
[cliente TCP] respuesta (23 bytes): 'Recibido: Hola servidor'

C:\Users\Agustin\Downloads>
```

Captura (filtro `tcp.port==12000`):

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 37 | 8.982901 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | 50963 → 12000 [SYN] Seq=0 Win=8192 Len=0 MSS=65495 WS=256 SACK_PERM |
| 38 | 8.982933 | 127.0.0.1 | 127.0.0.1 | TCP | 56 | 12000 → 50963 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=65495 WS=256 SA… |
| 39 | 8.982951 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50963 → 12000 [ACK] Seq=1 Ack=1 Win=525568 Len=0 |
| 40 | 8.983150 | 127.0.0.1 | 127.0.0.1 | TCP | 57 | 50963 → 12000 [PSH, ACK] Seq=1 Ack=1 Win=525568 Len=13 |
| 41 | 8.983168 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50963 [ACK] Seq=1 Ack=14 Win=525568 Len=0 |
| 42 | 8.983660 | 127.0.0.1 | 127.0.0.1 | TCP | 67 | 12000 → 50963 [PSH, ACK] Seq=1 Ack=14 Win=525568 Len=23 |
| 43 | 8.983682 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50963 → 12000 [ACK] Seq=14 Ack=24 Win=525568 Len=0 |
| 44 | 8.984922 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50963 → 12000 [FIN, ACK] Seq=14 Ack=24 Win=525568 Len=0 |
| 45 | 8.984946 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50963 [ACK] Seq=24 Ack=15 Win=525568 Len=0 |
| 46 | 8.985300 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 12000 → 50963 [FIN, ACK] Seq=24 Ack=15 Win=525568 Len=0 |
| 47 | 8.985326 | 127.0.0.1 | 127.0.0.1 | TCP | 44 | 50963 → 12000 [ACK] Seq=15 Ack=25 Win=525568 Len=0 |

### D)

| Llamada | ¿Dónde se ejecuta? | ¿Genera tráfico? | Segmentos que observan |
|---|---|---|---|
| `socket()` | servidor y cliente | No | ninguno |
| `bind()` | servidor | No | ninguno |
| `listen()` | servidor | No | ninguno |
| `connect()` | cliente | Sí | [SYN], [SYN, ACK] y [ACK] (handshake) |
| `accept()` | servidor | No | ninguno |
| `sendall()` | servidor | Sí | [PSH, ACK] y [ACK] |
| `recv()` | servidor | No | ninguno |
| `close()` | ambos | Sí | [FIN, ACK] y [ACK] por parte del cliente y servidor |

---

**Link al doc:** <https://docs.google.com/document/d/1UChoS8mlFiWt52pDY3ogPcIT01mUlF8xf05uMKBgKvc/edit?tab=t.0>

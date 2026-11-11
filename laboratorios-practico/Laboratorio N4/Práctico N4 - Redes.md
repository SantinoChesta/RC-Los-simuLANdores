<div align="center">
<img width="200" src="imagenes/logoUNC.png" />
<br><br>

# UNIVERSIDAD NACIONAL DE CÓRDOBA

### FACULTAD DE CIENCIAS EXACTAS, FÍSICAS Y NATURALES

### CÁTEDRA DE REDES DE COMPUTADORAS

## TRABAJO PRÁCTICO N°4

**Grupo: "Los simuLANdores"**

</div>

--- 

**Alumnos:**
- Barrio, Rafael
- Chesta, Santino
- Garay, Alexis Tomás
- Guzmán Gonzalez, Pedro
- Vera, Agustín
- Martin, Agostina Rocio
- Zucchella Paz, Valentino


**Profesor:** Ing. Santiago Martin Henn (laboratorio)

---

## Consignas

### 1) Alcance de Redes y Virtualización

- a) Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda.

- b) ¿Qué es una VLAN? ¿Cómo se clasifican?

- c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?

- d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?

---

### 2) Implementaremos la siguiente topología en Packet Tracer
<img width="600" src="imagenes/Picture1.png" />
<br><br>
Con la siguiente Tabla de ruteo:    

<img width="600" src="imagenes/Picture2.png" />

#### a) Desde cada computadora, ingresar a la terminal y configurar los switch. Nombrar a los mismos sw1 y sw2 respectivamente. Ayuda: investigar los comandos necesarios online si no te acordás, por ejemplo, para cambiar el nombre del switch:

```
switch>
switch>en
switch#conf t
switch(config)#hostname nombre
```

#### b) Asignar contraseñas privilegiadas, de consola y vty. Ayuda:

```
enable secret contrasena_exec
line console 0
password contrasena_consola
login
exit
line vty 0 15
password contrasena_vty
login
exit
```

#### c) Encriptar las contraseñas (Ayuda: utilizar service password-encryption)

#### d) Configurar las redes VLAN para ambos switch según la tabla de direcciones provista. Ayuda:
```
interface vlan 1
ip address <IP_address> <subnet_mask>
no shutdown
exit
```

#### e) Desconectar todas las interfaces que no estén siendo utilizadas (Ayuda: podés ver las interfaces utilizando show ip interface brief)

#### f) Guardar la configuración (write memory)

#### g) Testear comunicación usando pings entre las computadoras.

#### h) Crear VLANs en ambos switches. Ayuda:

```
sw1(config)# vlan 10
sw1(config-vlan)# name Laboratorio
sw1(config-vlan)# vlan 20
sw1(config-vlan)# name Bar
sw1(config-vlan)# vlan 99
sw1(config-vlan)# name Management
sw1(config-vlan)# end
```

#### i) Utilizar show vlan brief para visualizar la lista de VLANs en alguno de los switch. ¿Cuál es la VLAN utilizada por defecto?. Colocar el output en el informe.

#### j) Asignar la PC-A a la VLAN Laboratorio. Ayuda:
```
sw1(config)# interface f0/6
sw1(config-if)# switchport mode access
sw1(config-if)# switchport access vlan 10
```
#### k) Desde la VLAN 1, remover la ip de Management y configurarla para funcionar en la VLAN 99 (que configuramos como Management). Ayuda:
```
sw1(config)# interface vlan 1
sw1(config-if)# no ip address
sw1(config-if)# interface vlan 99
sw1(config-if)# ip address IP MASCARA
sw1(config-if)# end
```
#### l) Verificar el estado de la VLAN utilizando show vlan brief y el estado de las interfaces utilizando show ip interface brief. Colocar los output en el informe e interpretar.

#### m) Asignar la PC-B a la VLAN Laboratorio en el sw2. Repetir el inciso k) pero para el sw2.

#### n) Verificar la conectividad entre PC-A y PC-B utilizando pings. Verificar conectividad entre sw1 y sw2 utilizando pings. Interpretar los resultados.

---
### 3) Utilizando lo que aprendimos sobre VLAN, e investigando la configuración de NAT y ACLs, simularemos el despliegue de una red LAN a bordo de una aeronave. La idea es la siguiente, tendremos tres segmentos:


- i) Clase Turista: acceso solo a un sistema de entretenimiento (server local)
- ii) Clase Business: acceso a sistema de entretenimiento e internet.
- iii) Administración: acceso total.

<img width="600" src="imagenes/Picture3.png" />

Podés usar una topología de red como la siguiente:

<img width="400" src="imagenes/Picture4.png" />

Y la siguiente tabla de direccionamiento:

<img width="600" src="imagenes/Picture5.png" />

Pero como ya saben: pueden modificar lo que necesiten en tanto el espíritu de la actividad se mantenga.  

Luego de configurar la red realizarán las siguientes pruebas:  

<img width="600" src="imagenes/Picture6.png" />
<br><br>
Por supuesto pueden simular “internet” con cualquier cosa que responda del lado del ISP.  

Detallar en el informe el diagrama de red (hecho en PT), capturas de pantalla, y conclusiones.

---
## Rta Consigna 1

### a) 

- **PAN** (Personal Area Network): hasta 10 metros aproximadamente, conectar dispositivos de uso personal (celulares, computadoras, auriculares, etc.) mediante tecnologías Bluetooth o inalámbricas.

- **LAN** (Local Area Network): alcance de una oficina, hogar, edificio o conjunto de edificios próximos. Velocidades de transmisión de 10 Mbps a +10 Gbps y bajas tasas de error. Usan cableado UTP, fibra óptica o tecnologías inalámbricas Wi-Fi.

- **CAN** (Campus Area Network): alcance más extenso que una LAN (de 1 a 5 km), como un campus universitario, base militar o complejo industrial. Interconecta múltiples LAN dentro de un mismo recinto. Son de alta velocidad (redes troncales de fibra óptica).

- **MAN** (Metropolitan Area Network): alcance de ciudad (entre 10 y 50 km), al medio de LAN y WAN. Alta capacidad de transmisión a costo reducido para interconectar múltiples sedes corporativas, universidades o instituciones dentro de un área urbana. Un ejemplo son los anillos de fibra óptica urbana.

- **WAN** (Wide Area Network): alcance de áreas geográficas que abarcan regiones, países o continentes, usando infraestructura de empresas de telecomunicaciones. Compuesta por nodos de conmutación (de circuitos o de paquetes). Un ejemplo son las redes de fibra óptica interurbana o los enlaces satelitales.

- **GAN** (Global Area Network): alcance global. Interconecta redes a nivel mundial usando infraestructura satelital, cables submarinos transoceánicos y redes WAN interconectadas. El internet es una de estas.

### b) 
Una VLAN divide lógicamente una red física en varias redes independientes, aunque los dispositivos se conecten al mismo switch.  
Además para comunicarse entre VLANs hace falta enrutamiento (ir al switch), pero dentro de una misma VLAN se puede hacer broadcast sin pasar por el switch.  
Se pueden clasificar según cómo asigna dispositivos dentro de la misma o tambien segun su uso:

**Según cómo se asignan los dispositivos:**
| Tipo de VLAN  | ¿Cómo se asigna?                              | Ejemplo                          |
|---------------|-------------------------------------------------|-----------------------------------|
| Por puerto    | Según el puerto físico del switch               | Puerto 1 → VLAN 10               |
| Por MAC       | Según la dirección MAC del dispositivo          | MAC AA:BB:CC ... → VLAN 10        |
| Por protocolo | Según el protocolo utilizado                    | HTTP → VLAN 10                   |
| Por IP/subred | Según la IP o subred del dispositivo            | 192.168.10.0/24 → VLAN 10        |
| Dinámica      | Automáticamente mediante políticas/sistemas de gestión | Usuario autenticado → VLAN asignada |

**Según su uso:**

| Tipo de VLAN       | Uso                                      | Ejemplo               |
|--------------------|-------------------------------------------|------------------------|
| Data VLAN          | Tráfico normal de usuarios                | PCs, impresoras        |
| Voice VLAN         | Tráfico de telefonía IP                   | Teléfonos VoIP         |
| Management VLAN    | Administración de equipos de red          | Configurar un switch   |
| Native VLAN        | Tráfico sin etiquetar en un enlace trunk  | Tráfico sin tag 802.1Q |
| Default VLAN       | VLAN configurada por defecto              | Normalmente VLAN 1     |

--- 

### c) 
**IEEE 802.1Q** es un estándar de IEEE que define el etiquetado de VLAN en tramas Ethernet, permitiendo a los administradores segmentar una red física en múltiples redes lógicas.  
El etiquetado VLAN consiste en insertar información relacionada con la VLAN (identificador VLAN, VID) dentro de las tramas Ethernet, de modo que los dispositivos de red puedan identificar a qué VLAN pertenece cada trama al atravesar enlaces troncales.  
Como principales ventajas, están el uso eficiente de la infraestructur, mayor seguridad, mejor rendimiento por menos congestion, etc.  
Como desventajas, agrega complejidad de configuracion, dependencia critica de los enlaces troncales, etc.  

---
### d)
El **tagging**, su función más conocida, etiqueta las tramas Ethernet (en header de trama pone tag de 4 bytes), permitiendo que los switches sepan a qué VLAN pertenece cada trama cuando atraviesa enlaces que transportan múltiples VLANs.   
Este encabezado consta principalmente de la prioridad y, más importante, el VID (VLAN ID).

---

## Rta consigna 2

#### a) Desde cada computadora, ingresar a la terminal y configurar los switch. Nombrar a los mismos sw1 y sw2 respectivamente.

<img width="500" src="imagenes/Picture7.png" />  
<br><br>
<img width="550" src="imagenes/Picture8.png" />
<br><br>

---

#### b) Asignar contraseñas privilegiadas, de consola y vty.

Configuración de contraseñas  
<img width="400" src="imagenes/Picture9.png" />  

contraseña de ejecución.  
<img width="250" src="imagenes/Picture10.png" />  
<img width="350" src="imagenes/Picture11.png" />  

Contraseña de consola.    
<img width="300" src="imagenes/Picture12.png" />  
<img width="200" src="imagenes/Picture13.png" />  

Contraseña vty.  
<img width="150" src="imagenes/Picture14.png" />
<br><br>

---

#### c) Encriptar las contraseñas  

<img width="400" src="imagenes/Picture15.png" />
<br><br>

---

#### d) Configurar las redes VLAN para ambos switch según la tabla de direcciones provista.   

<img width="500" src="imagenes/Picture16.png" />  
<br><br>

---

#### e) Desconectar todas las interfaces que no estén siendo utilizadas.  

sw1:  
<img width="550" src="imagenes/Picture17.png" />  

sw2:  
<img width="550" src="imagenes/Picture18.png" />
<br><br>

---

#### f) Guardar la configuración (write memory)
<br>

---

#### g) Testear comunicación usando pings entre las computadoras.  

Ping desde PC-A a PC-B  
<img width="550" src="imagenes/Picture19.png" />   

Ping desde PC-B a PC-A

<img width="550" src="imagenes/Picture20.png" />
<br><br>

---

#### h) Crear VLANs en ambos switches.  

<img width="550" src="imagenes/Picture21.png" />   

<img width="550" src="imagenes/Picture22.png" />
<br><br> 

--- 

#### i) Utilizar show vlan brief para visualizar la lista de VLANs en alguno de los switch. ¿Cuál es la VLAN utilizada por defecto?. Colocar el output en el informe.   

La VLAN por defecto es la VLAN 1 

<img width="550" src="imagenes/Picture23.png" />
<br><br>

---

#### j) Asignar la PC-A a la VLAN Laboratorio.


<img width="400" src="imagenes/Picture24.png" />
<br><br>

---

#### k) Desde la VLAN 1, remover la ip de Management y configurarla para funcionar en la VLAN 99

<img width="550" src="imagenes/Picture26.png" />
<br><br>

---

#### l) Verificar el estado de la VLAN utilizando show vlan brief y el estado de las interfaces utilizando show ip interface brief. Colocar los output en el informe e interpretar.  

Ahora hay mas subredes y se asigno la PC-A a la subred Laboratorio  

<img width="550" src="imagenes/Picture27.png" />     
<br><br>

<img width="550" src="imagenes/Picture28.png" />
<br><br>

---

#### m) Asignar la PC-B a la VLAN Laboratorio en el sw2. Repetir el inciso k) pero para el sw2.  

<img width="550" src="imagenes/Picture29.png" />     
<br><br>
<img width="550" src="imagenes/Picture30.png" />
<br><br>

---

#### n) Verificar la conectividad entre PC-A y PC-B utilizando pings. Verificar conectividad entre sw1 y sw2 utilizando pings. Interpretar los resultados.

Ninguno de los dos ping funciona debido a que ningún enlace físico pertenece a la subred adecuada. Entre los switches, como la interfaz f0/1 pertenece a la subred default y no a management, estos no encuentran un camino hacia el otro. Si asignamos dicha interfaz a la subred Management si funciona el ping.  

<img width="550" src="imagenes/Picture31.png" />   
<br><br> 
<img width="550" src="imagenes/Picture32.png" />    
<br><br>
Por el lado del ping entre las PCs, esta no funciona debido a que no hay dispositivos pertenecientes a la subred Laboratorio que las conecten, es decir, los switches al no tener una dirección ip asignada a la subred y una interfaz que las conecten el ping no funciona.  
Asignando una ip a la subred Laboratorio en cada switch y asignando la interfaz f0/1 a esta el ping funciona.  
<br><br>
<img width="550" src="imagenes/Picture33.png" />
<br><br>
<img width="550" src="imagenes/Picture34.png" />
<br><br>
<img width="400" src="imagenes/Picture35.png" />
<br><br>

---

## Rta consigna 3

Primero realizo las conexiones en Cisco Packet Tracer

<img width="400" src="imagenes/Picture36.png" />       
<br><br>  
Luego de realizar la configuración de switch y router (comandos), a cada laptop le tengo que asignar ip (seleccione DHCP en ip config de laptop), además de lo mismo con el servidor de entretenimiento (si pone una IP distinta de 10.10.99.10 hacerlo con static), por último debo activar el firewall del server para que funcione.  

Además se debe asignar la IP correspondiente al servidor ISP de forma estática, quedando de la siguiente manera:     

<img width="300" src="imagenes/Picture37.png" />    
<br><br>  

**Nota, se modificaron algunos comandos de configuracion de Router** porque se bloqueaba mal al turista del internet, ahora con estos se aplican las reglas al tráfico que entran al router desde la VLAN10 (turistas).  

```
# Dispositivos de Turista acceden a su propio gateway (10.10.10.1).
access-list 100 permit ip 10.10.10.0 0.0.0.255 10.10.10.1 0.0.0.0 
# Turista accede al servidor de entretenimiento (10.10.99.10).
access-list 100 permit ip 10.10.10.0 0.0.0.255 host 10.10.99.10 
# Bloquea cualquier otro tráfico originado desde la VLAN Turista.
access-list 100 deny ip 10.10.10.0 0.0.0.255 any
# Permite el resto del tráfico que no pertenezca a Turista.   
access-list 100 permit ip any any               


# Aplica la ACL 100 al tráfico que ENTRA al router desde la VLAN10 (Turista)
interface FastEthernet0/0.10
ip access-group 100 in                          
```  
<br>

**Pruebas desde una laptop turista (1, 3 y 2)** hago ping a servidor de entretenimiento (acepta) y ping a servidor de internet (rechaza), luego entro a pagina http de servidor entretenimiento (acepta)

<img width="300" src="imagenes/Picture38.png" />    
<br><br>  
<img width="500" src="imagenes/Picture39.png" />    
<br><br>  

**Prueba desde laptop business (4 y 5)** visito por el web browser el index.html del server de entretenimiento y además hago pin a internet (server ISP)  

<img width="300" src="imagenes/Picture41.png" />    
<br><br>  
<img width="500" src="imagenes/Picture40.png" />    
<br><br>  


**Prueba desde laptop admin (6)** hacer ping a todos los dispositivos (gatewate admin, pc turistas, pc business, servidor entretenimiento, router a isp, servidor isp)  

Console output:
```
Pinging 10.10.10.1 with 32 bytes of data:
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Ping statistics for 10.10.10.1:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
   Minimum = 0ms, Maximum = 0ms, Average = 0ms
C:\>ping 10.10.20.1
Pinging 10.10.20.1 with 32 bytes of data:
Reply from 10.10.20.1: bytes=32 time<1ms TTL=255
Reply from 10.10.20.1: bytes=32 time<1ms TTL=255
Reply from 10.10.20.1: bytes=32 time<1ms TTL=255
Reply from 10.10.20.1: bytes=32 time<1ms TTL=255
Ping statistics for 10.10.20.1:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
   Minimum = 0ms, Maximum = 0ms, Average = 0ms
C:\>ping 10.10.99.10
Pinging 10.10.99.10 with 32 bytes of data:
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Ping statistics for 10.10.99.10:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
   Minimum = 0ms, Maximum = 0ms, Average = 0ms
C:\>ping 200.0.0.1
Pinging 200.0.0.1 with 32 bytes of data:
Reply from 200.0.0.1: bytes=32 time<1ms TTL=255
Reply from 200.0.0.1: bytes=32 time=11ms TTL=255
Reply from 200.0.0.1: bytes=32 time=8ms TTL=255
Reply from 200.0.0.1: bytes=32 time<1ms TTL=255
Ping statistics for 200.0.0.1:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
   Minimum = 0ms, Maximum = 11ms, Average = 4ms
C:\>ping 200.0.0.2
Pinging 200.0.0.2 with 32 bytes of data:
Reply from 200.0.0.2: bytes=32 time<1ms TTL=127
Reply from 200.0.0.2: bytes=32 time<1ms TTL=127
Reply from 200.0.0.2: bytes=32 time<1ms TTL=127
Reply from 200.0.0.2: bytes=32 time<1ms TTL=127
Ping statistics for 200.0.0.2:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
   Minimum = 0ms, Maximum = 0ms, Average = 0ms

```

---

## Link al documento de Google:

[Práctico N4 - Redes](https://docs.google.com/document/d/1eenqDYHEd9kh-qdxRdy2F9jqV9K425jajT4lwcxHSrY/edit?tab=t.0)
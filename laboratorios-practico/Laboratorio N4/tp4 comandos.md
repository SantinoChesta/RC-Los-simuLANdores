## Comandos comentados

#### Configuracion de Router

```bash
enable                                          # Entra a modo privilegiado (EXEC privilegiado)
configure terminal                              # Entra a modo de configuración global

! Subinterfaces para VLANs
interface FastEthernet0/0                       # Selecciona la interfaz física
no shutdown                                     # Activa la interfaz física (sin esto, ninguna subinterfaz funciona)

interface FastEthernet0/0.10                    # Crea/entra a la subinterfaz .10 (para VLAN 10)
encapsulation dot1Q 10                          # Le dice a esta subinterfaz que escuche/etiquete tráfico VLAN 10
ip address 10.10.10.1 255.255.255.0             # Le asigna IP = gateway de la VLAN Turista

interface FastEthernet0/0.20                    # Subinterfaz para VLAN 20
encapsulation dot1Q 20                          # Tag VLAN 20
ip address 10.10.20.1 255.255.255.0             # Gateway de la VLAN Business

interface FastEthernet0/0.99                    # Subinterfaz para VLAN 99
encapsulation dot1Q 99                          # Tag VLAN 99
ip address 10.10.99.1 255.255.255.0             # Gateway de la VLAN Admin

interface FastEthernet0/1                       # Selecciona la interfaz hacia el ISP (WAN)
ip address 200.0.0.1 255.255.255.252            # IP pública del router (enlace punto a punto /30)
no shutdown                                     # Activa esa interfaz física

! DHCP para cada clase
ip dhcp excluded-address 10.10.10.1 10.10.10.10 # Reserva ese rango para que DHCP no lo reparta (gateway/server)
ip dhcp excluded-address 10.10.20.1 10.10.20.10 # Idem para Business
ip dhcp excluded-address 10.10.99.1 10.10.99.10 # Idem para Admin

ip dhcp pool Turista                            # Crea el pool DHCP "Turista"
network 10.10.10.0 255.255.255.0                # Red que va a repartir
default-router 10.10.10.1                       # Gateway que se le da a los clientes
dns-server 10.10.100.10                         # DNS que se le da a los clientes (server local, ejemplo)

ip dhcp pool Business                           # Pool DHCP "Business"
network 10.10.20.0 255.255.255.0
default-router 10.10.20.1
dns-server 8.8.8.8                              # DNS público, porque esta VLAN sí sale a Internet

ip dhcp pool Admin                              # Pool DHCP "Admin"
network 10.10.99.0 255.255.255.0
default-router 10.10.99.1
dns-server 8.8.8.8

! NAT solo para VLAN20 (Business)
access-list 20 permit 10.10.20.0 0.0.0.255      # ACL estándar: matchea tráfico originado en 10.10.20.0/24
ip nat inside source list 20 interface FastEthernet0/1 overload
                                                 # Traduce (PAT) las IPs que matchean la ACL 20 a la IP
                                                 # pública de Fa0/1, compartiendo esa IP por puertos (overload)

! Marcar interfaces NAT
interface FastEthernet0/0.10
ip nat inside                                   # Marca esta subinterfaz como "lado privado" de NAT
!
interface FastEthernet0/0.20
ip nat inside                                   # Idem para Business (esta sí se traduce, por la ACL 20)
!
interface FastEthernet0/0.99
ip nat inside                                   # Idem para Admin (marcada inside, pero no matchea ACL 20)
!
interface FastEthernet0/1
ip nat outside                                  # Marca esta interfaz como "lado público" de NAT

! Bloquear Internet a VLAN10 (Turista)

!no access-list 100 # Elimina la ACL 100 anterior para reconstruirla desde cero.

access-list 100 permit ip 10.10.10.0 0.0.0.255 10.10.10.1 0.0.0.0 # Permite que los dispositivos de Turista accedan a su propio gateway (10.10.10.1).

access-list 100 permit ip 10.10.10.0 0.0.0.255 host 10.10.99.10 #  Permite que Turista acceda al servidor de entretenimiento (10.10.99.10).

access-list 100 deny ip 10.10.10.0 0.0.0.255 any   # Bloquea cualquier otro tráfico originado desde la VLAN Turista.

access-list 100 permit ip any any               # Permite el resto del tráfico que no pertenezca a Turista.

interface FastEthernet0/0.10
ip access-group 100 in                          # Aplica la ACL 100 al tráfico que ENTRA al router desde la VLAN10 (Turista)

! Ruta por defecto hacia ISP
ip route 0.0.0.0 0.0.0.0 200.0.0.2              # Ruta default: todo lo que no tenga ruta específica va al ISP
```

#### Configuración del Switch:

```bash
enable                                          # Modo privilegiado
configure terminal                              # Modo configuración global

vlan 10                                         # Crea la VLAN 10
name Turista                                    # Le pone nombre descriptivo
vlan 20                                         # Crea la VLAN 20
name Business
vlan 99                                         # Crea la VLAN 99
name Admin

! Puerto hacía router como trunk
interface FastEthernet0/1                       # Puerto conectado al router
switchport mode trunk                           # Modo trunk: transporta tráfico etiquetado de varias VLANs

! Asignar puertos a cada clase
interface range FastEthernet0/2 - 3             # Selecciona varios puertos a la vez (rango)
switchport mode access                          # Modo access: un puerto = una sola VLAN, sin tagging
switchport access vlan 10                       # Asigna esos puertos a la VLAN 10 (Turista)

interface range FastEthernet0/4 - 5
switchport mode access
switchport access vlan 20                       # Puertos para Business

interface FastEthernet0/6
switchport mode access
switchport access vlan 99                       # Puerto para Admin

interface FastEthernet0/7
switchport mode access
switchport access vlan 99                       # Puerto para el servidor (queda en la VLAN Admin, según el diseño del TP)
```

## Comandos Copiar y pegar en consola:

#### Configuración del router:

```bash
enable
configure terminal
! Subinterfaces para VLANs
interface FastEthernet0/0
no shutdown
interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 10.10.10.1 255.255.255.0
interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 10.10.20.1 255.255.255.0
interface FastEthernet0/0.99
encapsulation dot1Q 99
ip address 10.10.99.1 255.255.255.0
interface FastEthernet0/1
ip address 200.0.0.1 255.255.255.252
no shutdown
! DHCP para cada clase
ip dhcp excluded-address 10.10.10.1 10.10.10.10
ip dhcp excluded-address 10.10.20.1 10.10.20.10
ip dhcp excluded-address 10.10.99.1 10.10.99.10
ip dhcp pool Turista
network 10.10.10.0 255.255.255.0
default-router 10.10.10.1
dns-server 10.10.100.10
ip dhcp pool Business
network 10.10.20.0 255.255.255.0
default-router 10.10.20.1
dns-server 8.8.8.8
ip dhcp pool Admin
network 10.10.99.0 255.255.255.0
default-router 10.10.99.1
dns-server 8.8.8.8
! NAT solo para VLAN20 (Business)
access-list 20 permit 10.10.20.0 0.0.0.255
ip nat inside source list 20 interface FastEthernet0/1 overload
! Marcar interfaces NAT
interface FastEthernet0/0.10
ip nat inside
!
interface FastEthernet0/0.20
ip nat inside
!
interface FastEthernet0/0.99
ip nat inside
!
interface FastEthernet0/1
ip nat outside

! Bloquear Internet a VLAN10 (Turista)
! no access-list 100
! Elimina la ACL 100 anterior para reconstruirla desde cero.

access-list 100 permit ip 10.10.10.0 0.0.0.255 10.10.10.1 0.0.0.0
! Permite que los dispositivos de Turista accedan a su propio gateway (10.10.10.1).

access-list 100 permit ip 10.10.10.0 0.0.0.255 host 10.10.99.10
! Permite que Turista acceda al servidor de entretenimiento (10.10.99.10).

access-list 100 deny ip 10.10.10.0 0.0.0.255 any
! Bloquea cualquier otro tráfico originado desde la VLAN Turista.

access-list 100 permit ip any any
! Permite el resto del tráfico que no pertenezca a Turista.

interface FastEthernet0/0.10
ip access-group 100 in
! Ruta por defecto hacia ISP
ip route 0.0.0.0 0.0.0.0 200.0.0.2
```

#### Configuración del Switch:

```bash
enable
configure terminal
vlan 10
name Turista
vlan 20
name Business
vlan 99
name Admin
! Puerto hacía router como trunk
interface FastEthernet0/1
switchport mode trunk
! Asignar puertos a cada clase
interface range FastEthernet0/2 - 3
switchport mode access
switchport access vlan 10
interface range FastEthernet0/4 - 5
switchport mode access
switchport access vlan 20
interface FastEthernet0/6
switchport mode access
switchport access vlan 99
interface FastEthernet0/7
switchport mode access
switchport access vlan 99
! para el servidor
```

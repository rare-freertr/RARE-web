# Interoperability test: ospf point to point connection

Establish OSPF point to point adjaceny between FreerTr and cisco IOS 

### Topology diagram

![topology](/img/intop1-ospf01.png)

### Configuration

r1:
```
!
vrf def v1
 rd 1:1
 exit
router ospf4 1
 vrf v1
 router 4.4.4.1
 area 0 ena
 red conn
 exit
router ospf6 1
 vrf v1
 router 6.6.6.1
 area 0 ena
 red conn
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr fe80::1 ffff::
 router ospf4 1 ena
 router ospf6 1 ena
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
!
```

r2:
```
!
ip routing
ipv6 unicast-routing
interface loopback0
 ip addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
router ospf 1
 redistribute connected subnets
 exit
ipv6 router ospf 1
 redistribute connected
 exit
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 ipv6 enable
 ip ospf network point-to-point
 ip ospf 1 area 0
 ipv6 ospf network point-to-point
 ipv6 ospf 1 area 0
 no shutdown
 exit
!
```

### Verification

```
r1 ping 2.2.2.2 /vrf v1
r2 ping 2.2.2.1 /vrf v1
r1 ping 4321::2 /vrf v1
r2 ping 4321::1 /vrf v1

```

```
show ipv4 ospf 1 interfaces
<cli output>

```

```
show ipv4 ospf 1 neighbors
<cli output>

```

```
show ipv4 ospf 1 database 0
<cli output>

```

```
show ipv6 ospf 1 interfaces
<cli output>

```

```
show ipv6 ospf 1 neighbors
<cli output>

```

```
show ipv6 ospf 1 database 0
<cli output>

```

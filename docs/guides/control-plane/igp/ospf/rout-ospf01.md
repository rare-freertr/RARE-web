# Example: ospf point to point connection

Establish OSPF point to point adjaceny between 2 nodes

## Topology diagram

![topology](/img/rout-ospf01.png)

## Configuration

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
int lo1
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 router ospf4 1 ena
 router ospf6 1 ena
 exit
!
```

r2:
```
!
vrf def v1
 rd 1:1
 exit
router ospf4 1
 vrf v1
 router 4.4.4.2
 area 0 ena
 red conn
 exit
router ospf6 1
 vrf v1
 router 6.6.6.2
 area 0 ena
 red conn
 exit
int lo1
 vrf for v1
 ipv4 addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.2 255.255.255.0
 ipv6 addr 1234::2 ffff::
 router ospf4 1 ena
 router ospf6 1 ena
 exit
!
```

## Verification

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

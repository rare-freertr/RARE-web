# Example: p4lang: hairpin vpls/ldp with bgp

## **Topology diagram**

![topology](/img/p4lang-rout041.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz16r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 label-mode per-prefix
 exit
bridge 1
 rd 1:1
 rt-both 1:1
 mac-learn
 exit
bridge 2
 mac-learn
 exit
bridge 3
 mac-learn
 exit
vrf def v9
 rd 1:1
 exit
int lo9
 vrf for v9
 ipv4 addr 10.10.10.227 255.255.255.255
 exit
int eth1
 vrf for v9
 ipv4 addr 10.11.12.254 255.255.255.0
 exit
int eth2
 exit
server dhcp4 eth1
 pool 10.11.12.1 10.11.12.99
 gateway 10.11.12.254
 netmask 255.255.255.0
 dns-server 10.10.10.227
 domain-name p4l
 static 0000.0000.2222 10.11.12.111
 interface eth1
 vrf v9
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.101 255.255.255.255
 ipv6 addr 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
hair 1
 ether
 exit
hair 2
 ether
 exit
int sdn1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234:1::1 ffff:ffff::
 ipv6 ena
 mpls enable
 mpls ldp4
 mpls ldp6
 exit
int sdn2
 vrf for v1
 ipv4 addr 1.1.2.1 255.255.255.0
 ipv6 addr 1234:2::1 ffff:ffff::
 ipv6 ena
 mpls enable
 mpls ldp4
 mpls ldp6
 exit
int sdn3
 bridge-gr 2
 exit
int sdn4
 bridge-gr 3
 exit
int hair11
 bridge-gr 1
 exit
int hair12
 bridge-gr 2
 exit
int hair21
 bridge-gr 1
 exit
int hair22
 bridge-gr 3
 exit
router bgp4 1
 vrf v1
 address vpls
 local-as 1
 router-id 4.4.4.1
 temp a remote-as 1
 temp a update lo0
 temp a send-comm both
 temp a route-reflect
 neigh 2.2.2.103 temp a
 neigh 2.2.2.104 temp a
 afi-vpls 1:1 bridge 1
 afi-vpls 1:1 update lo0
 exit
router bgp6 1
 vrf v1
 address vpls
 local-as 1
 router-id 6.6.6.1
 temp a remote-as 1
 temp a update lo0
 temp a send-comm both
 temp a route-reflect
 neigh 4321::103 temp a
 neigh 4321::104 temp a
 exit
server p4lang p4
 interconnect eth2
 export-vrf v1 1
 export-br 1
 export-br 2
 export-br 3
 export-port sdn1 1 10
 export-port sdn2 2 10
 export-port sdn3 3 10
 export-port sdn4 4 10
 export-port hair11 dynamic
 export-port hair12 dynamic
 export-port hair21 dynamic
 export-port hair22 dynamic
 vrf v9
 exit
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.2.2
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
```

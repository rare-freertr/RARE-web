# Example: p4lang: bridging over l2tp vlan

## **Topology diagram**

![topology](/img/p4lang-rout088.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz64r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
vrf def v2
 rd 1:1
 exit
vrf def v8
 rd 1:1
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
bridge 1
 mac-learn
 exit
int sdn1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234:1::1 ffff:ffff::
 ipv6 ena
 exit
int sdn2
 bridge-gr 1
 exit
int sdn3
 exit
int sdn3.222
 vrf for v2
 ipv4 addr 9.9.9.1 255.255.255.0
 exit
int virt1
 enc ppp
 pseudo v2 sdn3.222 l2tp2 9.9.9.2 1234
 bridge-gr 1
 vrf for v8
 ipv4 addr 3.3.3.3 255.255.255.255
 exit
int sdn4
 bridge-gr 1
 exit
server p4lang p4
 interconnect eth2
 export-vrf v1 1
 export-vrf v2 2
 export-vrf v8 8
 export-br 1
 export-port sdn1 1 10
 export-port sdn2 2 10
 export-port sdn3 3 10
 export-port sdn4 4 10
 export-port virt1 dynamic
 vrf v9
 exit
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
```

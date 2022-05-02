# Example: interop1: ospf nondr

## **Topology diagram**

![topology](/img/intop1-ospf03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz11r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
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
 router ospf4 1 net broad
 router ospf4 1 prio 0
 router ospf6 1 ena
 router ospf6 1 net broad
 router ospf6 1 prio 0
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
```

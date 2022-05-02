# Example: interop1: bgp 6pe

## **Topology diagram**

![topology](/img/intop1-bgp18.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz52r1-log.run
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
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 mpls enable
 mpls ldp4
 exit
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
router bgp4 1
 vrf v1
 address olab
 local-as 1
 router-id 4.4.4.1
 neigh 2.2.2.2 remote-as 1
 neigh 2.2.2.2 update lo0
 neigh 2.2.2.2 send-comm both
 afi-other ena
 afi-other red conn
 exit
```

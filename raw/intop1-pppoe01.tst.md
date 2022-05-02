# Example: interop1: pppoe client

## **Topology diagram**

![topology](/img/intop1-pppoe01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz75r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
prefix-list p1
 permit 0.0.0.0/0
 exit
int di1
 enc ppp
 ppp ip4cp open
 vrf for v1
 ipv4 addr 3.3.3.3 255.255.255.0
 ppp ip4cp local 0.0.0.0
 ipv4 gateway-prefix p1
 exit
int eth1
 p2poe client di1
 exit
```

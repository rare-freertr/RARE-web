# Example: interop1: point2point ethernet encapsulation

## **Topology diagram**

![topology](/img/intop1-eth05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz74r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.2 255.255.255.254
 ipv6 addr 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
 exit
```

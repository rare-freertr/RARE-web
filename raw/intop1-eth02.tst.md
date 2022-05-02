# Example: interop1: dot1q encapsulation

## **Topology diagram**

![topology](/img/intop1-eth02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz12r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
int eth1.123
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
```

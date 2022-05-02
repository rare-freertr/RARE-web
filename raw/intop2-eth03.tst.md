# Example: interop2: dot1ad encapsulation

## **Topology diagram**

![topology](/img/intop2-eth03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz66r1-log.run
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
 enc dot1ad
 exit
int eth1.123
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
```

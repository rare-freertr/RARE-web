# Example: interop1: radius

## **Topology diagram**

![topology](/img/intop1-radius.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz40r1-log.run
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
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
aaa userlist usr
 username usr password pwd
 exit
server radius rad
 authen usr
 secret tester
 vrf v1
 exit
```

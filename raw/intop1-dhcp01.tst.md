# Example: interop1: dhcp server

## **Topology diagram**

![topology](/img/intop1-dhcp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz62r1-log.run
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
server dhcp4 dh
 pool 1.1.1.11 1.1.1.99
 gateway 1.1.1.1
 netmask 255.255.255.0
 interface ethernet1
 static 0000.0000.1100 1.1.1.2
 vrf v1
 exit
server dhcp6 dh
 netmask ffff:ffff:ffff:ffff::
 gateway 1234::1
 static 0000.0000.1100 1234::2
 interface ethernet1
 vrf v1
 exit
```

# Example: interop8: rip

## **Topology diagram**

![topology](/img/intop8-rip01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz56r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
router rip4 1
 vrf v1
 red conn
 exit
router rip6 1
 vrf v1
 red conn
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr fe80::1 ffff::
 router rip4 1 ena
 router rip6 1 ena
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
```

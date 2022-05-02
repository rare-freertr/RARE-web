# Example: interop1: vxlan tunnel

## **Topology diagram**

![topology](/img/intop1-tun03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz45r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
proxy-profile p1
 vrf v1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
bridge 1
 exit
vpdn bvi1
 bridge-group 1
 proxy p1
 target 1.1.1.2
 vcid 1111
 pwtype atm-port
 protocol vxlan
 exit
int bvi1
 macaddr 0000.0000.1234
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.0
 ipv6 addr 2222::1 ffff::
 ipv4 host-static 2.2.2.2 0000.0000.4321
 ipv6 host-static 2222::2 0000.0000.4321
 exit
```

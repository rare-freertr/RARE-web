# Example: interop9: fragmentation and reassembly

## **Topology diagram**

![topology](/img/intop9-eth03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz36r1-log.run
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
 mtu 1500
 enforce-mtu both
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 ipv4 reassembly 16
 ipv4 fragmentation 1400
 ipv6 reassembly 16
 ipv6 fragmentation 1400
 exit
```

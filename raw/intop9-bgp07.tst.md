# Example: interop9: bgp aspath

## **Topology diagram**

![topology](/img/intop9-bgp07.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz64r1-log.run
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
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
route-map rm1
 sequence 10 act deny
  match aspath .*1234.*
 sequence 20 act permit
 exit
router bgp4 1
 vrf v1
 no safe-ebgp
 address uni
 local-as 1
 router-id 4.4.4.1
 neigh 1.1.1.2 remote-as 2
 neigh 1.1.1.2 route-map-in rm1
 red conn
 exit
router bgp6 1
 vrf v1
 no safe-ebgp
 address uni
 local-as 1
 router-id 6.6.6.1
 neigh 1234::2 remote-as 2
 neigh 1234::2 route-map-in rm1
 red conn
 exit
```

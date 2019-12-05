# Example: interop9: ospf nssa area

## **Topology diagram**

![topology](/img/intop9-ospf06.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 1 enable
 area 1 nssa
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 1 enable
 area 1 nssa
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address fe80::1 ffff::
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
 no shutdown
 no log-link-change
 exit
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
end
```

**r2:**
```
hostname r2
set interfaces ge-0/0/0.0 family inet address 1.1.1.2/24
set interfaces ge-0/0/0.0 family inet6
set interfaces lo0.0 family inet address 2.2.2.2/32
set interfaces lo0.0 family inet6 address 4321::2/128
set protocols ospf area 1 interface ge-0/0/0.0 interface-type p2p
set protocols ospf area 1 interface lo0.0
set protocols ospf area 1 nssa
set protocols ospf3 area 1 interface ge-0/0/0.0 interface-type p2p
set protocols ospf3 area 1 interface lo0.0
set protocols ospf3 area 1 nssa
commit
```

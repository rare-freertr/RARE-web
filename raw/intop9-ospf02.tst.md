# Example: interop9: ospf dr

## **Topology diagram**

![topology](/img/intop9-ospf02.tst.png)

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
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 router ospf4 1 area 0
 router ospf4 1 network broadcast
 router ospf4 1 priority 10
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 network broadcast
 router ospf6 1 priority 10
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
set protocols ospf area 0 interface ge-0/0/0.0
set protocols ospf area 0 interface lo0.0
set protocols ospf3 area 0 interface ge-0/0/0.0
set protocols ospf3 area 0 interface lo0.0
commit
```

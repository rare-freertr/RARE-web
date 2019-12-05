# Example: interop8: ospf nssa area

## **Topology diagram**

![topology](/img/intop8-ospf06.tst.png)

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
ip forwarding
ipv6 forwarding
router ospf
 area 1 nssa
 exit
router ospf6
! area 1 nssa
 interface ens3 area 0.0.0.1
 interface lo area 0.0.0.1
 exit
interface lo
 ip addr 2.2.2.2/32
 ipv6 addr 4321::2/128
 ip ospf area 1
 exit
interface ens3
 ip address 1.1.1.2/24
 ip ospf area 1
 ip ospf network point-to-point
 ipv6 ospf6 network point-to-point
 no shutdown
 exit
```

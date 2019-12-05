# Example: interop2: ospf sr

## **Topology diagram**

![topology](/img/intop2-ospf11.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 2.2.2.1
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 segrout index 1
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 segrout index 2
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0010.5020.7c56
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 pseudowire v1 loopback0 pweompls 2.2.2.3 1234
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
interface loopback0
 ipv4 addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
interface gigabit0/0/0/0
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 enable
 no shutdown
 exit
interface gigabit0/0/0/1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 enable
 no shutdown
 exit
router ospf 1
 redistribute connected
 mpls traffic-eng router-id Loopback0
 area 0
  segment-routing forwarding mpls
  mpls traffic-eng
  segment-routing mpls
  interface Loopback0
   passive enable
   prefix-sid index 3
  interface gigabit0/0/0/0 network point-to-point
  interface gigabit0/0/0/1 network point-to-point
router ospfv3 1
 redistribute connected
 area 0
  interface gigabit0/0/0/0 network point-to-point
  interface gigabit0/0/0/1 network point-to-point
root
commit
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.3
 traffeng-id 2.2.2.3
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 segrout index 5
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 segrout index 6
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 000a.1e6a.2052
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
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

# Example: interop1: ospf te

## **Topology diagram**

![topology](/img/intop1-ospf07.tst.png)

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
 traffeng-id 2.2.2.1
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address fe80::1 ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 bandwidth 11
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 2.2.2.2
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 bandwidth 11
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 2.2.2.3
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.9 255.255.255.252
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
ip routing
ipv6 unicast-routing
mpls traffic-eng tunnels
no mpls traffic-eng signalling advertise implicit-null
interface loopback0
 ip addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
router ospf 1
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng area 0
 redistribute connected subnets
 exit
ipv6 router ospf 1
 redistribute connected
 exit
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 ipv6 enable
 ip ospf network point-to-point
 ip ospf 1 area 0
 ipv6 ospf network point-to-point
 ipv6 ospf 1 area 0
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
interface gigabit2
 ip address 1.1.2.2 255.255.255.0
 ipv6 enable
 ip ospf network point-to-point
 ip ospf 1 area 0
 ipv6 ospf network point-to-point
 ipv6 ospf 1 area 0
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
interface Tunnel1
 ip address 3.3.3.2 255.255.255.252
 tunnel mode mpls traffic-eng
 tunnel destination 2.2.2.1
 tunnel mpls traffic-eng path-option 1 dynamic
 exit
interface Tunnel2
 ip address 3.3.3.6 255.255.255.252
 tunnel mode mpls traffic-eng
 tunnel destination 2.2.2.3
 tunnel mpls traffic-eng path-option 1 dynamic
 exit
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.3
 traffeng-id 2.2.2.3
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address fe80::1 ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 bandwidth 11
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 2.2.2.2
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.5 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 bandwidth 11
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 2.2.2.1
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.10 255.255.255.252
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

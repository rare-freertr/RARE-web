# Example: interop1: isis sr

## **Topology diagram**

![topology](/img/intop1-isis10.tst.png)

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
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id 2.2.2.1
 is-type both
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id 6.6.6.1
 is-type both
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 segrout index 1
 router isis4 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 segrout index 2
 router isis6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 mpls enable
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 ipv6 access-group-out test6
 mpls enable
 router isis6 1 enable
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0074.6e19.7401
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 pseudowire v1 loopback1 pweompls 2.2.2.3 1234
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
segment-routing mpls
 set-attributes
  address-family ipv4
   explicit-null
 connected-prefix-sid-map
  address-family ipv4
   2.2.2.2/32 index 3
router isis
 net 48.0000.0000.1234.00
 metric-style wide
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
 redistribute connected
 is-type level-2-only
 segment-routing mpls
 address-family ipv6
  redistribute connected
 exit
interface gigabit2
 ip address 1.1.1.2 255.255.255.0
 isis network point-to-point
 ip router isis
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
interface gigabit1
 ipv6 enable
 isis network point-to-point
 ipv6 router isis
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
interface gigabit3
 ip address 1.1.2.2 255.255.255.0
 isis network point-to-point
 ip router isis
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
interface gigabit4
 ipv6 enable
 isis network point-to-point
 ipv6 router isis
 ip rsvp bandwidth
 mpls traffic-eng tunnels
 no shutdown
 exit
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
router isis4 1
 vrf v1
 net-id 48.4444.0000.3333.00
 traffeng-id 2.2.2.3
 is-type both
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.3333.00
 traffeng-id 6.6.6.3
 is-type both
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 segrout index 5
 router isis4 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 segrout index 6
 router isis6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 access-group-in test4
 mpls enable
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 ipv6 access-group-out test6
 mpls enable
 router isis6 1 enable
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 006d.5f49.7263
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 pseudowire v1 loopback1 pweompls 2.2.2.1 1234
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

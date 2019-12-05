# Example: interop9: isis te

## **Topology diagram**

![topology](/img/intop9-isis04.tst.png)

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
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id 2.2.2.1
 is-type both
 level2 traffeng
 level1 traffeng
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id 6.6.6.1
 is-type both
 level2 traffeng
 level1 traffeng
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 mpls enable
 mpls rsvp4
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
 mpls enable
 mpls rsvp6
 router isis6 1 enable
 router isis6 1 circuit both
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
set interfaces ge-0/0/0.0 family inet address 1.1.1.2/24
set interfaces ge-0/0/0.0 family iso
set interfaces ge-0/0/0.0 family mpls
set interfaces ge-0/0/1.0 family inet6
set interfaces ge-0/0/1.0 family iso
set interfaces ge-0/0/1.0 family mpls
set interfaces ge-0/0/2.0 family inet address 1.1.2.2/24
set interfaces ge-0/0/2.0 family iso
set interfaces ge-0/0/2.0 family mpls
set interfaces ge-0/0/3.0 family inet6
set interfaces ge-0/0/3.0 family iso
set interfaces ge-0/0/3.0 family mpls
set interfaces lo0.0 family inet address 2.2.2.2/32
set interfaces lo0.0 family inet6 address 4321::2/128
set interfaces lo0.0 family iso address 48.0000.0000.1234.00
set interfaces lo0.0 family inet address 3.3.3.2/32
set interfaces lo0.0 family inet address 3.3.3.6/32
set protocols rsvp interface lo0.0
set protocols rsvp interface ge-0/0/0.0
set protocols rsvp interface ge-0/0/1.0
set protocols rsvp interface ge-0/0/2.0
set protocols rsvp interface ge-0/0/3.0
set protocols mpls interface ge-0/0/0.0
set protocols mpls interface ge-0/0/1.0
set protocols mpls interface ge-0/0/2.0
set protocols mpls interface ge-0/0/3.0
set protocols isis interface ge-0/0/0.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/1.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/2.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/3.0 point-to-point hello-padding disable
set protocols isis interface lo0.0
set protocols isis traffic-engineering family inet shortcuts
set protocols isis traffic-engineering family inet6 shortcuts
commit
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
router isis4 1
 vrf v1
 net-id 48.4444.0000.3333.00
 traffeng-id 2.2.2.3
 is-type both
 level2 traffeng
 level1 traffeng
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.3333.00
 traffeng-id 6.6.6.3
 is-type both
 level2 traffeng
 level1 traffeng
 redistribute connected
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 mpls enable
 mpls rsvp4
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
 mpls enable
 mpls rsvp6
 router isis6 1 enable
 router isis6 1 circuit both
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

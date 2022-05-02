# Example: bgp over te

## **Topology diagram**

![topology](/img/mpls-te20.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz38r1-log.run
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
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.255
 ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1.1.2.2
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 2345::2
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 4321::1 ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 2.2.2.2 remote-as 1
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family unicast
 neighbor 2.2.2.2 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 4321::2 remote-as 1
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family unicast
 neighbor 4321::2 distance 200
 redistribute connected
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
ipv4 route v1 1.1.2.0 255.255.255.0 1.1.1.2
!
ipv6 route v1 2345:: ffff:: 1234::2
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz38r2-log.run
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
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 2345::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz38r3-log.run
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
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.255
 ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 2345::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1.1.1.1
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1234::1
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 4321::2 ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family unicast
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family unicast
 neighbor 2.2.2.1 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family unicast
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family unicast
 neighbor 4321::1 distance 200
 redistribute connected
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
ipv4 route v1 1.1.1.0 255.255.255.0 1.1.2.1
!
ipv6 route v1 1234:: ffff:: 2345::1
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

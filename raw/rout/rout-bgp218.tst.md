# Example: ebgp with ttl-security

## **Topology diagram**

![topology](/img/rout-bgp218.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz56r1-log.run
!
access-list test4
 sequence 10 permit 6 any all any all ttl 110-120
 sequence 20 deny 6 any all any all
 sequence 30 permit all any all any all
 exit
!
access-list test6
 sequence 10 permit 6 any all any all ttl 110-120
 sequence 20 deny 6 any all any all
 sequence 30 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 access-group-in test4
 ipv4 access-group-out test4
 ipv6 address 1234::1 ffff:ffff::
 ipv6 access-group-in test6
 ipv6 access-group-out test6
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 2
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 connection-mode passive
 neighbor 1.1.1.2 ttl-security 115
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234::2 remote-as 2
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family unicast
 neighbor 1234::2 distance 20
 neighbor 1234::2 connection-mode passive
 neighbor 1234::2 ttl-security 115
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

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz56r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 connection-mode active
 neighbor 1.1.1.1 ttl-security 115
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast
 neighbor 1234::1 remote-as 1
 no neighbor 1234::1 description
 neighbor 1234::1 local-as 2
 neighbor 1234::1 address-family unicast
 neighbor 1234::1 distance 20
 neighbor 1234::1 connection-mode active
 neighbor 1234::1 ttl-security 115
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

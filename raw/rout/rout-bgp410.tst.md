# Example: bgp remove private as out with routepolicy

## **Topology diagram**

![topology](/img/rout-bgp410.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz91r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 65534
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 65534
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 65534
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234:1::2 remote-as 1
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 65534
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 20
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
logging file debug ../binTmp/zzz91r2-log.run
!
route-policy rm1
 sequence 10 if privateas
 sequence 20   clear privateas
 sequence 30   pass
 sequence 40 enif
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.1 remote-as 65534
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 route-policy-out rm1
 neighbor 1.1.1.6 remote-as 65534
 no neighbor 1.1.1.6 description
 neighbor 1.1.1.6 local-as 1
 neighbor 1.1.1.6 address-family unicast
 neighbor 1.1.1.6 distance 20
 neighbor 1.1.1.6 route-policy-out rm1
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:1::1 remote-as 65534
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 20
 neighbor 1234:1::1 route-policy-out rm1
 neighbor 1234:2::2 remote-as 65534
 no neighbor 1234:2::2 description
 neighbor 1234:2::2 local-as 1
 neighbor 1234:2::2 address-family unicast
 neighbor 1234:2::2 distance 20
 neighbor 1234:2::2 route-policy-out rm1
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz91r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 65534
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.5 remote-as 1
 no neighbor 1.1.1.5 description
 neighbor 1.1.1.5 local-as 65534
 neighbor 1.1.1.5 address-family unicast
 neighbor 1.1.1.5 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 65534
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:2::1 remote-as 1
 no neighbor 1234:2::1 description
 neighbor 1234:2::1 local-as 65534
 neighbor 1234:2::1 address-family unicast
 neighbor 1234:2::1 distance 20
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

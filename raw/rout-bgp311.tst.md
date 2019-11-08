# Example: ebgp with nexthop tracking interface

## **Topology diagram**

![topology](/img/rout-bgp311.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
route-policy rm1
 sequence 10 pass
 exit
!
route-policy rm2
 sequence 10 set aspath 3 3 3
 sequence 20 pass
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff::
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
 router-id 4.4.4.1
 address-family unicast
 nexthop route-policy rm1
 neighbor 1.1.1.2 remote-as 2
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 route-policy-in rm2
 neighbor 1.1.1.2 route-policy-out rm2
 neighbor 1.1.1.6 remote-as 2
 no neighbor 1.1.1.6 description
 neighbor 1.1.1.6 local-as 1
 neighbor 1.1.1.6 address-family unicast
 neighbor 1.1.1.6 distance 20
 neighbor 1.1.1.6 fall-over
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 nexthop route-policy rm1
 neighbor 1234:1::2 remote-as 2
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 20
 neighbor 1234:1::2 route-policy-in rm2
 neighbor 1234:1::2 route-policy-out rm2
 neighbor 1234:2::2 remote-as 2
 no neighbor 1234:2::2 description
 neighbor 1234:2::2 local-as 1
 neighbor 1234:2::2 address-family unicast
 neighbor 1234:2::2 distance 20
 neighbor 1234:2::2 fall-over
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
route-policy rm1
 sequence 10 pass
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
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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
 local-as 2
 router-id 4.4.4.2
 address-family unicast
 nexthop route-policy rm1
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.5 remote-as 1
 no neighbor 1.1.1.5 description
 neighbor 1.1.1.5 local-as 2
 neighbor 1.1.1.5 address-family unicast
 neighbor 1.1.1.5 distance 20
 neighbor 1.1.1.5 fall-over
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast
 nexthop route-policy rm1
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 20
 neighbor 1234:2::1 remote-as 1
 no neighbor 1234:2::1 description
 neighbor 1234:2::1 local-as 2
 neighbor 1234:2::1 address-family unicast
 neighbor 1234:2::1 distance 20
 neighbor 1234:2::1 fall-over
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
end
```

## **Verification**

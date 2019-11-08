# Example: ebgp vpn client

## **Topology diagram**

![topology](/img/rout-bgp303.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match aspath .*3.*
 !
 sequence 20 action permit
 !
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
 ipv6 address 1234:1::1 ffff:ffff::
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
 neighbor 1.1.1.2 route-map-in rm1
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234:1::2 remote-as 2
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 20
 neighbor 1234:1::2 route-map-in rm1
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
 local-as 2
 router-id 4.4.4.2
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 internal-vpn-client
 neighbor 1.1.1.6 remote-as 3
 no neighbor 1.1.1.6 description
 neighbor 1.1.1.6 local-as 2
 neighbor 1.1.1.6 address-family unicast
 neighbor 1.1.1.6 distance 20
 neighbor 1.1.1.6 attribset
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 20
 neighbor 1234:1::1 internal-vpn-client
 neighbor 1234:2::2 remote-as 3
 no neighbor 1234:2::2 description
 neighbor 1234:2::2 local-as 2
 neighbor 1234:2::2 address-family unicast
 neighbor 1234:2::2 distance 20
 neighbor 1234:2::2 attribset
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
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 3
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.5 remote-as 2
 no neighbor 1.1.1.5 description
 neighbor 1.1.1.5 local-as 3
 neighbor 1.1.1.5 address-family unicast
 neighbor 1.1.1.5 distance 20
 neighbor 1.1.1.5 attribset
 neighbor 1.1.1.10 remote-as 4
 no neighbor 1.1.1.10 description
 neighbor 1.1.1.10 local-as 3
 neighbor 1.1.1.10 address-family unicast
 neighbor 1.1.1.10 distance 20
 neighbor 1.1.1.10 attribset
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 3
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:2::1 remote-as 2
 no neighbor 1234:2::1 description
 neighbor 1234:2::1 local-as 3
 neighbor 1234:2::1 address-family unicast
 neighbor 1234:2::1 distance 20
 neighbor 1234:2::1 attribset
 neighbor 1234:3::2 remote-as 4
 no neighbor 1234:3::2 description
 neighbor 1234:3::2 local-as 3
 neighbor 1234:3::2 address-family unicast
 neighbor 1234:3::2 distance 20
 neighbor 1234:3::2 attribset
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.13 255.255.255.252
 ipv6 address 1234:4::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 4
 router-id 4.4.4.4
 address-family unicast
 neighbor 1.1.1.9 remote-as 3
 no neighbor 1.1.1.9 description
 neighbor 1.1.1.9 local-as 4
 neighbor 1.1.1.9 address-family unicast
 neighbor 1.1.1.9 distance 20
 neighbor 1.1.1.9 attribset
 neighbor 1.1.1.14 remote-as 5
 no neighbor 1.1.1.14 description
 neighbor 1.1.1.14 local-as 4
 neighbor 1.1.1.14 address-family unicast
 neighbor 1.1.1.14 distance 20
 neighbor 1.1.1.14 internal-vpn-client
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 4
 router-id 6.6.6.4
 address-family unicast
 neighbor 1234:3::1 remote-as 3
 no neighbor 1234:3::1 description
 neighbor 1234:3::1 local-as 4
 neighbor 1234:3::1 address-family unicast
 neighbor 1234:3::1 distance 20
 neighbor 1234:3::1 attribset
 neighbor 1234:4::2 remote-as 5
 no neighbor 1234:4::2 description
 neighbor 1234:4::2 local-as 4
 neighbor 1234:4::2 address-family unicast
 neighbor 1234:4::2 distance 20
 neighbor 1234:4::2 internal-vpn-client
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

**r5:**
```
hostname r5
buggy
!
logging file debug ../binTmp/zzz-log-r5.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match aspath .*3.*
 !
 sequence 20 action permit
 !
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.5 255.255.255.255
 ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.14 255.255.255.252
 ipv6 address 1234:4::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 5
 router-id 4.4.4.5
 address-family unicast
 neighbor 1.1.1.13 remote-as 4
 no neighbor 1.1.1.13 description
 neighbor 1.1.1.13 local-as 5
 neighbor 1.1.1.13 address-family unicast
 neighbor 1.1.1.13 distance 20
 neighbor 1.1.1.13 route-map-in rm1
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 5
 router-id 6.6.6.5
 address-family unicast
 neighbor 1234:4::1 remote-as 4
 no neighbor 1234:4::1 description
 neighbor 1234:4::1 local-as 5
 neighbor 1234:4::1 address-family unicast
 neighbor 1234:4::1 distance 20
 neighbor 1234:4::1 route-map-in rm1
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

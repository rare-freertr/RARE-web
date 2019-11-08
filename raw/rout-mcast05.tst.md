# Example: multicast between pim and mldp

## **Topology diagram**

![topology](/img/rout-mcast05.tst.png)

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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
ipv6 route v1 :: :: 1234:1::2
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
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 multicast mldp-enable
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast multicast
 neighbor 2.2.2.3 remote-as 1
 no neighbor 2.2.2.3 description
 neighbor 2.2.2.3 local-as 1
 neighbor 2.2.2.3 address-family unicast multicast
 neighbor 2.2.2.3 distance 200
 neighbor 2.2.2.3 update-source loopback0
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast multicast
 neighbor 4321::3 remote-as 1
 no neighbor 4321::3 description
 neighbor 4321::3 local-as 1
 neighbor 4321::3 address-family unicast multicast
 neighbor 4321::3 distance 200
 neighbor 4321::3 update-source loopback0
 redistribute connected
 exit
!
!
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.5
!
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
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
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 multicast mldp-enable
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv4 multicast mldp-enable
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.6
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.10
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
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
 ipv4 address 1.1.1.10 255.255.255.252
 ipv4 multicast mldp-enable
 ipv6 address 1234:3::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.14 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:4::2 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family unicast multicast
 neighbor 2.2.2.1 remote-as 1
 no neighbor 2.2.2.1 description
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family unicast multicast
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 update-source loopback0
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family unicast multicast
 neighbor 4321::1 remote-as 1
 no neighbor 4321::1 description
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family unicast multicast
 neighbor 4321::1 distance 200
 neighbor 4321::1 update-source loopback0
 redistribute connected
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.9
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
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
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.13 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:4::1 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.14
!
ipv6 route v1 :: :: 1234:4::2
!
ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.1.14
!
ipv6 mroute v1 :: :: 1234:4::2
!
!
!
!
!
ipv4 multicast v1 join-group 232.2.2.2 1.1.1.1
!
ipv6 multicast v1 join-group ff06::1 1234:1::1
!
!
!
!
end
```

## **Verification**

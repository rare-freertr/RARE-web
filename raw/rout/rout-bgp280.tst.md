# Example: unicast+olab over ebgp

## **Topology diagram**

![topology](/img/rout-bgp280.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz45r1-log.run
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
 ipv6 address 1234:1::1 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 003b.3671.4e62
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.2 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 0026.4370.011d
 vrf forwarding v1
 ipv4 address 3.3.4.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 4321::2 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast olab
 neighbor 1.1.1.2 remote-as 2
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast olab
 neighbor 1.1.1.2 distance 20
 afi-other enable
 afi-other redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast olab
 neighbor 1234:1::2 remote-as 2
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast olab
 neighbor 1234:1::2 distance 20
 afi-other enable
 afi-other redistribute connected
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
logging file debug ../binTmp/zzz45r2-log.run
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
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0034.3d3b.7705
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 002a.081a.6a04
 vrf forwarding v1
 ipv4 address 3.3.4.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 4321::1 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast olab
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast olab
 neighbor 1.1.1.1 distance 20
 afi-other enable
 afi-other redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast olab
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family unicast olab
 neighbor 1234:1::1 distance 20
 afi-other enable
 afi-other redistribute connected
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
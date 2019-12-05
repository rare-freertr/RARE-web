# Example: interop9: bgp vpnv6

## **Topology diagram**

![topology](/img/intop9-bgp13.tst.png)

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
 label-mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
vrf definition v3
 rd 1:3
 rt-import 1:3
 rt-export 1:3
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
interface loopback2
 no description
 vrf forwarding v2
 ipv4 address 9.9.2.1 255.255.255.255
 ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 no description
 vrf forwarding v3
 ipv4 address 9.9.3.1 255.255.255.255
 ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
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
 address-family ovpnuni
 neighbor 2.2.2.2 remote-as 1
 no neighbor 2.2.2.2 description
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family ovpnuni
 neighbor 2.2.2.2 distance 200
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family ovpnuni
 neighbor 4321::2 remote-as 1
 no neighbor 4321::2 description
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family ovpnuni
 neighbor 4321::2 distance 200
 neighbor 4321::2 update-source loopback0
 neighbor 4321::2 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
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
set interfaces ge-0/0/0.0 family inet6 address 1234::2/64
set interfaces ge-0/0/0.0 family mpls
set interfaces lo0.0 family inet address 2.2.2.2/32
set interfaces lo0.0 family inet6 address 4321::2/128
set interfaces lo0.2 family inet address 9.9.2.2/32
set interfaces lo0.2 family inet6 address 9992::2/128
set interfaces lo0.3 family inet address 9.9.3.2/32
set interfaces lo0.3 family inet6 address 9993::2/128
set protocols ldp interface ge-0/0/0.0
set protocols mpls interface ge-0/0/0.0
set protocols mpls ipv6-tunneling
set routing-options rib inet.0 static route 2.2.2.1/32 next-hop 1.1.1.1
set routing-options rib inet6.0 static route 4321::1/128 next-hop 1234::1
set routing-options autonomous-system 1
set protocols bgp group peers type internal
set protocols bgp group peers peer-as 1
set protocols bgp group peers neighbor 2.2.2.1
set protocols bgp group peers local-address 2.2.2.2
set protocols bgp group peers family inet6-vpn unicast
set routing-instances v2 instance-type vrf
set routing-instances v2 interface lo0.2
set routing-instances v2 route-distinguisher 1:2
set routing-instances v2 vrf-target target:1:2
set routing-instances v2 vrf-table-label
set routing-instances v3 instance-type vrf
set routing-instances v3 interface lo0.3
set routing-instances v3 route-distinguisher 1:3
set routing-instances v3 vrf-target target:1:3
set routing-instances v3 vrf-table-label
commit
```

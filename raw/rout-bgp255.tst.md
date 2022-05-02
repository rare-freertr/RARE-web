# Example: othervpns over confed bgp

## **Topology diagram**

![topology](/img/rout-bgp255.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz79r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt4import 1:2
 rt4export 1:2
 rt6import 1:2
 rt6export 1:2
 exit
!
vrf definition v3
 rd 1:3
 rt4import 1:3
 rt4export 1:3
 rt6import 1:3
 rt6export 1:3
 exit
!
vrf definition v4
 rd 1:4
 rt4import 1:4
 rt4export 1:4
 rt6import 1:4
 rt6export 1:4
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v2
 ipv4 address 9.9.2.1 255.255.255.255
 ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 vrf forwarding v3
 ipv4 address 9.9.3.1 255.255.255.255
 ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 vrf forwarding v4
 ipv4 address 9.9.4.1 255.255.255.255
 ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
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
 no safe-ebgp
 address-family ovpnuni
 neighbor 2.2.2.2 remote-as 2
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family ovpnuni
 neighbor 2.2.2.2 distance 20
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 confederation-peer
 neighbor 2.2.2.2 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family ovpnuni
 neighbor 4321::2 remote-as 2
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family ovpnuni
 neighbor 4321::2 distance 20
 neighbor 4321::2 update-source loopback0
 neighbor 4321::2 confederation-peer
 neighbor 4321::2 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 redistribute connected
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
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz79r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt4import 1:2
 rt4export 1:2
 rt6import 1:2
 rt6export 1:2
 exit
!
vrf definition v3
 rd 1:3
 rt4import 1:3
 rt4export 1:3
 rt6import 1:3
 rt6export 1:3
 exit
!
vrf definition v4
 rd 1:4
 rt4import 1:4
 rt4export 1:4
 rt6import 1:4
 rt6export 1:4
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v2
 ipv4 address 9.9.2.2 255.255.255.255
 ipv6 address 9992::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 vrf forwarding v3
 ipv4 address 9.9.3.2 255.255.255.255
 ipv6 address 9993::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 vrf forwarding v4
 ipv4 address 9.9.4.2 255.255.255.255
 ipv6 address 9994::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 no safe-ebgp
 address-family ovpnuni
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 2
 neighbor 2.2.2.1 address-family ovpnuni
 neighbor 2.2.2.1 distance 20
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 confederation-peer
 neighbor 2.2.2.1 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family ovpnuni
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 2
 neighbor 4321::1 address-family ovpnuni
 neighbor 4321::1 distance 20
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 confederation-peer
 neighbor 4321::1 send-community standard extended
 afi-ovrf v2 enable
 afi-ovrf v2 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 redistribute connected
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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

# Example: unicast+evpn/vpws over bgp additional path

## **Topology diagram**

![topology](/img/rout-bgp389.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz4r1-log.run
!
bridge 1
 rd 1:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 1:3
 rt-import 1:3
 rt-export 1:3
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 mac-learn
 private-bridge
 exit
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.255
 ipv6 address 4444::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv6 address 4444::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.252
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
 address-family unicast evpn
 neighbor 2.2.2.2 remote-as 2
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family unicast evpn
 neighbor 2.2.2.2 distance 20
 neighbor 2.2.2.2 additional-path-rx unicast evpn
 neighbor 2.2.2.2 additional-path-tx unicast evpn
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 pmsitun
 neighbor 2.2.2.2 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 007b.5e78.5622
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0016.386a.2006
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family unicast evpn
 neighbor 4321::2 remote-as 2
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family unicast evpn
 neighbor 4321::2 distance 20
 neighbor 4321::2 additional-path-rx unicast evpn
 neighbor 4321::2 additional-path-tx unicast evpn
 neighbor 4321::2 update-source loopback0
 neighbor 4321::2 pmsitun
 neighbor 4321::2 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 001e.412c.0538
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 007c.7b43.531b
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
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
logging file debug ../binTmp/zzz4r2-log.run
!
bridge 1
 rd 2:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 2
 rd 2:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 2:3
 rt-import 1:3
 rt-export 1:3
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 2:4
 rt-import 1:4
 rt-export 1:4
 mac-learn
 private-bridge
 exit
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.255
 ipv6 address 4444::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv6 address 4444::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.252
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
 address-family unicast evpn
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 2
 neighbor 2.2.2.1 address-family unicast evpn
 neighbor 2.2.2.1 distance 20
 neighbor 2.2.2.1 additional-path-rx unicast evpn
 neighbor 2.2.2.1 additional-path-tx unicast evpn
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 pmsitun
 neighbor 2.2.2.1 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 002e.7112.1410
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 000d.0e3a.4264
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family unicast evpn
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 2
 neighbor 4321::1 address-family unicast evpn
 neighbor 4321::1 distance 20
 neighbor 4321::1 additional-path-rx unicast evpn
 neighbor 4321::1 additional-path-tx unicast evpn
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 pmsitun
 neighbor 4321::1 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0008.6618.2407
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 002e.1d0e.7646
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
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

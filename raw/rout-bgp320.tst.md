# Example: bgp routemap filtering with afi with soft-reconfig

## **Topology diagram**

![topology](/img/rout-bgp320.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz79r1-log.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match safi 128
 sequence 10 match rd 1:3
 !
 sequence 20 action deny
 sequence 20 match safi 65
 sequence 20 match rd 1:2
 !
 sequence 30 action permit
 !
 exit
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
 rd 1:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 1:2
 rt-import 1:2
 rt-export 1:2
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
 address-family vpnuni vpls
 neighbor 2.2.2.3 remote-as 1
 neighbor 2.2.2.3 local-as 1
 neighbor 2.2.2.3 address-family vpnuni vpls
 neighbor 2.2.2.3 distance 200
 neighbor 2.2.2.3 update-source loopback0
 neighbor 2.2.2.3 soft-reconfiguration
 neighbor 2.2.2.3 send-community standard extended
 neighbor 2.2.2.3 vpn-route-map-in rm1
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 afi-vpls 1:1 bridge-group 1
 afi-vpls 1:1 update-source loopback0
 afi-vpls 1:2 bridge-group 3
 afi-vpls 1:2 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family vpnuni vpls
 neighbor 4321::3 remote-as 1
 neighbor 4321::3 local-as 1
 neighbor 4321::3 address-family vpnuni vpls
 neighbor 4321::3 distance 200
 neighbor 4321::3 update-source loopback0
 neighbor 4321::3 soft-reconfiguration
 neighbor 4321::3 send-community standard extended
 neighbor 4321::3 vpn-route-map-in rm1
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 afi-vpls 1:1 bridge-group 2
 afi-vpls 1:1 update-source loopback0
 afi-vpls 1:2 bridge-group 4
 afi-vpls 1:2 update-source loopback0
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
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.6
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
!
!
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
logging file debug ../binTmp/zzz79r3-log.run
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
 rd 1:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 1:2
 rt-import 1:2
 rt-export 1:2
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v2
 ipv4 address 9.9.2.3 255.255.255.255
 ipv6 address 9992::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 vrf forwarding v3
 ipv4 address 9.9.3.3 255.255.255.255
 ipv6 address 9993::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 vrf forwarding v4
 ipv4 address 9.9.4.3 255.255.255.255
 ipv6 address 9994::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
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
 router-id 4.4.4.3
 address-family vpnuni vpls
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family vpnuni vpls
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 soft-reconfiguration
 neighbor 2.2.2.1 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 afi-vpls 1:1 bridge-group 1
 afi-vpls 1:1 update-source loopback0
 afi-vpls 1:2 bridge-group 3
 afi-vpls 1:2 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family vpnuni vpls
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family vpnuni vpls
 neighbor 4321::1 distance 200
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 soft-reconfiguration
 neighbor 4321::1 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 afi-vpls 1:1 bridge-group 2
 afi-vpls 1:1 update-source loopback0
 afi-vpls 1:2 bridge-group 4
 afi-vpls 1:2 update-source loopback0
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.5
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.5
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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

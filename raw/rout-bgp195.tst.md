# Example: multisite evpn/vxlan over ibgp rr

## **Topology diagram**

![topology](/img/rout-bgp195.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz30r1-log.run
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
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.0
 ipv6 address 4444::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family evpn
 neighbor 1.1.1.4 remote-as 1
 neighbor 1.1.1.4 local-as 1
 neighbor 1.1.1.4 address-family evpn
 neighbor 1.1.1.4 distance 200
 neighbor 1.1.1.4 update-source loopback0
 neighbor 1.1.1.4 pmsitun
 neighbor 1.1.1.4 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 0018.2600.5f4d
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family evpn
 neighbor 1234:1::4 remote-as 1
 neighbor 1234:1::4 local-as 1
 neighbor 1234:1::4 address-family evpn
 neighbor 1234:1::4 distance 200
 neighbor 1234:1::4 update-source loopback0
 neighbor 1234:1::4 pmsitun
 neighbor 1234:1::4 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0041.2b6e.5c46
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.3
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
!
!
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
logging file debug ../binTmp/zzz30r2-log.run
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
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.0
 ipv6 address 4444::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.2
 address-family evpn
 neighbor 1.1.1.4 remote-as 1
 neighbor 1.1.1.4 local-as 1
 neighbor 1.1.1.4 address-family evpn
 neighbor 1.1.1.4 distance 200
 neighbor 1.1.1.4 update-source loopback0
 neighbor 1.1.1.4 pmsitun
 neighbor 1.1.1.4 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 0048.7377.580f
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.2
 address-family evpn
 neighbor 1234:1::4 remote-as 1
 neighbor 1234:1::4 local-as 1
 neighbor 1234:1::4 address-family evpn
 neighbor 1234:1::4 distance 200
 neighbor 1234:1::4 update-source loopback0
 neighbor 1234:1::4 pmsitun
 neighbor 1234:1::4 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0069.3272.1168
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.3
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
!
!
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
logging file debug ../binTmp/zzz30r3-log.run
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.0
 ipv6 address 3333::3 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv4 address 4.4.4.3 255.255.255.0
 ipv6 address 4444::3 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234:1::3 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family evpn
 neighbor 1.1.1.4 remote-as 1
 neighbor 1.1.1.4 local-as 1
 neighbor 1.1.1.4 address-family evpn
 neighbor 1.1.1.4 distance 200
 neighbor 1.1.1.4 update-source loopback0
 neighbor 1.1.1.4 pmsitun
 neighbor 1.1.1.4 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 0050.505e.7d60
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family evpn
 neighbor 1234:1::4 remote-as 1
 neighbor 1234:1::4 local-as 1
 neighbor 1234:1::4 address-family evpn
 neighbor 1234:1::4 distance 200
 neighbor 1234:1::4 update-source loopback0
 neighbor 1234:1::4 pmsitun
 neighbor 1234:1::4 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0032.422e.7e4f
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz30r4-log.run
!
bridge 1
 mac-learn
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234:1::4 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.4
 address-family evpn
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family evpn
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 pmsitun
 neighbor 2.2.2.1 route-reflector-client
 neighbor 2.2.2.1 send-community standard extended
 neighbor 2.2.2.2 remote-as 1
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family evpn
 neighbor 2.2.2.2 distance 200
 neighbor 2.2.2.2 pmsitun
 neighbor 2.2.2.2 route-reflector-client
 neighbor 2.2.2.2 send-community standard extended
 neighbor 2.2.2.3 remote-as 1
 neighbor 2.2.2.3 local-as 1
 neighbor 2.2.2.3 address-family evpn
 neighbor 2.2.2.3 distance 200
 neighbor 2.2.2.3 pmsitun
 neighbor 2.2.2.3 route-reflector-client
 neighbor 2.2.2.3 send-community standard extended
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.4
 address-family evpn
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family evpn
 neighbor 4321::1 distance 200
 neighbor 4321::1 pmsitun
 neighbor 4321::1 route-reflector-client
 neighbor 4321::1 send-community standard extended
 neighbor 4321::2 remote-as 1
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family evpn
 neighbor 4321::2 distance 200
 neighbor 4321::2 pmsitun
 neighbor 4321::2 route-reflector-client
 neighbor 4321::2 send-community standard extended
 neighbor 4321::3 remote-as 1
 neighbor 4321::3 local-as 1
 neighbor 4321::3 address-family evpn
 neighbor 4321::3 distance 200
 neighbor 4321::3 pmsitun
 neighbor 4321::3 route-reflector-client
 neighbor 4321::3 send-community standard extended
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
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.3
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
!
!
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

# Example: ethersite othervpns over ibgp

## **Topology diagram**

![topology](/img/rout-bgp258.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz5r1-log.run
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
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 vrf forwarding v2
 ipv4 address 9.8.2.1 255.255.255.0
 ipv6 address 9982::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.13
 vrf forwarding v3
 ipv4 address 9.8.3.1 255.255.255.0
 ipv6 address 9983::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.14
 vrf forwarding v4
 ipv4 address 9.8.4.1 255.255.255.0
 ipv6 address 9984::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family ovpnuni
 neighbor 2.2.2.3 remote-as 1
 neighbor 2.2.2.3 local-as 1
 neighbor 2.2.2.3 address-family ovpnuni
 neighbor 2.2.2.3 distance 200
 neighbor 2.2.2.3 update-source loopback0
 neighbor 2.2.2.3 send-community standard extended
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
 address-family ovpnuni
 neighbor 4321::3 remote-as 1
 neighbor 4321::3 local-as 1
 neighbor 4321::3 address-family ovpnuni
 neighbor 4321::3 distance 200
 neighbor 4321::3 update-source loopback0
 neighbor 4321::3 send-community standard extended
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
logging file debug ../binTmp/zzz5r2-log.run
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
logging file debug ../binTmp/zzz5r3-log.run
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
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 vrf forwarding v2
 ipv4 address 9.7.2.1 255.255.255.0
 ipv6 address 9972::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.13
 vrf forwarding v3
 ipv4 address 9.7.3.1 255.255.255.0
 ipv6 address 9973::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.14
 vrf forwarding v4
 ipv4 address 9.7.4.1 255.255.255.0
 ipv6 address 9974::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family ovpnuni
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family ovpnuni
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 update-source loopback0
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
 local-as 1
 router-id 6.6.6.3
 address-family ovpnuni
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family ovpnuni
 neighbor 4321::1 distance 200
 neighbor 4321::1 update-source loopback0
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz5r4-log.run
!
vrf definition tester
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
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v2
 ipv4 address 9.8.2.2 255.255.255.0
 ipv6 address 9982::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 vrf forwarding v3
 ipv4 address 9.8.3.2 255.255.255.0
 ipv6 address 9983::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.14
 vrf forwarding v4
 ipv4 address 9.8.4.2 255.255.255.0
 ipv6 address 9984::2 ffff:ffff:ffff:ffff::
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
ipv4 route v2 0.0.0.0 0.0.0.0 9.8.2.1
!
ipv6 route v2 :: :: 9982::1
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v3 0.0.0.0 0.0.0.0 9.8.3.1
!
ipv6 route v3 :: :: 9983::1
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v4 0.0.0.0 0.0.0.0 9.8.4.1
!
ipv6 route v4 :: :: 9984::1
!
!
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

**r5:**
```
hostname r5
buggy
!
logging file debug ../binTmp/zzz5r5-log.run
!
vrf definition tester
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
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v2
 ipv4 address 9.7.2.2 255.255.255.0
 ipv6 address 9972::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 vrf forwarding v3
 ipv4 address 9.7.3.2 255.255.255.0
 ipv6 address 9973::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.14
 vrf forwarding v4
 ipv4 address 9.7.4.2 255.255.255.0
 ipv6 address 9974::2 ffff:ffff:ffff:ffff::
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
ipv4 route v2 0.0.0.0 0.0.0.0 9.7.2.1
!
ipv6 route v2 :: :: 9972::1
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v3 0.0.0.0 0.0.0.0 9.7.3.1
!
ipv6 route v3 :: :: 9973::1
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v4 0.0.0.0 0.0.0.0 9.7.4.1
!
ipv6 route v4 :: :: 9974::1
!
!
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

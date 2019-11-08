# Example: ethersite vpns over ibgp

## **Topology diagram**

![topology](/img/rout-bgp142.tst.png)

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
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
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
interface loopback4
 no description
 vrf forwarding v4
 ipv4 address 9.9.4.1 255.255.255.255
 ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 no description
 vrf forwarding v2
 ipv4 address 9.8.2.1 255.255.255.0
 ipv6 address 9982::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.13
 no description
 vrf forwarding v3
 ipv4 address 9.8.3.1 255.255.255.0
 ipv6 address 9983::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.14
 no description
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
 address-family vpnuni
 neighbor 2.2.2.3 remote-as 1
 no neighbor 2.2.2.3 description
 neighbor 2.2.2.3 local-as 1
 neighbor 2.2.2.3 address-family vpnuni
 neighbor 2.2.2.3 distance 200
 neighbor 2.2.2.3 update-source loopback0
 neighbor 2.2.2.3 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family vpnuni
 neighbor 4321::3 remote-as 1
 no neighbor 4321::3 description
 neighbor 4321::3 local-as 1
 neighbor 4321::3 address-family vpnuni
 neighbor 4321::3 distance 200
 neighbor 4321::3 update-source loopback0
 neighbor 4321::3 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 exit
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
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
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
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
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
interface loopback2
 no description
 vrf forwarding v2
 ipv4 address 9.9.2.3 255.255.255.255
 ipv6 address 9992::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 no description
 vrf forwarding v3
 ipv4 address 9.9.3.3 255.255.255.255
 ipv6 address 9993::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 no description
 vrf forwarding v4
 ipv4 address 9.9.4.3 255.255.255.255
 ipv6 address 9994::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 no description
 vrf forwarding v2
 ipv4 address 9.7.2.1 255.255.255.0
 ipv6 address 9972::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.13
 no description
 vrf forwarding v3
 ipv4 address 9.7.3.1 255.255.255.0
 ipv6 address 9973::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.14
 no description
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
 address-family vpnuni
 neighbor 2.2.2.1 remote-as 1
 no neighbor 2.2.2.1 description
 neighbor 2.2.2.1 local-as 1
 neighbor 2.2.2.1 address-family vpnuni
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family vpnuni
 neighbor 4321::1 remote-as 1
 no neighbor 4321::1 description
 neighbor 4321::1 local-as 1
 neighbor 4321::1 address-family vpnuni
 neighbor 4321::1 distance 200
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 redistribute connected
 exit
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
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v2
 ipv4 address 9.8.2.2 255.255.255.0
 ipv6 address 9982::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 no description
 vrf forwarding v3
 ipv4 address 9.8.3.2 255.255.255.0
 ipv6 address 9983::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.14
 no description
 vrf forwarding v4
 ipv4 address 9.8.4.2 255.255.255.0
 ipv6 address 9984::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
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
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v2
 ipv4 address 9.7.2.2 255.255.255.0
 ipv6 address 9972::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 no description
 vrf forwarding v3
 ipv4 address 9.7.3.2 255.255.255.0
 ipv6 address 9973::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.14
 no description
 vrf forwarding v4
 ipv4 address 9.7.4.2 255.255.255.0
 ipv6 address 9974::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
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
!
end
```

## **Verification**

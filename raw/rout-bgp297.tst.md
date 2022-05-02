# Example: bgp csc vpn with ldp

## **Topology diagram**

![topology](/img/rout-bgp297.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz17r1-log.run
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
vrf definition v3
 rd 1:3
 rt4import 1:3
 rt4export 1:3
 rt6import 1:3
 rt6export 1:3
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
 vrf forwarding v3
 ipv4 address 4.4.4.1 255.255.255.255
 ipv6 address 4444::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
router bgp4 4
 vrf v1
 local-as 4
 router-id 4.4.4.1
 no safe-ebgp
 address-family vpnuni
 neighbor 2.2.2.4 remote-as 4
 neighbor 2.2.2.4 local-as 4
 neighbor 2.2.2.4 address-family vpnuni
 neighbor 2.2.2.4 distance 200
 neighbor 2.2.2.4 update-source loopback0
 neighbor 2.2.2.4 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 exit
!
router bgp6 4
 vrf v1
 local-as 4
 router-id 6.6.6.1
 no safe-ebgp
 address-family vpnuni
 neighbor 4321::4 remote-as 4
 neighbor 4321::4 local-as 4
 neighbor 4321::4 address-family vpnuni
 neighbor 4321::4 distance 200
 neighbor 4321::4 update-source loopback0
 neighbor 4321::4 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
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
ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz17r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
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
 label4mode per-prefix
 label6mode per-prefix
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 3.3.3.101 255.255.255.255
 ipv6 address 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v2
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v2
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 2
 vrf v1
 local-as 2
 router-id 4.4.4.1
 no safe-ebgp
 address-family vpnuni
 neighbor 3.3.3.102 remote-as 2
 neighbor 3.3.3.102 local-as 2
 neighbor 3.3.3.102 address-family vpnuni
 neighbor 3.3.3.102 distance 200
 neighbor 3.3.3.102 update-source loopback0
 neighbor 3.3.3.102 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
router bgp6 2
 vrf v1
 local-as 2
 router-id 6.6.6.1
 no safe-ebgp
 address-family vpnuni
 neighbor 3333::102 remote-as 2
 neighbor 3333::102 local-as 2
 neighbor 3333::102 address-family vpnuni
 neighbor 3333::102 distance 200
 neighbor 3333::102 update-source loopback0
 neighbor 3333::102 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
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
ipv4 route v1 3.3.3.102 255.255.255.255 3.3.3.2
!
ipv6 route v1 3333::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 3333::2
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v2 2.2.2.1 255.255.255.255 1.1.1.1
!
ipv6 route v2 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
!
!
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
logging file debug ../binTmp/zzz17r3-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
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
interface ethernet1
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 3.3.3.5 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 3333::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 ipv6 access-group-in test6
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
ipv4 route v1 3.3.3.101 255.255.255.255 3.3.3.1
ipv4 route v1 3.3.3.102 255.255.255.255 3.3.3.6
!
ipv6 route v1 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 3333::1
ipv6 route v1 3333::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 3333::6
!
!
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
logging file debug ../binTmp/zzz17r4-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
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
 label4mode per-prefix
 label6mode per-prefix
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 3.3.3.102 255.255.255.255
 ipv6 address 3333::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v2
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 3.3.3.6 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 3333::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v2
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 2
 vrf v1
 local-as 2
 router-id 4.4.4.2
 no safe-ebgp
 address-family vpnuni
 neighbor 3.3.3.101 remote-as 2
 neighbor 3.3.3.101 local-as 2
 neighbor 3.3.3.101 address-family vpnuni
 neighbor 3.3.3.101 distance 200
 neighbor 3.3.3.101 update-source loopback0
 neighbor 3.3.3.101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
router bgp6 2
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family vpnuni
 neighbor 3333::101 remote-as 2
 neighbor 3333::101 local-as 2
 neighbor 3333::101 address-family vpnuni
 neighbor 3333::101 distance 200
 neighbor 3333::101 update-source loopback0
 neighbor 3333::101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
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
ipv4 route v1 3.3.3.101 255.255.255.255 3.3.3.5
!
ipv6 route v1 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 3333::5
!
!
!
!
!
!
!
!
!
!
!
!
ipv4 route v2 2.2.2.4 255.255.255.255 1.1.1.6
!
ipv6 route v2 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
!
!
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
logging file debug ../binTmp/zzz17r5-log.run
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
vrf definition v3
 rd 1:3
 rt4import 1:3
 rt4export 1:3
 rt6import 1:3
 rt6export 1:3
 label4mode per-prefix
 label6mode per-prefix
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v3
 ipv4 address 4.4.4.4 255.255.255.255
 ipv6 address 4444::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
router bgp4 4
 vrf v1
 local-as 4
 router-id 4.4.4.2
 no safe-ebgp
 address-family vpnuni
 neighbor 2.2.2.1 remote-as 4
 neighbor 2.2.2.1 local-as 4
 neighbor 2.2.2.1 address-family vpnuni
 neighbor 2.2.2.1 distance 200
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
 exit
!
router bgp6 4
 vrf v1
 local-as 4
 router-id 6.6.6.2
 no safe-ebgp
 address-family vpnuni
 neighbor 4321::1 remote-as 4
 neighbor 4321::1 local-as 4
 neighbor 4321::1 address-family vpnuni
 neighbor 4321::1 distance 200
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 redistribute connected
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
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.5
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
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
!
!
!
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

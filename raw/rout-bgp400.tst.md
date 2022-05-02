# Example: ebgp with php labels

## **Topology diagram**

![topology](/img/rout-bgp400.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz46r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 mtu 1500
 macaddr 002b.540b.5352
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 mtu 1500
 macaddr 005a.5879.1127
 vrf forwarding v1
 ipv4 address 3.3.4.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 4321::3 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 no safe-ebgp
 address-family labeled
 neighbor 1.1.1.2 remote-as 2
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family labeled
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 label-pop
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family labeled
 neighbor 1234:1::2 remote-as 2
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family labeled
 neighbor 1234:1::2 distance 20
 neighbor 1234:1::2 label-pop
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
!
!
!
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
logging file debug ../binTmp/zzz46r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
 ipv4 access-group-in test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 no safe-ebgp
 address-family labeled
 neighbor 1.1.1.1 remote-as 1
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family labeled
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 label-pop
 neighbor 1.1.1.6 remote-as 3
 neighbor 1.1.1.6 local-as 2
 neighbor 1.1.1.6 address-family labeled
 neighbor 1.1.1.6 distance 20
 neighbor 1.1.1.6 label-pop
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family labeled
 neighbor 1234:1::1 remote-as 1
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family labeled
 neighbor 1234:1::1 distance 20
 neighbor 1234:1::1 label-pop
 neighbor 1234:2::2 remote-as 3
 neighbor 1234:2::2 local-as 2
 neighbor 1234:2::2 address-family labeled
 neighbor 1234:2::2 distance 20
 neighbor 1234:2::2 label-pop
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
!
!
!
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
logging file debug ../binTmp/zzz46r3-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 mtu 1500
 macaddr 000b.6c03.0d1b
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 mtu 1500
 macaddr 007c.3a2e.0951
 vrf forwarding v1
 ipv4 address 3.3.4.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 4321::1 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 3
 router-id 4.4.4.3
 no safe-ebgp
 address-family labeled
 neighbor 1.1.1.5 remote-as 2
 neighbor 1.1.1.5 local-as 3
 neighbor 1.1.1.5 address-family labeled
 neighbor 1.1.1.5 distance 20
 neighbor 1.1.1.5 label-pop
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 3
 router-id 6.6.6.3
 no safe-ebgp
 address-family labeled
 neighbor 1234:2::1 remote-as 2
 neighbor 1234:2::1 local-as 3
 neighbor 1234:2::1 address-family labeled
 neighbor 1234:2::1 distance 20
 neighbor 1234:2::1 label-pop
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
!
!
!
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

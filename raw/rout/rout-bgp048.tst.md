# Example: bgp listen

## **Topology diagram**

![topology](/img/rout-bgp048.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz8r1-log.run
!
access-list all
 sequence 10 permit all any all any all
 exit
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 template p remote-as 2
 no template p description
 template p local-as 1
 template p address-family unicast
 template p distance 20
 template p override-peer-as-out
 listen all p
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 template p remote-as 2
 no template p description
 template p local-as 1
 template p address-family unicast
 template p distance 20
 template p override-peer-as-out
 listen all p
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
logging file debug ../binTmp/zzz8r2-log.run
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
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 20
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
logging file debug ../binTmp/zzz8r3-log.run
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.5 remote-as 1
 no neighbor 1.1.1.5 description
 neighbor 1.1.1.5 local-as 2
 neighbor 1.1.1.5 address-family unicast
 neighbor 1.1.1.5 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:2::1 remote-as 1
 no neighbor 1234:2::1 description
 neighbor 1234:2::1 local-as 2
 neighbor 1234:2::1 address-family unicast
 neighbor 1234:2::1 distance 20
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz8r4-log.run
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
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.4
 address-family unicast
 neighbor 1.1.1.9 remote-as 1
 no neighbor 1.1.1.9 description
 neighbor 1.1.1.9 local-as 2
 neighbor 1.1.1.9 address-family unicast
 neighbor 1.1.1.9 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.4
 address-family unicast
 neighbor 1234:3::1 remote-as 1
 no neighbor 1234:3::1 description
 neighbor 1234:3::1 local-as 2
 neighbor 1234:3::1 address-family unicast
 neighbor 1234:3::1 distance 20
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

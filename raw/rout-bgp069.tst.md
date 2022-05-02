# Example: confed bgp in chain with soft-reconfig

## **Topology diagram**

![topology](/img/rout-bgp069.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz49r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 no safe-ebgp
 address-family unicast
 neighbor 1.1.1.2 remote-as 2
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 soft-reconfiguration
 neighbor 1.1.1.2 confederation-peer
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family unicast
 neighbor 1234:1::2 remote-as 2
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 20
 neighbor 1234:1::2 soft-reconfiguration
 neighbor 1234:1::2 confederation-peer
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
logging file debug ../binTmp/zzz49r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 no safe-ebgp
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 soft-reconfiguration
 neighbor 1.1.1.1 confederation-peer
 neighbor 1.1.1.6 remote-as 3
 neighbor 1.1.1.6 local-as 2
 neighbor 1.1.1.6 address-family unicast
 neighbor 1.1.1.6 distance 20
 neighbor 1.1.1.6 soft-reconfiguration
 neighbor 1.1.1.6 confederation-peer
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 neighbor 1234:1::1 local-as 2
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 20
 neighbor 1234:1::1 soft-reconfiguration
 neighbor 1234:1::1 confederation-peer
 neighbor 1234:2::2 remote-as 3
 neighbor 1234:2::2 local-as 2
 neighbor 1234:2::2 address-family unicast
 neighbor 1234:2::2 distance 20
 neighbor 1234:2::2 soft-reconfiguration
 neighbor 1234:2::2 confederation-peer
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
logging file debug ../binTmp/zzz49r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 3
 router-id 4.4.4.3
 no safe-ebgp
 address-family unicast
 neighbor 1.1.1.5 remote-as 2
 neighbor 1.1.1.5 local-as 3
 neighbor 1.1.1.5 address-family unicast
 neighbor 1.1.1.5 distance 20
 neighbor 1.1.1.5 soft-reconfiguration
 neighbor 1.1.1.5 confederation-peer
 neighbor 1.1.1.10 remote-as 4
 neighbor 1.1.1.10 local-as 3
 neighbor 1.1.1.10 address-family unicast
 neighbor 1.1.1.10 distance 20
 neighbor 1.1.1.10 soft-reconfiguration
 neighbor 1.1.1.10 confederation-peer
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 3
 router-id 6.6.6.3
 no safe-ebgp
 address-family unicast
 neighbor 1234:2::1 remote-as 2
 neighbor 1234:2::1 local-as 3
 neighbor 1234:2::1 address-family unicast
 neighbor 1234:2::1 distance 20
 neighbor 1234:2::1 soft-reconfiguration
 neighbor 1234:2::1 confederation-peer
 neighbor 1234:3::2 remote-as 4
 neighbor 1234:3::2 local-as 3
 neighbor 1234:3::2 address-family unicast
 neighbor 1234:3::2 distance 20
 neighbor 1234:3::2 soft-reconfiguration
 neighbor 1234:3::2 confederation-peer
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
logging file debug ../binTmp/zzz49r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 4
 router-id 4.4.4.4
 no safe-ebgp
 address-family unicast
 neighbor 1.1.1.9 remote-as 3
 neighbor 1.1.1.9 local-as 4
 neighbor 1.1.1.9 address-family unicast
 neighbor 1.1.1.9 distance 20
 neighbor 1.1.1.9 soft-reconfiguration
 neighbor 1.1.1.9 confederation-peer
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 4
 router-id 6.6.6.4
 no safe-ebgp
 address-family unicast
 neighbor 1234:3::1 remote-as 3
 neighbor 1234:3::1 local-as 4
 neighbor 1234:3::1 address-family unicast
 neighbor 1234:3::1 distance 20
 neighbor 1234:3::1 soft-reconfiguration
 neighbor 1234:3::1 confederation-peer
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

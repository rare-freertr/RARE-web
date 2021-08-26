# Example: ibgp rr with labels

## **Topology diagram**

![topology](/img/rout-bgp403.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz56r1-log.run
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
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.11 255.255.255.255
 ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0042.2c61.0d4d
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback1 pweompls 2.2.2.12 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 0043.3471.1621
 vrf forwarding v1
 ipv4 address 3.3.4.1 255.255.255.0
 pseudowire v1 loopback1 pweompls 4321::12 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family labeled
 neighbor 1.1.1.3 remote-as 1
 no neighbor 1.1.1.3 description
 neighbor 1.1.1.3 local-as 1
 neighbor 1.1.1.3 address-family labeled
 neighbor 1.1.1.3 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family labeled
 neighbor 1234::3 remote-as 1
 no neighbor 1234::3 description
 neighbor 1234::3 local-as 1
 neighbor 1234::3 address-family labeled
 neighbor 1234::3 distance 200
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
logging file debug ../binTmp/zzz56r2-log.run
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
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.12 255.255.255.255
 ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0071.2073.462f
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback1 pweompls 2.2.2.11 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 002f.2f01.5b27
 vrf forwarding v1
 ipv4 address 3.3.4.2 255.255.255.0
 pseudowire v1 loopback1 pweompls 4321::11 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.2
 address-family labeled
 neighbor 1.1.1.3 remote-as 1
 no neighbor 1.1.1.3 description
 neighbor 1.1.1.3 local-as 1
 neighbor 1.1.1.3 address-family labeled
 neighbor 1.1.1.3 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.2
 address-family labeled
 neighbor 1234::3 remote-as 1
 no neighbor 1234::3 description
 neighbor 1234::3 local-as 1
 neighbor 1234::3 address-family labeled
 neighbor 1234::3 distance 200
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
logging file debug ../binTmp/zzz56r3-log.run
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.13 255.255.255.255
 ipv6 address 4321::13 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family labeled
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family labeled
 neighbor 1.1.1.1 distance 200
 neighbor 1.1.1.1 route-reflector-client
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family labeled
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 route-reflector-client
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family labeled
 neighbor 1234::1 remote-as 1
 no neighbor 1234::1 description
 neighbor 1234::1 local-as 1
 neighbor 1234::1 address-family labeled
 neighbor 1234::1 distance 200
 neighbor 1234::1 route-reflector-client
 neighbor 1234::2 remote-as 1
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family labeled
 neighbor 1234::2 distance 200
 neighbor 1234::2 route-reflector-client
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

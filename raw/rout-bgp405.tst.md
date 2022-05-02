# Example: bgp route server with labels

## **Topology diagram**

![topology](/img/rout-bgp405.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz19r1-log.run
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 mtu 1500
 macaddr 006e.3a1a.7b6c
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 mtu 1500
 macaddr 0038.0e40.0f4b
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
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family labeled
 neighbor 1234::2 remote-as 2
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family labeled
 neighbor 1234::2 distance 20
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
logging file debug ../binTmp/zzz19r2-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff:ffff::
 mpls enable
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
 neighbor 1.1.1.1 route-server-client
 neighbor 1.1.1.3 remote-as 3
 neighbor 1.1.1.3 local-as 2
 neighbor 1.1.1.3 address-family labeled
 neighbor 1.1.1.3 distance 20
 neighbor 1.1.1.3 route-server-client
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family labeled
 neighbor 1234::1 remote-as 1
 neighbor 1234::1 local-as 2
 neighbor 1234::1 address-family labeled
 neighbor 1234::1 distance 20
 neighbor 1234::1 route-server-client
 neighbor 1234::3 remote-as 3
 neighbor 1234::3 local-as 2
 neighbor 1234::3 address-family labeled
 neighbor 1234::3 distance 20
 neighbor 1234::3 route-server-client
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
logging file debug ../binTmp/zzz19r3-log.run
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
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff:ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 mtu 1500
 macaddr 0065.5f5a.493c
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 mtu 1500
 macaddr 0016.2845.466e
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
 neighbor 1.1.1.2 remote-as 2
 neighbor 1.1.1.2 local-as 3
 neighbor 1.1.1.2 address-family labeled
 neighbor 1.1.1.2 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 3
 router-id 6.6.6.3
 no safe-ebgp
 address-family labeled
 neighbor 1234::2 remote-as 2
 neighbor 1234::2 local-as 3
 neighbor 1234::2 address-family labeled
 neighbor 1234::2 distance 20
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

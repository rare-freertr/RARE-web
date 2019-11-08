# Example: interop1: bgp with labels

## **Topology diagram**

![topology](/img/intop1-bgp08.tst.png)

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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 003d.7059.4674
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family labeled
 neighbor 1.1.1.2 remote-as 2
 no neighbor 1.1.1.2 description
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
 address-family labeled
 neighbor 1234:1::2 remote-as 2
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family labeled
 neighbor 1234:1::2 distance 20
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
end
```

**r2:**
```
hostname r2
ip routing
ipv6 unicast-routing
interface loopback0
 ip addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
interface gigabit2
 ip address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2/64
 mpls bgp forwarding
 no shutdown
 exit
interface gigabit1
 ip address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2/64
 mpls bgp forwarding
 no shutdown
 exit
router bgp 2
 address-family ipv4 unicast
  bgp scan-time 5
  neighbor 1.1.1.1 remote-as 1
  neighbor 1.1.1.1 send-label explicit-null
  neighbor 1.1.2.1 remote-as 3
  neighbor 1.1.2.1 send-label explicit-null
  redistribute connected
 address-family ipv6 unicast
  bgp scan-time 5
  neighbor 1234:1::1 remote-as 1
  neighbor 1234:1::1 send-label
  neighbor 1234:2::1 remote-as 3
  neighbor 1234:2::1 send-label
  redistribute connected
 exit
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
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1234:2::1 ffff::
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0039.7760.6b42
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 3
 router-id 4.4.4.3
 address-family labeled
 neighbor 1.1.2.2 remote-as 2
 no neighbor 1.1.2.2 description
 neighbor 1.1.2.2 local-as 3
 neighbor 1.1.2.2 address-family labeled
 neighbor 1.1.2.2 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 3
 router-id 6.6.6.3
 address-family labeled
 neighbor 1234:2::2 remote-as 2
 no neighbor 1234:2::2 description
 neighbor 1234:2::2 local-as 3
 neighbor 1234:2::2 address-family labeled
 neighbor 1234:2::2 distance 20
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
end
```

## **Verification**

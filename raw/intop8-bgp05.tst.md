# Example: interop8: bgp metric

## **Topology diagram**

![topology](/img/intop8-bgp05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match metric 1234
 !
 sequence 20 action permit
 !
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 route-map-in rm1
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234::2 remote-as 1
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family unicast
 neighbor 1234::2 distance 200
 neighbor 1234::2 route-map-in rm1
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
ip forwarding
ipv6 forwarding
interface lo
 ip addr 2.2.2.2/32
 ip addr 2.2.2.3/32
 ip addr 2.2.2.4/32
 ipv6 addr 4321::2/128
 ipv6 addr 4321::3/128
 ipv6 addr 4321::4/128
 exit
interface ens3
 ip address 1.1.1.2/24
 ipv6 address 1234::2/64
 no shutdown
 exit
ip prefix-list pl1 seq 5 permit 2.2.2.3/32
route-map rm1 permit 10
 match ip address prefix-list pl1
 set metric 1234
route-map rm1 permit 20
 set metric 4321
ipv6 prefix-list pl2 seq 5 permit 4321::3/128
route-map rm2 permit 10
 match ipv6 address prefix-list pl2
 set metric 1234
route-map rm2 permit 20
 set metric 4321
router bgp 1
 neighbor 1.1.1.1 remote-as 1
 neighbor 1234::1 remote-as 1
 address-family ipv4 unicast
  neighbor 1.1.1.1 activate
  no neighbor 1234::1 activate
  redistribute connected route-map rm1
 address-family ipv6 unicast
  no neighbor 1.1.1.1 activate
  neighbor 1234::1 activate
  redistribute connected route-map rm2
 exit
```

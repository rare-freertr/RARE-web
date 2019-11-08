# Example: interop2: bgp community

## **Topology diagram**

![topology](/img/intop2-bgp06.tst.png)

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
 sequence 10 match stdcomm 1234:4321
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
 neighbor 1.1.1.2 send-community standard extended
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
 neighbor 1234::2 send-community standard extended
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
interface loopback0
 ipv4 addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
interface loopback1
 ipv4 addr 2.2.2.3 255.255.255.255
 ipv6 addr 4321::3/128
 exit
interface loopback2
 ipv4 addr 2.2.2.4 255.255.255.255
 ipv6 addr 4321::4/128
 exit
interface gigabit0/0/0/0
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2/64
 no shutdown
 exit
route-policy rp1
 if destination in (2.2.2.3/32, 4321::3/128) then
  set community (1234:4321)
 else
  set community (1234:1234)
 endif
 pass
 end-policy
router bgp 1
 address-family ipv4 unicast
  redistribute connected route-policy rp1
 address-family ipv6 unicast
  redistribute connected route-policy rp1
 neighbor 1.1.1.1
  remote-as 1
  address-family ipv4 unicast
 neighbor 1234::1
  remote-as 1
  address-family ipv6 unicast
root
commit
```

## **Verification**

# Example: interop2: bgp 6pe

## **Topology diagram**

![topology](/img/intop2-bgp21.tst.png)

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
 mpls enable
 mpls ldp4
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family other
 neighbor 2.2.2.2 remote-as 1
 no neighbor 2.2.2.2 description
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family other
 neighbor 2.2.2.2 distance 200
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 send-community standard extended
 afi-other redistribute connected
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
!
!
!
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
interface gigabit0/0/0/0
 ipv4 address 1.1.1.2 255.255.255.0
 no shutdown
 exit
mpls ldp
 address-family ipv4
 interface gigabit0/0/0/0
  address-family ipv4
router static
 address-family ipv4 unicast 2.2.2.1/32 1.1.1.1 gigabit0/0/0/0
 exit
router bgp 1
 address-family ipv4 unicast
  allocate-label all
  redistribute connected
 address-family ipv6 unicast
  allocate-label all
  redistribute connected
 neighbor 2.2.2.1
  remote-as 1
  update-source loopback0
  address-family ipv4 labeled-unicast
  address-family ipv6 labeled-unicast
root
commit
```

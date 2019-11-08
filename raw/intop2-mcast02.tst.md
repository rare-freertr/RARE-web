# Example: interop2: pim

## **Topology diagram**

![topology](/img/intop2-mcast02.tst.png)

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
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv4 pim enable
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 pim enable
 ipv6 address 1234::1 ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
!
!
!
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
interface gigabit0/0/0/0
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 addr 1234::2/64
 no shutdown
 exit
interface loopback0
 ipv4 addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
router static
 address-family ipv4 unicast 2.2.2.1/32 gigabit0/0/0/0 1.1.1.1
 address-family ipv6 unicast 4321::1/128 gigabit0/0/0/0 1234::1
multicast-routing
 address-family ipv4
  interface Loopback0 enable
  interface gigabit0/0/0/0 enable
  static-rpf 2.2.2.1 32 gigabit0/0/0/0 1.1.1.1
 address-family ipv6
  interface Loopback0 enable
  interface gigabit0/0/0/0 enable
  static-rpf 4321::1 128 gigabit0/0/0/0 1234::1
router pim
 address-family ipv4
  interface Loopback0 enable
  interface gigabit0/0/0/0 enable
 address-family ipv6
  interface Loopback0 enable
  interface gigabit0/0/0/0 enable
router igmp interface Loopback0
  join-group 232.2.2.2 2.2.2.1
  version 3
router mld interface Loopback0
  join-group ff06::1 4321::1
  version 2
router igmp
root
commit
```

## **Verification**

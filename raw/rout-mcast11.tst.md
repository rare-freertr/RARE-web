# Example: multicast routing decoupled from unicast

## **Topology diagram**

![topology](/img/rout-mcast11.tst.png)

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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
ipv6 route v1 :: :: 1234:1::2
!
!
!
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
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:3::2 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv4 pim enable
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 pim enable
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.6
!
ipv6 route v1 :: :: 1234:2::2
!
ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.1.10
!
ipv6 mroute v1 :: :: 1234:3::2
!
!
!
!
!
ipv4 multicast v1 join-group 232.2.2.2 1.1.1.1
!
ipv6 multicast v1 join-group ff06::1 1234:1::1
!
!
!
!
end
```

## **Verification**

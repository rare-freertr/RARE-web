# Example: multicast routing with pim join source

## **Topology diagram**

![topology](/img/rout-mcast12.tst.png)

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
interface loopback1
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
 ipv4 pim enable
 ipv4 pim join-source loopback1
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 pim enable
 ipv6 pim join-source loopback1
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
interface loopback1
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
 ipv4 pim enable
 ipv4 pim join-source loopback1
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 pim enable
 ipv6 pim join-source loopback1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 pim enable
 ipv4 pim join-source loopback1
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 pim enable
 ipv6 pim join-source loopback1
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
interface loopback1
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
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 pim enable
 ipv4 pim join-source loopback1
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 pim enable
 ipv6 pim join-source loopback1
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.6
!
ipv6 route v1 :: :: 1234:2::2
!
ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.1.6
!
ipv6 mroute v1 :: :: 1234:2::2
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

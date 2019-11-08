# Example: policy routing with nexthop

## **Topology diagram**

![topology](/img/rout-pbr01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list a2b4
 sequence 10 permit all 2.2.2.101 255.255.255.255 all 2.2.2.201 255.255.255.255 all
 exit
!
access-list a2b6
 sequence 10 permit all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.101 255.255.255.255
 ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
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
ipv4 pbr v1 sequence 10 a2b4 v1 nexthop 1.1.1.2
!
ipv6 pbr v1 sequence 10 a2b6 v1 nexthop 1234:1::2
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
access-list a2b4
 sequence 10 permit all 2.2.2.101 255.255.255.255 all 2.2.2.201 255.255.255.255 all
 exit
!
access-list a2b6
 sequence 10 permit all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 exit
!
access-list b2a4
 sequence 10 permit all 2.2.2.201 255.255.255.255 all 2.2.2.101 255.255.255.255 all
 exit
!
access-list b2a6
 sequence 10 permit all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
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
!
!
!
!
!
!
!
ipv4 pbr v1 sequence 10 a2b4 v1 nexthop 1.1.1.5
ipv4 pbr v1 sequence 20 b2a4 v1 nexthop 1.1.1.1
!
ipv6 pbr v1 sequence 10 a2b6 v1 nexthop 1234:2::1
ipv6 pbr v1 sequence 20 b2a6 v1 nexthop 1234:1::1
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
access-list b2a4
 sequence 10 permit all 2.2.2.201 255.255.255.255 all 2.2.2.101 255.255.255.255 all
 exit
!
access-list b2a6
 sequence 10 permit all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.201 255.255.255.255
 ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
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
!
!
!
!
!
!
!
ipv4 pbr v1 sequence 10 b2a4 v1 nexthop 1.1.1.6
!
ipv6 pbr v1 sequence 10 b2a6 v1 nexthop 1234:2::2
!
!
!
!
!
!
end
```

## **Verification**

```
r2#
r2#
r2#show ipv4 pbr v1
r2#show ipv4 pbr v1
 sequence 10 a2b4 v1 nexthop 1.1.1.5
  match=14 packets (1288 bytes)
 sequence 20 b2a4 v1 nexthop 1.1.1.1
  match=13 packets (1196 bytes)
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pbr v1
r2#show ipv6 pbr v1
 sequence 10 a2b6 v1 nexthop 1234:2::1
  match=10 packets (1120 bytes)
 sequence 20 b2a6 v1 nexthop 1234:1::1
  match=10 packets (1120 bytes)
r2#
r2#
```

# Example: ldp over ethernet

## **Topology diagram**

![topology](/img/mpls-ldp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
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
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
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
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
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

```
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf  | iface     | hop     | label      | targets | bytes |
 |--------|------|-----------|---------|------------|---------|-------|
 | 508172 | v1:6 | ethernet1 | 1234::2 | 242488     |         | 0     |
 | 699474 | v1:6 | null      | null    | unlabelled | local   | 1120  |
 | 701351 | v1:4 | ethernet1 | 1.1.1.2 | 488991     |         | 0     |
 | 744882 | v1:4 | null      | null    | unlabelled | local   | 1288  |
 |________|______|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 sum
r1#show ipv4 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | learn | advert | l2learn | l2advert | mplearn | mpadvert | neighbor | uptime   |
 |-------|--------|---------|----------|---------|----------|----------|----------|
 | 4     | 4      | 0       | 0        | 0       | 0        | 1.1.1.2  | 00:00:21 |
 |_______|________|_________|__________|_________|__________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 sum
r1#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | learn | advert | l2learn | l2advert | mplearn | mpadvert | neighbor | uptime   |
 |-------|--------|---------|----------|---------|----------|----------|----------|
 | 4     | 4      | 0       | 0        | 0       | 0        | 1234::2  | 00:00:21 |
 |_______|________|_________|__________|_________|__________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 dat
r1#show ipv4 ldp v1 dat
 |~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix     | local  | remote | hop     |
 |------------|--------|--------|---------|
 | 1.1.1.0/24 | 744882 |        | null    |
 | 1.1.1.1/32 | 744882 |        | null    |
 | 2.2.2.1/32 | 744882 |        | null    |
 | 2.2.2.2/32 | 701351 | 488991 | 1.1.1.2 |
 |____________|________|________|_________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 dat
r1#show ipv6 ldp v1 dat
 |~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix      | local  | remote | hop     |
 |-------------|--------|--------|---------|
 | 1234::/16   | 699474 |        | null    |
 | 1234::1/128 | 699474 |        | null    |
 | 4321::1/128 | 699474 |        | null    |
 | 4321::2/128 | 508172 | 242488 | 1234::2 |
 |_____________|________|________|_________|
r1#
r1#
```

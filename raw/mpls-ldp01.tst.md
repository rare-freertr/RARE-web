# Example: ldp over ethernet

## **Topology diagram**

![topology](/img/mpls-ldp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz40r1-log.run
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
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
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
 no ipv4 unreachables
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 no ipv6 unreachables
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
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
logging file debug ../binTmp/zzz40r2-log.run
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
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
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
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 no ipv4 unreachables
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 no ipv6 unreachables
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
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

## **Verification**

```
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop     | label      | targets | bytes |
 |--------|----------|-----------|---------|------------|---------|-------|
 | 162435 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 206546 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 307899 | v1:6     | null      | null    | unlabelled | local   | 832   |
 | 382899 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 597167 | v1:6     | ethernet1 | 1234::2 | 742349     |         | 0     |
 | 644427 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 666383 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 796240 | v1:4     | ethernet1 | 1.1.1.2 | 623954     |         | 0     |
 | 848574 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 915725 | v1:4     | null      | null    | unlabelled | local   | 768   |
 |________|__________|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 sum
r1#show ipv4 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                     |
 | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
 |-------|--------|-------|--------|-------|--------|----------|----------|
 | 4     | 4      | 0     | 0      | 0     | 0      | 1.1.1.2  | 00:00:20 |
 |_______|________|_______|________|_______|________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 sum
r1#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                     |
 | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
 |-------|--------|-------|--------|-------|--------|----------|----------|
 | 4     | 4      | 0     | 0      | 0     | 0      | 1234::2  | 00:00:20 |
 |_______|________|_______|________|_______|________|__________|__________|
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
 | 1.1.1.0/24 | 915725 |        | null    |
 | 1.1.1.1/32 | 915725 |        | null    |
 | 2.2.2.1/32 | 915725 |        | null    |
 | 2.2.2.2/32 | 796240 | 623954 | 1.1.1.2 |
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
 | 1234::/16   | 307899 |        | null    |
 | 1234::1/128 | 307899 |        | null    |
 | 4321::1/128 | 307899 |        | null    |
 | 4321::2/128 | 597167 | 742349 | 1234::2 |
 |_____________|________|________|_________|
r1#
r1#
```

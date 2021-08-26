# Example: static routing with labels

## **Topology diagram**

![topology](/img/rout-static06.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz21r1-log.run
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
 ipv4 access-group-in test4
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2 mplsexp
!
ipv6 route v1 :: :: 1234:1::2 mplsexp
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
logging file debug ../binTmp/zzz21r2-log.run
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
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.222 255.255.255.255
 ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
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
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1 mplsexp
ipv4 route v1 2.2.2.201 255.255.255.255 1.1.1.5 mplsexp
!
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1 mplsexp
ipv6 route v1 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1 mplsexp
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz21r3-log.run
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
 ipv4 access-group-in test4
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.6 mplsexp
!
ipv6 route v1 :: :: 1234:2::2 mplsexp
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
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix       | metric | iface     | hop     | time     |
 |-----|--------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:05 |
 | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:05 |
 | C   | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:05 |
 | LOC | 1.1.1.6/32   | 0/1    | ethernet2 | null    | 00:00:05 |
 | S   | 2.2.2.101/32 | 1/0    | ethernet1 | 1.1.1.1 | 00:00:05 |
 | S   | 2.2.2.201/32 | 1/0    | ethernet2 | 1.1.1.5 | 00:00:05 |
 | C   | 2.2.2.222/32 | 0/0    | loopback0 | null    | 00:00:05 |
 |_____|______________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric | iface     | hop       | time     |
 |-----|---------------|--------|-----------|-----------|----------|
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:05 |
 | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:05 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:05 |
 | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:05 |
 | S   | 4321::101/128 | 1/0    | ethernet1 | 1234:1::1 | 00:00:05 |
 | S   | 4321::201/128 | 1/0    | ethernet2 | 1234:2::1 | 00:00:05 |
 | C   | 4321::222/128 | 0/0    | loopback0 | null      | 00:00:05 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

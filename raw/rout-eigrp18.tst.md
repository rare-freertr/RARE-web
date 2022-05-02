# Example: eigrp auto mesh tunnel

## **Topology diagram**

![topology](/img/rout-eigrp18.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz54r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
prefix-list all
 sequence 10 permit 0.0.0.0/0 ge 0 le 32
 sequence 20 permit ::/0 ge 0 le 128
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
router eigrp4 1
 vrf v1
 router-id 4.4.4.1
 as 1
 redistribute connected
 automesh all
 exit
!
router eigrp6 1
 vrf v1
 router-id 6.6.6.1
 as 1
 redistribute connected
 automesh all
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
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 9999::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router eigrp4 1 enable
 router eigrp6 1 enable
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
logging file debug ../binTmp/zzz54r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
prefix-list all
 sequence 10 permit 0.0.0.0/0 ge 0 le 32
 sequence 20 permit ::/0 ge 0 le 128
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
router eigrp4 1
 vrf v1
 router-id 4.4.4.2
 as 1
 redistribute connected
 automesh all
 exit
!
router eigrp6 1
 vrf v1
 router-id 6.6.6.2
 as 1
 redistribute connected
 automesh all
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
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 9999::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router eigrp4 1 enable
 router eigrp6 1 enable
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
r2#show ipv4 eigrp 1 sum
r2#show ipv4 eigrp 1 sum
 |~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface   | peer    | learned | adverted | uptime   |
 |---------|---------|---------|----------|----------|
 | serial1 | 9.9.9.1 | 1       | 1        | 00:00:03 |
 |_________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 eigrp 1 sum
r2#show ipv6 eigrp 1 sum
 |~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface   | peer    | learned | adverted | uptime   |
 |---------|---------|---------|----------|----------|
 | serial1 | 9999::1 | 1       | 1        | 00:00:03 |
 |_________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 eigrp 1 rou
r2#show ipv4 eigrp 1 rou
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | null | 2.2.2.1/32 | 90/10  | serial1   | 9.9.9.1 | 00:00:03 |
 | C    | 2.2.2.2/32 | 0/0    | loopback0 | null    | 00:00:04 |
 | C    | 9.9.9.0/24 | 0/0    | serial1   | null    | 00:00:04 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 eigrp 1 rou
r2#show ipv6 eigrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop     | time     |
 |------|-------------|--------|-----------|---------|----------|
 | null | 4321::1/128 | 90/10  | serial1   | 9999::1 | 00:00:03 |
 | C    | 4321::2/128 | 0/0    | loopback0 | null    | 00:00:04 |
 | C    | 9999::/16   | 0/0    | serial1   | null    | 00:00:04 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | D   | 2.2.2.1/32 | 90/10  | serial1   | 9.9.9.1 | 00:00:03 |
 | C   | 2.2.2.2/32 | 0/0    | loopback0 | null    | 00:00:09 |
 | C   | 9.9.9.0/24 | 0/0    | serial1   | null    | 00:00:04 |
 | MSH | 9.9.9.1/32 | 0/3    | serial1   | 9.9.9.1 | never    |
 | LOC | 9.9.9.2/32 | 0/1    | serial1   | null    | 00:00:04 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | D   | 4321::1/128 | 90/10  | serial1   | 9999::1 | 00:00:04 |
 | C   | 4321::2/128 | 0/0    | loopback0 | null    | 00:00:09 |
 | C   | 9999::/16   | 0/0    | serial1   | null    | 00:00:04 |
 | MSH | 9999::1/128 | 0/3    | serial1   | 9999::1 | never    |
 | LOC | 9999::2/128 | 0/1    | serial1   | null    | 00:00:04 |
 |_____|_____________|________|___________|_________|__________|
r2#
r2#
```

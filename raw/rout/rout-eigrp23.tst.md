# Example: eigrp ecmp connection

## **Topology diagram**

![topology](/img/rout-eigrp23.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz21r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router eigrp4 1
 vrf v1
 router-id 4.4.4.1
 as 1
 redistribute connected
 ecmp
 exit
!
router eigrp6 1
 vrf v1
 router-id 6.6.6.1
 as 1
 redistribute connected
 ecmp
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.252
 ipv6 address 1234:21::1 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.10 255.255.255.252
 ipv6 address 1234:23::2 ffff:ffff::
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
logging file debug ../binTmp/zzz21r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router eigrp4 1
 vrf v1
 router-id 4.4.4.2
 as 1
 redistribute connected
 ecmp
 exit
!
router eigrp6 1
 vrf v1
 router-id 6.6.6.2
 as 1
 redistribute connected
 ecmp
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.252
 ipv6 address 1234:21::2 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.5 255.255.255.252
 ipv6 address 1234:22::1 ffff:ffff::
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz21r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router eigrp4 1
 vrf v1
 router-id 4.4.4.3
 as 1
 redistribute connected
 ecmp
 exit
!
router eigrp6 1
 vrf v1
 router-id 6.6.6.3
 as 1
 redistribute connected
 ecmp
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.6 255.255.255.252
 ipv6 address 1234:22::2 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 router eigrp4 1 enable
 router eigrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.9 255.255.255.252
 ipv6 address 1234:23::1 ffff:ffff::
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
 |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface        | peer    | learned | adverted | uptime   |
 |--------------|---------|---------|----------|----------|
 | ethernet1.11 | 1.1.1.1 | 7       | 8        | 00:00:05 |
 | ethernet1.22 | 1.1.2.1 | 8       | 6        | 00:00:05 |
 | ethernet2.11 | 1.1.1.6 | 7       | 7        | 00:00:05 |
 | ethernet2.22 | 1.1.2.6 | 8       | 7        | 00:00:05 |
 |______________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 eigrp 1 sum
r2#show ipv6 eigrp 1 sum
 |~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface        | peer       | learned | adverted | uptime   |
 |--------------|------------|---------|----------|----------|
 | ethernet1.11 | 1234:1::1  | 5       | 8        | 00:00:05 |
 | ethernet1.22 | 1234:21::1 | 8       | 6        | 00:00:05 |
 | ethernet2.11 | 1234:2::2  | 7       | 7        | 00:00:05 |
 | ethernet2.22 | 1234:22::2 | 7       | 7        | 00:00:05 |
 |______________|____________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 eigrp 1 rou
r2#show ipv4 eigrp 1 rou
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface        | hop     | time     |
 |------|------------|--------|--------------|---------|----------|
 | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:06 |
 | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:06 |
 | null | 1.1.1.8/30 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
 | null | 1.1.1.8/30 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
 | null | 1.1.1.8/30 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
 | null | 1.1.1.8/30 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:02 |
 | C    | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:06 |
 | C    | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:06 |
 | null | 1.1.2.8/30 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:04 |
 | null | 1.1.2.8/30 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:04 |
 | null | 1.1.2.8/30 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:04 |
 | null | 1.1.2.8/30 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:04 |
 | null | 2.2.2.1/32 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
 | null | 2.2.2.1/32 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:06 |
 | null | 2.2.2.3/32 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:03 |
 | null | 2.2.2.3/32 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:05 |
 |______|____________|________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 eigrp 1 rou
r2#show ipv6 eigrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric | iface        | hop        | time     |
 |------|--------------|--------|--------------|------------|----------|
 | C    | 1234:1::/32  | 0/0    | ethernet1.11 | null       | 00:00:06 |
 | C    | 1234:2::/32  | 0/0    | ethernet2.11 | null       | 00:00:06 |
 | null | 1234:3::/32  | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
 | null | 1234:3::/32  | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:03 |
 | null | 1234:3::/32  | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:03 |
 | null | 1234:3::/32  | 90/10  | ethernet2.22 | 1234:22::2 | 00:00:03 |
 | C    | 1234:21::/32 | 0/0    | ethernet1.22 | null       | 00:00:06 |
 | C    | 1234:22::/32 | 0/0    | ethernet2.22 | null       | 00:00:06 |
 | null | 1234:23::/32 | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
 | null | 1234:23::/32 | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:05 |
 | null | 1234:23::/32 | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:05 |
 | null | 4321::1/128  | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
 | null | 4321::1/128  | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:05 |
 | C    | 4321::2/128  | 0/0    | loopback1    | null       | 00:00:06 |
 | null | 4321::3/128  | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:05 |
 | null | 4321::3/128  | 90/10  | ethernet2.22 | 1234:22::2 | 00:00:05 |
 |______|______________|________|______________|____________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface        | hop     | time     |
 |-----|------------|--------|--------------|---------|----------|
 | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:06 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:06 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:06 |
 | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:06 |
 | D   | 1.1.1.8/30 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
 | D   | 1.1.1.8/30 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
 | D   | 1.1.1.8/30 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
 | D   | 1.1.1.8/30 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:02 |
 | C   | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:06 |
 | LOC | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:06 |
 | C   | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:06 |
 | LOC | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:06 |
 | D   | 1.1.2.8/30 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:04 |
 | D   | 1.1.2.8/30 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:04 |
 | D   | 1.1.2.8/30 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:04 |
 | D   | 1.1.2.8/30 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:04 |
 | D   | 2.2.2.1/32 | 90/10  | ethernet1.11 | 1.1.1.1 | 00:00:03 |
 | D   | 2.2.2.1/32 | 90/10  | ethernet1.22 | 1.1.2.1 | 00:00:03 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:06 |
 | D   | 2.2.2.3/32 | 90/10  | ethernet2.11 | 1.1.1.6 | 00:00:05 |
 | D   | 2.2.2.3/32 | 90/10  | ethernet2.22 | 1.1.2.6 | 00:00:05 |
 |_____|____________|________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix         | metric | iface        | hop        | time     |
 |-----|----------------|--------|--------------|------------|----------|
 | C   | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:06 |
 | LOC | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:06 |
 | C   | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:06 |
 | LOC | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:06 |
 | D   | 1234:3::/32    | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:03 |
 | D   | 1234:3::/32    | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:03 |
 | D   | 1234:3::/32    | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:03 |
 | D   | 1234:3::/32    | 90/10  | ethernet2.22 | 1234:22::2 | 00:00:03 |
 | C   | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:06 |
 | LOC | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:06 |
 | C   | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:06 |
 | LOC | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:06 |
 | D   | 1234:23::/32   | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
 | D   | 1234:23::/32   | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:05 |
 | D   | 1234:23::/32   | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:05 |
 | D   | 4321::1/128    | 90/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
 | D   | 4321::1/128    | 90/10  | ethernet1.22 | 1234:21::1 | 00:00:05 |
 | C   | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:06 |
 | D   | 4321::3/128    | 90/10  | ethernet2.11 | 1234:2::2  | 00:00:05 |
 | D   | 4321::3/128    | 90/10  | ethernet2.22 | 1234:22::2 | 00:00:05 |
 |_____|________________|________|______________|____________|__________|
r2#
r2#
```

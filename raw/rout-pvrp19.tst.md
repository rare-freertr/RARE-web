# Example: pvrp with bfd

## **Topology diagram**

![topology](/img/rout-pvrp19.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz59r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.1
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.1
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 bfd 100 100 3
 router pvrp4 1 enable
 router pvrp4 1 bfd
 router pvrp6 1 enable
 router pvrp6 1 bfd
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 bfd 100 100 3
 router pvrp4 1 enable
 router pvrp4 1 bfd
 router pvrp4 1 metric-in 100
 router pvrp6 1 enable
 router pvrp6 1 bfd
 router pvrp6 1 metric-in 100
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
logging file debug ../binTmp/zzz59r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.2
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.2
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 bfd 100 100 3
 router pvrp4 1 enable
 router pvrp4 1 bfd
 router pvrp6 1 enable
 router pvrp6 1 bfd
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 bfd 100 100 3
 router pvrp4 1 enable
 router pvrp4 1 bfd
 router pvrp4 1 metric-in 100
 router pvrp6 1 enable
 router pvrp6 1 bfd
 router pvrp6 1 metric-in 100
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
r2#show ipv4 pvrp 1 sum
r2#show ipv4 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
 |-----------|---------|------|-----------|---------|---------|----------|----------|
 | ethernet2 | 4.4.4.1 | r1   | ethernet2 | 1.1.1.5 | 2       | 1        | 00:00:11 |
 |___________|_________|______|___________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 sum
r2#show ipv6 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer      | learned | adverted | uptime   |
 |-----------|---------|------|-----------|-----------|---------|----------|----------|
 | ethernet2 | 6.6.6.1 | r1   | ethernet2 | 1234:2::1 | 2       | 1        | 00:00:11 |
 |___________|_________|______|___________|___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 pvrp 1 rou
r2#show ipv4 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | null | 1.1.1.0/30 | 80/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C    | 1.1.1.4/30 | 1/0    | ethernet2 | null    | 00:00:02 |
 | null | 2.2.2.1/32 | 80/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:02 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 rou
r2#show ipv6 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop       | time     |
 |------|-------------|--------|-----------|-----------|----------|
 | null | 1234:1::/32 | 80/100 | ethernet2 | 1234:2::1 | 00:00:07 |
 | C    | 1234:2::/32 | 1/0    | ethernet2 | null      | 00:00:02 |
 | null | 4321::1/128 | 80/100 | ethernet2 | 1234:2::1 | 00:00:07 |
 | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:02 |
 |______|_____________|________|___________|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | P    | 1.1.1.0/30 | 80/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:17 |
 | LOC  | 1.1.1.6/32 | 0/1    | ethernet2 | null    | 00:00:17 |
 | P EX | 2.2.2.1/32 | 80/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:17 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric | iface     | hop       | time     |
 |------|---------------|--------|-----------|-----------|----------|
 | P    | 1234:1::/32   | 80/100 | ethernet2 | 1234:2::1 | 00:00:07 |
 | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:17 |
 | LOC  | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:17 |
 | P EX | 4321::1/128   | 80/100 | ethernet2 | 1234:2::1 | 00:00:07 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:17 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

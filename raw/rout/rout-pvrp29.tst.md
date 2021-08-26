# Example: pvrp prefix movement

## **Topology diagram**

![topology](/img/rout-pvrp29.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz10r1-log.run
!
route-map rm1
 sequence 10 action permit
 sequence 10 set metric set 10
 !
 exit
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
 advertise 2.2.2.1/32 route-map rm1
 advertise 2.2.2.222/32 route-map rm1
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.1
 advertise 4321::1/128 route-map rm1
 advertise 4321::222/128 route-map rm1
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
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.222 255.255.255.255
 ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
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
 router pvrp4 1 enable
 router pvrp6 1 enable
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
server telnet tel
 port 666
 no exec authorization
 no login authentication
 vrf v1
 exit
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
logging file debug ../binTmp/zzz10r2-log.run
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
 advertise 2.2.2.2/32
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.2
 advertise 4321::2/128
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
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
logging file debug ../binTmp/zzz10r3-log.run
!
route-map rm1
 sequence 10 action permit
 sequence 10 set metric set 20
 !
 exit
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
 router-id 4.4.4.3
 advertise 2.2.2.3/32 route-map rm1
 advertise 2.2.2.222/32 route-map rm1
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.3
 advertise 4321::3/128 route-map rm1
 advertise 4321::222/128 route-map rm1
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
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.222 255.255.255.255
 ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.103 255.255.255.255
 ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
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
server telnet tel
 port 666
 no exec authorization
 no login authentication
 vrf v1
 exit
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
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 2       | 3        | 00:00:26 |
 | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.1.6 | 2       | 4        | 00:00:26 |
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
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 2       | 3        | 00:00:26 |
 | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1234:2::2 | 2       | 4        | 00:00:26 |
 |___________|_________|______|___________|___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 pvrp 1 rou
r2#show ipv4 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric | iface     | hop     | time     |
 |------|--------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30   | 1/0    | ethernet1 | null    | 00:00:06 |
 | C    | 1.1.1.4/30   | 1/0    | ethernet2 | null    | 00:00:06 |
 | null | 2.2.2.1/32   | 80/20  | ethernet1 | 1.1.1.1 | 00:00:06 |
 | C    | 2.2.2.2/32   | 1/0    | loopback1 | null    | 00:00:06 |
 | null | 2.2.2.3/32   | 80/30  | ethernet2 | 1.1.1.6 | 00:00:22 |
 | null | 2.2.2.222/32 | 80/20  | ethernet1 | 1.1.1.1 | 00:00:06 |
 |______|______________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 rou
r2#show ipv6 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric | iface     | hop       | time     |
 |------|---------------|--------|-----------|-----------|----------|
 | C    | 1234:1::/32   | 1/0    | ethernet1 | null      | 00:00:06 |
 | C    | 1234:2::/32   | 1/0    | ethernet2 | null      | 00:00:06 |
 | null | 4321::1/128   | 80/20  | ethernet1 | 1234:1::1 | 00:00:06 |
 | C    | 4321::2/128   | 1/0    | loopback1 | null      | 00:00:06 |
 | null | 4321::3/128   | 80/30  | ethernet2 | 1234:2::2 | 00:00:23 |
 | null | 4321::222/128 | 80/20  | ethernet1 | 1234:1::1 | 00:00:06 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric | iface     | hop     | time     |
 |------|--------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:31 |
 | LOC  | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:31 |
 | C    | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:31 |
 | LOC  | 1.1.1.5/32   | 0/1    | ethernet2 | null    | 00:00:31 |
 | P EX | 2.2.2.1/32   | 80/20  | ethernet1 | 1.1.1.1 | 00:00:07 |
 | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:31 |
 | P EX | 2.2.2.3/32   | 80/30  | ethernet2 | 1.1.1.6 | 00:00:23 |
 | P EX | 2.2.2.222/32 | 80/20  | ethernet1 | 1.1.1.1 | 00:00:07 |
 |______|______________|________|___________|_________|__________|
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:31 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:31 |
 | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:31 |
 | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:31 |
 | P EX | 4321::1/128   | 80/20  | ethernet1 | 1234:1::1 | 00:00:07 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:32 |
 | P EX | 4321::3/128   | 80/30  | ethernet2 | 1234:2::2 | 00:00:24 |
 | P EX | 4321::222/128 | 80/20  | ethernet1 | 1234:1::1 | 00:00:07 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

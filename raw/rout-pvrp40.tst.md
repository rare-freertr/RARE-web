# Example: pvrp peer metric

## **Topology diagram**

![topology](/img/rout-pvrp40.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz48r1-log.run
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
router pvrp4 1
 vrf v1
 router-id 4.4.4.1
 labels
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.1
 labels
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 router pvrp4 1 enable
 router pvrp4 1 metric-in 100
 router pvrp6 1 enable
 router pvrp6 1 metric-in 100
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1235::1 ffff::
 mpls enable
 router pvrp4 1 enable
 router pvrp4 1 metric-in 1
 router pvrp6 1 enable
 router pvrp6 1 metric-in 1
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
logging file debug ../binTmp/zzz48r2-log.run
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
router pvrp4 1
 vrf v1
 router-id 4.4.4.2
 labels
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.2
 labels
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
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 mpls enable
 router pvrp4 1 enable
 router pvrp4 1 accept-metric
 router pvrp4 1 metric-in 2
 router pvrp6 1 enable
 router pvrp6 1 accept-metric
 router pvrp6 1 metric-in 2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1235::2 ffff::
 mpls enable
 router pvrp4 1 enable
 router pvrp4 1 accept-metric
 router pvrp4 1 metric-in 200
 router pvrp6 1 enable
 router pvrp6 1 accept-metric
 router pvrp6 1 metric-in 200
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
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 2       | 3        | 00:00:08 |
 | ethernet2 | 4.4.4.1 | r1   | ethernet2 | 1.1.2.1 | 2       | 2        | 00:00:08 |
 |___________|_________|______|___________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 sum
r2#show ipv6 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
 |-----------|---------|------|-----------|---------|---------|----------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | 2       | 3        | 00:00:08 |
 | ethernet2 | 6.6.6.1 | r1   | ethernet2 | 1235::1 | 2       | 2        | 00:00:08 |
 |___________|_________|______|___________|_________|_________|__________|__________|
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
 | C    | 1.1.1.0/24 | 1/0    | ethernet1 | null    | 00:00:02 |
 | C    | 1.1.2.0/24 | 1/0    | ethernet2 | null    | 00:00:02 |
 | null | 2.2.2.1/32 | 80/1   | ethernet2 | 1.1.2.1 | 00:00:02 |
 | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:13 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 rou
r2#show ipv6 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop     | time     |
 |------|-------------|--------|-----------|---------|----------|
 | C    | 1234::/16   | 1/0    | ethernet1 | null    | 00:00:04 |
 | C    | 1235::/16   | 1/0    | ethernet2 | null    | 00:00:04 |
 | null | 4321::1/128 | 80/1   | ethernet2 | 1235::1 | 00:00:05 |
 | C    | 4321::2/128 | 2/0    | loopback1 | null    | 00:00:13 |
 |______|_____________|________|___________|_________|__________|
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
 | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:14 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:14 |
 | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:13 |
 | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:13 |
 | P EX | 2.2.2.1/32 | 80/1   | ethernet2 | 1.1.2.1 | 00:00:03 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:14 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop     | time     |
 |------|-------------|--------|-----------|---------|----------|
 | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:14 |
 | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:14 |
 | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:13 |
 | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:13 |
 | P EX | 4321::1/128 | 80/1   | ethernet2 | 1235::1 | 00:00:05 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:14 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

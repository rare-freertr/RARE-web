# Example: pvrp point2multipoint connection

## **Topology diagram**

![topology](/img/rout-pvrp02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz65r1-log.run
!
bridge 1
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
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
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
logging file debug ../binTmp/zzz65r2-log.run
!
bridge 1
 mac-learn
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
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 bridge-group 1
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
logging file debug ../binTmp/zzz65r3-log.run
!
bridge 1
 mac-learn
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
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.3
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 bridge-group 1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz65r4-log.run
!
bridge 1
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
 router-id 4.4.4.4
 redistribute connected
 exit
!
router pvrp6 1
 vrf v1
 router-id 6.6.6.4
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234::4 ffff::
 router pvrp4 1 enable
 router pvrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
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
 |~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface | router  | name | peerif | peer    | learned | adverted | uptime   |
 |-------|---------|------|--------|---------|---------|----------|----------|
 | bvi1  | 4.4.4.1 | r1   | bvi1   | 1.1.1.1 | 1       | 1        | 00:00:11 |
 | bvi1  | 4.4.4.3 | r3   | bvi1   | 1.1.1.3 | 1       | 1        | 00:00:11 |
 | bvi1  | 4.4.4.4 | r4   | bvi1   | 1.1.1.4 | 1       | 1        | 00:00:11 |
 |_______|_________|______|________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 sum
r2#show ipv6 pvrp 1 sum
 |~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface | router  | name | peerif | peer    | learned | adverted | uptime   |
 |-------|---------|------|--------|---------|---------|----------|----------|
 | bvi1  | 6.6.6.1 | r1   | bvi1   | 1234::1 | 1       | 1        | 00:00:11 |
 | bvi1  | 6.6.6.3 | r3   | bvi1   | 1234::3 | 1       | 1        | 00:00:11 |
 | bvi1  | 6.6.6.4 | r4   | bvi1   | 1234::4 | 1       | 1        | 00:00:11 |
 |_______|_________|______|________|_________|_________|__________|__________|
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
 | C    | 1.1.1.0/24 | 1/0    | bvi1      | null    | 00:00:06 |
 | null | 2.2.2.1/32 | 80/10  | bvi1      | 1.1.1.1 | 00:00:06 |
 | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:16 |
 | null | 2.2.2.3/32 | 80/10  | bvi1      | 1.1.1.3 | 00:00:08 |
 | null | 2.2.2.4/32 | 80/10  | bvi1      | 1.1.1.4 | 00:00:06 |
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
 | C    | 1234::/16   | 1/0    | bvi1      | null    | 00:00:06 |
 | null | 4321::1/128 | 80/10  | bvi1      | 1234::1 | 00:00:06 |
 | C    | 4321::2/128 | 2/0    | loopback1 | null    | 00:00:16 |
 | null | 4321::3/128 | 80/10  | bvi1      | 1234::3 | 00:00:06 |
 | null | 4321::4/128 | 80/10  | bvi1      | 1234::4 | 00:00:08 |
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
 | C    | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:16 |
 | LOC  | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:16 |
 | P EX | 2.2.2.1/32 | 80/10  | bvi1      | 1.1.1.1 | 00:00:07 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:16 |
 | P EX | 2.2.2.3/32 | 80/10  | bvi1      | 1.1.1.3 | 00:00:08 |
 | P EX | 2.2.2.4/32 | 80/10  | bvi1      | 1.1.1.4 | 00:00:06 |
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
 | C    | 1234::/16   | 0/0    | bvi1      | null    | 00:00:16 |
 | LOC  | 1234::2/128 | 0/1    | bvi1      | null    | 00:00:16 |
 | P EX | 4321::1/128 | 80/10  | bvi1      | 1234::1 | 00:00:07 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:17 |
 | P EX | 4321::3/128 | 80/10  | bvi1      | 1234::3 | 00:00:07 |
 | P EX | 4321::4/128 | 80/10  | bvi1      | 1234::4 | 00:00:08 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

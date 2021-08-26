# Example: lsrp point2multipoint connection with bidir check

## **Topology diagram**

![topology](/img/rout-lsrp37.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz85r1-log.run
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.1
 spf-bidir
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
 spf-bidir
 redistribute connected
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
logging file debug ../binTmp/zzz85r2-log.run
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.2
 spf-bidir
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
 spf-bidir
 redistribute connected
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
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
logging file debug ../binTmp/zzz85r3-log.run
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.3
 spf-bidir
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
 spf-bidir
 redistribute connected
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
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
logging file debug ../binTmp/zzz85r4-log.run
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.4
 spf-bidir
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.4
 spf-bidir
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234::4 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface | router  | name | peerif | peer    | ready | uptime   |
 |-------|---------|------|--------|---------|-------|----------|
 | bvi1  | 4.4.4.1 | r1   | bvi1   | 1.1.1.1 | true  | 00:00:09 |
 | bvi1  | 4.4.4.3 | r3   | bvi1   | 1.1.1.3 | true  | 00:00:09 |
 | bvi1  | 4.4.4.4 | r4   | bvi1   | 1.1.1.4 | true  | 00:00:09 |
 |_______|_________|______|________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 nei
r2#show ipv6 lsrp 1 nei
 |~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface | router  | name | peerif | peer    | ready | uptime   |
 |-------|---------|------|--------|---------|-------|----------|
 | bvi1  | 6.6.6.1 | r1   | bvi1   | 1234::1 | true  | 00:00:10 |
 | bvi1  | 6.6.6.3 | r3   | bvi1   | 1234::3 | true  | 00:00:10 |
 | bvi1  | 6.6.6.4 | r4   | bvi1   | 1234::4 | true  | 00:00:10 |
 |_______|_________|______|________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 dat
r2#show ipv4 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 4.4.4.1 | r1   | 3   | 2   | 8   | 2cda3740 | 00:59:55 |
 | 4.4.4.2 | r2   | 3   | 2   | 8   | 0b58797e | 00:59:55 |
 | 4.4.4.3 | r3   | 3   | 2   | 9   | 2cda3740 | 00:59:55 |
 | 4.4.4.4 | r4   | 3   | 2   | 9   | 31400d77 | 00:59:53 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 dat
r2#show ipv6 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 6.6.6.1 | r1   | 3   | 2   | 7   | b525f480 | 00:59:55 |
 | 6.6.6.2 | r2   | 3   | 2   | 8   | b525f480 | 00:59:55 |
 | 6.6.6.3 | r3   | 3   | 2   | 9   | 13a84c3e | 00:59:54 |
 | 6.6.6.4 | r4   | 3   | 2   | 9   | 7ec3997c | 00:59:54 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 tre
r2#show ipv4 lsrp 1 tre
`--r2
  |`--r1
  |`--r3
   `--r4
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 tre
r2#show ipv6 lsrp 1 tre
`--r2
  |`--r1
  |`--r3
   `--r4
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
 | C    | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:15 |
 | LOC  | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:15 |
 | L EX | 2.2.2.1/32 | 70/10  | bvi1      | 1.1.1.1 | 00:00:04 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:15 |
 | L EX | 2.2.2.3/32 | 70/10  | bvi1      | 1.1.1.3 | 00:00:05 |
 | L EX | 2.2.2.4/32 | 70/10  | bvi1      | 1.1.1.4 | 00:00:06 |
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
 | C    | 1234::/16   | 0/0    | bvi1      | null    | 00:00:15 |
 | LOC  | 1234::2/128 | 0/1    | bvi1      | null    | 00:00:15 |
 | L EX | 4321::1/128 | 70/10  | bvi1      | 1234::1 | 00:00:04 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:15 |
 | L EX | 4321::3/128 | 70/10  | bvi1      | 1234::3 | 00:00:05 |
 | L EX | 4321::4/128 | 70/10  | bvi1      | 1234::4 | 00:00:08 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```
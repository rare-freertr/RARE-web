# Example: isis chain of broadcast nets with bidir check

## **Topology diagram**

![topology](/img/rout-isis62.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz1r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv6 address 1234:1::1 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
logging file debug ../binTmp/zzz1r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.2222.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.2222.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv6 address 1234:1::2 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 no description
 vrf forwarding v1
 ipv6 address 1234:2::1 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
logging file debug ../binTmp/zzz1r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.3333.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.3333.00
 traffeng-id ::
 is-type both
 level2 spf-bidir
 level1 spf-bidir
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv6 address 1234:2::2 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
r2#show ipv4 isis 1 nei
r2#show ipv4 isis 1 nei
 |~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |--------------|----------------|-------|----------------|------------|---------------|-------|----------|
 | ethernet1.11 | 0000.0000.1111 | 1     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:06 |
 | ethernet1.11 | 0000.0000.1111 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:06 |
 | ethernet2.11 | 0000.0000.3333 | 1     | 4444.0000.3333 | 1.1.1.6    | ::            | 0     | 00:00:06 |
 | ethernet2.11 | 0000.0000.3333 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | 0     | 00:00:06 |
 |______________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 nei
r2#show ipv6 isis 1 nei
 |~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |--------------|----------------|-------|----------------|------------|---------------|-------|----------|
 | ethernet1.12 | 0000.0000.1111 | 1     | 6666.0000.1111 | 1234:1::1  | ::            | 0     | 00:00:06 |
 | ethernet1.12 | 0000.0000.1111 | 2     | 6666.0000.1111 | 1234:1::1  | ::            | 0     | 00:00:06 |
 | ethernet2.12 | 0000.0000.3333 | 1     | 6666.0000.3333 | 1234:2::2  | ::            | 0     | 00:00:06 |
 | ethernet2.12 | 0000.0000.3333 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | 0     | 00:00:06 |
 |______________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 dat 2
r2#show ipv4 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
 | lspid                | sequence | flags | len | time      |
 |----------------------|----------|-------|-----|-----------|
 | 4444.0000.1111.00-00 | 0000000b | apo   | 79  | 00:19:56  |
 | 4444.0000.1111.3a-00 | 00000002 | apo   | 13  | -00:00:07 |
 | 4444.0000.2222.00-00 | 0000000f | apo   | 92  | 00:19:53  |
 | 4444.0000.2222.22-00 | 00000001 | apo   | 26  | 00:19:52  |
 | 4444.0000.3333.00-00 | 00000008 | apo   | 68  | 00:19:52  |
 | 4444.0000.3333.5a-00 | 00000002 | apo   | 26  | 00:19:52  |
 |______________________|__________|_______|_____|___________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 dat 2
r2#show ipv6 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
 | lspid                | sequence | flags | len | time      |
 |----------------------|----------|-------|-----|-----------|
 | 6666.0000.1111.00-00 | 0000000b | apo   | 120 | 00:19:52  |
 | 6666.0000.1111.30-00 | 00000002 | apo   | 13  | -00:00:07 |
 | 6666.0000.2222.00-00 | 0000000e | apo   | 133 | 00:19:53  |
 | 6666.0000.2222.75-00 | 00000002 | apo   | 26  | 00:19:52  |
 | 6666.0000.3333.00-00 | 00000009 | apo   | 96  | 00:19:52  |
 | 6666.0000.3333.2d-00 | 00000002 | apo   | 26  | 00:19:52  |
 |______________________|__________|_______|_____|___________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 tre 2
r2#show ipv4 isis 1 tre 2
`--r2
  |`--4444.0000.2222.22
  |   `--r1
   `--4444.0000.3333.5a
      `--r3
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 tre 2
r2#show ipv6 isis 1 tre 2
`--r2
  |`--6666.0000.2222.75
  |   `--r1
   `--6666.0000.3333.2d
      `--r3
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:07 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:07 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:07 |
 | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:07 |
 | I   | 2.2.2.1/32 | 115/10 | ethernet1.11 | 1.1.1.1 | 00:00:07 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:08 |
 | I   | 2.2.2.3/32 | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:07 |
 |_____|____________|________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric | iface        | hop       | time     |
 |------|---------------|--------|--------------|-----------|----------|
 | C    | 1234:1::/32   | 0/0    | ethernet1.12 | null      | 00:00:07 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1.12 | null      | 00:00:07 |
 | C    | 1234:2::/32   | 0/0    | ethernet2.12 | null      | 00:00:07 |
 | LOC  | 1234:2::1/128 | 0/1    | ethernet2.12 | null      | 00:00:07 |
 | I EX | 4321::1/128   | 115/10 | ethernet1.12 | 1234:1::1 | 00:00:07 |
 | C    | 4321::2/128   | 0/0    | loopback1    | null      | 00:00:08 |
 | I EX | 4321::3/128   | 115/10 | ethernet2.12 | 1234:2::2 | 00:00:07 |
 |______|_______________|________|______________|___________|__________|
r2#
r2#
```

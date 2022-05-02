# Example: isis triangle connection

## **Topology diagram**

![topology](/img/rout-isis048.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz51r1-log.run
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
 net-id 11.4444.0000.1111.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 11.6666.0000.1111.00
 traffeng-id ::
 is-type level2
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v1
 ipv6 address 1234:1::1 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 100
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 vrf forwarding v1
 ipv6 address 1234:3::2 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 100
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
logging file debug ../binTmp/zzz51r2-log.run
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
 net-id 22.4444.0000.2222.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 22.6666.0000.2222.00
 traffeng-id ::
 is-type level2
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
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v1
 ipv6 address 1234:1::2 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 vrf forwarding v1
 ipv6 address 1234:2::1 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
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
logging file debug ../binTmp/zzz51r3-log.run
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
router isis4 1
 vrf v1
 net-id 22.4444.0000.3333.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 22.6666.0000.3333.00
 traffeng-id ::
 is-type level2
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
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v1
 ipv6 address 1234:2::2 ffff:ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv4 access-group-in test4
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 100
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 vrf forwarding v1
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 access-group-in test6
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 100
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
 | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:16 |
 | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | up    | 00:00:15 |
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
 | ethernet1.12 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234:1::1  | ::            | up    | 00:00:16 |
 | ethernet2.12 | 0000.0000.0000 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | up    | 00:00:15 |
 |______________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 dat 2
r2#show ipv4 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
 | lspid                | sequence | flags | len | time     |
 |----------------------|----------|-------|-----|----------|
 | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:42 |
 | 4444.0000.1111.00-00 | 0000000a | apo   | 70  | 00:19:53 |
 | 4444.0000.2222.00-00 | 0000000b | apo   | 70  | 00:19:53 |
 | 4444.0000.3333.00-00 | 0000000a | apo   | 70  | 00:19:53 |
 |______________________|__________|_______|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 dat 2
r2#show ipv6 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
 | lspid                | sequence | flags | len | time     |
 |----------------------|----------|-------|-----|----------|
 | 6666.0000.1111.00-00 | 0000000a | apo   | 85  | 00:19:53 |
 | 6666.0000.2222.00-00 | 00000009 | apo   | 85  | 00:19:53 |
 | 6666.0000.3333.00-00 | 0000000c | apo   | 85  | 00:19:52 |
 |______________________|__________|_______|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 tre 2
r2#show ipv4 isis 1 tre 2
`--r2
  |`--r1
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
  |`--r1
   `--r3
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric  | iface        | hop     | time     |
 |-----|------------|---------|--------------|---------|----------|
 | C   | 1.1.1.0/30 | 0/0     | ethernet1.11 | null    | 00:00:17 |
 | LOC | 1.1.1.2/32 | 0/1     | ethernet1.11 | null    | 00:00:17 |
 | C   | 1.1.1.4/30 | 0/0     | ethernet2.11 | null    | 00:00:17 |
 | LOC | 1.1.1.5/32 | 0/1     | ethernet2.11 | null    | 00:00:17 |
 | I   | 1.1.1.8/30 | 115/110 | ethernet2.11 | 1.1.1.6 | 00:00:06 |
 | I   | 2.2.2.1/32 | 115/10  | ethernet1.11 | 1.1.1.1 | 00:00:16 |
 | C   | 2.2.2.2/32 | 0/0     | loopback1    | null    | 00:00:17 |
 | I   | 2.2.2.3/32 | 115/10  | ethernet2.11 | 1.1.1.6 | 00:00:06 |
 |_____|____________|_________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric  | iface        | hop       | time     |
 |------|---------------|---------|--------------|-----------|----------|
 | C    | 1234:1::/32   | 0/0     | ethernet1.12 | null      | 00:00:17 |
 | LOC  | 1234:1::2/128 | 0/1     | ethernet1.12 | null      | 00:00:17 |
 | C    | 1234:2::/32   | 0/0     | ethernet2.12 | null      | 00:00:17 |
 | LOC  | 1234:2::1/128 | 0/1     | ethernet2.12 | null      | 00:00:17 |
 | I    | 1234:3::/32   | 115/110 | ethernet2.12 | 1234:2::2 | 00:00:06 |
 | I EX | 4321::1/128   | 115/10  | ethernet1.12 | 1234:1::1 | 00:00:16 |
 | C    | 4321::2/128   | 0/0     | loopback1    | null      | 00:00:17 |
 | I EX | 4321::3/128   | 115/10  | ethernet2.12 | 1234:2::2 | 00:00:06 |
 |______|_______________|_________|______________|___________|__________|
r2#
r2#
```

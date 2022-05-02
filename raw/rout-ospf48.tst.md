# Example: ospf ecmp connection

## **Topology diagram**

![topology](/img/rout-ospf48.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz12r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
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
 ipv6 address 1234:1::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.252
 ipv6 address 1234:21::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
 ipv6 address 1234:3::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 vrf forwarding v1
 ipv4 address 1.1.2.10 255.255.255.252
 ipv6 address 1234:23::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
logging file debug ../binTmp/zzz12r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.2
 traffeng-id 0.0.0.0
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
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
 ipv6 address 1234:1::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.252
 ipv6 address 1234:21::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
 ipv6 address 1234:2::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 vrf forwarding v1
 ipv4 address 1.1.2.5 255.255.255.252
 ipv6 address 1234:22::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
logging file debug ../binTmp/zzz12r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.3
 traffeng-id 0.0.0.0
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 0 enable
 area 0 spf-ecmp
 redistribute connected
 ecmp
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
 ipv6 address 1234:2::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.22
 vrf forwarding v1
 ipv4 address 1.1.2.6 255.255.255.252
 ipv6 address 1234:22::2 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
 ipv6 address 1234:3::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.22
 vrf forwarding v1
 ipv4 address 1.1.2.9 255.255.255.252
 ipv6 address 1234:23::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | area | address | routerid | state | uptime   |
 |--------------|------|---------|----------|-------|----------|
 | ethernet1.11 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:03 |
 | ethernet1.22 | 0    | 1.1.2.1 | 4.4.4.1  | full  | 00:00:03 |
 | ethernet2.11 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:03 |
 | ethernet2.22 | 0    | 1.1.2.6 | 4.4.4.3  | full  | 00:00:03 |
 |______________|______|_________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 nei
r2#show ipv6 ospf 1 nei
 |~~~~~~~~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | area | address    | routerid | state | uptime   |
 |--------------|------|------------|----------|-------|----------|
 | ethernet1.11 | 0    | 1234:1::1  | 6.6.6.1  | full  | 00:00:03 |
 | ethernet1.22 | 0    | 1234:21::1 | 6.6.6.1  | full  | 00:00:03 |
 | ethernet2.11 | 0    | 1234:2::2  | 6.6.6.3  | full  | 00:00:03 |
 | ethernet2.22 | 0    | 1234:22::2 | 6.6.6.3  | full  | 00:00:03 |
 |______________|______|____________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid   | sequence | type        | len | time     |
 |----------|---------|----------|-------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1 | 80000009 | router      | 100 | 00:00:03 |
 | 4.4.4.2  | 4.4.4.2 | 8000000a | router      | 100 | 00:00:03 |
 | 4.4.4.3  | 4.4.4.3 | 80000009 | router      | 100 | 00:00:03 |
 | 4.4.4.1  | 0.0.0.0 | 80000008 | asExternal  | 16  | 01:00:03 |
 | 4.4.4.2  | 0.0.0.0 | 80000006 | asExternal  | 16  | 01:00:04 |
 | 4.4.4.3  | 0.0.0.0 | 80000008 | asExternal  | 16  | 01:00:04 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.1  | 1.1.1.8 | 80000001 | asExternal  | 16  | 00:00:03 |
 | 4.4.4.3  | 1.1.1.8 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.1  | 1.1.2.0 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.2  | 1.1.2.0 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.2  | 1.1.2.4 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.3  | 1.1.2.4 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.1  | 1.1.2.8 | 80000001 | asExternal  | 16  | 00:00:03 |
 | 4.4.4.3  | 1.1.2.8 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal  | 16  | 00:00:04 |
 | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:04 |
 | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:04 |
 | 4.4.4.3  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:04 |
 |__________|_________|__________|_____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid     | sequence | type       | len | time     |
 |----------|-----------|----------|------------|-----|----------|
 | 6.6.6.1  | 379099748 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.1  | 379099749 | 80000001 | link       | 24  | 00:00:03 |
 | 6.6.6.1  | 379099750 | 80000001 | link       | 24  | 00:00:03 |
 | 6.6.6.1  | 379099751 | 80000001 | link       | 24  | 00:00:03 |
 | 6.6.6.3  | 432689719 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.3  | 432689720 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.3  | 432689721 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.3  | 432689722 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.2  | 928252164 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.2  | 928252165 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.2  | 928252166 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.2  | 928252167 | 80000001 | link       | 24  | 00:00:04 |
 | 6.6.6.1  | 0         | 80000005 | router     | 68  | 00:00:03 |
 | 6.6.6.2  | 0         | 80000006 | router     | 68  | 00:00:03 |
 | 6.6.6.3  | 0         | 80000005 | router     | 68  | 00:00:03 |
 | 6.6.6.1  | 379099748 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.1  | 379099749 | 80000001 | prefix     | 20  | 00:00:03 |
 | 6.6.6.1  | 379099750 | 80000001 | prefix     | 20  | 00:00:03 |
 | 6.6.6.1  | 379099751 | 80000001 | prefix     | 20  | 00:00:03 |
 | 6.6.6.3  | 432689719 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.3  | 432689720 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.3  | 432689721 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.3  | 432689722 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.2  | 928252164 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.2  | 928252165 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.2  | 928252166 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.2  | 928252167 | 80000001 | prefix     | 20  | 00:00:04 |
 | 6.6.6.1  | 0         | 80000008 | asExternal | 16  | 00:00:03 |
 | 6.6.6.2  | 0         | 80000008 | asExternal | 16  | 00:00:04 |
 | 6.6.6.3  | 0         | 80000009 | asExternal | 16  | 00:00:04 |
 | 6.6.6.1  | 1         | 80000005 | asExternal | 16  | 00:00:03 |
 | 6.6.6.2  | 1         | 80000005 | asExternal | 16  | 00:00:04 |
 | 6.6.6.3  | 1         | 80000007 | asExternal | 16  | 00:00:04 |
 | 6.6.6.1  | 2         | 80000002 | asExternal | 16  | 00:00:03 |
 | 6.6.6.2  | 2         | 80000002 | asExternal | 16  | 00:00:04 |
 | 6.6.6.3  | 2         | 80000004 | asExternal | 16  | 00:00:04 |
 | 6.6.6.1  | 3         | 80000002 | asExternal | 16  | 00:00:03 |
 | 6.6.6.2  | 3         | 80000002 | asExternal | 16  | 00:00:04 |
 | 6.6.6.3  | 3         | 80000003 | asExternal | 16  | 00:00:04 |
 | 6.6.6.1  | 4         | 80000001 | asExternal | 28  | 00:00:03 |
 | 6.6.6.2  | 4         | 80000001 | asExternal | 28  | 00:00:04 |
 | 6.6.6.3  | 4         | 80000001 | asExternal | 28  | 00:00:04 |
 |__________|___________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
`--r2
  |`--r1
  |`--r1
  |`--r3
   `--r3
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
`--6.6.6.2/00000000
  |`--6.6.6.1/00000000
  |`--6.6.6.1/00000000
  |`--6.6.6.3/00000000
   `--6.6.6.3/00000000
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface        | hop     | time     |
 |------|------------|--------|--------------|---------|----------|
 | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:05 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:05 |
 | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:05 |
 | LOC  | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:05 |
 | O    | 1.1.1.8/30 | 110/20 | ethernet1.11 | 1.1.1.1 | 00:00:04 |
 | O    | 1.1.1.8/30 | 110/20 | ethernet1.22 | 1.1.2.1 | 00:00:04 |
 | O    | 1.1.1.8/30 | 110/20 | ethernet2.11 | 1.1.1.6 | 00:00:04 |
 | O    | 1.1.1.8/30 | 110/20 | ethernet2.22 | 1.1.2.6 | 00:00:04 |
 | C    | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:05 |
 | LOC  | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:05 |
 | C    | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:04 |
 | LOC  | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:04 |
 | O    | 1.1.2.8/30 | 110/20 | ethernet1.11 | 1.1.1.1 | 00:00:04 |
 | O    | 1.1.2.8/30 | 110/20 | ethernet1.22 | 1.1.2.1 | 00:00:04 |
 | O    | 1.1.2.8/30 | 110/20 | ethernet2.11 | 1.1.1.6 | 00:00:04 |
 | O    | 1.1.2.8/30 | 110/20 | ethernet2.22 | 1.1.2.6 | 00:00:04 |
 | O E2 | 2.2.2.1/32 | 110/0  | ethernet1.11 | 1.1.1.1 | 00:00:04 |
 | O E2 | 2.2.2.1/32 | 110/0  | ethernet1.22 | 1.1.2.1 | 00:00:04 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:05 |
 | O E2 | 2.2.2.3/32 | 110/0  | ethernet2.11 | 1.1.1.6 | 00:00:04 |
 | O E2 | 2.2.2.3/32 | 110/0  | ethernet2.22 | 1.1.2.6 | 00:00:04 |
 |______|____________|________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix         | metric | iface        | hop        | time     |
 |------|----------------|--------|--------------|------------|----------|
 | C    | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:05 |
 | LOC  | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:05 |
 | C    | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:05 |
 | LOC  | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:05 |
 | O    | 1234:3::/32    | 110/20 | ethernet1.11 | 1234:1::1  | 00:00:04 |
 | O    | 1234:3::/32    | 110/20 | ethernet1.22 | 1234:21::1 | 00:00:04 |
 | O    | 1234:3::/32    | 110/20 | ethernet2.11 | 1234:2::2  | 00:00:04 |
 | O    | 1234:3::/32    | 110/20 | ethernet2.22 | 1234:22::2 | 00:00:04 |
 | C    | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:05 |
 | LOC  | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:05 |
 | C    | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:05 |
 | LOC  | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:05 |
 | O    | 1234:23::/32   | 110/20 | ethernet1.11 | 1234:1::1  | 00:00:04 |
 | O    | 1234:23::/32   | 110/20 | ethernet1.22 | 1234:21::1 | 00:00:04 |
 | O    | 1234:23::/32   | 110/20 | ethernet2.11 | 1234:2::2  | 00:00:04 |
 | O    | 1234:23::/32   | 110/20 | ethernet2.22 | 1234:22::2 | 00:00:04 |
 | O E2 | 4321::1/128    | 110/0  | ethernet1.11 | 1234:1::1  | 00:00:04 |
 | O E2 | 4321::1/128    | 110/0  | ethernet1.22 | 1234:21::1 | 00:00:04 |
 | C    | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:05 |
 | O E2 | 4321::3/128    | 110/0  | ethernet2.11 | 1234:2::2  | 00:00:04 |
 | O E2 | 4321::3/128    | 110/0  | ethernet2.22 | 1234:22::2 | 00:00:04 |
 |______|________________|________|______________|____________|__________|
r2#
r2#
```

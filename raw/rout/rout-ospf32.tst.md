# Example: ospf change in metric

## **Topology diagram**

![topology](/img/rout-ospf32.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz46r1-log.run
!
route-map rm1
 sequence 10 action permit
 sequence 10 set metric set 1000
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
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected route-map rm1
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 redistribute connected route-map rm1
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz46r2-log.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match metric 2000-4000
 !
 sequence 20 action permit
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
router ospf4 1
 vrf v1
 router-id 4.4.4.2
 traffeng-id 0.0.0.0
 area 0 enable
 area 0 route-map-from rm1
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 area 0 route-map-from rm1
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
interface ethernet2
 no description
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz46r3-log.run
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
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 0 enable
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
 |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | area | address | routerid | state | uptime   |
 |-----------|------|---------|----------|-------|----------|
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | 4     | 00:00:09 |
 | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | 4     | 00:00:09 |
 |___________|______|_________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 nei
r2#show ipv6 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | area | address   | routerid | state | uptime   |
 |-----------|------|-----------|----------|-------|----------|
 | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | 4     | 00:00:09 |
 | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | 4     | 00:00:09 |
 |___________|______|___________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid   | sequence | type       | len | time     |
 |----------|---------|----------|------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1 | 80000004 | router     | 28  | 00:00:09 |
 | 4.4.4.2  | 4.4.4.2 | 80000006 | router     | 52  | 00:00:09 |
 | 4.4.4.3  | 4.4.4.3 | 80000004 | router     | 28  | 00:00:06 |
 | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:10 |
 | 4.4.4.2  | 0.0.0.0 | 80000004 | asExternal | 16  | 01:00:10 |
 | 4.4.4.3  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:10 |
 | 4.4.4.1  | 1.1.1.0 | 80000003 | asExternal | 16  | 00:00:04 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:10 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal | 16  | 00:00:10 |
 | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal | 16  | 00:00:10 |
 | 4.4.4.1  | 2.2.2.1 | 80000003 | asExternal | 16  | 00:00:04 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal | 16  | 00:00:10 |
 | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal | 16  | 00:00:10 |
 |__________|_________|__________|____________|_____|__________|
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
 | 6.6.6.3  | 97427775  | 80000001 | link       | 24  | 00:00:10 |
 | 6.6.6.1  | 171250907 | 80000001 | link       | 24  | 00:00:10 |
 | 6.6.6.2  | 357039143 | 80000001 | link       | 24  | 00:00:10 |
 | 6.6.6.2  | 357039144 | 80000001 | link       | 24  | 00:00:10 |
 | 6.6.6.1  | 0         | 80000003 | router     | 20  | 00:00:09 |
 | 6.6.6.2  | 0         | 80000004 | router     | 36  | 00:00:09 |
 | 6.6.6.3  | 0         | 80000003 | router     | 20  | 00:00:06 |
 | 6.6.6.3  | 97427775  | 80000001 | prefix     | 20  | 00:00:10 |
 | 6.6.6.1  | 171250907 | 80000001 | prefix     | 20  | 00:00:10 |
 | 6.6.6.2  | 357039143 | 80000001 | prefix     | 20  | 00:00:10 |
 | 6.6.6.2  | 357039144 | 80000001 | prefix     | 20  | 00:00:10 |
 | 6.6.6.1  | 0         | 80000005 | asExternal | 16  | 00:00:04 |
 | 6.6.6.2  | 0         | 80000006 | asExternal | 16  | 00:00:10 |
 | 6.6.6.3  | 0         | 80000003 | asExternal | 16  | 00:00:10 |
 | 6.6.6.1  | 1         | 80000003 | asExternal | 28  | 00:00:04 |
 | 6.6.6.2  | 1         | 80000003 | asExternal | 16  | 00:00:10 |
 | 6.6.6.3  | 1         | 80000001 | asExternal | 28  | 00:00:10 |
 | 6.6.6.2  | 2         | 80000001 | asExternal | 28  | 00:00:10 |
 |__________|___________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
`--4.4.4.2
  |`--4.4.4.1
   `--4.4.4.3
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
   `--6.6.6.3/00000000
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric   | iface     | hop     | time     |
 |------|------------|----------|-----------|---------|----------|
 | C    | 1.1.1.0/30 | 0/0      | ethernet1 | null    | 00:00:10 |
 | LOC  | 1.1.1.2/32 | 0/1      | ethernet1 | null    | 00:00:10 |
 | C    | 1.1.1.4/30 | 0/0      | ethernet2 | null    | 00:00:10 |
 | LOC  | 1.1.1.5/32 | 0/1      | ethernet2 | null    | 00:00:10 |
 | O E2 | 2.2.2.1/32 | 110/5000 | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C    | 2.2.2.2/32 | 0/0      | loopback1 | null    | 00:00:10 |
 | O E2 | 2.2.2.3/32 | 110/0    | ethernet2 | 1.1.1.6 | 00:00:07 |
 |______|____________|__________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric   | iface     | hop       | time     |
 |------|---------------|----------|-----------|-----------|----------|
 | C    | 1234:1::/32   | 0/0      | ethernet1 | null      | 00:00:10 |
 | LOC  | 1234:1::2/128 | 0/1      | ethernet1 | null      | 00:00:10 |
 | C    | 1234:2::/32   | 0/0      | ethernet2 | null      | 00:00:10 |
 | LOC  | 1234:2::1/128 | 0/1      | ethernet2 | null      | 00:00:10 |
 | O E2 | 4321::1/128   | 110/5000 | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0      | loopback1 | null      | 00:00:10 |
 | O E2 | 4321::3/128   | 110/0    | ethernet2 | 1234:2::2 | 00:00:07 |
 |______|_______________|__________|___________|___________|__________|
r2#
r2#
```
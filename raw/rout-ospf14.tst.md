# Example: ospf external1 vs external2

## **Topology diagram**

![topology](/img/rout-ospf14.tst.png)

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
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
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
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.111 255.255.255.255
 ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz1r2-log.run
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
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
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
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 cost 100
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 cost 100
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
prefix-list p4
 sequence 10 deny 2.2.2.222/32 ge 32 le 32
 sequence 20 permit 0.0.0.0/0 ge 0 le 32
 exit
!
prefix-list p6
 sequence 10 deny 4321::222/128 ge 128 le 128
 sequence 20 permit ::/0 ge 0 le 128
 exit
!
route-map rm1
 sequence 10 action permit
 sequence 10 set origin set 111
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
 router-id 4.4.4.3
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected prefix-list p4 route-map rm1
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 0 enable
 redistribute connected prefix-list p6 route-map rm1
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
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.111 255.255.255.255
 ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 vrf forwarding v1
 ipv4 address 2.2.2.222 255.255.255.255
 ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | area | address | routerid | state | uptime   |
 |-----------|------|---------|----------|-------|----------|
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:10 |
 | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:11 |
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
 | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:11 |
 | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:11 |
 |___________|______|___________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid     | sequence | type        | len | time     |
 |----------|-----------|----------|-------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1   | 80000004 | router      | 28  | 00:00:08 |
 | 4.4.4.2  | 4.4.4.2   | 80000007 | router      | 52  | 00:00:08 |
 | 4.4.4.3  | 4.4.4.3   | 80000004 | router      | 28  | 00:00:08 |
 | 4.4.4.1  | 0.0.0.0   | 80000004 | asExternal  | 16  | 01:00:12 |
 | 4.4.4.2  | 0.0.0.0   | 80000004 | asExternal  | 16  | 01:00:11 |
 | 4.4.4.1  | 1.1.1.0   | 80000001 | asExternal  | 16  | 00:00:12 |
 | 4.4.4.2  | 1.1.1.0   | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.2  | 1.1.1.4   | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.3  | 1.1.1.4   | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.1  | 2.2.2.1   | 80000001 | asExternal  | 16  | 00:00:12 |
 | 4.4.4.2  | 2.2.2.2   | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.3  | 2.2.2.3   | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.1  | 2.2.2.111 | 80000001 | asExternal  | 16  | 00:00:12 |
 | 4.4.4.3  | 2.2.2.111 | 80000001 | asExternal  | 16  | 00:00:11 |
 | 4.4.4.1  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:12 |
 | 4.4.4.2  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:12 |
 | 4.4.4.3  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:11 |
 |__________|___________|__________|_____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid      | sequence | type       | len | time     |
 |----------|------------|----------|------------|-----|----------|
 | 6.6.6.2  | 19480422   | 80000001 | link       | 24  | 00:00:11 |
 | 6.6.6.2  | 19480423   | 80000001 | link       | 24  | 00:00:11 |
 | 6.6.6.1  | 354747515  | 80000001 | link       | 24  | 00:00:12 |
 | 6.6.6.3  | 1056854594 | 80000001 | link       | 24  | 00:00:11 |
 | 6.6.6.1  | 0          | 80000003 | router     | 20  | 00:00:08 |
 | 6.6.6.2  | 0          | 80000004 | router     | 36  | 00:00:08 |
 | 6.6.6.3  | 0          | 80000003 | router     | 20  | 00:00:08 |
 | 6.6.6.2  | 19480422   | 80000001 | prefix     | 20  | 00:00:11 |
 | 6.6.6.2  | 19480423   | 80000002 | prefix     | 20  | 00:00:11 |
 | 6.6.6.1  | 354747515  | 80000001 | prefix     | 20  | 00:00:12 |
 | 6.6.6.3  | 1056854594 | 80000001 | prefix     | 20  | 00:00:11 |
 | 6.6.6.1  | 0          | 80000003 | asExternal | 16  | 00:00:12 |
 | 6.6.6.2  | 0          | 80000005 | asExternal | 16  | 00:00:11 |
 | 6.6.6.3  | 0          | 80000002 | asExternal | 16  | 00:00:11 |
 | 6.6.6.1  | 1          | 80000002 | asExternal | 28  | 00:00:12 |
 | 6.6.6.2  | 1          | 80000003 | asExternal | 16  | 00:00:11 |
 | 6.6.6.3  | 1          | 80000002 | asExternal | 28  | 00:00:11 |
 | 6.6.6.1  | 2          | 80000001 | asExternal | 28  | 00:00:12 |
 | 6.6.6.2  | 2          | 80000001 | asExternal | 28  | 00:00:11 |
 | 6.6.6.3  | 2          | 80000001 | asExternal | 28  | 00:00:11 |
 |__________|____________|__________|____________|_____|__________|
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
   `--6.6.6.3/00000000
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric  | iface     | hop     | time     |
 |------|--------------|---------|-----------|---------|----------|
 | C    | 1.1.1.0/30   | 0/0     | ethernet1 | null    | 00:00:12 |
 | LOC  | 1.1.1.2/32   | 0/1     | ethernet1 | null    | 00:00:12 |
 | C    | 1.1.1.4/30   | 0/0     | ethernet2 | null    | 00:00:12 |
 | LOC  | 1.1.1.5/32   | 0/1     | ethernet2 | null    | 00:00:12 |
 | O E2 | 2.2.2.1/32   | 110/0   | ethernet1 | 1.1.1.1 | 00:00:08 |
 | C    | 2.2.2.2/32   | 0/0     | loopback1 | null    | 00:00:12 |
 | O E1 | 2.2.2.3/32   | 110/100 | ethernet2 | 1.1.1.6 | 00:00:08 |
 | O E1 | 2.2.2.111/32 | 110/100 | ethernet2 | 1.1.1.6 | 00:00:08 |
 |______|______________|_________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric  | iface     | hop       | time     |
 |------|---------------|---------|-----------|-----------|----------|
 | C    | 1234:1::/32   | 0/0     | ethernet1 | null      | 00:00:12 |
 | LOC  | 1234:1::2/128 | 0/1     | ethernet1 | null      | 00:00:12 |
 | C    | 1234:2::/32   | 0/0     | ethernet2 | null      | 00:00:12 |
 | LOC  | 1234:2::1/128 | 0/1     | ethernet2 | null      | 00:00:12 |
 | O E2 | 4321::1/128   | 110/0   | ethernet1 | 1234:1::1 | 00:00:08 |
 | C    | 4321::2/128   | 0/0     | loopback1 | null      | 00:00:12 |
 | O E1 | 4321::3/128   | 110/100 | ethernet2 | 1234:2::2 | 00:00:08 |
 | O E1 | 4321::111/128 | 110/100 | ethernet2 | 1234:2::2 | 00:00:08 |
 |______|_______________|_________|___________|___________|__________|
r2#
r2#
```

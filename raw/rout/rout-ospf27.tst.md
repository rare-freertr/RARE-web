# Example: ospf with te

## **Topology diagram**

![topology](/img/rout-ospf27.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz18r1-log.run
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
 traffeng-id 4.4.4.1
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 area 0 traffeng
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
logging file debug ../binTmp/zzz18r2-log.run
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
 traffeng-id 4.4.4.2
 area 0 enable
 area 0 traffeng
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 area 0 traffeng
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | 4     | 00:00:00 |
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
 | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | 4     | 00:00:00 |
 |___________|______|___________|__________|_______|__________|
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
 | 4.4.4.1  | 4.4.4.1 | 80000005 | router      | 28  | 00:00:00 |
 | 4.4.4.2  | 4.4.4.2 | 80000005 | router      | 28  | 00:00:00 |
 | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:00 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:00 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:01 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:00 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:01 |
 | 4.4.4.1  | 1.0.0.0 | 80000001 | opaque-area | 8   | 00:00:00 |
 | 4.4.4.2  | 1.0.0.0 | 80000001 | opaque-area | 8   | 00:00:01 |
 | 4.4.4.1  | 1.0.0.1 | 80000001 | opaque-area | 112 | 00:00:00 |
 | 4.4.4.2  | 1.0.0.1 | 80000001 | opaque-area | 112 | 00:00:00 |
 | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 8   | 00:00:00 |
 | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 8   | 00:00:01 |
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
 | 6.6.6.2  | 217852946 | 80000001 | link       | 24  | 00:00:01 |
 | 6.6.6.1  | 840643936 | 80000001 | link       | 24  | 00:00:00 |
 | 6.6.6.1  | 0         | 80000004 | router     | 20  | 00:00:00 |
 | 6.6.6.2  | 0         | 80000004 | router     | 20  | 00:00:00 |
 | 6.6.6.2  | 217852946 | 80000001 | prefix     | 20  | 00:00:01 |
 | 6.6.6.1  | 840643936 | 80000001 | prefix     | 20  | 00:00:00 |
 | 6.6.6.1  | 0         | 80000004 | asExternal | 16  | 00:00:00 |
 | 6.6.6.2  | 0         | 80000003 | asExternal | 16  | 00:00:01 |
 | 6.6.6.1  | 1         | 80000001 | asExternal | 28  | 00:00:00 |
 | 6.6.6.2  | 1         | 80000001 | asExternal | 28  | 00:00:01 |
 | 6.6.6.1  | 0         | 80000001 | traffEng   | 20  | 00:00:00 |
 | 6.6.6.2  | 0         | 80000001 | traffEng   | 20  | 00:00:01 |
 | 6.6.6.1  | 1         | 80000001 | traffEng   | 140 | 00:00:00 |
 | 6.6.6.2  | 1         | 80000001 | traffEng   | 140 | 00:00:00 |
 | 6.6.6.1  | 0         | 80000001 | rtrInfo    | 8   | 00:00:00 |
 | 6.6.6.2  | 0         | 80000001 | rtrInfo    | 8   | 00:00:01 |
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
   `--4.4.4.1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
`--6.6.6.2/00000000
   `--6.6.6.1/00000000
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
 | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:01 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:01 |
 | O E2 | 2.2.2.1/32 | 110/0  | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:01 |
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:01 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:01 |
 | O E2 | 4321::1/128   | 110/0  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:01 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

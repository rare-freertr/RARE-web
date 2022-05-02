# Example: ospf with polka

## **Topology diagram**

![topology](/img/rout-ospf50.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz74r1-log.run
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
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 segrout index 1
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 segrout index 1
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 polka enable 1 65536 10
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 2.2.2.3
 tunnel domain-name 2.2.2.2
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 4321::3
 tunnel domain-name 4321::2
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 3333::1 ffff::
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
logging file debug ../binTmp/zzz74r2-log.run
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
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 segrout index 2
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 segrout index 2
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 polka enable 2 65536 10
 mpls enable
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
 polka enable 2 65536 10
 mpls enable
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
logging file debug ../binTmp/zzz74r3-log.run
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
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 segrout 10
 area 0 enable
 area 0 segrout
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 segrout index 3
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 segrout index 3
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 polka enable 3 65536 10
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 2.2.2.1
 tunnel domain-name 2.2.2.2
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 4321::1
 tunnel domain-name 4321::2
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 3333::2 ffff::
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
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:05 |
 | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:05 |
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
 | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:05 |
 | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:06 |
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
 | 4.4.4.1  | 4.4.4.1 | 80000005 | router      | 40  | 00:00:05 |
 | 4.4.4.2  | 4.4.4.2 | 80000007 | router      | 64  | 00:00:03 |
 | 4.4.4.3  | 4.4.4.3 | 80000005 | router      | 40  | 00:00:06 |
 | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:05 |
 | 4.4.4.2  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:06 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:06 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:07 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:06 |
 | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:06 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:06 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:07 |
 | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal  | 16  | 00:00:06 |
 | 4.4.4.1  | 3.3.3.0 | 80000001 | asExternal  | 16  | 00:00:01 |
 | 4.4.4.3  | 3.3.3.0 | 80000001 | asExternal  | 16  | 00:00:01 |
 | 4.4.4.1  | 4.0.0.0 | 80000002 | opaque-area | 40  | 00:00:05 |
 | 4.4.4.2  | 4.0.0.0 | 80000002 | opaque-area | 40  | 00:00:07 |
 | 4.4.4.3  | 4.0.0.0 | 80000002 | opaque-area | 40  | 00:00:06 |
 | 4.4.4.1  | 7.0.0.1 | 80000002 | opaque-area | 24  | 00:00:05 |
 | 4.4.4.2  | 7.0.0.1 | 80000002 | opaque-area | 24  | 00:00:07 |
 | 4.4.4.3  | 7.0.0.1 | 80000002 | opaque-area | 24  | 00:00:06 |
 | 4.4.4.1  | 8.0.0.1 | 80000001 | opaque-area | 36  | 00:00:05 |
 | 4.4.4.2  | 8.0.0.1 | 80000002 | opaque-area | 36  | 00:00:03 |
 | 4.4.4.3  | 8.0.0.1 | 80000001 | opaque-area | 36  | 00:00:06 |
 | 4.4.4.2  | 8.0.0.2 | 80000001 | opaque-area | 36  | 00:00:03 |
 |__________|_________|__________|_____________|_____|__________|
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
 | 6.6.6.2  | 665932474  | 80000001 | link       | 24  | 00:00:07 |
 | 6.6.6.2  | 665932475  | 80000001 | link       | 24  | 00:00:07 |
 | 6.6.6.2  | 665932476  | 80000001 | link       | 24  | 00:00:07 |
 | 6.6.6.3  | 799620591  | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.3  | 799620592  | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.1  | 1052712509 | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.1  | 1052712510 | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.1  | 0          | 80000004 | router     | 20  | 00:00:06 |
 | 6.6.6.2  | 0          | 80000005 | router     | 36  | 00:00:06 |
 | 6.6.6.3  | 0          | 80000004 | router     | 20  | 00:00:06 |
 | 6.6.6.2  | 665932474  | 80000001 | prefix     | 32  | 00:00:07 |
 | 6.6.6.2  | 665932475  | 80000001 | prefix     | 20  | 00:00:07 |
 | 6.6.6.2  | 665932476  | 80000001 | prefix     | 20  | 00:00:07 |
 | 6.6.6.3  | 799620591  | 80000001 | prefix     | 32  | 00:00:06 |
 | 6.6.6.3  | 799620592  | 80000001 | prefix     | 20  | 00:00:06 |
 | 6.6.6.1  | 1052712509 | 80000001 | prefix     | 32  | 00:00:06 |
 | 6.6.6.1  | 1052712510 | 80000001 | prefix     | 20  | 00:00:06 |
 | 6.6.6.1  | 0          | 80000003 | asExternal | 16  | 00:00:06 |
 | 6.6.6.2  | 0          | 80000005 | asExternal | 16  | 00:00:07 |
 | 6.6.6.3  | 0          | 80000003 | asExternal | 16  | 00:00:06 |
 | 6.6.6.1  | 1          | 80000004 | asExternal | 16  | 00:00:01 |
 | 6.6.6.2  | 1          | 80000003 | asExternal | 16  | 00:00:07 |
 | 6.6.6.3  | 1          | 80000002 | asExternal | 16  | 00:00:01 |
 | 6.6.6.1  | 2          | 80000003 | asExternal | 28  | 00:00:01 |
 | 6.6.6.2  | 2          | 80000001 | asExternal | 28  | 00:00:07 |
 | 6.6.6.3  | 2          | 80000001 | asExternal | 28  | 00:00:01 |
 | 6.6.6.1  | 0          | 80000001 | rtrInfo    | 32  | 00:00:06 |
 | 6.6.6.2  | 0          | 80000001 | rtrInfo    | 32  | 00:00:07 |
 | 6.6.6.3  | 0          | 80000001 | rtrInfo    | 32  | 00:00:06 |
 | 6.6.6.1  | 0          | 80000003 | ext-router | 36  | 00:00:06 |
 | 6.6.6.2  | 0          | 80000004 | ext-router | 68  | 00:00:06 |
 | 6.6.6.3  | 0          | 80000003 | ext-router | 36  | 00:00:06 |
 | 6.6.6.1  | 1          | 80000002 | ext-prefix | 52  | 00:00:06 |
 | 6.6.6.2  | 1          | 80000002 | ext-prefix | 52  | 00:00:07 |
 | 6.6.6.3  | 1          | 80000002 | ext-prefix | 52  | 00:00:06 |
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
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:07 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:07 |
 | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:07 |
 | LOC  | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:07 |
 | O    | 2.2.2.1/32 | 110/20 | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:08 |
 | O    | 2.2.2.3/32 | 110/20 | ethernet2 | 1.1.1.6 | 00:00:07 |
 | O E2 | 3.3.3.0/30 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:02 |
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:08 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:08 |
 | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:07 |
 | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:07 |
 | O E2 | 3333::/16     | 110/0  | ethernet1 | 1234:1::1 | 00:00:02 |
 | O    | 4321::1/128   | 110/20 | ethernet1 | 1234:1::1 | 00:00:07 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:08 |
 | O    | 4321::3/128   | 110/20 | ethernet2 | 1234:2::2 | 00:00:07 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 segrou v1
r2#show ipv4 segrou v1
 |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix     | index | base   | oldbase |
 |------------|-------|--------|---------|
 | 2.2.2.1/32 | 1     | 235013 | 235013  |
 | 2.2.2.3/32 | 3     | 51982  | 51982   |
 |____________|_______|________|_________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 segrou v1
r2#show ipv6 segrou v1
 |~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix      | index | base   | oldbase |
 |-------------|-------|--------|---------|
 | 4321::1/128 | 1     | 30469  | 30469   |
 | 4321::3/128 | 3     | 414974 | 414974  |
 |_____________|_______|________|_________|
r2#
r2#
```

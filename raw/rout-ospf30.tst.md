# Example: ospf transit area with sr

## **Topology diagram**

![topology](/img/rout-ospf30.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
 no description
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
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 access-group-in test6
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
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
 area 1 enable
 area 1 segrout
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
 area 1 enable
 area 1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
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
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 access-group-in test6
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
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
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
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
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
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.3
 traffeng-id 0.0.0.0
 segrout 10
 area 1 enable
 area 1 segrout
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 segrout 10
 area 1 enable
 area 1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf4 1 segrout index 3
 router ospf4 1 segrout node
 router ospf6 1 enable
 router ospf6 1 area 1
 router ospf6 1 segrout index 3
 router ospf6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 access-group-in test6
 mpls enable
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
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
end
```

## **Verification**

```
r2#
r2#
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | address | routerid | uptime   |
 |-----------|---------|----------|----------|
 | ethernet1 | 1.1.1.1 | 4.4.4.1  | 00:00:07 |
 | ethernet2 | 1.1.1.6 | 4.4.4.3  | 00:00:07 |
 |___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 nei
r2#show ipv6 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | address   | routerid | uptime   |
 |-----------|-----------|----------|----------|
 | ethernet1 | 1234:1::1 | 6.6.6.1  | 00:00:07 |
 | ethernet2 | 1234:2::2 | 6.6.6.3  | 00:00:07 |
 |___________|___________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid   | sequence | type           | len | time     |
 |----------|---------|----------|----------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1 | 80000006 | router         | 40  | 00:00:06 |
 | 4.4.4.2  | 4.4.4.2 | 80000008 | router         | 40  | 00:00:04 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | summaryNetwork | 8   | 00:00:08 |
 | 4.4.4.2  | 2.2.2.3 | 80000001 | summaryNetwork | 8   | 00:00:07 |
 | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal     | 16  | 01:00:08 |
 | 4.4.4.2  | 0.0.0.0 | 80000004 | asExternal     | 16  | 01:00:08 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal     | 16  | 00:00:07 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal     | 16  | 00:00:08 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal     | 16  | 00:00:08 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal     | 16  | 00:00:08 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal     | 16  | 00:00:08 |
 | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area    | 32  | 00:00:08 |
 | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area    | 32  | 00:00:08 |
 | 4.4.4.1  | 7.0.0.1 | 80000001 | opaque-area    | 24  | 00:00:08 |
 | 4.4.4.2  | 7.0.0.1 | 80000002 | opaque-area    | 24  | 00:00:08 |
 | 4.4.4.2  | 7.0.0.2 | 80000001 | opaque-area    | 24  | 00:00:07 |
 | 4.4.4.1  | 8.0.0.1 | 80000001 | opaque-area    | 36  | 00:00:06 |
 | 4.4.4.2  | 8.0.0.1 | 80000001 | opaque-area    | 36  | 00:00:04 |
 |__________|_________|__________|________________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid | sequence | type         | len | time     |
 |----------|-------|----------|--------------|-----|----------|
 | 6.6.6.1  | 10011 | 80000001 | link         | 24  | 00:00:08 |
 | 6.6.6.2  | 10011 | 80000001 | link         | 24  | 00:00:08 |
 | 6.6.6.1  | 10012 | 80000001 | link         | 24  | 00:00:07 |
 | 6.6.6.2  | 10012 | 80000001 | link         | 24  | 00:00:08 |
 | 6.6.6.2  | 10013 | 80000002 | link         | 24  | 01:00:08 |
 | 6.6.6.1  | 0     | 80000004 | router       | 20  | 00:00:07 |
 | 6.6.6.2  | 0     | 80000004 | router       | 20  | 00:00:04 |
 | 6.6.6.2  | 0     | 80000001 | iaPrefix     | 12  | 00:00:08 |
 | 6.6.6.2  | 1     | 80000001 | iaPrefix     | 24  | 00:00:07 |
 | 6.6.6.1  | 10011 | 80000001 | prefix       | 32  | 00:00:08 |
 | 6.6.6.2  | 10011 | 80000001 | prefix       | 32  | 00:00:08 |
 | 6.6.6.1  | 10012 | 80000001 | prefix       | 20  | 00:00:07 |
 | 6.6.6.2  | 10012 | 80000001 | prefix       | 20  | 00:00:08 |
 | 6.6.6.2  | 10013 | 80000002 | prefix       | 20  | 01:00:08 |
 | 6.6.6.1  | 0     | 80000004 | asExternal   | 16  | 00:00:08 |
 | 6.6.6.2  | 0     | 80000003 | asExternal   | 16  | 00:00:08 |
 | 6.6.6.1  | 1     | 80000001 | asExternal   | 28  | 00:00:08 |
 | 6.6.6.2  | 1     | 80000002 | asExternal   | 16  | 00:00:08 |
 | 6.6.6.2  | 2     | 80000001 | asExternal   | 28  | 00:00:08 |
 | 6.6.6.1  | 0     | 80000001 | rtrInfo      | 32  | 00:00:08 |
 | 6.6.6.2  | 0     | 80000001 | rtrInfo      | 32  | 00:00:08 |
 | 6.6.6.1  | 0     | 80000003 | ext-router   | 36  | 00:00:07 |
 | 6.6.6.2  | 0     | 80000003 | ext-router   | 36  | 00:00:04 |
 | 6.6.6.2  | 2     | 80000001 | ext-iaPrefix | 40  | 00:00:07 |
 | 6.6.6.1  | 1     | 80000002 | ext-prefix   | 40  | 00:00:08 |
 | 6.6.6.2  | 1     | 80000002 | ext-prefix   | 40  | 00:00:08 |
 |__________|_______|__________|______________|_____|__________|
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:05 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:05 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:05 |
 | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:05 |
 | O   | 2.2.2.1/32 | 110/1  | ethernet1 | 1.1.1.1 | 00:00:05 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:05 |
 | O   | 2.2.2.3/32 | 110/1  | ethernet2 | 1.1.1.6 | 00:00:08 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric | iface     | hop       | time     |
 |-----|---------------|--------|-----------|-----------|----------|
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:05 |
 | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:05 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:05 |
 | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:05 |
 | O   | 4321::1/128   | 110/1  | ethernet1 | 1234:1::1 | 00:00:05 |
 | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:05 |
 | O   | 4321::3/128   | 110/1  | ethernet2 | 1234:2::2 | 00:00:08 |
 |_____|_______________|________|___________|___________|__________|
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
 | 2.2.2.1/32 | 1     | 368016 | 368016  |
 | 2.2.2.3/32 | 3     | 300913 | 300913  |
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
 | 4321::1/128 | 1     | 266044 | 266044  |
 | 4321::3/128 | 3     | 988532 | 988532  |
 |_____________|_______|________|_________|
r2#
r2#
```

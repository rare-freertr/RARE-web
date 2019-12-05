# Example: ospf point2point chain

## **Topology diagram**

![topology](/img/rout-ospf06.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
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
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
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
interface ethernet2
 no description
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
!
!
!
!
!
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.4
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.4
 traffeng-id ::
 area 0 enable
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
interface ethernet1
 no description
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
!
!
!
!
!
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
 | ethernet1 | 1.1.1.1 | 4.4.4.1  | 00:00:11 |
 | ethernet2 | 1.1.1.6 | 4.4.4.3  | 00:00:11 |
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
 | ethernet1 | 1234:1::1 | 6.6.6.1  | 00:00:12 |
 | ethernet2 | 1234:2::2 | 6.6.6.3  | 00:00:12 |
 |___________|___________|__________|__________|
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
 | 4.4.4.1  | 4.4.4.1 | 80000004 | router     | 28  | 00:00:11 |
 | 4.4.4.2  | 4.4.4.2 | 80000006 | router     | 52  | 00:00:11 |
 | 4.4.4.3  | 4.4.4.3 | 80000006 | router     | 52  | 00:00:08 |
 | 4.4.4.4  | 4.4.4.4 | 80000004 | router     | 28  | 00:00:10 |
 | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:12 |
 | 4.4.4.2  | 0.0.0.0 | 80000004 | asExternal | 16  | 01:00:12 |
 | 4.4.4.3  | 0.0.0.0 | 80000004 | asExternal | 16  | 01:00:11 |
 | 4.4.4.4  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:11 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.3  | 1.1.1.8 | 80000001 | asExternal | 16  | 00:00:11 |
 | 4.4.4.4  | 1.1.1.8 | 80000001 | asExternal | 16  | 00:00:11 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal | 16  | 00:00:12 |
 | 4.4.4.4  | 2.2.2.4 | 80000001 | asExternal | 16  | 00:00:11 |
 |__________|_________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid | sequence | type       | len | time     |
 |----------|-------|----------|------------|-----|----------|
 | 6.6.6.1  | 10012 | 80000001 | link       | 24  | 00:00:12 |
 | 6.6.6.2  | 10012 | 80000001 | link       | 24  | 00:00:13 |
 | 6.6.6.3  | 10012 | 80000001 | link       | 24  | 00:00:12 |
 | 6.6.6.4  | 10012 | 80000001 | link       | 24  | 00:00:11 |
 | 6.6.6.2  | 10013 | 80000001 | link       | 24  | 00:00:12 |
 | 6.6.6.3  | 10013 | 80000001 | link       | 24  | 00:00:12 |
 | 6.6.6.1  | 0     | 80000003 | router     | 20  | 00:00:11 |
 | 6.6.6.2  | 0     | 80000004 | router     | 36  | 00:00:11 |
 | 6.6.6.3  | 0     | 80000004 | router     | 36  | 00:00:08 |
 | 6.6.6.4  | 0     | 80000003 | router     | 20  | 00:00:10 |
 | 6.6.6.1  | 10012 | 80000001 | prefix     | 20  | 00:00:12 |
 | 6.6.6.2  | 10012 | 80000001 | prefix     | 20  | 00:00:13 |
 | 6.6.6.3  | 10012 | 80000001 | prefix     | 20  | 00:00:12 |
 | 6.6.6.4  | 10012 | 80000001 | prefix     | 20  | 00:00:11 |
 | 6.6.6.2  | 10013 | 80000001 | prefix     | 20  | 00:00:12 |
 | 6.6.6.3  | 10013 | 80000001 | prefix     | 20  | 00:00:11 |
 | 6.6.6.1  | 0     | 80000003 | asExternal | 16  | 00:00:12 |
 | 6.6.6.2  | 0     | 80000005 | asExternal | 16  | 00:00:12 |
 | 6.6.6.3  | 0     | 80000005 | asExternal | 16  | 00:00:11 |
 | 6.6.6.4  | 0     | 80000003 | asExternal | 16  | 00:00:11 |
 | 6.6.6.1  | 1     | 80000001 | asExternal | 28  | 00:00:12 |
 | 6.6.6.2  | 1     | 80000003 | asExternal | 16  | 00:00:12 |
 | 6.6.6.3  | 1     | 80000003 | asExternal | 16  | 00:00:12 |
 | 6.6.6.4  | 1     | 80000001 | asExternal | 28  | 00:00:11 |
 | 6.6.6.2  | 2     | 80000001 | asExternal | 28  | 00:00:12 |
 | 6.6.6.3  | 2     | 80000001 | asExternal | 28  | 00:00:12 |
 |__________|_______|__________|____________|_____|__________|
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
      `--4.4.4.4
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
      `--6.6.6.4/00000000
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:09 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:09 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:09 |
 | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:09 |
 | O   | 1.1.1.8/30 | 110/1  | ethernet2 | 1.1.1.6 | 00:00:09 |
 | O   | 2.2.2.1/32 | 110/0  | ethernet1 | 1.1.1.1 | 00:00:09 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:09 |
 | O   | 2.2.2.3/32 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:09 |
 | O   | 2.2.2.4/32 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:09 |
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:09 |
 | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:09 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:09 |
 | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:09 |
 | O   | 1234:3::/32   | 110/1  | ethernet2 | 1234:2::2 | 00:00:09 |
 | O   | 4321::1/128   | 110/0  | ethernet1 | 1234:1::1 | 00:00:09 |
 | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:09 |
 | O   | 4321::3/128   | 110/0  | ethernet2 | 1234:2::2 | 00:00:09 |
 | O   | 4321::4/128   | 110/0  | ethernet2 | 1234:2::2 | 00:00:09 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

# Example: ospf multi area

## **Topology diagram**

![topology](/img/rout-ospf44.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz40r1-log.run
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
 area 1 enable
 area 2 enable
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 1 enable
 area 2 enable
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.11 255.255.255.255
 ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 2
 router ospf6 1 enable
 router ospf6 1 area 2
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
 router ospf4 1 area 1 2
 router ospf6 1 enable
 router ospf6 1 area 1 2
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
logging file debug ../binTmp/zzz40r2-log.run
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
 area 1 enable
 area 2 enable
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 1 enable
 area 2 enable
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.22 255.255.255.255
 ipv6 address 4321::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 2
 router ospf6 1 enable
 router ospf6 1 area 2
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
 router ospf4 1 area 1 2
 router ospf6 1 enable
 router ospf6 1 area 1 2
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
 router ospf4 1 area 1 2
 router ospf6 1 enable
 router ospf6 1 area 1 2
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
logging file debug ../binTmp/zzz40r3-log.run
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
 area 1 enable
 area 2 enable
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 1 enable
 area 2 enable
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 1
 router ospf6 1 enable
 router ospf6 1 area 1
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.33 255.255.255.255
 ipv6 address 4321::33 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 2
 router ospf6 1 enable
 router ospf6 1 area 2
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
 router ospf4 1 area 1 2
 router ospf6 1 enable
 router ospf6 1 area 1 2
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
 | ethernet1 | 1    | 1.1.1.1 | 4.4.4.1  | 4     | 00:00:06 |
 | ethernet1 | 2    | 1.1.1.1 | 4.4.4.1  | 4     | 00:00:06 |
 | ethernet2 | 1    | 1.1.1.6 | 4.4.4.3  | 4     | 00:00:06 |
 | ethernet2 | 2    | 1.1.1.6 | 4.4.4.3  | 4     | 00:00:06 |
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
 | ethernet1 | 1    | 1234:1::1 | 6.6.6.1  | 4     | 00:00:06 |
 | ethernet1 | 2    | 1234:1::1 | 6.6.6.1  | 4     | 00:00:06 |
 | ethernet2 | 1    | 1234:2::2 | 6.6.6.3  | 4     | 00:00:06 |
 | ethernet2 | 2    | 1234:2::2 | 6.6.6.3  | 4     | 00:00:06 |
 |___________|______|___________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~|~~~~~~|
 | routerid | lsaid | sequence | type | len | time |
 |----------|-------|----------|------|-----|------|
 |__________|_______|__________|______|_____|______|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~|~~~~~~|
 | routerid | lsaid | sequence | type | len | time |
 |----------|-------|----------|------|-----|------|
 |__________|_______|__________|______|_____|______|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/30  | 0/0    | ethernet1 | null    | 00:00:07 |
 | LOC | 1.1.1.2/32  | 0/1    | ethernet1 | null    | 00:00:07 |
 | C   | 1.1.1.4/30  | 0/0    | ethernet2 | null    | 00:00:07 |
 | LOC | 1.1.1.5/32  | 0/1    | ethernet2 | null    | 00:00:07 |
 | O   | 2.2.2.1/32  | 110/1  | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C   | 2.2.2.2/32  | 0/0    | loopback1 | null    | 00:00:07 |
 | O   | 2.2.2.3/32  | 110/1  | ethernet2 | 1.1.1.6 | 00:00:03 |
 | O   | 2.2.2.11/32 | 110/1  | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C   | 2.2.2.22/32 | 0/0    | loopback2 | null    | 00:00:07 |
 | O   | 2.2.2.33/32 | 110/1  | ethernet2 | 1.1.1.6 | 00:00:03 |
 |_____|_____________|________|___________|_________|__________|
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:07 |
 | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:07 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:07 |
 | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:07 |
 | O   | 4321::1/128   | 110/1  | ethernet1 | 1234:1::1 | 00:00:03 |
 | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:07 |
 | O   | 4321::3/128   | 110/1  | ethernet2 | 1234:2::2 | 00:00:03 |
 | O   | 4321::11/128  | 110/1  | ethernet1 | 1234:1::1 | 00:00:03 |
 | C   | 4321::22/128  | 0/0    | loopback2 | null      | 00:00:07 |
 | O   | 4321::33/128  | 110/1  | ethernet2 | 1234:2::2 | 00:00:03 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

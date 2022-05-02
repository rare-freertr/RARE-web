# Example: ospf address unsuppression

## **Topology diagram**

![topology](/img/rout-ospf52.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz14r1-log.run
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
 area 0 suppress-prefix
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 area 0 suppress-prefix
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 passive
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 passive
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 passive
 router ospf4 1 unsuppress-prefix
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 passive
 router ospf6 1 unsuppress-prefix
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 passive
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 passive
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
logging file debug ../binTmp/zzz14r2-log.run
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
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.111 255.255.255.255
 ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 passive
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 passive
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:04 |
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
 | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:04 |
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
 | 4.4.4.1  | 4.4.4.1 | 80000003 | router      | 28  | 00:00:01 |
 | 4.4.4.2  | 4.4.4.2 | 80000004 | router      | 40  | 00:00:01 |
 | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:05 |
 | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:05 |
 |__________|_________|__________|_____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid     | sequence | type   | len | time     |
 |----------|-----------|----------|--------|-----|----------|
 | 6.6.6.2  | 274783533 | 80000001 | link   | 24  | 00:00:05 |
 | 6.6.6.2  | 274783534 | 80000001 | link   | 24  | 00:00:05 |
 | 6.6.6.1  | 515471251 | 80000001 | link   | 24  | 00:00:05 |
 | 6.6.6.1  | 515471252 | 80000001 | link   | 24  | 00:00:04 |
 | 6.6.6.1  | 515471253 | 80000001 | link   | 24  | 00:00:04 |
 | 6.6.6.1  | 515471254 | 80000001 | link   | 24  | 00:00:04 |
 | 6.6.6.1  | 0         | 80000002 | router | 20  | 00:00:01 |
 | 6.6.6.2  | 0         | 80000002 | router | 20  | 00:00:01 |
 | 6.6.6.2  | 274783533 | 80000001 | prefix | 32  | 00:00:05 |
 | 6.6.6.2  | 274783534 | 80000001 | prefix | 20  | 00:00:05 |
 | 6.6.6.1  | 515471252 | 80000001 | prefix | 32  | 00:00:04 |
 |__________|___________|__________|________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
`--r2
   `--r1
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
 |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix       | metric | iface     | hop     | time     |
 |-----|--------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:05 |
 | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:05 |
 | O   | 2.2.2.2/32   | 110/20 | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C   | 2.2.2.111/32 | 0/0    | loopback1 | null    | 00:00:05 |
 |_____|______________|________|___________|_________|__________|
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
 | O   | 4321::2/128   | 110/20 | ethernet1 | 1234:1::1 | 00:00:02 |
 | C   | 4321::111/128 | 0/0    | loopback1 | null      | 00:00:05 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

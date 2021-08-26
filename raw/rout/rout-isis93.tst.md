# Example: integrated isis change in tag

## **Topology diagram**

![topology](/img/rout-isis93.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz93r1-log.run
!
route-map rm1
 sequence 10 action permit
 sequence 10 set tag set 1000
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
router isis4 1
 vrf v1
 net-id 11.4444.0000.1111.00
 traffeng-id ::
 is-type both
 afi-other enable
 afi-other redistribute connected route-map rm1
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
 router isis4 1 enable
 router isis4 1 other-enable
 router isis4 1 circuit both
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
logging file debug ../binTmp/zzz93r2-log.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match tag 2000-4000
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
router isis6 1
 vrf v1
 net-id 22.6666.0000.2222.00
 traffeng-id ::
 is-type both
 level2 route-map-from rm1
 level2 other-route-map-from rm1
 level1 route-map-from rm1
 level1 other-route-map-from rm1
 afi-other enable
 afi-other redistribute connected
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
 router isis6 1 enable
 router isis6 1 other-enable
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router isis6 1 enable
 router isis6 1 other-enable
 router isis6 1 circuit both
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
logging file debug ../binTmp/zzz93r3-log.run
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
 is-type both
 afi-other enable
 afi-other redistribute connected
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
 router isis4 1 enable
 router isis4 1 other-enable
 router isis4 1 circuit both
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
% no such process
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 nei
r2#show ipv6 isis 1 nei
 |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
 | ethernet1 | 0000.0000.0000 | 1     | 4444.0000.1111 | 1234:1::1  | 1.1.1.1       | 2     | 00:00:15 |
 | ethernet1 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234:1::1  | 1.1.1.1       | 0     | 00:00:15 |
 | ethernet2 | 0000.0000.0000 | 1     | 4444.0000.3333 | 1234:2::2  | 1.1.1.6       | 0     | 00:00:15 |
 | ethernet2 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1234:2::2  | 1.1.1.6       | 0     | 00:00:15 |
 |___________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 dat 2
r2#show ipv4 isis 1 dat 2
% no such process
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
 | 4444.0000.1111.00-00 | 0000000f | apo   | 97  | 00:19:54 |
 | 4444.0000.3333.00-00 | 0000000c | apo   | 141 | 00:19:44 |
 | 6666.0000.2222.00-00 | 00000013 | apo   | 154 | 00:19:44 |
 |______________________|__________|_______|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 tre 2
r2#show ipv4 isis 1 tre 2
% no such process
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:16 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:16 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:16 |
 | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:16 |
 | I   | 2.2.2.1/32 | 115/10 | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:16 |
 | I   | 2.2.2.3/32 | 115/10 | ethernet2 | 1.1.1.6 | 00:00:15 |
 |_____|____________|________|___________|_________|__________|
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:16 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:16 |
 | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:16 |
 | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:16 |
 | I EX | 4321::1/128   | 115/10 | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:16 |
 | I EX | 4321::3/128   | 115/10 | ethernet2 | 1234:2::2 | 00:00:15 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```
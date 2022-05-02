# Example: rip incoming routepolicy metric

## **Topology diagram**

![topology](/img/rout-rip18.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz65r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router rip4 1
 vrf v1
 exit
!
router rip6 1
 vrf v1
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router rip4 1 enable
 router rip6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.111 255.255.255.255
 ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router rip4 1 enable
 router rip6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.222 255.255.255.255
 ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 router rip4 1 enable
 router rip6 1 enable
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

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz65r2-log.run
!
route-policy rm1
 sequence 10 set metric add 9
 sequence 20 pass
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router rip4 1
 vrf v1
 redistribute connected
 exit
!
router rip6 1
 vrf v1
 redistribute connected
 exit
!
interface loopback0
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
 router rip4 1 enable
 router rip6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router rip4 1 enable
 router rip4 1 route-policy-in rm1
 router rip6 1 enable
 router rip6 1 route-policy-in rm1
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
logging file debug ../binTmp/zzz65r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router rip4 1
 vrf v1
 exit
!
router rip6 1
 vrf v1
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router rip4 1 enable
 router rip6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.111 255.255.255.255
 ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router rip4 1 enable
 router rip6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 router rip4 1 enable
 router rip6 1 enable
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
r2#show ipv4 rip 1 sum
r2#show ipv4 rip 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor | uptime   |
 |-----------|-------|----------|----------|
 | ethernet1 | 2     | 1.1.1.1  | 00:00:11 |
 | ethernet2 | 2     | 1.1.1.6  | 00:00:11 |
 |___________|_______|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 rip 1 sum
r2#show ipv6 rip 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor  | uptime   |
 |-----------|-------|-----------|----------|
 | ethernet1 | 2     | 1234:1::1 | 00:00:11 |
 | ethernet2 | 2     | 1234:2::2 | 00:00:11 |
 |___________|_______|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 rip 1 dat
r2#show ipv4 rip 1 dat
 |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix       | metric | iface     | hop     | time     |
 |-----|--------------|--------|-----------|---------|----------|
 | R   | 1.1.1.0/30   | 1/0    | ethernet1 | null    | 00:00:41 |
 | R   | 1.1.1.4/30   | 1/0    | ethernet2 | null    | 00:00:41 |
 | R   | 2.2.2.1/32   | 120/1  | ethernet1 | 1.1.1.1 | 00:00:11 |
 | R   | 2.2.2.3/32   | 120/10 | ethernet2 | 1.1.1.6 | 00:00:11 |
 | R   | 2.2.2.111/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:11 |
 |_____|______________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 rip 1 dat
r2#show ipv6 rip 1 dat
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric | iface     | hop       | time     |
 |-----|---------------|--------|-----------|-----------|----------|
 | R   | 1234:1::/32   | 1/0    | ethernet1 | null      | 00:00:41 |
 | R   | 1234:2::/32   | 1/0    | ethernet2 | null      | 00:00:41 |
 | R   | 4321::1/128   | 120/1  | ethernet1 | 1234:1::1 | 00:00:11 |
 | R   | 4321::3/128   | 120/10 | ethernet2 | 1234:2::2 | 00:00:11 |
 | R   | 4321::111/128 | 120/1  | ethernet1 | 1234:1::1 | 00:00:11 |
 |_____|_______________|________|___________|___________|__________|
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
 | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:41 |
 | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:41 |
 | C   | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:41 |
 | LOC | 1.1.1.5/32   | 0/1    | ethernet2 | null    | 00:00:41 |
 | R   | 2.2.2.1/32   | 120/1  | ethernet1 | 1.1.1.1 | 00:00:11 |
 | C   | 2.2.2.2/32   | 0/0    | loopback0 | null    | 00:00:41 |
 | R   | 2.2.2.3/32   | 120/10 | ethernet2 | 1.1.1.6 | 00:00:11 |
 | R   | 2.2.2.111/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:11 |
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:42 |
 | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:42 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:41 |
 | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:41 |
 | R   | 4321::1/128   | 120/1  | ethernet1 | 1234:1::1 | 00:00:11 |
 | C   | 4321::2/128   | 0/0    | loopback0 | null      | 00:00:42 |
 | R   | 4321::3/128   | 120/10 | ethernet2 | 1234:2::2 | 00:00:12 |
 | R   | 4321::111/128 | 120/1  | ethernet1 | 1234:1::1 | 00:00:11 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

# Example: rip with bfd

## **Topology diagram**

![topology](/img/rout-rip20.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz12r1-log.run
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
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 bfd 100 100 3
 router rip4 1 enable
 router rip4 1 bfd
 router rip6 1 enable
 router rip6 1 bfd
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 bfd 100 100 3
 router rip4 1 enable
 router rip4 1 bfd
 router rip4 1 distance 130
 router rip6 1 enable
 router rip6 1 bfd
 router rip6 1 distance 130
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
logging file debug ../binTmp/zzz12r2-log.run
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
 ipv4 bfd 100 100 3
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 bfd 100 100 3
 router rip4 1 enable
 router rip4 1 bfd
 router rip6 1 enable
 router rip6 1 bfd
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv4 bfd 100 100 3
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 bfd 100 100 3
 router rip4 1 enable
 router rip4 1 bfd
 router rip4 1 distance 130
 router rip6 1 enable
 router rip6 1 bfd
 router rip6 1 distance 130
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
 | ethernet2 | 4     | 1.1.1.5  | 00:00:07 |
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
 | ethernet2 | 4     | 1234:2::1 | 00:00:07 |
 |___________|_______|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 rip 1 dat
r2#show ipv4 rip 1 dat
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | R   | 1.1.1.0/30 | 130/1  | ethernet2 | 1.1.1.5 | 00:00:07 |
 | R   | 1.1.1.4/30 | 1/0    | ethernet2 | null    | 00:00:37 |
 | R   | 2.2.2.1/32 | 130/1  | ethernet2 | 1.1.1.5 | 00:00:07 |
 | R   | 2.2.2.2/32 | 130/2  | ethernet2 | 1.1.1.5 | 00:00:07 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 rip 1 dat
r2#show ipv6 rip 1 dat
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop       | time     |
 |-----|-------------|--------|-----------|-----------|----------|
 | R   | 1234:1::/32 | 130/1  | ethernet2 | 1234:2::1 | 00:00:07 |
 | R   | 1234:2::/32 | 1/0    | ethernet2 | null      | 00:00:37 |
 | R   | 4321::1/128 | 130/1  | ethernet2 | 1234:2::1 | 00:00:07 |
 | R   | 4321::2/128 | 130/2  | ethernet2 | 1234:2::1 | 00:00:07 |
 |_____|_____________|________|___________|___________|__________|
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
 | R   | 1.1.1.0/30 | 130/1  | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:37 |
 | LOC | 1.1.1.6/32 | 0/1    | ethernet2 | null    | 00:00:37 |
 | R   | 2.2.2.1/32 | 130/1  | ethernet2 | 1.1.1.5 | 00:00:07 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:37 |
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
 | R   | 1234:1::/32   | 130/1  | ethernet2 | 1234:2::1 | 00:00:07 |
 | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:37 |
 | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:37 |
 | R   | 4321::1/128   | 130/1  | ethernet2 | 1234:2::1 | 00:00:07 |
 | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:37 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

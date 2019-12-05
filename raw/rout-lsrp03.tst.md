# Example: lsrp point2point chain

## **Topology diagram**

![topology](/img/rout-lsrp03.tst.png)

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
router lsrp4 1
 vrf v1
 router-id 4.4.4.1
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
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
 router lsrp4 1 enable
 router lsrp6 1 enable
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.2
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
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
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.3
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
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
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
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
router lsrp4 1
 vrf v1
 router-id 4.4.4.4
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.4
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
 router lsrp4 1 enable
 router lsrp6 1 enable
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
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peer    | ready | uptime   |
 |-----------|---------|------|---------|-------|----------|
 | ethernet1 | 4.4.4.1 | r1   | 1.1.1.1 | true  | 00:00:12 |
 | ethernet2 | 4.4.4.3 | r3   | 1.1.1.6 | true  | 00:00:12 |
 |___________|_________|______|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 nei
r2#show ipv6 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peer      | ready | uptime   |
 |-----------|---------|------|-----------|-------|----------|
 | ethernet1 | 6.6.6.1 | r1   | 1234:1::1 | true  | 00:00:12 |
 | ethernet2 | 6.6.6.3 | r3   | 1234:2::2 | true  | 00:00:12 |
 |___________|_________|______|___________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 dat
r2#show ipv4 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo        | left     |
 |---------|------|-----|-----|-----|-------------|----------|
 | 4.4.4.1 | r1   | 1   | 2   | 6   | 0           | 00:59:50 |
 | 4.4.4.2 | r2   | 2   | 3   | 11  | -895827968  | 00:59:50 |
 | 4.4.4.3 | r3   | 2   | 3   | 11  | -2141633566 | 00:59:55 |
 | 4.4.4.4 | r4   | 1   | 2   | 7   | 127637240   | 00:59:55 |
 |_________|______|_____|_____|_____|_____________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 dat
r2#show ipv6 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo       | left     |
 |---------|------|-----|-----|-----|------------|----------|
 | 6.6.6.1 | r1   | 1   | 2   | 7   | 0          | 00:59:51 |
 | 6.6.6.2 | r2   | 2   | 3   | 11  | 1929548798 | 00:59:55 |
 | 6.6.6.3 | r3   | 2   | 3   | 11  | 1049815609 | 00:59:55 |
 | 6.6.6.4 | r4   | 1   | 2   | 6   | 0          | 00:59:43 |
 |_________|______|_____|_____|_____|____________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 tre
r2#show ipv4 lsrp 1 tre
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
r2#show ipv6 lsrp 1 tre
r2#show ipv6 lsrp 1 tre
`--6.6.6.2
  |`--6.6.6.1
   `--6.6.6.3
      `--6.6.6.4
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
 | L   | 1.1.1.8/30 | 70/10  | ethernet2 | 1.1.1.6 | 00:00:05 |
 | L   | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:05 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:05 |
 | L   | 2.2.2.3/32 | 70/10  | ethernet2 | 1.1.1.6 | 00:00:05 |
 | L   | 2.2.2.4/32 | 70/20  | ethernet2 | 1.1.1.6 | 00:00:05 |
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
 | L   | 1234:3::/32   | 70/10  | ethernet2 | 1234:2::2 | 00:00:05 |
 | L   | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:05 |
 | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:05 |
 | L   | 4321::3/128   | 70/10  | ethernet2 | 1234:2::2 | 00:00:05 |
 | L   | 4321::4/128   | 70/20  | ethernet2 | 1234:2::2 | 00:00:05 |
 |_____|_______________|________|___________|___________|__________|
r2#
r2#
```

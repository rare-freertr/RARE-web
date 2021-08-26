# Example: lsrp with php sr

## **Topology diagram**

![topology](/img/rout-lsrp30.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz84r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.1
 segrout 10 1 pop
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
 segrout 10 1 pop
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 001f.6a68.6012
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 pseudowire v1 loopback1 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 005c.693c.151e
 vrf forwarding v1
 ipv4 address 3.3.4.1 255.255.255.0
 pseudowire v1 loopback1 pweompls 4321::3 1234
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
logging file debug ../binTmp/zzz84r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.2
 segrout 10 2 pop
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
 segrout 10 2 pop
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
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1235::2 ffff::
 ipv6 access-group-in test6
 mpls enable
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
!
!
!
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
logging file debug ../binTmp/zzz84r3-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.3
 segrout 10 3 pop
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
 segrout 10 3 pop
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
 ipv4 address 1.1.2.3 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1235::3 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 004a.6a76.2d14
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 pseudowire v1 loopback1 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 0011.002c.6967
 vrf forwarding v1
 ipv4 address 3.3.4.2 255.255.255.0
 pseudowire v1 loopback1 pweompls 4321::1 1234
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
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:29 |
 | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.2.3 | true  | 00:00:29 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 nei
r2#show ipv6 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:29 |
 | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1235::3 | true  | 00:00:29 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 dat
r2#show ipv4 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 4.4.4.1 | r1   | 1   | 4   | 11  | 722ed93c | 00:59:34 |
 | 4.4.4.2 | r2   | 2   | 3   | 11  | 3456ff9d | 00:59:35 |
 | 4.4.4.3 | r3   | 1   | 4   | 11  | 0bcce45e | 00:59:35 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 dat
r2#show ipv6 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 6.6.6.1 | r1   | 1   | 2   | 7   | 722ed93c | 00:59:34 |
 | 6.6.6.2 | r2   | 2   | 3   | 11  | 2507cc5f | 00:59:36 |
 | 6.6.6.3 | r3   | 1   | 2   | 7   | dca61ffd | 00:59:36 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 tre
r2#show ipv4 lsrp 1 tre
`--r2
  |`--r1
   `--r3
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 tre
r2#show ipv6 lsrp 1 tre
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
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:34 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:34 |
 | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:34 |
 | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:34 |
 | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:26 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:34 |
 | L EX | 2.2.2.3/32 | 70/10  | ethernet2 | 1.1.2.3 | 00:00:25 |
 | L EX | 3.3.3.0/24 | 70/10  | ethernet2 | 1.1.2.3 | 00:00:25 |
 | L EX | 3.3.4.0/24 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:26 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop     | time     |
 |------|-------------|--------|-----------|---------|----------|
 | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:34 |
 | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:34 |
 | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:34 |
 | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:34 |
 | L EX | 4321::1/128 | 70/10  | ethernet1 | 1234::1 | 00:00:25 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:34 |
 | L EX | 4321::3/128 | 70/10  | ethernet2 | 1235::3 | 00:00:24 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 segrou v1
r2#show ipv4 segrou v1
 |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~~~~|
 | prefix     | index | base    | oldbase |
 |------------|-------|---------|---------|
 | 2.2.2.1/32 | 1     | 1015751 | 1015751 |
 | 2.2.2.3/32 | 3     | 600602  | 600602  |
 | 3.3.3.0/24 | 3     | 600602  | 600602  |
 | 3.3.4.0/24 | 1     | 1015751 | 1015751 |
 |____________|_______|_________|_________|
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
 | 4321::1/128 | 1     | 177395 | 177395  |
 | 4321::3/128 | 3     | 817276 | 817276  |
 |_____________|_______|________|_________|
r2#
r2#
```

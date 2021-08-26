# Example: lsrp with selective sr

## **Topology diagram**

![topology](/img/rout-lsrp33.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz75r1-log.run
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
 segrout 10 0
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
 segrout 10 0
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router lsrp4 1 enable
 router lsrp4 1 segrout 1
 router lsrp6 1 enable
 router lsrp6 1 segrout 1
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz75r2-log.run
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
 segrout 10 0
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
 segrout 10 0
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router lsrp4 1 enable
 router lsrp4 1 segrout 2
 router lsrp6 1 enable
 router lsrp6 1 segrout 2
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
logging file debug ../binTmp/zzz75r3-log.run
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
 segrout 10 0
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
 segrout 10 0
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router lsrp4 1 enable
 router lsrp4 1 segrout 3
 router lsrp6 1 enable
 router lsrp6 1 segrout 3
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
r2#sho
r2#sho
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:09 |
 | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.2.3 | true  | 00:00:09 |
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
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:09 |
 | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1235::3 | true  | 00:00:09 |
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
 | 4.4.4.1 | r1   | 1   | 2   | 9   | b06d2c5d | 00:59:57 |
 | 4.4.4.2 | r2   | 2   | 3   | 13  | cba4b9b7 | 00:59:57 |
 | 4.4.4.3 | r3   | 1   | 2   | 9   | 2585017d | 00:59:54 |
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
 | 6.6.6.1 | r1   | 1   | 2   | 9   | 6af37363 | 00:59:55 |
 | 6.6.6.2 | r2   | 2   | 3   | 13  | 517adb5d | 00:59:55 |
 | 6.6.6.3 | r3   | 1   | 2   | 9   | 2585017d | 00:59:54 |
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:15 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:15 |
 | C   | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:15 |
 | LOC | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:15 |
 | L   | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:15 |
 | L   | 2.2.2.3/32 | 70/10  | ethernet2 | 1.1.2.3 | 00:00:06 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | C   | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:15 |
 | LOC | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:15 |
 | C   | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:15 |
 | LOC | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:15 |
 | L   | 4321::1/128 | 70/10  | ethernet1 | 1234::1 | 00:00:05 |
 | C   | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:15 |
 | L   | 4321::3/128 | 70/10  | ethernet2 | 1235::3 | 00:00:06 |
 |_____|_____________|________|___________|_________|__________|
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
 | 2.2.2.1/32 | 1     | 892517 | 892517  |
 | 2.2.2.3/32 | 3     | 210264 | 210264  |
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
 | 4321::1/128 | 1     | 836124 | 836124  |
 | 4321::3/128 | 3     | 64750  | 64750   |
 |_____________|_______|________|_________|
r2#
r2#
```
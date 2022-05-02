# Example: babel ingress route filtering with routepolicy

## **Topology diagram**

![topology](/img/rout-babel07.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz77r1-log.run
!
route-policy p4
 sequence 10 if network 2.2.2.12/32 ge 32 le 32
 sequence 20   drop
 sequence 30 else
 sequence 40   pass
 sequence 50 enif
 exit
!
route-policy p6
 sequence 10 if network 4321::12/128 ge 128 le 128
 sequence 20   drop
 sequence 30 else
 sequence 40   pass
 sequence 50 enif
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router babel4 1
 vrf v1
 router-id 1111-2222-3333-0001
 redistribute connected
 exit
!
router babel6 1
 vrf v1
 router-id 1111-2222-3333-0001
 redistribute connected
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.11 255.255.255.255
 ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.21 255.255.255.255
 ipv6 address 4321::21 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 router babel4 1 enable
 router babel4 1 route-policy-in p4
 router babel6 1 enable
 router babel6 1 route-policy-in p6
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
logging file debug ../binTmp/zzz77r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router babel4 1
 vrf v1
 router-id 1111-2222-3333-0002
 redistribute connected
 exit
!
router babel6 1
 vrf v1
 router-id 1111-2222-3333-0002
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
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.12 255.255.255.255
 ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 vrf forwarding v1
 ipv4 address 2.2.2.22 255.255.255.255
 ipv6 address 4321::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 router babel4 1 enable
 router babel6 1 enable
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
r2#show ipv4 babel 1 sum
r2#show ipv4 babel 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor | uptime   |
 |-----------|-------|----------|----------|
 | ethernet1 | 4     | 1.1.1.1  | 00:00:04 |
 |___________|_______|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 babel 1 sum
r2#show ipv6 babel 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor  | uptime   |
 |-----------|-------|-----------|----------|
 | ethernet1 | 4     | 1234:1::1 | 00:00:04 |
 |___________|_______|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 babel 1 dat
r2#show ipv4 babel 1 dat
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric  | iface     | hop     | time     |
 |-----|-------------|---------|-----------|---------|----------|
 | A   | 1.1.1.0/30  | 1/0     | ethernet1 | null    | 00:00:24 |
 | A   | 2.2.2.1/32  | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 | A   | 2.2.2.11/32 | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 | A   | 2.2.2.21/32 | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 |_____|_____________|_________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 babel 1 dat
r2#show ipv6 babel 1 dat
 |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix       | metric  | iface     | hop       | time     |
 |-----|--------------|---------|-----------|-----------|----------|
 | A   | 1234:1::/32  | 1/0     | ethernet1 | null      | 00:00:24 |
 | A   | 4321::1/128  | 130/100 | ethernet1 | 1234:1::1 | 00:00:04 |
 | A   | 4321::11/128 | 130/100 | ethernet1 | 1234:1::1 | 00:00:04 |
 | A   | 4321::21/128 | 130/100 | ethernet1 | 1234:1::1 | 00:00:04 |
 |_____|______________|_________|___________|___________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric  | iface     | hop     | time     |
 |-----|-------------|---------|-----------|---------|----------|
 | C   | 1.1.1.0/30  | 0/0     | ethernet1 | null    | 00:00:25 |
 | LOC | 1.1.1.2/32  | 0/1     | ethernet1 | null    | 00:00:25 |
 | A   | 2.2.2.1/32  | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 | C   | 2.2.2.2/32  | 0/0     | loopback0 | null    | 00:00:25 |
 | A   | 2.2.2.11/32 | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 | C   | 2.2.2.12/32 | 0/0     | loopback1 | null    | 00:00:25 |
 | A   | 2.2.2.21/32 | 130/100 | ethernet1 | 1.1.1.1 | 00:00:04 |
 | C   | 2.2.2.22/32 | 0/0     | loopback2 | null    | 00:00:25 |
 |_____|_____________|_________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric  | iface     | hop       | time     |
 |-----|---------------|---------|-----------|-----------|----------|
 | C   | 1234:1::/32   | 0/0     | ethernet1 | null      | 00:00:25 |
 | LOC | 1234:1::2/128 | 0/1     | ethernet1 | null      | 00:00:25 |
 | A   | 4321::1/128   | 130/100 | ethernet1 | 1234:1::1 | 00:00:05 |
 | C   | 4321::2/128   | 0/0     | loopback0 | null      | 00:00:25 |
 | A   | 4321::11/128  | 130/100 | ethernet1 | 1234:1::1 | 00:00:05 |
 | C   | 4321::12/128  | 0/0     | loopback1 | null      | 00:00:25 |
 | A   | 4321::21/128  | 130/100 | ethernet1 | 1234:1::1 | 00:00:05 |
 | C   | 4321::22/128  | 0/0     | loopback2 | null      | 00:00:25 |
 |_____|_______________|_________|___________|___________|__________|
r2#
r2#
```

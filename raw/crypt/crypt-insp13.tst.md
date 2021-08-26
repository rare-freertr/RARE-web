# Example: mpls inspection with selective egress drop

## **Topology diagram**

![topology](/img/crypt-insp13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz79r1-log.run
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
 label-mode per-prefix
 exit
!
interface loopback0
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
 no ipv4 unreachables
 ipv4 access-group-in test4
 ipv6 address 1234:1::1 ffff:ffff::
 no ipv6 unreachables
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
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
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
!
!
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
logging file debug ../binTmp/zzz79r2-log.run
!
access-list test
 sequence 10 permit all 2.2.2.3 255.255.255.255 all any all
 sequence 20 permit all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
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
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 mpls inspect mac drop-tx allow-list test
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.2.3
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::3
!
!
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
logging file debug ../binTmp/zzz79r3-log.run
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
 label-mode per-prefix
 exit
!
interface loopback0
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
 no ipv4 unreachables
 ipv4 access-group-in test4
 ipv6 address 1234:2::3 ffff:ffff::
 no ipv6 unreachables
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.2.2
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.2.2
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
!
!
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
r2#show mpls insp eth1 sess
r2#show mpls insp eth1 sess
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source              | target              | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
 | tx  | 1   | 0   | 2.2.2.3 | 828307524 | 2.2.2.1 | 828307524 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 828307525 | 2.2.2.1 | 828307525 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 828307526 | 2.2.2.1 | 828307526 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 828307527 | 2.2.2.1 | 828307527 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 828307528 | 2.2.2.1 | 828307528 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687365 | 2.2.2.2 | 977687365 | 1  | 1  | 44 | 44 | 00:00:17 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687366 | 2.2.2.2 | 977687366 | 1  | 1  | 44 | 44 | 00:00:17 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687367 | 2.2.2.2 | 977687367 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687368 | 2.2.2.2 | 977687368 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687369 | 2.2.2.2 | 977687369 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687370 | 2.2.2.2 | 977687370 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687371 | 2.2.2.2 | 977687371 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687372 | 2.2.2.3 | 977687372 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687373 | 2.2.2.3 | 977687373 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687374 | 2.2.2.3 | 977687374 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687375 | 2.2.2.3 | 977687375 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 977687376 | 2.2.2.3 | 977687376 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115292 | 4321::2 | 716115292 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115293 | 4321::2 | 716115293 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115294 | 4321::2 | 716115294 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115295 | 4321::2 | 716115295 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115296 | 4321::2 | 716115296 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115297 | 4321::2 | 716115297 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115298 | 4321::3 | 716115298 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115299 | 4321::3 | 716115299 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115300 | 4321::3 | 716115300 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115301 | 4321::3 | 716115301 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 716115302 | 4321::3 | 716115302 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 58  | 0   | 4321::3 | 932019156 | 4321::1 | 932019156 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 932019157 | 4321::1 | 932019157 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 932019158 | 4321::1 | 932019158 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 932019159 | 4321::1 | 932019159 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 932019160 | 4321::1 | 932019160 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show mpls insp eth1 top
r2#show mpls insp eth1 top
 |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
 |         | packet  | byte      |          |
 | addr    | rx | tx | rx  | tx  | time     |
 |---------|----|----|-----|-----|----------|
 | 2.2.2.1 | 17 | 17 | 748 | 748 | 00:00:17 |
 | 2.2.2.2 | 7  | 7  | 308 | 308 | 00:00:17 |
 | 2.2.2.3 | 10 | 10 | 440 | 440 | 00:00:10 |
 | 4321::1 | 16 | 16 | 384 | 384 | 00:00:12 |
 | 4321::2 | 6  | 6  | 144 | 144 | 00:00:12 |
 | 4321::3 | 10 | 10 | 240 | 240 | 00:00:10 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

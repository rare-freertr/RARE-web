# Example: mpls inspection with selective ingress drop

## **Topology diagram**

![topology](/img/crypt-insp12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz60r1-log.run
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
logging file debug ../binTmp/zzz60r2-log.run
!
access-list test
 sequence 10 permit all any all 2.2.2.3 255.255.255.255 all
 sequence 20 permit all any all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
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
 mpls inspect mac drop-rx allow-list test
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
logging file debug ../binTmp/zzz60r3-log.run
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
 | rx  | 1   | 0   | 2.2.2.1 | 389627646 | 2.2.2.3 | 389627646 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 389627647 | 2.2.2.3 | 389627647 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 389627648 | 2.2.2.3 | 389627648 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 389627649 | 2.2.2.3 | 389627649 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 389627650 | 2.2.2.3 | 389627650 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 1   | 0   | 2.2.2.3 | 606213468 | 2.2.2.1 | 606213468 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 606213469 | 2.2.2.1 | 606213469 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 606213470 | 2.2.2.1 | 606213470 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 606213471 | 2.2.2.1 | 606213471 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 606213472 | 2.2.2.1 | 606213472 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 791802474 | 2.2.2.1 | 791802474 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 791802475 | 2.2.2.1 | 791802475 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 791802476 | 2.2.2.1 | 791802476 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 791802477 | 2.2.2.1 | 791802477 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 791802478 | 2.2.2.1 | 791802478 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 243911124 | 4321::1 | 243911124 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 243911125 | 4321::1 | 243911125 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 243911126 | 4321::1 | 243911126 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 243911127 | 4321::1 | 243911127 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 243911128 | 4321::1 | 243911128 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389607 | 4321::1 | 791389607 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389608 | 4321::1 | 791389608 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389609 | 4321::1 | 791389609 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389610 | 4321::1 | 791389610 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389611 | 4321::1 | 791389611 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389612 | 4321::1 | 791389612 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389613 | 4321::1 | 791389613 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389614 | 4321::1 | 791389614 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 791389615 | 4321::1 | 791389615 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 58  | 0   | 4321::1 | 989991625 | 4321::3 | 989991625 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 989991626 | 4321::3 | 989991626 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 989991627 | 4321::3 | 989991627 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 989991628 | 4321::3 | 989991628 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 989991629 | 4321::3 | 989991629 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
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
 | 2.2.2.1 | 15 | 15 | 660 | 660 | 00:00:13 |
 | 2.2.2.2 | 5  | 5  | 220 | 220 | 00:00:13 |
 | 2.2.2.3 | 10 | 10 | 440 | 440 | 00:00:00 |
 | 4321::1 | 19 | 19 | 456 | 456 | 00:00:12 |
 | 4321::2 | 9  | 9  | 216 | 216 | 00:00:12 |
 | 4321::3 | 10 | 10 | 240 | 240 | 00:00:00 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

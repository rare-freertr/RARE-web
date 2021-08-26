# Example: mpls inspection with egress drop

## **Topology diagram**

![topology](/img/crypt-insp09.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz3r1-log.run
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
logging file debug ../binTmp/zzz3r2-log.run
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
 mpls inspect mac drop-tx
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
logging file debug ../binTmp/zzz3r3-log.run
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
 | rx  | 1   | 0   | 2.2.2.1 | 770557799 | 2.2.2.2 | 770557799 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557800 | 2.2.2.2 | 770557800 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557801 | 2.2.2.2 | 770557801 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557802 | 2.2.2.2 | 770557802 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557803 | 2.2.2.2 | 770557803 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557804 | 2.2.2.2 | 770557804 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557805 | 2.2.2.2 | 770557805 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557806 | 2.2.2.2 | 770557806 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557807 | 2.2.2.2 | 770557807 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557808 | 2.2.2.3 | 770557808 | 1  | 0  | 44 | 0  | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557809 | 2.2.2.3 | 770557809 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557810 | 2.2.2.3 | 770557810 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557811 | 2.2.2.3 | 770557811 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557812 | 2.2.2.3 | 770557812 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557813 | 2.2.2.3 | 770557813 | 1  | 1  | 44 | 44 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557814 | 2.2.2.3 | 770557814 | 1  | 1  | 44 | 44 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557815 | 2.2.2.3 | 770557815 | 1  | 1  | 44 | 44 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557816 | 2.2.2.3 | 770557816 | 1  | 1  | 44 | 44 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 770557817 | 2.2.2.3 | 770557817 | 1  | 1  | 44 | 44 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297289 | 4321::2 | 474297289 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297290 | 4321::2 | 474297290 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297291 | 4321::2 | 474297291 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297292 | 4321::2 | 474297292 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297293 | 4321::2 | 474297293 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297294 | 4321::3 | 474297294 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297295 | 4321::3 | 474297295 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297296 | 4321::3 | 474297296 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297297 | 4321::3 | 474297297 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 474297298 | 4321::3 | 474297298 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
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
 | 2.2.2.1 | 19 | 18 | 836 | 792 | 00:00:24 |
 | 2.2.2.2 | 9  | 9  | 396 | 396 | 00:00:24 |
 | 2.2.2.3 | 10 | 9  | 440 | 396 | 00:00:22 |
 | 4321::1 | 10 | 10 | 240 | 240 | 00:00:22 |
 | 4321::2 | 5  | 5  | 120 | 120 | 00:00:22 |
 | 4321::3 | 5  | 5  | 120 | 120 | 00:00:20 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

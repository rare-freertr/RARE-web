# Example: mpls inspection

## **Topology diagram**

![topology](/img/crypt-insp05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz23r1-log.run
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
logging file debug ../binTmp/zzz23r2-log.run
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
 mpls inspect mac
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
logging file debug ../binTmp/zzz23r3-log.run
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
 | tx  | 1   | 0   | 2.2.2.2 | 105433207 | 2.2.2.1 | 105433207 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 105433208 | 2.2.2.1 | 105433208 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 105433209 | 2.2.2.1 | 105433209 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 105433210 | 2.2.2.1 | 105433210 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 105433211 | 2.2.2.1 | 105433211 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468782 | 2.2.2.2 | 169468782 | 1  | 1  | 44 | 44 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468783 | 2.2.2.2 | 169468783 | 1  | 1  | 44 | 44 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468784 | 2.2.2.2 | 169468784 | 1  | 1  | 44 | 44 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468785 | 2.2.2.2 | 169468785 | 1  | 1  | 44 | 44 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468786 | 2.2.2.2 | 169468786 | 1  | 1  | 44 | 44 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468787 | 2.2.2.2 | 169468787 | 1  | 1  | 44 | 44 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468788 | 2.2.2.2 | 169468788 | 1  | 1  | 44 | 44 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468789 | 2.2.2.2 | 169468789 | 1  | 1  | 44 | 44 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468790 | 2.2.2.3 | 169468790 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468791 | 2.2.2.3 | 169468791 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468792 | 2.2.2.3 | 169468792 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468793 | 2.2.2.3 | 169468793 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 169468794 | 2.2.2.3 | 169468794 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 1   | 0   | 2.2.2.3 | 344127657 | 2.2.2.1 | 344127657 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 344127658 | 2.2.2.1 | 344127658 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 344127659 | 2.2.2.1 | 344127659 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 344127660 | 2.2.2.1 | 344127660 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 344127661 | 2.2.2.1 | 344127661 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 651710653 | 4321::1 | 651710653 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 651710654 | 4321::1 | 651710654 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 651710655 | 4321::1 | 651710655 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 651710656 | 4321::1 | 651710656 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 651710657 | 4321::1 | 651710657 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 760081819 | 4321::1 | 760081819 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 760081820 | 4321::1 | 760081820 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 760081821 | 4321::1 | 760081821 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 760081822 | 4321::1 | 760081822 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 760081823 | 4321::1 | 760081823 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 58  | 0   | 4321::1 | 840739285 | 4321::2 | 840739285 | 1  | 1  | 24 | 24 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739286 | 4321::2 | 840739286 | 1  | 1  | 24 | 24 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739287 | 4321::2 | 840739287 | 1  | 1  | 24 | 24 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739288 | 4321::2 | 840739288 | 1  | 1  | 24 | 24 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739289 | 4321::2 | 840739289 | 1  | 1  | 24 | 24 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739290 | 4321::3 | 840739290 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739291 | 4321::3 | 840739291 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739292 | 4321::3 | 840739292 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739293 | 4321::3 | 840739293 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 840739294 | 4321::3 | 840739294 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show mpls insp eth1 top
r2#show mpls insp eth1 top
 |~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
 |         | packet  | byte        |          |
 | addr    | rx | tx | rx   | tx   | time     |
 |---------|----|----|------|------|----------|
 | 2.2.2.1 | 23 | 23 | 1012 | 1012 | 00:00:02 |
 | 2.2.2.2 | 13 | 13 | 572  | 572  | 00:00:02 |
 | 2.2.2.3 | 10 | 10 | 440  | 440  | 00:00:01 |
 | 4321::1 | 20 | 20 | 480  | 480  | 00:00:01 |
 | 4321::2 | 10 | 10 | 240  | 240  | 00:00:01 |
 | 4321::3 | 10 | 10 | 240  | 240  | 00:00:00 |
 |_________|____|____|______|______|__________|
r2#
r2#
```

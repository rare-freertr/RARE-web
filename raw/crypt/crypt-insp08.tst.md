# Example: mpls inspection with ingress drop

## **Topology diagram**

![topology](/img/crypt-insp08.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz59r1-log.run
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
logging file debug ../binTmp/zzz59r2-log.run
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
 mpls inspect mac drop-rx
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
logging file debug ../binTmp/zzz59r3-log.run
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
 | tx  | 1   | 0   | 2.2.2.3 | 192220488 | 2.2.2.1 | 192220488 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 192220489 | 2.2.2.1 | 192220489 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 192220490 | 2.2.2.1 | 192220490 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 192220491 | 2.2.2.1 | 192220491 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 192220492 | 2.2.2.1 | 192220492 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115661 | 2.2.2.1 | 884115661 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115662 | 2.2.2.1 | 884115662 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115663 | 2.2.2.1 | 884115663 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115664 | 2.2.2.1 | 884115664 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115665 | 2.2.2.1 | 884115665 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 884115666 | 2.2.2.1 | 884115666 | 1  | 1  | 44 | 44 | 00:00:21 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 370169352 | 4321::1 | 370169352 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 370169353 | 4321::1 | 370169353 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 370169354 | 4321::1 | 370169354 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 370169355 | 4321::1 | 370169355 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 370169356 | 4321::1 | 370169356 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 795648054 | 4321::1 | 795648054 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 795648055 | 4321::1 | 795648055 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 795648056 | 4321::1 | 795648056 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 795648057 | 4321::1 | 795648057 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 795648058 | 4321::1 | 795648058 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
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
 | 2.2.2.1 | 11 | 11 | 484 | 484 | 00:00:22 |
 | 2.2.2.2 | 6  | 6  | 264 | 264 | 00:00:22 |
 | 2.2.2.3 | 5  | 5  | 220 | 220 | 00:00:00 |
 | 4321::1 | 10 | 10 | 240 | 240 | 00:00:21 |
 | 4321::2 | 5  | 5  | 120 | 120 | 00:00:21 |
 | 4321::3 | 5  | 5  | 120 | 120 | 00:00:00 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

# Example: mpls inspection with selective egress drop

## **Topology diagram**

![topology](/img/crypt-insp13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz46r1-log.run
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
 label4mode per-prefix
 label6mode per-prefix
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
interface ethernet1
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
logging file debug ../binTmp/zzz46r2-log.run
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
 label4mode per-prefix
 label6mode per-prefix
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
interface ethernet1
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
logging file debug ../binTmp/zzz46r3-log.run
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
 label4mode per-prefix
 label6mode per-prefix
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source               | target               |      | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port       | addr    | port       | url  | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|------------|---------|------------|------|----|----|----|----|----------|----------------|----------------|
 | rx  | 1   | 0   | 2.2.2.1 | 793961305  | 2.2.2.2 | 793961305  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961306  | 2.2.2.2 | 793961306  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961307  | 2.2.2.2 | 793961307  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961308  | 2.2.2.2 | 793961308  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961309  | 2.2.2.2 | 793961309  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961310  | 2.2.2.3 | 793961310  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961311  | 2.2.2.3 | 793961311  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961312  | 2.2.2.3 | 793961312  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961313  | 2.2.2.3 | 793961313  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 793961314  | 2.2.2.3 | 793961314  | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 1   | 0   | 2.2.2.3 | 1005585672 | 2.2.2.1 | 1005585672 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 1005585673 | 2.2.2.1 | 1005585673 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 1005585674 | 2.2.2.1 | 1005585674 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 1005585675 | 2.2.2.1 | 1005585675 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 1005585676 | 2.2.2.1 | 1005585676 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 525566951  | 4321::1 | 525566951  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 525566952  | 4321::1 | 525566952  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 525566953  | 4321::1 | 525566953  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 525566954  | 4321::1 | 525566954  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 525566955  | 4321::1 | 525566955  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 58  | 0   | 4321::1 | 1046870382 | 4321::2 | 1046870382 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870383 | 4321::2 | 1046870383 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870384 | 4321::2 | 1046870384 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870385 | 4321::2 | 1046870385 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870386 | 4321::2 | 1046870386 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870387 | 4321::3 | 1046870387 | null | 1  | 0  | 64 | 0  | 00:00:13 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870388 | 4321::3 | 1046870388 | null | 1  | 0  | 64 | 0  | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870389 | 4321::3 | 1046870389 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870390 | 4321::3 | 1046870390 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870391 | 4321::3 | 1046870391 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870392 | 4321::3 | 1046870392 | null | 1  | 1  | 64 | 64 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870393 | 4321::3 | 1046870393 | null | 1  | 1  | 64 | 64 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870394 | 4321::3 | 1046870394 | null | 1  | 1  | 64 | 64 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870395 | 4321::3 | 1046870395 | null | 1  | 1  | 64 | 64 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1046870396 | 4321::3 | 1046870396 | null | 1  | 1  | 64 | 64 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
 |_____|_____|_____|_________|____________|_________|____________|______|____|____|____|____|__________|________________|________________|
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
 | 2.2.2.1 | 15 | 15 | 960  | 960  | 00:00:14 |
 | 2.2.2.2 | 5  | 5  | 320  | 320  | 00:00:14 |
 | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:14 |
 | 4321::1 | 20 | 18 | 1280 | 1152 | 00:00:14 |
 | 4321::2 | 5  | 5  | 320  | 320  | 00:00:14 |
 | 4321::3 | 15 | 13 | 960  | 832  | 00:00:13 |
 |_________|____|____|______|______|__________|
r2#
r2#
```

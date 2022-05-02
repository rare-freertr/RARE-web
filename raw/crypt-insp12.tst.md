# Example: mpls inspection with selective ingress drop

## **Topology diagram**

![topology](/img/crypt-insp12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz30r1-log.run
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
logging file debug ../binTmp/zzz30r2-log.run
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
 mpls inspect mac drop-rx allow-list test
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
logging file debug ../binTmp/zzz30r3-log.run
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
 | tx  | 1   | 0   | 2.2.2.3 | 527891671  | 2.2.2.1 | 527891671  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 527891672  | 2.2.2.1 | 527891672  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 527891673  | 2.2.2.1 | 527891673  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 527891674  | 2.2.2.1 | 527891674  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.3 | 527891675  | 2.2.2.1 | 527891675  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890237  | 2.2.2.1 | 770890237  | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890238  | 2.2.2.1 | 770890238  | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890239  | 2.2.2.1 | 770890239  | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890240  | 2.2.2.1 | 770890240  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890241  | 2.2.2.1 | 770890241  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890242  | 2.2.2.1 | 770890242  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890243  | 2.2.2.1 | 770890243  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 1   | 0   | 2.2.2.2 | 770890244  | 2.2.2.1 | 770890244  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 1   | 0   | 2.2.2.1 | 1066486980 | 2.2.2.3 | 1066486980 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 1066486981 | 2.2.2.3 | 1066486981 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 1066486982 | 2.2.2.3 | 1066486982 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 1066486983 | 2.2.2.3 | 1066486983 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 1066486984 | 2.2.2.3 | 1066486984 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 58  | 0   | 4321::3 | 192947766  | 4321::1 | 192947766  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 192947767  | 4321::1 | 192947767  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 192947768  | 4321::1 | 192947768  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 192947769  | 4321::1 | 192947769  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::3 | 192947770  | 4321::1 | 192947770  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 949063134  | 4321::1 | 949063134  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 949063135  | 4321::1 | 949063135  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 949063136  | 4321::1 | 949063136  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 949063137  | 4321::1 | 949063137  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | tx  | 58  | 0   | 4321::2 | 949063138  | 4321::1 | 949063138  | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
 | rx  | 58  | 0   | 4321::1 | 1008620157 | 4321::3 | 1008620157 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1008620158 | 4321::3 | 1008620158 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1008620159 | 4321::3 | 1008620159 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1008620160 | 4321::3 | 1008620160 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 1008620161 | 4321::3 | 1008620161 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
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
 | 2.2.2.1 | 18 | 18 | 1152 | 1152 | 00:00:13 |
 | 2.2.2.2 | 8  | 8  | 512  | 512  | 00:00:13 |
 | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:01 |
 | 4321::1 | 15 | 15 | 960  | 960  | 00:00:12 |
 | 4321::2 | 5  | 5  | 320  | 320  | 00:00:12 |
 | 4321::3 | 10 | 10 | 640  | 640  | 00:00:00 |
 |_________|____|____|______|______|__________|
r2#
r2#
```

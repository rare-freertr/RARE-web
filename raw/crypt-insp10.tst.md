# Example: interface inspection with selective ingress drop

## **Topology diagram**

![topology](/img/crypt-insp10.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz52r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 host-static 1234:1::2 0000.0000.2222
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
logging file debug ../binTmp/zzz52r2-log.run
!
access-list test4
 sequence 10 permit all any all 2.2.2.3 255.255.255.255 all
 exit
!
access-list test6
 sequence 10 permit all any all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv4 inspect mac drop-rx allow-list test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 inspect mac drop-rx allow-list test6
 ipv6 host-static 1234:1::1 0000.0000.1111
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
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
logging file debug ../binTmp/zzz52r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv6 address 1234:2::3 ffff:ffff::
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
r2#show ipv4 insp eth1
r2#show ipv4 insp eth1
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source              | target              |      | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|----------------|----------------|
 | tx  | 1   | 0   | 2.2.2.3 | 885319090 | 2.2.2.1 | 885319090 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 885319091 | 2.2.2.1 | 885319091 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 885319092 | 2.2.2.1 | 885319092 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 885319093 | 2.2.2.1 | 885319093 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 885319094 | 2.2.2.1 | 885319094 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775265 | 2.2.2.1 | 901775265 | null | 0  | 1  | 0  | 64 | 00:00:15 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775266 | 2.2.2.1 | 901775266 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775267 | 2.2.2.1 | 901775267 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775268 | 2.2.2.1 | 901775268 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775269 | 2.2.2.1 | 901775269 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775270 | 2.2.2.1 | 901775270 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775271 | 2.2.2.1 | 901775271 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775272 | 2.2.2.1 | 901775272 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775273 | 2.2.2.1 | 901775273 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 901775274 | 2.2.2.1 | 901775274 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | rx  | 1   | 0   | 2.2.2.1 | 968685102 | 2.2.2.3 | 968685102 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 968685103 | 2.2.2.3 | 968685103 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 968685104 | 2.2.2.3 | 968685104 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 968685105 | 2.2.2.3 | 968685105 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 1   | 0   | 2.2.2.1 | 968685106 | 2.2.2.3 | 968685106 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 insp eth1
r2#show ipv6 insp eth1
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source               | target               |      | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port       | addr    | port       | url  | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|------------|---------|------------|------|----|----|----|----|----------|----------------|----------------|
 | tx  | 58  | 0   | 4321::3 | 431895889  | 4321::1 | 431895889  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 431895890  | 4321::1 | 431895890  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 431895891  | 4321::1 | 431895891  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 431895892  | 4321::1 | 431895892  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 431895893  | 4321::1 | 431895893  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | rx  | 58  | 0   | 4321::1 | 995828327  | 4321::3 | 995828327  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 995828328  | 4321::3 | 995828328  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 995828329  | 4321::3 | 995828329  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 995828330  | 4321::3 | 995828330  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | rx  | 58  | 0   | 4321::1 | 995828331  | 4321::3 | 995828331  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
 | tx  | 58  | 0   | 4321::2 | 1031445578 | 4321::1 | 1031445578 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 1031445579 | 4321::1 | 1031445579 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 1031445580 | 4321::1 | 1031445580 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 1031445581 | 4321::1 | 1031445581 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 1031445582 | 4321::1 | 1031445582 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
 |_____|_____|_____|_________|____________|_________|____________|______|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 top eth1
r2#show ipv4 top eth1
 |~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
 |         | packet  | byte        |          |
 | addr    | rx | tx | rx   | tx   | time     |
 |---------|----|----|------|------|----------|
 | 2.2.2.1 | 19 | 20 | 1216 | 1280 | 00:00:15 |
 | 2.2.2.2 | 9  | 10 | 576  | 640  | 00:00:15 |
 | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:00 |
 |_________|____|____|______|______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 top eth1
r2#show ipv6 top eth1
 |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
 |         | packet  | byte      |          |
 | addr    | rx | tx | rx  | tx  | time     |
 |---------|----|----|-----|-----|----------|
 | 4321::1 | 15 | 15 | 960 | 960 | 00:00:13 |
 | 4321::2 | 5  | 5  | 320 | 320 | 00:00:13 |
 | 4321::3 | 10 | 10 | 640 | 640 | 00:00:00 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

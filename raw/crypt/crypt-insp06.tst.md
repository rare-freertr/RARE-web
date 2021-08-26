# Example: interface inspection with ingress drop

## **Topology diagram**

![topology](/img/crypt-insp06.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz44r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
logging file debug ../binTmp/zzz44r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 ipv4 inspect mac drop-rx
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 inspect mac drop-rx
 ipv6 host-static 1234:1::1 0000.0000.1111
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
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
logging file debug ../binTmp/zzz44r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source              | target              | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
 | tx  | 1   | 0   | 2.2.2.2 | 511577405 | 2.2.2.1 | 511577405 | 0  | 1  | 0  | 44 | 00:00:25 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577406 | 2.2.2.1 | 511577406 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577407 | 2.2.2.1 | 511577407 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577408 | 2.2.2.1 | 511577408 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577409 | 2.2.2.1 | 511577409 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577410 | 2.2.2.1 | 511577410 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577411 | 2.2.2.1 | 511577411 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577412 | 2.2.2.1 | 511577412 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577413 | 2.2.2.1 | 511577413 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.2 | 511577414 | 2.2.2.1 | 511577414 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 1   | 0   | 2.2.2.3 | 811298428 | 2.2.2.1 | 811298428 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 811298429 | 2.2.2.1 | 811298429 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 811298430 | 2.2.2.1 | 811298430 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 811298431 | 2.2.2.1 | 811298431 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 1   | 0   | 2.2.2.3 | 811298432 | 2.2.2.1 | 811298432 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 insp eth1
r2#show ipv6 insp eth1
 |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
 |                 | source              | target              | packet  | byte    |          | mac                             |
 | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
 |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
 | tx  | 58  | 0   | 4321::3 | 977029869 | 4321::1 | 977029869 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 977029870 | 4321::1 | 977029870 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 977029871 | 4321::1 | 977029871 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 977029872 | 4321::1 | 977029872 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::3 | 977029873 | 4321::1 | 977029873 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
 | tx  | 58  | 0   | 4321::2 | 983101881 | 4321::1 | 983101881 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 983101882 | 4321::1 | 983101882 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 983101883 | 4321::1 | 983101883 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 983101884 | 4321::1 | 983101884 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 | tx  | 58  | 0   | 4321::2 | 983101885 | 4321::1 | 983101885 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
 |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 top eth1
r2#show ipv4 top eth1
 |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
 |         | packet  | byte      |          |
 | addr    | rx | tx | rx  | tx  | time     |
 |---------|----|----|-----|-----|----------|
 | 2.2.2.1 | 14 | 15 | 616 | 660 | 00:00:25 |
 | 2.2.2.2 | 9  | 10 | 396 | 440 | 00:00:25 |
 | 2.2.2.3 | 5  | 5  | 220 | 220 | 00:00:00 |
 |_________|____|____|_____|_____|__________|
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
 | 4321::1 | 10 | 10 | 240 | 240 | 00:00:23 |
 | 4321::2 | 5  | 5  | 120 | 120 | 00:00:23 |
 | 4321::3 | 5  | 5  | 120 | 120 | 00:00:00 |
 |_________|____|____|_____|_____|__________|
r2#
r2#
```

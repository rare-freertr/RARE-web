# Example: route inspection

## **Topology diagram**

![topology](/img/crypt-insp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz25r1-log.run
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
logging file debug ../binTmp/zzz25r2-log.run
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
 ipv6 address 1234:1::2 ffff:ffff::
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
logging file debug ../binTmp/zzz25r3-log.run
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
r2#show ipv4 counter v1
r2#show ipv4 counter v1
 |~~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
 |            | transmit    | receive     |          |
 | prefix     | pack | byte | pack | byte | time     |
 |------------|------|------|------|------|----------|
 | 1.1.1.0/24 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1.1.1.2/32 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1.1.2.0/24 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1.1.2.2/32 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 2.2.2.1/32 | 28   | 1792 | 0    | 0    | 00:00:06 |
 | 2.2.2.2/32 | 24   | 1536 | 0    | 0    | 00:00:06 |
 | 2.2.2.3/32 | 25   | 1600 | 0    | 0    | 00:00:06 |
 |____________|______|______|______|______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 counter v1
r2#show ipv6 counter v1
 |~~~~~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
 |               | transmit    | receive     |          |
 | prefix        | pack | byte | pack | byte | time     |
 |---------------|------|------|------|------|----------|
 | 1234:1::/32   | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1234:1::2/128 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1234:2::/32   | 0    | 0    | 0    | 0    | 00:00:06 |
 | 1234:2::2/128 | 0    | 0    | 0    | 0    | 00:00:06 |
 | 4321::1/128   | 20   | 1280 | 0    | 0    | 00:00:06 |
 | 4321::2/128   | 20   | 1280 | 0    | 0    | 00:00:06 |
 | 4321::3/128   | 20   | 1280 | 0    | 0    | 00:00:06 |
 |_______________|______|______|______|______|__________|
r2#
r2#
```

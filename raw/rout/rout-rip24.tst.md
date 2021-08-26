# Example: rip auto mesh tunnel

## **Topology diagram**

![topology](/img/rout-rip24.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz28r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
prefix-list all
 sequence 10 permit 0.0.0.0/0 ge 0 le 32
 sequence 20 permit ::/0 ge 0 le 128
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
router rip4 1
 vrf v1
 redistribute connected
 automesh all
 exit
!
router rip6 1
 vrf v1
 redistribute connected
 automesh all
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
interface serial1
 no description
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 9999::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router rip4 1 enable
 router rip6 1 enable
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
logging file debug ../binTmp/zzz28r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
prefix-list all
 sequence 10 permit 0.0.0.0/0 ge 0 le 32
 sequence 20 permit ::/0 ge 0 le 128
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
router rip4 1
 vrf v1
 redistribute connected
 automesh all
 exit
!
router rip6 1
 vrf v1
 redistribute connected
 automesh all
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
interface serial1
 no description
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 9999::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls rsvp4
 mpls rsvp6
 router rip4 1 enable
 router rip6 1 enable
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
r2#show ipv4 rip 1 sum
r2#show ipv4 rip 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor | uptime   |
 |-----------|-------|----------|----------|
 | serial1   | 2     | 9.9.9.1  | 00:00:03 |
 |___________|_______|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 rip 1 sum
r2#show ipv6 rip 1 sum
 |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | learn | neighbor | uptime   |
 |-----------|-------|----------|----------|
 | serial1   | 2     | 9999::1  | 00:00:03 |
 |___________|_______|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 rip 1 dat
r2#show ipv4 rip 1 dat
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface   | hop     | time     |
 |-----|------------|--------|---------|---------|----------|
 | R   | 2.2.2.1/32 | 120/1  | serial1 | 9.9.9.1 | 00:00:03 |
 | R   | 9.9.9.0/24 | 1/0    | serial1 | null    | 00:00:03 |
 |_____|____________|________|_________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 rip 1 dat
r2#show ipv6 rip 1 dat
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface   | hop     | time     |
 |-----|-------------|--------|---------|---------|----------|
 | R   | 4321::1/128 | 120/1  | serial1 | 9999::1 | 00:00:03 |
 | R   | 9999::/16   | 1/0    | serial1 | null    | 00:00:03 |
 |_____|_____________|________|_________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | R   | 2.2.2.1/32 | 120/1  | serial1   | 9.9.9.1 | 00:00:03 |
 | C   | 2.2.2.2/32 | 0/0    | loopback0 | null    | 00:00:33 |
 | C   | 9.9.9.0/24 | 0/0    | serial1   | null    | 00:00:33 |
 | MSH | 9.9.9.1/32 | 0/3    | serial1   | 9.9.9.1 | never    |
 | LOC | 9.9.9.2/32 | 0/1    | serial1   | null    | 00:00:33 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | R   | 4321::1/128 | 120/1  | serial1   | 9999::1 | 00:00:04 |
 | C   | 4321::2/128 | 0/0    | loopback0 | null    | 00:00:34 |
 | C   | 9999::/16   | 0/0    | serial1   | null    | 00:00:33 |
 | MSH | 9999::1/128 | 0/3    | serial1   | 9999::1 | never    |
 | LOC | 9999::2/128 | 0/1    | serial1   | null    | 00:00:33 |
 |_____|_____________|________|___________|_________|__________|
r2#
r2#
```

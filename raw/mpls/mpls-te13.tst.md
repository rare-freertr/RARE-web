# Example: p2mp te

## **Topology diagram**

![topology](/img/mpls-te13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz84r1-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.11.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 9.9.9.9
 tunnel domain-name 2.2.2.2 2.2.2.3
 tunnel mode p2mpte
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 9999::9
 tunnel domain-name 4321::2 4321::3
 tunnel mode p2mpte
 vrf forwarding v1
 ipv6 address 3333::1 ffff:ffff::
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.11.2
!
ipv6 route v1 :: :: 1234:1::2
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
logging file debug ../binTmp/zzz84r2-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.12.1 255.255.255.0
 ipv6 address 1234:2::1 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.1
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 4321::1
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 3333::2 ffff:ffff::
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.12.2
!
ipv6 route v1 :: :: 1234:2::2
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
logging file debug ../binTmp/zzz84r3-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.13.1 255.255.255.0
 ipv6 address 1234:3::1 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.1
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 4321::1
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 3333::3 ffff:ffff::
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.13.2
!
ipv6 route v1 :: :: 1234:3::2
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz84r4-log.run
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
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.11.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.12.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 no description
 vrf forwarding v1
 ipv4 address 1.1.13.2 255.255.255.0
 ipv6 address 1234:3::2 ffff:ffff::
 mpls enable
 mpls rsvp4
 mpls rsvp6
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.11.1
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.12.1
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.13.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
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
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|
 | label  | vrf      | iface     | hop       | label      | targets | bytes   |
 |--------|----------|-----------|-----------|------------|---------|---------|
 | 48496  | v1:4     | null      | null      | unlabelled | local   | 997888  |
 | 68100  | tester:6 | null      | null      | unlabelled | local   | 0       |
 | 218833 | v1:6     | ethernet1 | 1234:1::2 | unlabelled |         | 0       |
 | 417721 | v1:4     | ethernet1 | 1.1.11.2  | unlabelled |         | 0       |
 | 478945 | v1:6     | null      | null      | unlabelled | local   | 356928  |
 | 524659 | v1:6     | null      | null      | unlabelled | local   | 520576  |
 | 642021 | tester:4 | null      | null      | unlabelled | local   | 0       |
 | 730961 | v1:6     | null      | null      | unlabelled | local   | 0       |
 | 752111 | v1:4     | null      | null      | unlabelled | local   | 1905984 |
 | 923869 | v1:4     | null      | null      | unlabelled | local   | 0       |
 |________|__________|___________|___________|____________|_________|_________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 rsvp v1 sum
r1#show ipv4 rsvp v1 sum
 |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id    | subgroup | id | target  | id         | description |
 |---------|-------|----------|----|---------|------------|-------------|
 | 2.2.2.1 | 2129  | 2.2.2.2  | 1  | 2.2.2.2 | 139526144  | r1:tunnel1  |
 | 2.2.2.1 | 2129  | 2.2.2.3  | 2  | 2.2.2.3 | 139526145  | r1:tunnel1  |
 | 2.2.2.3 | 14740 | ::       | 0  | 2.2.2.1 | 1087812664 | r3:tunnel1  |
 | 2.2.2.2 | 15902 | ::       | 0  | 2.2.2.1 | 997355463  | r2:tunnel1  |
 |_________|_______|__________|____|_________|____________|_____________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 rsvp v1 sum
r1#show ipv6 rsvp v1 sum
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id   | subgroup | id | target  | id         | description |
 |---------|------|----------|----|---------|------------|-------------|
 | 4321::2 | 1027 | ::       | 0  | 4321::1 | 331351560  | r2:tunnel2  |
 | 4321::3 | 5986 | ::       | 0  | 4321::1 | 1657242613 | r3:tunnel2  |
 | 4321::1 | 9538 | 4321::2  | 1  | 4321::2 | 625082368  | r1:tunnel2  |
 | 4321::1 | 9538 | 4321::3  | 2  | 4321::3 | 625082369  | r1:tunnel2  |
 |_________|______|__________|____|_________|____________|_____________|
r1#
r1#
```

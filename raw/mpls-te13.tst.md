# Example: p2mp te

## **Topology diagram**

![topology](/img/mpls-te13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz74r1-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz74r2-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz74r3-log.run
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
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz74r4-log.run
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
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 mpls rsvp4
 mpls rsvp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|
 | label   | vrf      | iface     | hop       | label      | targets | bytes   |
 |---------|----------|-----------|-----------|------------|---------|---------|
 | 103693  | v1:4     | ethernet1 | 1.1.11.2  | unlabelled |         | 0       |
 | 294113  | tester:6 | null      | null      | unlabelled | local   | 0       |
 | 449032  | tester:6 | null      | null      | unlabelled | local   | 0       |
 | 461052  | v1:6     | null      | null      | unlabelled | local   | 0       |
 | 500816  | v1:4     | null      | null      | unlabelled | local   | 0       |
 | 503381  | tester:4 | null      | null      | unlabelled | local   | 0       |
 | 657338  | tester:6 | null      | null      | unlabelled | local   | 0       |
 | 689606  | v1:4     | null      | null      | unlabelled | local   | 3100800 |
 | 693956  | v1:6     | ethernet1 | 1234:1::2 | unlabelled |         | 0       |
 | 752071  | tester:4 | null      | null      | unlabelled | local   | 0       |
 | 795960  | v1:6     | null      | null      | unlabelled | local   | 1186560 |
 | 864424  | tester:4 | null      | null      | unlabelled | local   | 0       |
 | 912405  | v1:6     | null      | null      | unlabelled | local   | 433088  |
 | 1030998 | v1:4     | null      | null      | unlabelled | local   | 1133888 |
 |_________|__________|___________|___________|____________|_________|_________|
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
 | 2.2.2.2 | 1937  | ::       | 0  | 2.2.2.1 | 1081711413 | r2:tunnel1  |
 | 2.2.2.3 | 16883 | ::       | 0  | 2.2.2.1 | 897628895  | r3:tunnel1  |
 | 2.2.2.1 | 18988 | 2.2.2.2  | 1  | 2.2.2.2 | 1244397568 | r1:tunnel1  |
 | 2.2.2.1 | 18988 | 2.2.2.3  | 2  | 2.2.2.3 | 1244397569 | r1:tunnel1  |
 |_________|_______|__________|____|_________|____________|_____________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 rsvp v1 sum
r1#show ipv6 rsvp v1 sum
 |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id    | subgroup | id | target  | id         | description |
 |---------|-------|----------|----|---------|------------|-------------|
 | 4321::2 | 1320  | ::       | 0  | 4321::1 | 1677074988 | r2:tunnel2  |
 | 4321::1 | 8021  | 4321::2  | 1  | 4321::2 | 525664256  | r1:tunnel2  |
 | 4321::1 | 8021  | 4321::3  | 2  | 4321::3 | 525664257  | r1:tunnel2  |
 | 4321::3 | 12230 | ::       | 0  | 4321::1 | 2120620476 | r3:tunnel2  |
 |_________|_______|__________|____|_________|____________|_____________|
r1#
r1#
```

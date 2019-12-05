# Example: p2mp te

## **Topology diagram**

![topology](/img/mpls-te13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
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
!
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
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
!
end
```

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
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
!
end
```

## **Verification**

```
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | label   | vrf  | iface     | hop       | label      | targets | bytes    |
 |---------|------|-----------|-----------|------------|---------|----------|
 | 9287    | v1:6 | null      | null      | unlabelled | local   | 5273072  |
 | 20524   | v1:6 | null      | null      | unlabelled | local   | 9700992  |
 | 118639  | v1:4 | null      | null      | unlabelled | local   | 31351760 |
 | 280075  | v1:6 | ethernet1 | 1234:1::2 | unlabelled |         | 0        |
 | 712480  | v1:4 | null      | null      | unlabelled | local   | 8201708  |
 | 891108  | v1:4 | null      | null      | unlabelled | local   | 0        |
 | 927599  | v1:4 | ethernet1 | 1.1.11.2  | unlabelled |         | 0        |
 | 1022966 | v1:6 | null      | null      | unlabelled | local   | 0        |
 |_________|______|___________|___________|____________|_________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 rsvp v1 sum
r1#show ipv4 rsvp v1 sum
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id   | subgroup | id | target  | id         | description |
 |---------|------|----------|----|---------|------------|-------------|
 | 2.2.2.2 | 1304 | ::       | 0  | 2.2.2.1 | 2094194309 | r2:tunnel1  |
 | 2.2.2.1 | 8194 | 2.2.2.2  | 1  | 2.2.2.2 | 537001984  | r1:tunnel1  |
 | 2.2.2.1 | 8194 | 2.2.2.3  | 2  | 2.2.2.3 | 537001985  | r1:tunnel1  |
 | 2.2.2.3 | 8241 | ::       | 0  | 2.2.2.1 | 177718089  | r3:tunnel1  |
 |_________|______|__________|____|_________|____________|_____________|
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
 | 4321::2 | 5121  | ::       | 0  | 4321::1 | 1039196388 | r2:tunnel2  |
 | 4321::3 | 8122  | ::       | 0  | 4321::1 | 147602438  | r3:tunnel2  |
 | 4321::1 | 31003 | 4321::2  | 1  | 4321::2 | 2031812608 | r1:tunnel2  |
 | 4321::1 | 31003 | 4321::3  | 2  | 4321::3 | 2031812609 | r1:tunnel2  |
 |_________|_______|__________|____|_________|____________|_____________|
r1#
r1#
```

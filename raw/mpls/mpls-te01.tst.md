# Example: te over ethernet

## **Topology diagram**

![topology](/img/mpls-te01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz94r1-log.run
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
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 ipv6 access-group-in test6
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
 tunnel source ethernet1
 tunnel destination 1.1.1.2
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1234::2
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 4321::1 ffff::
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
logging file debug ../binTmp/zzz94r2-log.run
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
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 ipv6 access-group-in test6
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
 tunnel source ethernet1
 tunnel destination 1.1.1.1
 tunnel mode p2pte
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1234::1
 tunnel mode p2pte
 vrf forwarding v1
 ipv6 address 4321::2 ffff::
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
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf      | iface | hop  | label      | targets | bytes |
 |---------|----------|-------|------|------------|---------|-------|
 | 115749  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 185155  | v1:4     | null  | null | unlabelled | local   | 0     |
 | 238364  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 409987  | v1:6     | null  | null | unlabelled | local   | 640   |
 | 881952  | v1:4     | null  | null | unlabelled | local   | 640   |
 | 1011223 | v1:6     | null  | null | unlabelled | local   | 0     |
 |_________|__________|_______|______|____________|_________|_______|
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
 | 1.1.1.2 | 18395 | ::       | 0  | 1.1.1.1 | 1836463951 | r2:tunnel1  |
 | 1.1.1.1 | 22590 | ::       | 0  | 1.1.1.2 | 434691076  | r1:tunnel1  |
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
 | 1234::1 | 9438  | ::       | 0  | 1234::2 | 151091380  | r1:tunnel2  |
 | 1234::2 | 28516 | ::       | 0  | 1234::1 | 1761234810 | r2:tunnel2  |
 |_________|_______|__________|____|_________|____________|_____________|
r1#
r1#
```

# Example: bidir te with global id

## **Topology diagram**

![topology](/img/mpls-te18.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz1r1-log.run
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
 tunnel association 4.3.2.1 1234 12345678
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
 tunnel association 4444::5555 1234 12345678
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
logging file debug ../binTmp/zzz1r2-log.run
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
 tunnel association 4.3.2.1 1234 12345678
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
 tunnel association 4444::5555 1234 12345678
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
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface | hop  | label      | targets | bytes |
 |--------|----------|-------|------|------------|---------|-------|
 | 305292 | v1:6     | null  | null | unlabelled | local   | 640   |
 | 398192 | v1:6     | null  | null | unlabelled | local   | 0     |
 | 670509 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 804966 | tester:4 | null  | null | unlabelled | local   | 0     |
 | 841928 | v1:4     | null  | null | unlabelled | local   | 640   |
 | 852004 | v1:4     | null  | null | unlabelled | local   | 0     |
 |________|__________|_______|______|____________|_________|_______|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 rsvp v1 sum
r1#show ipv4 rsvp v1 sum
 |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id    | subgroup | id | target  | id        | description |
 |---------|-------|----------|----|---------|-----------|-------------|
 | 1.1.1.2 | 17900 | ::       | 0  | 1.1.1.1 | 346810235 | r2:tunnel1  |
 | 1.1.1.1 | 25786 | ::       | 0  | 1.1.1.2 | 314114021 | r1:tunnel1  |
 |_________|_______|__________|____|_________|___________|_____________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 rsvp v1 sum
r1#show ipv6 rsvp v1 sum
 |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~|
 | source  | id    | subgroup | id | target  | id        | description |
 |---------|-------|----------|----|---------|-----------|-------------|
 | 1234::2 | 16245 | ::       | 0  | 1234::1 | 935736866 | r2:tunnel2  |
 | 1234::1 | 19333 | ::       | 0  | 1234::2 | 611699162 | r1:tunnel2  |
 |_________|_______|__________|____|_________|___________|_____________|
r1#
r1#
```

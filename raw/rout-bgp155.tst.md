# Example: bgp auto mesh tunnel

## **Topology diagram**

![topology](/img/rout-bgp155.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 9.9.9.2 remote-as 2
 no neighbor 9.9.9.2 description
 neighbor 9.9.9.2 local-as 1
 neighbor 9.9.9.2 address-family unicast
 neighbor 9.9.9.2 distance 20
 redistribute connected
 automesh all
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 9999::2 remote-as 2
 no neighbor 9999::2 description
 neighbor 9999::2 local-as 1
 neighbor 9999::2 address-family unicast
 neighbor 9999::2 distance 20
 redistribute connected
 automesh all
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
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
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast
 neighbor 9.9.9.1 remote-as 1
 no neighbor 9.9.9.1 description
 neighbor 9.9.9.1 local-as 2
 neighbor 9.9.9.1 address-family unicast
 neighbor 9.9.9.1 distance 20
 redistribute connected
 automesh all
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast
 neighbor 9999::1 remote-as 1
 no neighbor 9999::1 description
 neighbor 9999::1 local-as 2
 neighbor 9999::1 address-family unicast
 neighbor 9999::1 distance 20
 redistribute connected
 automesh all
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
end
```

## **Verification**

```
r1#
r1#
r1#show ipv4 bgp 1 sum
r1#show ipv4 bgp 1 sum
 |~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~|
 | as | afis | ready | neighbor | uptime |
 |----|------|-------|----------|--------|
 | 2  |      | false | 9.9.9.2  | never  |
 |____|______|_______|__________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 sum
r1#show ipv6 bgp 1 sum
 |~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~|
 | as | afis | ready | neighbor | uptime |
 |----|------|-------|----------|--------|
 | 2  |      | false | 9999::2  | never  |
 |____|______|_______|__________|________|
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
 | 9.9.9.1 | 10588 | ::       | 0  | 9.9.9.2 | 2001055419 | r1:automesh |
 | 9.9.9.2 | 23434 | ::       | 0  | 9.9.9.1 | 445864299  | r2:automesh |
 |_________|_______|__________|____|_________|____________|_____________|
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
 | 9999::1 | 13813 | ::       | 0  | 9999::2 | 599451811 | r1:automesh |
 | 9999::2 | 21524 | ::       | 0  | 9999::1 | 416832092 | r2:automesh |
 |_________|_______|__________|____|_________|___________|_____________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 route v1
r1#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:03 |
 | C   | 9.9.9.0/24 | 0/0    | serial1   | null    | 00:00:03 |
 | LOC | 9.9.9.1/32 | 0/1    | serial1   | null    | 00:00:03 |
 | MSH | 9.9.9.2/32 | 0/3    | serial1   | 9.9.9.2 | never    |
 |_____|____________|________|___________|_________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 route v1
r1#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | C   | 4321::1/128 | 0/0    | loopback0 | null    | 00:00:00 |
 | B   | 4321::2/128 | 20/0   | serial1   | 9999::2 | 00:00:00 |
 | C   | 9999::/16   | 0/0    | serial1   | null    | 00:00:00 |
 | LOC | 9999::1/128 | 0/1    | serial1   | null    | 00:00:00 |
 | MSH | 9999::2/128 | 0/3    | serial1   | 9999::2 | never    |
 |_____|_____________|________|___________|_________|__________|
r1#
r1#
```

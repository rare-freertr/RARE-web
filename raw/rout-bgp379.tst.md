# Example: evpn/vpws over ebgp

## **Topology diagram**

![topology](/img/rout-bgp379.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 rd 1:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 1:3
 rt-import 1:3
 rt-export 1:3
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 mac-learn
 private-bridge
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
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv6 address 4444::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 no description
 vrf forwarding v1
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 no description
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family evpn
 neighbor 2.2.2.2 remote-as 2
 no neighbor 2.2.2.2 description
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family evpn
 neighbor 2.2.2.2 distance 20
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 pmsitun
 neighbor 2.2.2.2 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 004e.7c76.5418
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 006d.5e48.573c
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family evpn
 neighbor 4321::2 remote-as 2
 no neighbor 4321::2 description
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family evpn
 neighbor 4321::2 distance 20
 neighbor 4321::2 update-source loopback0
 neighbor 4321::2 pmsitun
 neighbor 4321::2 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0041.7312.6b52
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 0020.0d2e.330b
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
!
!
!
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
bridge 1
 rd 2:1
 rt-import 1:1
 rt-export 1:1
 mac-learn
 private-bridge
 exit
!
bridge 2
 rd 2:2
 rt-import 1:2
 rt-export 1:2
 mac-learn
 private-bridge
 exit
!
bridge 3
 rd 2:3
 rt-import 1:3
 rt-export 1:3
 mac-learn
 private-bridge
 exit
!
bridge 4
 rd 2:4
 rt-import 1:4
 rt-export 1:4
 mac-learn
 private-bridge
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
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv6 address 4444::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 no description
 vrf forwarding v1
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 no description
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family evpn
 neighbor 2.2.2.1 remote-as 1
 no neighbor 2.2.2.1 description
 neighbor 2.2.2.1 local-as 2
 neighbor 2.2.2.1 address-family evpn
 neighbor 2.2.2.1 distance 20
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 pmsitun
 neighbor 2.2.2.1 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 0008.011e.1404
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0030.3169.2e7c
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family evpn
 neighbor 4321::1 remote-as 1
 no neighbor 4321::1 description
 neighbor 4321::1 local-as 2
 neighbor 4321::1 address-family evpn
 neighbor 4321::1 distance 20
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 pmsitun
 neighbor 4321::1 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 001b.3533.5504
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 007e.5a3b.5240
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
!
!
!
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
 |~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | afis | ready | neighbor | uptime   |
 |----|------|-------|----------|----------|
 | 2  | evpn | true  | 2.2.2.2  | 00:00:16 |
 |____|______|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 sum
r1#show ipv6 bgp 1 sum
 |~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | afis | ready | neighbor | uptime   |
 |----|------|-------|----------|----------|
 | 2  | evpn | true  | 4321::2  | 00:00:08 |
 |____|______|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 evpn dat
r1#show ipv4 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix         | hop     | metric     | aspath |
 |----------------|---------|------------|--------|
 | 100::65#:: 1:1 | 2.2.2.1 | 0/0/0/0    |        |
 | 100::66#:: 1:3 | 2.2.2.1 | 0/0/0/0    |        |
 | 100::65#:: 2:1 | 2.2.2.2 | 20/100/0/0 | 2      |
 | 100::66#:: 2:3 | 2.2.2.2 | 20/100/0/0 | 2      |
 |________________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 evpn dat
r1#show ipv6 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix         | hop     | metric     | aspath |
 |----------------|---------|------------|--------|
 | 100::65#:: 1:2 | 4321::1 | 0/0/0/0    |        |
 | 100::66#:: 1:4 | 4321::1 | 0/0/0/0    |        |
 | 100::65#:: 2:2 | 4321::2 | 20/100/0/0 | 2      |
 | 100::66#:: 2:4 | 4321::2 | 20/100/0/0 | 2      |
 |________________|_________|____________|________|
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:21 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:21 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:21 |
 | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:21 |
 | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:21 |
 | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:21 |
 | C   | 4.4.4.0/30 | 0/0    | bvi4      | null    | 00:00:21 |
 | LOC | 4.4.4.1/32 | 0/1    | bvi4      | null    | 00:00:21 |
 |_____|____________|________|___________|_________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 route v1
r1#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric | iface     | hop       | time     |
 |-----|---------------|--------|-----------|-----------|----------|
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:19 |
 | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:19 |
 | C   | 3333::/16     | 0/0    | bvi3      | null      | 00:00:19 |
 | LOC | 3333::1/128   | 0/1    | bvi3      | null      | 00:00:19 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:19 |
 | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:19 |
 | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:19 |
 | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:19 |
 |_____|_______________|________|___________|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 1
r1#show bridge 1
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | interface        | forward | physical | tx   | rx   | drop |
 |------------------|---------|----------|------|------|------|
 | bvi              | true    | true     | 0    | 0    | 0    |
 | evpn 2.2.2.2 101 | true    | false    | 1064 | 1064 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 0041.060a.233f | evpn 2.2.2.2 101 | 00:00:02 | 1034 | 1064 | 0    |
 | 0054.0662.6a47 | bvi              | 00:00:02 | 1064 | 1304 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 2
r1#show bridge 2
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | interface        | forward | physical | tx   | rx   | drop |
 |------------------|---------|----------|------|------|------|
 | bvi              | true    | true     | 0    | 0    | 0    |
 | evpn 4321::2 101 | true    | false    | 1744 | 1630 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 000e.6269.6d15 | bvi              | 00:00:01 | 1556 | 1998 | 0    |
 | 0020.1638.5411 | evpn 4321::2 101 | 00:00:01 | 1670 | 1630 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 3
r1#show bridge 3
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | interface        | forward | physical | tx   | rx   | drop |
 |------------------|---------|----------|------|------|------|
 | bvi              | true    | true     | 0    | 0    | 0    |
 | evpn 2.2.2.2 102 | true    | false    | 1744 | 1630 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 000b.120b.673d | evpn 2.2.2.2 102 | 00:00:03 | 1670 | 1630 | 0    |
 | 0079.6d40.0b50 | bvi              | 00:00:03 | 1556 | 1998 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 4
r1#show bridge 4
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~|~~~~~|~~~~~~|
 | interface        | forward | physical | tx  | rx  | drop |
 |------------------|---------|----------|-----|-----|------|
 | bvi              | true    | true     | 0   | 0   | 0    |
 | evpn 4321::2 102 | true    | false    | 970 | 970 | 0    |
 |__________________|_________|__________|_____|_____|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx  | rx   | drop |
 |----------------|------------------|----------|-----|------|------|
 | 0050.4a74.4d4a | bvi              | 00:00:02 | 970 | 1090 | 0    |
 | 0051.7071.7255 | evpn 4321::2 102 | 00:00:02 | 940 | 970  | 0    |
 |________________|__________________|__________|_____|______|______|
r1#
r1#
```

# Example: evpn/vxlan over ebgp

## **Topology diagram**

![topology](/img/rout-bgp189.tst.png)

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
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.252
 ipv6 address 4444::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
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
 afi-evpn 101 bmac 007e.2a6d.583b
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
 afi-evpn 101 bmac 003a.1559.5d38
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.252
 ipv6 address 4444::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
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
 afi-evpn 101 bmac 0028.531d.6744
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
 afi-evpn 101 bmac 0008.3508.7b4b
 afi-evpn 101 encapsulation vxlan
 afi-evpn 101 update-source loopback0
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
 | 2  | evpn | true  | 2.2.2.2  | 00:00:13 |
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
 | 2  | evpn | true  | 4321::2  | 00:00:17 |
 |____|______|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 evpn dat
r1#show ipv4 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                   | hop     | metric     | aspath |
 |--------------------------|---------|------------|--------|
 | 200::4:6367:40c#:: 1:1   | 2.2.2.2 | 20/100/0/0 | 2      |
 | 200::19:6658:345c#:: 1:1 | 2.2.2.1 | 0/0/0/0    |        |
 | 300::#2.2.2.2 1:1        | 2.2.2.2 | 20/100/0/0 | 2      |
 | 300::#2.2.2.1 1:1        | 2.2.2.1 | 0/0/0/0    |        |
 |__________________________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 evpn dat
r1#show ipv6 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                   | hop     | metric     | aspath |
 |--------------------------|---------|------------|--------|
 | 200::1c:d3e:3b10#:: 1:2  | 4321::1 | 0/0/0/0    |        |
 | 200::4d:3206:6e5e#:: 1:2 | 4321::2 | 20/100/0/0 | 2      |
 | 300::#4321::2 1:2        | 4321::2 | 20/100/0/0 | 2      |
 | 300::#4321::1 1:2        | 4321::1 | 0/0/0/0    |        |
 |__________________________|_________|____________|________|
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:29 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:29 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:29 |
 | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:29 |
 | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:29 |
 | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:29 |
 | C   | 4.4.4.0/30 | 0/0    | bvi2      | null    | 00:00:29 |
 | LOC | 4.4.4.1/32 | 0/1    | bvi2      | null    | 00:00:29 |
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:29 |
 | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:29 |
 | C   | 3333::/16     | 0/0    | bvi1      | null      | 00:00:29 |
 | LOC | 3333::1/128   | 0/1    | bvi1      | null      | 00:00:29 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:29 |
 | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:29 |
 | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:29 |
 | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:29 |
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
 | vxlan to 2.2.2.2 | true    | false    | 3090 | 3336 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 0004.6367.040c | vxlan to 2.2.2.2 | 00:00:02 | 2986 | 2976 | 0    |
 | 0019.6658.345c | bvi              | 00:00:02 | 2902 | 3644 | 0    |
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
 | vxlan to 4321::2 | true    | false    | 3090 | 3336 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 001c.0d3e.3b10 | bvi              | 00:00:02 | 2902 | 3344 | 0    |
 | 004d.3206.6e5e | vxlan to 4321::2 | 00:00:02 | 2986 | 2976 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

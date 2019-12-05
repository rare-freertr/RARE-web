# Example: evpn/cmac over ebgp

## **Topology diagram**

![topology](/img/rout-bgp203.tst.png)

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
 afi-evpn 101 bmac 0045.4934.6d56
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0014.6b3b.2056
 afi-evpn 102 encapsulation cmac
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
 afi-evpn 101 bmac 0000.6709.603d
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 001c.5238.370d
 afi-evpn 102 encapsulation cmac
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
 afi-evpn 101 bmac 0064.0173.6e55
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0021.5c4e.0377
 afi-evpn 102 encapsulation cmac
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
 afi-evpn 101 bmac 0045.713a.6e4d
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 005d.1573.5a4b
 afi-evpn 102 encapsulation cmac
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
 | 2  | evpn | true  | 2.2.2.2  | 00:00:15 |
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
 | 2  | evpn | true  | 4321::2  | 00:00:16 |
 |____|______|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 evpn dat
r1#show ipv4 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                        | hop     | metric     | aspath |
 |-------------------------------|---------|------------|--------|
 | 200:0:65::e:497e:3922#:: 1:1  | 2.2.2.2 | 20/100/0/0 | 2      |
 | 200:0:65::14:2b66:597a#:: 1:1 | 2.2.2.1 | 0/0/0/0    |        |
 | 300:0:65::#2.2.2.2 1:1        | 2.2.2.2 | 20/100/0/0 | 2      |
 | 300:0:65::#2.2.2.1 1:1        | 2.2.2.1 | 0/0/0/0    |        |
 | 200:0:66::44:6a76:203d#:: 1:3 | 2.2.2.2 | 20/100/0/0 | 2      |
 | 200:0:66::73:2c3e:941#:: 1:3  | 2.2.2.1 | 0/0/0/0    |        |
 | 300:0:66::#2.2.2.2 1:3        | 2.2.2.2 | 20/100/0/0 | 2      |
 | 300:0:66::#2.2.2.1 1:3        | 2.2.2.1 | 0/0/0/0    |        |
 |_______________________________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 evpn dat
r1#show ipv6 bgp 1 evpn dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                        | hop     | metric     | aspath |
 |-------------------------------|---------|------------|--------|
 | 200:0:65::58:1269:140f#:: 1:2 | 4321::2 | 20/100/0/0 | 2      |
 | 200:0:65::5d:562c:284d#:: 1:2 | 4321::1 | 0/0/0/0    |        |
 | 300:0:65::#4321::2 1:2        | 4321::2 | 20/100/0/0 | 2      |
 | 300:0:65::#4321::1 1:2        | 4321::1 | 0/0/0/0    |        |
 | 200:0:66::33:5e47:653a#:: 1:4 | 4321::2 | 20/100/0/0 | 2      |
 | 200:0:66::71:7a34:b15#:: 1:4  | 4321::1 | 0/0/0/0    |        |
 | 300:0:66::#4321::2 1:4        | 4321::2 | 20/100/0/0 | 2      |
 | 300:0:66::#4321::1 1:4        | 4321::1 | 0/0/0/0    |        |
 |_______________________________|_________|____________|________|
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:24 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:24 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:24 |
 | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:24 |
 | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:24 |
 | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:24 |
 | C   | 4.4.4.0/30 | 0/0    | bvi4      | null    | 00:00:24 |
 | LOC | 4.4.4.1/32 | 0/1    | bvi4      | null    | 00:00:24 |
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:22 |
 | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:22 |
 | C   | 3333::/16     | 0/0    | bvi3      | null      | 00:00:22 |
 | LOC | 3333::1/128   | 0/1    | bvi3      | null      | 00:00:22 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:22 |
 | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:22 |
 | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:22 |
 | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:22 |
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
 | evpn 2.2.2.2 101 | true    | false    | 1252 | 1252 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 000e.497e.3922 | evpn 2.2.2.2 101 | 00:00:02 | 1222 | 1252 | 0    |
 | 0014.2b66.597a | bvi              | 00:00:02 | 1252 | 1582 | 0    |
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
 | 0058.1269.140f | evpn 4321::2 101 | 00:00:01 | 1670 | 1630 | 0    |
 | 005d.562c.284d | bvi              | 00:00:01 | 1556 | 1998 | 0    |
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
 | 0044.6a76.203d | evpn 2.2.2.2 102 | 00:00:03 | 1670 | 1630 | 0    |
 | 0073.2c3e.0941 | bvi              | 00:00:03 | 1556 | 1998 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 4
r1#show bridge 4
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | interface        | forward | physical | tx   | rx   | drop |
 |------------------|---------|----------|------|------|------|
 | bvi              | true    | true     | 0    | 0    | 0    |
 | evpn 4321::2 102 | true    | false    | 1158 | 1158 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx   | rx   | drop |
 |----------------|------------------|----------|------|------|------|
 | 0033.5e47.653a | evpn 4321::2 102 | 00:00:02 | 1128 | 1158 | 0    |
 | 0071.7a34.0b15 | bvi              | 00:00:02 | 1158 | 1218 | 0    |
 |________________|__________________|__________|______|______|______|
r1#
r1#
```

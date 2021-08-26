# Example: evpn/cmac over ebgp

## **Topology diagram**

![topology](/img/rout-bgp203.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz55r1-log.run
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
 afi-evpn 101 bmac 003b.2749.0d2e
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0052.434c.104a
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
 afi-evpn 101 bmac 005e.5f06.4c56
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 0045.4074.2658
 afi-evpn 102 encapsulation cmac
 afi-evpn 102 update-source loopback0
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
logging file debug ../binTmp/zzz55r2-log.run
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
 afi-evpn 101 bmac 0059.466c.4540
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0058.6575.4e1d
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
 afi-evpn 101 bmac 003f.7756.0760
 afi-evpn 101 encapsulation cmac
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 0079.6166.1d6b
 afi-evpn 102 encapsulation cmac
 afi-evpn 102 update-source loopback0
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
r1#show ipv4 bgp 1 sum
r1#show ipv4 bgp 1 sum
 |~~~~|~~~~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | learn | sent | ready | neighbor | uptime   |
 |----|-------|------|-------|----------|----------|
 | 2  | 4     | 8    | true  | 2.2.2.2  | 00:00:16 |
 |____|_______|______|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 sum
r1#show ipv6 bgp 1 sum
 |~~~~|~~~~~~~|~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | learn | sent | ready | neighbor | uptime   |
 |----|-------|------|-------|----------|----------|
 | 2  | 4     | 8    | true  | 4321::2  | 00:00:16 |
 |____|_______|______|_______|__________|__________|
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
 | 200:0:65::d:5a0a:327a#:: 1:1  | 2.2.2.2 | 20/100/0/0 | 2      |
 | 200:0:65::38:7a49:726#:: 1:1  | 2.2.2.1 | 0/0/0/0    |        |
 | 300:0:65::#2.2.2.2 1:1        | 2.2.2.2 | 20/100/0/0 | 2      |
 | 300:0:65::#2.2.2.1 1:1        | 2.2.2.1 | 0/0/0/0    |        |
 | 200:0:66::25:6125:5d52#:: 1:3 | 2.2.2.1 | 0/0/0/0    |        |
 | 200:0:66::34:7244:174f#:: 1:3 | 2.2.2.2 | 20/100/0/0 | 2      |
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
 | 200:0:65::17:3838:3e49#:: 1:2 | 4321::1 | 0/0/0/0    |        |
 | 200:0:65::65:6505:373a#:: 1:2 | 4321::2 | 20/100/0/0 | 2      |
 | 300:0:65::#4321::2 1:2        | 4321::2 | 20/100/0/0 | 2      |
 | 300:0:65::#4321::1 1:2        | 4321::1 | 0/0/0/0    |        |
 | 200:0:66::55:6665:5e6c#:: 1:4 | 4321::2 | 20/100/0/0 | 2      |
 | 200:0:66::57:62d:4a#:: 1:4    | 4321::1 | 0/0/0/0    |        |
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:18 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:18 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:18 |
 | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:04 |
 | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:18 |
 | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:18 |
 | C   | 4.4.4.0/30 | 0/0    | bvi4      | null    | 00:00:18 |
 | LOC | 4.4.4.1/32 | 0/1    | bvi4      | null    | 00:00:18 |
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
 | C   | 3333::/16     | 0/0    | bvi3      | null      | 00:00:18 |
 | LOC | 3333::1/128   | 0/1    | bvi3      | null      | 00:00:18 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:19 |
 | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:10 |
 | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:18 |
 | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:18 |
 |_____|_______________|________|___________|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 1
r1#show bridge 1
 |~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|
 |                                 | packet         | byte             |     |
 | iface            | fwd  | phys  | tx | rx | drop | tx  | rx  | drop | grp |
 |------------------|------|-------|----|----|------|-----|-----|------|-----|
 | bvi              | true | true  | 0  | 0  | 0    | 0   | 0   | 0    |     |
 | evpn 2.2.2.2 101 | true | false | 12 | 12 | 0    | 756 | 756 | 0    |     |
 |__________________|______|_______|____|____|______|_____|_____|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                                              | packet         | byte             |
 | addr           | iface            | time     | tx | rx | drop | tx  | rx  | drop |
 |----------------|------------------|----------|----|----|------|-----|-----|------|
 | 000d.5a0a.327a | evpn 2.2.2.2 101 | 00:00:19 | 11 | 12 | 0    | 726 | 756 | 0    |
 | 0038.7a49.0726 | bvi              | 00:00:19 | 12 | 15 | 0    | 756 | 846 | 0    |
 |________________|__________________|__________|____|____|______|_____|_____|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 2
r1#show bridge 2
 |~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                                 | packet         | byte               |     |
 | iface            | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
 |------------------|------|-------|----|----|------|------|------|------|-----|
 | bvi              | true | true  | 0  | 0  | 0    | 0    | 0    | 0    |     |
 | evpn 4321::2 101 | true | false | 16 | 15 | 0    | 1072 | 1006 | 0    |     |
 |__________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
 |                                              | packet         | byte              |
 | addr           | iface            | time     | tx | rx | drop | tx  | rx   | drop |
 |----------------|------------------|----------|----|----|------|-----|------|------|
 | 0017.3838.3e49 | bvi              | 00:00:19 | 14 | 19 | 0    | 932 | 1326 | 0    |
 | 0065.6505.373a | evpn 4321::2 101 | 00:00:19 | 15 | 15 | 0    | 998 | 1006 | 0    |
 |________________|__________________|__________|____|____|______|_____|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 3
r1#show bridge 3
 |~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                                 | packet         | byte               |     |
 | iface            | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
 |------------------|------|-------|----|----|------|------|------|------|-----|
 | bvi              | true | true  | 0  | 0  | 0    | 0    | 0    | 0    |     |
 | evpn 2.2.2.2 102 | true | false | 16 | 15 | 0    | 1072 | 1006 | 0    |     |
 |__________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
 |                                              | packet         | byte              |
 | addr           | iface            | time     | tx | rx | drop | tx  | rx   | drop |
 |----------------|------------------|----------|----|----|------|-----|------|------|
 | 0025.6125.5d52 | bvi              | 00:00:19 | 14 | 19 | 0    | 932 | 1326 | 0    |
 | 0034.7244.174f | evpn 2.2.2.2 102 | 00:00:19 | 15 | 15 | 0    | 998 | 1006 | 0    |
 |________________|__________________|__________|____|____|______|_____|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show bridge 4
r1#show bridge 4
 |~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|
 |                                 | packet         | byte             |     |
 | iface            | fwd  | phys  | tx | rx | drop | tx  | rx  | drop | grp |
 |------------------|------|-------|----|----|------|-----|-----|------|-----|
 | bvi              | true | true  | 0  | 0  | 0    | 0   | 0   | 0    |     |
 | evpn 4321::2 102 | true | false | 3  | 0  | 0    | 90  | 0   | 0    |     |
 | evpn 4321::2 102 | true | false | 13 | 13 | 0    | 822 | 822 | 0    |     |
 |__________________|______|_______|____|____|______|_____|_____|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                                              | packet         | byte             |
 | addr           | iface            | time     | tx | rx | drop | tx  | rx  | drop |
 |----------------|------------------|----------|----|----|------|-----|-----|------|
 | 0055.6665.5e6c | evpn 4321::2 102 | 00:00:19 | 12 | 13 | 0    | 792 | 822 | 0    |
 | 0057.062d.004a | bvi              | 00:00:19 | 13 | 15 | 0    | 822 | 882 | 0    |
 |________________|__________________|__________|____|____|______|_____|_____|______|
r1#
r1#
```

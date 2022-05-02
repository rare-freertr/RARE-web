# Example: evpn/vpws over ebgp

## **Topology diagram**

![topology](/img/rout-bgp379.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz75r1-log.run
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
 label4mode per-prefix
 label6mode per-prefix
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv6 address 4444::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 vrf forwarding v1
 ipv4 address 4.4.4.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 no safe-ebgp
 address-family evpn
 neighbor 2.2.2.2 remote-as 2
 neighbor 2.2.2.2 local-as 1
 neighbor 2.2.2.2 address-family evpn
 neighbor 2.2.2.2 distance 20
 neighbor 2.2.2.2 update-source loopback0
 neighbor 2.2.2.2 pmsitun
 neighbor 2.2.2.2 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 004c.1e45.1a0f
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0066.1433.0f41
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 no safe-ebgp
 address-family evpn
 neighbor 4321::2 remote-as 2
 neighbor 4321::2 local-as 1
 neighbor 4321::2 address-family evpn
 neighbor 4321::2 distance 20
 neighbor 4321::2 update-source loopback0
 neighbor 4321::2 pmsitun
 neighbor 4321::2 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0008.2b47.3d3f
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 006d.581e.340a
 afi-evpn 102 encapsulation vpws
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
logging file debug ../binTmp/zzz75r2-log.run
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
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv6 address 4444::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi4
 vrf forwarding v1
 ipv4 address 4.4.4.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 no safe-ebgp
 address-family evpn
 neighbor 2.2.2.1 remote-as 1
 neighbor 2.2.2.1 local-as 2
 neighbor 2.2.2.1 address-family evpn
 neighbor 2.2.2.1 distance 20
 neighbor 2.2.2.1 update-source loopback0
 neighbor 2.2.2.1 pmsitun
 neighbor 2.2.2.1 send-community standard extended
 afi-evpn 101 bridge-group 1
 afi-evpn 101 bmac 007a.6c17.2d38
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 3
 afi-evpn 102 bmac 0055.0039.104f
 afi-evpn 102 encapsulation vpws
 afi-evpn 102 update-source loopback0
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family evpn
 neighbor 4321::1 remote-as 1
 neighbor 4321::1 local-as 2
 neighbor 4321::1 address-family evpn
 neighbor 4321::1 distance 20
 neighbor 4321::1 update-source loopback0
 neighbor 4321::1 pmsitun
 neighbor 4321::1 send-community standard extended
 afi-evpn 101 bridge-group 2
 afi-evpn 101 bmac 0075.0a0d.624d
 afi-evpn 101 encapsulation vpws
 afi-evpn 101 update-source loopback0
 afi-evpn 102 bridge-group 4
 afi-evpn 102 bmac 001f.2926.755c
 afi-evpn 102 encapsulation vpws
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
 |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
 | neighbor | as | ready | learn | sent | uptime   |
 |----------|----|-------|-------|------|----------|
 | 2.2.2.2  | 2  | true  | 2     | 4    | 00:00:13 |
 |__________|____|_______|_______|______|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 sum
r1#show ipv6 bgp 1 sum
 |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
 | neighbor | as | ready | learn | sent | uptime   |
 |----------|----|-------|-------|------|----------|
 | 4321::2  | 2  | true  | 2     | 4    | 00:00:13 |
 |__________|____|_______|_______|______|__________|
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
 | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:16 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:16 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:16 |
 | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:03 |
 | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:16 |
 | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:16 |
 | C   | 4.4.4.0/30 | 0/0    | bvi4      | null    | 00:00:16 |
 | LOC | 4.4.4.1/32 | 0/1    | bvi4      | null    | 00:00:16 |
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
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:17 |
 | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:17 |
 | C   | 3333::/16     | 0/0    | bvi3      | null      | 00:00:17 |
 | LOC | 3333::1/128   | 0/1    | bvi3      | null      | 00:00:17 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:17 |
 | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:04 |
 | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:17 |
 | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:17 |
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
 | brprt bvi        |      |       |    |    |      |     |     |      |     |
 | evpn 2.2.2.2 101 | true | false | 13 | 13 | 0    | 822 | 822 | 0    |     |
 |__________________|______|_______|____|____|______|_____|_____|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                                            | packet             | byte             |  |
 | addr           | iface            | static | time     | tx | rx | drop | tx  | rx  | drop |
 |----------------|------------------|--------|----------|----|----|------|-----|-----|------|
 | 0019.415e.6a66 | evpn 2.2.2.2 101 | false  | 00:00:17 | 12 | 13 | 0    | 792 | 822 | 0    |
 | 0048.6d15.5833 | bvi              | false  | 00:00:17 | 13 | 15 | 0    | 822 | 882 | 0    |
 |________________|__________________|________|__________|____|____|______|_____|_____|______|
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
 | brprt bvi        |      |       |    |    |      |      |      |      |     |
 | evpn 4321::2 101 | true | false | 16 | 15 | 0    | 1072 | 1006 | 0    |     |
 |__________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
 |                                            | packet             | byte              |  |
 | addr           | iface            | static | time     | tx | rx | drop | tx  | rx   | drop |
 |----------------|------------------|--------|----------|----|----|------|-----|------|------|
 | 000a.2132.135b | evpn 4321::2 101 | false  | 00:00:17 | 15 | 15 | 0    | 998 | 1006 | 0    |
 | 0049.5724.7640 | bvi              | false  | 00:00:17 | 14 | 19 | 0    | 932 | 1326 | 0    |
 |________________|__________________|________|__________|____|____|______|_____|______|______|
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
 | brprt bvi        |      |       |    |    |      |      |      |      |     |
 | evpn 2.2.2.2 102 | true | false | 16 | 15 | 0    | 1072 | 1006 | 0    |     |
 |__________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
 |                                            | packet             | byte              |  |
 | addr           | iface            | static | time     | tx | rx | drop | tx  | rx   | drop |
 |----------------|------------------|--------|----------|----|----|------|-----|------|------|
 | 000d.2225.303c | bvi              | false  | 00:00:17 | 14 | 19 | 0    | 932 | 1326 | 0    |
 | 0028.3421.1165 | evpn 2.2.2.2 102 | false  | 00:00:17 | 15 | 15 | 0    | 998 | 1006 | 0    |
 |________________|__________________|________|__________|____|____|______|_____|______|______|
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
 | brprt bvi        |      |       |    |    |      |     |     |      |     |
 | evpn 4321::2 102 | true | false | 15 | 15 | 0    | 954 | 954 | 0    |     |
 |__________________|______|_______|____|____|______|_____|_____|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                                            | packet             | byte             |  |
 | addr           | iface            | static | time     | tx | rx | drop | tx  | rx  | drop |
 |----------------|------------------|--------|----------|----|----|------|-----|-----|------|
 | 0018.0577.0e27 | bvi              | false  | 00:00:17 | 15 | 15 | 0    | 954 | 954 | 0    |
 | 0020.3f4c.7561 | evpn 4321::2 102 | false  | 00:00:17 | 14 | 15 | 0    | 924 | 954 | 0    |
 |________________|__________________|________|__________|____|____|______|_____|_____|______|
r1#
r1#
```

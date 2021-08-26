# Example: p2p ldp tunnel

## **Topology diagram**

![topology](/img/mpls-ldp12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz26r1-log.run
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.3
 tunnel mode p2pldp
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
 tunnel destination 4321::3
 tunnel mode p2pldp
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
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
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
logging file debug ../binTmp/zzz26r2-log.run
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1234:2::1 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.2.2
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
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
logging file debug ../binTmp/zzz26r3-log.run
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.1
 tunnel mode p2pldp
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
 tunnel mode p2pldp
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
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.2.1
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.2.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
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
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop       | label      | targets | bytes |
 |--------|----------|-----------|-----------|------------|---------|-------|
 | 91672  | tester:4 | null      | null      | unlabelled | local   | 0     |
 | 170567 | v1:4     | ethernet1 | 1.1.1.2   | 484257     |         | 0     |
 | 206420 | v1:6     | null      | null      | unlabelled | local   | 832   |
 | 273172 | v1:6     | ethernet1 | 1234:1::2 | 660320     |         | 0     |
 | 411703 | v1:6     | ethernet1 | 1234:1::2 | 262220     |         | 0     |
 | 458982 | tester:6 | null      | null      | unlabelled | local   | 0     |
 | 909400 | v1:4     | null      | null      | unlabelled | local   | 640   |
 | 930796 | v1:4     | ethernet1 | 1.1.1.2   | 517768     |         | 0     |
 |________|__________|___________|___________|____________|_________|_______|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 sum
r1#show ipv4 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                     |
 | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
 |-------|--------|-------|--------|-------|--------|----------|----------|
 | 7     | 7      | 0     | 0      | 0     | 0      | 1.1.1.2  | 00:00:11 |
 |_______|________|_______|________|_______|________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 sum
r1#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                      |
 | learn | advert | learn | advert | learn | advert | neighbor  | uptime   |
 |-------|--------|-------|--------|-------|--------|-----------|----------|
 | 7     | 7      | 0     | 0      | 0     | 0      | 1234:1::2 | 00:00:11 |
 |_______|________|_______|________|_______|________|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 dat
r1#show ipv4 ldp v1 dat
 |~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix     | local  | remote | hop     |
 |------------|--------|--------|---------|
 | 1.1.1.0/24 | 909400 |        | null    |
 | 1.1.1.1/32 | 909400 |        | null    |
 | 2.2.2.1/32 | 909400 |        | null    |
 | 2.2.2.2/32 | 170567 | 484257 | 1.1.1.2 |
 | 2.2.2.3/32 | 930796 | 517768 | 1.1.1.2 |
 | 3.3.3.0/24 | 909400 |        | null    |
 | 3.3.3.1/32 | 909400 |        | null    |
 |____________|________|________|_________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 dat
r1#show ipv6 ldp v1 dat
 |~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|
 | prefix        | local  | remote | hop       |
 |---------------|--------|--------|-----------|
 | 1234:1::/32   | 206420 |        | null      |
 | 1234:1::1/128 | 206420 |        | null      |
 | 3333::/32     | 206420 |        | null      |
 | 3333::1/128   | 206420 |        | null      |
 | 4321::1/128   | 206420 |        | null      |
 | 4321::2/128   | 273172 | 660320 | 1234:1::2 |
 | 4321::3/128   | 411703 | 262220 | 1234:1::2 |
 |_______________|________|________|___________|
r1#
r1#
```

```
r1#
r1#
r1#show inter tun1 full
r1#show inter tun1 full
tunnel1 is up (since 00:00:16, 2 changes)
 description:
 type is p2pldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip4 address=3.3.3.1/24, netmask=255.255.255.0, ifcid=519406391
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 15 packets (990 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~|~~~~~~|
 |       | packet         | byte            |
 | time  | tx | rx | drop | tx  | rx | drop |
 |-------|----|----|------|-----|----|------|
 | 1sec  | 5  | 0  | 0    | 330 | 0  | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0  | 0    |
 |_______|____|____|______|_____|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~|~~~~~~|
 |                          | packet         | byte            |
 | type   | value | handler | tx | rx | drop | tx  | rx | drop |
 |--------|-------|---------|----|----|------|-----|----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0  | 0    |
 | ethtyp | 0800  | ip4     | 15 | 0  | 0    | 990 | 0  | 0    |
 |________|_______|_________|____|____|______|_____|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 15   | 990  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~|~~~~~~|
 |            | packet         | byte            |
 | size       | tx | rx | drop | tx  | rx | drop |
 |------------|----|----|------|-----|----|------|
 | 0-255      | 15 | 0  | 0    | 990 | 0  | 0    |
 | 256-511    | 0  | 0  | 0    | 0   | 0  | 0    |
 | 512-767    | 0  | 0  | 0    | 0   | 0  | 0    |
 | 768-1023   | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0   | 0  | 0    |
 |____________|____|____|______|_____|____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet           | byte             |
 | class | cos | exp | prec | cos | exp | prec |
 |-------|-----|-----|------|-----|-----|------|
 | 0     | 15  | 15  | 15   | 990 | 990 | 990  |
 | 1     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 2     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 3     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 4     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 5     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 6     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 7     | 0   | 0   | 0    | 0   | 0   | 0    |
 |_______|_____|_____|______|_____|_____|______|
        2640|
        2376|#  #
        2112|#  #
        1848|#  #
        1584|#  #
        1320|#  #
        1056|#  #
         792|#  #
         528|#  #
         264|#  # #####
           0|#  # #####
         bps|0---------10--------20--------30--------40--------50-------- seconds
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- minutes
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- hours
r1#
r1#
```

```
r1#
r1#
r1#show inter tun2 full
r1#show inter tun2 full
tunnel2 is up (since 00:00:16, 2 changes)
 description:
 type is p2pldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip6 address=3333::1/32, netmask=ffff:ffff::, ifcid=340915066
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 18 packets (1220 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~|~~~~~~|
 |       | packet         | byte            |
 | time  | tx | rx | drop | tx  | rx | drop |
 |-------|----|----|------|-----|----|------|
 | 1sec  | 10 | 0  | 0    | 660 | 0  | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0  | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0  | 0    |
 |_______|____|____|______|_____|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx   | rx | drop |
 |--------|-------|---------|----|----|------|------|----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0  | 0    |
 | ethtyp | 86dd  | ip6     | 18 | 0  | 0    | 1220 | 0  | 0    |
 |________|_______|_________|____|____|______|______|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 58    | 18   | 1220 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 |            | packet         | byte             |
 | size       | tx | rx | drop | tx   | rx | drop |
 |------------|----|----|------|------|----|------|
 | 0-255      | 18 | 0  | 0    | 1220 | 0  | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0  | 0    |
 |____________|____|____|______|______|____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |       | packet           | byte               |
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 18  | 18  | 18   | 1220 | 1220 | 1220 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        5280|
        4752|#
        4224|#
        3696|#
        3168|#
        2640|#
        2112|#
        1584|#              #
        1056|##             #
         528|##             #
           0|####           #
         bps|0---------10--------20--------30--------40--------50-------- seconds
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- minutes
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- hours
r1#
r1#
```

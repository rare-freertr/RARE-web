# Example: ethernet over mpls

## **Topology diagram**

![topology](/img/mpls-pwe09.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 mac-learn
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
 ipv4 address 3.3.3.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source loopback0
 exit
!
vpdn eompls
 bridge-group 1
 proxy p1
 target 2.2.2.2
 mtu 1500
 vcid 1234
 pwtype ethernet
 protocol pweompls
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
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
 mac-learn
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
 ipv4 address 3.3.3.2 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source loopback0
 exit
!
vpdn eompls
 bridge-group 1
 proxy p1
 target 2.2.2.1
 mtu 1500
 vcid 1234
 pwtype ethernet
 protocol pweompls
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
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
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf  | iface     | hop     | label      | targets | bytes |
 |---------|------|-----------|---------|------------|---------|-------|
 | 385758  | v1:4 | null      | null    | unlabelled | pwe     | 1102  |
 | 534862  | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 543395  | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 880837  | v1:6 | ethernet1 | 1234::2 | unlabelled |         | 0     |
 | 1016298 | v1:4 | ethernet1 | 1.1.1.2 | unlabelled |         | 0     |
 |_________|______|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 sum
r1#show ipv4 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | learn | advert | l2learn | l2advert | mplearn | mpadvert | neighbor | uptime   |
 |-------|--------|---------|----------|---------|----------|----------|----------|
 | 0     | 0      | 0       | 0        | 0       | 0        | 1.1.1.2  | 00:00:05 |
 | 6     | 6      | 1       | 1        | 0       | 0        | 2.2.2.2  | 00:00:09 |
 |_______|________|_________|__________|_________|__________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 sum
r1#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | learn | advert | l2learn | l2advert | mplearn | mpadvert | neighbor | uptime   |
 |-------|--------|---------|----------|---------|----------|----------|----------|
 | 0     | 0      | 0       | 0        | 0       | 0        | 1234::2  | 00:00:05 |
 |_______|________|_________|__________|_________|__________|__________|__________|
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
 | pwe 2.2.2.2 1234 | true    | false    | 1090 | 1102 | 0    |
 |__________________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~|~~~~~~|~~~~~~|
 | address        | interface        | time     | tx  | rx   | drop |
 |----------------|------------------|----------|-----|------|------|
 | 0045.5262.4b2a | pwe 2.2.2.2 1234 | 00:00:00 | 940 | 970  | 0    |
 | 0050.0f32.034d | bvi              | 00:00:00 | 970 | 1090 | 0    |
 |________________|__________________|__________|_____|______|______|
r1#
r1#
```

```
r1#
r1#
r1#show inter bvi1 full
r1#show inter bvi1 full
bvi1 is up (since 00:00:10, 1 changes)
 description:
 type is bridged, hwaddr=0050.0f32.034d, mtu=1500, bw=8000kbps, vrf=v1
 ip4 address=3.3.3.1/24, netmask=255.255.255.0, ifcid=10013
 received 11 packets (970 bytes) dropped 0 packets (0 bytes)
 transmitted 15 packets (1090 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 940  | 940     | 0    | 10   | 10      | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 940 | 940 | 0    |
 | ethtyp | 0806  | arp4    | 5  | 1  | 0    | 150 | 30  | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 10   | 940  |
 | 0     | 5    | 150  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~~|
 | size       | tx | rx | drop | tx   | rx  | drop |
 |------------|----|----|------|------|-----|------|
 | 0-255      | 15 | 11 | 0    | 1090 | 970 | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0   | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0   | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0   | 0    |
 |____________|____|____|______|______|_____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 15  | 15  | 15   | 1090 | 1090 | 1090 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         15k|
         13k|#
         12k|#
         10k|#
        9024|#
        7520|#
        6016|#
        4512|#
        3008|#
        1504|#
           0|# #####
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
r1#show ipv4 arp bvi1
r1#show ipv4 arp bvi1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
 | mac            | address | time     | static |
 |----------------|---------|----------|--------|
 | 0045.5262.4b2a | 3.3.3.2 | 00:00:10 | false  |
 |________________|_________|__________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 neigh bvi1
r1#show ipv6 neigh bvi1
% protocol not enabled
r1#
r1#
```

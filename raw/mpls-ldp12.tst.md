# Example: p2p ldp tunnel

## **Topology diagram**

![topology](/img/mpls-ldp12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
!
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
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
!
end
```

## **Verification**

```
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf  | iface     | hop       | label      | targets | bytes |
 |---------|------|-----------|-----------|------------|---------|-------|
 | 417829  | v1:6 | ethernet1 | 1234:1::2 | 112945     |         | 0     |
 | 437487  | v1:4 | ethernet1 | 1.1.1.2   | 544838     |         | 0     |
 | 474779  | v1:6 | ethernet1 | 1234:1::2 | 229281     |         | 0     |
 | 687059  | v1:4 | ethernet1 | 1.1.1.2   | 633456     |         | 0     |
 | 826339  | v1:6 | null      | null      | unlabelled | local   | 1120  |
 | 1026787 | v1:4 | null      | null      | unlabelled | local   | 920   |
 |_________|______|___________|___________|____________|_________|_______|
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
 | 7     | 7      | 0       | 0        | 0       | 0        | 1.1.1.2  | 00:00:09 |
 |_______|________|_________|__________|_________|__________|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 ldp v1 sum
r1#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | learn | advert | l2learn | l2advert | mplearn | mpadvert | neighbor  | uptime   |
 |-------|--------|---------|----------|---------|----------|-----------|----------|
 | 7     | 7      | 0       | 0        | 0       | 0        | 1234:1::2 | 00:00:14 |
 |_______|________|_________|__________|_________|__________|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 ldp v1 dat
r1#show ipv4 ldp v1 dat
 |~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~|~~~~~~~~~|
 | prefix     | local   | remote | hop     |
 |------------|---------|--------|---------|
 | 1.1.1.0/24 | 1026787 |        | null    |
 | 1.1.1.1/32 | 1026787 |        | null    |
 | 2.2.2.1/32 | 1026787 |        | null    |
 | 2.2.2.2/32 | 437487  | 544838 | 1.1.1.2 |
 | 2.2.2.3/32 | 687059  | 633456 | 1.1.1.2 |
 | 3.3.3.0/24 | 1026787 |        | null    |
 | 3.3.3.1/32 | 1026787 |        | null    |
 |____________|_________|________|_________|
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
 | 1234:1::/32   | 826339 |        | null      |
 | 1234:1::1/128 | 826339 |        | null      |
 | 3333::/32     | 826339 |        | null      |
 | 3333::1/128   | 826339 |        | null      |
 | 4321::1/128   | 826339 |        | null      |
 | 4321::2/128   | 474779 | 229281 | 1234:1::2 |
 | 4321::3/128   | 417829 | 112945 | 1234:1::2 |
 |_______________|________|________|___________|
r1#
r1#
```

```
r1#
r1#
r1#show inter tun1 full
r1#show inter tun1 full
tunnel1 is up (since 00:00:15, 2 changes)
 description:
 type is p2pldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip4 address=3.3.3.1/24, netmask=255.255.255.0, ifcid=10013
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 15 packets (1410 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx   | rx | drop |
 |--------|-------|---------|----|----|------|------|----|------|
 | ethtyp | 0800  | ip4     | 15 | 0  | 0    | 1410 | 0  | 0    |
 |________|_______|_________|____|____|______|______|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 15   | 1410 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 | size       | tx | rx | drop | tx   | rx | drop |
 |------------|----|----|------|------|----|------|
 | 0-255      | 15 | 0  | 0    | 1410 | 0  | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0  | 0    |
 |____________|____|____|______|______|____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 15  | 15  | 15   | 1410 | 1410 | 1410 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        7520|
        6768| #
        6016| #
        5264| #
        4512| #
        3760| #
        3008| #
        2256| #
        1504| #
         752| #
           0| # #####
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
tunnel2 is up (since 00:00:15, 2 changes)
 description:
 type is p2pldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip6 address=3333::1/32, netmask=ffff:ffff::, ifcid=10013
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 13 packets (1370 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx   | rx | drop |
 |--------|-------|---------|----|----|------|------|----|------|
 | ethtyp | 86dd  | ip6     | 13 | 0  | 0    | 1370 | 0  | 0    |
 |________|_______|_________|____|____|______|______|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 58    | 13   | 1370 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~|~~~~~~|
 | size       | tx | rx | drop | tx   | rx | drop |
 |------------|----|----|------|------|----|------|
 | 0-255      | 13 | 0  | 0    | 1370 | 0  | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0  | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0  | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0  | 0    |
 |____________|____|____|______|______|____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 13  | 13  | 13   | 1370 | 1370 | 1370 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        9120|
        8208| #
        7296| #
        6384| #
        5472| #
        4560| #
        3648| #
        2736| #
        1824| #            #
         912| #            #
           0| #            #
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

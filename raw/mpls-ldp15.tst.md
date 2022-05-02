# Example: mp2mp ldp tunnel

## **Topology diagram**

![topology](/img/mpls-ldp15.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz76r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
interface ethernet1
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
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.2
 tunnel mode mp2mpldp
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 4321::2
 tunnel mode mp2mpldp
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
ipv6 route v1 :: :: 1234:1::2
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
logging file debug ../binTmp/zzz76r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
interface ethernet1
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
interface ethernet3
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1234:3::1 ffff:ffff::
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
ipv4 route v1 2.2.2.4 255.255.255.255 1.1.3.2
!
ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
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
logging file debug ../binTmp/zzz76r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.2
 tunnel mode mp2mpldp
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 4321::2
 tunnel mode mp2mpldp
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.1
!
ipv6 route v1 :: :: 1234:2::1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz76r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1234:3::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2.2.2.2
 tunnel mode mp2mpldp
 vrf forwarding v1
 ipv4 address 3.3.3.4 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel key 1234
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 4321::2
 tunnel mode mp2mpldp
 vrf forwarding v1
 ipv6 address 3333::4 ffff:ffff::
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.3.1
!
ipv6 route v1 :: :: 1234:3::1
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
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~|
 | label  | vrf      | iface | hop  | label      | targets         | bytes  |
 |--------|----------|-------|------|------------|-----------------|--------|
 | 58     | tester:6 | null  | null | unlabelled | local           | 0      |
 | 48609  | tester:4 | null  | null | unlabelled | local           | 0      |
 | 129071 | tester:6 | null  | null | unlabelled | local           | 0      |
 | 205674 | v1:4     | null  | null | unlabelled | local           | 0      |
 | 448141 | tester:4 | null  | null | unlabelled | local           | 0      |
 | 452536 | v1:6     | null  | null | unlabelled | local           | 0      |
 | 551919 | v1:4     | null  | null | unlabelled | local duplicate | 461120 |
 | 556165 | tester:6 | null  | null | unlabelled | local           | 0      |
 | 685297 | tester:4 | null  | null | unlabelled | local           | 0      |
 | 922973 | v1:6     | null  | null | unlabelled | local duplicate | 387392 |
 |________|__________|_______|______|____________|_________________|________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv4 ldp v1 sum
r3#show ipv4 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                     |
 | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
 |-------|--------|-------|--------|-------|--------|----------|----------|
 | 0     | 0      | 0     | 0      | 1     | 1      | 1.1.2.1  | 00:00:07 |
 |_______|________|_______|________|_______|________|__________|__________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv6 ldp v1 sum
r3#show ipv6 ldp v1 sum
 |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | prefix         | layer2         | p2mp           |                      |
 | learn | advert | learn | advert | learn | advert | neighbor  | uptime   |
 |-------|--------|-------|--------|-------|--------|-----------|----------|
 | 0     | 0      | 0     | 0      | 1     | 1      | 1234:2::1 | 00:00:07 |
 |_______|________|_______|________|_______|________|___________|__________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv4 ldp v1 mpdat
r3#show ipv4 ldp v1 mpdat
 |~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | type  | local      | root    | opaque               | uplink  | peers                       |
 |-------|------------|---------|----------------------|---------|-----------------------------|
 | mp2mp | false true | 2.2.2.2 | 01 00 04 00 00 04 d2 | 1.1.2.1 | local 551919/1.1.2.1/904596 |
 |_______|____________|_________|______________________|_________|_____________________________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv6 ldp v1 mpdat
r3#show ipv6 ldp v1 mpdat
 |~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | type  | local      | root    | opaque               | uplink    | peers                         |
 |-------|------------|---------|----------------------|-----------|-------------------------------|
 | mp2mp | false true | 4321::2 | 01 00 04 00 00 04 d2 | 1234:2::1 | local 922973/1234:2::1/524599 |
 |_______|____________|_________|______________________|___________|_______________________________|
r3#
r3#
```

```
r3#
r3#
r3#show inter tun1 full
r3#show inter tun1 full
tunnel1 is up
 description:
 state changed 15 times, last at 2022-05-02 21:14:08, 00:00:13 ago
 last packet input never ago, output 00:00:00 ago, drop never ago
 type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ipv4 address=3.3.3.3/24, mask=255.255.255.0, ifcid=725207220
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 7765 packets (512490 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |       | packet           | byte               |
 | time  | tx   | rx | drop | tx     | rx | drop |
 |-------|------|----|------|--------|----|------|
 | 1sec  | 2157 | 0  | 0    | 142362 | 0  | 0    |
 | 1min  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1hour | 0    | 0  | 0    | 0      | 0  | 0    |
 |_______|______|____|______|________|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |                          | packet           | byte               |
 | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
 |--------|-------|---------|------|----|------|--------|----|------|
 | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
 | ethtyp | 0800  | ip4     | 7772 | 0  | 0    | 512952 | 0  | 0    |
 |________|_______|_________|______|____|______|________|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~~~|
 | proto | pack | byte   |
 |-------|------|--------|
 | 1     | 7772 | 512952 |
 |_______|______|________|
 |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |            | packet           | byte               |
 | size       | tx   | rx | drop | tx     | rx | drop |
 |------------|------|----|------|--------|----|------|
 | 0-255      | 7772 | 0  | 0    | 512952 | 0  | 0    |
 | 256-511    | 0    | 0  | 0    | 0      | 0  | 0    |
 | 512-767    | 0    | 0  | 0    | 0      | 0  | 0    |
 | 768-1023   | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1024-1279  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1280-1535  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1536-1791  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1792-65535 | 0    | 0  | 0    | 0      | 0  | 0    |
 |____________|______|____|______|________|____|______|
 |~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|
 |       | packet             | byte                     |
 | class | cos  | exp  | prec | cos    | exp    | prec   |
 |-------|------|------|------|--------|--------|--------|
 | 0     | 7772 | 7772 | 7772 | 512952 | 512952 | 512952 |
 | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
 |_______|______|______|______|________|________|________|
       1775k| #
       1597k| #
       1420k| #
       1242k| #
       1065k|##
        887k|###
        710k|###
        532k|###
        355k|###
        177k|###
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- seconds
          10|
           9|
           8|
           7|
           6|
           5|
           4|
           3|
           2|
           1|
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- minutes
          10|
           9|
           8|
           7|
           6|
           5|
           4|
           3|
           2|
           1|
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- hours
r3#
r3#
```

```
r3#
r3#
r3#show inter tun2 full
r3#show inter tun2 full
tunnel2 is up
 description:
 state changed 15 times, last at 2022-05-02 21:14:08, 00:00:13 ago
 last packet input never ago, output 00:00:00 ago, drop never ago
 type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ipv6 address=3333::3/32, mask=ffff:ffff::, ifcid=426557553
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 4862 packets (320924 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |       | packet           | byte               |
 | time  | tx   | rx | drop | tx     | rx | drop |
 |-------|------|----|------|--------|----|------|
 | 1sec  | 1965 | 0  | 0    | 129690 | 0  | 0    |
 | 1min  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1hour | 0    | 0  | 0    | 0      | 0  | 0    |
 |_______|______|____|______|________|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |                          | packet           | byte               |
 | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
 |--------|-------|---------|------|----|------|--------|----|------|
 | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
 | ethtyp | 86dd  | ip6     | 4862 | 0  | 0    | 320924 | 0  | 0    |
 |________|_______|_________|______|____|______|________|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~~~|
 | proto | pack | byte   |
 |-------|------|--------|
 | 58    | 4863 | 320990 |
 |_______|______|________|
 |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |            | packet           | byte               |
 | size       | tx   | rx | drop | tx     | rx | drop |
 |------------|------|----|------|--------|----|------|
 | 0-255      | 4864 | 0  | 0    | 321056 | 0  | 0    |
 | 256-511    | 0    | 0  | 0    | 0      | 0  | 0    |
 | 512-767    | 0    | 0  | 0    | 0      | 0  | 0    |
 | 768-1023   | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1024-1279  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1280-1535  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1536-1791  | 0    | 0  | 0    | 0      | 0  | 0    |
 | 1792-65535 | 0    | 0  | 0    | 0      | 0  | 0    |
 |____________|______|____|______|________|____|______|
 |~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|
 |       | packet             | byte                     |
 | class | cos  | exp  | prec | cos    | exp    | prec   |
 |-------|------|------|------|--------|--------|--------|
 | 0     | 4865 | 4865 | 4865 | 321122 | 321122 | 321122 |
 | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
 |_______|______|______|______|________|________|________|
       1037k|#
        933k|#
        830k|#
        726k|#
        622k|#
        518k|#
        415k|##
        311k|##
        207k|##
        103k|##
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- seconds
          10|
           9|
           8|
           7|
           6|
           5|
           4|
           3|
           2|
           1|
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- minutes
          10|
           9|
           8|
           7|
           6|
           5|
           4|
           3|
           2|
           1|
           0|############################################################
         bps|0---------10--------20--------30--------40--------50-------- hours
r3#
r3#
```

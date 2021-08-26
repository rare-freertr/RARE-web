# Example: mp2mp ldp tunnel

## **Topology diagram**

![topology](/img/mpls-ldp15.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz13r1-log.run
!
vrf definition tester
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
 no description
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
logging file debug ../binTmp/zzz13r2-log.run
!
vrf definition tester
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
interface ethernet3
 no description
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
logging file debug ../binTmp/zzz13r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
 no description
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
logging file debug ../binTmp/zzz13r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
 no description
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
 no description
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
 | 280289 | tester:6 | null  | null | unlabelled | local           | 0      |
 | 407001 | v1:4     | null  | null | unlabelled | local           | 0      |
 | 542788 | v1:6     | null  | null | unlabelled | local duplicate | 140288 |
 | 705081 | v1:4     | null  | null | unlabelled | local duplicate | 592704 |
 | 777960 | tester:4 | null  | null | unlabelled | local           | 0      |
 | 785696 | v1:6     | null  | null | unlabelled | local           | 0      |
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
 | 0     | 0      | 0     | 0      | 1     | 1      | 1.1.2.1  | 00:00:06 |
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
 | 0     | 0      | 0     | 0      | 1     | 1      | 1234:2::1 | 00:00:11 |
 |_______|________|_______|________|_______|________|___________|__________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv4 ldp v1 mpdat
r3#show ipv4 ldp v1 mpdat
 |~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | type  | root    | opaque               | uplink  | peers                       |
 |-------|---------|----------------------|---------|-----------------------------|
 | mp2mp | 2.2.2.2 | 01 00 04 00 00 04 d2 | 1.1.2.1 | local 705081/1.1.2.1/189843 |
 |_______|_________|______________________|_________|_____________________________|
r3#
r3#
```

```
r3#
r3#
r3#show ipv6 ldp v1 mpdat
r3#show ipv6 ldp v1 mpdat
 |~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | type  | root    | opaque               | uplink    | peers                          |
 |-------|---------|----------------------|-----------|--------------------------------|
 | mp2mp | 4321::2 | 01 00 04 00 00 04 d2 | 1234:2::1 | local 542788/1234:2::1/1025960 |
 |_______|_________|______________________|___________|________________________________|
r3#
r3#
```

```
r3#
r3#
r3#show inter tun1 full
r3#show inter tun1 full
tunnel1 is up (since 00:00:17, 1 changes)
 description:
 type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip4 address=3.3.3.3/24, netmask=255.255.255.0, ifcid=219906660
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 3063 packets (202158 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~|~~~~|~~~~~~|~~~~~~~|~~~~|~~~~~~|
 |       | packet          | byte              |
 | time  | tx  | rx | drop | tx    | rx | drop |
 |-------|-----|----|------|-------|----|------|
 | 1sec  | 604 | 0  | 0    | 39864 | 0  | 0    |
 | 1min  | 0   | 0  | 0    | 0     | 0  | 0    |
 | 1hour | 0   | 0  | 0    | 0     | 0  | 0    |
 |_______|_____|____|______|_______|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |                          | packet           | byte               |
 | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
 |--------|-------|---------|------|----|------|--------|----|------|
 | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
 | ethtyp | 0800  | ip4     | 3075 | 0  | 0    | 202950 | 0  | 0    |
 |________|_______|_________|______|____|______|________|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~~~|
 | proto | pack | byte   |
 |-------|------|--------|
 | 1     | 3075 | 202950 |
 |_______|______|________|
 |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |            | packet           | byte               |
 | size       | tx   | rx | drop | tx     | rx | drop |
 |------------|------|----|------|--------|----|------|
 | 0-255      | 3076 | 0  | 0    | 203016 | 0  | 0    |
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
 | 0     | 3076 | 3076 | 3076 | 203016 | 203016 | 203016 |
 | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
 |_______|______|______|______|________|________|________|
        524k|
        471k|  #
        419k| ##
        367k| ##
        314k|###
        262k|###
        209k|####
        157k|####
        104k|####
         52k|####
           0|####
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
r3#
r3#
```

```
r3#
r3#
r3#show inter tun2 full
r3#show inter tun2 full
tunnel2 is up (since 00:00:17, 1 changes)
 description:
 type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ip6 address=3333::3/32, netmask=ffff:ffff::, ifcid=493694704
 received 0 packets (0 bytes) dropped 0 packets (0 bytes)
 transmitted 2232 packets (147344 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~|~~~~|~~~~~~|~~~~~~~|~~~~|~~~~~~|
 |       | packet          | byte              |
 | time  | tx  | rx | drop | tx    | rx | drop |
 |-------|-----|----|------|-------|----|------|
 | 1sec  | 623 | 0  | 0    | 41118 | 0  | 0    |
 | 1min  | 0   | 0  | 0    | 0     | 0  | 0    |
 | 1hour | 0   | 0  | 0    | 0     | 0  | 0    |
 |_______|_____|____|______|_______|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |                          | packet           | byte               |
 | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
 |--------|-------|---------|------|----|------|--------|----|------|
 | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
 | ethtyp | 86dd  | ip6     | 2232 | 0  | 0    | 147344 | 0  | 0    |
 |________|_______|_________|______|____|______|________|____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~~~|
 | proto | pack | byte   |
 |-------|------|--------|
 | 58    | 2233 | 147410 |
 |_______|______|________|
 |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
 |            | packet           | byte               |
 | size       | tx   | rx | drop | tx     | rx | drop |
 |------------|------|----|------|--------|----|------|
 | 0-255      | 2233 | 0  | 0    | 147410 | 0  | 0    |
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
 | 0     | 2233 | 2233 | 2233 | 147410 | 147410 | 147410 |
 | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
 | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
 |_______|______|______|______|________|________|________|
        397k|
        357k| #
        317k|##
        277k|###
        238k|###
        198k|###
        158k|###
        119k|###
         79k|###
         39k|###
           0|####            #
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
r3#
r3#
```

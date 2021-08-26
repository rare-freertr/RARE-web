# Example: bridged mac rewrite

## **Topology diagram**

![topology](/img/conn-bridge14.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz81r1-log.run
!
bridge 1
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
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
logging file debug ../binTmp/zzz81r2-log.run
!
bridge 1
 mac-learn
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 bridge-macrewrite 0000.1234.1234
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
 bridge-macrewrite 0000.1234.1234
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
logging file debug ../binTmp/zzz81r3-log.run
!
bridge 1
 mac-learn
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
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
logging file debug ../binTmp/zzz81r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234::4 ffff::
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
r2#
r2#
r2#show bridge 1
r2#show bridge 1
 |~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                         | packet           | byte               |     |
 | iface     | fwd  | phys | tx  | rx  | drop | tx   | rx   | drop | grp |
 |-----------|------|------|-----|-----|------|------|------|------|-----|
 | bvi       | true | true | 0   | 0   | 0    | 0    | 0    | 0    |     |
 | ethernet1 | true | true | 101 | 93  | 0    | 6690 | 6072 | 0    |     |
 | ethernet2 | true | true | 117 | 116 | 0    | 7640 | 7664 | 0    |     |
 |___________|______|______|_____|_____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                       | packet         | byte               |
 | addr           | iface     | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|-----------|----------|----|----|------|------|------|------|
 | 0000.0000.4444 | ethernet2 | 00:00:19 | 54 | 58 | 0    | 3572 | 3832 | 0    |
 | 0012.1a31.000c | ethernet1 | 00:00:19 | 87 | 93 | 0    | 5646 | 6072 | 0    |
 | 005b.6f5a.6b7a | ethernet2 | 00:00:19 | 54 | 58 | 0    | 3572 | 3832 | 0    |
 | 0079.4244.4e1c | bvi       | 00:00:19 | 80 | 83 | 0    | 5228 | 5434 | 0    |
 |________________|___________|__________|____|____|______|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:19, 1 changes)
 description:
 type is bridged, hwaddr=0079.4244.4e1c, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=52362516
 ip6 address=1234::2/16, netmask=ffff::, ifcid=269394033
 received 91 packets (5992 bytes) dropped 0 packets (0 bytes)
 transmitted 83 packets (5434 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |       | packet         | byte               |
 | time  | tx | rx | drop | tx   | rx   | drop |
 |-------|----|----|------|------|------|------|
 | 1sec  | 25 | 25 | 0    | 1650 | 1650 | 0    |
 | 1min  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1hour | 0  | 0  | 0    | 0    | 0    | 0    |
 |_______|____|____|______|______|______|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 0800  | ip4     | 42 | 42 | 0    | 2772 | 2772 | 0    |
 | ethtyp | 0806  | arp4    | 3  | 5  | 0    | 90   | 180  | 0    |
 | ethtyp | 86dd  | ip6     | 38 | 44 | 0    | 2572 | 3040 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 0     | 3    | 90   |
 | 1     | 42   | 2772 |
 | 58    | 38   | 2572 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 83 | 91 | 0    | 5434 | 5992 | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0    | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0    | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0    | 0    |
 |____________|____|____|______|______|______|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |       | packet           | byte               |
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 83  | 83  | 83   | 5434 | 5434 | 5434 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         26k|
         23k|#
         21k|#
         18k|#
         15k|#
         13k|#
         10k|#
        7920|#
        5280|# # #    #     # #
        2640|#####    ##    ###
           0|#####  # ### # ###
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
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 arp bvi1
r2#show ipv4 arp bvi1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
 | mac            | address | time     | static |
 |----------------|---------|----------|--------|
 | 0012.1a31.000c | 1.1.1.1 | 00:00:18 | false  |
 | 005b.6f5a.6b7a | 1.1.1.3 | 00:00:18 | false  |
 | 0000.0000.4444 | 1.1.1.4 | 00:00:18 | false  |
 |________________|_________|__________|________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 neigh bvi1
r2#show ipv6 neigh bvi1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
 | mac            | address                  | time     | static | router |
 |----------------|--------------------------|----------|--------|--------|
 | 0012.1a31.000c | 1234::1                  | 00:00:18 | false  | false  |
 | 005b.6f5a.6b7a | 1234::3                  | 00:00:18 | false  | false  |
 | 0000.0000.4444 | 1234::4                  | 00:00:18 | false  | false  |
 | 0000.0000.4444 | fe80::200:ff:fe00:4444   | 00:00:18 | false  | false  |
 | 005b.6f5a.6b7a | fe80::25b:6fff:fe5a:6b7a | 00:00:18 | false  | false  |
 |________________|__________________________|__________|________|________|
r2#
r2#
```

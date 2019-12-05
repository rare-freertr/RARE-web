# Example: spantree over ethernet

## **Topology diagram**

![topology](/img/conn-stp.tst.png)

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
 stp-mode ieee
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
 stp-mode ieee
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
end
```

## **Verification**

```
r2#
r2#
r2#show bridge 1
r2#show bridge 1
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | interface | forward | physical | tx   | rx   | drop |
 |-----------|---------|----------|------|------|------|
 | bvi       | true    | true     | 0    | 0    | 0    |
 | ethernet1 | true    | true     | 2800 | 2992 | 0    |
 | ethernet2 | true    | true     | 384  | 200  | 0    |
 |___________|_________|__________|______|______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface | time     | tx   | rx   | drop |
 |----------------|-----------|----------|------|------|------|
 | 0008.7844.415d | bvi       | 00:00:00 | 2610 | 2854 | 0    |
 | 0065.0d09.1432 | ethernet1 | 00:00:00 | 2526 | 2720 | 0    |
 |________________|___________|__________|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:10, 1 changes)
 description:
 type is bridged, hwaddr=0008.7844.415d, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=10011
 ip6 address=1234::2/16, netmask=ffff::, ifcid=10011
 received 27 packets (2720 bytes) dropped 0 packets (0 bytes)
 transmitted 29 packets (2854 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 1040 | 1040    | 0    | 10   | 10      | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 940  | 940  | 0    |
 | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30   | 36   | 0    |
 | ethtyp | 86dd  | ip6     | 18 | 16 | 0    | 1884 | 1744 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 58    | 18   | 1884 |
 | 1     | 10   | 940  |
 | 0     | 1    | 30   |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 29 | 27 | 0    | 2854 | 2720 | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0    | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0    | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0    | 0    |
 |____________|____|____|______|______|______|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | class | cos | exp | prec | cos  | exp  | prec |
 |-------|-----|-----|------|------|------|------|
 | 0     | 29  | 29  | 29   | 2854 | 2854 | 2854 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         16k|
         14k|#
         13k|#
         11k|#
        9984|#
        8320|#  #
        6656|#  #
        4992|## #
        3328|## #
        1664|####     #
           0|#### #   #
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
 | 0065.0d09.1432 | 1.1.1.1 | 00:00:10 | false  |
 |________________|_________|__________|________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 neigh bvi1
r2#show ipv6 neigh bvi1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
 | mac            | address                 | time     | static | router |
 |----------------|-------------------------|----------|--------|--------|
 | 0065.0d09.1432 | 1234::1                 | 00:00:10 | false  | false  |
 | 0065.0d09.1432 | fe80::265:dff:fe09:1432 | 00:00:10 | false  | false  |
 |________________|_________________________|__________|________|________|
r2#
r2#
```

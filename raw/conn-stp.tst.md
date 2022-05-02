# Example: spantree over ethernet

## **Topology diagram**

![topology](/img/conn-stp.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz62r1-log.run
!
bridge 1
 mac-learn
 stp-mode ieee
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
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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
logging file debug ../binTmp/zzz62r2-log.run
!
bridge 1
 mac-learn
 stp-mode ieee
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
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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

## **Verification**

```
r2#
r2#
r2#show bridge 1
r2#show bridge 1
 |~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                         | packet         | byte               |     |
 | iface     | fwd  | phys | tx | rx | drop | tx   | rx   | drop | grp |
 |-----------|------|------|----|----|------|------|------|------|-----|
 | brprt bvi |      |      |    |    |      |      |      |      |     |
 | ethernet1 | true | true | 32 | 35 | 0    | 1962 | 2106 | 0    |     |
 | ethernet2 | true | true | 8  | 5  | 0    | 384  | 200  | 0    |     |
 |___________|______|______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|
 | iface     | fwd  | phys | tx | rx | drop |
 |-----------|------|------|----|----|------|
 | brprt bvi |      |      |    |    |      |
 | ethernet1 | true | true | 5  | 35 | 30   |
 | ethernet2 | true | true | 5  | 5  | 0    |
 |___________|______|______|____|____|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                     | packet             | byte               |  |
 | addr           | iface     | static | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|-----------|--------|----------|----|----|------|------|------|------|
 | 0006.5c11.256b | bvi       | false  | 00:00:09 | 26 | 30 | 0    | 1724 | 2016 | 0    |
 | 002a.6a31.4a16 | ethernet1 | false  | 00:00:09 | 26 | 28 | 0    | 1688 | 1834 | 0    |
 |________________|___________|________|__________|____|____|______|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up
 description:
 state changed 3 times, last at 2022-05-02 21:15:10, 00:00:09 ago
 last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
 type is bridged, hwaddr=0006.5c11.256b, mtu=1500, bw=100mbps, vrf=v1
 ipv4 address=1.1.1.2/24, mask=255.255.255.0, ifcid=478431407
 ipv6 address=1234::2/16, mask=ffff::, ifcid=61836186
 received 28 packets (1834 bytes) dropped 0 packets (0 bytes)
 transmitted 30 packets (2016 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 3  | 3  | 0    | 198 | 198 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 0800  | ip4     | 11 | 11 | 0    | 726  | 726  | 0    |
 | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30   | 36   | 0    |
 | ethtyp | 86dd  | ip6     | 18 | 16 | 0    | 1260 | 1072 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 0     | 1    | 30   |
 | 1     | 11   | 726  |
 | 58    | 18   | 1260 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 30 | 28 | 0    | 2016 | 1834 | 0    |
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
 | 0     | 30  | 30  | 30   | 2016 | 2016 | 2016 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        6460|  #
        5814|  #
        5168|  #
        4522|  #
        3876|  #
        3230|  #
        2584|# #
        1938|# #     #
        1292|###     #
         646|### #   #
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
 | 002a.6a31.4a16 | 1.1.1.1 | 00:00:09 | false  |
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
 | 002a.6a31.4a16 | 1234::1                  | 00:00:09 | false  | false  |
 | 002a.6a31.4a16 | fe80::22a:6aff:fe31:4a16 | 00:00:09 | false  | false  |
 |________________|__________________________|__________|________|________|
r2#
r2#
```

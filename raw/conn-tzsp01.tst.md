# Example: tzsp over ipv4

## **Topology diagram**

![topology](/img/conn-tzsp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz66r1-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn vx
 bridge-group 1
 proxy p1
 target 1.1.1.2
 protocol tzsp
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
logging file debug ../binTmp/zzz66r2-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn vx
 bridge-group 1
 proxy p1
 target 1.1.1.1
 protocol tzsp
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
 |~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                                | packet         | byte               |     |
 | iface           | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
 |-----------------|------|-------|----|----|------|------|------|------|-----|
 | brprt bvi       |      |       |    |    |      |      |      |      |     |
 | tzsp to 1.1.1.1 | true | false | 33 | 31 | 0    | 2206 | 2390 | 0    |     |
 |_________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                           | packet             | byte               |  |
 | addr           | iface           | static | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|-----------------|--------|----------|----|----|------|------|------|------|
 | 0002.225c.107a | bvi             | false  | 00:00:05 | 30 | 33 | 0    | 1988 | 2206 | 0    |
 | 0022.047d.1f2f | tzsp to 1.1.1.1 | false  | 00:00:05 | 29 | 31 | 0    | 1878 | 2018 | 0    |
 |________________|_________________|________|__________|____|____|______|______|______|______|
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
 state changed 3 times, last at 2022-05-02 21:08:36, 00:00:05 ago
 last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
 type is bridged, hwaddr=0002.225c.107a, mtu=1400, bw=4000kbps, vrf=v1
 ipv4 address=2.2.2.2/24, mask=255.255.255.0, ifcid=792796855
 ipv6 address=4321::2/16, mask=ffff::, ifcid=504992562
 received 31 packets (2018 bytes) dropped 0 packets (0 bytes)
 transmitted 33 packets (2206 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 10 | 10 | 0    | 660 | 660 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 0800  | ip4     | 14 | 14 | 0    | 924  | 924  | 0    |
 | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30   | 30   | 0    |
 | ethtyp | 86dd  | ip6     | 18 | 16 | 0    | 1252 | 1064 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 0     | 1    | 30   |
 | 1     | 14   | 924  |
 | 58    | 18   | 1252 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 33 | 31 | 0    | 2206 | 2018 | 0    |
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
 | 0     | 33  | 33  | 33   | 2206 | 2206 | 2206 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
       12.2k|  #
       11.2k|  #
       10.3k|# #
        9344|# #
        8368|# #
        7392|# #
        6416|# #
        5440|# #
        4464|# #
        3488|####
        2512|#####
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
 | 0022.047d.1f2f | 2.2.2.1 | 00:00:04 | false  |
 |________________|_________|__________|________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 neigh bvi1
r2#show ipv6 neigh bvi1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
 | mac            | address | time     | static | router |
 |----------------|---------|----------|--------|--------|
 | 0022.047d.1f2f | 4321::1 | 00:00:04 | false  | false  |
 |________________|_________|__________|________|________|
r2#
r2#
```

# Example: uti over ipv4

## **Topology diagram**

![topology](/img/conn-uti01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz57r1-log.run
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
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
vpdn er
 bridge-group 1
 proxy p1
 target 1.1.1.2
 vcid 123
 protocol uti
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
logging file debug ../binTmp/zzz57r2-log.run
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
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
vpdn er
 bridge-group 1
 proxy p1
 target 1.1.1.1
 vcid 123
 protocol uti
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
 |~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                               | packet         | byte               |     |
 | iface          | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
 |----------------|------|-------|----|----|------|------|------|------|-----|
 | bvi            | true | true  | 0  | 0  | 0    | 0    | 0    | 0    |     |
 | uti to 1.1.1.1 | true | false | 33 | 33 | 0    | 2206 | 2602 | 0    |     |
 |________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                            | packet         | byte               |
 | addr           | iface          | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|----------------|----------|----|----|------|------|------|------|
 | 003c.2a1e.0c13 | uti to 1.1.1.1 | 00:00:05 | 30 | 33 | 0    | 1952 | 2206 | 0    |
 | 005a.2e4d.225f | bvi            | 00:00:05 | 28 | 33 | 0    | 1848 | 2206 | 0    |
 |________________|________________|__________|____|____|______|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:05, 1 changes)
 description:
 type is bridged, hwaddr=005a.2e4d.225f, mtu=1400, bw=10mbps, vrf=v1
 ip4 address=2.2.2.2/24, netmask=255.255.255.0, ifcid=822481088
 ip6 address=4321::2/16, netmask=ffff::, ifcid=586805305
 received 33 packets (2206 bytes) dropped 0 packets (0 bytes)
 transmitted 33 packets (2206 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 5  | 5  | 0    | 330 | 330 | 0    |
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
 | ethtyp | 86dd  | ip6     | 18 | 18 | 0    | 1252 | 1252 | 0    |
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
 | 0-255      | 33 | 33 | 0    | 2206 | 2206 | 0    |
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
         11k|
         10k|  #
        9395|  #
        8220|  #
        7046|  #
        5872|  #
        4697|# #
        3523|#####
        2348|#####
        1174|#####
           0|#####
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
 | 003c.2a1e.0c13 | 2.2.2.1 | 00:00:04 | false  |
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
 | 003c.2a1e.0c13 | 4321::1                 | 00:00:04 | false  | false  |
 | 003c.2a1e.0c13 | fe80::23c:2aff:fe1e:c13 | 00:00:04 | false  | false  |
 |________________|_________________________|__________|________|________|
r2#
r2#
```
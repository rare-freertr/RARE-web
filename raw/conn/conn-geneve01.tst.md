# Example: geneve over ipv4

## **Topology diagram**

![topology](/img/conn-geneve01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz32r1-log.run
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
vpdn vx
 bridge-group 1
 proxy p1
 target 1.1.1.2
 vcid 123
 protocol geneve
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
logging file debug ../binTmp/zzz32r2-log.run
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
vpdn vx
 bridge-group 1
 proxy p1
 target 1.1.1.1
 vcid 123
 protocol geneve
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
 |~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
 |                                  | packet         | byte               |     |
 | iface             | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
 |-------------------|------|-------|----|----|------|------|------|------|-----|
 | bvi               | true | true  | 0  | 0  | 0    | 0    | 0    | 0    |     |
 | geneve to 1.1.1.1 | true | false | 27 | 27 | 0    | 1802 | 2126 | 0    |     |
 |___________________|______|_______|____|____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                               | packet         | byte               |
 | addr           | iface             | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|-------------------|----------|----|----|------|------|------|------|
 | 0029.090d.3d22 | bvi               | 00:00:03 | 23 | 27 | 0    | 1518 | 1802 | 0    |
 | 007e.1b3a.635c | geneve to 1.1.1.1 | 00:00:03 | 24 | 27 | 0    | 1548 | 1802 | 0    |
 |________________|___________________|__________|____|____|______|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:03, 1 changes)
 description:
 type is bridged, hwaddr=0029.090d.3d22, mtu=1400, bw=4000kbps, vrf=v1
 ip4 address=2.2.2.2/24, netmask=255.255.255.0, ifcid=869375837
 ip6 address=4321::2/16, netmask=ffff::, ifcid=89366634
 received 27 packets (1802 bytes) dropped 0 packets (0 bytes)
 transmitted 27 packets (1802 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 3  | 3  | 0    | 198 | 198 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
 | ethtyp | 0800  | ip4     | 13 | 13 | 0    | 858 | 858 | 0    |
 | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30  | 30  | 0    |
 | ethtyp | 86dd  | ip6     | 13 | 13 | 0    | 914 | 914 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 0     | 1    | 30   |
 | 1     | 13   | 858  |
 | 58    | 13   | 914  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 27 | 27 | 0    | 1802 | 1802 | 0    |
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
 | 0     | 27  | 27  | 27   | 1802 | 1802 | 1802 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        4064|
        3657|  #
        3251|  #
        2844|# #
        2438|# #
        2032|# #
        1625|# #
        1219|# #
         812|# #
         406|###
           0|###
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
 | 007e.1b3a.635c | 2.2.2.1 | 00:00:03 | false  |
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
 | 007e.1b3a.635c | 4321::1                  | 00:00:03 | false  | false  |
 | 007e.1b3a.635c | fe80::27e:1bff:fe3a:635c | 00:00:03 | false  | true   |
 |________________|__________________________|__________|________|________|
r2#
r2#
```

# Example: chain bridged ethernet

## **Topology diagram**

![topology](/img/conn-bridge01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz30r1-log.run
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
logging file debug ../binTmp/zzz30r2-log.run
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz30r3-log.run
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
logging file debug ../binTmp/zzz30r4-log.run
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
 | ethernet1 | true | true | 87  | 78  | 0    | 5712 | 5114 | 0    |     |
 | ethernet2 | true | true | 107 | 107 | 0    | 7012 | 7024 | 0    |     |
 |___________|______|______|_____|_____|______|______|______|______|_____|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                                       | packet         | byte               |
 | addr           | iface     | time     | tx | rx | drop | tx   | rx   | drop |
 |----------------|-----------|----------|----|----|------|------|------|------|
 | 0000.0000.4444 | ethernet2 | 00:00:15 | 48 | 53 | 0    | 3168 | 3494 | 0    |
 | 0001.446c.4e41 | ethernet1 | 00:00:15 | 75 | 78 | 0    | 4854 | 5114 | 0    |
 | 0032.154d.7477 | bvi       | 00:00:15 | 74 | 78 | 0    | 4824 | 5096 | 0    |
 | 005b.3708.5a47 | ethernet2 | 00:00:15 | 48 | 54 | 0    | 3168 | 3530 | 0    |
 |________________|___________|__________|____|____|______|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:15, 1 changes)
 description:
 type is bridged, hwaddr=0032.154d.7477, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=270412531
 ip6 address=1234::2/16, netmask=ffff::, ifcid=258102470
 received 87 packets (5730 bytes) dropped 0 packets (0 bytes)
 transmitted 78 packets (5096 bytes) promisc=false macsec=false
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
 | ethtyp | 0800  | ip4     | 42 | 42 | 0    | 2772 | 2772 | 0    |
 | ethtyp | 0806  | arp4    | 3  | 6  | 0    | 90   | 216  | 0    |
 | ethtyp | 86dd  | ip6     | 33 | 39 | 0    | 2234 | 2742 | 0    |
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
 | 58    | 33   | 2234 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 78 | 87 | 0    | 5096 | 5730 | 0    |
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
 | 0     | 78  | 78  | 78   | 5096 | 5096 | 5096 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         21k|
         19k|   #
         16k|   #
         14k|   #
         12k|   #
         10k|   #   #
        8448|#  #   #      #
        6336|#  #   #      #
        4224|# ## # #    # #
        2112|# ######    ###
           0|# ######  # ###
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
 | 0001.446c.4e41 | 1.1.1.1 | 00:00:14 | false  |
 | 005b.3708.5a47 | 1.1.1.3 | 00:00:14 | false  |
 | 0000.0000.4444 | 1.1.1.4 | 00:00:14 | false  |
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
 | 0001.446c.4e41 | 1234::1                  | 00:00:15 | false  | false  |
 | 005b.3708.5a47 | 1234::3                  | 00:00:15 | false  | false  |
 | 0000.0000.4444 | 1234::4                  | 00:00:15 | false  | false  |
 | 0000.0000.4444 | fe80::200:ff:fe00:4444   | 00:00:15 | false  | true   |
 | 0001.446c.4e41 | fe80::201:44ff:fe6c:4e41 | 00:00:15 | false  | true   |
 | 005b.3708.5a47 | fe80::25b:37ff:fe08:5a47 | 00:00:15 | false  | true   |
 |________________|__________________________|__________|________|________|
r2#
r2#
```

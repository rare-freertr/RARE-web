# Example: bridged mac rewrite

## **Topology diagram**

![topology](/img/conn-bridge14.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
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
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
bridge 1
 mac-learn
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
end
```

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
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
end
```

## **Verification**

```
r2#
r2#
r2#show bridge 1
r2#show bridge 1
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~|~~~~~~|
 | interface | forward | physical | tx    | rx    | drop |
 |-----------|---------|----------|-------|-------|------|
 | bvi       | true    | true     | 0     | 0     | 0    |
 | ethernet1 | true    | true     | 8292  | 7730  | 0    |
 | ethernet2 | true    | true     | 10500 | 10476 | 0    |
 |___________|_________|__________|_______|_______|______|
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | address        | interface | time     | tx   | rx   | drop |
 |----------------|-----------|----------|------|------|------|
 | 0000.0000.4444 | ethernet2 | 00:00:00 | 4912 | 5238 | 0    |
 | 002b.4136.2933 | ethernet2 | 00:00:01 | 4912 | 5238 | 0    |
 | 003b.5d12.4e3a | ethernet1 | 00:00:00 | 7470 | 7730 | 0    |
 | 0062.1223.1b4c | bvi       | 00:00:00 | 7440 | 7712 | 0    |
 |________________|___________|__________|______|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show inter bvi1 full
r2#show inter bvi1 full
bvi1 is up (since 00:00:16, 1 changes)
 description:
 type is bridged, hwaddr=0062.1223.1b4c, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=10011
 ip6 address=1234::2/16, netmask=ffff::, ifcid=10011
 received 86 packets (8310 bytes) dropped 0 packets (0 bytes)
 transmitted 78 packets (7712 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 570  | 570     | 0    | 5    | 5       | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0800  | ip4     | 42 | 42 | 0    | 3948 | 3948 | 0    |
 | ethtyp | 0806  | arp4    | 3  | 5  | 0    | 90   | 180  | 0    |
 | ethtyp | 86dd  | ip6     | 33 | 39 | 0    | 3674 | 4182 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 42   | 3948 |
 | 58    | 33   | 3674 |
 | 0     | 3    | 90   |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 78 | 86 | 0    | 7712 | 8310 | 0    |
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
 | 0     | 78  | 78  | 78   | 7712 | 7712 | 7712 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         25k|
         23k|  #
         20k|  #
         18k|  #
         15k| ###    #
         12k| ###    #
         10k| ###    #
        7728|#### #  #    # #
        5152|####### #    ###
        2576|####### #    ###
           0|#########  # ###
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
 | 003b.5d12.4e3a | 1.1.1.1 | 00:00:15 | false  |
 | 002b.4136.2933 | 1.1.1.3 | 00:00:15 | false  |
 | 0000.0000.4444 | 1.1.1.4 | 00:00:15 | false  |
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
 | 003b.5d12.4e3a | 1234::1                  | 00:00:16 | false  | false  |
 | 002b.4136.2933 | 1234::3                  | 00:00:16 | false  | false  |
 | 0000.0000.4444 | 1234::4                  | 00:00:16 | false  | false  |
 | 0000.0000.4444 | fe80::200:ff:fe00:4444   | 00:00:16 | false  | true   |
 | 002b.4136.2933 | fe80::22b:41ff:fe36:2933 | 00:00:16 | false  | true   |
 | 003b.5d12.4e3a | fe80::23b:5dff:fe12:4e3a | 00:00:16 | false  | true   |
 |________________|__________________________|__________|________|________|
r2#
r2#
```

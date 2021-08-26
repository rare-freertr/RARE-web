# Example: nsh over ethernet

## **Topology diagram**

![topology](/img/mpls-nsh01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz24r1-log.run
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1111::1 ffff::
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
logging file debug ../binTmp/zzz24r2-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 no description
 nsh enable
 nsh xconnect 2 255
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 nsh enable
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
nsh 2 255 interface ethernet2 0000.1111.2222
!
nsh 3 254 interface ethernet1 0000.1111.2222 rawpack keephdr
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
logging file debug ../binTmp/zzz24r3-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 no description
 nsh enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 nsh enable
 nsh xconnect 3 255
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
nsh 2 254 interface ethernet2 0000.1111.2222 rawpack keephdr
!
nsh 3 255 interface ethernet1 0000.1111.2222
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
logging file debug ../binTmp/zzz24r4-log.run
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
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff::
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
r2#show inter eth1 full
r2#show inter eth1 full
ethernet1 is promisc, up (since 00:00:03, 1 changes)
 description:
 type is ethernet, hwaddr=0000.0000.2222, mtu=1500, bw=100mbps
 received 28 packets (1874 bytes) dropped 0 packets (0 bytes)
 transmitted 28 packets (1874 bytes) promisc=true macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 4  | 4  | 0    | 264 | 264 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | ffff  | nshx    | 0  | 28 | 0    | 0    | 1874 | 0    |
 | ethtyp | 894f  | nsh     | 28 | 0  | 0    | 1874 | 0    | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 3     | 28   | 1874 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 28 | 28 | 0    | 1874 | 1874 | 0    |
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
 | 0     | 28  | 28  | 28   | 1874 | 1874 | 1874 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        4640|
        4176|##
        3712|##
        3248|##
        2784|##
        2320|##
        1856|##
        1392|##
         928|##
         464|##
           0|##
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
r2#sh
r2#sh
r2#show inter eth2 full
r2#show inter eth2 full
ethernet2 is up (since 00:00:03, 1 changes)
 description:
 type is ethernet, hwaddr=0000.0000.2222, mtu=1500, bw=100mbps
 received 28 packets (2490 bytes) dropped 0 packets (0 bytes)
 transmitted 28 packets (2490 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |       | packet         | byte               |
 | time  | tx | rx | drop | tx   | rx   | drop |
 |-------|----|----|------|------|------|------|
 | 1sec  | 20 | 20 | 0    | 1760 | 1760 | 0    |
 | 1min  | 0  | 0  | 0    | 0    | 0    | 0    |
 | 1hour | 0  | 0  | 0    | 0    | 0    | 0    |
 |_______|____|____|______|______|______|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 894f  | nsh     | 28 | 28 | 0    | 2490 | 2490 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 3     | 28   | 2490 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 28 | 28 | 0    | 2490 | 2490 | 0    |
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
 | 0     | 28  | 28  | 28   | 2490 | 2490 | 2490 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         28k|
         25k|#
         22k|#
         19k|#
         16k|#
         14k|#
         11k|#
        8448|#
        5632|# #
        2816|###
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
r2#show nsh for
r2#show nsh for
 |~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~|
 | sp | si  | target                             | bytes |
 |----|-----|------------------------------------|-------|
 | 2  | 255 | interface ethernet2 0000.1111.2222 | 2210  |
 | 3  | 254 | interface ethernet1 0000.1111.2222 | 2210  |
 |____|_____|____________________________________|_______|
r2#
r2#
```

```
r2#
r2#
r2#show nsh for 2 255
r2#show nsh for 2 255
 |~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category  | value                        |
 |-----------|------------------------------|
 | path      | 2                            |
 | index     | 255                          |
 | out path  | 2                            |
 | out index | 254                          |
 | iface     | ethernet2                    |
 | target    | 0000.1111.2222               |
 | route     | null null                    |
 | rawpack   | false                        |
 | keephdr   | false                        |
 | counter   | tx=0(0) rx=2210(28) drp=0(0) |
 |___________|______________________________|
r2#
r2#
```

```
r2#
r2#
r2#show nsh for 3 254
r2#show nsh for 3 254
 |~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category  | value                        |
 |-----------|------------------------------|
 | path      | 3                            |
 | index     | 254                          |
 | out path  | 3                            |
 | out index | 253                          |
 | iface     | ethernet1                    |
 | target    | 0000.1111.2222               |
 | route     | null null                    |
 | rawpack   | true                         |
 | keephdr   | true                         |
 | counter   | tx=0(0) rx=2210(28) drp=0(0) |
 |___________|______________________________|
r2#
r2#
```

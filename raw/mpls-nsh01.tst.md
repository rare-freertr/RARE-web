# Example: nsh over ethernet

## **Topology diagram**

![topology](/img/mpls-nsh01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz46r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz46r2-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 nsh enable
 nsh xconnect 2 255
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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
logging file debug ../binTmp/zzz46r3-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 nsh enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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
logging file debug ../binTmp/zzz46r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
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
ethernet1 is up, promisc
 description:
 state changed 3 times, last at 2022-05-02 21:08:27, 00:00:07 ago
 last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
 type is ethernet, hwaddr=0000.0000.2222, mtu=1500, bw=100mbps
 received 34 packets (2286 bytes) dropped 0 packets (0 bytes)
 transmitted 30 packets (1966 bytes) macsec=false sgt=false
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
 | ethtyp | ffff  | nshx    | 0  | 34 | 0    | 0    | 2286 | 0    |
 | ethtyp | 894f  | nsh     | 30 | 0  | 0    | 1966 | 0    | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 3     | 30   | 1966 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 30 | 34 | 0    | 1966 | 2286 | 0    |
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
 | 0     | 30  | 30  | 30   | 1966 | 1966 | 1966 |
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
        3876|  # #
        3230|  # #
        2584|# # #
        1938|# # #
        1292|### ###
         646|### ###
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
r2#show inter eth2 full
r2#show inter eth2 full
ethernet2 is up
 description:
 state changed 3 times, last at 2022-05-02 21:08:27, 00:00:07 ago
 last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
 type is ethernet, hwaddr=0000.0000.2222, mtu=1500, bw=100mbps
 received 30 packets (2626 bytes) dropped 0 packets (0 bytes)
 transmitted 34 packets (3034 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 3  | 3  | 0    | 264 | 264 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |                          | packet         | byte               |
 | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
 |--------|-------|---------|----|----|------|------|------|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 894f  | nsh     | 34 | 30 | 0    | 3034 | 2626 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 3     | 34   | 3034 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 34 | 30 | 0    | 3034 | 2626 | 0    |
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
 | 0     | 34  | 34  | 34   | 3034 | 3034 | 3034 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        8570|  #
        7713|  #
        6856|  #
        5999|  #
        5142|  # #
        4285|  # #
        3428|# # #
        2571|# # #
        1714|### ###
         857|### ###
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
r2#show nsh for
r2#show nsh for
 |~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~|
 | sp | si  | target                             | bytes |
 |----|-----|------------------------------------|-------|
 | 2  | 255 | interface ethernet2 0000.1111.2222 | 2694  |
 | 3  | 254 | interface ethernet1 0000.1111.2222 | 2326  |
 |____|_____|____________________________________|_______|
r2#
r2#
```

```
r2#
r2#
r2#show nsh for 2 255
r2#show nsh for 2 255
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category         | value                                                |
 |------------------|------------------------------------------------------|
 | path             | 2                                                    |
 | index            | 255                                                  |
 | out path         | 2                                                    |
 | out index        | 254                                                  |
 | iface            | ethernet2                                            |
 | target           | 0000.1111.2222                                       |
 | route            | null null                                            |
 | rawpack          | false                                                |
 | keephdr          | false                                                |
 | counter          | tx=0(0) rx=2694(34) drp=0(0)                         |
 | lastio           | input 00:00:00 ago, output never ago, drop never ago |
 | hardware counter | null                                                 |
 |__________________|______________________________________________________|
r2#
r2#
```

```
r2#
r2#
r2#show nsh for 3 254
r2#show nsh for 3 254
 |~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category         | value                                                |
 |------------------|------------------------------------------------------|
 | path             | 3                                                    |
 | index            | 254                                                  |
 | out path         | 3                                                    |
 | out index        | 253                                                  |
 | iface            | ethernet1                                            |
 | target           | 0000.1111.2222                                       |
 | route            | null null                                            |
 | rawpack          | true                                                 |
 | keephdr          | true                                                 |
 | counter          | tx=0(0) rx=2326(30) drp=0(0)                         |
 | lastio           | input 00:00:00 ago, output never ago, drop never ago |
 | hardware counter | null                                                 |
 |__________________|______________________________________________________|
r2#
r2#
```

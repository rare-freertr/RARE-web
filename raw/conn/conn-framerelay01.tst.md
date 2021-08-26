# Example: framerelay ansi

## **Topology diagram**

![topology](/img/conn-framerelay01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz27r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation framerelay
 framerelay mode dce
 framerelay dlci 123
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
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
logging file debug ../binTmp/zzz27r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation framerelay
 framerelay mode dte
 framerelay dlci 123
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
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
r1#
r1#
r1#show inter ser1 full
r1#show inter ser1 full
serial1 is up (since 00:00:02, 2 changes)
 description:
 type is serial, hwaddr=none, mtu=1498, bw=2000kbps, vrf=v1
 ip4 address=1.1.1.1/24, netmask=255.255.255.0, ifcid=544027268
 ip6 address=1234::1/16, netmask=ffff::, ifcid=351335869
 received 27 packets (1814 bytes) dropped 4 packets (296 bytes)
 transmitted 24 packets (1584 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 4  | 4  | 0    | 264 | 264 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
 | ethtyp | 0800  | ip4     | 15 | 14 | 0    | 990 | 924 | 0    |
 | ethtyp | 86dd  | ip6     | 13 | 13 | 0    | 890 | 890 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 14   | 924  |
 | 58    | 10   | 660  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 24 | 27 | 0    | 1584 | 1814 | 0    |
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
 | 0     | 24  | 24  | 24   | 1584 | 1584 | 1584 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
        4224|
        3801|##
        3379|##
        2956|##
        2534|##
        2112|##
        1689|##
        1267|##
         844|##
         422|##
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
r1#
r1#
```

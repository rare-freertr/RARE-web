# Example: raw encapsulation

## **Topology diagram**

![topology](/img/conn-raw.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz87r1-log.run
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
 encapsulation raw
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
logging file debug ../binTmp/zzz87r2-log.run
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
 encapsulation raw
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
serial1 is up (since 00:00:01, 1 changes)
 description:
 type is serial, hwaddr=none, mtu=1500, bw=2000kbps, vrf=v1
 ip4 address=1.1.1.1/24, netmask=255.255.255.0, ifcid=626470391
 ip6 address=1234::1/16, netmask=ffff::, ifcid=174397974
 received 23 packets (1550 bytes) dropped 0 packets (0 bytes)
 transmitted 23 packets (1550 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~|~~~~|~~~~~~|
 |       | packet         | byte           |
 | time  | tx | rx | drop | tx | rx | drop |
 |-------|----|----|------|----|----|------|
 | 1sec  | 0  | 0  | 0    | 0  | 0  | 0    |
 | 1min  | 0  | 0  | 0    | 0  | 0  | 0    |
 | 1hour | 0  | 0  | 0    | 0  | 0  | 0    |
 |_______|____|____|______|____|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
 | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 660 | 660 | 0    |
 | ethtyp | 86dd  | ip6     | 13 | 13 | 0    | 890 | 890 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 10   | 660  |
 | 58    | 13   | 890  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 23 | 23 | 0    | 1550 | 1550 | 0    |
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
 | 0     | 23  | 23  | 23   | 1550 | 1550 | 1550 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
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

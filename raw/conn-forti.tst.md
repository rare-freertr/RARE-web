# Example: ppp over forti

## **Topology diagram**

![topology](/img/conn-forti.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz71r1-log.run
!
aaa userlist usr
 username c
 username c password $v10$Yw==
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface dialer1
 encapsulation ppp
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 2222::1 ffff:ffff:ffff:ffff::
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
server http h
 host * path /
 host * forti dialer1
 host * authentication usr
 vrf v1
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
logging file debug ../binTmp/zzz71r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface dialer1
 encapsulation ppp
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 2222::2 ffff:ffff:ffff:ffff::
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
vpdn forti
 interface dialer1
 proxy p1
 target http://1.1.1.1/
 username c
 password $v10$Yw==
 protocol forti
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
r2#show inter dia1 full
r2#show inter dia1 full
dialer1 is up
 description:
 state changed 3 times, last at 2022-05-02 21:12:22, 00:00:00 ago
 last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
 type is dialer, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
 ipv4 address=2.2.2.2/24, mask=255.255.255.0, ifcid=613358297
 ipv6 address=2222::2/64, mask=ffff:ffff:ffff:ffff::, ifcid=716464043
 received 13 packets (890 bytes) dropped 0 packets (0 bytes)
 transmitted 13 packets (890 bytes) macsec=false sgt=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet         | byte             |
 | time  | tx | rx | drop | tx  | rx  | drop |
 |-------|----|----|------|-----|-----|------|
 | 1sec  | 13 | 13 | 0    | 890 | 890 | 0    |
 | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
 |_______|____|____|______|_____|_____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
 | ethtyp | 0800  | ip4     | 5  | 5  | 0    | 330 | 330 | 0    |
 | ethtyp | 86dd  | ip6     | 8  | 8  | 0    | 560 | 560 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 5    | 330  |
 | 58    | 8    | 560  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |            | packet         | byte             |
 | size       | tx | rx | drop | tx  | rx  | drop |
 |------------|----|----|------|-----|-----|------|
 | 0-255      | 13 | 13 | 0    | 890 | 890 | 0    |
 | 256-511    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 512-767    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 768-1023   | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0   | 0   | 0    |
 |____________|____|____|______|_____|_____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet           | byte             |
 | class | cos | exp | prec | cos | exp | prec |
 |-------|-----|-----|------|-----|-----|------|
 | 0     | 13  | 13  | 13   | 890 | 890 | 890  |
 | 1     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 2     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 3     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 4     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 5     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 6     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 7     | 0   | 0   | 0    | 0   | 0   | 0    |
 |_______|_____|_____|______|_____|_____|______|
       14.2k|#
       12.8k|#
       11.3k|#
        9968|#
        8544|#
        7120|#
        5696|#
        4272|#
        2848|#
        1424|#
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

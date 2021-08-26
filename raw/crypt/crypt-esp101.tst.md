# Example: ipv4 in esp over ipv4

## **Topology diagram**

![topology](/img/crypt-esp101.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz67r1-log.run
!
crypto ipsec ips
 group 02
 cipher des
 hash md5
 seconds 3600
 bytes 1024000
 key $v10$dGVzdGVy
 exit
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
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel protection ips
 tunnel source ethernet1
 tunnel destination 1.1.1.2
 tunnel mode ipsec
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff::
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
logging file debug ../binTmp/zzz67r2-log.run
!
crypto ipsec ips
 group 02
 cipher des
 hash md5
 seconds 3600
 bytes 1024000
 key $v10$dGVzdGVy
 exit
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
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel protection ips
 tunnel source ethernet1
 tunnel destination 1.1.1.1
 tunnel mode ipsec
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
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
r1#show inter tun1 full
r1#show inter tun1 full
tunnel1 is up (since 00:00:12, 1 changes)
 description:
 type is ipsec, hwaddr=none, mtu=65479, bw=1000mbps, vrf=v1
 ip4 address=2.2.2.1/24, netmask=255.255.255.0, ifcid=375182821
 ip6 address=4321::1/16, netmask=ffff::, ifcid=685137968
 received 14 packets (924 bytes) dropped 0 packets (0 bytes)
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
 | ethtyp | 0800  | ip4     | 15 | 14 | 0    | 990 | 924 | 0    |
 | ethtyp | 86dd  | ip6     | 8  | 0  | 0    | 560 | 0   | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 15   | 990  |
 | 58    | 8    | 560  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~~|
 |            | packet         | byte              |
 | size       | tx | rx | drop | tx   | rx  | drop |
 |------------|----|----|------|------|-----|------|
 | 0-255      | 23 | 14 | 0    | 1550 | 924 | 0    |
 | 256-511    | 0  | 0  | 0    | 0    | 0   | 0    |
 | 512-767    | 0  | 0  | 0    | 0    | 0   | 0    |
 | 768-1023   | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0    | 0   | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0    | 0   | 0    |
 |____________|____|____|______|______|_____|______|
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
         11k|
        9979|         #
        8870|         #
        7761|         #
        6652|         #
        5544|         #
        4435|         #
        3326|         ##
        2217|         ###
        1108|         ###
           0|     #######
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

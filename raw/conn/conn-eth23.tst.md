# Example: secondary addresses over ethernet

## **Topology diagram**

![topology](/img/conn-eth23.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz30r1-log.run
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
 ipv4 secondary-address 1.1.1.111
 ipv4 secondary-address 1.1.1.112
 ipv4 secondary-address 1.1.1.113
 ipv6 address 1234::1 ffff::
 ipv6 secondary-address 1234::111
 ipv6 secondary-address 1234::112
 ipv6 secondary-address 1234::113
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
r1#show inter eth1 full
r1#show inter eth1 full
ethernet1 is promisc, up (since 00:00:19, 1 changes)
 description:
 type is ethernet, hwaddr=0000.0000.1111, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=1.1.1.1/24, netmask=255.255.255.0, ifcid=937356438
 ip6 address=1234::1/16, netmask=ffff::, ifcid=389290449
 received 90 packets (5852 bytes) dropped 0 packets (0 bytes)
 transmitted 96 packets (6172 bytes) promisc=true macsec=false
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
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
 | ethtyp | 0800  | ip4     | 41 | 41 | 0    | 2706 | 2706 | 0    |
 | ethtyp | 0806  | arp4    | 7  | 4  | 0    | 210  | 144  | 0    |
 | ethtyp | 86dd  | ip6     | 48 | 45 | 0    | 3256 | 3002 | 0    |
 |________|_______|_________|____|____|______|______|______|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 0     | 7    | 210  |
 | 1     | 41   | 2706 |
 | 58    | 48   | 3256 |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
 |            | packet         | byte               |
 | size       | tx | rx | drop | tx   | rx   | drop |
 |------------|----|----|------|------|------|------|
 | 0-255      | 96 | 90 | 0    | 6172 | 5852 | 0    |
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
 | 0     | 96  | 96  | 96   | 6172 | 6172 | 6172 |
 | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
 | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
 |_______|_____|_____|______|______|______|______|
         11k|
         10k|            # #
        9395|            # #
        8220|            # #
        7046|            # #
        5872| # # #      # #
        4697| # # # # #  # #
        3523|########## #####
        2348|########## #####
        1174|########## #######
           0|########## #######
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

```
r1#
r1#
r1#show ipv4 arp eth1
r1#show ipv4 arp eth1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
 | mac            | address | time     | static |
 |----------------|---------|----------|--------|
 | 0000.0000.2222 | 1.1.1.2 | 00:00:17 | false  |
 |________________|_________|__________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 neigh eth1
r1#show ipv6 neigh eth1
 |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
 | mac            | address                | time     | static | router |
 |----------------|------------------------|----------|--------|--------|
 | 0000.0000.2222 | 1234::2                | 00:00:17 | false  | false  |
 | 0000.0000.2222 | fe80::200:ff:fe00:2222 | 00:00:17 | false  | false  |
 |________________|________________________|__________|________|________|
r1#
r1#
```
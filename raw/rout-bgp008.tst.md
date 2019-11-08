# Example: ibgp rr in subnet

## **Topology diagram**

![topology](/img/rout-bgp008.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 route-reflector-client
 neighbor 1.1.1.3 remote-as 1
 no neighbor 1.1.1.3 description
 neighbor 1.1.1.3 local-as 1
 neighbor 1.1.1.3 address-family unicast
 neighbor 1.1.1.3 distance 200
 neighbor 1.1.1.3 route-reflector-client
 neighbor 1.1.1.4 remote-as 1
 no neighbor 1.1.1.4 description
 neighbor 1.1.1.4 local-as 1
 neighbor 1.1.1.4 address-family unicast
 neighbor 1.1.1.4 distance 200
 neighbor 1.1.1.4 route-reflector-client
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234:1::2 remote-as 1
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 200
 neighbor 1234:1::2 route-reflector-client
 neighbor 1234:1::3 remote-as 1
 no neighbor 1234:1::3 description
 neighbor 1234:1::3 local-as 1
 neighbor 1234:1::3 address-family unicast
 neighbor 1234:1::3 distance 200
 neighbor 1234:1::3 route-reflector-client
 neighbor 1234:1::4 remote-as 1
 no neighbor 1234:1::4 description
 neighbor 1234:1::4 local-as 1
 neighbor 1234:1::4 address-family unicast
 neighbor 1234:1::4 distance 200
 neighbor 1234:1::4 route-reflector-client
 redistribute connected
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
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
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.2
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.2
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 200
 redistribute connected
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234:1::3 ffff:ffff::
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
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 200
 redistribute connected
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234:1::4 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.4
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 200
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.4
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 200
 redistribute connected
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
r1#
r1#
r1#show ipv4 bgp 1 sum
r1#show ipv4 bgp 1 sum
 |~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | afis    | ready | neighbor | uptime   |
 |----|---------|-------|----------|----------|
 | 1  | unicast | true  | 1.1.1.2  | 00:00:16 |
 | 1  | unicast | true  | 1.1.1.3  | 00:00:13 |
 | 1  | unicast | true  | 1.1.1.4  | 00:00:09 |
 |____|_________|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 sum
r1#show ipv6 bgp 1 sum
 |~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | as | afis    | ready | neighbor  | uptime   |
 |----|---------|-------|-----------|----------|
 | 1  | unicast | true  | 1234:1::2 | 00:00:21 |
 | 1  | unicast | true  | 1234:1::3 | 00:00:18 |
 | 1  | unicast | true  | 1234:1::4 | 00:00:21 |
 |____|_________|_______|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 group
r1#show ipv4 bgp 1 group
 |~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | as | group | neighbor | uptime   |
 |----|-------|----------|----------|
 | 1  | 0     | 1.1.1.2  | 00:00:16 |
 | 1  | 0     | 1.1.1.3  | 00:00:13 |
 | 1  | 0     | 1.1.1.4  | 00:00:09 |
 |____|_______|__________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 group
r1#show ipv6 bgp 1 group
 |~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | as | group | neighbor  | uptime   |
 |----|-------|-----------|----------|
 | 1  | 0     | 1234:1::2 | 00:00:22 |
 | 1  | 0     | 1234:1::3 | 00:00:18 |
 | 1  | 0     | 1234:1::4 | 00:00:22 |
 |____|_______|___________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 group 0 uni
r1#show ipv4 bgp 1 group 0 uni
 |~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|
 | prefix     | hop     | metric      | aspath |
 |------------|---------|-------------|--------|
 | 1.1.1.0/24 | 1.1.1.1 | 0/100/0/0   |        |
 | 2.2.2.1/32 | 1.1.1.1 | 0/100/0/0   |        |
 | 2.2.2.2/32 | 1.1.1.2 | 200/100/0/0 |        |
 | 2.2.2.3/32 | 1.1.1.3 | 200/100/0/0 |        |
 | 2.2.2.4/32 | 1.1.1.4 | 200/100/0/0 |        |
 |____________|_________|_____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 group 0 uni
r1#show ipv6 bgp 1 group 0 uni
 |~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|
 | prefix      | hop       | metric      | aspath |
 |-------------|-----------|-------------|--------|
 | 1234:1::/32 | 1234:1::1 | 0/100/0/0   |        |
 | 4321::1/128 | 1234:1::1 | 0/100/0/0   |        |
 | 4321::2/128 | 1234:1::2 | 200/100/0/0 |        |
 | 4321::3/128 | 1234:1::3 | 200/100/0/0 |        |
 | 4321::4/128 | 1234:1::4 | 200/100/0/0 |        |
 |_____________|___________|_____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 best
r1#show ipv4 bgp 1 best
 |~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category        | value                              |
 |-----------------|------------------------------------|
 | version         | 10                                 |
 | full run        | 6 times                            |
 | full last       | 2019-11-07 13:25:24 (00:00:09 ago) |
 | full time       | 1 ms                               |
 | incr run        | 3 times                            |
 | incr last       | 2019-11-07 13:25:24 (00:00:09 ago) |
 | incr time       | 1 ms                               |
 | changes         | 2, total=6                         |
 | rpki table      | 0                                  |
 | unicast table   | 3, list=0                          |
 | multicast table | 0, list=0                          |
 | other table     | 0, list=0                          |
 | flowspec table  | 0, list=0                          |
 | vpnuni table    | 0, list=0                          |
 | vpnmlt table    | 0, list=0                          |
 | vpnflw table    | 0, list=0                          |
 | ovpnuni table   | 0, list=0                          |
 | ovpnmlt table   | 0, list=0                          |
 | ovpnflw table   | 0, list=0                          |
 | vpls table      | 0, list=0                          |
 | mspw table      | 0, list=0                          |
 | evpn table      | 0, list=0                          |
 | mdt table       | 0, list=0                          |
 | srte table      | 0, list=0                          |
 | mvpn table      | 0, list=0                          |
 | omvpn table     | 0, list=0                          |
 |_________________|____________________________________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 best
r1#show ipv6 bgp 1 best
 |~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | category        | value                              |
 |-----------------|------------------------------------|
 | version         | 10                                 |
 | full run        | 6 times                            |
 | full last       | 2019-11-07 13:25:15 (00:00:19 ago) |
 | full time       | 1 ms                               |
 | incr run        | 3 times                            |
 | incr last       | 2019-11-07 13:25:15 (00:00:19 ago) |
 | incr time       | 0 ms                               |
 | changes         | 2, total=6                         |
 | rpki table      | 0                                  |
 | unicast table   | 3, list=0                          |
 | multicast table | 0, list=0                          |
 | other table     | 0, list=0                          |
 | flowspec table  | 0, list=0                          |
 | vpnuni table    | 0, list=0                          |
 | vpnmlt table    | 0, list=0                          |
 | vpnflw table    | 0, list=0                          |
 | ovpnuni table   | 0, list=0                          |
 | ovpnmlt table   | 0, list=0                          |
 | ovpnflw table   | 0, list=0                          |
 | vpls table      | 0, list=0                          |
 | mspw table      | 0, list=0                          |
 | evpn table      | 0, list=0                          |
 | mdt table       | 0, list=0                          |
 | srte table      | 0, list=0                          |
 | mvpn table      | 0, list=0                          |
 | omvpn table     | 0, list=0                          |
 |_________________|____________________________________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 route v1
r1#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:10 |
 | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:10 |
 | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:10 |
 | B   | 2.2.2.2/32 | 200/0  | ethernet1 | 1.1.1.2 | 00:00:18 |
 | B   | 2.2.2.3/32 | 200/0  | ethernet1 | 1.1.1.3 | 00:00:15 |
 | B   | 2.2.2.4/32 | 200/0  | ethernet1 | 1.1.1.4 | 00:00:10 |
 |_____|____________|________|___________|_________|__________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 route v1
r1#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix        | metric | iface     | hop       | time     |
 |-----|---------------|--------|-----------|-----------|----------|
 | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:20 |
 | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:20 |
 | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:20 |
 | B   | 4321::2/128   | 200/0  | ethernet1 | 1234:1::2 | 00:00:23 |
 | B   | 4321::3/128   | 200/0  | ethernet1 | 1234:1::3 | 00:00:20 |
 | B   | 4321::4/128   | 200/0  | ethernet1 | 1234:1::4 | 00:00:23 |
 |_____|_______________|________|___________|___________|__________|
r1#
r1#
```

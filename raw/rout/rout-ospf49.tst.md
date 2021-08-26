# Example: ospf with bgp linkstate

## **Topology diagram**

![topology](/img/rout-ospf49.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz51r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 0 enable
 justadvert loopback1
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 justadvert loopback1
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.101 255.255.255.255
 ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234::1 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast linkstate
 linkstate ospf4 1 0
 neighbor 1.1.1.2 remote-as 2
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast linkstate
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 linkstate
 justadvert loopback2
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast linkstate
 linkstate ospf6 1 0
 neighbor 1234::2 remote-as 2
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family unicast linkstate
 neighbor 1234::2 distance 20
 neighbor 1234::2 linkstate
 justadvert loopback2
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
logging file debug ../binTmp/zzz51r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.2
 traffeng-id 0.0.0.0
 area 0 enable
 justadvert loopback1
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 justadvert loopback1
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.102 255.255.255.255
 ipv6 address 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234::2 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast linkstate
 linkstate ospf4 1 0
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast linkstate
 neighbor 1.1.1.1 distance 20
 neighbor 1.1.1.1 linkstate
 justadvert loopback2
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 address-family unicast linkstate
 linkstate ospf6 1 0
 neighbor 1234::1 remote-as 1
 no neighbor 1234::1 description
 neighbor 1234::1 local-as 2
 neighbor 1234::1 address-family unicast linkstate
 neighbor 1234::1 distance 20
 neighbor 1234::1 linkstate
 justadvert loopback2
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
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | area | address | routerid | state | uptime   |
 |-----------|------|---------|----------|-------|----------|
 | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | 4     | 00:00:04 |
 |___________|______|_________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 nei
r2#show ipv6 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | area | address | routerid | state | uptime   |
 |-----------|------|---------|----------|-------|----------|
 | ethernet1 | 0    | 1234::1 | 6.6.6.1  | 4     | 00:00:04 |
 |___________|______|_________|__________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid   | sequence | type       | len | time     |
 |----------|---------|----------|------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1 | 80000004 | router     | 28  | 00:00:04 |
 | 4.4.4.2  | 4.4.4.2 | 80000004 | router     | 28  | 00:00:04 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal | 16  | 00:00:04 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal | 16  | 00:00:05 |
 |__________|_________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid      | sequence | type       | len | time     |
 |----------|------------|----------|------------|-----|----------|
 | 6.6.6.1  | 857967142  | 80000001 | link       | 24  | 00:00:05 |
 | 6.6.6.2  | 1058247395 | 80000001 | link       | 24  | 00:00:05 |
 | 6.6.6.1  | 0          | 80000003 | router     | 20  | 00:00:05 |
 | 6.6.6.2  | 0          | 80000003 | router     | 20  | 00:00:02 |
 | 6.6.6.1  | 857967142  | 80000001 | prefix     | 20  | 00:00:05 |
 | 6.6.6.2  | 1058247395 | 80000001 | prefix     | 20  | 00:00:05 |
 | 6.6.6.1  | 0          | 80000001 | asExternal | 28  | 00:00:05 |
 | 6.6.6.2  | 0          | 80000001 | asExternal | 28  | 00:00:05 |
 |__________|____________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
`--4.4.4.2
   `--4.4.4.1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
`--6.6.6.2/00000000
   `--6.6.6.1/00000000
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric | iface     | hop     | time     |
 |------|--------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:05 |
 | LOC  | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:05 |
 | O E2 | 2.2.2.1/32   | 110/0  | ethernet1 | 1.1.1.1 | 00:00:05 |
 | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:06 |
 | B    | 2.2.2.101/32 | 20/0   | ethernet1 | 1.1.1.1 | 00:00:02 |
 | C    | 2.2.2.102/32 | 0/0    | loopback2 | null    | 00:00:06 |
 |______|______________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix        | metric | iface     | hop     | time     |
 |------|---------------|--------|-----------|---------|----------|
 | C    | 1234::/16     | 0/0    | ethernet1 | null    | 00:00:06 |
 | LOC  | 1234::2/128   | 0/1    | ethernet1 | null    | 00:00:06 |
 | O E2 | 4321::1/128   | 110/0  | ethernet1 | 1234::1 | 00:00:02 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null    | 00:00:06 |
 | B    | 4321::101/128 | 20/0   | ethernet1 | 1234::1 | 00:00:02 |
 | C    | 4321::102/128 | 0/0    | loopback2 | null    | 00:00:06 |
 |______|_______________|________|___________|_________|__________|
r2#
r2#
```

```
r1#
r1#
r1#show ipv4 bgp 1 uni dat
r1#show ipv4 bgp 1 uni dat
 |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix       | hop     | metric     | aspath |
 |--------------|---------|------------|--------|
 | 2.2.2.102/32 | 1.1.1.2 | 20/100/0/0 | 2      |
 |______________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 uni dat
r1#show ipv6 bgp 1 uni dat
 |~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix        | hop     | metric     | aspath |
 |---------------|---------|------------|--------|
 | 4321::102/128 | 1234::2 | 20/100/0/0 | 2      |
 |_______________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv4 bgp 1 links dat
r1#show ipv4 bgp 1 links dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                                      | hop     | metric     | aspath |
 |---------------------------------------------|---------|------------|--------|
 | 11a:3c27:4a29:359a:41ea:11a3:db56:ee23/128  | 1.1.1.2 | 20/100/0/0 | 2      |
 | 1207:95c8:9082:49e9:a38f:83d1:a15d:3811/128 | null    | 0/0/0/0    |        |
 | 2066:2eb9:85ce:eb29:45d7:c306:e60c:ad9d/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 42da:c210:bec7:6f85:64b6:c594:d219:eedc/128 | null    | 0/0/0/0    |        |
 | 79e3:a371:a1cd:8ec:e871:5e1:7fa8:86ce/128   | null    | 0/0/0/0    |        |
 | 86db:9f2c:5dd0:ea3c:bb5c:48e5:8582:18ff/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 898e:d222:b783:565:9b88:122d:fc85:e8d/128   | 1.1.1.2 | 20/100/0/0 | 2      |
 | 9995:e117:1c50:c969:8161:6219:d28c:c1b8/128 | null    | 0/0/0/0    |        |
 | 99f2:bfe2:9c2f:b905:f66d:cede:ba54:e8fd/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 9bb4:39f7:ff97:8b9d:ef2:9878:861b:d5a2/128  | null    | 0/0/0/0    |        |
 | a16b:7551:35fa:ebd3:8ff5:be93:e374:e4f1/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | b9c6:39ad:2ddd:5708:c760:bda1:6164:c541/128 | null    | 0/0/0/0    |        |
 | d447:f77a:75a3:c3fd:58f9:f57c:7a16:a2de/128 | null    | 0/0/0/0    |        |
 | d54a:5476:fd35:942a:5375:e6c3:1fc9:f3c8/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | e75f:d9f:f184:b5d7:6fc0:9202:2d46:268e/128  | null    | 0/0/0/0    |        |
 | fe29:a7e8:9291:2653:9087:8ddb:fc29:bae3/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 |_____________________________________________|_________|____________|________|
r1#
r1#
```

```
r1#
r1#
r1#show ipv6 bgp 1 links dat
r1#show ipv6 bgp 1 links dat
 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
 | prefix                                      | hop     | metric     | aspath |
 |---------------------------------------------|---------|------------|--------|
 | 1ac:a12f:b68e:5b4:6b30:5105:8482:e222/128   | null    | 0/0/0/0    |        |
 | 417:fdb4:21a:bec6:b6e5:901e:4344:63db/128   | null    | 0/0/0/0    |        |
 | deb:8d9e:8f15:e32:1fac:3901:d725:cadb/128   | null    | 0/0/0/0    |        |
 | 1673:faf4:64be:d50c:efd9:c83:45e4:1795/128  | null    | 0/0/0/0    |        |
 | 167e:22cc:e1a4:6082:13a9:d0d:43da:f97c/128  | 1234::2 | 20/100/0/0 | 2      |
 | 1e15:d93a:c114:9280:d4fc:df1b:98cb:9ea3/128 | 1234::2 | 20/100/0/0 | 2      |
 | 3e7f:9c96:b17:52:96d3:f0db:ea1d:bc52/128    | null    | 0/0/0/0    |        |
 | 4a71:fb79:b4c3:60ae:7dfc:9261:6eea:96e8/128 | 1234::2 | 20/100/0/0 | 2      |
 | 5ac6:c75a:ee87:f808:5ec7:7048:37df:3df9/128 | null    | 0/0/0/0    |        |
 | 5c78:c9f8:f125:8b2e:c156:2053:ca6c:d551/128 | 1234::2 | 20/100/0/0 | 2      |
 | 6a30:dc85:7547:649b:30a8:83ce:9a07:24c3/128 | null    | 0/0/0/0    |        |
 | 7ab5:c342:dbda:a906:6019:d82f:c44d:c304/128 | null    | 0/0/0/0    |        |
 | 81a8:659e:fb1a:7ed2:40b6:80d4:6258:647f/128 | 1234::2 | 20/100/0/0 | 2      |
 | b226:7c28:d2bd:1112:32c7:1366:4d31:f3d8/128 | 1234::2 | 20/100/0/0 | 2      |
 | e7b2:80d4:f88:5aea:80d0:9b37:d4b1:5a0/128   | 1234::2 | 20/100/0/0 | 2      |
 | fd43:5442:10f8:cd77:6b23:6878:64e2:5d0/128  | 1234::2 | 20/100/0/0 | 2      |
 |_____________________________________________|_________|____________|________|
r1#
r1#
```

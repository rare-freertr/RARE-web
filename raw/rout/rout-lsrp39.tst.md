# Example: lsrp with bgp linkstate

## **Topology diagram**

![topology](/img/rout-lsrp39.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz47r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.1
 justadvert loopback1
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
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
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast linkstate
 linkstate lsrp4 1 0
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
 linkstate lsrp6 1 0
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
logging file debug ../binTmp/zzz47r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.2
 justadvert loopback1
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
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
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 address-family unicast linkstate
 linkstate lsrp4 1 0
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
 linkstate lsrp6 1 0
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
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:06 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 nei
r2#show ipv6 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:06 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 dat
r2#show ipv4 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 4.4.4.1 | r1   | 1   | 2   | 4   | 55c2a7bf | 00:59:56 |
 | 4.4.4.2 | r2   | 1   | 2   | 4   | efc4fb78 | 00:59:56 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 dat
r2#show ipv6 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 6.6.6.1 | r1   | 1   | 2   | 4   | 55c2a7bf | 00:59:58 |
 | 6.6.6.2 | r2   | 1   | 2   | 4   | efc4fb78 | 00:59:58 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 tre
r2#show ipv4 lsrp 1 tre
`--r2
   `--r1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 tre
r2#show ipv6 lsrp 1 tre
`--r2
   `--r1
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
 | C    | 1.1.1.0/24   | 0/0    | ethernet1 | null    | 00:00:12 |
 | LOC  | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:12 |
 | L EX | 2.2.2.1/32   | 70/10  | ethernet1 | 1.1.1.1 | 00:00:04 |
 | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:12 |
 | B    | 2.2.2.101/32 | 20/0   | ethernet1 | 1.1.1.1 | 00:00:09 |
 | C    | 2.2.2.102/32 | 0/0    | loopback2 | null    | 00:00:12 |
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
 | C    | 1234::/16     | 0/0    | ethernet1 | null    | 00:00:12 |
 | LOC  | 1234::2/128   | 0/1    | ethernet1 | null    | 00:00:12 |
 | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null    | 00:00:12 |
 | B    | 4321::101/128 | 20/0   | ethernet1 | 1234::1 | 00:00:09 |
 | C    | 4321::102/128 | 0/0    | loopback2 | null    | 00:00:12 |
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
 | 1397:1cd7:1e93:7b19:b0b8:58d2:92ee:e7a/128  | null    | 0/0/0/0    |        |
 | 3a0b:6d1f:cb89:bdfd:9073:97c7:cf7e:8fc0/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 3d7b:5a94:8ba0:98b6:2641:bc31:c3ec:14b2/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 42e2:899d:5813:d92:6c96:905d:5adf:85b3/128  | null    | 0/0/0/0    |        |
 | 489e:450b:3160:bccc:ca9f:f631:7f2:ebe2/128  | 1.1.1.2 | 20/100/0/0 | 2      |
 | 70a5:d724:24:83a9:765c:f4d5:8cf:aad8/128    | 1.1.1.2 | 20/100/0/0 | 2      |
 | 7512:4c43:7a26:ab69:3000:26ef:50e1:c2c5/128 | null    | 0/0/0/0    |        |
 | 9697:4068:c2dc:7e4c:4f80:780d:47e5:4734/128 | 1.1.1.2 | 20/100/0/0 | 2      |
 | 9e35:eee6:5ac2:69ae:e3c7:67a:a767:5d97/128  | null    | 0/0/0/0    |        |
 | a938:6f76:da1e:fdef:ce59:c2eb:cc26:628/128  | null    | 0/0/0/0    |        |
 | b240:899:5911:cb03:3b69:ac55:4b8c:2674/128  | 1.1.1.2 | 20/100/0/0 | 2      |
 | b428:8c01:c417:8e10:b892:157:9bb7:62a7/128  | null    | 0/0/0/0    |        |
 | d3b8:752e:3a70:8c26:8b48:f10a:7ca4:4479/128 | null    | 0/0/0/0    |        |
 | d83a:aa11:cc03:f4f9:ce58:2f31:21dc:dd53/128 | 1.1.1.2 | 20/100/0/0 | 2      |
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
 | e9:b12f:8124:3e9:a1a3:ab32:21e8:c85a/128    | null    | 0/0/0/0    |        |
 | 284:c758:150:3d26:80c0:d77b:5b50:dbfb/128   | 1234::2 | 20/100/0/0 | 2      |
 | 960:681d:a6ac:3124:318c:d0e9:5a42:d623/128  | 1234::2 | 20/100/0/0 | 2      |
 | 9f5:7fc2:3cf8:9462:cf52:9a8e:68b6:99b0/128  | null    | 0/0/0/0    |        |
 | 120e:47a:41c4:5480:9f07:a653:6f1a:579e/128  | 1234::2 | 20/100/0/0 | 2      |
 | 2a33:54a8:5e34:ad7:a2f2:5073:2b17:a746/128  | null    | 0/0/0/0    |        |
 | 2e88:7451:ea4c:a2a4:343e:a76e:ad70:dfed/128 | 1234::2 | 20/100/0/0 | 2      |
 | 4e76:ccc4:c6a2:a9f0:87d0:201a:6c10:9d97/128 | 1234::2 | 20/100/0/0 | 2      |
 | 9981:7ba1:6e5d:d878:1d03:d6a9:b030:a41e/128 | null    | 0/0/0/0    |        |
 | a3db:af06:eb95:ea8b:7613:41d1:c2f1:e710/128 | 1234::2 | 20/100/0/0 | 2      |
 | b964:4dff:5681:a150:602:182e:b714:6836/128  | null    | 0/0/0/0    |        |
 | c0bf:d1a0:95c4:71f6:2380:ecbf:4958:35cc/128 | null    | 0/0/0/0    |        |
 | c0e2:d082:3a5c:d0ff:e10a:feb6:6e44:862/128  | null    | 0/0/0/0    |        |
 | c9cf:971:2a39:f4e3:ba5:8681:1f58:f725/128   | 1234::2 | 20/100/0/0 | 2      |
 |_____________________________________________|_________|____________|________|
r1#
r1#
```

# Example: sr in chain

## **Topology diagram**

![topology](/img/mpls-sr01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz29r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
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
 segrout 10 1
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
 segrout 10 1
 redistribute connected
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
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
logging file debug ../binTmp/zzz29r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
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
 segrout 10 2
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
 segrout 10 2
 redistribute connected
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1234::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1235::2 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz29r3-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
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
 router-id 4.4.4.3
 segrout 10 3
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
 segrout 10 3
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.3 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1235::3 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.3.3 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1236::3 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz29r4-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
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
 router-id 4.4.4.4
 segrout 10 4
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.4
 segrout 10 4
 redistribute connected
 exit
!
interface loopback1
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
 ipv4 address 1.1.3.4 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address 1236::4 ffff::
 ipv6 access-group-in test6
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
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
r1#show mpls for
r1#show mpls for
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf      | iface     | hop     | label      | targets | bytes |
 |---------|----------|-----------|---------|------------|---------|-------|
 | 62206   | v1:6     | ethernet1 | 1234::2 | 3          |         | 0     |
 | 201547  | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 350935  | v1:4     | ethernet1 | 1.1.1.2 | 3          |         | 0     |
 | 750072  | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 819824  | null     | null      | null    | unlabelled |         | 0     |
 | 819825  | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 819826  | v1:4     | ethernet1 | 1.1.1.2 | 35578      |         | 0     |
 | 819827  | v1:4     | ethernet1 | 1.1.1.2 | 35579      |         | 0     |
 | 819828  | v1:4     | ethernet1 | 1.1.1.2 | 35580      |         | 0     |
 | 819829  | null     | null      | null    | unlabelled |         | 0     |
 | 819830  | null     | null      | null    | unlabelled |         | 0     |
 | 819831  | null     | null      | null    | unlabelled |         | 0     |
 | 819832  | null     | null      | null    | unlabelled |         | 0     |
 | 819833  | null     | null      | null    | unlabelled |         | 0     |
 | 898256  | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 911349  | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 1020620 | null     | null      | null    | unlabelled |         | 0     |
 | 1020621 | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 1020622 | v1:6     | ethernet1 | 1234::2 | 179141     |         | 0     |
 | 1020623 | v1:6     | ethernet1 | 1234::2 | 179142     |         | 0     |
 | 1020624 | v1:6     | ethernet1 | 1234::2 | 179143     |         | 0     |
 | 1020625 | null     | null      | null    | unlabelled |         | 0     |
 | 1020626 | null     | null      | null    | unlabelled |         | 0     |
 | 1020627 | null     | null      | null    | unlabelled |         | 0     |
 | 1020628 | null     | null      | null    | unlabelled |         | 0     |
 | 1020629 | null     | null      | null    | unlabelled |         | 0     |
 |_________|__________|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r2#
r2#
r2#show mpls forw
r2#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop     | label      | targets | bytes |
 |--------|----------|-----------|---------|------------|---------|-------|
 | 35576  | null     | null      | null    | unlabelled |         | 0     |
 | 35577  | v1:4     | ethernet1 | 1.1.1.1 | 819825     |         | 1280  |
 | 35578  | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 35579  | v1:4     | ethernet2 | 1.1.2.3 | 644362     |         | 640   |
 | 35580  | v1:4     | ethernet2 | 1.1.2.3 | 644363     |         | 640   |
 | 35581  | null     | null      | null    | unlabelled |         | 0     |
 | 35582  | null     | null      | null    | unlabelled |         | 0     |
 | 35583  | null     | null      | null    | unlabelled |         | 0     |
 | 35584  | null     | null      | null    | unlabelled |         | 0     |
 | 35585  | null     | null      | null    | unlabelled |         | 0     |
 | 155997 | v1:6     | ethernet2 | 1235::3 | 3          |         | 0     |
 | 171544 | v1:4     | ethernet2 | 1.1.2.3 | 3          |         | 0     |
 | 179139 | null     | null      | null    | unlabelled |         | 0     |
 | 179140 | v1:6     | ethernet1 | 1234::1 | 1020621    |         | 1280  |
 | 179141 | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 179142 | v1:6     | ethernet2 | 1235::3 | 738290     |         | 640   |
 | 179143 | v1:6     | ethernet2 | 1235::3 | 738291     |         | 640   |
 | 179144 | null     | null      | null    | unlabelled |         | 0     |
 | 179145 | null     | null      | null    | unlabelled |         | 0     |
 | 179146 | null     | null      | null    | unlabelled |         | 0     |
 | 179147 | null     | null      | null    | unlabelled |         | 0     |
 | 179148 | null     | null      | null    | unlabelled |         | 0     |
 | 345463 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 360908 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 400755 | v1:4     | ethernet1 | 1.1.1.1 | 3          |         | 0     |
 | 607238 | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 746738 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 878613 | v1:6     | ethernet1 | 1234::1 | 3          |         | 0     |
 |________|__________|___________|_________|____________|_________|_______|
r2#
r2#
```

```
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop     | label      | targets | bytes |
 |--------|----------|-----------|---------|------------|---------|-------|
 | 16120  | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 167403 | v1:4     | ethernet2 | 1.1.3.4 | 3          |         | 0     |
 | 256568 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 394625 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 602177 | v1:4     | ethernet1 | 1.1.2.2 | 3          |         | 0     |
 | 644359 | null     | null      | null    | unlabelled |         | 0     |
 | 644360 | v1:4     | ethernet1 | 1.1.2.2 | 35577      |         | 640   |
 | 644361 | v1:4     | ethernet1 | 1.1.2.2 | 35578      |         | 640   |
 | 644362 | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 644363 | v1:4     | ethernet2 | 1.1.3.4 | 756758     |         | 1280  |
 | 644364 | null     | null      | null    | unlabelled |         | 0     |
 | 644365 | null     | null      | null    | unlabelled |         | 0     |
 | 644366 | null     | null      | null    | unlabelled |         | 0     |
 | 644367 | null     | null      | null    | unlabelled |         | 0     |
 | 644368 | null     | null      | null    | unlabelled |         | 0     |
 | 727207 | v1:6     | ethernet1 | 1235::2 | 3          |         | 0     |
 | 738287 | null     | null      | null    | unlabelled |         | 0     |
 | 738288 | v1:6     | ethernet1 | 1235::2 | 179140     |         | 640   |
 | 738289 | v1:6     | ethernet1 | 1235::2 | 179141     |         | 640   |
 | 738290 | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 738291 | v1:6     | ethernet2 | 1236::4 | 364035     |         | 1280  |
 | 738292 | null     | null      | null    | unlabelled |         | 0     |
 | 738293 | null     | null      | null    | unlabelled |         | 0     |
 | 738294 | null     | null      | null    | unlabelled |         | 0     |
 | 738295 | null     | null      | null    | unlabelled |         | 0     |
 | 738296 | null     | null      | null    | unlabelled |         | 0     |
 | 779139 | v1:6     | ethernet2 | 1236::4 | 3          |         | 0     |
 | 787388 | tester:4 | null      | null    | unlabelled | local   | 0     |
 |________|__________|___________|_________|____________|_________|_______|
r3#
r3#
```

```
r4#
r4#
r4#show mpls forw
r4#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop     | label      | targets | bytes |
 |--------|----------|-----------|---------|------------|---------|-------|
 | 364031 | null     | null      | null    | unlabelled |         | 0     |
 | 364032 | v1:6     | ethernet1 | 1236::3 | 738288     |         | 0     |
 | 364033 | v1:6     | ethernet1 | 1236::3 | 738289     |         | 0     |
 | 364034 | v1:6     | ethernet1 | 1236::3 | 738290     |         | 0     |
 | 364035 | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 364036 | null     | null      | null    | unlabelled |         | 0     |
 | 364037 | null     | null      | null    | unlabelled |         | 0     |
 | 364038 | null     | null      | null    | unlabelled |         | 0     |
 | 364039 | null     | null      | null    | unlabelled |         | 0     |
 | 364040 | null     | null      | null    | unlabelled |         | 0     |
 | 600754 | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 633130 | v1:4     | ethernet1 | 1.1.3.3 | 3          |         | 0     |
 | 663131 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 756754 | null     | null      | null    | unlabelled |         | 0     |
 | 756755 | v1:4     | ethernet1 | 1.1.3.3 | 644360     |         | 0     |
 | 756756 | v1:4     | ethernet1 | 1.1.3.3 | 644361     |         | 0     |
 | 756757 | v1:4     | ethernet1 | 1.1.3.3 | 644362     |         | 0     |
 | 756758 | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 756759 | null     | null      | null    | unlabelled |         | 0     |
 | 756760 | null     | null      | null    | unlabelled |         | 0     |
 | 756761 | null     | null      | null    | unlabelled |         | 0     |
 | 756762 | null     | null      | null    | unlabelled |         | 0     |
 | 756763 | null     | null      | null    | unlabelled |         | 0     |
 | 866778 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 868479 | v1:6     | ethernet1 | 1236::3 | 3          |         | 0     |
 | 886611 | tester:6 | null      | null    | unlabelled | local   | 0     |
 |________|__________|___________|_________|____________|_________|_______|
r4#
r4#
```

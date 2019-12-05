# Example: sr in chain

## **Topology diagram**

![topology](/img/mpls-sr01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
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
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
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
end
```

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
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
end
```

## **Verification**

```
r1#
r1#
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf  | iface     | hop     | label      | targets | bytes |
 |--------|------|-----------|---------|------------|---------|-------|
 | 9126   | null | null      | null    | unlabelled |         | 0     |
 | 9127   | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 9128   | v1:6 | ethernet1 | 1234::2 | 301353     |         | 0     |
 | 9129   | v1:6 | ethernet1 | 1234::2 | 301354     |         | 0     |
 | 9130   | v1:6 | ethernet1 | 1234::2 | 301355     |         | 0     |
 | 9131   | null | null      | null    | unlabelled |         | 0     |
 | 9132   | null | null      | null    | unlabelled |         | 0     |
 | 9133   | null | null      | null    | unlabelled |         | 0     |
 | 9134   | null | null      | null    | unlabelled |         | 0     |
 | 9135   | null | null      | null    | unlabelled |         | 0     |
 | 25870  | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 699554 | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 804360 | null | null      | null    | unlabelled |         | 0     |
 | 804361 | v1:4 | null      | null    | unlabelled | local   | 2944  |
 | 804362 | v1:4 | ethernet1 | 1.1.1.2 | 615912     |         | 0     |
 | 804363 | v1:4 | ethernet1 | 1.1.1.2 | 615913     |         | 0     |
 | 804364 | v1:4 | ethernet1 | 1.1.1.2 | 615914     |         | 0     |
 | 804365 | null | null      | null    | unlabelled |         | 0     |
 | 804366 | null | null      | null    | unlabelled |         | 0     |
 | 804367 | null | null      | null    | unlabelled |         | 0     |
 | 804368 | null | null      | null    | unlabelled |         | 0     |
 | 804369 | null | null      | null    | unlabelled |         | 0     |
 | 823333 | v1:6 | ethernet1 | 1234::2 | 3          |         | 0     |
 | 897139 | v1:4 | ethernet1 | 1.1.1.2 | 3          |         | 0     |
 |________|______|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r2#
r2#
r2#show mpls forw
r2#show mpls forw
 |~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf  | iface     | hop     | label      | targets | bytes |
 |--------|------|-----------|---------|------------|---------|-------|
 | 180161 | v1:6 | ethernet1 | 1234::1 | 3          |         | 0     |
 | 301351 | null | null      | null    | unlabelled |         | 0     |
 | 301352 | v1:6 | ethernet1 | 1234::1 | 9127       |         | 2240  |
 | 301353 | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 301354 | v1:6 | ethernet2 | 1235::3 | 678742     |         | 1120  |
 | 301355 | v1:6 | ethernet2 | 1235::3 | 678743     |         | 1120  |
 | 301356 | null | null      | null    | unlabelled |         | 0     |
 | 301357 | null | null      | null    | unlabelled |         | 0     |
 | 301358 | null | null      | null    | unlabelled |         | 0     |
 | 301359 | null | null      | null    | unlabelled |         | 0     |
 | 301360 | null | null      | null    | unlabelled |         | 0     |
 | 408261 | v1:4 | ethernet2 | 1.1.2.3 | 3          |         | 0     |
 | 615910 | null | null      | null    | unlabelled |         | 0     |
 | 615911 | v1:4 | ethernet1 | 1.1.1.1 | 804361     |         | 1840  |
 | 615912 | v1:4 | null      | null    | unlabelled | local   | 2944  |
 | 615913 | v1:4 | ethernet2 | 1.1.2.3 | 174096     |         | 920   |
 | 615914 | v1:4 | ethernet2 | 1.1.2.3 | 174097     |         | 920   |
 | 615915 | null | null      | null    | unlabelled |         | 0     |
 | 615916 | null | null      | null    | unlabelled |         | 0     |
 | 615917 | null | null      | null    | unlabelled |         | 0     |
 | 615918 | null | null      | null    | unlabelled |         | 0     |
 | 615919 | null | null      | null    | unlabelled |         | 0     |
 | 761588 | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 841387 | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 849492 | v1:6 | ethernet2 | 1235::3 | 3          |         | 0     |
 | 865589 | v1:4 | ethernet1 | 1.1.1.1 | 3          |         | 0     |
 |________|______|___________|_________|____________|_________|_______|
r2#
r2#
```

```
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf  | iface     | hop     | label      | targets | bytes |
 |--------|------|-----------|---------|------------|---------|-------|
 | 174093 | null | null      | null    | unlabelled |         | 0     |
 | 174094 | v1:4 | ethernet1 | 1.1.2.2 | 615911     |         | 920   |
 | 174095 | v1:4 | ethernet1 | 1.1.2.2 | 615912     |         | 920   |
 | 174096 | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 174097 | v1:4 | ethernet2 | 1.1.3.4 | 328494     |         | 1840  |
 | 174098 | null | null      | null    | unlabelled |         | 0     |
 | 174099 | null | null      | null    | unlabelled |         | 0     |
 | 174100 | null | null      | null    | unlabelled |         | 0     |
 | 174101 | null | null      | null    | unlabelled |         | 0     |
 | 174102 | null | null      | null    | unlabelled |         | 0     |
 | 275694 | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 411264 | v1:6 | ethernet1 | 1235::2 | 3          |         | 0     |
 | 634309 | v1:4 | ethernet2 | 1.1.3.4 | 3          |         | 0     |
 | 649106 | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 678739 | null | null      | null    | unlabelled |         | 0     |
 | 678740 | v1:6 | ethernet1 | 1235::2 | 301352     |         | 1120  |
 | 678741 | v1:6 | ethernet1 | 1235::2 | 301353     |         | 1120  |
 | 678742 | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 678743 | v1:6 | ethernet2 | 1236::4 | 758345     |         | 2240  |
 | 678744 | null | null      | null    | unlabelled |         | 0     |
 | 678745 | null | null      | null    | unlabelled |         | 0     |
 | 678746 | null | null      | null    | unlabelled |         | 0     |
 | 678747 | null | null      | null    | unlabelled |         | 0     |
 | 678748 | null | null      | null    | unlabelled |         | 0     |
 | 841622 | v1:6 | ethernet2 | 1236::4 | 3          |         | 0     |
 | 872388 | v1:4 | ethernet1 | 1.1.2.2 | 3          |         | 0     |
 |________|______|___________|_________|____________|_________|_______|
r3#
r3#
```

```
r4#
r4#
r4#show mpls forw
r4#show mpls forw
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf  | iface     | hop     | label      | targets | bytes |
 |---------|------|-----------|---------|------------|---------|-------|
 | 97876   | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 328490  | null | null      | null    | unlabelled |         | 0     |
 | 328491  | v1:4 | ethernet1 | 1.1.3.3 | 174094     |         | 0     |
 | 328492  | v1:4 | ethernet1 | 1.1.3.3 | 174095     |         | 0     |
 | 328493  | v1:4 | ethernet1 | 1.1.3.3 | 174096     |         | 0     |
 | 328494  | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 328495  | null | null      | null    | unlabelled |         | 0     |
 | 328496  | null | null      | null    | unlabelled |         | 0     |
 | 328497  | null | null      | null    | unlabelled |         | 0     |
 | 328498  | null | null      | null    | unlabelled |         | 0     |
 | 328499  | null | null      | null    | unlabelled |         | 0     |
 | 728473  | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 758341  | null | null      | null    | unlabelled |         | 0     |
 | 758342  | v1:6 | ethernet1 | 1236::3 | 678740     |         | 0     |
 | 758343  | v1:6 | ethernet1 | 1236::3 | 678741     |         | 0     |
 | 758344  | v1:6 | ethernet1 | 1236::3 | 678742     |         | 0     |
 | 758345  | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 758346  | null | null      | null    | unlabelled |         | 0     |
 | 758347  | null | null      | null    | unlabelled |         | 0     |
 | 758348  | null | null      | null    | unlabelled |         | 0     |
 | 758349  | null | null      | null    | unlabelled |         | 0     |
 | 758350  | null | null      | null    | unlabelled |         | 0     |
 | 759363  | v1:4 | ethernet1 | 1.1.3.3 | 3          |         | 0     |
 | 1019718 | v1:6 | ethernet1 | 1236::3 | 3          |         | 0     |
 |_________|______|___________|_________|____________|_________|_______|
r4#
r4#
```

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
 | 59721  | v1:4 | ethernet1 | 1.1.1.2 | 3          |         | 0     |
 | 253284 | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 478740 | null | null      | null    | unlabelled |         | 0     |
 | 478741 | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 478742 | v1:4 | ethernet1 | 1.1.1.2 | 519367     |         | 0     |
 | 478743 | v1:4 | ethernet1 | 1.1.1.2 | 519368     |         | 0     |
 | 478744 | v1:4 | ethernet1 | 1.1.1.2 | 519369     |         | 0     |
 | 478745 | null | null      | null    | unlabelled |         | 0     |
 | 478746 | null | null      | null    | unlabelled |         | 0     |
 | 478747 | null | null      | null    | unlabelled |         | 0     |
 | 478748 | null | null      | null    | unlabelled |         | 0     |
 | 478749 | null | null      | null    | unlabelled |         | 0     |
 | 687071 | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 930850 | v1:6 | ethernet1 | 1234::2 | 3          |         | 0     |
 | 981996 | null | null      | null    | unlabelled |         | 0     |
 | 981997 | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 981998 | v1:6 | ethernet1 | 1234::2 | 259971     |         | 0     |
 | 981999 | v1:6 | ethernet1 | 1234::2 | 259972     |         | 0     |
 | 982000 | v1:6 | ethernet1 | 1234::2 | 259973     |         | 0     |
 | 982001 | null | null      | null    | unlabelled |         | 0     |
 | 982002 | null | null      | null    | unlabelled |         | 0     |
 | 982003 | null | null      | null    | unlabelled |         | 0     |
 | 982004 | null | null      | null    | unlabelled |         | 0     |
 | 982005 | null | null      | null    | unlabelled |         | 0     |
 |________|______|___________|_________|____________|_________|_______|
r1#
r1#
```

```
r2#
r2#
r2#show mpls forw
r2#show mpls forw
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf  | iface     | hop     | label      | targets | bytes |
 |---------|------|-----------|---------|------------|---------|-------|
 | 3124    | v1:4 | ethernet1 | 1.1.1.1 | 3          |         | 0     |
 | 200340  | v1:6 | ethernet1 | 1234::1 | 3          |         | 0     |
 | 259969  | null | null      | null    | unlabelled |         | 0     |
 | 259970  | v1:6 | ethernet1 | 1234::1 | 981997     |         | 2240  |
 | 259971  | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 259972  | v1:6 | ethernet2 | 1235::3 | 715493     |         | 1120  |
 | 259973  | v1:6 | ethernet2 | 1235::3 | 715494     |         | 1120  |
 | 259974  | null | null      | null    | unlabelled |         | 0     |
 | 259975  | null | null      | null    | unlabelled |         | 0     |
 | 259976  | null | null      | null    | unlabelled |         | 0     |
 | 259977  | null | null      | null    | unlabelled |         | 0     |
 | 259978  | null | null      | null    | unlabelled |         | 0     |
 | 443687  | v1:6 | ethernet2 | 1235::3 | 3          |         | 0     |
 | 510763  | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 519365  | null | null      | null    | unlabelled |         | 0     |
 | 519366  | v1:4 | ethernet1 | 1.1.1.1 | 478741     |         | 1840  |
 | 519367  | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 519368  | v1:4 | ethernet2 | 1.1.2.3 | 1000428    |         | 920   |
 | 519369  | v1:4 | ethernet2 | 1.1.2.3 | 1000429    |         | 920   |
 | 519370  | null | null      | null    | unlabelled |         | 0     |
 | 519371  | null | null      | null    | unlabelled |         | 0     |
 | 519372  | null | null      | null    | unlabelled |         | 0     |
 | 519373  | null | null      | null    | unlabelled |         | 0     |
 | 519374  | null | null      | null    | unlabelled |         | 0     |
 | 585986  | v1:4 | ethernet2 | 1.1.2.3 | 3          |         | 0     |
 | 1017724 | v1:6 | null      | null    | unlabelled | local   | 0     |
 |_________|______|___________|_________|____________|_________|_______|
r2#
r2#
```

```
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf  | iface     | hop     | label      | targets | bytes |
 |---------|------|-----------|---------|------------|---------|-------|
 | 370620  | v1:6 | ethernet2 | 1236::4 | 3          |         | 0     |
 | 479919  | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 618493  | v1:4 | ethernet1 | 1.1.2.2 | 3          |         | 0     |
 | 625538  | v1:6 | ethernet1 | 1235::2 | 3          |         | 0     |
 | 715490  | null | null      | null    | unlabelled |         | 0     |
 | 715491  | v1:6 | ethernet1 | 1235::2 | 259970     |         | 1120  |
 | 715492  | v1:6 | ethernet1 | 1235::2 | 259971     |         | 1120  |
 | 715493  | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 715494  | v1:6 | ethernet2 | 1236::4 | 360286     |         | 2240  |
 | 715495  | null | null      | null    | unlabelled |         | 0     |
 | 715496  | null | null      | null    | unlabelled |         | 0     |
 | 715497  | null | null      | null    | unlabelled |         | 0     |
 | 715498  | null | null      | null    | unlabelled |         | 0     |
 | 715499  | null | null      | null    | unlabelled |         | 0     |
 | 745398  | v1:4 | ethernet2 | 1.1.3.4 | 3          |         | 0     |
 | 755124  | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 1000425 | null | null      | null    | unlabelled |         | 0     |
 | 1000426 | v1:4 | ethernet1 | 1.1.2.2 | 519366     |         | 920   |
 | 1000427 | v1:4 | ethernet1 | 1.1.2.2 | 519367     |         | 920   |
 | 1000428 | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 1000429 | v1:4 | ethernet2 | 1.1.3.4 | 86527      |         | 1840  |
 | 1000430 | null | null      | null    | unlabelled |         | 0     |
 | 1000431 | null | null      | null    | unlabelled |         | 0     |
 | 1000432 | null | null      | null    | unlabelled |         | 0     |
 | 1000433 | null | null      | null    | unlabelled |         | 0     |
 | 1000434 | null | null      | null    | unlabelled |         | 0     |
 |_________|______|___________|_________|____________|_________|_______|
r3#
r3#
```

```
r4#
r4#
r4#show mpls forw
r4#show mpls forw
 |~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf  | iface     | hop     | label      | targets | bytes |
 |--------|------|-----------|---------|------------|---------|-------|
 | 86523  | null | null      | null    | unlabelled |         | 0     |
 | 86524  | v1:4 | ethernet1 | 1.1.3.3 | 1000426    |         | 0     |
 | 86525  | v1:4 | ethernet1 | 1.1.3.3 | 1000427    |         | 0     |
 | 86526  | v1:4 | ethernet1 | 1.1.3.3 | 1000428    |         | 0     |
 | 86527  | v1:4 | null      | null    | unlabelled | local   | 2760  |
 | 86528  | null | null      | null    | unlabelled |         | 0     |
 | 86529  | null | null      | null    | unlabelled |         | 0     |
 | 86530  | null | null      | null    | unlabelled |         | 0     |
 | 86531  | null | null      | null    | unlabelled |         | 0     |
 | 86532  | null | null      | null    | unlabelled |         | 0     |
 | 360282 | null | null      | null    | unlabelled |         | 0     |
 | 360283 | v1:6 | ethernet1 | 1236::3 | 715491     |         | 0     |
 | 360284 | v1:6 | ethernet1 | 1236::3 | 715492     |         | 0     |
 | 360285 | v1:6 | ethernet1 | 1236::3 | 715493     |         | 0     |
 | 360286 | v1:6 | null      | null    | unlabelled | local   | 3360  |
 | 360287 | null | null      | null    | unlabelled |         | 0     |
 | 360288 | null | null      | null    | unlabelled |         | 0     |
 | 360289 | null | null      | null    | unlabelled |         | 0     |
 | 360290 | null | null      | null    | unlabelled |         | 0     |
 | 360291 | null | null      | null    | unlabelled |         | 0     |
 | 662570 | v1:6 | null      | null    | unlabelled | local   | 0     |
 | 744992 | v1:6 | ethernet1 | 1236::3 | 3          |         | 0     |
 | 851519 | v1:4 | null      | null    | unlabelled | local   | 0     |
 | 962275 | v1:4 | ethernet1 | 1.1.3.3 | 3          |         | 0     |
 |________|______|___________|_________|____________|_________|_______|
r4#
r4#
```

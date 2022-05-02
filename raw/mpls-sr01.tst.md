# Example: sr in chain

## **Topology diagram**

![topology](/img/mpls-sr01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz71r1-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz71r2-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz71r3-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz71r4-log.run
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
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
r1#show mpls forw
r1#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface     | hop     | label      | targets | bytes |
 |--------|----------|-----------|---------|------------|---------|-------|
 | 130949 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 162899 | null     | null      | null    | unlabelled |         | 0     |
 | 162900 | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 162901 | v1:4     | ethernet1 | 1.1.1.2 | 719832     |         | 0     |
 | 162902 | v1:4     | ethernet1 | 1.1.1.2 | 719833     |         | 0     |
 | 162903 | v1:4     | ethernet1 | 1.1.1.2 | 719834     |         | 0     |
 | 162904 | null     | null      | null    | unlabelled |         | 0     |
 | 162905 | null     | null      | null    | unlabelled |         | 0     |
 | 162906 | null     | null      | null    | unlabelled |         | 0     |
 | 162907 | null     | null      | null    | unlabelled |         | 0     |
 | 162908 | null     | null      | null    | unlabelled |         | 0     |
 | 167595 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 169428 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 266420 | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 463791 | null     | null      | null    | unlabelled |         | 0     |
 | 463792 | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 463793 | v1:6     | ethernet1 | 1234::2 | 56210      |         | 0     |
 | 463794 | v1:6     | ethernet1 | 1234::2 | 56211      |         | 0     |
 | 463795 | v1:6     | ethernet1 | 1234::2 | 56212      |         | 0     |
 | 463796 | null     | null      | null    | unlabelled |         | 0     |
 | 463797 | null     | null      | null    | unlabelled |         | 0     |
 | 463798 | null     | null      | null    | unlabelled |         | 0     |
 | 463799 | null     | null      | null    | unlabelled |         | 0     |
 | 463800 | null     | null      | null    | unlabelled |         | 0     |
 | 472264 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 679329 | v1:6     | ethernet1 | 1234::2 | 3          |         | 0     |
 | 700526 | v1:4     | ethernet1 | 1.1.1.2 | 3          |         | 0     |
 | 803227 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 811714 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 883854 | tester:6 | null      | null    | unlabelled | local   | 0     |
 |________|__________|___________|_________|____________|_________|_______|
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
 | 1382   | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 24497  | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 56208  | null     | null      | null    | unlabelled |         | 0     |
 | 56209  | v1:6     | ethernet1 | 1234::1 | 463792     |         | 1280  |
 | 56210  | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 56211  | v1:6     | ethernet2 | 1235::3 | 585712     |         | 640   |
 | 56212  | v1:6     | ethernet2 | 1235::3 | 585713     |         | 640   |
 | 56213  | null     | null      | null    | unlabelled |         | 0     |
 | 56214  | null     | null      | null    | unlabelled |         | 0     |
 | 56215  | null     | null      | null    | unlabelled |         | 0     |
 | 56216  | null     | null      | null    | unlabelled |         | 0     |
 | 56217  | null     | null      | null    | unlabelled |         | 0     |
 | 234837 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 300101 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 361135 | v1:4     | ethernet2 | 1.1.2.3 | 3          |         | 0     |
 | 403945 | v1:6     | ethernet2 | 1235::3 | 3          |         | 0     |
 | 443743 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 622066 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 719830 | null     | null      | null    | unlabelled |         | 0     |
 | 719831 | v1:4     | ethernet1 | 1.1.1.1 | 162900     |         | 1280  |
 | 719832 | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 719833 | v1:4     | ethernet2 | 1.1.2.3 | 601322     |         | 640   |
 | 719834 | v1:4     | ethernet2 | 1.1.2.3 | 601323     |         | 640   |
 | 719835 | null     | null      | null    | unlabelled |         | 0     |
 | 719836 | null     | null      | null    | unlabelled |         | 0     |
 | 719837 | null     | null      | null    | unlabelled |         | 0     |
 | 719838 | null     | null      | null    | unlabelled |         | 0     |
 | 719839 | null     | null      | null    | unlabelled |         | 0     |
 | 881139 | v1:4     | ethernet1 | 1.1.1.1 | 3          |         | 0     |
 | 884197 | v1:6     | ethernet1 | 1234::1 | 3          |         | 0     |
 | 904499 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 932129 | tester:4 | null      | null    | unlabelled | local   | 0     |
 |________|__________|___________|_________|____________|_________|_______|
r2#
r2#
```

```
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf      | iface     | hop     | label      | targets | bytes |
 |---------|----------|-----------|---------|------------|---------|-------|
 | 11712   | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 119543  | v1:4     | ethernet2 | 1.1.3.4 | 3          |         | 0     |
 | 178242  | v1:6     | ethernet1 | 1235::2 | 3          |         | 0     |
 | 353228  | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 384204  | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 500968  | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 530286  | v1:4     | ethernet1 | 1.1.2.2 | 3          |         | 0     |
 | 585709  | null     | null      | null    | unlabelled |         | 0     |
 | 585710  | v1:6     | ethernet1 | 1235::2 | 56209      |         | 640   |
 | 585711  | v1:6     | ethernet1 | 1235::2 | 56210      |         | 640   |
 | 585712  | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 585713  | v1:6     | ethernet2 | 1236::4 | 544        |         | 1280  |
 | 585714  | null     | null      | null    | unlabelled |         | 0     |
 | 585715  | null     | null      | null    | unlabelled |         | 0     |
 | 585716  | null     | null      | null    | unlabelled |         | 0     |
 | 585717  | null     | null      | null    | unlabelled |         | 0     |
 | 585718  | null     | null      | null    | unlabelled |         | 0     |
 | 601319  | null     | null      | null    | unlabelled |         | 0     |
 | 601320  | v1:4     | ethernet1 | 1.1.2.2 | 719831     |         | 640   |
 | 601321  | v1:4     | ethernet1 | 1.1.2.2 | 719832     |         | 640   |
 | 601322  | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 601323  | v1:4     | ethernet2 | 1.1.3.4 | 790753     |         | 1280  |
 | 601324  | null     | null      | null    | unlabelled |         | 0     |
 | 601325  | null     | null      | null    | unlabelled |         | 0     |
 | 601326  | null     | null      | null    | unlabelled |         | 0     |
 | 601327  | null     | null      | null    | unlabelled |         | 0     |
 | 601328  | null     | null      | null    | unlabelled |         | 0     |
 | 660084  | v1:6     | ethernet2 | 1236::4 | 3          |         | 0     |
 | 769754  | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 785129  | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 993392  | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 1039029 | tester:6 | null      | null    | unlabelled | local   | 0     |
 |_________|__________|___________|_________|____________|_________|_______|
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
 | 540    | null     | null      | null    | unlabelled |         | 0     |
 | 541    | v1:6     | ethernet1 | 1236::3 | 585710     |         | 0     |
 | 542    | v1:6     | ethernet1 | 1236::3 | 585711     |         | 0     |
 | 543    | v1:6     | ethernet1 | 1236::3 | 585712     |         | 0     |
 | 544    | v1:6     | null      | null    | unlabelled | local   | 1920  |
 | 545    | null     | null      | null    | unlabelled |         | 0     |
 | 546    | null     | null      | null    | unlabelled |         | 0     |
 | 547    | null     | null      | null    | unlabelled |         | 0     |
 | 548    | null     | null      | null    | unlabelled |         | 0     |
 | 549    | null     | null      | null    | unlabelled |         | 0     |
 | 80245  | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 82451  | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 164696 | tester:4 | null      | null    | unlabelled | local   | 0     |
 | 334601 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 380796 | tester:6 | null      | null    | unlabelled | local   | 0     |
 | 489722 | v1:4     | ethernet1 | 1.1.3.3 | 3          |         | 0     |
 | 589332 | v1:4     | null      | null    | unlabelled | local   | 0     |
 | 738379 | v1:6     | null      | null    | unlabelled | local   | 0     |
 | 763606 | v1:6     | ethernet1 | 1236::3 | 3          |         | 0     |
 | 790749 | null     | null      | null    | unlabelled |         | 0     |
 | 790750 | v1:4     | ethernet1 | 1.1.3.3 | 601320     |         | 0     |
 | 790751 | v1:4     | ethernet1 | 1.1.3.3 | 601321     |         | 0     |
 | 790752 | v1:4     | ethernet1 | 1.1.3.3 | 601322     |         | 0     |
 | 790753 | v1:4     | null      | null    | unlabelled | local   | 1920  |
 | 790754 | null     | null      | null    | unlabelled |         | 0     |
 | 790755 | null     | null      | null    | unlabelled |         | 0     |
 | 790756 | null     | null      | null    | unlabelled |         | 0     |
 | 790757 | null     | null      | null    | unlabelled |         | 0     |
 | 790758 | null     | null      | null    | unlabelled |         | 0     |
 | 886950 | tester:4 | null      | null    | unlabelled | local   | 0     |
 |________|__________|___________|_________|____________|_________|_______|
r4#
r4#
```

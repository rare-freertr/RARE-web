# Example: bier in chain

## **Topology diagram**

![topology](/img/mpls-bier01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz61r1-log.run
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
 bier 256 10 1
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
 bier 256 10 1
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
 ipv6 address 1234::1 ffff::
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel key 1
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 9.9.9.9
 tunnel domain-name 2.2.2.4
 tunnel mode bier
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel key 1
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 9999::9
 tunnel domain-name 4321::4
 tunnel mode bier
 vrf forwarding v1
 ipv6 address 4321::1111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
logging file debug ../binTmp/zzz61r2-log.run
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
 bier 256 10 2
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
 bier 256 10 2
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
 ipv6 address 1234::2 ffff::
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
 ipv6 address 1235::2 ffff::
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
logging file debug ../binTmp/zzz61r3-log.run
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
 bier 256 10 3
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.3
 bier 256 10 3
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
 ipv6 address 1235::3 ffff::
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
 ipv6 address 1236::3 ffff::
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
logging file debug ../binTmp/zzz61r4-log.run
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
 bier 256 10 4
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.4
 bier 256 10 4
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
 ipv6 address 1236::4 ffff::
 mpls enable
 router lsrp4 1 enable
 router lsrp6 1 enable
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel key 4
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 9.9.9.9
 tunnel domain-name 2.2.2.1
 tunnel mode bier
 vrf forwarding v1
 ipv4 address 3.3.3.4 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 tunnel key 4
 tunnel vrf v1
 tunnel source loopback1
 tunnel destination 9999::9
 tunnel domain-name 4321::1
 tunnel mode bier
 vrf forwarding v1
 ipv6 address 4321::1114 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface | hop  | label      | targets | bytes |
 |--------|----------|-------|------|------------|---------|-------|
 | 35992  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 128055 | v1:4     | null  | null | unlabelled | local   | 0     |
 | 176139 | tester:4 | null  | null | unlabelled | local   | 0     |
 | 238573 | v1:6     | null  | null | unlabelled | local   | 0     |
 | 263290 | v1:4     | null  | null | unlabelled | bier    | 520   |
 | 356826 | v1:6     | null  | null | unlabelled | bier    | 520   |
 | 370037 | tester:4 | null  | null | unlabelled | local   | 0     |
 | 379283 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 419716 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 527864 | tester:6 | null  | null | unlabelled | local   | 0     |
 |________|__________|_______|______|____________|_________|_______|
r1#
r1#
```

```
r2#
r2#
r2#show mpls forw
r2#show mpls forw
 |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label  | vrf      | iface | hop  | label      | targets | bytes |
 |--------|----------|-------|------|------------|---------|-------|
 | 24108  | v1:6     | null  | null | unlabelled | local   | 0     |
 | 260465 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 434267 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 509604 | tester:4 | null  | null | unlabelled | local   | 0     |
 | 555791 | tester:6 | null  | null | unlabelled | local   | 0     |
 | 603242 | v1:6     | null  | null | unlabelled | bier    | 1040  |
 | 662033 | tester:4 | null  | null | unlabelled | local   | 0     |
 | 666861 | v1:4     | null  | null | unlabelled | local   | 0     |
 | 702693 | v1:4     | null  | null | unlabelled | bier    | 1040  |
 | 706436 | tester:4 | null  | null | unlabelled | local   | 0     |
 |________|__________|_______|______|____________|_________|_______|
r2#
r2#
```

```
r3#
r3#
r3#show mpls forw
r3#show mpls forw
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf      | iface | hop  | label      | targets | bytes |
 |---------|----------|-------|------|------------|---------|-------|
 | 187148  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 317940  | v1:6     | null  | null | unlabelled | bier    | 1040  |
 | 487076  | v1:6     | null  | null | unlabelled | local   | 0     |
 | 488462  | v1:4     | null  | null | unlabelled | bier    | 1040  |
 | 561544  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 639356  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 689261  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 716377  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 887679  | v1:4     | null  | null | unlabelled | local   | 0     |
 | 1031613 | tester:4 | null  | null | unlabelled | local   | 0     |
 |_________|__________|_______|______|____________|_________|_______|
r3#
r3#
```

```
r4#
r4#
r4#show mpls forw
r4#show mpls forw
 |~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
 | label   | vrf      | iface | hop  | label      | targets | bytes |
 |---------|----------|-------|------|------------|---------|-------|
 | 191699  | v1:4     | null  | null | unlabelled | local   | 0     |
 | 239473  | v1:6     | null  | null | unlabelled | bier    | 520   |
 | 263372  | v1:4     | null  | null | unlabelled | bier    | 520   |
 | 503223  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 597052  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 683940  | v1:6     | null  | null | unlabelled | local   | 0     |
 | 839929  | tester:6 | null  | null | unlabelled | local   | 0     |
 | 972928  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 999767  | tester:4 | null  | null | unlabelled | local   | 0     |
 | 1037574 | tester:6 | null  | null | unlabelled | local   | 0     |
 |_________|__________|_______|______|____________|_________|_______|
r4#
r4#
```

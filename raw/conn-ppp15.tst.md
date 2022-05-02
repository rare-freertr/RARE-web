# Example: ppp labeled gateway

## **Topology diagram**

![topology](/img/conn-ppp15.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz39r1-log.run
!
aaa userlist usr
 username c
 username c password $v10$Yw==
 exit
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 1234:: ffff:: all 1234:: ffff:: all
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
interface serial1
 encapsulation ppp
 ppp authentication usr
 ppp ip4cp open
 ppp ip4cp peer 1.1.1.2
 ppp ip4cp local 1.1.1.1
 ppp ip6cp open
 ppp ip6cp peer 0000-0000-0000-0002
 ppp ip6cp local 0000-0000-0000-0001
 ppp ip6cp keep
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 no ipv4 unreachables
 ipv4 gateway-labeled explicit-null
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff:ffff:ffff:ffff::
 no ipv6 unreachables
 ipv6 gateway-labeled explicit-null
 ipv6 access-group-in test6
 mpls enable
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
logging file debug ../binTmp/zzz39r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 1234:: ffff:: all 1234:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
prefix-list p6
 sequence 10 permit 1234::1/128 ge 128 le 128
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 encapsulation ppp
 ppp username c
 ppp password $v10$Yw==
 ppp ip4cp open
 ppp ip4cp local 0.0.0.0
 ppp ip6cp open
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.255
 no ipv4 unreachables
 ipv4 gateway-labeled explicit-null
 ipv4 access-group-in test4
 ipv6 address fe80::20c:1eff:fe14:164a ffff:ffff:ffff:ffff::
 no ipv6 unreachables
 ipv6 gateway-labeled explicit-null
 ipv6 gateway-prefix p6
 ipv6 access-group-in test6
 ipv6 slaac-client enable
 mpls enable
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

# Example: ppp address propagation

## **Topology diagram**

![topology](/img/conn-ppp14.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz62r1-log.run
!
aaa userlist usr
 username c
 username c password $v10$Yw==
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
 no description
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
 ipv6 address 1234::1 ffff:ffff:ffff:ffff::
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
logging file debug ../binTmp/zzz62r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation ppp
 ppp username c
 ppp password $v10$Yw==
 ppp ip4cp open
 ppp ip4cp local 0.0.0.0
 ppp ip6cp open
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.255
 ipv6 address fe80::27e:2fff:fe31:7468 ffff:ffff:ffff:ffff::
 ipv6 slaac
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

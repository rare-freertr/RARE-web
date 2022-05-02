# Example: ppp no local address

## **Topology diagram**

![topology](/img/conn-ppp17.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz55r1-log.run
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
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 2222::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
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
 no ipv4 gateway-connected
 no ipv4 gateway-local
 ipv6 address 1234::1 ffff:ffff:ffff:ffff::
 no ipv6 gateway-connected
 no ipv6 gateway-local
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
logging file debug ../binTmp/zzz55r2-log.run
!
prefix-list p4
 sequence 10 permit 2.2.2.1/32 ge 32 le 32
 exit
!
prefix-list p6
 sequence 10 permit 2222::1/128 ge 128 le 128
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 1.1.1.0 255.255.255.252
 ipv6 address 1234:: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
 no shutdown
 no log-link-change
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
 ipv4 gateway-prefix p4
 ipv6 address fe80::27a:18ff:fe00:3c28 ffff:ffff:ffff:ffff::
 ipv6 gateway-prefix p6
 ipv6 slaac-client enable
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

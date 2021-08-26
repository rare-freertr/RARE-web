# Example: interworking with ethernet over packet over udp

## **Topology diagram**

![topology](/img/conn-pckou15.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz58r1-log.run
!
bridge 1
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
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
server pckoudp pou
 no clone
 bridge 1
 vrf v1
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
logging file debug ../binTmp/zzz58r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 006c.5952.7e6b
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff:ffff::
 pseudowire v1 ethernet1 pckoudp 1.1.1.1 2554
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
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

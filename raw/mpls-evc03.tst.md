# Example: bridged evcs over gre

## **Topology diagram**

![topology](/img/mpls-evc03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz75r1-log.run
!
bridge 1
 exit
!
bridge 2
 exit
!
bridge 3
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
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1111::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1112::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1113::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source serial1
 tunnel destination 2.2.2.2
 tunnel mode gre
 no shutdown
 no log-link-change
 exit
!
interface tunnel1.11
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface tunnel1.12
 bridge-group 2
 no shutdown
 no log-link-change
 exit
!
interface tunnel1.13
 bridge-group 3
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
logging file debug ../binTmp/zzz75r2-log.run
!
bridge 1
 exit
!
bridge 2
 exit
!
bridge 3
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
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1112::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi3
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1113::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source serial1
 tunnel destination 2.2.2.1
 tunnel mode gre
 service-instance 11 bridge-group 1
 service-instance 12 bridge-group 2
 service-instance 13 bridge-group 3
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

# Example: xconnect terminated on pwhe xconnect evcs

## **Topology diagram**

![topology](/img/mpls-evc10.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz44r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1111::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1112::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1113::1 ffff::
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
logging file debug ../binTmp/zzz44r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 xconnect v1 ethernet2 vxlan 2.2.2.2 123
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 2222::1 ffff::
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
logging file debug ../binTmp/zzz44r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 2222::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.0
 ipv6 address 3333::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 mtu 1500
 macaddr 0055.4357.3744
 service-instance 11 xconnect v1 ethernet2 vxlan 3.3.3.2 123
 service-instance 12 xconnect v1 ethernet2 geneve 3.3.3.2 123
 service-instance 13 xconnect v1 ethernet2 etherip 3.3.3.2 123
 pseudowire v1 ethernet1 vxlan 2.2.2.1 123
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
logging file debug ../binTmp/zzz44r4-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.0
 ipv6 address 3333::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface pwether11
 mtu 1500
 macaddr 0024.704e.621e
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff::
 pseudowire v1 ethernet1 vxlan 3.3.3.1 123
 no shutdown
 no log-link-change
 exit
!
interface pwether12
 mtu 1500
 macaddr 006a.1c32.734e
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1112::2 ffff::
 pseudowire v1 ethernet1 geneve 3.3.3.1 123
 no shutdown
 no log-link-change
 exit
!
interface pwether13
 mtu 1500
 macaddr 006d.1f64.6d23
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1113::2 ffff::
 pseudowire v1 ethernet1 etherip 3.3.3.1 123
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

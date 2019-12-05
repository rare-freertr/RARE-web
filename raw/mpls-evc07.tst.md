# Example: xconnect evcs terminated on pwhes

## **Topology diagram**

![topology](/img/mpls-evc07.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1111::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1112::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.13
 no description
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 service-instance 11 xconnect v1 ethernet2 vxlan 2.2.2.2 123
 service-instance 12 xconnect v1 ethernet2 geneve 2.2.2.2 123
 service-instance 13 xconnect v1 ethernet2 etherip 2.2.2.2 123
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
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
end
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 2222::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface pwether11
 no description
 mtu 1500
 macaddr 0077.2044.5a11
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff::
 pseudowire v1 ethernet1 vxlan 2.2.2.1 123
 no shutdown
 no log-link-change
 exit
!
interface pwether12
 no description
 mtu 1500
 macaddr 0006.7379.3c7a
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1112::2 ffff::
 pseudowire v1 ethernet1 geneve 2.2.2.1 123
 no shutdown
 no log-link-change
 exit
!
interface pwether13
 no description
 mtu 1500
 macaddr 005c.5864.4a2f
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1113::2 ffff::
 pseudowire v1 ethernet1 etherip 2.2.2.1 123
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

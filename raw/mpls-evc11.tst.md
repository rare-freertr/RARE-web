# Example: xconnect evcs terminated on vpdns

## **Topology diagram**

![topology](/img/mpls-evc11.tst.png)

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
bridge 11
 exit
!
bridge 12
 exit
!
bridge 13
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi12
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1112::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi13
 no description
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1113::2 ffff::
 no shutdown
 no log-link-change
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
proxy-profile p1
 vrf v1
 exit
!
vpdn bvi11
 bridge-group 11
 proxy p1
 target 2.2.2.1
 vcid 123
 protocol vxlan
 exit
!
vpdn bvi12
 bridge-group 12
 proxy p1
 target 2.2.2.1
 vcid 123
 protocol geneve
 exit
!
vpdn bvi13
 bridge-group 13
 proxy p1
 target 2.2.2.1
 vcid 123
 protocol etherip
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

# Example: interop1: dhcp server

## **Topology diagram**

![topology](/img/intop1-dhcp01.tst.png)

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
server dhcp4 dh
 pool 1.1.1.11 1.1.1.99
 gateway 1.1.1.1
 netmask 255.255.255.0
 no dns-server
 domain-name 
 static 0000.0000.2222 1.1.1.2
 interface ethernet1
 vrf v1
 exit
!
server dhcp6 dh
 no dns-server
 domain-name 
 static 0000.0000.2222 1234::2
 interface ethernet1
 vrf v1
 exit
!
!
end
```

**r2:**
```
hostname r2
ip routing
ipv6 unicast-routing
interface loop0
 ipv6 address fe80::1 link-local
 ipv6 enable
 ipv6 address prefix ::/128
 exit
interface gigabit1
 ip address dhcp
 ipv6 address fe80::1 link-local
 ipv6 enable
 ipv6 dhcp client pd hint 1234::2/128
 ipv6 dhcp client pd prefix
 no shutdown
 exit
```

## **Verification**

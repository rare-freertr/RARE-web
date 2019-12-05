# Example: interop9: dot1q encapsulation

## **Topology diagram**

![topology](/img/intop9-eth02.tst.png)

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
interface ethernet1.123
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
end
```

**r2:**
```
hostname r2
set interfaces ge-0/0/0 vlan-tagging
set interfaces ge-0/0/0.123 vlan-id 123
set interfaces ge-0/0/0.123 family inet address 1.1.1.2/24
set interfaces ge-0/0/0.123 family inet6 address 1234::2/64
commit
```

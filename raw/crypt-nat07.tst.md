# Example: ipv4-ipv6 protocol translation

## **Topology diagram**

![topology](/img/crypt-nat07.tst.png)

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
 ipv4 address 1.1.1.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
!
!
!
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
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address 1234::101:106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel key 120
 tunnel vrf v1
 tunnel source ethernet2
 tunnel destination 1234::101:101
 tunnel mode 6to4
 vrf forwarding v1
 ipv4 address 1.1.1.0 255.255.255.0
 ipv6 address 1234::101:100 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
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
 ipv6 address 1234::101:105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffc
 no shutdown
 no log-link-change
 exit
!
!
!
ipv6 route v1 :: :: 1234::101:106
!
!
!
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

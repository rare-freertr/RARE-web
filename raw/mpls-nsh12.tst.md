# Example: nsh ip

## **Topology diagram**

![topology](/img/mpls-nsh12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list test4
 sequence 10 permit all 1.1.1.1 255.255.255.255 all any all
 exit
!
access-list test6
 sequence 10 permit all 1111::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1111::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 nsh enable
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
ipv4 pbr v1 sequence 10 test4 v1 nsh 2 255
!
ipv6 pbr v1 sequence 10 test6 v1 nsh 2 255
!
!
!
!
!
nsh 2 255 interface ethernet1 0000.1111.2222
!
nsh 3 253 route v1
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
interface ethernet1
 no description
 nsh enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 nsh enable
 no shutdown
 no log-link-change
 exit
!
nsh 2 254 interface ethernet2 0000.1111.2222
!
nsh 3 254 interface ethernet1 0000.1111.2222
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
access-list test4
 sequence 10 permit all 1.1.1.2 255.255.255.255 all any all
 exit
!
access-list test6
 sequence 10 permit all 1111::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1111::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 nsh enable
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
ipv4 pbr v1 sequence 10 test4 v1 nsh 3 255
!
ipv6 pbr v1 sequence 10 test6 v1 nsh 3 255
!
!
!
!
!
nsh 2 253 route v1
!
nsh 3 255 interface ethernet1 0000.1111.2222
!
!
end
```

## **Verification**

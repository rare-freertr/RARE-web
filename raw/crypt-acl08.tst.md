# Example: egress bridged access list

## **Topology diagram**

![topology](/img/crypt-acl08.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list test4
 sequence 10 deny all 1.1.1.2 255.255.255.255 all 1.1.1.3 255.255.255.255 all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 1234::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
 sequence 20 permit all any all any all
 exit
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 bridge-filter ipv4out test4
 bridge-filter ipv6out test6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
 bridge-filter ipv4out test4
 bridge-filter ipv6out test6
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
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff:ffff::
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
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff:ffff::
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

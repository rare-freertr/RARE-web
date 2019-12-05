# Example: ingress source matching hibryd access list

## **Topology diagram**

![topology](/img/crypt-acl21.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
object-group network test4
 sequence 10 2.2.2.102 255.255.255.255
 sequence 20 2.2.2.202 255.255.255.255
 exit
!
object-group network test6
 sequence 10 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 sequence 20 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
!
access-list test4
 sequence 10 deny all obj test4 all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all obj test6 all any all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.101 255.255.255.255
 ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.102 255.255.255.255
 ipv6 address 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 access-group-in test4
 ipv6 address 1234::1 ffff:ffff::
 ipv6 access-group-in test6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
ipv6 route v1 :: :: 1234::2
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.201 255.255.255.255
 ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.202 255.255.255.255
 ipv6 address 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1
!
ipv6 route v1 :: :: 1234::1
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

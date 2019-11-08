# Example: static routing with tcp tracker

## **Topology diagram**

![topology](/img/rout-static04.tst.png)

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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.101 255.255.255.255
 ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
tracker t1
 mode tcp
 target 1.1.2.2
 vrf v1
 interval 1000
 timeout 500
 size 23
 start
 exit
!
tracker t2
 mode tcp
 target 1234:2::2
 vrf v1
 interval 1000
 timeout 500
 size 23
 start
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.2 distance 11 tracker t1
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2 distance 22
!
ipv6 route v1 :: :: 1234:2::2 distance 11 tracker t2
ipv6 route v1 :: :: 1234:1::2 distance 22
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
server telnet tel
 no exec authorization
 no login authentication
 vrf v1
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
tracker t1
 mode tcp
 target 1.1.2.1
 vrf v1
 interval 1000
 timeout 500
 size 23
 start
 exit
!
tracker t2
 mode tcp
 target 1234:2::1
 vrf v1
 interval 1000
 timeout 500
 size 23
 start
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.1 distance 11 tracker t1
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1 distance 22
!
ipv6 route v1 :: :: 1234:2::1 distance 11 tracker t2
ipv6 route v1 :: :: 1234:1::1 distance 22
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
server telnet tel
 no exec authorization
 no login authentication
 vrf v1
 exit
!
!
end
```

## **Verification**

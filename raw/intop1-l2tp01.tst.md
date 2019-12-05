# Example: interop1: l2tp2 client

## **Topology diagram**

![topology](/img/intop1-l2tp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
prefix-list p1
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface dialer1
 no description
 encapsulation ppp
 ppp ip4cp local 0.0.0.0
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.0
 ipv4 gateway-prefix p1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn l2tp
 interface dialer1
 proxy p1
 target 1.1.1.2
 called 1234
 calling 4321
 direction incoming
 protocol l2tp2
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
ip routing
ipv6 unicast-routing
interface Loopback0
 ip address 2.2.2.1 255.255.255.255
 exit
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 no shutdown
 exit
ip local pool p1 2.2.2.11 2.2.2.99
interface virtual-template1
 ip unnumbered Loopback0
 peer default ip address pool p1
 exit
vpdn enable
vpdn-group 1
 accept-dialin
  protocol l2tp
  virtual-template 1
 no l2tp tunnel authentication
 exit
```

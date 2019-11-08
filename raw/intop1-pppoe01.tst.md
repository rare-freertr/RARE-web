# Example: interop1: pppoe client

## **Topology diagram**

![topology](/img/intop1-pppoe01.tst.png)

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
 p2poe client dialer1
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
ip routing
ipv6 unicast-routing
interface Loopback0
 ip address 2.2.2.1 255.255.255.255
 exit
ip local pool p1 2.2.2.11 2.2.2.99
interface virtual-template1
 ip unnumbered Loopback0
 peer default ip address pool p1
 exit
vpdn enable
bba-group pppoe global
 virtual-template 1
 ac name inet
 exit
interface gigabit1
 pppoe enable group global
 no shutdown
 exit
```

## **Verification**

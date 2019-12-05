# Example: interop1: ethernet tunneling with l2tp3

## **Topology diagram**

![topology](/img/intop1-l2tp04.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 mac-learn
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff:ffff::
 no shutdown
 no log-link-change
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
server l2tp3 l2tp
 no clone
 bridge 1
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
interface gigabit2
 ip address 1.1.1.2 255.255.255.0
 no shutdown
 exit
vpdn enable
l2tp-class l2tpc
 exit
pseudowire-class l2tp
 encapsulation l2tpv3
 protocol l2tpv3ietf l2tpc
 ip local interface gigabit2
 exit
interface gigabit1
 xconnect 1.1.1.1 1234 pw-class l2tp
 no shutdown
 exit
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
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
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

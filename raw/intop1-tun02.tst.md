# Example: interop1: ipip tunnel

## **Topology diagram**

![topology](/img/intop1-tun02.tst.png)

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
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1.1.1.2
 tunnel mode ipip
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 2222::1 ffff::
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
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2/64
 no shutdown
 exit
interface tunnel1
 tunnel source gigabit1
 tunnel destination 1.1.1.1
 tunnel mode ipip
 ip address 2.2.2.2 255.255.255.0
 exit
interface tunnel2
 tunnel source gigabit1
 tunnel destination 1.1.1.1
 tunnel mode ipv6ip
 ipv6 address 2222::2/64
 exit
```

## **Verification**

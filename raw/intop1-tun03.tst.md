# Example: interop1: vxlan tunnel

## **Topology diagram**

![topology](/img/intop1-tun03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
 macaddr 0000.0000.1234
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv4 host-static 2.2.2.2 0000.0000.4321
 ipv6 address 2222::1 ffff::
 ipv6 host-static 2222::2 0000.0000.4321
 no shutdown
 no log-link-change
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
proxy-profile p1
 vrf v1
 exit
!
vpdn bvi1
 bridge-group 1
 proxy p1
 target 1.1.1.2
 vcid 1111
 pwtype atm-port
 protocol vxlan
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
vxlan source-port-range dummy-l2-tunnel-udp 4789 4789
interface Tunnel1
 tunnel source gigabit1
 tunnel destination 1.1.1.1
 tunnel mode vxlan ipv4 0000.0000.4321 0000.0000.1234
 tunnel vxlan vni 1111
 ip address 2.2.2.2 255.255.255.252
 ipv6 address 2222::2/64
 exit
```

## **Verification**

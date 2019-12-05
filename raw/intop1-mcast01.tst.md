# Example: interop1: igmp3/mld2

## **Topology diagram**

![topology](/img/intop1-mcast01.tst.png)

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
 ipv4 address 2.2.2.1 255.255.255.255
 ipv4 multicast host-enable
 ipv4 multicast host-proxy
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 ipv6 multicast host-enable
 ipv6 multicast host-proxy
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 multicast host-enable
 ipv4 multicast host-proxy
 ipv6 address fe80::1 ffff::
 ipv6 multicast host-enable
 ipv6 multicast host-proxy
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff fe80::2
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
ip multicast-routing distributed
ipv6 multicast-routing
ip pim ssm default
interface loopback0
 ip addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 ip pim sparse-mode
 ip igmp version 3
 ipv6 pim
 exit
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 ipv6 enable
 ipv6 address fe80::2 link-local
 ip pim sparse-mode
 ip igmp version 3
 ipv6 pim
 ip igmp join-group 232.2.2.2 source 2.2.2.1
 ipv6 mld join-group ff06::1 4321::1
 no shutdown
 exit
ip route 2.2.2.1 255.255.255.255 1.1.1.1
ipv6 route 4321::1/128 gigabit1 fe80::1
```

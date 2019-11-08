# Example: interop1: dhcp client

## **Topology diagram**

![topology](/img/intop1-dhcp02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
prefix-list p4
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
!
prefix-list p6
 sequence 10 permit ::/0 ge 0 le 0
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 0.0.0.0 255.255.255.255
 ipv4 gateway-prefix p4
 ipv4 dhcp-client enable
 ipv4 dhcp-client early
 ipv6 address fe80::200:ff:fe00:1111 ffff:ffff:ffff:ffff::
 ipv6 gateway-prefix p6
 ipv6 dhcp-client enable
 ipv6 dhcp-client prefix
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
ipv6 local pool dhcpv6 1234:1234:1234::/40 48
ipv6 dhcp pool dhcpv6
 prefix-delegation pool dhcpv6 lifetime 1800 1800
 exit
interface loop0
 ipv6 address 4321::1/128
 exit
interface gigabit1
 ip address 1.1.1.1 255.255.255.0
 ipv6 enable
 ipv6 dhcp server dhcpv6
 no shutdown
 exit
ip dhcp pool p1
 network 1.1.1.0 255.255.255.0
 default-router 1.1.1.1
 exit
```

## **Verification**

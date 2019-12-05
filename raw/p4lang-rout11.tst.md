# Example: p4lang: vpn with bgp over srv6

## **Topology diagram**

![topology](/img/p4lang-rout11.tst.png)

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
 label-mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
vrf definition v9
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
 vrf forwarding v2
 ipv4 address 3.3.3.101 255.255.255.255
 ipv6 address 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback9
 no description
 vrf forwarding v9
 ipv4 address 10.10.10.227 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v9
 ipv4 address 10.11.12.254 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface sdn1
 no description
 mtu 1500
 macaddr 0010.411e.4737
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 enable
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 no description
 mtu 1500
 macaddr 000d.1357.0640
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 enable
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 004b.4d2a.1710
 vrf forwarding v2
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 enable
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 0006.1769.2749
 vrf forwarding v2
 ipv4 address 1.1.4.1 255.255.255.0
 ipv6 address 1234:4::1 ffff:ffff::
 ipv6 enable
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source sdn1
 tunnel destination 4444:1::
 tunnel mode srv6
 vrf forwarding v1
 ipv6 address 4444:1:: ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family vpnuni
 template a remote-as 1
 no template a description
 template a local-as 1
 template a address-family vpnuni
 template a distance 200
 template a update-source loopback0
 template a segrout
 template a route-reflector-client
 template a send-community standard extended
 neighbor 2.2.2.103 template a
 neighbor 2.2.2.104 template a
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family vpnuni
 template a remote-as 1
 no template a description
 template a local-as 1
 template a address-family vpnuni
 template a distance 200
 template a update-source loopback0
 template a segrout
 template a route-reflector-client
 template a send-community standard extended
 neighbor 4321::103 template a
 neighbor 4321::104 template a
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
!
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.2.2
!
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4444:3:: ffff:ffff:: 1234:1::2
ipv6 route v1 4444:4:: ffff:ffff:: 1234:2::2
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
ipv4 route v2 3.3.3.105 255.255.255.255 1.1.3.2
ipv4 route v2 3.3.3.106 255.255.255.255 1.1.4.2
!
ipv6 route v2 3333::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
ipv6 route v2 3333::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
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
!
!
!
!
!
!
!
!
!
server p4lang p4
 export-vrf v1 1
 export-vrf v2 2
 export-port sdn1 1
 export-port sdn2 2
 export-port sdn3 3
 export-port sdn4 4
 export-srv6 tunnel1
 interconnect ethernet2
 vrf v9
 exit
!
server dhcp4 eth1
 pool 10.11.12.1 10.11.12.99
 gateway 10.11.12.254
 netmask 255.255.255.0
 dns-server 10.10.10.227
 domain-name p4l
 static 0000.0000.2222 10.11.12.111
 interface ethernet1
 vrf v9
 exit
!
!
end
```

**r2:**
```
hostname r2
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
 label-mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.103 255.255.255.255
 ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 no description
 vrf forwarding v2
 ipv4 address 3.3.3.103 255.255.255.255
 ipv6 address 3333::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 4444:3::
 tunnel mode srv6
 vrf forwarding v1
 ipv6 address 4444:3:: ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family vpnuni
 neighbor 2.2.2.101 remote-as 1
 no neighbor 2.2.2.101 description
 neighbor 2.2.2.101 local-as 1
 neighbor 2.2.2.101 address-family vpnuni
 neighbor 2.2.2.101 distance 200
 neighbor 2.2.2.101 update-source loopback0
 neighbor 2.2.2.101 segrout
 neighbor 2.2.2.101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family vpnuni
 neighbor 4321::101 remote-as 1
 no neighbor 4321::101 description
 neighbor 4321::101 local-as 1
 neighbor 4321::101 address-family vpnuni
 neighbor 4321::101 distance 200
 neighbor 4321::101 update-source loopback0
 neighbor 4321::101 segrout
 neighbor 4321::101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
!
ipv4 route v1 1.1.2.0 255.255.255.0 1.1.1.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.1.1
!
ipv6 route v1 1234:2:: ffff:ffff:: 1234:1::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4444:1:: ffff:ffff:: 1234:1::1
ipv6 route v1 4444:4:: ffff:ffff:: 1234:1::1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.104 255.255.255.255
 ipv6 address 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 no description
 vrf forwarding v2
 ipv4 address 3.3.3.104 255.255.255.255
 ipv6 address 3333::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 4444:4::
 tunnel mode srv6
 vrf forwarding v1
 ipv6 address 4444:4:: ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.4
 address-family vpnuni
 neighbor 2.2.2.101 remote-as 1
 no neighbor 2.2.2.101 description
 neighbor 2.2.2.101 local-as 1
 neighbor 2.2.2.101 address-family vpnuni
 neighbor 2.2.2.101 distance 200
 neighbor 2.2.2.101 update-source loopback0
 neighbor 2.2.2.101 segrout
 neighbor 2.2.2.101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.4
 address-family vpnuni
 neighbor 4321::101 remote-as 1
 no neighbor 4321::101 description
 neighbor 4321::101 local-as 1
 neighbor 4321::101 address-family vpnuni
 neighbor 4321::101 distance 200
 neighbor 4321::101 update-source loopback0
 neighbor 4321::101 segrout
 neighbor 4321::101 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v2 redistribute static
 exit
!
!
ipv4 route v1 1.1.1.0 255.255.255.0 1.1.2.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.2.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.2.1
!
ipv6 route v1 1234:1:: ffff:ffff:: 1234:2::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4444:1:: ffff:ffff:: 1234:2::1
ipv6 route v1 4444:3:: ffff:ffff:: 1234:2::1
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

**r5:**
```
hostname r5
buggy
!
logging file debug ../binTmp/zzz-log-r5.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.105 255.255.255.255
 ipv6 address 3333::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.3.1
ipv4 route v1 3.3.3.101 255.255.255.255 1.1.3.1
ipv4 route v1 3.3.3.103 255.255.255.255 1.1.3.1
ipv4 route v1 3.3.3.104 255.255.255.255 1.1.3.1
ipv4 route v1 3.3.3.106 255.255.255.255 1.1.3.1
!
ipv6 route v1 1234:4:: ffff:ffff:: 1234:3::1
ipv6 route v1 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 3333::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 3333::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 3333::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
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

**r6:**
```
hostname r6
buggy
!
logging file debug ../binTmp/zzz-log-r6.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.106 255.255.255.255
 ipv6 address 3333::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.4.2 255.255.255.0
 ipv6 address 1234:4::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.3.0 255.255.255.0 1.1.4.1
ipv4 route v1 3.3.3.101 255.255.255.255 1.1.4.1
ipv4 route v1 3.3.3.103 255.255.255.255 1.1.4.1
ipv4 route v1 3.3.3.104 255.255.255.255 1.1.4.1
ipv4 route v1 3.3.3.105 255.255.255.255 1.1.4.1
!
ipv6 route v1 1234:3:: ffff:ffff:: 1234:4::1
ipv6 route v1 3333::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 3333::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 3333::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 3333::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
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

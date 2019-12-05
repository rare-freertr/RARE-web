# Example: interop8: ldp lsp

## **Topology diagram**

![topology](/img/intop8-ldp01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::202:201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6 loopback0
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 003f.336a.3536
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 pseudowire v1 loopback0 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 006a.1178.5f50
 vrf forwarding v1
 ipv4 address 3.3.4.1 255.255.255.252
 pseudowire v1 loopback0 pweompls 4321::202:203 1234
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
!
ipv6 route v1 4321::202:203 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff fe80::200:ff:fe00:2222
ipv6 route v1 4444::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff fe80::200:ff:fe00:2222
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
ip forwarding
ipv6 forwarding
interface lo
 ip addr 2.2.2.2/32
 ipv6 addr 4444::2/128
 exit
interface ens3
 ip address 1.1.1.2/24
 no shutdown
 exit
interface ens4
 ip address 1.1.2.2/24
 no shutdown
 exit
ip route 2.2.2.1 255.255.255.255 1.1.1.1
ipv6 route 4321::202:201/128 fe80::1 ens3
ip route 2.2.2.3 255.255.255.255 1.1.2.1
ipv6 route 4321::202:203/128 fe80::4 ens4
mpls ldp
 address-family ipv4
  discovery transport-address 2.2.2.2
  ttl-security disable
  interface ens3
  interface ens4
  exit
 address-family ipv6
  discovery transport-address 4444::2
  ttl-security disable
  interface ens3
  interface ens4
  exit
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::202:203 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 access-group-in test4
 ipv6 address fe80::4 ffff::
 ipv6 access-group-in test6
 mpls enable
 mpls ldp4
 mpls ldp6 loopback0
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0075.3626.4327
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 pseudowire v1 loopback0 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 006c.7838.175e
 vrf forwarding v1
 ipv4 address 3.3.4.2 255.255.255.252
 pseudowire v1 loopback0 pweompls 4321::202:201 1234
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.1 255.255.255.255 1.1.2.2
ipv4 route v1 2.2.2.2 255.255.255.255 1.1.2.2
!
ipv6 route v1 4321::202:201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff fe80::200:ff:fe00:2211
ipv6 route v1 4444::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff fe80::200:ff:fe00:2211
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

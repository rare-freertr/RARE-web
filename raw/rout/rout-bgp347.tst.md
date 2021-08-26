# Example: vpns over srv6 over ibgp

## **Topology diagram**

![topology](/img/rout-bgp347.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz81r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
vrf definition v3
 rd 1:3
 rt-import 1:3
 rt-export 1:3
 exit
!
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 exit
!
interface loopback2
 no description
 vrf forwarding v2
 ipv4 address 9.9.2.1 255.255.255.255
 ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 no description
 vrf forwarding v3
 ipv4 address 9.9.3.1 255.255.255.255
 ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 no description
 vrf forwarding v4
 ipv4 address 9.9.4.1 255.255.255.255
 ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 4321:1::
 tunnel mode srv6
 vrf forwarding v1
 ipv6 address 4321:1:: ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family vpnuni ovpnuni
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family vpnuni ovpnuni
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 segrout
 neighbor 1.1.1.2 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 srv6 tunnel1
 afi-vrf v3 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 srv6 tunnel1
 afi-ovrf v3 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family vpnuni ovpnuni
 neighbor 1234::2 remote-as 1
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family vpnuni ovpnuni
 neighbor 1234::2 distance 200
 neighbor 1234::2 segrout
 neighbor 1234::2 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 srv6 tunnel1
 afi-vrf v4 redistribute connected
 afi-ovrf v2 enable
 afi-ovrf v2 srv6 tunnel1
 afi-ovrf v2 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 srv6 tunnel1
 afi-ovrf v4 redistribute connected
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
!
ipv6 route v1 4321:2:: ffff:ffff:: 1234::2
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
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
logging file debug ../binTmp/zzz81r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
vrf definition v2
 rd 1:2
 rt-import 1:2
 rt-export 1:2
 exit
!
vrf definition v3
 rd 1:3
 rt-import 1:3
 rt-export 1:3
 exit
!
vrf definition v4
 rd 1:4
 rt-import 1:4
 rt-export 1:4
 exit
!
interface loopback2
 no description
 vrf forwarding v2
 ipv4 address 9.9.2.3 255.255.255.255
 ipv6 address 9992::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback3
 no description
 vrf forwarding v3
 ipv4 address 9.9.3.3 255.255.255.255
 ipv6 address 9993::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback4
 no description
 vrf forwarding v4
 ipv4 address 9.9.4.3 255.255.255.255
 ipv6 address 9994::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 4321:2::
 tunnel mode srv6
 vrf forwarding v1
 ipv6 address 4321:2:: ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.2
 address-family vpnuni ovpnuni
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family vpnuni ovpnuni
 neighbor 1.1.1.1 distance 200
 neighbor 1.1.1.1 segrout
 neighbor 1.1.1.1 send-community standard extended
 afi-vrf v3 enable
 afi-vrf v3 srv6 tunnel1
 afi-vrf v3 redistribute connected
 afi-ovrf v3 enable
 afi-ovrf v3 srv6 tunnel1
 afi-ovrf v3 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family vpnuni ovpnuni
 neighbor 1234::1 remote-as 1
 no neighbor 1234::1 description
 neighbor 1234::1 local-as 1
 neighbor 1234::1 address-family vpnuni ovpnuni
 neighbor 1234::1 distance 200
 neighbor 1234::1 segrout
 neighbor 1234::1 send-community standard extended
 afi-vrf v2 enable
 afi-vrf v2 srv6 tunnel1
 afi-vrf v2 redistribute connected
 afi-vrf v4 enable
 afi-vrf v4 srv6 tunnel1
 afi-vrf v4 redistribute connected
 afi-ovrf v2 enable
 afi-ovrf v2 srv6 tunnel1
 afi-ovrf v2 redistribute connected
 afi-ovrf v4 enable
 afi-ovrf v4 srv6 tunnel1
 afi-ovrf v4 redistribute connected
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
!
ipv6 route v1 4321:1:: ffff:ffff:: 1234::1
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

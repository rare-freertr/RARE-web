# Example: olab over srv6 over bgp with soft-reconfig

## **Topology diagram**

![topology](/img/rout-bgp374.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz14r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 address-family olab
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family olab
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 soft-reconfiguration
 neighbor 1.1.1.2 segrout
 afi-other enable
 afi-other srv6 tunnel1
 afi-other redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family olab
 neighbor 1234::2 remote-as 1
 no neighbor 1234::2 description
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family olab
 neighbor 1234::2 distance 200
 neighbor 1234::2 soft-reconfiguration
 neighbor 1234::2 segrout
 afi-other enable
 afi-other srv6 tunnel1
 afi-other redistribute connected
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
logging file debug ../binTmp/zzz14r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
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
 address-family olab
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family olab
 neighbor 1.1.1.1 distance 200
 neighbor 1.1.1.1 soft-reconfiguration
 neighbor 1.1.1.1 segrout
 afi-other enable
 afi-other srv6 tunnel1
 afi-other redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.2
 address-family olab
 neighbor 1234::1 remote-as 1
 no neighbor 1234::1 description
 neighbor 1234::1 local-as 1
 neighbor 1234::1 address-family olab
 neighbor 1234::1 distance 200
 neighbor 1234::1 soft-reconfiguration
 neighbor 1234::1 segrout
 afi-other enable
 afi-other srv6 tunnel1
 afi-other redistribute connected
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

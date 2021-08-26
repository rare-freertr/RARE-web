# Example: bgp routemap filtering with bandwidth with soft-reconfig

## **Topology diagram**

![topology](/img/rout-bgp094.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz99r1-log.run
!
bridge 1
 mac-learn
 exit
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 1
 no neighbor 1.1.1.2 description
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 200
 neighbor 1.1.1.2 soft-reconfiguration
 neighbor 1.1.1.2 traffeng
 neighbor 1.1.1.2 route-reflector-client
 neighbor 1.1.1.3 remote-as 1
 no neighbor 1.1.1.3 description
 neighbor 1.1.1.3 local-as 1
 neighbor 1.1.1.3 address-family unicast
 neighbor 1.1.1.3 distance 200
 neighbor 1.1.1.3 soft-reconfiguration
 neighbor 1.1.1.3 traffeng
 neighbor 1.1.1.3 route-reflector-client
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234:1::2 remote-as 1
 no neighbor 1234:1::2 description
 neighbor 1234:1::2 local-as 1
 neighbor 1234:1::2 address-family unicast
 neighbor 1234:1::2 distance 200
 neighbor 1234:1::2 soft-reconfiguration
 neighbor 1234:1::2 traffeng
 neighbor 1234:1::2 route-reflector-client
 neighbor 1234:1::3 remote-as 1
 no neighbor 1234:1::3 description
 neighbor 1234:1::3 local-as 1
 neighbor 1234:1::3 address-family unicast
 neighbor 1234:1::3 distance 200
 neighbor 1234:1::3 soft-reconfiguration
 neighbor 1234:1::3 traffeng
 neighbor 1234:1::3 route-reflector-client
 redistribute connected
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
logging file debug ../binTmp/zzz99r2-log.run
!
route-map rm1
 sequence 10 action permit
 sequence 10 set bandwidth set 8888
 !
 exit
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
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.2
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 200
 neighbor 1.1.1.1 soft-reconfiguration
 neighbor 1.1.1.1 traffeng
 redistribute connected route-map rm1
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.2
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 200
 neighbor 1234:1::1 soft-reconfiguration
 neighbor 1234:1::1 traffeng
 redistribute connected route-map rm1
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz99r3-log.run
!
route-map rm1
 sequence 10 action deny
 sequence 10 match bandwidth 8888
 !
 sequence 20 action permit
 !
 exit
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234:1::3 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.3
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 no neighbor 1.1.1.1 description
 neighbor 1.1.1.1 local-as 1
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 200
 neighbor 1.1.1.1 soft-reconfiguration
 neighbor 1.1.1.1 traffeng
 neighbor 1.1.1.1 route-map-in rm1
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.3
 address-family unicast
 neighbor 1234:1::1 remote-as 1
 no neighbor 1234:1::1 description
 neighbor 1234:1::1 local-as 1
 neighbor 1234:1::1 address-family unicast
 neighbor 1234:1::1 distance 200
 neighbor 1234:1::1 soft-reconfiguration
 neighbor 1234:1::1 traffeng
 neighbor 1234:1::1 route-map-in rm1
 redistribute connected
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

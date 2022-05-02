# Example: safe ebgp policy with prefixlist

## **Topology diagram**

![topology](/img/rout-bgp568.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz31r1-log.run
!
prefix-list p4
 sequence 10 permit 0.0.0.0/0 ge 0 le 32
 exit
!
prefix-list p6
 sequence 10 permit ::/0 ge 0 le 128
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
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 1
 router-id 4.4.4.1
 address-family unicast
 neighbor 1.1.1.2 remote-as 2
 neighbor 1.1.1.2 local-as 1
 neighbor 1.1.1.2 address-family unicast
 neighbor 1.1.1.2 distance 20
 neighbor 1.1.1.2 prefix-list-in p4
 neighbor 1.1.1.2 prefix-list-out p4
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 1
 router-id 6.6.6.1
 address-family unicast
 neighbor 1234::2 remote-as 2
 neighbor 1234::2 local-as 1
 neighbor 1234::2 address-family unicast
 neighbor 1234::2 distance 20
 neighbor 1234::2 prefix-list-in p6
 neighbor 1234::2 prefix-list-out p6
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
logging file debug ../binTmp/zzz31r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 2
 router-id 4.4.4.2
 no safe-ebgp
 address-family unicast
 neighbor 1.1.1.1 remote-as 1
 neighbor 1.1.1.1 local-as 2
 neighbor 1.1.1.1 address-family unicast
 neighbor 1.1.1.1 distance 20
 redistribute connected
 exit
!
router bgp6 1
 vrf v1
 local-as 2
 router-id 6.6.6.2
 no safe-ebgp
 address-family unicast
 neighbor 1234::1 remote-as 1
 neighbor 1234::1 local-as 2
 neighbor 1234::1 address-family unicast
 neighbor 1234::1 distance 20
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

# Example: qos policer otherflowspec

## **Topology diagram**

![topology](/img/qos-copp17.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz73r1-log.run
!
vrf definition tester
 exit
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz73r2-log.run
!
access-list a4
 sequence 10 permit 1 any all any all
 exit
!
access-list a6
 sequence 10 permit 58 any all any all
 exit
!
policy-map p4
 sequence 10 action police
 sequence 10 match access-group a4
 sequence 10 access-rate 163840
 !
 exit
!
policy-map p6
 sequence 10 action police
 sequence 10 match access-group a6
 sequence 10 access-rate 163840
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
router bgp4 1
 vrf v1
 local-as 0
 router-id 0.0.0.0
 address-family unicast
 afi-other enable
 no afi-other vpn-mode
 afi-other flowspec-install
 afi-other flowspec-advert p6
 exit
!
router bgp6 1
 vrf v1
 local-as 0
 router-id 0.0.0.0
 address-family unicast
 afi-other enable
 no afi-other vpn-mode
 afi-other flowspec-install
 afi-other flowspec-advert p4
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

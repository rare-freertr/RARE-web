# Example: interop1: rip authentication

## **Topology diagram**

![topology](/img/intop1-rip03.tst.png)

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
router rip4 1
 vrf v1
 redistribute connected
 exit
!
router rip6 1
 vrf v1
 redistribute connected
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
 ipv6 address fe80::1 ffff::
 router rip4 1 enable
 router rip4 1 password $v10$dGVzdGVy
 router rip6 1 enable
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
interface loopback0
 ip addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2/128
 exit
router rip
 version 2
 redistribute connected
 no auto-summary
 network 1.0.0.0
 exit
ipv6 router rip 1
 redistribute connected
 exit
key chain kc
 key 0
  key-string tester
 exit
interface gigabit1
 ip address 1.1.1.2 255.255.255.0
 ipv6 enable
 ip rip authentication key-chain kc
 ip rip authentication mode text
 ipv6 rip 1 enable
 no shutdown
 exit
```

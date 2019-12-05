# Example: interop8: isis authentication

## **Topology diagram**

![topology](/img/intop8-isis06.tst.png)

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
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type both
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 password $v10$dGVzdGVy
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address fe80::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 password $v10$dGVzdGVy
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
ip forwarding
ipv6 forwarding
interface lo
 ip addr 2.2.2.2/32
 ipv6 addr 4321::2/128
 exit
router isis 1
 net 48.0000.0000.1234.00
 metric-style wide
 redistribute ipv4 connected level-2
 redistribute ipv6 connected level-2
 exit
interface ens3
 ip address 1.1.1.2/24
 ip router isis 1
 isis network point-to-point
 isis password clear tester
 no shutdown
 exit
interface ens4
 ipv6 router isis 1
 isis network point-to-point
 isis password clear tester
 no shutdown
 exit
```

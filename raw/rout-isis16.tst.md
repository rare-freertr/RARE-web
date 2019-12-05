# Example: isis address suppression

## **Topology diagram**

![topology](/img/rout-isis16.tst.png)

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
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type both
 exit
!
interface loopback11
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback12
 no description
 vrf forwarding v1
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback21
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 router isis4 1 suppress-prefix
 no shutdown
 no log-link-change
 exit
!
interface loopback22
 no description
 vrf forwarding v1
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 router isis6 1 suppress-prefix
 no shutdown
 no log-link-change
 exit
!
interface loopback31
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback32
 no description
 vrf forwarding v1
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv6 address 1234::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
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
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.2222.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.2222.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 vrf forwarding v1
 ipv6 address 1234::2 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
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

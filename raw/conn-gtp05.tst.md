# Example: gtp tunnel

## **Topology diagram**

![topology](/img/conn-gtp05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz80r1-log.run
!
ipv4 pool p4 2.2.2.1 0.0.0.1 254
!
ipv6 pool p6 2222::1111 ::1 254
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
 ipv4 address 4.4.4.4 255.255.255.255
 ipv6 address 4444::4 ffff::
 no shutdown
 no log-link-change
 exit
!
interface dialer1
 encapsulation iponly
 vrf forwarding v1
 ipv4 address 2.2.2.0 255.255.255.255
 ipv4 pool p4
 ipv6 address 2222:: ffff::
 ipv6 pool p6
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
server gtp gtp
 clone dialer1
 vrf v1
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
logging file debug ../binTmp/zzz80r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 1.1.1.1
 tunnel mode gtp
 vrf forwarding v1
 ipv4 address 3.3.3.3 0.0.0.0
 ipv6 address 3333::3333 ::
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

# Example: serial hairpin

## **Topology diagram**

![topology](/img/conn-hairpin02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz22r1-log.run
!
hairpin 1
 no ethernet
 exit
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
 exit
!
interface hairpin11
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface hairpin12
 vrf forwarding v2
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
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
!
!
!
!
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

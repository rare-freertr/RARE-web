# Example: framerelay q933

## **Topology diagram**

![topology](/img/conn-framerelay03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz88r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation framerelay
 framerelay mode dce
 framerelay lmi q933a
 framerelay dlci 123
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
logging file debug ../binTmp/zzz88r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation framerelay
 framerelay mode dte
 framerelay lmi q933a
 framerelay dlci 123
 vrf forwarding v1
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
# Example: pppoe over bridge encapsulation

## **Topology diagram**

![topology](/img/conn-pppoe02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz32r1-log.run
!
ipv4 pool p4 2.2.2.1 0.0.0.1 254
!
bridge 1
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
 ipv4 address 1.1.1.1 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 p2poe server dialer1
 no shutdown
 no log-link-change
 exit
!
interface dialer1
 encapsulation ppp
 ppp ip4cp open
 ppp ip4cp local 2.2.2.0
 vrf forwarding v1
 ipv4 address 2.2.2.0 255.255.255.255
 ipv4 pool p4
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
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
logging file debug ../binTmp/zzz32r2-log.run
!
prefix-list p1
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
!
bridge 1
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 p2poe client dialer1
 no shutdown
 no log-link-change
 exit
!
interface dialer1
 encapsulation ppp
 ppp ip4cp open
 ppp ip4cp local 0.0.0.0
 vrf forwarding v1
 ipv4 address 3.3.3.3 255.255.255.128
 ipv4 gateway-prefix p1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 bridge-group 1
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

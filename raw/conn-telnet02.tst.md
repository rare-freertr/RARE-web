# Example: telnet inspection

## **Topology diagram**

![topology](/img/conn-telnet02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
aaa userlist usr
 no log-error
 username c
 username c password $v10$Yw==
 username c privilege 14
 exit
!
ipv4 pool p4 2.2.2.1 0.0.0.1 254
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface dialer1
 no description
 encapsulation ppp
 ppp ip4cp open
 ppp ip4cp local 2.2.2.0
 vrf forwarding v1
 ipv4 address 2.2.2.0 255.255.255.255
 ipv4 inspect
 ipv4 pool p4
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 ipv4 inspect
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
server telnet tel
 exec interface dialer1
 no exec authorization
 login authentication usr
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
logging file debug ../binTmp/zzz-log-r2.run
!
chat-script login
 sequence 10 recv 5000 .*ser
 sequence 20 send c
 sequence 30 binsend 13
 sequence 40 recv 5000 .*ass
 sequence 50 send c
 sequence 60 binsend 13
 sequence 70 send ppp
 sequence 80 binsend 13
 exit
!
prefix-list p1
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface dialer1
 no description
 encapsulation ppp
 ppp ip4cp open
 ppp ip4cp local 0.0.0.0
 vrf forwarding v1
 ipv4 address 4.4.4.4 255.255.255.128
 ipv4 gateway-prefix p1
 ipv4 inspect
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 ipv4 inspect
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn tel
 interface dialer1
 proxy p1
 script login
 target 3.3.3.1
 vcid 23
 protocol telnet
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

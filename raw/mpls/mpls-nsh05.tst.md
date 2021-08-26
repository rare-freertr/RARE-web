# Example: nsh over ppp

## **Topology diagram**

![topology](/img/mpls-nsh05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz40r1-log.run
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
 ipv6 address 1111::1 ffff::
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
logging file debug ../binTmp/zzz40r2-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 no description
 nsh enable
 nsh xconnect 2 255
 no shutdown
 no log-link-change
 exit
!
interface serial1
 no description
 encapsulation ppp
 nsh enable
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
nsh 2 255 interface serial1 0000.1111.2222
!
nsh 3 254 interface ethernet1 0000.1111.2222 rawpack keephdr
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz40r3-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 no description
 nsh enable
 nsh xconnect 3 255
 no shutdown
 no log-link-change
 exit
!
interface serial1
 no description
 encapsulation ppp
 nsh enable
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
nsh 2 254 interface ethernet1 0000.1111.2222 rawpack keephdr
!
nsh 3 255 interface serial1 0000.1111.2222
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz40r4-log.run
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
 ipv6 address 1111::2 ffff::
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

# Example: nsh loop

## **Topology diagram**

![topology](/img/mpls-nsh10.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz29r1-log.run
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
logging file debug ../binTmp/zzz29r2-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 nsh enable
 nsh xconnect 2 255
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
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
nsh 2 251 interface ethernet2 0000.1111.2222
!
nsh 2 253 interface ethernet2 0000.1111.2222
!
nsh 2 255 interface ethernet2 0000.1111.2222
!
nsh 3 250 interface ethernet1 0000.1111.2222 rawpack keephdr
!
nsh 3 252 interface ethernet2 0000.1111.2222
!
nsh 3 254 interface ethernet2 0000.1111.2222
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
logging file debug ../binTmp/zzz29r3-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 nsh enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 nsh enable
 nsh xconnect 3 255
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
nsh 2 250 interface ethernet2 0000.1111.2222 rawpack keephdr
!
nsh 2 252 interface ethernet1 0000.1111.2222
!
nsh 2 254 interface ethernet1 0000.1111.2222
!
nsh 3 251 interface ethernet1 0000.1111.2222
!
nsh 3 253 interface ethernet1 0000.1111.2222
!
nsh 3 255 interface ethernet1 0000.1111.2222
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
logging file debug ../binTmp/zzz29r4-log.run
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

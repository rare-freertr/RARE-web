# Example: proxy local arp/nd

## **Topology diagram**

![topology](/img/conn-eth14.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz70r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.255
 ipv6 address 1234::9 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 proxy-local
 ipv6 address 1234::1 ffff::
 ipv6 proxy-local
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
logging file debug ../binTmp/zzz70r2-log.run
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
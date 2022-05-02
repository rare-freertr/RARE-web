# Example: p4lang downlink

## **Topology diagram**

![topology](/img/conn-p4lang02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz21r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no shutdown
 no log-link-change
 exit
!
interface sdn1
 mtu 1500
 macaddr 003f.5e62.0322
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
server p4lang p4
 export-vrf v1 1
 export-port sdn1 1 0 0 0 0
 interconnect ethernet1
 downlink 9 ethernet2
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
logging file debug ../binTmp/zzz21r2-log.run
!
hairpin 1
 exit
!
hairpin 2
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface hairpin11
 no shutdown
 no log-link-change
 exit
!
interface hairpin12
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface hairpin21
 no shutdown
 no log-link-change
 exit
!
interface hairpin22
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
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
server pktmux pm
 cpuport ethernet1
 dataport hairpin11 1
 dataport hairpin21 9
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
logging file debug ../binTmp/zzz21r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no shutdown
 no log-link-change
 exit
!
interface sdn1
 mtu 1500
 macaddr 0037.6e04.571c
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff::
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
server p4lang p4
 export-vrf v1 1
 export-port sdn1 9 0 0 0 0
 interconnect ethernet1
 vrf v1
 exit
!
!
end
```

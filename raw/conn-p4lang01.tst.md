# Example: p4lang demultiplexer

## **Topology diagram**

![topology](/img/conn-p4lang01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz4r1-log.run
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
 macaddr 000e.0e3c.0e69
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 mtu 1500
 macaddr 000a.1a4c.3653
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
 export-port sdn1 1 0 0 0 0
 export-port sdn2 9 0 0 0 0
 interconnect ethernet1
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
logging file debug ../binTmp/zzz4r2-log.run
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

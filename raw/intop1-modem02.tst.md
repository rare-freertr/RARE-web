# Example: interop1: modem with ulaw

## **Topology diagram**

![topology](/img/intop1-modem02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
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
server modem sm
 codec ulaw
 no exec authorization
 no login authentication
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
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
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
dial-peer 1
 match-calling .*
 match-called .*
 codec ulaw
 port-local 5060
 vrf v1
 myname 99
 target 1.1.1.1
 direction both
 exit
!
dial-peer 2
 match-calling .*
 match-called .*
 codec ulaw
 port-local 5060
 vrf v1
 myname 99
 target 1.1.2.1
 direction both
 exit
!
!
end
```

**r3:**
```
hostname r3
ip routing
ipv6 unicast-routing
interface gigabit2
 ip address 1.1.3.1 255.255.255.0
 no shutdown
 exit
interface gigabit1
 ip address 1.1.2.1 255.255.255.0
 no shutdown
 exit
voice service voip
 no ip address trusted authenticate

 allow-connections h323 to h323
 allow-connections h323 to sip
 allow-connections sip to h323
 allow-connections sip to sip
sip-ua
 connection-reuse
dial-peer voice 1 voip
 destination-pattern 2[0-9]
 media flow-through
 session protocol sipv2
 session target ipv4:1.1.2.2
 session transport udp
 codec g711ulaw
 no vad
dial-peer voice 2 voip
 destination-pattern 3[0-9]
 media flow-through
 session protocol sipv2
 session target ipv4:1.1.3.2
 session transport udp
 codec g711ulaw
 no vad
```

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.3.2 255.255.255.0
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
translation-rule 1
 match ^.*<sip:(?<n>.*)@(?<d>.*)>.*$
 match ^sip:(?<n>.*)@(?<d>.*)$
 match ^(?<n>.*)$
 text "
 variable n
 text "
 character 32
 text <sip:
 variable n
 text @1.1.3.1>
 exit
!
dial-peer 1
 match-calling .*
 match-called .*
 translate-out-calling 1
 translate-out-called 1
 codec ulaw
 port-local 5060
 vrf v1
 myname 99
 target 1.1.3.1
 direction both
 exit
!
!
end
```

## **Verification**

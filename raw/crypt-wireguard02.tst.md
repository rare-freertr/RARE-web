# Example: wireguard over ipv6

## **Topology diagram**

![topology](/img/crypt-wireguard02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz54r1-log.run
!
crypto ipsec ips
 key $v10$RUZ3MnJKRWRxRkdEZ0M4MHVtM2Z3TW1BYWZ3cVhubytQc2JNSFBaMHVtTT1NNnZEVjhRZGlXRFFwcFZLaktmOHhqb0t0eUdBZVJLL1VlNDhrd0tJNVNzPQ==
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel protection ips
 tunnel source serial1
 tunnel destination 1234::2
 tunnel mode wireguard
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
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz54r2-log.run
!
crypto ipsec ips
 key $v10$NkpoeXZLUHV0UTlETkx1cE9QbURuUUxSV3RVV2xVakk2UFRKL0laOWwxdz1iUU1tcENhR1Z5cTlmK3Y0OFhHbWZINURNTHl0a3F6aUlEK3JCSCtxUWljPQ==
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 tunnel vrf v1
 tunnel protection ips
 tunnel source serial1
 tunnel destination 1234::1
 tunnel mode wireguard
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
!
end
```

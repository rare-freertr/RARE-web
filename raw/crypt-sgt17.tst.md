# Example: sgt over macsec vlan encapsulation

## **Topology diagram**

![topology](/img/crypt-sgt17.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz39r1-log.run
!
crypto ipsec ips
 group 02
 cipher des
 hash md5
 key $v10$dGVzdGVy
 exit
!
policy-map p1
 sequence 10 action drop
 sequence 10 match sgt 123
 !
 sequence 20 action transit
 !
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
 macsec ips
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.123
 sgt enable
 service-policy-in p1
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
!
ipv6 route v1 :: :: 1234::2
!
!
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
logging file debug ../binTmp/zzz39r2-log.run
!
crypto ipsec ips
 group 02
 cipher des
 hash md5
 key $v10$dGVzdGVy
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
 macsec ips
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.123
 sgt enable
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 sgt enable
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz39r3-log.run
!
policy-map p1
 sequence 10 action transit
 sequence 10 match length 300-500
 sequence 10 set sgt set 123
 !
 sequence 20 action transit
 sequence 20 set sgt set 122
 !
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
 sgt enable
 service-policy-out p1
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
ipv4 route v1 0.0.0.0 0.0.0.0 2.2.2.1
!
ipv6 route v1 :: :: 4321::1
!
!
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

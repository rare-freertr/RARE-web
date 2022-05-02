# Example: qos ingress shaper action

## **Topology diagram**

![topology](/img/qos-action11.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz43r1-log.run
!
policy-map p1
 sequence 10 action shape
 sequence 10 access-rate 65536
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
!
!
!
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
logging file debug ../binTmp/zzz43r2-log.run
!
policy-map p1
 sequence 10 action police
 sequence 10 access-rate 81920
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
 service-policy-in p1
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

## **Verification**

```
r2#
r2#
r2#show policy int eth1 in
r2#show policy int eth1 in
 |~~~~~|~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
 | seq | chld | queue | intrvl | byt/int | rxb   | rxp | trnsmt                               |
 |-----|------|-------|--------|---------|-------|-----|--------------------------------------|
 | 10  | 0    | 0/128 | 100    | 1024    | 52214 | 518 | tx=52112(517) rx=52214(518) drp=0(0) |
 |_____|______|_______|________|_________|_______|_____|______________________________________|
r2#
r2#
```

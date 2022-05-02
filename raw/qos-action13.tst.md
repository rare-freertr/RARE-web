# Example: qos ingress hierarchical action

## **Topology diagram**

![topology](/img/qos-action13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz14r1-log.run
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
logging file debug ../binTmp/zzz14r2-log.run
!
policy-map p1
 sequence 10 action police
 sequence 10 access-rate 81920
 !
 exit
!
policy-map p2
 sequence 10 action shape
 sequence 10 access-rate 163840
 sequence 10 service-policy p1
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
 service-policy-in p2
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
 | 10  | 1    | 0/128 | 100    | 2048    | 0     | 0   | tx=0(0) rx=0(0) drp=0(0)             |
 | 10  | 0    | 0/128 | 100    | 1024    | 42014 | 418 | tx=38342(382) rx=42014(418) drp=0(0) |
 |_____|______|_______|________|_________|_______|_____|______________________________________|
r2#
r2#
```

# Example: qos ingress drop action

## **Topology diagram**

![topology](/img/qos-action03.tst.png)

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
policy-map p1
 sequence 10 action drop
 !
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
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
end
```

## **Verification**

```
r2#
r2#
r2#show policy eth1 in
r2#show policy eth1 in
description=
  childs=0, queues=0/128, interval=100, bytes/interval=0
  match=23 packets (3204 bytes)
  transmit=0 packets (0 bytes)
r2#
r2#
```

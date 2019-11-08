# Example: qos ingress hierarchical action

## **Topology diagram**

![topology](/img/qos-action13.tst.png)

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
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
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
end
```

## **Verification**

```
r2#
r2#
r2#show policy eth1 in
r2#show policy eth1 in
description=
  childs=1, queues=0/128, interval=100, bytes/interval=2048
  match=0 packets (0 bytes)
  transmit=0 packets (0 bytes)
description=
  childs=0, queues=0/128, interval=100, bytes/interval=1024
  match=418 packets (57706 bytes)
  transmit=366 packets (50386 bytes)
r2#
r2#
```

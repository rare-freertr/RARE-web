# Example: qos ingress exp set

## **Topology diagram**

![topology](/img/qos-set09.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
policy-map p1
 sequence 10 action drop
 sequence 10 match exp 4
 !
 sequence 20 action transit
 !
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.255
 ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 service-policy-in p1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 3.3.3.2 255.255.255.255 1.1.1.2
!
ipv6 route v1 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
!
!
!
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
 sequence 10 action transit
 sequence 10 match length 300-500
 sequence 10 set exp set 4
 !
 sequence 20 action transit
 sequence 20 set exp set 5
 !
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface ethernet1
 no description
 service-policy-in p1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 service-policy-in p1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 3.3.3.1 255.255.255.255 1.1.1.1
ipv4 route v1 3.3.3.2 255.255.255.255 2.2.2.2
!
ipv6 route v1 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
ipv6 route v1 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 4321::2
!
!
!
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
policy-map p1
 sequence 10 action drop
 sequence 10 match exp 4
 !
 sequence 20 action transit
 !
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.255
 ipv6 address 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 service-policy-in p1
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 3.3.3.1 255.255.255.255 2.2.2.1
!
ipv6 route v1 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 4321::1
!
!
!
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

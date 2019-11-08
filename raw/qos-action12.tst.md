# Example: qos egress shaper action

## **Topology diagram**

![topology](/img/qos-action12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
policy-map p1
 sequence 10 action shape
 sequence 10 access-rate 65536
 !
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 service-policy-out p1
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

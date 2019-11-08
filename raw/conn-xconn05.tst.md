# Example: cross connect atmdxi interfaces

## **Topology diagram**

![topology](/img/conn-xconn05.tst.png)

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
interface serial1
 no description
 encapsulation atmdxi
 atmdxi vpi 1
 atmdxi vci 2
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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
interface serial1
 no description
 encapsulation atmdxi
 atmdxi vpi 1
 atmdxi vci 2
 no shutdown
 no log-link-change
 exit
!
interface serial2
 no description
 encapsulation atmdxi
 atmdxi vpi 1
 atmdxi vci 2
 no shutdown
 no log-link-change
 exit
!
connect con
 side1 serial1
 side2 serial2
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
logging file debug ../binTmp/zzz-log-r3.run
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation atmdxi
 atmdxi vpi 1
 atmdxi vci 2
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
end
```

## **Verification**

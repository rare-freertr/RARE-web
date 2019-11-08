# Example: interop2: dot1ad encapsulation

## **Topology diagram**

![topology](/img/intop2-eth03.tst.png)

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
 encapsulation dot1ad
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.123
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
interface gigabit0/0/0/0
 no shutdown
 exit
interface gigabit0/0/0/0.123
 encapsulation dot1ad 123
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2/64
 exit
root
commit
```

## **Verification**

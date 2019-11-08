# Example: ppp with chap authentication

## **Topology diagram**

![topology](/img/conn-ppp06.tst.png)

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
 encapsulation ppp
 ppp username c
 ppp password $v10$Yw==
 ppp refuseauth eap
 ppp ip4cp close
 ppp ip6cp close
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
aaa userlist usr
 no log-error
 username c
 username c password $v10$Yw==
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface serial1
 no description
 encapsulation ppp
 ppp authentication usr
 ppp refuseauth pap
 ppp ip4cp close
 ppp ip6cp close
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

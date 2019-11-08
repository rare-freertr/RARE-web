# Example: static arp/nd entry

## **Topology diagram**

![topology](/img/conn-eth10.tst.png)

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
 macaddr 0000.0000.1111
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 host-static 1.1.1.2 0000.0000.2222
 ipv6 address 1234::1 ffff::
 ipv6 host-static 1234::2 0000.0000.2222
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
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 macaddr 0000.0000.2222
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 host-static 1.1.1.1 0000.0000.1111
 ipv6 address 1234::2 ffff::
 ipv6 host-static 1234::1 0000.0000.1111
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

# Example: bundle hairpin

## **Topology diagram**

![topology](/img/conn-hairpin03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bundle 1
 exit
!
hairpin 1
 ethernet
 exit
!
vrf definition v1
 rd 1:1
 exit
!
vrf definition v2
 rd 1:2
 exit
!
interface bundle1
 no description
 vrf forwarding v2
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface hairpin11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface hairpin12
 no description
 bundle-group 1
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
!
end
```

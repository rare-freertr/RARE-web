# Example: interop1: pppoe with eap

## **Topology diagram**

![topology](/img/intop1-pppoe05.tst.png)

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
interface dialer1
 no description
 encapsulation ppp
 ppp username usr
 ppp password $v10$cHdk
 ppp ip4cp open
 ppp ip4cp local 2.2.2.1
 ppp ip6cp open
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address fe80::1234 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 p2poe server dialer1
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
ip routing
ipv6 unicast-routing
username usr password pwd
interface dialer1
 encapsulation ppp
 ip address 2.2.2.2 255.255.255.0
 ipv6 address fe80::4321 link-local
 dialer pool 1
 dialer persistent
 ppp authentication eap
 ppp eap local
 exit
interface gigabit1
 pppoe-client dial-pool-number 1
 no shutdown
 exit
```

## **Verification**

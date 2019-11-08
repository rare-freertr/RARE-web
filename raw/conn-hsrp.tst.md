# Example: hsrp over ethernet

## **Topology diagram**

![topology](/img/conn-hsrp.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 mac-learn
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.254
!
ipv6 route v1 :: :: 1234::254
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
bridge 1
 mac-learn
 block-unicast
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv4 hsrp address 1.1.1.254
 ipv4 hsrp group 0
 ipv4 hsrp mac-address 0000.0c9f.f000
 ipv4 hsrp version 2
 ipv4 hsrp timer 3000 10000
 ipv4 hsrp priority 120
 ipv4 hsrp preempt
 no ipv4 hsrp tracker
 ipv6 address 1234::2 ffff::
 ipv6 hsrp address 1234::254
 ipv6 hsrp group 0
 ipv6 hsrp mac-address 0005.73a0.0000
 ipv6 hsrp version 2
 ipv6 hsrp timer 3000 10000
 ipv6 hsrp priority 120
 ipv6 hsrp preempt
 no ipv6 hsrp tracker
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
bridge 1
 mac-learn
 block-unicast
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.0
 ipv6 address 4321::3 ffff::
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv4 hsrp address 1.1.1.254
 ipv4 hsrp group 0
 ipv4 hsrp mac-address 0000.0c9f.f000
 ipv4 hsrp version 2
 ipv4 hsrp timer 3000 10000
 ipv4 hsrp priority 110
 ipv4 hsrp preempt
 no ipv4 hsrp tracker
 ipv6 address 1234::3 ffff::
 ipv6 hsrp address 1234::254
 ipv6 hsrp group 0
 ipv6 hsrp mac-address 0005.73a0.0000
 ipv6 hsrp version 2
 ipv6 hsrp timer 3000 10000
 ipv6 hsrp priority 110
 ipv6 hsrp preempt
 no ipv6 hsrp tracker
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 bridge-group 1
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

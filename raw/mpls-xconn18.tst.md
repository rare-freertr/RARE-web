# Example: cross connect with everything

## **Topology diagram**

![topology](/img/mpls-xconn18.tst.png)

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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.0
 ipv6 address 4321::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet10
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.37 255.255.255.252
 ipv6 address 1234:10::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet4
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.13 255.255.255.252
 ipv6 address 1234:4::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet5
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.17 255.255.255.252
 ipv6 address 1234:5::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet6
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.21 255.255.255.252
 ipv6 address 1234:6::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet7
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.25 255.255.255.252
 ipv6 address 1234:7::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet8
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.29 255.255.255.252
 ipv6 address 1234:8::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet9
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.33 255.255.255.252
 ipv6 address 1234:9::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
proxy-profile p2
 vrf v1
 source loopback0
 exit
!
vpdn dlsw
 bridge-group 1
 proxy p1
 target 1.1.1.38
 vcid 1234
 protocol dlsw
 exit
!
vpdn eip
 bridge-group 1
 proxy p1
 target 1.1.1.26
 vcid 1234
 protocol etherip
 exit
!
vpdn eompls
 bridge-group 1
 proxy p2
 target 3.3.3.3
 mtu 1500
 vcid 1234
 pwtype ethernet
 protocol pweompls
 exit
!
vpdn gnv
 bridge-group 1
 proxy p1
 target 1.1.1.18
 vcid 1234
 protocol geneve
 exit
!
vpdn l2tp
 bridge-group 1
 proxy p1
 target 1.1.1.2
 vcid 1234
 pwtype ethernet
 protocol l2tp3
 exit
!
vpdn ngr
 bridge-group 1
 proxy p1
 target 1.1.1.30
 vcid 1234
 protocol nvgre
 exit
!
vpdn pou
 bridge-group 1
 proxy p1
 target 1.1.1.10
 vcid 1234
 protocol pckoudp
 exit
!
vpdn rspn
 bridge-group 1
 proxy p1
 target 1.1.1.22
 vcid 123
 protocol erspan
 exit
!
vpdn uti
 bridge-group 1
 proxy p1
 target 1.1.1.34
 vcid 1234
 protocol uti
 exit
!
vpdn vxl
 bridge-group 1
 proxy p1
 target 1.1.1.14
 vcid 1234
 protocol vxlan
 exit
!
!
ipv4 route v1 3.3.3.3 255.255.255.255 1.1.1.6
!
ipv6 route v1 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
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
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.0
 ipv6 address 4321::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn l2tp
 bridge-group 1
 proxy p1
 target 1.1.1.1
 vcid 1234
 direction incoming
 pwtype ethernet
 protocol l2tp3
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
 ipv4 address 3.3.3.3 255.255.255.255
 ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.0
 ipv6 address 4321::3 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source loopback0
 exit
!
vpdn eompls
 bridge-group 1
 proxy p1
 target 3.3.3.1
 mtu 1500
 vcid 1234
 pwtype ethernet
 protocol pweompls
 exit
!
!
ipv4 route v1 3.3.3.1 255.255.255.255 1.1.1.5
!
ipv6 route v1 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.0
 ipv6 address 4321::4 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn pou
 bridge-group 1
 proxy p1
 target 1.1.1.9
 vcid 1234
 protocol pckoudp
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

**r5:**
```
hostname r5
buggy
!
logging file debug ../binTmp/zzz-log-r5.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.5 255.255.255.0
 ipv6 address 4321::5 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.14 255.255.255.252
 ipv6 address 1234:4::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
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
server vxlan vxl
 bridge 1
 instance 1234
 vrf v1
 exit
!
!
end
```

**r6:**
```
hostname r6
buggy
!
logging file debug ../binTmp/zzz-log-r6.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.6 255.255.255.0
 ipv6 address 4321::6 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.18 255.255.255.252
 ipv6 address 1234:5::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
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
server geneve gnv
 bridge 1
 vni 1234
 vrf v1
 exit
!
!
end
```

**r7:**
```
hostname r7
buggy
!
logging file debug ../binTmp/zzz-log-r7.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.7 255.255.255.0
 ipv6 address 4321::7 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.22 255.255.255.252
 ipv6 address 1234:6::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn rspn
 bridge-group 1
 proxy p1
 target 1.1.1.21
 vcid 123
 protocol erspan
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

**r8:**
```
hostname r8
buggy
!
logging file debug ../binTmp/zzz-log-r8.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.8 255.255.255.0
 ipv6 address 4321::8 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.26 255.255.255.252
 ipv6 address 1234:7::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn eip
 bridge-group 1
 proxy p1
 target 1.1.1.25
 vcid 1234
 protocol etherip
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

**r9:**
```
hostname r9
buggy
!
logging file debug ../binTmp/zzz-log-r9.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.9 255.255.255.0
 ipv6 address 4321::9 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.30 255.255.255.252
 ipv6 address 1234:8::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn ngr
 bridge-group 1
 proxy p1
 target 1.1.1.29
 vcid 1234
 protocol nvgre
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

**r10:**
```
hostname r10
buggy
!
logging file debug ../binTmp/zzz-log-r10.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.10 255.255.255.0
 ipv6 address 4321::10 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.34 255.255.255.252
 ipv6 address 1234:9::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn uti
 bridge-group 1
 proxy p1
 target 1.1.1.33
 vcid 1234
 protocol uti
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

**r11:**
```
hostname r11
buggy
!
logging file debug ../binTmp/zzz-log-r11.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.11 255.255.255.0
 ipv6 address 4321::11 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.38 255.255.255.252
 ipv6 address 1234:10::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn uti
 bridge-group 1
 proxy p1
 target 1.1.1.37
 vcid 1234
 protocol dlsw
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

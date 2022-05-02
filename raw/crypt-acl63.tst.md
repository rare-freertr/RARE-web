# Example: reflexive access list

## **Topology diagram**

![topology](/img/crypt-acl63.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz27r1-log.run
!
access-list dyn4i
 hidden
 exit
!
access-list dyn4o
 hidden
 exit
!
access-list dyn6i
 hidden
 exit
!
access-list dyn6o
 hidden
 exit
!
access-list test4i
 sequence 10 evaluate permit dyn4i
 sequence 20 deny all any all any all
 exit
!
access-list test4o
 sequence 10 evaluate permit dyn4o
 sequence 20 permit all any all any all
 sequence 20 reflect dyn4o dyn4i 30000
 !
 exit
!
access-list test6i
 sequence 1 permit 58 fe80:: ffff:: all any all
 sequence 2 permit 58 any all fe80:: ffff:: all
 sequence 10 evaluate permit dyn6i
 sequence 20 deny all any all any all
 exit
!
access-list test6o
 sequence 10 evaluate permit dyn6o
 sequence 20 permit all any all any all
 sequence 20 reflect dyn6o dyn6i 30000
 !
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv4 access-group-in test4i
 ipv4 access-group-out test4o
 ipv6 address 1234::1 ffff:ffff::
 ipv6 access-group-in test6i
 ipv6 access-group-out test6o
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz27r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234::2 ffff:ffff::
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
!
end
```

# Example: source port randomization

## **Topology diagram**

![topology](/img/crypt-nat11.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz91r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
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
server telnet tel
 port 666
 no exec authorization
 no login authentication
 vrf v1
 exit
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
logging file debug ../binTmp/zzz91r2-log.run
!
access-list test4
 sequence 10 permit all 1.1.1.4 255.255.255.252 all 1.1.1.0 255.255.255.252 all
 exit
!
access-list test6
 sequence 10 permit all 1234:2:: ffff:ffff:: all 1234:1:: ffff:ffff:: all
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
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
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
ipv4 nat v1 sequence 10 srclist test4 interface ethernet1
ipv4 nat v1 sequence 10 randomize 1024 2048
!
ipv6 nat v1 sequence 10 srclist test6 interface ethernet1
ipv6 nat v1 sequence 10 randomize 1024 2048
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz91r3-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.5
!
ipv6 route v1 :: :: 1234:2::1
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

## **Verification**

```
r2#
r2#
r2#show ipv4 nat v1 tran
r2#show ipv4 nat v1 tran
 |~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|
 |       | original                     | translated                   |                                              |
 | proto | source        | target       | source       | target        | age      | last     | timeout  | pack | byte |
 |-------|---------------|--------------|--------------|---------------|----------|----------|----------|------|------|
 | 6     | 1.1.1.1 666   | 1.1.1.2 2037 | 1.1.1.1 666  | 1.1.1.6 41433 | 00:00:04 | 00:00:02 | 00:05:00 | 14   | 1174 |
 | 6     | 1.1.1.6 41433 | 1.1.1.1 666  | 1.1.1.2 2037 | 1.1.1.1 666   | 00:00:04 | 00:00:02 | 00:05:00 | 12   | 510  |
 |_______|_______________|______________|______________|_______________|__________|__________|__________|______|______|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 nat v1 tran
r2#show ipv6 nat v1 tran
 |~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|
 |       | original                         | translated                       |                                              |
 | proto | source          | target         | source         | target          | age      | last     | timeout  | pack | byte |
 |-------|-----------------|----------------|----------------|-----------------|----------|----------|----------|------|------|
 | 6     | 1234:1::1 666   | 1234:1::2 1578 | 1234:1::1 666  | 1234:2::2 57112 | 00:00:02 | 00:00:00 | 00:05:00 | 12   | 1359 |
 | 6     | 1234:2::2 57112 | 1234:1::1 666  | 1234:1::2 1578 | 1234:1::1 666   | 00:00:02 | 00:00:00 | 00:05:00 | 12   | 752  |
 |_______|_________________|________________|________________|_________________|__________|__________|__________|______|______|
r2#
r2#
```

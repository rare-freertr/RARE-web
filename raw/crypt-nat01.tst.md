# Example: source list translation to interface

## **Topology diagram**

![topology](/img/crypt-nat01.tst.png)

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
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
access-list test4
 sequence 10 permit all any all any all
 exit
!
access-list test6
 sequence 10 permit all 1234:2:: ffff:ffff:: all 1234:1:: ffff:ffff:: all
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
ipv4 nat v1 sequence 10 srclist test4 interface ethernet1
!
ipv6 nat v1 sequence 10 srclist test6 interface ethernet1
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
!
end
```

## **Verification**

```
r2#
r2#
r2#show ipv4 nat v1 tran
r2#show ipv4 nat v1 tran
 |~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|
 | proto | origSrc       | origTrg       | newSrc        | newTrg        |
 |-------|---------------|---------------|---------------|---------------|
 | 1     | 1.1.1.1 14750 | 1.1.1.2 14750 | 1.1.1.1 14750 | 1.1.1.6 14750 |
 | 1     | 1.1.1.6 14750 | 1.1.1.1 14750 | 1.1.1.2 14750 | 1.1.1.1 14750 |
 | 1     | 1.1.1.1 14751 | 1.1.1.2 14751 | 1.1.1.1 14751 | 1.1.1.6 14751 |
 | 1     | 1.1.1.6 14751 | 1.1.1.1 14751 | 1.1.1.2 14751 | 1.1.1.1 14751 |
 | 1     | 1.1.1.1 14752 | 1.1.1.2 14752 | 1.1.1.1 14752 | 1.1.1.6 14752 |
 | 1     | 1.1.1.6 14752 | 1.1.1.1 14752 | 1.1.1.2 14752 | 1.1.1.1 14752 |
 | 1     | 1.1.1.1 14753 | 1.1.1.2 14753 | 1.1.1.1 14753 | 1.1.1.6 14753 |
 | 1     | 1.1.1.6 14753 | 1.1.1.1 14753 | 1.1.1.2 14753 | 1.1.1.1 14753 |
 | 1     | 1.1.1.1 14754 | 1.1.1.2 14754 | 1.1.1.1 14754 | 1.1.1.6 14754 |
 | 1     | 1.1.1.6 14754 | 1.1.1.1 14754 | 1.1.1.2 14754 | 1.1.1.1 14754 |
 | 1     | 1.1.1.1 14755 | 1.1.1.2 14755 | 1.1.1.1 14755 | 1.1.1.6 14755 |
 | 1     | 1.1.1.6 14755 | 1.1.1.1 14755 | 1.1.1.2 14755 | 1.1.1.1 14755 |
 | 1     | 1.1.1.1 14756 | 1.1.1.2 14756 | 1.1.1.1 14756 | 1.1.1.6 14756 |
 | 1     | 1.1.1.6 14756 | 1.1.1.1 14756 | 1.1.1.2 14756 | 1.1.1.1 14756 |
 | 1     | 1.1.1.1 14757 | 1.1.1.2 14757 | 1.1.1.1 14757 | 1.1.1.6 14757 |
 | 1     | 1.1.1.6 14757 | 1.1.1.1 14757 | 1.1.1.2 14757 | 1.1.1.1 14757 |
 | 1     | 1.1.1.1 14758 | 1.1.1.2 14758 | 1.1.1.1 14758 | 1.1.1.6 14758 |
 | 1     | 1.1.1.6 14758 | 1.1.1.1 14758 | 1.1.1.2 14758 | 1.1.1.1 14758 |
 |_______|_______________|_______________|_______________|_______________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 nat v1 tran
r2#show ipv6 nat v1 tran
 |~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~|
 | proto | origSrc       | origTrg       | newSrc        | newTrg        |
 |-------|---------------|---------------|---------------|---------------|
 | 58    | 1234:1::1 539 | 1234:1::2 539 | 1234:1::1 539 | 1234:2::2 539 |
 | 58    | 1234:2::2 539 | 1234:1::1 539 | 1234:1::2 539 | 1234:1::1 539 |
 | 58    | 1234:1::1 540 | 1234:1::2 540 | 1234:1::1 540 | 1234:2::2 540 |
 | 58    | 1234:2::2 540 | 1234:1::1 540 | 1234:1::2 540 | 1234:1::1 540 |
 | 58    | 1234:1::1 541 | 1234:1::2 541 | 1234:1::1 541 | 1234:2::2 541 |
 | 58    | 1234:2::2 541 | 1234:1::1 541 | 1234:1::2 541 | 1234:1::1 541 |
 | 58    | 1234:1::1 542 | 1234:1::2 542 | 1234:1::1 542 | 1234:2::2 542 |
 | 58    | 1234:2::2 542 | 1234:1::1 542 | 1234:1::2 542 | 1234:1::1 542 |
 | 58    | 1234:1::1 543 | 1234:1::2 543 | 1234:1::1 543 | 1234:2::2 543 |
 | 58    | 1234:2::2 543 | 1234:1::1 543 | 1234:1::2 543 | 1234:1::1 543 |
 |_______|_______________|_______________|_______________|_______________|
r2#
r2#
```

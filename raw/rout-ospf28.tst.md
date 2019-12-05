# Example: ospf peer template

## **Topology diagram**

![topology](/img/rout-ospf28.tst.png)

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
router ospf4 1
 vrf v1
 router-id 4.4.4.1
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.1
 traffeng-id ::
 area 0 enable
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 template template1
 no shutdown
 exit
!
interface template1
 no description
 vrf forwarding v1
 ipv4 address 9.9.9.9 255.255.255.0
 ipv6 address 9999::9 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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
router ospf4 1
 vrf v1
 router-id 4.4.4.2
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.2
 traffeng-id ::
 area 0 enable
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 template template1
 no shutdown
 exit
!
interface template1
 no description
 vrf forwarding v1
 ipv4 address 9.9.9.9 255.255.255.0
 ipv6 address 9999::9 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf6 1 enable
 router ospf6 1 area 0
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

```
r2#
r2#
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | address | routerid | uptime   |
 |-----------|---------|----------|----------|
 | ethernet1 | 1.1.1.1 | 4.4.4.1  | 00:00:05 |
 |___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 nei
r2#show ipv6 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | address | routerid | uptime   |
 |-----------|---------|----------|----------|
 | ethernet1 | 1234::1 | 6.6.6.1  | 00:00:05 |
 |___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 dat 0
r2#show ipv4 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid   | sequence | type       | len | time     |
 |----------|---------|----------|------------|-----|----------|
 | 4.4.4.1  | 4.4.4.1 | 80000005 | router     | 40  | 00:00:04 |
 | 4.4.4.2  | 4.4.4.2 | 80000005 | router     | 40  | 00:00:02 |
 | 4.4.4.2  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:06 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:06 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:06 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal | 16  | 00:00:06 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal | 16  | 00:00:06 |
 | 4.4.4.1  | 9.9.9.0 | 80000001 | asExternal | 16  | 00:00:06 |
 | 4.4.4.2  | 9.9.9.0 | 80000001 | asExternal | 16  | 00:00:06 |
 |__________|_________|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 dat 0
r2#show ipv6 ospf 1 dat 0
 |~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
 | routerid | lsaid | sequence | type       | len | time     |
 |----------|-------|----------|------------|-----|----------|
 | 6.6.6.1  | 10012 | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.2  | 10012 | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.1  | 10013 | 80000001 | link       | 24  | 00:00:05 |
 | 6.6.6.2  | 10013 | 80000001 | link       | 24  | 00:00:06 |
 | 6.6.6.1  | 0     | 80000003 | router     | 20  | 00:00:05 |
 | 6.6.6.2  | 0     | 80000003 | router     | 20  | 00:00:02 |
 | 6.6.6.1  | 10012 | 80000001 | prefix     | 20  | 00:00:06 |
 | 6.6.6.2  | 10012 | 80000001 | prefix     | 20  | 00:00:06 |
 | 6.6.6.1  | 10013 | 80000001 | prefix     | 20  | 00:00:05 |
 | 6.6.6.2  | 10013 | 80000001 | prefix     | 20  | 00:00:06 |
 | 6.6.6.1  | 0     | 80000003 | asExternal | 16  | 00:00:06 |
 | 6.6.6.2  | 0     | 80000004 | asExternal | 16  | 00:00:06 |
 | 6.6.6.1  | 1     | 80000002 | asExternal | 28  | 00:00:06 |
 | 6.6.6.2  | 1     | 80000002 | asExternal | 28  | 00:00:06 |
 | 6.6.6.1  | 2     | 80000001 | asExternal | 16  | 00:00:06 |
 | 6.6.6.2  | 2     | 80000001 | asExternal | 16  | 00:00:06 |
 |__________|_______|__________|____________|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 ospf 1 tre 0
r2#show ipv4 ospf 1 tre 0
`--4.4.4.2
   `--4.4.4.1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
`--6.6.6.2/00000000
   `--6.6.6.1/00000000
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:03 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:03 |
 | O   | 2.2.2.1/32 | 110/0  | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:03 |
 | C   | 9.9.9.0/24 | 0/0    | template1 | null    | 00:00:03 |
 | LOC | 9.9.9.9/32 | 0/1    | template1 | null    | 00:00:03 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | C   | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:03 |
 | LOC | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:03 |
 | O   | 4321::1/128 | 110/0  | ethernet1 | 1234::1 | 00:00:03 |
 | C   | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:03 |
 | C   | 9999::/16   | 0/0    | template1 | null    | 00:00:03 |
 | LOC | 9999::9/128 | 0/1    | template1 | null    | 00:00:03 |
 |_____|_____________|________|___________|_________|__________|
r2#
r2#
```

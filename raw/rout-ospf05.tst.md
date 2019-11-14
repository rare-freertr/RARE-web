# Example: ospf nonbroadcast connection

## **Topology diagram**

![topology](/img/rout-ospf05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 exit
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 resend-packet
 ipv6 address 1234::1 ffff::
 ipv6 resend-packet
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 network nonbroadcast
 router ospf4 1 priority 1
 router ospf4 1 hello-time 30000
 router ospf4 1 dead-time 120000
 router ospf4 1 neighbor 1.1.1.2
 router ospf4 1 neighbor 1.1.1.3
 router ospf4 1 neighbor 1.1.1.4
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 network nonbroadcast
 router ospf6 1 priority 1
 router ospf6 1 hello-time 30000
 router ospf6 1 dead-time 120000
 router ospf6 1 neighbor 1234::2
 router ospf6 1 neighbor 1234::3
 router ospf6 1 neighbor 1234::4
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

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
bridge 1
 mac-learn
 exit
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 network nonbroadcast
 router ospf4 1 hello-time 30000
 router ospf4 1 dead-time 120000
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 network nonbroadcast
 router ospf6 1 hello-time 30000
 router ospf6 1 dead-time 120000
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
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router ospf4 1
 vrf v1
 router-id 4.4.4.3
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.3
 traffeng-id ::
 area 0 enable
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234::3 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 network nonbroadcast
 router ospf4 1 hello-time 30000
 router ospf4 1 dead-time 120000
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 network nonbroadcast
 router ospf6 1 hello-time 30000
 router ospf6 1 dead-time 120000
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
router ospf4 1
 vrf v1
 router-id 4.4.4.4
 traffeng-id 0.0.0.0
 area 0 enable
 redistribute connected
 exit
!
router ospf6 1
 vrf v1
 router-id 6.6.6.4
 traffeng-id ::
 area 0 enable
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234::4 ffff::
 router ospf4 1 enable
 router ospf4 1 area 0
 router ospf4 1 network nonbroadcast
 router ospf4 1 hello-time 30000
 router ospf4 1 dead-time 120000
 router ospf6 1 enable
 router ospf6 1 area 0
 router ospf6 1 network nonbroadcast
 router ospf6 1 hello-time 30000
 router ospf6 1 dead-time 120000
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

```
r2#
r2#
r2#show ipv4 ospf 1 nei
r2#show ipv4 ospf 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | interface | address | routerid | uptime   |
 |-----------|---------|----------|----------|
 | bvi1      | 1.1.1.1 | 4.4.4.1  | 00:00:20 |
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
 | bvi1      | 1234::1 | 6.6.6.1  | 00:00:31 |
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
 | 4.4.4.1  | 4.4.4.1 | 80000003 | router     | 16  | 00:00:31 |
 | 4.4.4.2  | 4.4.4.2 | 80000005 | router     | 16  | 00:00:11 |
 | 4.4.4.3  | 4.4.4.3 | 80000005 | router     | 16  | 00:00:11 |
 | 4.4.4.4  | 4.4.4.4 | 80000003 | router     | 16  | 00:00:20 |
 | 4.4.4.1  | 1.1.1.1 | 80000004 | network    | 20  | 00:00:11 |
 | 4.4.4.3  | 0.0.0.0 | 80000002 | asExternal | 16  | 01:00:31 |
 | 4.4.4.4  | 0.0.0.0 | 80000004 | asExternal | 16  | 01:00:30 |
 | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.3  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.4  | 1.1.1.0 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal | 16  | 00:00:31 |
 | 4.4.4.4  | 2.2.2.4 | 80000001 | asExternal | 16  | 00:00:31 |
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
 | 6.6.6.1  | 10012 | 80000002 | link       | 24  | 00:00:31 |
 | 6.6.6.2  | 10012 | 80000001 | link       | 24  | 00:00:32 |
 | 6.6.6.3  | 10012 | 80000001 | link       | 24  | 00:00:31 |
 | 6.6.6.4  | 10012 | 80000001 | link       | 24  | 00:00:31 |
 | 6.6.6.1  | 0     | 80000003 | router     | 20  | 00:00:31 |
 | 6.6.6.2  | 0     | 80000003 | router     | 20  | 00:00:21 |
 | 6.6.6.3  | 0     | 80000003 | router     | 20  | 00:00:21 |
 | 6.6.6.4  | 0     | 80000003 | router     | 20  | 00:00:21 |
 | 6.6.6.1  | 10012 | 80000004 | network    | 20  | 00:00:21 |
 | 6.6.6.1  | 10012 | 80000001 | prefix     | 20  | 00:00:31 |
 | 6.6.6.2  | 10012 | 80000001 | prefix     | 20  | 00:00:32 |
 | 6.6.6.3  | 10012 | 80000001 | prefix     | 20  | 00:00:31 |
 | 6.6.6.4  | 10012 | 80000001 | prefix     | 20  | 00:00:31 |
 | 6.6.6.1  | 0     | 80000002 | asExternal | 16  | 00:00:31 |
 | 6.6.6.2  | 0     | 80000002 | asExternal | 16  | 00:00:32 |
 | 6.6.6.3  | 0     | 80000003 | asExternal | 16  | 00:00:31 |
 | 6.6.6.4  | 0     | 80000002 | asExternal | 16  | 00:00:31 |
 | 6.6.6.1  | 1     | 80000001 | asExternal | 28  | 00:00:31 |
 | 6.6.6.2  | 1     | 80000001 | asExternal | 28  | 00:00:32 |
 | 6.6.6.3  | 1     | 80000001 | asExternal | 28  | 00:00:31 |
 | 6.6.6.4  | 1     | 80000001 | asExternal | 28  | 00:00:31 |
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
   `--1.1.1.1
     |`--4.4.4.1
     |`--4.4.4.3
      `--4.4.4.4
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 ospf 1 tre 0
r2#show ipv6 ospf 1 tre 0
`--6.6.6.1/0000271c
  |`--6.6.6.1/00000000
  |`--6.6.6.3/00000000
   `--6.6.6.4/00000000
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
 | C   | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:11 |
 | LOC | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:11 |
 | O   | 2.2.2.1/32 | 110/0  | bvi1      | 1.1.1.1 | 00:00:11 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:11 |
 | O   | 2.2.2.3/32 | 110/0  | bvi1      | 1.1.1.1 | 00:00:11 |
 | O   | 2.2.2.4/32 | 110/0  | bvi1      | 1.1.1.1 | 00:00:11 |
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
 | C   | 1234::/16   | 0/0    | bvi1      | null    | 00:00:20 |
 | LOC | 1234::2/128 | 0/1    | bvi1      | null    | 00:00:20 |
 | O   | 4321::1/128 | 110/0  | bvi1      | 1234::1 | 00:00:20 |
 | C   | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:20 |
 | O   | 4321::3/128 | 110/0  | bvi1      | 1234::1 | 00:00:20 |
 | O   | 4321::4/128 | 110/0  | bvi1      | 1234::1 | 00:00:20 |
 |_____|_____________|________|___________|_________|__________|
r2#
r2#
```

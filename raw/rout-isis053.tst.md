# Example: isis autoroute

## **Topology diagram**

![topology](/img/rout-isis053.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz38r1-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.11 255.255.255.255
 ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.1 255.255.255.0
 ipv4 access-group-in test4
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface serial2
 encapsulation hdlc
 vrf forwarding v1
 ipv6 address 9999::1 ffff::
 ipv6 access-group-in test6
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface serial3
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.8.1 255.255.255.0
 ipv4 autoroute isis4 1 2.2.2.2 9.9.8.2
 no shutdown
 no log-link-change
 exit
!
interface serial4
 encapsulation hdlc
 vrf forwarding v1
 ipv6 address 9998::1 ffff::
 ipv6 autoroute isis6 1 4321::2 9998::2
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
logging file debug ../binTmp/zzz38r2-log.run
!
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny 58 any all any all
 sequence 20 permit all any all any all
 exit
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 label4mode per-prefix
 label6mode per-prefix
 exit
!
router isis4 1
 vrf v1
 net-id 00.0000.0000.0000.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 00.0000.0000.0000.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
interface loopback0
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.12 255.255.255.255
 ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface serial1
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.9.2 255.255.255.0
 ipv4 access-group-in test4
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface serial2
 encapsulation hdlc
 vrf forwarding v1
 ipv6 address 9999::2 ffff::
 ipv6 access-group-in test6
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface serial3
 encapsulation hdlc
 vrf forwarding v1
 ipv4 address 9.9.8.2 255.255.255.0
 ipv4 autoroute isis4 1 2.2.2.1 9.9.8.1
 no shutdown
 no log-link-change
 exit
!
interface serial4
 encapsulation hdlc
 vrf forwarding v1
 ipv6 address 9998::2 ffff::
 ipv6 autoroute isis6 1 4321::1 9998::1
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

## **Verification**

```
r2#
r2#
r2#show ipv4 isis 1 nei
r2#show ipv4 isis 1 nei
 |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
 | serial1   | 0000.0000.0000 | 2     | 4444.0000.1111 | 9.9.9.1    | ::            | up    | 00:00:21 |
 |___________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 nei
r2#show ipv6 isis 1 nei
 |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
 | serial2   | 0000.0000.0000 | 2     | 6666.0000.1111 | 9999::1    | ::            | up    | 00:00:21 |
 |___________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 dat 2
r2#show ipv4 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
 | lspid                | sequence | flags | len | time     |
 |----------------------|----------|-------|-----|----------|
 | 0000.0000.0000.00-00 | 0000000a | apo   | 65  | 00:19:37 |
 | 4444.0000.1111.00-00 | 00000007 | apo   | 66  | 00:19:37 |
 |______________________|__________|_______|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 dat 2
r2#show ipv6 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
 | lspid                | sequence | flags | len | time     |
 |----------------------|----------|-------|-----|----------|
 | 0000.0000.0000.00-00 | 0000000e | apo   | 91  | 00:19:37 |
 | 6666.0000.1111.00-00 | 00000008 | apo   | 92  | 00:19:37 |
 |______________________|__________|_______|_____|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 tre 2
r2#show ipv4 isis 1 tre 2
`--r2
   `--r1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 tre 2
r2#show ipv6 isis 1 tre 2
`--r2
   `--r1
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 route v1
r2#show ipv4 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface     | hop     | time     |
 |-----|-------------|--------|-----------|---------|----------|
 | I   | 2.2.2.1/32  | 115/10 | serial3   | 9.9.8.1 | 00:00:23 |
 | C   | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:33 |
 | I   | 2.2.2.11/32 | 115/10 | serial3   | 9.9.8.1 | 00:00:23 |
 | C   | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:33 |
 | C   | 9.9.8.0/24  | 0/0    | serial3   | null    | 00:00:29 |
 | LOC | 9.9.8.2/32  | 0/1    | serial3   | null    | 00:00:29 |
 | C   | 9.9.9.0/24  | 0/0    | serial1   | null    | 00:00:29 |
 | LOC | 9.9.9.2/32  | 0/1    | serial1   | null    | 00:00:29 |
 |_____|_____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix       | metric | iface     | hop     | time     |
 |------|--------------|--------|-----------|---------|----------|
 | I EX | 4321::1/128  | 115/10 | serial4   | 9998::1 | 00:00:23 |
 | C    | 4321::2/128  | 0/0    | loopback0 | null    | 00:00:33 |
 | I EX | 4321::11/128 | 115/10 | serial4   | 9998::1 | 00:00:23 |
 | C    | 4321::12/128 | 0/0    | loopback1 | null    | 00:00:33 |
 | C    | 9998::/16    | 0/0    | serial4   | null    | 00:00:29 |
 | LOC  | 9998::2/128  | 0/1    | serial4   | null    | 00:00:29 |
 | C    | 9999::/16    | 0/0    | serial2   | null    | 00:00:29 |
 | LOC  | 9999::2/128  | 0/1    | serial2   | null    | 00:00:29 |
 |______|______________|________|___________|_________|__________|
r2#
r2#
```

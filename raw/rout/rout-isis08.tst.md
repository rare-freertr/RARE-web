# Example: isis over gre

## **Topology diagram**

![topology](/img/rout-isis08.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz9r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type both
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
 ipv4 address 9.9.9.1 255.255.255.252
 ipv6 address 9999::1 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 9999::2
 tunnel mode gre
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 9.9.9.2
 tunnel mode gre
 vrf forwarding v1
 ipv6 address 1234::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
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
logging file debug ../binTmp/zzz9r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.2222.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.2222.00
 traffeng-id ::
 is-type both
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
 ipv4 address 9.9.9.2 255.255.255.252
 ipv6 address 9999::2 ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel1
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 9999::1
 tunnel mode gre
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 no description
 tunnel vrf v1
 tunnel source ethernet1
 tunnel destination 9.9.9.1
 tunnel mode gre
 vrf forwarding v1
 ipv6 address 1234::2 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
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
 | tunnel1   | 0000.0000.0000 | 1     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:04 |
 | tunnel1   | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:04 |
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
 | tunnel2   | 0000.0000.0000 | 1     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:04 |
 | tunnel2   | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:04 |
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
 | 4444.0000.1111.00-00 | 00000009 | apo   | 67  | 00:19:58 |
 | 4444.0000.2222.00-00 | 0000000a | apo   | 67  | 00:19:55 |
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
 | 6666.0000.1111.00-00 | 00000008 | apo   | 92  | 00:19:54 |
 | 6666.0000.2222.00-00 | 00000009 | apo   | 92  | 00:19:54 |
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface     | hop     | time     |
 |-----|------------|--------|-----------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0    | tunnel1   | null    | 00:00:15 |
 | LOC | 1.1.1.2/32 | 0/1    | tunnel1   | null    | 00:00:15 |
 | I   | 2.2.2.1/32 | 115/10 | tunnel1   | 1.1.1.1 | 00:00:04 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:15 |
 | C   | 9.9.9.0/30 | 0/0    | ethernet1 | null    | 00:00:15 |
 | LOC | 9.9.9.2/32 | 0/1    | ethernet1 | null    | 00:00:15 |
 |_____|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop     | time     |
 |------|-------------|--------|-----------|---------|----------|
 | C    | 1234::/16   | 0/0    | tunnel2   | null    | 00:00:15 |
 | LOC  | 1234::2/128 | 0/1    | tunnel2   | null    | 00:00:15 |
 | I EX | 4321::1/128 | 115/10 | tunnel2   | 1234::1 | 00:00:05 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:15 |
 | C    | 9999::/16   | 0/0    | ethernet1 | null    | 00:00:15 |
 | LOC  | 9999::2/128 | 0/1    | ethernet1 | null    | 00:00:15 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

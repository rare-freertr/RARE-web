# Example: isis dynamic icmp metric

## **Topology diagram**

![topology](/img/rout-isis105.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz45r1-log.run
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
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 100
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv6 address 1234::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 100
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet4
 vrf forwarding v1
 ipv6 address 1235::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 1
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
logging file debug ../binTmp/zzz45r2-log.run
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
 is-type level2
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.2222.00
 traffeng-id ::
 is-type level2
 redistribute connected
 exit
!
interface loopback1
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 2
 router isis4 1 dynamic-metric icmpecho
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv6 address 1234::2 ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 2
 router isis6 1 dynamic-metric icmpecho
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 vrf forwarding v1
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1235::2 ffff::
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 metric 200
 router isis4 1 dynamic-metric icmpecho
 no shutdown
 no log-link-change
 exit
!
interface ethernet4
 vrf forwarding v1
 ipv6 address 1235::2 ffff::
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 metric 200
 router isis6 1 dynamic-metric icmpecho
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
 | ethernet3 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.2.1    | ::            | up    | 00:00:01 |
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
 | ethernet4 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1235::1    | ::            | up    | 00:00:02 |
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
 | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:57 |
 | 4444.0000.1111.00-00 | 0000000a | apo   | 55  | 00:19:57 |
 | 4444.0000.2222.00-00 | 0000000b | apo   | 55  | 00:19:58 |
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
 | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:57 |
 | 6666.0000.1111.00-00 | 0000000a | apo   | 68  | 00:19:58 |
 | 6666.0000.2222.00-00 | 0000000f | apo   | 68  | 00:19:58 |
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric  | iface     | hop     | time     |
 |-----|------------|---------|-----------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0     | ethernet1 | null    | 00:00:03 |
 | LOC | 1.1.1.2/32 | 0/1     | ethernet1 | null    | 00:00:03 |
 | C   | 1.1.2.0/24 | 0/0     | ethernet3 | null    | 00:00:02 |
 | LOC | 1.1.2.2/32 | 0/1     | ethernet3 | null    | 00:00:02 |
 | I   | 2.2.2.1/32 | 115/200 | ethernet3 | 1.1.2.1 | 00:00:02 |
 | C   | 2.2.2.2/32 | 0/0     | loopback1 | null    | 00:00:03 |
 |_____|____________|_________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric  | iface     | hop     | time     |
 |------|-------------|---------|-----------|---------|----------|
 | C    | 1234::/16   | 0/0     | ethernet2 | null    | 00:00:03 |
 | LOC  | 1234::2/128 | 0/1     | ethernet2 | null    | 00:00:03 |
 | C    | 1235::/16   | 0/0     | ethernet4 | null    | 00:00:02 |
 | LOC  | 1235::2/128 | 0/1     | ethernet4 | null    | 00:00:02 |
 | I EX | 4321::1/128 | 115/200 | ethernet4 | 1235::1 | 00:00:01 |
 | C    | 4321::2/128 | 0/0     | loopback1 | null    | 00:00:03 |
 |______|_____________|_________|___________|_________|__________|
r2#
r2#
```

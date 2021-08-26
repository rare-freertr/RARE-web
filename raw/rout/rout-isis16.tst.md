# Example: isis address suppression

## **Topology diagram**

![topology](/img/rout-isis16.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz75r1-log.run
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
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id ::
 is-type both
 exit
!
interface loopback11
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback12
 no description
 vrf forwarding v1
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback21
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 router isis4 1 suppress-prefix
 no shutdown
 no log-link-change
 exit
!
interface loopback22
 no description
 vrf forwarding v1
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 router isis6 1 suppress-prefix
 no shutdown
 no log-link-change
 exit
!
interface loopback31
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 router isis4 1 enable
 router isis4 1 passive
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface loopback32
 no description
 vrf forwarding v1
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 passive
 router isis6 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
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
logging file debug ../binTmp/zzz75r2-log.run
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
interface ethernet1
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.11
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
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
 |~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |--------------|----------------|-------|----------------|------------|---------------|-------|----------|
 | ethernet1.11 | 0000.0000.0000 | 1     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:02 |
 | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:02 |
 |______________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 nei
r2#show ipv6 isis 1 nei
 |~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | interface    | mac address    | level | routerid       | ip address | other address | state | uptime   |
 |--------------|----------------|-------|----------------|------------|---------------|-------|----------|
 | ethernet1.12 | 0000.0000.0000 | 1     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:02 |
 | ethernet1.12 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:02 |
 |______________|________________|_______|________________|____________|_______________|_______|__________|
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
 | 4444.0000.1111.00-00 | 00000007 | apo   | 56  | 00:19:57 |
 | 4444.0000.2222.00-00 | 00000006 | apo   | 56  | 00:19:57 |
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
 | 6666.0000.1111.00-00 | 00000007 | apo   | 82  | 00:19:57 |
 | 6666.0000.2222.00-00 | 00000006 | apo   | 82  | 00:19:57 |
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
 |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix     | metric | iface        | hop     | time     |
 |-----|------------|--------|--------------|---------|----------|
 | C   | 1.1.1.0/24 | 0/0    | ethernet1.11 | null    | 00:00:04 |
 | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:04 |
 | I   | 2.2.2.1/32 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:03 |
 | I   | 2.2.2.3/32 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:03 |
 |_____|____________|________|______________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 route v1
r2#show ipv6 route v1
 |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ | prefix      | metric | iface        | hop     | time     |
 |-----|-------------|--------|--------------|---------|----------|
 | C   | 1234::/16   | 0/0    | ethernet1.12 | null    | 00:00:04 |
 | LOC | 1234::2/128 | 0/1    | ethernet1.12 | null    | 00:00:04 |
 | I   | 4321::1/128 | 115/20 | ethernet1.12 | 1234::1 | 00:00:03 |
 | I   | 4321::3/128 | 115/20 | ethernet1.12 | 1234::1 | 00:00:03 |
 |_____|_____________|________|______________|_________|__________|
r2#
r2#
```

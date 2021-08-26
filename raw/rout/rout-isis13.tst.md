# Example: isis broadcast subnet

## **Topology diagram**

![topology](/img/rout-isis13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz70r1-log.run
!
bridge 1
 exit
!
bridge 2
 exit
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv6 address 1234::1 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 bridge-group 2
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
logging file debug ../binTmp/zzz70r2-log.run
!
bridge 1
 mac-learn
 exit
!
bridge 2
 mac-learn
 exit
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
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv6 address 1234::2 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 bridge-group 2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.11
 no description
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet2.12
 no description
 bridge-group 2
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz70r3-log.run
!
bridge 1
 exit
!
bridge 2
 exit
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
 net-id 48.4444.0000.3333.00
 traffeng-id ::
 is-type both
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.3333.00
 traffeng-id ::
 is-type both
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
 router isis4 1 enable
 router isis4 1 circuit both
 router isis4 1 network broadcast
 no shutdown
 no log-link-change
 exit
!
interface bvi2
 no description
 vrf forwarding v1
 ipv6 address 1234::3 ffff::
 router isis6 1 enable
 router isis6 1 circuit both
 router isis6 1 network broadcast
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
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1.12
 no description
 bridge-group 2
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
 | bvi1      | 0019.680e.2a15 | 1     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:08 |
 | bvi1      | 005e.7d6e.1b12 | 1     | 4444.0000.3333 | 1.1.1.3    | ::            | 0     | 00:00:08 |
 | bvi1      | 0019.680e.2a15 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | 0     | 00:00:08 |
 | bvi1      | 005e.7d6e.1b12 | 2     | 4444.0000.3333 | 1.1.1.3    | ::            | 0     | 00:00:08 |
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
 | bvi2      | 0047.2068.7a61 | 1     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:08 |
 | bvi2      | 004c.141b.5b3b | 1     | 6666.0000.3333 | 1234::3    | ::            | 0     | 00:00:08 |
 | bvi2      | 0047.2068.7a61 | 2     | 6666.0000.1111 | 1234::1    | ::            | 0     | 00:00:08 |
 | bvi2      | 004c.141b.5b3b | 2     | 6666.0000.3333 | 1234::3    | ::            | 0     | 00:00:08 |
 |___________|________________|_______|________________|____________|_______________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 dat 2
r2#show ipv4 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
 | lspid                | sequence | flags | len | time      |
 |----------------------|----------|-------|-----|-----------|
 | 4444.0000.1111.00-00 | 0000000b | apo   | 67  | 00:19:50  |
 | 4444.0000.1111.35-00 | 00000002 | apo   | 13  | -00:00:08 |
 | 4444.0000.2222.00-00 | 00000008 | apo   | 67  | 00:19:51  |
 | 4444.0000.2222.28-00 | 00000005 | apo   | 39  | 00:19:51  |
 | 4444.0000.3333.00-00 | 00000009 | apo   | 67  | 00:19:50  |
 | 4444.0000.3333.1b-00 | 00000002 | apo   | 13  | -00:00:08 |
 |______________________|__________|_______|_____|___________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 dat 2
r2#show ipv6 isis 1 dat 2
 |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
 | lspid                | sequence | flags | len | time      |
 |----------------------|----------|-------|-----|-----------|
 | 6666.0000.1111.00-00 | 0000000a | apo   | 106 | 00:19:50  |
 | 6666.0000.1111.12-00 | 00000002 | apo   | 13  | -00:00:08 |
 | 6666.0000.2222.00-00 | 0000000a | apo   | 106 | 00:19:51  |
 | 6666.0000.2222.49-00 | 00000003 | apo   | 39  | 00:19:51  |
 | 6666.0000.3333.00-00 | 0000000a | apo   | 106 | 00:19:50  |
 | 6666.0000.3333.41-00 | 00000002 | apo   | 13  | -00:00:08 |
 |______________________|__________|_______|_____|___________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 isis 1 tre 2
r2#show ipv4 isis 1 tre 2
`--r2
   `--4444.0000.2222.28
     |`--r1
      `--r3
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 isis 1 tre 2
r2#show ipv6 isis 1 tre 2
`--r2
   `--6666.0000.2222.49
     |`--r1
      `--r3
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
 | C   | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:09 |
 | LOC | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:09 |
 | I   | 2.2.2.1/32 | 115/10 | bvi1      | 1.1.1.1 | 00:00:08 |
 | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:09 |
 | I   | 2.2.2.3/32 | 115/10 | bvi1      | 1.1.1.3 | 00:00:08 |
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
 | C    | 1234::/16   | 0/0    | bvi2      | null    | 00:00:09 |
 | LOC  | 1234::2/128 | 0/1    | bvi2      | null    | 00:00:09 |
 | I EX | 4321::1/128 | 115/10 | bvi2      | 1234::1 | 00:00:08 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:09 |
 | I EX | 4321::3/128 | 115/10 | bvi2      | 1234::3 | 00:00:08 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

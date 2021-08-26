# Example: lsrp peer template

## **Topology diagram**

![topology](/img/rout-lsrp15.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz64r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.1
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.1
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
interface template1
 no description
 vrf forwarding v1
 ipv4 address 9.9.9.9 255.255.255.0
 ipv6 address 9999::9 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
logging file debug ../binTmp/zzz64r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 4.4.4.2
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 6.6.6.2
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
interface template1
 no description
 vrf forwarding v1
 ipv4 address 9.9.9.9 255.255.255.0
 ipv6 address 9999::9 ffff::
 router lsrp4 1 enable
 router lsrp6 1 enable
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
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
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
r2#show ipv4 lsrp 1 nei
r2#show ipv4 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:04 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 nei
r2#show ipv6 lsrp 1 nei
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | ready | uptime   |
 |-----------|---------|------|-----------|---------|-------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:09 |
 |___________|_________|______|___________|_________|_______|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp 1 dat
r2#show ipv4 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 4.4.4.1 | r1   | 1   | 3   | 8   | 722ed93c | 00:59:59 |
 | 4.4.4.2 | r2   | 1   | 3   | 10  | efc4fb78 | 00:59:59 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 dat
r2#show ipv6 lsrp 1 dat
 |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | id      | name | nei | net | seq | topo     | left     |
 |---------|------|-----|-----|-----|----------|----------|
 | 6.6.6.1 | r1   | 1   | 3   | 8   | 722ed93c | 00:59:56 |
 | 6.6.6.2 | r2   | 1   | 3   | 10  | efc4fb78 | 00:59:56 |
 |_________|______|_____|_____|_____|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 lsrp
r2#show ipv4 lsrp
r2#show ipv4 lsrp 1 tre
r2#show ipv4 lsrp 1 tre
`--r2
   `--r1
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 lsrp 1 tre
r2#show ipv6 lsrp 1 tre
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
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:09 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:09 |
 | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:09 |
 | C    | 9.9.9.0/24 | 0/0    | template1 | null    | 00:00:09 |
 | LOC  | 9.9.9.9/32 | 0/1    | template1 | null    | 00:00:09 |
 |______|____________|________|___________|_________|__________|
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
 | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:09 |
 | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:09 |
 | L EX | 4321::1/128 | 70/10  | ethernet1 | 1234::1 | 00:00:03 |
 | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:10 |
 | C    | 9999::/16   | 0/0    | template1 | null    | 00:00:09 |
 | LOC  | 9999::9/128 | 0/1    | template1 | null    | 00:00:09 |
 |______|_____________|________|___________|_________|__________|
r2#
r2#
```

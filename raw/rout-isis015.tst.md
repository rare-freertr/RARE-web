# Example: isis updown bit with narrow metric
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    buggy
    !
    logging file debug ../binTmp/zzz66r1-log.run
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
     net-id 11.4444.0000.1111.00
     traffeng-id ::
     is-type level1
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 11.6666.0000.1111.00
     traffeng-id ::
     is-type level1
     no metric-wide
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:1::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level1
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
    logging file debug ../binTmp/zzz66r2-log.run
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
     net-id 11.4444.0000.2222.00
     traffeng-id ::
     is-type both
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 11.6666.0000.2222.00
     traffeng-id ::
     is-type both
     no metric-wide
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:1::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit both
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
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     vrf forwarding v1
     ipv6 address 1234:2::1 ffff:ffff::
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz66r3-log.run
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
     net-id 22.4444.0000.3333.00
     traffeng-id ::
     is-type both
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 22.6666.0000.3333.00
     traffeng-id ::
     is-type both
     no metric-wide
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
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:2::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit both
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
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     vrf forwarding v1
     ipv6 address 1234:3::1 ffff:ffff::
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz66r4-log.run
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
     net-id 22.4444.0000.4444.00
     traffeng-id ::
     is-type level1
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 22.6666.0000.4444.00
     traffeng-id ::
     is-type level1
     no metric-wide
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
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:3::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level1
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
     vrf forwarding v1
     ipv4 address 1.1.1.13 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     vrf forwarding v1
     ipv6 address 1234:4::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level1
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
    
    **r5:**
    ```
    hostname r5
    buggy
    !
    logging file debug ../binTmp/zzz66r5-log.run
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
     net-id 22.4444.0000.5555.00
     traffeng-id ::
     is-type both
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 22.6666.0000.5555.00
     traffeng-id ::
     is-type both
     no metric-wide
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     ipv4 address 1.1.1.14 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:4::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit both
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
     vrf forwarding v1
     ipv4 address 1.1.1.17 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     vrf forwarding v1
     ipv6 address 1234:5::1 ffff:ffff::
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
    
    **r6:**
    ```
    hostname r6
    buggy
    !
    logging file debug ../binTmp/zzz66r6-log.run
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
     net-id 33.4444.0000.6666.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 33.6666.0000.6666.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     ipv4 address 1.1.1.18 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:5::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 nei
    r2#show ipv4 isis 1 nei
     |~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface    | mac address    | level | routerid       | ip address | other address | state | uptime   |
     |--------------|----------------|-------|----------------|------------|---------------|-------|----------|
     | ethernet1.11 | 0000.0000.0000 | 1     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:32 |
     | ethernet2.11 | 0000.0000.0000 | 1     | 4444.0000.3333 | 1.1.1.6    | ::            | down  | 00:00:23 |
     | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | up    | 00:00:23 |
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
     | ethernet1.12 | 0000.0000.0000 | 1     | 6666.0000.1111 | 1234:1::1  | ::            | up    | 00:00:32 |
     | ethernet2.12 | 0000.0000.0000 | 1     | 6666.0000.3333 | 1234:2::2  | ::            | down  | 00:00:33 |
     | ethernet2.12 | 0000.0000.0000 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | up    | 00:00:33 |
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
     | 4444.0000.2222.00-00 | 0000000b | apo   | 81  | 00:19:36 |
     | 4444.0000.3333.00-00 | 0000000c | apo   | 123 | 00:19:39 |
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
     | 6666.0000.2222.00-00 | 0000000b | apo   | 97  | 00:19:26 |
     | 6666.0000.3333.00-00 | 0000000b | apo   | 145 | 00:19:39 |
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
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface        | hop     | time     |
     |------|-------------|--------|--------------|---------|----------|
     | C    | 1.1.1.0/30  | 0/0    | ethernet1.11 | null    | 00:00:34 |
     | LOC  | 1.1.1.2/32  | 0/1    | ethernet1.11 | null    | 00:00:34 |
     | C    | 1.1.1.4/30  | 0/0    | ethernet2.11 | null    | 00:00:34 |
     | LOC  | 1.1.1.5/32  | 0/1    | ethernet2.11 | null    | 00:00:34 |
     | I    | 1.1.1.8/30  | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:24 |
     | I    | 1.1.1.12/30 | 115/30 | ethernet2.11 | 1.1.1.6 | 00:00:24 |
     | I    | 1.1.1.16/30 | 115/40 | ethernet2.11 | 1.1.1.6 | 00:00:21 |
     | I EX | 2.2.2.1/32  | 115/10 | ethernet1.11 | 1.1.1.1 | 00:00:24 |
     | C    | 2.2.2.2/32  | 0/0    | loopback1    | null    | 00:00:34 |
     | I EX | 2.2.2.3/32  | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:24 |
     | I EX | 2.2.2.4/32  | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:24 |
     | I EX | 2.2.2.5/32  | 115/30 | ethernet2.11 | 1.1.1.6 | 00:00:21 |
     |______|_____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface        | hop       | time     |
     |------|---------------|--------|--------------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1.12 | null      | 00:00:38 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1.12 | null      | 00:00:38 |
     | C    | 1234:2::/32   | 0/0    | ethernet2.12 | null      | 00:00:38 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2.12 | null      | 00:00:38 |
     | I    | 1234:3::/32   | 115/20 | ethernet2.12 | 1234:2::2 | 00:00:37 |
     | I    | 1234:4::/32   | 115/30 | ethernet2.12 | 1234:2::2 | 00:00:28 |
     | I    | 1234:5::/32   | 115/40 | ethernet2.12 | 1234:2::2 | 00:00:25 |
     | I EX | 4321::1/128   | 115/10 | ethernet1.12 | 1234:1::1 | 00:00:37 |
     | C    | 4321::2/128   | 0/0    | loopback1    | null      | 00:00:38 |
     | I EX | 4321::3/128   | 115/10 | ethernet2.12 | 1234:2::2 | 00:00:37 |
     | I EX | 4321::4/128   | 115/20 | ethernet2.12 | 1234:2::2 | 00:00:28 |
     | I EX | 4321::5/128   | 115/30 | ethernet2.12 | 1234:2::2 | 00:00:25 |
     |______|_______________|________|______________|___________|__________|
    r2#
    r2#
    ```

# Example: isis narrow metric
    
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
    logging file debug ../binTmp/zzz58r1-log.run
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
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     no metric-wide
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::1 ffff:ffff::
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz58r2-log.run
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
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     no metric-wide
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     vrf forwarding v1
     ipv6 address 1234:2::1 ffff:ffff::
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz58r3-log.run
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
     is-type level2
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.3333.00
     traffeng-id ::
     is-type level2
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:2::2 ffff:ffff::
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
     | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:12 |
     | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | up    | 00:00:12 |
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
     | ethernet1.12 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234:1::1  | ::            | up    | 00:00:12 |
     | ethernet2.12 | 0000.0000.0000 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | up    | 00:00:12 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:46 |
     | 4444.0000.1111.00-00 | 00000006 | apo   | 53  | 00:19:47 |
     | 4444.0000.2222.00-00 | 0000000a | apo   | 81  | 00:19:47 |
     | 4444.0000.3333.00-00 | 00000007 | apo   | 53  | 00:19:56 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:46 |
     | 6666.0000.1111.00-00 | 00000007 | apo   | 61  | 00:19:46 |
     | 6666.0000.2222.00-00 | 00000009 | apo   | 87  | 00:19:47 |
     | 6666.0000.3333.00-00 | 00000007 | apo   | 61  | 00:19:56 |
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
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface        | hop     | time     |
     |------|------------|--------|--------------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:13 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:13 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:13 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:13 |
     | I EX | 2.2.2.1/32 | 115/10 | ethernet1.11 | 1.1.1.1 | 00:00:13 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:13 |
     | I EX | 2.2.2.3/32 | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:04 |
     |______|____________|________|______________|_________|__________|
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
     | C    | 1234:1::/32   | 0/0    | ethernet1.12 | null      | 00:00:14 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1.12 | null      | 00:00:14 |
     | C    | 1234:2::/32   | 0/0    | ethernet2.12 | null      | 00:00:14 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2.12 | null      | 00:00:14 |
     | I EX | 4321::1/128   | 115/10 | ethernet1.12 | 1234:1::1 | 00:00:13 |
     | C    | 4321::2/128   | 0/0    | loopback1    | null      | 00:00:14 |
     | I EX | 4321::3/128   | 115/10 | ethernet2.12 | 1234:2::2 | 00:00:13 |
     |______|_______________|________|______________|___________|__________|
    r2#
    r2#
    ```

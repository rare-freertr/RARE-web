# Example: integrated isis ecmp connection
    
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
    logging file debug ../binTmp/zzz76r1-log.run
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
     is-type level2
     level2 spf-ecmp
     level1 spf-ecmp
     afi-other enable
     afi-other redistribute connected
     afi-other ecmp
     redistribute connected
     ecmp
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
     ipv6 address 1234:1::1 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:21::1 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
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
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.10 255.255.255.252
     ipv6 address 1234:23::2 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
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
    logging file debug ../binTmp/zzz76r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis6 1
     vrf v1
     net-id 22.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     level2 spf-ecmp
     level1 spf-ecmp
     afi-other enable
     afi-other redistribute connected
     afi-other ecmp
     redistribute connected
     ecmp
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
     ipv6 address 1234:1::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:21::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
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
     ipv6 address 1234:2::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.252
     ipv6 address 1234:22::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
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
    logging file debug ../binTmp/zzz76r3-log.run
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
     is-type level2
     level2 spf-ecmp
     level1 spf-ecmp
     afi-other enable
     afi-other redistribute connected
     afi-other ecmp
     redistribute connected
     ecmp
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
     ipv6 address 1234:2::2 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.252
     ipv6 address 1234:22::2 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
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
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.9 255.255.255.252
     ipv6 address 1234:23::1 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
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
    % no such process
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
     | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234:1::1  | 1.1.1.1       | up    | 00:00:11 |
     | ethernet1.22 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234:21::1 | 1.1.2.1       | up    | 00:00:11 |
     | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1234:2::2  | 1.1.1.6       | up    | 00:00:11 |
     | ethernet2.22 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1234:22::2 | 1.1.2.6       | up    | 00:00:11 |
     |______________|________________|_______|________________|____________|_______________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 dat 2
    r2#show ipv4 isis 1 dat 2
    % no such process
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
     | 4444.0000.1111.00-00 | 00000019 | apo   | 191 | 00:19:47 |
     | 4444.0000.3333.00-00 | 00000021 | apo   | 191 | 00:19:47 |
     | 6666.0000.2222.00-00 | 0000001f | apo   | 191 | 00:19:47 |
     |______________________|__________|_______|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 tre 2
    r2#show ipv4 isis 1 tre 2
    % no such process
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
      |`--r1
      |`--r3
       `--r3
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:13 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:13 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:13 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:13 |
     | I   | 1.1.1.8/30 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:13 |
     | I   | 1.1.1.8/30 | 115/20 | ethernet1.22 | 1.1.2.1 | 00:00:13 |
     | I   | 1.1.1.8/30 | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:13 |
     | I   | 1.1.1.8/30 | 115/20 | ethernet2.22 | 1.1.2.6 | 00:00:13 |
     | C   | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:13 |
     | LOC | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:13 |
     | C   | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:13 |
     | LOC | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:13 |
     | I   | 1.1.2.8/30 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:13 |
     | I   | 1.1.2.8/30 | 115/20 | ethernet1.22 | 1.1.2.1 | 00:00:13 |
     | I   | 1.1.2.8/30 | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:13 |
     | I   | 1.1.2.8/30 | 115/20 | ethernet2.22 | 1.1.2.6 | 00:00:13 |
     | I   | 2.2.2.1/32 | 115/10 | ethernet1.11 | 1.1.1.1 | 00:00:13 |
     | I   | 2.2.2.1/32 | 115/10 | ethernet1.22 | 1.1.2.1 | 00:00:13 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:14 |
     | I   | 2.2.2.3/32 | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:13 |
     | I   | 2.2.2.3/32 | 115/10 | ethernet2.22 | 1.1.2.6 | 00:00:13 |
     |_____|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix         | metric | iface        | hop        | time     |
     |------|----------------|--------|--------------|------------|----------|
     | C    | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:14 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:14 |
     | C    | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:13 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:13 |
     | I    | 1234:3::/32    | 115/20 | ethernet1.11 | 1234:1::1  | 00:00:13 |
     | I    | 1234:3::/32    | 115/20 | ethernet1.22 | 1234:21::1 | 00:00:13 |
     | I    | 1234:3::/32    | 115/20 | ethernet2.11 | 1234:2::2  | 00:00:13 |
     | I    | 1234:3::/32    | 115/20 | ethernet2.22 | 1234:22::2 | 00:00:13 |
     | C    | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:14 |
     | LOC  | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:14 |
     | C    | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:13 |
     | LOC  | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:13 |
     | I    | 1234:23::/32   | 115/20 | ethernet1.11 | 1234:1::1  | 00:00:13 |
     | I    | 1234:23::/32   | 115/20 | ethernet1.22 | 1234:21::1 | 00:00:13 |
     | I    | 1234:23::/32   | 115/20 | ethernet2.11 | 1234:2::2  | 00:00:13 |
     | I    | 1234:23::/32   | 115/20 | ethernet2.22 | 1234:22::2 | 00:00:13 |
     | I EX | 4321::1/128    | 115/10 | ethernet1.11 | 1234:1::1  | 00:00:13 |
     | I EX | 4321::1/128    | 115/10 | ethernet1.22 | 1234:21::1 | 00:00:13 |
     | C    | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:14 |
     | I EX | 4321::3/128    | 115/10 | ethernet2.11 | 1234:2::2  | 00:00:13 |
     | I EX | 4321::3/128    | 115/10 | ethernet2.22 | 1234:22::2 | 00:00:13 |
     |______|________________|________|______________|____________|__________|
    r2#
    r2#
    ```

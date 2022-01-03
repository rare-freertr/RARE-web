# Example: integrated isis address unsuppression
    
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
    logging file debug ../binTmp/zzz1r1-log.run
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
     level2 suppress-prefix
     level2 other-suppress-prefix
     level1 suppress-prefix
     level1 other-suppress-prefix
     afi-other enable
     exit
    !
    interface loopback11
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 passive
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface loopback21
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 passive
     router isis4 1 circuit level2
     router isis4 1 unsuppress-prefix
     router isis4 1 other-unsuppress-prefix
     no shutdown
     no log-link-change
     exit
    !
    interface loopback31
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 passive
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
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
    logging file debug ../binTmp/zzz1r2-log.run
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
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     afi-other enable
     afi-other redistribute connected
     redistribute connected
     exit
    !
    interface loopback11
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 passive
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
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
     |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
     |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
     | ethernet1 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234::1    | 1.1.1.1       | up    | 00:00:04 |
     |___________|________________|_______|________________|____________|_______________|_______|__________|
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
     | 4444.0000.1111.00-00 | 00000005 | apo   | 60  | 00:19:54 |
     | 6666.0000.2222.00-00 | 0000000f | apo   | 80  | 00:19:54 |
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
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface      | hop     | time     |
     |-----|--------------|--------|------------|---------|----------|
     | C   | 1.1.1.0/24   | 0/0    | ethernet1  | null    | 00:00:06 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1  | null    | 00:00:06 |
     | I   | 2.2.2.2/32   | 115/20 | ethernet1  | 1.1.1.1 | 00:00:02 |
     | C   | 2.2.2.111/32 | 0/0    | loopback11 | null    | 00:00:06 |
     |_____|______________|________|____________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface      | hop     | time     |
     |-----|---------------|--------|------------|---------|----------|
     | C   | 1234::/16     | 0/0    | ethernet1  | null    | 00:00:06 |
     | LOC | 1234::2/128   | 0/1    | ethernet1  | null    | 00:00:06 |
     | I   | 4321::2/128   | 115/20 | ethernet1  | 1234::1 | 00:00:02 |
     | C   | 4321::111/128 | 0/0    | loopback11 | null    | 00:00:06 |
     |_____|_______________|________|____________|_________|__________|
    r2#
    r2#
    ```

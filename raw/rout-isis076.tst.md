# Example: integrated isis inter level egress filtering with prefixlist
    
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
    logging file debug ../binTmp/zzz12r1-log.run
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
     net-id 22.4444.0000.1111.00
     traffeng-id ::
     is-type level2
     afi-other enable
     afi-other redistribute connected
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
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz12r2-log.run
    !
    prefix-list p4
     sequence 10 deny 2.2.2.8/29 ge 29 le 32
     sequence 20 permit 0.0.0.0/0 ge 0 le 32
     exit
    !
    prefix-list p6
     sequence 10 deny 4321::10/124 ge 124 le 128
     sequence 20 permit ::/0 ge 0 le 128
     exit
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
     is-type both
     level2 prefix-list-into p6
     level2 other-prefix-list-into p4
     level1 prefix-list-into p6
     level1 other-prefix-list-into p4
     afi-other enable
     afi-other redistribute connected
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
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 circuit both
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 other-enable
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
    logging file debug ../binTmp/zzz12r3-log.run
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
     is-type level1
     afi-other enable
     afi-other redistribute connected
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
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.13 255.255.255.255
     ipv6 address 4321::13 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level1
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
     | ethernet1 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234:1::1  | 1.1.1.1       | up    | 00:00:07 |
     | ethernet2 | 0000.0000.0000 | 1     | 4444.0000.3333 | 1234:2::2  | 1.1.1.6       | up    | 00:00:07 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:51 |
     | 4444.0000.1111.00-00 | 0000000c | apo   | 118 | 00:19:51 |
     | 6666.0000.2222.00-00 | 00000013 | apo   | 141 | 00:19:52 |
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
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30  | 0/0    | ethernet1 | null    | 00:00:08 |
     | LOC | 1.1.1.2/32  | 0/1    | ethernet1 | null    | 00:00:08 |
     | C   | 1.1.1.4/30  | 0/0    | ethernet2 | null    | 00:00:08 |
     | LOC | 1.1.1.5/32  | 0/1    | ethernet2 | null    | 00:00:08 |
     | I   | 2.2.2.1/32  | 115/10 | ethernet1 | 1.1.1.1 | 00:00:08 |
     | C   | 2.2.2.2/32  | 0/0    | loopback1 | null    | 00:00:08 |
     | I   | 2.2.2.3/32  | 115/10 | ethernet2 | 1.1.1.6 | 00:00:08 |
     | I   | 2.2.2.11/32 | 115/10 | ethernet1 | 1.1.1.1 | 00:00:08 |
     | C   | 2.2.2.12/32 | 0/0    | loopback2 | null    | 00:00:08 |
     | I   | 2.2.2.13/32 | 115/10 | ethernet2 | 1.1.1.6 | 00:00:08 |
     |_____|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:08 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:08 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:08 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:08 |
     | I EX | 4321::1/128   | 115/10 | ethernet1 | 1234:1::1 | 00:00:08 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:08 |
     | I EX | 4321::3/128   | 115/10 | ethernet2 | 1234:2::2 | 00:00:08 |
     | I EX | 4321::11/128  | 115/10 | ethernet1 | 1234:1::1 | 00:00:08 |
     | C    | 4321::12/128  | 0/0    | loopback2 | null      | 00:00:08 |
     | I EX | 4321::13/128  | 115/10 | ethernet2 | 1234:2::2 | 00:00:08 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

# Example: isis with mpolka
    
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
    logging file debug ../binTmp/zzz31r1-log.run
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
     traffeng-id 4.4.4.1
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id 6.6.6.1
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 segrout index 1
     router isis4 1 segrout node
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 segrout index 1
     router isis6 1 segrout node
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
     mpolka enable 1 65536 10
     mpls enable
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::1 ffff:ffff::
     mpolka enable 1 65536 10
     mpls enable
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 2.2.2.3
     tunnel domain-name 2.2.2.2 2.2.2.3 , 2.2.2.3 2.2.2.3 ,
     tunnel mode mpolka
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source loopback2
     tunnel destination 4321::3
     tunnel domain-name 4321::2 4321::3 , 4321::3 4321::3 ,
     tunnel mode mpolka
     vrf forwarding v1
     ipv6 address 3333::1 ffff::
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
    logging file debug ../binTmp/zzz31r2-log.run
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
     traffeng-id 4.4.4.2
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id 6.6.6.2
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 segrout index 2
     router isis4 1 segrout node
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 segrout index 2
     router isis6 1 segrout node
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
     mpolka enable 2 65536 10
     mpls enable
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::2 ffff:ffff::
     mpolka enable 2 65536 10
     mpls enable
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
     mpolka enable 2 65536 10
     mpls enable
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     vrf forwarding v1
     ipv6 address 1234:2::1 ffff:ffff::
     mpolka enable 2 65536 10
     mpls enable
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
    logging file debug ../binTmp/zzz31r3-log.run
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
     traffeng-id 4.4.4.3
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.3333.00
     traffeng-id 6.6.6.3
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 segrout index 3
     router isis4 1 segrout node
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 segrout index 3
     router isis6 1 segrout node
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
     mpolka enable 3 65536 10
     mpls enable
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:2::2 ffff:ffff::
     mpolka enable 3 65536 10
     mpls enable
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 2.2.2.1
     tunnel domain-name 2.2.2.1 2.2.2.1 , 2.2.2.2 2.2.2.1 ,
     tunnel mode mpolka
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source loopback2
     tunnel destination 4321::1
     tunnel domain-name 4321::1 4321::1 , 4321::2 4321::1 ,
     tunnel mode mpolka
     vrf forwarding v1
     ipv6 address 3333::2 ffff::
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
     | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:06 |
     | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | up    | 00:00:16 |
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
     | ethernet1.12 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234:1::1  | ::            | up    | 00:00:16 |
     | ethernet2.12 | 0000.0000.0000 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | up    | 00:00:16 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:42 |
     | 4444.0000.1111.00-00 | 0000000b | apo   | 91  | 00:19:57 |
     | 4444.0000.2222.00-00 | 0000000d | apo   | 111 | 00:19:53 |
     | 4444.0000.3333.00-00 | 0000000e | apo   | 91  | 00:19:58 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:42 |
     | 6666.0000.1111.00-00 | 0000000e | apo   | 104 | 00:19:47 |
     | 6666.0000.2222.00-00 | 0000000f | apo   | 126 | 00:19:43 |
     | 6666.0000.3333.00-00 | 0000000e | apo   | 104 | 00:19:48 |
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
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface        | hop     | time     |
     |-----|------------|--------|--------------|---------|----------|
     | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:17 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:17 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:17 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:17 |
     | I   | 2.2.2.1/32 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:07 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:17 |
     | I   | 2.2.2.3/32 | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:16 |
     | I   | 3.3.3.0/30 | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     |_____|____________|________|______________|_________|__________|
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
     | C    | 1234:1::/32   | 0/0    | ethernet1.12 | null      | 00:00:17 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1.12 | null      | 00:00:17 |
     | C    | 1234:2::/32   | 0/0    | ethernet2.12 | null      | 00:00:17 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2.12 | null      | 00:00:17 |
     | I EX | 3333::/16     | 115/10 | ethernet1.12 | 1234:1::1 | 00:00:12 |
     | I    | 4321::1/128   | 115/20 | ethernet1.12 | 1234:1::1 | 00:00:17 |
     | C    | 4321::2/128   | 0/0    | loopback2    | null      | 00:00:17 |
     | I    | 4321::3/128   | 115/20 | ethernet2.12 | 1234:2::2 | 00:00:16 |
     |______|_______________|________|______________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 segrou v1
    r2#show ipv4 segrou v1
     |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|
     | prefix     | index | base   | oldbase |
     |------------|-------|--------|---------|
     | 2.2.2.1/32 | 1     | 121037 | 121037  |
     | 2.2.2.3/32 | 3     | 386047 | 386047  |
     |____________|_______|________|_________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 segrou v1
    r2#show ipv6 segrou v1
     |~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|
     | prefix      | index | base   | oldbase |
     |-------------|-------|--------|---------|
     | 4321::1/128 | 1     | 674889 | 674889  |
     | 4321::3/128 | 3     | 667388 | 667388  |
     |_____________|_______|________|_________|
    r2#
    r2#
    ```

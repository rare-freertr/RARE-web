# Example: isis multi-topology with bier
    
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
    logging file debug ../binTmp/zzz34r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
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
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 bier index 1
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 bier index 1
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
     ipv4 access-group-in test4
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
     ipv6 access-group-in test6
     mpls enable
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.3
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback2
     tunnel destination 9999::9
     tunnel domain-name 4321::3
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
    logging file debug ../binTmp/zzz34r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
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
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 bier index 2
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 bier index 2
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
     ipv4 access-group-in test4
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
     ipv6 access-group-in test6
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
     ipv4 access-group-in test4
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
     ipv6 access-group-in test6
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
    logging file debug ../binTmp/zzz34r3-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
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
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.3333.00
     traffeng-id ::
     is-type level2
     multi-topology
     bier 256 10
     level2 bier
     level1 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 bier index 3
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 bier index 3
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
     ipv4 access-group-in test4
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
     ipv6 access-group-in test6
     mpls enable
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 3
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.1
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 3
     tunnel vrf v1
     tunnel source loopback2
     tunnel destination 9999::9
     tunnel domain-name 4321::1
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1112 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
     | ethernet1.11 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:13 |
     | ethernet2.11 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1.1.1.6    | ::            | up    | 00:00:13 |
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
     | ethernet1.12 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234:1::1  | ::            | up    | 00:00:13 |
     | ethernet2.12 | 0000.0000.0000 | 2     | 6666.0000.3333 | 1234:2::2  | ::            | up    | 00:00:13 |
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
     | 4444.0000.1111.00-00 | 0000000a | apo   | 83  | 00:19:46 |
     | 4444.0000.2222.00-00 | 0000000c | apo   | 98  | 00:19:46 |
     | 4444.0000.3333.00-00 | 0000000a | apo   | 83  | 00:19:45 |
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
     | 0000.0000.0000.00-00 | 00000001 | apo   | 10  | 00:19:45 |
     | 6666.0000.1111.00-00 | 0000000a | apo   | 110 | 00:19:46 |
     | 6666.0000.2222.00-00 | 0000000b | apo   | 113 | 00:19:46 |
     | 6666.0000.3333.00-00 | 0000000a | apo   | 110 | 00:19:45 |
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:14 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:14 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:14 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:14 |
     | I   | 2.2.2.1/32 | 115/20 | ethernet1.11 | 1.1.1.1 | 00:00:13 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:14 |
     | I   | 2.2.2.3/32 | 115/20 | ethernet2.11 | 1.1.1.6 | 00:00:13 |
     | I   | 3.3.3.0/30 | 115/10 | ethernet2.11 | 1.1.1.6 | 00:00:13 |
     |_____|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix         | metric | iface        | hop       | time     |
     |------|----------------|--------|--------------|-----------|----------|
     | C    | 1234:1::/32    | 0/0    | ethernet1.12 | null      | 00:00:14 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1.12 | null      | 00:00:14 |
     | C    | 1234:2::/32    | 0/0    | ethernet2.12 | null      | 00:00:14 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2.12 | null      | 00:00:14 |
     | I    | 4321::1/128    | 115/20 | ethernet1.12 | 1234:1::1 | 00:00:13 |
     | C    | 4321::2/128    | 0/0    | loopback2    | null      | 00:00:14 |
     | I    | 4321::3/128    | 115/20 | ethernet2.12 | 1234:2::2 | 00:00:13 |
     | I EX | 4321::1110/124 | 115/10 | ethernet2.12 | 1234:2::2 | 00:00:13 |
     |______|________________|________|______________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 bier v1
    r2#show ipv4 bier v1
     |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | prefix     | index | base   | oldbase | size  |
     |------------|-------|--------|---------|-------|
     | 2.2.2.1/32 | 1     | 118352 | 118352  | 3-256 |
     | 2.2.2.3/32 | 3     | 434874 | 434874  | 3-256 |
     |____________|_______|________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bier v1
    r2#show ipv6 bier v1
     |~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | prefix      | index | base   | oldbase | size  |
     |-------------|-------|--------|---------|-------|
     | 4321::1/128 | 1     | 782330 | 782330  | 3-256 |
     | 4321::3/128 | 3     | 293322 | 293322  | 3-256 |
     |_____________|_______|________|_________|_______|
    r2#
    r2#
    ```

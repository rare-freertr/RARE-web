# Example: integrated isis with php sr
    
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
    logging file debug ../binTmp/zzz97r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
     traffeng-id 4.4.4.1
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     afi-other enable
     afi-other redistribute connected
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     router isis4 1 segrout index 1
     router isis4 1 segrout other-index 2
     router isis4 1 segrout node
     router isis4 1 segrout pop
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     no description
     mtu 1500
     macaddr 0066.6e35.757d
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback1 pweompls 2.2.2.3 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 000e.1d58.2722
     vrf forwarding v1
     ipv4 address 3.3.4.1 255.255.255.0
     pseudowire v1 loopback1 pweompls 4321::3 1234
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
    logging file debug ../binTmp/zzz97r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id 6.6.6.2
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     afi-other enable
     afi-other redistribute connected
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 circuit level2
     router isis6 1 segrout index 3
     router isis6 1 segrout other-index 4
     router isis6 1 segrout node
     router isis6 1 segrout pop
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router isis6 1 enable
     router isis6 1 other-enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
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
    logging file debug ../binTmp/zzz97r3-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 4321:: ffff:: all 4321:: ffff:: all
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
     traffeng-id 4.4.4.3
     is-type level2
     segrout 10
     level2 segrout
     level1 segrout
     afi-other enable
     afi-other redistribute connected
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     router isis4 1 segrout index 5
     router isis4 1 segrout other-index 6
     router isis4 1 segrout node
     router isis4 1 segrout pop
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router isis4 1 enable
     router isis4 1 other-enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     no description
     mtu 1500
     macaddr 0040.1f5f.560a
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback1 pweompls 2.2.2.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 0079.6268.2626
     vrf forwarding v1
     ipv4 address 3.3.4.2 255.255.255.0
     pseudowire v1 loopback1 pweompls 4321::1 1234
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
     | ethernet1 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1234:1::1  | 1.1.1.1       | up    | 00:00:36 |
     | ethernet2 | 0000.0000.0000 | 2     | 4444.0000.3333 | 1234:2::2  | 1.1.1.6       | up    | 00:00:36 |
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
     | 4444.0000.1111.00-00 | 0000001b | apo   | 153 | 00:19:22 |
     | 4444.0000.3333.00-00 | 00000019 | apo   | 153 | 00:19:22 |
     | 6666.0000.2222.00-00 | 0000001b | apo   | 183 | 00:19:23 |
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:38 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:38 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:38 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:38 |
     | I   | 2.2.2.1/32 | 115/20 | ethernet1 | 1.1.1.1 | 00:00:37 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:38 |
     | I   | 2.2.2.3/32 | 115/20 | ethernet2 | 1.1.1.6 | 00:00:34 |
     | I   | 3.3.3.0/24 | 115/10 | ethernet2 | 1.1.1.6 | 00:00:34 |
     | I   | 3.3.4.0/24 | 115/10 | ethernet1 | 1.1.1.1 | 00:00:37 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface     | hop       | time     |
     |-----|---------------|--------|-----------|-----------|----------|
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:38 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:38 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:38 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:38 |
     | I   | 4321::1/128   | 115/20 | ethernet1 | 1234:1::1 | 00:00:37 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:38 |
     | I   | 4321::3/128   | 115/20 | ethernet2 | 1234:2::2 | 00:00:34 |
     |_____|_______________|________|___________|___________|__________|
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
     | 2.2.2.1/32 | 1     | 529304 | 529304  |
     | 2.2.2.3/32 | 5     | 588793 | 588793  |
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
     | 4321::1/128 | 2     | 529304 | 529304  |
     | 4321::3/128 | 6     | 588793 | 588793  |
     |_____________|_______|________|_________|
    r2#
    r2#
    ```

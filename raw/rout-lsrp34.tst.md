# Example: lsrp with selective bier
    
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
    logging file debug ../binTmp/zzz6r1-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     bier 256 10 0
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     bier 256 10 0
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp4 1 bier 1
     router lsrp6 1 enable
     router lsrp6 1 bier 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
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
     no description
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
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
    logging file debug ../binTmp/zzz6r2-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     bier 256 10 0
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     bier 256 10 0
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp4 1 bier 2
     router lsrp6 1 enable
     router lsrp6 1 bier 2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    logging file debug ../binTmp/zzz6r3-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.3
     bier 256 10 0
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     bier 256 10 0
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp4 1 bier 3
     router lsrp6 1 enable
     router lsrp6 1 bier 3
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.3 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::3 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
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
     no description
     tunnel key 3
     tunnel vrf v1
     tunnel source loopback1
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
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:17 |
     | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.2.3 | true  | 00:00:17 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:17 |
     | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1235::3 | true  | 00:00:17 |
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
     | 4.4.4.1 | r1   | 1   | 3   | 10  | b2f83345 | 00:59:46 |
     | 4.4.4.2 | r2   | 2   | 3   | 13  | c68f402a | 00:59:47 |
     | 4.4.4.3 | r3   | 1   | 3   | 10  | 7b7cad5a | 00:59:47 |
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
     | 6.6.6.1 | r1   | 1   | 3   | 10  | c81f5462 | 00:59:46 |
     | 6.6.6.2 | r2   | 2   | 3   | 13  | 10358654 | 00:59:46 |
     | 6.6.6.3 | r3   | 1   | 3   | 10  | c2f77457 | 00:59:46 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 tre
    r2#show ipv4 lsrp 1 tre
    `--r2
      |`--r1
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 tre
    r2#show ipv6 lsrp 1 tre
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
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:25 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:25 |
     | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:25 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:25 |
     | L    | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:15 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:25 |
     | L    | 2.2.2.3/32 | 70/10  | ethernet2 | 1.1.2.3 | 00:00:14 |
     | L EX | 3.3.3.0/30 | 70/10  | ethernet2 | 1.1.2.3 | 00:00:14 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix         | metric | iface     | hop     | time     |
     |------|----------------|--------|-----------|---------|----------|
     | C    | 1234::/16      | 0/0    | ethernet1 | null    | 00:00:25 |
     | LOC  | 1234::2/128    | 0/1    | ethernet1 | null    | 00:00:25 |
     | C    | 1235::/16      | 0/0    | ethernet2 | null    | 00:00:25 |
     | LOC  | 1235::2/128    | 0/1    | ethernet2 | null    | 00:00:25 |
     | L    | 4321::1/128    | 70/10  | ethernet1 | 1234::1 | 00:00:15 |
     | C    | 4321::2/128    | 0/0    | loopback1 | null    | 00:00:25 |
     | L    | 4321::3/128    | 70/10  | ethernet2 | 1235::3 | 00:00:15 |
     | L EX | 4321::1110/124 | 70/10  | ethernet2 | 1235::3 | 00:00:15 |
     |______|________________|________|___________|_________|__________|
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
     | 2.2.2.1/32 | 1     | 661687 | 661687  | 3-256 |
     | 2.2.2.3/32 | 3     | 328431 | 328431  | 3-256 |
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
     | 4321::1/128 | 1     | 68307  | 68307   | 3-256 |
     | 4321::3/128 | 3     | 354500 | 354500  | 3-256 |
     |_____________|_______|________|_________|_______|
    r2#
    r2#
    ```

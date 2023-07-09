# Example: pvrp with php labels
    
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
    logging file debug ../binTmp/zzz78r1-log.run
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.1
     labels
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
     labels
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     router pvrp4 1 enable
     router pvrp4 1 label-pop
     router pvrp6 1 enable
     router pvrp6 1 label-pop
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 001b.4151.685b
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback1 pweompls 2.2.2.3 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0049.124e.576d
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
    logging file debug ../binTmp/zzz78r2-log.run
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.2
     labels
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
     labels
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
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router pvrp4 1 enable
     router pvrp4 1 label-pop
     router pvrp6 1 enable
     router pvrp6 1 label-pop
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router pvrp4 1 enable
     router pvrp4 1 label-pop
     router pvrp6 1 enable
     router pvrp6 1 label-pop
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
    logging file debug ../binTmp/zzz78r3-log.run
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.3
     labels
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.3
     labels
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
     vrf forwarding v1
     ipv4 address 1.1.2.3 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::3 ffff::
     ipv6 access-group-in test6
     mpls enable
     router pvrp4 1 enable
     router pvrp4 1 label-pop
     router pvrp6 1 enable
     router pvrp6 1 label-pop
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 0057.6c2e.3c14
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback1 pweompls 2.2.2.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0026.2354.677c
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
    r2#show ipv4 pvrp 1 sum
    r2#show ipv4 pvrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
     |-----------|---------|------|-----------|---------|---------|----------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 3       | 4        | 00:00:27 |
     | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.2.3 | 3       | 4        | 00:00:26 |
     |___________|_________|______|___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 sum
    r2#show ipv6 pvrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
     |-----------|---------|------|-----------|---------|---------|----------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | 1       | 3        | 00:00:27 |
     | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1235::3 | 1       | 3        | 00:00:26 |
     |___________|_________|______|___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 pvrp 1 rou
    r2#show ipv4 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/24 | 1/0    | ethernet1 | null    | 00:00:22 |
     | C    | 1.1.2.0/24 | 1/0    | ethernet2 | null    | 00:00:22 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:24 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:32 |
     | null | 2.2.2.3/32 | 80/10  | ethernet2 | 1.1.2.3 | 00:00:22 |
     | null | 3.3.3.0/24 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:23 |
     | null | 3.3.3.0/24 | 80/10  | ethernet2 | 1.1.2.3 | 00:00:22 |
     | null | 3.3.4.0/24 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:23 |
     | null | 3.3.4.0/24 | 80/10  | ethernet2 | 1.1.2.3 | 00:00:22 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 rou
    r2#show ipv6 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | C    | 1234::/16   | 1/0    | ethernet1 | null    | 00:00:22 |
     | C    | 1235::/16   | 1/0    | ethernet2 | null    | 00:00:22 |
     | null | 4321::1/128 | 80/10  | ethernet1 | 1234::1 | 00:00:23 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null    | 00:00:32 |
     | null | 4321::3/128 | 80/10  | ethernet2 | 1235::3 | 00:00:22 |
     |______|_____________|________|___________|_________|__________|
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
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:32 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:32 |
     | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:32 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:32 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:24 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:32 |
     | P EX | 2.2.2.3/32 | 80/10  | ethernet2 | 1.1.2.3 | 00:00:23 |
     | P EX | 3.3.3.0/24 | 80/10  | ethernet2 | 1.1.2.3 | 00:00:23 |
     | P EX | 3.3.4.0/24 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:24 |
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
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:32 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:32 |
     | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:32 |
     | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:32 |
     | P EX | 4321::1/128 | 80/10  | ethernet1 | 1234::1 | 00:00:23 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:32 |
     | P EX | 4321::3/128 | 80/10  | ethernet2 | 1235::3 | 00:00:22 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

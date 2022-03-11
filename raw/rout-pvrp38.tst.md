# Example: pvrp unstub interface
    
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
    logging file debug ../binTmp/zzz55r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
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
    logging file debug ../binTmp/zzz55r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.2
     stub
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
     stub
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
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 unstub
     router pvrp6 1 enable
     router pvrp6 1 unstub
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 unstub
     router pvrp6 1 enable
     router pvrp6 1 unstub
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
    logging file debug ../binTmp/zzz55r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.3
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.3
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
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
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
    logging file debug ../binTmp/zzz55r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.4
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.4
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
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 5        | 00:00:12 |
     | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.1.6 | 3       | 3        | 00:00:12 |
     |___________|_________|______|___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 sum
    r2#show ipv6 pvrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer      | learned | adverted | uptime   |
     |-----------|---------|------|-----------|-----------|---------|----------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 5        | 00:00:12 |
     | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1234:2::2 | 3       | 3        | 00:00:12 |
     |___________|_________|______|___________|___________|_________|__________|__________|
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
     | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:08 |
     | C    | 1.1.1.4/30 | 1/0    | ethernet2 | null    | 00:00:08 |
     | null | 1.1.1.8/30 | 80/10  | ethernet2 | 1.1.1.6 | 00:00:08 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:08 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:17 |
     | null | 2.2.2.3/32 | 80/10  | ethernet2 | 1.1.1.6 | 00:00:08 |
     | null | 2.2.2.4/32 | 80/20  | ethernet2 | 1.1.1.6 | 00:00:08 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 rou
    r2#show ipv6 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop       | time     |
     |------|-------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:03 |
     | C    | 1234:2::/32 | 1/0    | ethernet2 | null      | 00:00:03 |
     | null | 1234:3::/32 | 80/10  | ethernet2 | 1234:2::2 | 00:00:09 |
     | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:03 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:18 |
     | null | 4321::3/128 | 80/10  | ethernet2 | 1234:2::2 | 00:00:09 |
     | null | 4321::4/128 | 80/20  | ethernet2 | 1234:2::2 | 00:00:08 |
     |______|_____________|________|___________|___________|__________|
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:18 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:18 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:18 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:18 |
     | P    | 1.1.1.8/30 | 80/10  | ethernet2 | 1.1.1.6 | 00:00:09 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:08 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:18 |
     | P EX | 2.2.2.3/32 | 80/10  | ethernet2 | 1.1.1.6 | 00:00:09 |
     | P EX | 2.2.2.4/32 | 80/20  | ethernet2 | 1.1.1.6 | 00:00:09 |
     |______|____________|________|___________|_________|__________|
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:18 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:18 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:18 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:18 |
     | P    | 1234:3::/32   | 80/10  | ethernet2 | 1234:2::2 | 00:00:10 |
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:04 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:18 |
     | P EX | 4321::3/128   | 80/10  | ethernet2 | 1234:2::2 | 00:00:10 |
     | P EX | 4321::4/128   | 80/20  | ethernet2 | 1234:2::2 | 00:00:09 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

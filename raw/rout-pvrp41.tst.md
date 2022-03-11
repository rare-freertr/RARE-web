# Example: pvrp ecmp connection
    
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
    logging file debug ../binTmp/zzz86r1-log.run
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
     ecmp
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
     ecmp
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
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
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:21::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
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
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.10 255.255.255.252
     ipv6 address 1234:23::2 ffff:ffff::
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
    logging file debug ../binTmp/zzz86r2-log.run
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
     redistribute connected
     ecmp
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
     redistribute connected
     ecmp
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:21::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.252
     ipv6 address 1234:22::1 ffff:ffff::
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz86r3-log.run
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
     ecmp
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.3
     redistribute connected
     ecmp
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
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
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.252
     ipv6 address 1234:22::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
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
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.9 255.255.255.252
     ipv6 address 1234:23::1 ffff:ffff::
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
     |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface        | router  | name | peerif       | peer    | learned | adverted | uptime   |
     |--------------|---------|------|--------------|---------|---------|----------|----------|
     | ethernet1.11 | 4.4.4.1 | r1   | ethernet1.11 | 1.1.1.1 | 6       | 8        | 00:00:06 |
     | ethernet1.22 | 4.4.4.1 | r1   | ethernet1.22 | 1.1.2.1 | 6       | 6        | 00:00:06 |
     | ethernet2.11 | 4.4.4.3 | r3   | ethernet1.11 | 1.1.1.6 | 6       | 7        | 00:00:06 |
     | ethernet2.22 | 4.4.4.3 | r3   | ethernet1.22 | 1.1.2.6 | 6       | 7        | 00:00:06 |
     |______________|_________|______|______________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 sum
    r2#show ipv6 pvrp 1 sum
     |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface        | router  | name | peerif       | peer       | learned | adverted | uptime   |
     |--------------|---------|------|--------------|------------|---------|----------|----------|
     | ethernet1.11 | 6.6.6.1 | r1   | ethernet1.11 | 1234:1::1  | 6       | 7        | 00:00:06 |
     | ethernet1.22 | 6.6.6.1 | null | null         | 1234:21::1 | 0       | 0        | 00:00:06 |
     | ethernet2.11 | 6.6.6.3 | null | null         | 1234:2::2  | 0       | 0        | 00:00:07 |
     | ethernet2.22 | 6.6.6.3 | r3   | ethernet1.22 | 1234:22::2 | 6       | 5        | 00:00:06 |
     |______________|_________|______|______________|____________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 pvrp 1 rou
    r2#show ipv4 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface        | hop     | time     |
     |------|------------|--------|--------------|---------|----------|
     | C    | 1.1.1.0/30 | 1/0    | ethernet1.11 | null    | 00:00:00 |
     | C    | 1.1.1.4/30 | 1/0    | ethernet2.11 | null    | 00:00:00 |
     | null | 1.1.1.8/30 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:00 |
     | null | 1.1.1.8/30 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:01 |
     | null | 1.1.1.8/30 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     | null | 1.1.1.8/30 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:01 |
     | C    | 1.1.2.0/30 | 1/0    | ethernet1.22 | null    | 00:00:00 |
     | C    | 1.1.2.4/30 | 1/0    | ethernet2.22 | null    | 00:00:00 |
     | null | 1.1.2.8/30 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:00 |
     | null | 1.1.2.8/30 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:01 |
     | null | 1.1.2.8/30 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     | null | 1.1.2.8/30 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:01 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:00 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1    | null    | 00:00:11 |
     | null | 2.2.2.3/32 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     | null | 2.2.2.3/32 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:01 |
     |______|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 rou
    r2#show ipv6 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface        | hop        | time     |
     |------|--------------|--------|--------------|------------|----------|
     | C    | 1234:1::/32  | 1/0    | ethernet1.11 | null       | 00:00:00 |
     | C    | 1234:2::/32  | 1/0    | ethernet2.11 | null       | 00:00:00 |
     | null | 1234:3::/32  | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | null | 1234:3::/32  | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | null | 1234:3::/32  | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:02 |
     | C    | 1234:21::/32 | 1/0    | ethernet1.22 | null       | 00:00:00 |
     | C    | 1234:22::/32 | 1/0    | ethernet2.22 | null       | 00:00:00 |
     | null | 1234:23::/32 | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | null | 1234:23::/32 | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | null | 1234:23::/32 | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:02 |
     | null | 4321::1/128  | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | null | 4321::1/128  | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | C    | 4321::2/128  | 2/0    | loopback1    | null       | 00:00:11 |
     | null | 4321::3/128  | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:02 |
     |______|______________|________|______________|____________|__________|
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:12 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:12 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:12 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:12 |
     | P    | 1.1.1.8/30 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
     | P    | 1.1.1.8/30 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
     | P    | 1.1.1.8/30 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     | P    | 1.1.1.8/30 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:02 |
     | C    | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:12 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:12 |
     | C    | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:11 |
     | LOC  | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:11 |
     | P    | 1.1.2.8/30 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
     | P    | 1.1.2.8/30 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
     | P    | 1.1.2.8/30 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:02 |
     | P    | 1.1.2.8/30 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:02 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:12 |
     | P EX | 2.2.2.3/32 | 80/10  | ethernet2.11 | 1.1.1.6 | 00:00:01 |
     | P EX | 2.2.2.3/32 | 80/10  | ethernet2.22 | 1.1.2.6 | 00:00:01 |
     |______|____________|________|______________|_________|__________|
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
     | C    | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:12 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:12 |
     | C    | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:12 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:12 |
     | P    | 1234:3::/32    | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | P    | 1234:3::/32    | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | P    | 1234:3::/32    | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:00 |
     | C    | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:12 |
     | LOC  | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:12 |
     | C    | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:11 |
     | LOC  | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:11 |
     | P    | 1234:23::/32   | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:02 |
     | P    | 1234:23::/32   | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:02 |
     | P    | 1234:23::/32   | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:02 |
     | P EX | 4321::1/128    | 80/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | P EX | 4321::1/128    | 80/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | C    | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:12 |
     | P EX | 4321::3/128    | 80/10  | ethernet2.22 | 1234:22::2 | 00:00:02 |
     |______|________________|________|______________|____________|__________|
    r2#
    r2#
    ```

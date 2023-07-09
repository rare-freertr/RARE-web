# Example: pvrp peer template
    
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
    logging file debug ../binTmp/zzz19r1-log.run
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
    interface template1
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
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
     ipv6 address 1234::1 ffff::
     template template1
     no shutdown
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
    logging file debug ../binTmp/zzz19r2-log.run
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
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
     redistribute connected
     exit
    !
    interface template1
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
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
     ipv6 address 1234::2 ffff::
     template template1
     no shutdown
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 2       | 2        | 00:00:06 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | 2       | 2        | 00:00:06 |
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
     | C    | 1.1.1.0/24 | 1/0    | ethernet1 | null    | 00:00:01 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:06 |
     | C    | 9.9.9.0/24 | 1/0    | template1 | null    | 00:00:01 |
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
     | C    | 1234::/16   | 1/0    | ethernet1 | null    | 00:00:03 |
     | null | 4321::1/128 | 80/10  | ethernet1 | 1234::1 | 00:00:03 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null    | 00:00:06 |
     | C    | 9999::/16   | 1/0    | template1 | null    | 00:00:03 |
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
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:06 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:06 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:07 |
     | C    | 9.9.9.0/24 | 0/0    | template1 | null    | 00:00:06 |
     | LOC  | 9.9.9.9/32 | 0/1    | template1 | null    | 00:00:06 |
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
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:06 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:06 |
     | P EX | 4321::1/128 | 80/10  | ethernet1 | 1234::1 | 00:00:03 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:07 |
     | C    | 9999::/16   | 0/0    | template1 | null    | 00:00:07 |
     | LOC  | 9999::9/128 | 0/1    | template1 | null    | 00:00:07 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

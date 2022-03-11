# Example: pvrp dynamic twamp metric
    
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
    logging file debug ../binTmp/zzz33r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     router pvrp4 1 enable
     router pvrp4 1 metric-in 100
     router pvrp6 1 enable
     router pvrp6 1 metric-in 100
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1235::1 ffff::
     router pvrp4 1 enable
     router pvrp4 1 metric-in 1
     router pvrp6 1 enable
     router pvrp6 1 metric-in 1
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
    logging file debug ../binTmp/zzz33r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     router pvrp4 1 enable
     router pvrp4 1 dynamic-metric twamp
     router pvrp4 1 metric-in 2
     router pvrp6 1 enable
     router pvrp6 1 dynamic-metric twamp
     router pvrp6 1 metric-in 2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1235::2 ffff::
     router pvrp4 1 enable
     router pvrp4 1 dynamic-metric twamp
     router pvrp4 1 metric-in 200
     router pvrp6 1 enable
     router pvrp6 1 dynamic-metric twamp
     router pvrp6 1 metric-in 200
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 2       | 2        | 00:00:04 |
     | ethernet2 | 4.4.4.1 | null | null      | 1.1.2.1 | 0       | 0        | 00:00:04 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | 2       | 2        | 00:00:05 |
     | ethernet2 | 6.6.6.1 | r1   | ethernet2 | 1235::1 | 2       | 3        | 00:00:05 |
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
     | C    | 1.1.1.0/24 | 1/0    | ethernet1 | null    | 00:00:02 |
     | C    | 1.1.2.0/24 | 1/0    | ethernet2 | null    | 00:00:02 |
     | null | 2.2.2.1/32 | 80/2   | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:10 |
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
     | C    | 1234::/16   | 1/0    | ethernet1 | null    | 00:00:00 |
     | C    | 1235::/16   | 1/0    | ethernet2 | null    | 00:00:00 |
     | null | 4321::1/128 | 80/2   | ethernet1 | 1234::1 | 00:00:01 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null    | 00:00:10 |
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
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:10 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:10 |
     | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:10 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:10 |
     | P EX | 2.2.2.1/32 | 80/2   | ethernet1 | 1.1.1.1 | 00:00:03 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:10 |
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
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:10 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:10 |
     | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:10 |
     | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:10 |
     | P EX | 4321::1/128 | 80/2   | ethernet1 | 1234::1 | 00:00:02 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:10 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

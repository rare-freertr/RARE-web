# Example: static routing over point2point ethernet
    
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
    logging file debug ../binTmp/zzz32r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.254
     ipv6 address 1234:1::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
    !
    ipv6 route v1 :: :: 1234:1::2
    !
    !
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
    logging file debug ../binTmp/zzz32r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.254
     ipv6 address 1234:1::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.254
     ipv6 address 1234:2::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
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
    ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.3
    ipv4 route v1 2.2.2.201 255.255.255.255 1.1.1.7
    !
    ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
    ipv6 route v1 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::3
    !
    !
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
    logging file debug ../binTmp/zzz32r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.201 255.255.255.255
     ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.7 255.255.255.254
     ipv6 address 1234:2::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.6
    !
    ipv6 route v1 :: :: 1234:2::2
    !
    !
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
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop     | time     |
     |-----|--------------|--------|-----------|---------|----------|
     | C   | 1.1.1.2/31   | 0/0    | ethernet1 | null    | 00:00:01 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:01 |
     | C   | 1.1.1.6/31   | 0/0    | ethernet2 | null    | 00:00:01 |
     | LOC | 1.1.1.6/32   | 0/1    | ethernet2 | null    | 00:00:01 |
     | S   | 2.2.2.101/32 | 1/0    | ethernet1 | 1.1.1.3 | 00:00:01 |
     | S   | 2.2.2.201/32 | 1/0    | ethernet2 | 1.1.1.7 | 00:00:01 |
     |_____|______________|________|___________|_________|__________|
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
     | C   | 1234:1::2/127 | 0/0    | ethernet1 | null      | 00:00:02 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:02 |
     | C   | 1234:2::2/127 | 0/0    | ethernet2 | null      | 00:00:01 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:01 |
     | S   | 4321::101/128 | 1/0    | ethernet1 | 1234:1::3 | 00:00:01 |
     | S   | 4321::201/128 | 1/0    | ethernet2 | 1234:2::3 | 00:00:01 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

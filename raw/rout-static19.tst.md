# Example: verify source with static routing
    
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
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:1::3 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:3::1 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
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
    ipv4 route v1 2.2.2.99 255.255.255.255 1.1.1.10
    !
    ipv6 route v1 :: :: 1234:1::2
    ipv6 route v1 4321::99 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::3
    !
    !
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:1::2 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:2::2 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
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
    ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
    ipv4 route v1 2.2.2.201 255.255.255.255 1.1.1.5
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
    logging file debug ../binTmp/zzz55r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.201 255.255.255.255
     ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.99 255.255.255.255
     ipv6 address 4321::99 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:2::3 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv4 verify-source rx
     ipv6 address 1234:3::3 ffff:ffff:ffff:ffff::
     ipv6 verify-source rx
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
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:23 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:23 |
     | C   | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:23 |
     | LOC | 1.1.1.6/32   | 0/1    | ethernet2 | null    | 00:00:23 |
     | S   | 2.2.2.101/32 | 1/0    | ethernet1 | 1.1.1.1 | 00:00:23 |
     | S   | 2.2.2.201/32 | 1/0    | ethernet2 | 1.1.1.5 | 00:00:23 |
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
     | C   | 1234:1::/64   | 0/0    | ethernet1 | null      | 00:00:24 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:24 |
     | C   | 1234:2::/64   | 0/0    | ethernet2 | null      | 00:00:23 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:23 |
     | S   | 4321::101/128 | 1/0    | ethernet1 | 1234:1::3 | 00:00:23 |
     | S   | 4321::201/128 | 1/0    | ethernet2 | 1234:2::3 | 00:00:23 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

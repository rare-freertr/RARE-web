# Example: recursive static routing
    
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
    logging file debug ../binTmp/zzz60r1-log.run
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.102 255.255.255.255
     ipv6 address 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
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
    logging file debug ../binTmp/zzz60r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
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
    ipv4 route v1 2.2.2.102 255.255.255.255 2.2.2.101 recurigp
    ipv4 route v1 2.2.2.201 255.255.255.255 1.1.1.5
    ipv4 route v1 2.2.2.202 255.255.255.255 2.2.2.201 recurigp
    !
    ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 4321::101 recurigp
    ipv6 route v1 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    ipv6 route v1 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 4321::201 recurigp
    !
    !
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
    logging file debug ../binTmp/zzz60r3-log.run
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.202 255.255.255.255
     ipv6 address 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
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
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:07 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:07 |
     | C   | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:07 |
     | LOC | 1.1.1.6/32   | 0/1    | ethernet2 | null    | 00:00:07 |
     | S   | 2.2.2.101/32 | 1/0    | ethernet1 | 1.1.1.1 | 00:00:06 |
     | S   | 2.2.2.102/32 | 1/0    | ethernet1 | 1.1.1.1 | 00:00:06 |
     | S   | 2.2.2.201/32 | 1/0    | ethernet2 | 1.1.1.5 | 00:00:06 |
     | S   | 2.2.2.202/32 | 1/0    | ethernet2 | 1.1.1.5 | 00:00:06 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:07 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:07 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:07 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:07 |
     | S   | 4321::101/128 | 1/0    | ethernet1 | 1234:1::1 | 00:00:07 |
     | S   | 4321::102/128 | 1/0    | ethernet1 | 1234:1::1 | 00:00:07 |
     | S   | 4321::201/128 | 1/0    | ethernet2 | 1234:2::1 | 00:00:07 |
     | S   | 4321::202/128 | 1/0    | ethernet2 | 1234:2::1 | 00:00:07 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

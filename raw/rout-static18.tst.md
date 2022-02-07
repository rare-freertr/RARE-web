# Example: static routing with nrpe tracker
    
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
    logging file debug ../binTmp/zzz87r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     exit
    !
    tracker t1
     mode nrpe
     target 2.2.2.101/c1
     interval 1000
     timeout 500
     start
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.2 distance 11 tracker t1
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2 distance 22
    !
    ipv6 route v1 :: :: 1234:2::2 distance 11 tracker t1
    ipv6 route v1 :: :: 1234:1::2 distance 22
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    check c1
     command sho inter descr
     require-text interface;state;description
     require-text loopback0;up;
     require-text ethernet1;admin;
     require-text ethernet2;up;
     exit
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    server nrpe n
     vrf v1
     exit
    !
    client proxy p1
    !
    end
    ```
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz87r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     exit
    !
    tracker t1
     mode nrpe
     target 2.2.2.201/c1
     interval 1000
     timeout 500
     start
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.1 distance 11 tracker t1
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1 distance 22
    !
    ipv6 route v1 :: :: 1234:2::1 distance 11 tracker t1
    ipv6 route v1 :: :: 1234:1::1 distance 22
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    check c1
     command sho inter descr
     require-text interface;state;description
     require-text loopback0;up;
     require-text ethernet1;up;
     require-text ethernet2;up;
     exit
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    server nrpe n
     vrf v1
     exit
    !
    client proxy p1
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
     | S   | 0.0.0.0/0    | 22/0   | ethernet1 | 1.1.1.1 | 00:00:04 |
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:11 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:11 |
     | C   | 2.2.2.201/32 | 0/0    | loopback0 | null    | 00:00:11 |
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
     | S   | ::/0          | 22/0   | ethernet1 | 1234:1::1 | 00:00:04 |
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:11 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:11 |
     | C   | 4321::201/128 | 0/0    | loopback0 | null      | 00:00:11 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

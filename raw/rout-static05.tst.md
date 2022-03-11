# Example: static routing with bfd tracker
    
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
    logging file debug ../binTmp/zzz1r1-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 bfd 100 100 3
     no shutdown
     no log-link-change
     exit
    !
    tracker t1
     mode bfd
     target 1.1.2.2
     vrf v1
     interval 1000
     timeout 500
     start
     exit
    !
    tracker t2
     mode bfd
     target 1234:2::2
     vrf v1
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
    ipv6 route v1 :: :: 1234:2::2 distance 11 tracker t2
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
    server telnet tel
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    logging file debug ../binTmp/zzz1r2-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 bfd 100 100 3
     no shutdown
     no log-link-change
     exit
    !
    tracker t1
     mode bfd
     target 1.1.2.1
     vrf v1
     interval 1000
     timeout 500
     start
     exit
    !
    tracker t2
     mode bfd
     target 1234:2::1
     vrf v1
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
    ipv6 route v1 :: :: 1234:2::1 distance 11 tracker t2
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
    server telnet tel
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    r2#show tracker
    r2#show tracker
     |~~~~~~|~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | name | type   | mode | target    | state | changes | changed  |
     |------|--------|------|-----------|-------|---------|----------|
     | t1   | normal | bfd  | 1.1.2.1   | up    | 1       | 00:00:02 |
     | t2   | normal | bfd  | 1234:2::1 | up    | 1       | 00:00:01 |
     |______|________|______|___________|_______|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 bfd v1 nei
    r2#show ipv4 bfd v1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~|
     | interface | address | state | uptime   | clients |
     |-----------|---------|-------|----------|---------|
     | ethernet2 | 1.1.2.1 | up    | 00:00:04 | tracker |
     |___________|_________|_______|__________|_________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bfd v1 nei
    r2#show ipv6 bfd v1 nei
     |~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~|
     | interface | address   | state | uptime   | clients |
     |-----------|-----------|-------|----------|---------|
     | ethernet2 | 1234:2::1 | up    | 00:00:04 | tracker |
     |___________|___________|_______|__________|_________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop     | time     |
     |-----|--------------|--------|-----------|---------|----------|
     | S   | 0.0.0.0/0    | 11/0   | ethernet2 | 1.1.2.1 | 00:00:02 |
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:05 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:05 |
     | C   | 1.1.2.0/30   | 0/0    | ethernet2 | null    | 00:00:05 |
     | LOC | 1.1.2.2/32   | 0/1    | ethernet2 | null    | 00:00:05 |
     | C   | 2.2.2.201/32 | 0/0    | loopback0 | null    | 00:00:05 |
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
     | S   | ::/0          | 11/0   | ethernet2 | 1234:2::1 | 00:00:01 |
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:05 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:05 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:05 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:05 |
     | C   | 4321::201/128 | 0/0    | loopback0 | null      | 00:00:05 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

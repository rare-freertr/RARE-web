# Example: multicast routing with static flooding
    
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
    logging file debug ../binTmp/zzz46r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 multicast static-group 232.2.2.2 1.1.1.1
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 multicast static-group ff06::1 1234:1::1
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
    logging file debug ../binTmp/zzz46r2-log.run
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
     ipv4 multicast static-group 232.2.2.2 1.1.1.1
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 multicast static-group ff06::1 1234:1::1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv4 multicast static-group 232.2.2.2 1.1.1.1
     ipv6 address 1234:3::2 ffff:ffff::
     ipv6 multicast static-group ff06::1 1234:1::1
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
    logging file debug ../binTmp/zzz46r3-log.run
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
    ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.1.6
    !
    ipv6 mroute v1 :: :: 1234:2::2
    !
    !
    !
    !
    !
    ipv4 multicast v1 join-group 232.2.2.2 1.1.1.1
    !
    ipv6 multicast v1 join-group ff06::1 1234:1::1
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
    logging file debug ../binTmp/zzz46r4-log.run
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
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.10
    !
    ipv6 route v1 :: :: 1234:3::2
    !
    ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.1.10
    !
    ipv6 mroute v1 :: :: 1234:3::2
    !
    !
    !
    !
    !
    ipv4 multicast v1 join-group 232.2.2.2 1.1.1.1
    !
    ipv6 multicast v1 join-group ff06::1 1234:1::1
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
    r2#show ipv4 mroute v1
    r2#show ipv4 mroute v1
     |~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | source  | group     | interface | upstream | targets | bytes |
     |---------|-----------|-----------|----------|---------|-------|
     | 1.1.1.1 | 232.2.2.2 | ethernet1 | 1.1.1.1  | ifc=2   | 320   |
     |_________|___________|___________|__________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 mroute v1
    r2#show ipv6 mroute v1
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | source    | group   | interface | upstream  | targets | bytes |
     |-----------|---------|-----------|-----------|---------|-------|
     | 1234:1::1 | ff06::1 | ethernet1 | 1234:1::1 | ifc=2   | 320   |
     |___________|_________|___________|___________|_________|_______|
    r2#
    r2#
    ```

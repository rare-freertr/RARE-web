# Example: multicast routing with igmp/mld
    
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
    logging file debug ../binTmp/zzz31r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
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
    logging file debug ../binTmp/zzz31r2-log.run
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
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:3::2 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
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
    logging file debug ../binTmp/zzz31r3-log.run
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
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
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
    logging file debug ../binTmp/zzz31r4-log.run
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
     ipv4 address 1.1.1.9 255.255.255.252
     ipv4 multicast host-enable
     ipv4 multicast host-proxy
     ipv6 address 1234:3::1 ffff:ffff::
     ipv6 multicast host-enable
     ipv6 multicast host-proxy
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

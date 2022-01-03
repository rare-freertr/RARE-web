# Example: bgp ecmp connection
    
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:21::1 ffff:ffff::
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.10 255.255.255.252
     ipv6 address 1234:23::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family unicast
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 additional-path-rx unicast
     neighbor 1.1.1.2 additional-path-tx unicast
     neighbor 1.1.1.9 remote-as 3
     no neighbor 1.1.1.9 description
     neighbor 1.1.1.9 local-as 1
     neighbor 1.1.1.9 address-family unicast
     neighbor 1.1.1.9 distance 20
     neighbor 1.1.1.9 additional-path-rx unicast
     neighbor 1.1.1.9 additional-path-tx unicast
     neighbor 1.1.2.2 remote-as 2
     no neighbor 1.1.2.2 description
     neighbor 1.1.2.2 local-as 1
     neighbor 1.1.2.2 address-family unicast
     neighbor 1.1.2.2 distance 20
     neighbor 1.1.2.2 additional-path-rx unicast
     neighbor 1.1.2.2 additional-path-tx unicast
     neighbor 1.1.2.9 remote-as 3
     no neighbor 1.1.2.9 description
     neighbor 1.1.2.9 local-as 1
     neighbor 1.1.2.9 address-family unicast
     neighbor 1.1.2.9 distance 20
     neighbor 1.1.2.9 additional-path-rx unicast
     neighbor 1.1.2.9 additional-path-tx unicast
     redistribute connected
     ecmp
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast
     neighbor 1234:1::2 remote-as 2
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
     neighbor 1234:1::2 additional-path-rx unicast
     neighbor 1234:1::2 additional-path-tx unicast
     neighbor 1234:3::1 remote-as 3
     no neighbor 1234:3::1 description
     neighbor 1234:3::1 local-as 1
     neighbor 1234:3::1 address-family unicast
     neighbor 1234:3::1 distance 20
     neighbor 1234:3::1 additional-path-rx unicast
     neighbor 1234:3::1 additional-path-tx unicast
     neighbor 1234:21::2 remote-as 2
     no neighbor 1234:21::2 description
     neighbor 1234:21::2 local-as 1
     neighbor 1234:21::2 address-family unicast
     neighbor 1234:21::2 distance 20
     neighbor 1234:21::2 additional-path-rx unicast
     neighbor 1234:21::2 additional-path-tx unicast
     neighbor 1234:23::1 remote-as 3
     no neighbor 1234:23::1 description
     neighbor 1234:23::1 local-as 1
     neighbor 1234:23::1 address-family unicast
     neighbor 1234:23::1 distance 20
     neighbor 1234:23::1 additional-path-rx unicast
     neighbor 1234:23::1 additional-path-tx unicast
     redistribute connected
     ecmp
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:21::2 ffff:ffff::
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.252
     ipv6 address 1234:22::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 additional-path-rx unicast
     neighbor 1.1.1.1 additional-path-tx unicast
     neighbor 1.1.1.6 remote-as 3
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 2
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     neighbor 1.1.1.6 additional-path-rx unicast
     neighbor 1.1.1.6 additional-path-tx unicast
     neighbor 1.1.2.1 remote-as 1
     no neighbor 1.1.2.1 description
     neighbor 1.1.2.1 local-as 2
     neighbor 1.1.2.1 address-family unicast
     neighbor 1.1.2.1 distance 20
     neighbor 1.1.2.1 additional-path-rx unicast
     neighbor 1.1.2.1 additional-path-tx unicast
     neighbor 1.1.2.6 remote-as 3
     no neighbor 1.1.2.6 description
     neighbor 1.1.2.6 local-as 2
     neighbor 1.1.2.6 address-family unicast
     neighbor 1.1.2.6 distance 20
     neighbor 1.1.2.6 additional-path-rx unicast
     neighbor 1.1.2.6 additional-path-tx unicast
     redistribute connected
     ecmp
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 additional-path-rx unicast
     neighbor 1234:1::1 additional-path-tx unicast
     neighbor 1234:2::2 remote-as 3
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 2
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
     neighbor 1234:2::2 additional-path-rx unicast
     neighbor 1234:2::2 additional-path-tx unicast
     neighbor 1234:21::1 remote-as 1
     no neighbor 1234:21::1 description
     neighbor 1234:21::1 local-as 2
     neighbor 1234:21::1 address-family unicast
     neighbor 1234:21::1 distance 20
     neighbor 1234:21::1 additional-path-rx unicast
     neighbor 1234:21::1 additional-path-tx unicast
     neighbor 1234:22::2 remote-as 3
     no neighbor 1234:22::2 description
     neighbor 1234:22::2 local-as 2
     neighbor 1234:22::2 address-family unicast
     neighbor 1234:22::2 distance 20
     neighbor 1234:22::2 additional-path-rx unicast
     neighbor 1234:22::2 additional-path-tx unicast
     redistribute connected
     ecmp
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
    logging file debug ../binTmp/zzz1r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.252
     ipv6 address 1234:22::2 ffff:ffff::
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.9 255.255.255.252
     ipv6 address 1234:23::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 3
     router-id 4.4.4.3
     address-family unicast
     neighbor 1.1.1.5 remote-as 2
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 3
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     neighbor 1.1.1.5 additional-path-rx unicast
     neighbor 1.1.1.5 additional-path-tx unicast
     neighbor 1.1.1.10 remote-as 1
     no neighbor 1.1.1.10 description
     neighbor 1.1.1.10 local-as 3
     neighbor 1.1.1.10 address-family unicast
     neighbor 1.1.1.10 distance 20
     neighbor 1.1.1.10 additional-path-rx unicast
     neighbor 1.1.1.10 additional-path-tx unicast
     neighbor 1.1.2.5 remote-as 2
     no neighbor 1.1.2.5 description
     neighbor 1.1.2.5 local-as 3
     neighbor 1.1.2.5 address-family unicast
     neighbor 1.1.2.5 distance 20
     neighbor 1.1.2.5 additional-path-rx unicast
     neighbor 1.1.2.5 additional-path-tx unicast
     neighbor 1.1.2.10 remote-as 1
     no neighbor 1.1.2.10 description
     neighbor 1.1.2.10 local-as 3
     neighbor 1.1.2.10 address-family unicast
     neighbor 1.1.2.10 distance 20
     neighbor 1.1.2.10 additional-path-rx unicast
     neighbor 1.1.2.10 additional-path-tx unicast
     redistribute connected
     ecmp
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     address-family unicast
     neighbor 1234:2::1 remote-as 2
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 3
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 20
     neighbor 1234:2::1 additional-path-rx unicast
     neighbor 1234:2::1 additional-path-tx unicast
     neighbor 1234:3::2 remote-as 1
     no neighbor 1234:3::2 description
     neighbor 1234:3::2 local-as 3
     neighbor 1234:3::2 address-family unicast
     neighbor 1234:3::2 distance 20
     neighbor 1234:3::2 additional-path-rx unicast
     neighbor 1234:3::2 additional-path-tx unicast
     neighbor 1234:22::1 remote-as 2
     no neighbor 1234:22::1 description
     neighbor 1234:22::1 local-as 3
     neighbor 1234:22::1 address-family unicast
     neighbor 1234:22::1 distance 20
     neighbor 1234:22::1 additional-path-rx unicast
     neighbor 1234:22::1 additional-path-tx unicast
     neighbor 1234:23::2 remote-as 1
     no neighbor 1234:23::2 description
     neighbor 1234:23::2 local-as 3
     neighbor 1234:23::2 address-family unicast
     neighbor 1234:23::2 distance 20
     neighbor 1234:23::2 additional-path-rx unicast
     neighbor 1234:23::2 additional-path-tx unicast
     redistribute connected
     ecmp
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

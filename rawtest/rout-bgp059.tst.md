# Example: bgp override as in
    
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
     label-mode per-prefix
     exit
    !
    interface loopback0
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
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 65535
     router-id 4.4.4.1
     address-family unicast
     neighbor 1.1.1.2 remote-as 1
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 65535
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 65535
     router-id 6.6.6.1
     address-family unicast
     neighbor 1234:1::2 remote-as 1
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 65535
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
     redistribute connected
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
     label-mode per-prefix
     exit
    !
    interface loopback0
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family unicast
     neighbor 1.1.1.1 remote-as 65535
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 override-peer-as-in
     neighbor 1.1.1.6 remote-as 65535
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 1
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     neighbor 1.1.1.6 override-peer-as-in
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family unicast
     neighbor 1234:1::1 remote-as 65535
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 override-peer-as-in
     neighbor 1234:2::2 remote-as 65535
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 1
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
     neighbor 1234:2::2 override-peer-as-in
     redistribute connected
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
     label-mode per-prefix
     exit
    !
    interface loopback0
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
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 65535
     router-id 4.4.4.3
     address-family unicast
     neighbor 1.1.1.5 remote-as 1
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 65535
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 65535
     router-id 6.6.6.3
     address-family unicast
     neighbor 1234:2::1 remote-as 1
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 65535
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 20
     redistribute connected
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

# Example: ebgp over loopback
    
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
    logging file debug ../binTmp/zzz70r1-log.run
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
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     neighbor 2.2.2.2 remote-as 2
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family unicast
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 4321::2 remote-as 2
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family unicast
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
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
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    !
    !
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
    logging file debug ../binTmp/zzz70r2-log.run
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
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 2.2.2.1 remote-as 1
     neighbor 2.2.2.1 local-as 2
     neighbor 2.2.2.1 address-family unicast
     neighbor 2.2.2.1 distance 20
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.3 remote-as 3
     neighbor 2.2.2.3 local-as 2
     neighbor 2.2.2.3 address-family unicast
     neighbor 2.2.2.3 distance 20
     neighbor 2.2.2.3 update-source loopback0
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 4321::1 remote-as 1
     neighbor 4321::1 local-as 2
     neighbor 4321::1 address-family unicast
     neighbor 4321::1 distance 20
     neighbor 4321::1 update-source loopback0
     neighbor 4321::3 remote-as 3
     neighbor 4321::3 local-as 2
     neighbor 4321::3 address-family unicast
     neighbor 4321::3 distance 20
     neighbor 4321::3 update-source loopback0
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.6
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    !
    !
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
    logging file debug ../binTmp/zzz70r3-log.run
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
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.13 255.255.255.255
     ipv6 address 4321::13 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 3
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 2.2.2.2 remote-as 2
     neighbor 2.2.2.2 local-as 3
     neighbor 2.2.2.2 address-family unicast
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 4321::2 remote-as 2
     neighbor 4321::2 local-as 3
     neighbor 4321::2 address-family unicast
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.5
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.5
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    !
    !
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

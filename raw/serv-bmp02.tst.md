# Example: dynamic bmp peer
    
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
    logging file debug ../binTmp/zzz92r1-log.run
    !
    access-list test
     sequence 10 permit all any all any all
     exit
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
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     monitor bmp p1 1.1.1.1 17971
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 255
     neighbor 1.1.1.2 monitor bmp
     redistribute connected
     exit
    !
    router bgp4 2
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     template t remote-as 2
     no template t description
     template t local-as 1
     template t address-family unicast
     template t distance 20
     template t shutdown
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     monitor bmp p1 1.1.1.1 17972
     neighbor 1234:1::2 remote-as 2
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 255
     neighbor 1234:1::2 monitor bmp
     redistribute connected
     exit
    !
    router bgp6 2
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     template t remote-as 2
     no template t description
     template t local-as 1
     template t address-family unicast
     template t distance 20
     template t shutdown
     exit
    !
    proxy-profile p1
     vrf v1
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
    server bmp2mrt bmp1
     dyneigh test rx bgp4 2 t
     vrf v1
     exit
    !
    server bmp2mrt bmp2
     port 17972
     dyneigh test rx bgp6 2 t
     vrf v1
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
    logging file debug ../binTmp/zzz92r2-log.run
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
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.6 remote-as 3
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 2
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:2::2 remote-as 3
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 2
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
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
    logging file debug ../binTmp/zzz92r3-log.run
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
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
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
     neighbor 1.1.1.5 remote-as 2
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 3
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     neighbor 1.1.1.10 remote-as 4
     no neighbor 1.1.1.10 description
     neighbor 1.1.1.10 local-as 3
     neighbor 1.1.1.10 address-family unicast
     neighbor 1.1.1.10 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:2::1 remote-as 2
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 3
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 20
     neighbor 1234:3::2 remote-as 4
     no neighbor 1234:3::2 description
     neighbor 1234:3::2 local-as 3
     neighbor 1234:3::2 address-family unicast
     neighbor 1234:3::2 distance 20
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz92r4-log.run
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
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 4
     router-id 4.4.4.4
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.9 remote-as 3
     no neighbor 1.1.1.9 description
     neighbor 1.1.1.9 local-as 4
     neighbor 1.1.1.9 address-family unicast
     neighbor 1.1.1.9 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 4
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast
     neighbor 1234:3::1 remote-as 3
     no neighbor 1234:3::1 description
     neighbor 1234:3::1 local-as 4
     neighbor 1234:3::1 address-family unicast
     neighbor 1234:3::1 distance 20
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

# Example: bgp routemap filtering with peer large community
    
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
    logging file debug ../binTmp/zzz71r1-log.run
    !
    route-map rm1
     sequence 10 action deny
     sequence 10 match peerlrg 1:2:3
     !
     sequence 20 action permit
     !
     exit
    !
    bridge 1
     mac-learn
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
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     bridge-group 1
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
     neighbor 1.1.1.2 remote-as 2
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 ungroup-remoteas
     neighbor 1.1.1.2 route-server-client
     neighbor 1.1.1.2 send-community all
     neighbor 1.1.1.2 route-map-out rm1
     neighbor 1.1.1.3 remote-as 3
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family unicast
     neighbor 1.1.1.3 distance 20
     neighbor 1.1.1.3 ungroup-remoteas
     neighbor 1.1.1.3 route-server-client
     neighbor 1.1.1.3 send-community all
     neighbor 1.1.1.3 route-map-out rm1
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 2
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
     neighbor 1234:1::2 ungroup-remoteas
     neighbor 1234:1::2 route-server-client
     neighbor 1234:1::2 send-community all
     neighbor 1234:1::2 route-map-out rm1
     neighbor 1234:1::3 remote-as 3
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family unicast
     neighbor 1234:1::3 distance 20
     neighbor 1234:1::3 ungroup-remoteas
     neighbor 1234:1::3 route-server-client
     neighbor 1234:1::3 send-community all
     neighbor 1234:1::3 route-map-out rm1
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
    logging file debug ../binTmp/zzz71r2-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
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
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 send-community all
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
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 send-community all
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
    logging file debug ../binTmp/zzz71r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set lrgcomm 1:2:2
     !
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
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234:1::3 ffff:ffff::
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
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 3
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 send-community all
     redistribute connected route-map rm1
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 3
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 send-community all
     redistribute connected route-map rm1
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

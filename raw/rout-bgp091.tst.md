# Example: bgp distance with soft-reconfig
    
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
    logging file debug ../binTmp/zzz96r1-log.run
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     neighbor 1.1.1.2 remote-as 1
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 200
     neighbor 1.1.1.2 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 1
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 200
     neighbor 1234:1::2 soft-reconfiguration
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
    server telnet tel
     port 666
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
    logging file debug ../binTmp/zzz96r2-log.run
    !
    prefix-list p4
     sequence 10 deny 2.2.2.222/32 ge 32 le 32
     sequence 20 permit 0.0.0.0/0 ge 0 le 32
     exit
    !
    prefix-list p6
     sequence 10 deny 4321::222/128 ge 128 le 128
     sequence 20 permit ::/0 ge 0 le 128
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
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 123
     neighbor 1.1.1.1 soft-reconfiguration
     neighbor 1.1.1.1 prefix-list-in p4
     neighbor 1.1.1.6 remote-as 1
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 1
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 234
     neighbor 1.1.1.6 soft-reconfiguration
     neighbor 1.1.1.6 prefix-list-in p4
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 123
     neighbor 1234:1::1 soft-reconfiguration
     neighbor 1234:1::1 prefix-list-in p6
     neighbor 1234:2::2 remote-as 1
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 1
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 234
     neighbor 1234:2::2 soft-reconfiguration
     neighbor 1234:2::2 prefix-list-in p6
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
    logging file debug ../binTmp/zzz96r3-log.run
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     local-as 1
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.5 remote-as 1
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 1
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 200
     neighbor 1.1.1.5 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:2::1 remote-as 1
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 1
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 200
     neighbor 1234:2::1 soft-reconfiguration
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

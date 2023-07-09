# Example: bgp rpki
    
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
    logging file debug ../binTmp/zzz36r1-log.run
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
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     local-as 3
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.2 remote-as 1
     neighbor 1.1.1.2 local-as 3
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 1
     neighbor 1234:1::2 local-as 3
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
    logging file debug ../binTmp/zzz36r2-log.run
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
    route-map rm1
     sequence 10 action permit
     sequence 10 set locpref set 1234
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
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     local-as 1
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     rpki a r 2.2.2.2 323
     neighbor 1.1.1.1 remote-as 3
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 prefix-list-in p4
     neighbor 1.1.1.6 remote-as 2
     neighbor 1.1.1.6 local-as 1
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     neighbor 1.1.1.6 prefix-list-in p4
     neighbor 1.1.1.6 route-map-in rm1
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     rpki a r 4321::2 323
     neighbor 1234:1::1 remote-as 3
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 prefix-list-in p6
     neighbor 1234:2::2 remote-as 2
     neighbor 1234:2::2 local-as 1
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
     neighbor 1234:2::2 prefix-list-in p6
     neighbor 1234:2::2 route-map-in rm1
     redistribute connected
     exit
    !
    proxy-profile r
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
    server rpki r
     prefix4 2.2.2.111/32 32 3
     prefix6 4321::111/128 128 3
     vrf v1
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
    logging file debug ../binTmp/zzz36r3-log.run
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
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     local-as 2
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.5 remote-as 1
     neighbor 1.1.1.5 local-as 2
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:2::1 remote-as 1
     neighbor 1234:2::1 local-as 2
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

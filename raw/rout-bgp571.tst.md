# Example: ebgp over common subnet
    
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
    logging file debug ../binTmp/zzz21r1-log.run
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
    interface serial1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.1
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0001
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.255
     ipv6 address 1234::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234::2 remote-as 2
     neighbor 1234::2 local-as 1
     neighbor 1234::2 address-family unicast
     neighbor 1234::2 distance 20
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
    logging file debug ../binTmp/zzz21r2-log.run
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
    interface loopback9
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.255
     ipv6 address 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.2
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0002
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.255
     no ipv4 gateway-connected
     no ipv4 gateway-local
     ipv6 address 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no ipv6 gateway-connected
     no ipv6 gateway-local
     no shutdown
     no log-link-change
     exit
    !
    interface serial2
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.2
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0002
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.255
     no ipv4 gateway-connected
     no ipv4 gateway-local
     ipv6 address 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no ipv6 gateway-connected
     no ipv6 gateway-local
     no shutdown
     no log-link-change
     exit
    !
    interface serial3
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.2
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0002
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.255
     no ipv4 gateway-connected
     no ipv4 gateway-local
     ipv6 address 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no ipv6 gateway-connected
     no ipv6 gateway-local
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
     neighbor 1.1.1.1 update-source loopback9
     neighbor 1.1.1.3 remote-as 3
     neighbor 1.1.1.3 local-as 2
     neighbor 1.1.1.3 address-family unicast
     neighbor 1.1.1.3 distance 20
     neighbor 1.1.1.3 update-source loopback9
     neighbor 1.1.1.4 remote-as 4
     neighbor 1.1.1.4 local-as 2
     neighbor 1.1.1.4 address-family unicast
     neighbor 1.1.1.4 distance 20
     neighbor 1.1.1.4 update-source loopback9
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234::1 remote-as 1
     neighbor 1234::1 local-as 2
     neighbor 1234::1 address-family unicast
     neighbor 1234::1 distance 20
     neighbor 1234::1 update-source loopback9
     neighbor 1234::3 remote-as 3
     neighbor 1234::3 local-as 2
     neighbor 1234::3 address-family unicast
     neighbor 1234::3 distance 20
     neighbor 1234::3 update-source loopback9
     neighbor 1234::4 remote-as 4
     neighbor 1234::4 local-as 2
     neighbor 1234::4 address-family unicast
     neighbor 1234::4 distance 20
     neighbor 1234::4 update-source loopback9
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
    logging file debug ../binTmp/zzz21r3-log.run
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
    interface serial1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.3
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0003
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.255
     ipv6 address 1234::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     neighbor 1.1.1.2 remote-as 2
     neighbor 1.1.1.2 local-as 3
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234::2 remote-as 2
     neighbor 1234::2 local-as 3
     neighbor 1234::2 address-family unicast
     neighbor 1234::2 distance 20
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
    logging file debug ../binTmp/zzz21r4-log.run
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
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 1.1.1.4
     ppp ip6cp open
     ppp ip6cp local 0000-0000-0000-0004
     ppp ip6cp keep
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.255
     ipv6 address 1234::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     neighbor 1.1.1.2 remote-as 2
     neighbor 1.1.1.2 local-as 4
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 4
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast
     neighbor 1234::2 remote-as 2
     neighbor 1234::2 local-as 4
     neighbor 1234::2 address-family unicast
     neighbor 1234::2 distance 20
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

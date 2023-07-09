# Example: unicast+olab over ebgp
    
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
    logging file debug ../binTmp/zzz61r1-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 0054.2116.6257
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.2 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0037.5f1c.2961
     vrf forwarding v1
     ipv4 address 3.3.4.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::2 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast olab
     neighbor 1.1.1.2 remote-as 2
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast olab
     neighbor 1.1.1.2 distance 20
     afi-other enable
     afi-other redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast olab
     neighbor 1234:1::2 remote-as 2
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast olab
     neighbor 1234:1::2 distance 20
     afi-other enable
     afi-other redistribute connected
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
    logging file debug ../binTmp/zzz61r2-log.run
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
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 0071.5651.0b2f
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0035.7756.577e
     vrf forwarding v1
     ipv4 address 3.3.4.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::1 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast olab
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast olab
     neighbor 1.1.1.1 distance 20
     afi-other enable
     afi-other redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast olab
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast olab
     neighbor 1234:1::1 distance 20
     afi-other enable
     afi-other redistribute connected
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

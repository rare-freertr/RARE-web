# Example: bgp interas vpn with rr peering
    
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
    logging file debug ../binTmp/zzz69r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
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
     vrf forwarding v2
     ipv4 address 3.3.3.1 255.255.255.255
     ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.2 remote-as 1
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family vpnuni
     neighbor 2.2.2.2 distance 200
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::2 remote-as 1
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family vpnuni
     neighbor 4321::2 distance 200
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
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
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.2
    ipv4 route v1 2.2.2.5 255.255.255.255 1.1.1.2
    ipv4 route v1 2.2.2.6 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz69r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
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
     vrf forwarding v2
     ipv4 address 3.3.3.2 255.255.255.255
     ipv6 address 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.2
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.1 remote-as 1
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family vpnuni
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 route-reflector-client
     neighbor 2.2.2.1 next-hop-unchanged
     neighbor 2.2.2.1 send-community standard extended
     neighbor 2.2.2.3 remote-as 1
     neighbor 2.2.2.3 local-as 1
     neighbor 2.2.2.3 address-family vpnuni
     neighbor 2.2.2.3 distance 200
     neighbor 2.2.2.3 update-source loopback0
     neighbor 2.2.2.3 route-reflector-client
     neighbor 2.2.2.3 next-hop-unchanged
     neighbor 2.2.2.3 send-community standard extended
     neighbor 2.2.2.5 remote-as 2
     neighbor 2.2.2.5 local-as 1
     neighbor 2.2.2.5 address-family vpnuni
     neighbor 2.2.2.5 distance 20
     neighbor 2.2.2.5 update-source loopback0
     neighbor 2.2.2.5 next-hop-unchanged
     neighbor 2.2.2.5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::1 remote-as 1
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family vpnuni
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 route-reflector-client
     neighbor 4321::1 next-hop-unchanged
     neighbor 4321::1 send-community standard extended
     neighbor 4321::3 remote-as 1
     neighbor 4321::3 local-as 1
     neighbor 4321::3 address-family vpnuni
     neighbor 4321::3 distance 200
     neighbor 4321::3 update-source loopback0
     neighbor 4321::3 route-reflector-client
     neighbor 4321::3 next-hop-unchanged
     neighbor 4321::3 send-community standard extended
     neighbor 4321::5 remote-as 2
     neighbor 4321::5 local-as 1
     neighbor 4321::5 address-family vpnuni
     neighbor 4321::5 distance 20
     neighbor 4321::5 update-source loopback0
     neighbor 4321::5 next-hop-unchanged
     neighbor 4321::5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
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
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.6
    ipv4 route v1 2.2.2.5 255.255.255.255 1.1.1.6
    ipv4 route v1 2.2.2.6 255.255.255.255 1.1.1.6
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz69r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
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
     vrf forwarding v2
     ipv4 address 3.3.3.3 255.255.255.255
     ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.2 remote-as 1
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family vpnuni
     neighbor 2.2.2.2 distance 200
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp4 2
     vrf v1
     local-as 1
     router-id 4.4.4.3
     no safe-ebgp
     address-family labeled
     neighbor 1.1.1.10 remote-as 2
     neighbor 1.1.1.10 local-as 1
     neighbor 1.1.1.10 address-family labeled
     neighbor 1.1.1.10 distance 20
     redistribute connected
     redistribute static
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::2 remote-as 1
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family vpnuni
     neighbor 4321::2 distance 200
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 2
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family labeled
     neighbor 1234:3::2 remote-as 2
     neighbor 1234:3::2 local-as 1
     neighbor 1234:3::2 address-family labeled
     neighbor 1234:3::2 distance 20
     redistribute connected
     redistribute static
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
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz69r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
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
    interface loopback1
     vrf forwarding v2
     ipv4 address 3.3.3.4 255.255.255.255
     ipv6 address 3333::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.13 255.255.255.252
     ipv6 address 1234:4::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.3
     no safe-ebgp
     address-family labeled
     neighbor 1.1.1.9 remote-as 1
     neighbor 1.1.1.9 local-as 2
     neighbor 1.1.1.9 address-family labeled
     neighbor 1.1.1.9 distance 20
     redistribute connected
     redistribute static
     exit
    !
    router bgp4 2
     vrf v1
     local-as 2
     router-id 4.4.4.4
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.5 remote-as 2
     neighbor 2.2.2.5 local-as 2
     neighbor 2.2.2.5 address-family vpnuni
     neighbor 2.2.2.5 distance 200
     neighbor 2.2.2.5 update-source loopback0
     neighbor 2.2.2.5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.3
     no safe-ebgp
     address-family labeled
     neighbor 1234:3::1 remote-as 1
     neighbor 1234:3::1 local-as 2
     neighbor 1234:3::1 address-family labeled
     neighbor 1234:3::1 distance 20
     redistribute connected
     redistribute static
     exit
    !
    router bgp6 2
     vrf v1
     local-as 2
     router-id 6.6.6.4
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::5 remote-as 2
     neighbor 4321::5 local-as 2
     neighbor 4321::5 address-family vpnuni
     neighbor 4321::5 distance 200
     neighbor 4321::5 update-source loopback0
     neighbor 4321::5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
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
    ipv4 route v1 2.2.2.5 255.255.255.255 1.1.1.14
    ipv4 route v1 2.2.2.6 255.255.255.255 1.1.1.14
    !
    ipv6 route v1 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
    ipv6 route v1 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    
    **r5:**
    ```
    hostname r5
    buggy
    !
    logging file debug ../binTmp/zzz69r5-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v2
     ipv4 address 3.3.3.5 255.255.255.255
     ipv6 address 3333::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.14 255.255.255.252
     ipv6 address 1234:4::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.17 255.255.255.252
     ipv6 address 1234:5::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 2
     vrf v1
     local-as 2
     router-id 4.4.4.5
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.2 remote-as 1
     neighbor 2.2.2.2 local-as 2
     neighbor 2.2.2.2 address-family vpnuni
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 next-hop-unchanged
     neighbor 2.2.2.2 send-community standard extended
     neighbor 2.2.2.4 remote-as 2
     neighbor 2.2.2.4 local-as 2
     neighbor 2.2.2.4 address-family vpnuni
     neighbor 2.2.2.4 distance 200
     neighbor 2.2.2.4 update-source loopback0
     neighbor 2.2.2.4 route-reflector-client
     neighbor 2.2.2.4 next-hop-unchanged
     neighbor 2.2.2.4 send-community standard extended
     neighbor 2.2.2.6 remote-as 2
     neighbor 2.2.2.6 local-as 2
     neighbor 2.2.2.6 address-family vpnuni
     neighbor 2.2.2.6 distance 200
     neighbor 2.2.2.6 update-source loopback0
     neighbor 2.2.2.6 route-reflector-client
     neighbor 2.2.2.6 next-hop-unchanged
     neighbor 2.2.2.6 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 2
     vrf v1
     local-as 2
     router-id 6.6.6.5
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::2 remote-as 1
     neighbor 4321::2 local-as 2
     neighbor 4321::2 address-family vpnuni
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 next-hop-unchanged
     neighbor 4321::2 send-community standard extended
     neighbor 4321::4 remote-as 2
     neighbor 4321::4 local-as 2
     neighbor 4321::4 address-family vpnuni
     neighbor 4321::4 distance 200
     neighbor 4321::4 update-source loopback0
     neighbor 4321::4 route-reflector-client
     neighbor 4321::4 next-hop-unchanged
     neighbor 4321::4 send-community standard extended
     neighbor 4321::6 remote-as 2
     neighbor 4321::6 local-as 2
     neighbor 4321::6 address-family vpnuni
     neighbor 4321::6 distance 200
     neighbor 4321::6 update-source loopback0
     neighbor 4321::6 route-reflector-client
     neighbor 4321::6 next-hop-unchanged
     neighbor 4321::6 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.13
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.13
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.13
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.13
    ipv4 route v1 2.2.2.6 255.255.255.255 1.1.1.18
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
    ipv6 route v1 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    
    **r6:**
    ```
    hostname r6
    buggy
    !
    logging file debug ../binTmp/zzz69r6-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt4import 1:2
     rt4export 1:2
     rt6import 1:2
     rt6export 1:2
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v2
     ipv4 address 3.3.3.6 255.255.255.255
     ipv6 address 3333::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.18 255.255.255.252
     ipv6 address 1234:5::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 2
     vrf v1
     local-as 2
     router-id 4.4.4.6
     no safe-ebgp
     address-family vpnuni
     neighbor 2.2.2.5 remote-as 2
     neighbor 2.2.2.5 local-as 2
     neighbor 2.2.2.5 address-family vpnuni
     neighbor 2.2.2.5 distance 200
     neighbor 2.2.2.5 update-source loopback0
     neighbor 2.2.2.5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 2
     vrf v1
     local-as 2
     router-id 6.6.6.6
     no safe-ebgp
     address-family vpnuni
     neighbor 4321::5 remote-as 2
     neighbor 4321::5 local-as 2
     neighbor 4321::5 address-family vpnuni
     neighbor 4321::5 distance 200
     neighbor 4321::5 update-source loopback0
     neighbor 4321::5 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.17
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.17
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.17
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.17
    ipv4 route v1 2.2.2.5 255.255.255.255 1.1.1.17
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::1
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::1
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::1
    ipv6 route v1 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:5::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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

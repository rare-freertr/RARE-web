# Example: bgp dual core csc vpn
    
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
    logging file debug ../binTmp/zzz29r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    vrf definition v3
     rd 1:2
     rt-import 1:2
     rt-export 1:2
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
    interface loopback2
     no description
     vrf forwarding v3
     ipv4 address 3.3.3.1 255.255.255.255
     ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
    interface pwether1
     no description
     mtu 1500
     macaddr 0017.792c.2749
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.0
     pseudowire v3 loopback2 pweompls 3.3.3.3 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 0076.442c.2b31
     vrf forwarding v1
     ipv4 address 5.5.5.1 255.255.255.0
     pseudowire v3 loopback2 pweompls 3333::3 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family vpnuni
     neighbor 2.2.2.2 remote-as 1
     no neighbor 2.2.2.2 description
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family vpnuni
     neighbor 2.2.2.2 distance 200
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family vpnuni
     neighbor 4321::2 remote-as 1
     no neighbor 4321::2 description
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family vpnuni
     neighbor 4321::2 distance 200
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
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
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz29r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:0
     label-mode per-prefix
     exit
    !
    vrf definition v3
     rd 1:2
     rt-import 1:2
     rt-export 1:2
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
    interface loopback1
     no description
     vrf forwarding v2
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v3
     ipv4 address 3.3.3.2 255.255.255.255
     ipv6 address 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
     no description
     vrf forwarding v2
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
     address-family vpnuni
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family vpnuni
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v3 redistribute bgp4 2
     exit
    !
    router bgp4 2
     vrf v2
     local-as 2
     router-id 4.4.4.2
     address-family vpnuni
     neighbor 2.2.2.3 remote-as 2
     no neighbor 2.2.2.3 description
     neighbor 2.2.2.3 local-as 2
     neighbor 2.2.2.3 address-family vpnuni
     neighbor 2.2.2.3 distance 200
     neighbor 2.2.2.3 update-source loopback1
     neighbor 2.2.2.3 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v3 redistribute bgp4 1
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     address-family vpnuni
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family vpnuni
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v3 redistribute bgp6 2
     exit
    !
    router bgp6 2
     vrf v2
     local-as 2
     router-id 6.6.6.2
     address-family vpnuni
     neighbor 4321::3 remote-as 2
     no neighbor 4321::3 description
     neighbor 4321::3 local-as 2
     neighbor 4321::3 address-family vpnuni
     neighbor 4321::3 distance 200
     neighbor 4321::3 update-source loopback1
     neighbor 4321::3 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v3 redistribute bgp6 1
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
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v2 2.2.2.3 255.255.255.255 1.1.1.6
    !
    ipv6 route v2 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz29r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v2
     rd 1:1
     label-mode per-prefix
     exit
    !
    vrf definition v3
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     label-mode per-prefix
     exit
    !
    interface loopback1
     no description
     vrf forwarding v2
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v3
     ipv4 address 3.3.3.3 255.255.255.255
     ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v2
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     no description
     mtu 1500
     macaddr 0027.0d23.2270
     vrf forwarding v2
     ipv4 address 4.4.4.3 255.255.255.0
     pseudowire v3 loopback2 pweompls 3.3.3.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 005a.2533.6370
     vrf forwarding v2
     ipv4 address 5.5.5.3 255.255.255.0
     pseudowire v3 loopback2 pweompls 3333::1 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v2
     local-as 2
     router-id 4.4.4.3
     address-family vpnuni
     neighbor 2.2.2.2 remote-as 2
     no neighbor 2.2.2.2 description
     neighbor 2.2.2.2 local-as 2
     neighbor 2.2.2.2 address-family vpnuni
     neighbor 2.2.2.2 distance 200
     neighbor 2.2.2.2 update-source loopback1
     neighbor 2.2.2.2 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     exit
    !
    router bgp6 1
     vrf v2
     local-as 2
     router-id 6.6.6.3
     address-family vpnuni
     neighbor 4321::2 remote-as 2
     no neighbor 4321::2 description
     neighbor 4321::2 local-as 2
     neighbor 4321::2 address-family vpnuni
     neighbor 4321::2 distance 200
     neighbor 4321::2 update-source loopback1
     neighbor 4321::2 send-community standard extended
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
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
    ipv4 route v2 2.2.2.2 255.255.255.255 1.1.1.5
    !
    ipv6 route v2 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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

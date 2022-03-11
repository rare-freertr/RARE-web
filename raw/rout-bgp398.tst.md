# Example: unified mpls with ldp
    
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
    logging file debug ../binTmp/zzz22r1-log.run
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
     macaddr 0002.4f39.0860
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.6 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 000b.6506.6f53
     vrf forwarding v1
     ipv4 address 3.3.4.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::6 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family labeled
     neighbor 2.2.2.3 remote-as 1
     no neighbor 2.2.2.3 description
     neighbor 2.2.2.3 local-as 1
     neighbor 2.2.2.3 address-family labeled
     neighbor 2.2.2.3 distance 200
     neighbor 2.2.2.3 update-source loopback0
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family labeled
     neighbor 4321::3 remote-as 1
     no neighbor 4321::3 description
     neighbor 4321::3 local-as 1
     neighbor 4321::3 address-family labeled
     neighbor 4321::3 distance 200
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
    logging file debug ../binTmp/zzz22r2-log.run
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
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
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
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz22r3-log.run
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
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
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
     address-family labeled
     neighbor 1.1.1.10 remote-as 1
     no neighbor 1.1.1.10 description
     neighbor 1.1.1.10 local-as 1
     neighbor 1.1.1.10 address-family labeled
     neighbor 1.1.1.10 distance 200
     neighbor 1.1.1.10 route-reflector-client
     neighbor 1.1.1.10 next-hop-self
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family labeled
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 next-hop-self
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family labeled
     neighbor 1234:3::2 remote-as 1
     no neighbor 1234:3::2 description
     neighbor 1234:3::2 local-as 1
     neighbor 1234:3::2 address-family labeled
     neighbor 1234:3::2 distance 200
     neighbor 1234:3::2 route-reflector-client
     neighbor 1234:3::2 next-hop-self
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family labeled
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 next-hop-self
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz22r4-log.run
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
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
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
     local-as 1
     router-id 4.4.4.4
     no safe-ebgp
     address-family labeled
     neighbor 1.1.1.9 remote-as 1
     no neighbor 1.1.1.9 description
     neighbor 1.1.1.9 local-as 1
     neighbor 1.1.1.9 address-family labeled
     neighbor 1.1.1.9 distance 200
     neighbor 1.1.1.9 route-reflector-client
     neighbor 1.1.1.9 next-hop-self
     neighbor 2.2.2.6 remote-as 1
     no neighbor 2.2.2.6 description
     neighbor 2.2.2.6 local-as 1
     neighbor 2.2.2.6 address-family labeled
     neighbor 2.2.2.6 distance 200
     neighbor 2.2.2.6 update-source loopback0
     neighbor 2.2.2.6 next-hop-self
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.4
     no safe-ebgp
     address-family labeled
     neighbor 1234:3::1 remote-as 1
     no neighbor 1234:3::1 description
     neighbor 1234:3::1 local-as 1
     neighbor 1234:3::1 address-family labeled
     neighbor 1234:3::1 distance 200
     neighbor 1234:3::1 route-reflector-client
     neighbor 1234:3::1 next-hop-self
     neighbor 4321::6 remote-as 1
     no neighbor 4321::6 description
     neighbor 4321::6 local-as 1
     neighbor 4321::6 address-family labeled
     neighbor 4321::6 distance 200
     neighbor 4321::6 update-source loopback0
     neighbor 4321::6 next-hop-self
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
    logging file debug ../binTmp/zzz22r5-log.run
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
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
     no description
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.13
    ipv4 route v1 2.2.2.6 255.255.255.255 1.1.1.18
    !
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
    logging file debug ../binTmp/zzz22r6-log.run
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
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
    interface pwether1
     no description
     mtu 1500
     macaddr 0077.5477.1d64
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 0023.6738.2d67
     vrf forwarding v1
     ipv4 address 3.3.4.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::1 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.6
     no safe-ebgp
     address-family labeled
     neighbor 2.2.2.4 remote-as 1
     no neighbor 2.2.2.4 description
     neighbor 2.2.2.4 local-as 1
     neighbor 2.2.2.4 address-family labeled
     neighbor 2.2.2.4 distance 200
     neighbor 2.2.2.4 update-source loopback0
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.6
     no safe-ebgp
     address-family labeled
     neighbor 4321::4 remote-as 1
     no neighbor 4321::4 description
     neighbor 4321::4 local-as 1
     neighbor 4321::4 address-family labeled
     neighbor 4321::4 distance 200
     neighbor 4321::4 update-source loopback0
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
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.17
    ipv4 route v1 2.2.2.5 255.255.255.255 1.1.1.17
    !
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

# Example: multicast vpn routing with mldp
    
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
    logging file debug ../binTmp/zzz90r1-log.run
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
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mdt4
     mdt6
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
     vrf forwarding v2
     ipv4 address 3.3.3.1 255.255.255.255
     ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family vpnuni vpnmlt
     neighbor 2.2.2.3 remote-as 1
     no neighbor 2.2.2.3 description
     neighbor 2.2.2.3 local-as 1
     neighbor 2.2.2.3 address-family vpnuni vpnmlt
     neighbor 2.2.2.3 distance 200
     neighbor 2.2.2.3 update-source loopback0
     neighbor 2.2.2.3 send-community standard extended
     neighbor 2.2.2.4 remote-as 1
     no neighbor 2.2.2.4 description
     neighbor 2.2.2.4 local-as 1
     neighbor 2.2.2.4 address-family vpnuni vpnmlt
     neighbor 2.2.2.4 distance 200
     neighbor 2.2.2.4 update-source loopback0
     neighbor 2.2.2.4 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family vpnuni vpnmlt
     neighbor 4321::3 remote-as 1
     no neighbor 4321::3 description
     neighbor 4321::3 local-as 1
     neighbor 4321::3 address-family vpnuni vpnmlt
     neighbor 4321::3 distance 200
     neighbor 4321::3 update-source loopback0
     neighbor 4321::3 send-community standard extended
     neighbor 4321::4 remote-as 1
     no neighbor 4321::4 description
     neighbor 4321::4 local-as 1
     neighbor 4321::4 address-family vpnuni vpnmlt
     neighbor 4321::4 distance 200
     neighbor 4321::4 update-source loopback0
     neighbor 4321::4 send-community standard extended
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
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.5
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.5
    !
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz90r2-log.run
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
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
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
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.6
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.10
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.1.14
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
    !
    !
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
    logging file debug ../binTmp/zzz90r3-log.run
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
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mdt4
     mdt6
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
     vrf forwarding v2
     ipv4 address 3.3.3.3 255.255.255.255
     ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family vpnuni vpnmlt
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family vpnuni vpnmlt
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family vpnuni vpnmlt
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family vpnuni vpnmlt
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.9
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 multicast v2 join-group 232.2.2.2 3.3.3.1
    !
    ipv6 multicast v2 join-group ff06::1 3333::1
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
    logging file debug ../binTmp/zzz90r4-log.run
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
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mdt4
     mdt6
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
    interface loopback1
     no description
     vrf forwarding v2
     ipv4 address 3.3.3.4 255.255.255.255
     ipv6 address 3333::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     address-family vpnuni vpnmlt
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family vpnuni vpnmlt
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.4
     address-family vpnuni vpnmlt
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family vpnuni vpnmlt
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
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
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 multicast v2 join-group 232.2.2.2 3.3.3.1
    !
    ipv6 multicast v2 join-group ff06::1 3333::1
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

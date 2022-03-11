# Example: evpn/pbb over ibgp rr
    
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
    logging file debug ../binTmp/zzz75r1-log.run
    !
    bridge 1
     rd 1:1
     rt-import 1:1
     rt-export 1:1
     mac-learn
     private-bridge
     exit
    !
    bridge 2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mac-learn
     private-bridge
     exit
    !
    bridge 3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     mac-learn
     private-bridge
     exit
    !
    bridge 4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
     mac-learn
     private-bridge
     exit
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 4444::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi3
     no description
     vrf forwarding v1
     ipv6 address 3333::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi4
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
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
     address-family evpn
     neighbor 1.1.1.3 remote-as 1
     no neighbor 1.1.1.3 description
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family evpn
     neighbor 1.1.1.3 distance 200
     neighbor 1.1.1.3 update-source loopback0
     neighbor 1.1.1.3 pmsitun
     neighbor 1.1.1.3 send-community standard extended
     afi-evpn 101 bridge-group 1
     afi-evpn 101 bmac 007c.372b.6b7c
     afi-evpn 101 encapsulation pbb
     afi-evpn 101 update-source loopback0
     afi-evpn 102 bridge-group 3
     afi-evpn 102 bmac 0063.3e6a.7871
     afi-evpn 102 encapsulation pbb
     afi-evpn 102 update-source loopback0
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family evpn
     neighbor 1234:1::3 remote-as 1
     no neighbor 1234:1::3 description
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family evpn
     neighbor 1234:1::3 distance 200
     neighbor 1234:1::3 update-source loopback0
     neighbor 1234:1::3 pmsitun
     neighbor 1234:1::3 send-community standard extended
     afi-evpn 101 bridge-group 2
     afi-evpn 101 bmac 0002.7a20.6a2c
     afi-evpn 101 encapsulation pbb
     afi-evpn 101 update-source loopback0
     afi-evpn 102 bridge-group 4
     afi-evpn 102 bmac 0041.0c61.7703
     afi-evpn 102 encapsulation pbb
     afi-evpn 102 update-source loopback0
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
    logging file debug ../binTmp/zzz75r2-log.run
    !
    bridge 1
     rd 1:1
     rt-import 1:1
     rt-export 1:1
     mac-learn
     private-bridge
     exit
    !
    bridge 2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mac-learn
     private-bridge
     exit
    !
    bridge 3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     mac-learn
     private-bridge
     exit
    !
    bridge 4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
     mac-learn
     private-bridge
     exit
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 4444::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi3
     no description
     vrf forwarding v1
     ipv6 address 3333::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi4
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
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
     address-family evpn
     neighbor 1.1.1.3 remote-as 1
     no neighbor 1.1.1.3 description
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family evpn
     neighbor 1.1.1.3 distance 200
     neighbor 1.1.1.3 update-source loopback0
     neighbor 1.1.1.3 pmsitun
     neighbor 1.1.1.3 send-community standard extended
     afi-evpn 101 bridge-group 1
     afi-evpn 101 bmac 0049.215f.5b34
     afi-evpn 101 encapsulation pbb
     afi-evpn 101 update-source loopback0
     afi-evpn 102 bridge-group 3
     afi-evpn 102 bmac 0001.527c.7c46
     afi-evpn 102 encapsulation pbb
     afi-evpn 102 update-source loopback0
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     no safe-ebgp
     address-family evpn
     neighbor 1234:1::3 remote-as 1
     no neighbor 1234:1::3 description
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family evpn
     neighbor 1234:1::3 distance 200
     neighbor 1234:1::3 update-source loopback0
     neighbor 1234:1::3 pmsitun
     neighbor 1234:1::3 send-community standard extended
     afi-evpn 101 bridge-group 2
     afi-evpn 101 bmac 0048.143a.0953
     afi-evpn 101 encapsulation pbb
     afi-evpn 101 update-source loopback0
     afi-evpn 102 bridge-group 4
     afi-evpn 102 bmac 0053.0439.4d7a
     afi-evpn 102 encapsulation pbb
     afi-evpn 102 update-source loopback0
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
    logging file debug ../binTmp/zzz75r3-log.run
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234:1::3 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     no safe-ebgp
     address-family evpn
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family evpn
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 pmsitun
     neighbor 2.2.2.1 route-reflector-client
     neighbor 2.2.2.1 send-community standard extended
     neighbor 2.2.2.2 remote-as 1
     no neighbor 2.2.2.2 description
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family evpn
     neighbor 2.2.2.2 distance 200
     neighbor 2.2.2.2 pmsitun
     neighbor 2.2.2.2 route-reflector-client
     neighbor 2.2.2.2 send-community standard extended
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family evpn
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family evpn
     neighbor 4321::1 distance 200
     neighbor 4321::1 pmsitun
     neighbor 4321::1 route-reflector-client
     neighbor 4321::1 send-community standard extended
     neighbor 4321::2 remote-as 1
     no neighbor 4321::2 description
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family evpn
     neighbor 4321::2 distance 200
     neighbor 4321::2 pmsitun
     neighbor 4321::2 route-reflector-client
     neighbor 4321::2 send-community standard extended
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
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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

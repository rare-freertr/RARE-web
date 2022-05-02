# Example: bgp othervpns aggregation
    
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
    logging file debug ../binTmp/zzz79r1-log.run
    !
    route-map p4
     sequence 10 action permit
     sequence 10 match network 9.9.2.0/24 ge 24 le 24
     !
     sequence 20 action permit
     sequence 20 match network 9.9.3.0/24 ge 24 le 24
     !
     sequence 30 action permit
     sequence 30 match network 9.9.4.0/24 ge 24 le 24
     !
     exit
    !
    route-map p6
     sequence 10 action permit
     sequence 10 match network 9992::/32 ge 32 le 32
     !
     sequence 20 action permit
     sequence 20 match network 9993::/32 ge 32 le 32
     !
     sequence 30 action permit
     sequence 30 match network 9994::/32 ge 32 le 32
     !
     exit
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
    vrf definition v3
     rd 1:3
     rt4import 1:3
     rt4export 1:3
     rt6import 1:3
     rt6export 1:3
     exit
    !
    vrf definition v4
     rd 1:4
     rt4import 1:4
     rt4export 1:4
     rt6import 1:4
     rt6export 1:4
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
    interface loopback21
     vrf forwarding v2
     ipv4 address 9.9.2.1 255.255.255.255
     ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback22
     vrf forwarding v2
     ipv4 address 9.9.2.11 255.255.255.255
     ipv6 address 9992::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback23
     vrf forwarding v2
     ipv4 address 9.9.2.111 255.255.255.255
     ipv6 address 9992::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback31
     vrf forwarding v3
     ipv4 address 9.9.3.1 255.255.255.255
     ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback32
     vrf forwarding v3
     ipv4 address 9.9.3.11 255.255.255.255
     ipv6 address 9993::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback33
     vrf forwarding v3
     ipv4 address 9.9.3.111 255.255.255.255
     ipv6 address 9993::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback41
     vrf forwarding v4
     ipv4 address 9.9.4.1 255.255.255.255
     ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback42
     vrf forwarding v4
     ipv4 address 9.9.4.11 255.255.255.255
     ipv6 address 9994::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback43
     vrf forwarding v4
     ipv4 address 9.9.4.111 255.255.255.255
     ipv6 address 9994::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     address-family ovpnuni
     neighbor 2.2.2.2 remote-as 2
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family ovpnuni
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     neighbor 2.2.2.2 ovpn-route-map-in p6
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family ovpnuni
     neighbor 4321::2 remote-as 2
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family ovpnuni
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     neighbor 4321::2 ovpn-route-map-in p4
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz79r2-log.run
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
    vrf definition v3
     rd 1:3
     rt4import 1:3
     rt4export 1:3
     rt6import 1:3
     rt6export 1:3
     exit
    !
    vrf definition v4
     rd 1:4
     rt4import 1:4
     rt4export 1:4
     rt6import 1:4
     rt6export 1:4
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
    interface loopback21
     vrf forwarding v2
     ipv4 address 9.9.2.2 255.255.255.255
     ipv6 address 9992::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback22
     vrf forwarding v2
     ipv4 address 9.9.2.22 255.255.255.255
     ipv6 address 9992::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback23
     vrf forwarding v2
     ipv4 address 9.9.2.222 255.255.255.255
     ipv6 address 9992::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback31
     vrf forwarding v3
     ipv4 address 9.9.3.2 255.255.255.255
     ipv6 address 9993::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback32
     vrf forwarding v3
     ipv4 address 9.9.3.22 255.255.255.255
     ipv6 address 9993::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback33
     vrf forwarding v3
     ipv4 address 9.9.3.222 255.255.255.255
     ipv6 address 9993::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback41
     vrf forwarding v4
     ipv4 address 9.9.4.2 255.255.255.255
     ipv6 address 9994::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback42
     vrf forwarding v4
     ipv4 address 9.9.4.22 255.255.255.255
     ipv6 address 9994::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback43
     vrf forwarding v4
     ipv4 address 9.9.4.222 255.255.255.255
     ipv6 address 9994::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family ovpnuni
     neighbor 2.2.2.1 remote-as 1
     neighbor 2.2.2.1 local-as 2
     neighbor 2.2.2.1 address-family ovpnuni
     neighbor 2.2.2.1 distance 20
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v2 aggregate 9992::/32
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v3 aggregate 9993::/32
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
     afi-ovrf v4 aggregate 9994::/32
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family ovpnuni
     neighbor 4321::1 remote-as 1
     neighbor 4321::1 local-as 2
     neighbor 4321::1 address-family ovpnuni
     neighbor 4321::1 distance 20
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v2 aggregate 9.9.2.0/24
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v3 aggregate 9.9.3.0/24
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
     afi-ovrf v4 aggregate 9.9.4.0/24
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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

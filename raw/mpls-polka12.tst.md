# Example: bgp vpns over polka
    
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
    logging file debug ../binTmp/zzz68r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     segrout 10 1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     segrout 10 1
     redistribute connected
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
    interface loopback2
     vrf forwarding v2
     ipv4 address 9.9.2.1 255.255.255.255
     ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v3
     ipv4 address 9.9.3.1 255.255.255.255
     ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v4
     ipv4 address 9.9.4.1 255.255.255.255
     ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234:1::1 ffff:ffff::
     polka enable 1 65536 10
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.3
     tunnel domain-name 2.2.2.2
     tunnel mode polka
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::3
     tunnel domain-name 4321::2
     tunnel mode polka
     vrf forwarding v1
     ipv6 address 3333::1 ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family vpnuni
     neighbor 3.3.3.2 remote-as 1
     neighbor 3.3.3.2 local-as 1
     neighbor 3.3.3.2 address-family vpnuni
     neighbor 3.3.3.2 distance 200
     neighbor 3.3.3.2 update-source tunnel1
     neighbor 3.3.3.2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v4 enable
     afi-vrf v4 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family vpnuni
     neighbor 3333::2 remote-as 1
     neighbor 3333::2 local-as 1
     neighbor 3333::2 address-family vpnuni
     neighbor 3333::2 distance 200
     neighbor 3333::2 update-source tunnel2
     neighbor 3333::2 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v4 enable
     afi-vrf v4 redistribute connected
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz68r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     segrout 10 2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     segrout 10 2
     redistribute connected
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     polka enable 2 65536 10
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.0
     ipv6 address 1234:2::2 ffff:ffff::
     polka enable 2 65536 10
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    !
    !
    !
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
    logging file debug ../binTmp/zzz68r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.3
     segrout 10 3
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     segrout 10 3
     redistribute connected
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
    interface loopback2
     vrf forwarding v2
     ipv4 address 9.9.2.3 255.255.255.255
     ipv6 address 9992::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v3
     ipv4 address 9.9.3.3 255.255.255.255
     ipv6 address 9993::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v4
     ipv4 address 9.9.4.3 255.255.255.255
     ipv6 address 9994::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.0
     ipv6 address 1234:2::3 ffff:ffff::
     polka enable 3 65536 10
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.1
     tunnel domain-name 2.2.2.2
     tunnel mode polka
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::1
     tunnel domain-name 4321::2
     tunnel mode polka
     vrf forwarding v1
     ipv6 address 3333::2 ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family vpnuni
     neighbor 3.3.3.1 remote-as 1
     neighbor 3.3.3.1 local-as 1
     neighbor 3.3.3.1 address-family vpnuni
     neighbor 3.3.3.1 distance 200
     neighbor 3.3.3.1 update-source tunnel1
     neighbor 3.3.3.1 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v4 enable
     afi-vrf v4 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family vpnuni
     neighbor 3333::1 remote-as 1
     neighbor 3333::1 local-as 1
     neighbor 3333::1 address-family vpnuni
     neighbor 3333::1 distance 200
     neighbor 3333::1 update-source tunnel2
     neighbor 3333::1 send-community standard extended
     afi-vrf v2 enable
     afi-vrf v2 redistribute connected
     afi-vrf v3 enable
     afi-vrf v3 redistribute connected
     afi-vrf v4 enable
     afi-vrf v4 redistribute connected
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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

# Example: ibgp rr othervpns prefix movement
    
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
    logging file debug ../binTmp/zzz7r1-log.run
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
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family ovpnuni
     neighbor 1.1.1.2 remote-as 1
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family ovpnuni
     neighbor 1.1.1.2 distance 200
     neighbor 1.1.1.2 route-reflector-client
     neighbor 1.1.1.2 send-community standard extended
     neighbor 1.1.1.3 remote-as 1
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family ovpnuni
     neighbor 1.1.1.3 distance 200
     neighbor 1.1.1.3 route-reflector-client
     neighbor 1.1.1.3 send-community standard extended
     neighbor 1.1.1.4 remote-as 1
     neighbor 1.1.1.4 local-as 1
     neighbor 1.1.1.4 address-family ovpnuni
     neighbor 1.1.1.4 distance 200
     neighbor 1.1.1.4 route-reflector-client
     neighbor 1.1.1.4 send-community standard extended
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
     address-family ovpnuni
     neighbor 1234:1::2 remote-as 1
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family ovpnuni
     neighbor 1234:1::2 distance 200
     neighbor 1234:1::2 route-reflector-client
     neighbor 1234:1::2 send-community standard extended
     neighbor 1234:1::3 remote-as 1
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family ovpnuni
     neighbor 1234:1::3 distance 200
     neighbor 1234:1::3 route-reflector-client
     neighbor 1234:1::3 send-community standard extended
     neighbor 1234:1::4 remote-as 1
     neighbor 1234:1::4 local-as 1
     neighbor 1234:1::4 address-family ovpnuni
     neighbor 1234:1::4 distance 200
     neighbor 1234:1::4 route-reflector-client
     neighbor 1234:1::4 send-community standard extended
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz7r2-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set aspath 1000
     !
     exit
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
    interface loopback2
     vrf forwarding v2
     ipv4 address 9.9.2.2 255.255.255.255
     ipv6 address 9992::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v3
     ipv4 address 9.9.3.2 255.255.255.255
     ipv6 address 9993::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v4
     ipv4 address 9.9.4.2 255.255.255.255
     ipv6 address 9994::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback41
     vrf forwarding v4
     ipv4 address 9.9.4.222 255.255.255.255
     ipv6 address 9994::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback42
     vrf forwarding v4
     ipv4 address 9.9.4.102 255.255.255.255
     ipv6 address 9994::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.2
     address-family ovpnuni
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family ovpnuni
     neighbor 1.1.1.1 distance 200
     neighbor 1.1.1.1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 advertise 9994::2/128 route-map rm1
     afi-ovrf v4 advertise 9994::222/128 route-map rm1
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     address-family ovpnuni
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family ovpnuni
     neighbor 1234:1::1 distance 200
     neighbor 1234:1::1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 advertise 9.9.4.2/32 route-map rm1
     afi-ovrf v4 advertise 9.9.4.222/32 route-map rm1
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
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v4
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz7r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set aspath 1000 1000 1000
     !
     exit
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
    interface loopback41
     vrf forwarding v4
     ipv4 address 9.9.4.222 255.255.255.255
     ipv6 address 9994::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback42
     vrf forwarding v4
     ipv4 address 9.9.4.103 255.255.255.255
     ipv6 address 9994::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234:1::3 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family ovpnuni
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family ovpnuni
     neighbor 1.1.1.1 distance 200
     neighbor 1.1.1.1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 advertise 9994::3/128 route-map rm1
     afi-ovrf v4 advertise 9994::222/128 route-map rm1
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family ovpnuni
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family ovpnuni
     neighbor 1234:1::1 distance 200
     neighbor 1234:1::1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 advertise 9.9.4.3/32 route-map rm1
     afi-ovrf v4 advertise 9.9.4.222/32 route-map rm1
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
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v4
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz7r4-log.run
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
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v2
     ipv4 address 9.9.2.4 255.255.255.255
     ipv6 address 9992::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v3
     ipv4 address 9.9.3.4 255.255.255.255
     ipv6 address 9993::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v4
     ipv4 address 9.9.4.4 255.255.255.255
     ipv6 address 9994::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.0
     ipv6 address 1234:1::4 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     address-family ovpnuni
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family ovpnuni
     neighbor 1.1.1.1 distance 200
     neighbor 1.1.1.1 send-community standard extended
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
     router-id 6.6.6.4
     address-family ovpnuni
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family ovpnuni
     neighbor 1234:1::1 distance 200
     neighbor 1234:1::1 send-community standard extended
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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

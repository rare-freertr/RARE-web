# Example: bgp prefix hammering
    
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
    logging file debug ../binTmp/zzz63r1-log.run
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
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 2222::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.255
     ipv6 address 4444::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234:1::1 ffff:ffff::
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
    interface ethernet3
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet5
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family unicast
     neighbor 1.1.1.2 remote-as 1
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 200
     neighbor 1.1.1.2 route-reflector-client
     neighbor 1.1.1.3 remote-as 1
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family unicast
     neighbor 1.1.1.3 distance 200
     neighbor 1.1.1.3 route-reflector-client
     neighbor 1.1.1.4 remote-as 1
     neighbor 1.1.1.4 local-as 1
     neighbor 1.1.1.4 address-family unicast
     neighbor 1.1.1.4 distance 200
     neighbor 1.1.1.4 route-reflector-client
     neighbor 1.1.1.5 remote-as 1
     neighbor 1.1.1.5 local-as 1
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 200
     neighbor 1.1.1.5 route-reflector-client
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast
     neighbor 1234:1::2 remote-as 1
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 200
     neighbor 1234:1::2 route-reflector-client
     neighbor 1234:1::3 remote-as 1
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family unicast
     neighbor 1234:1::3 distance 200
     neighbor 1234:1::3 route-reflector-client
     neighbor 1234:1::4 remote-as 1
     neighbor 1234:1::4 local-as 1
     neighbor 1234:1::4 address-family unicast
     neighbor 1234:1::4 distance 200
     neighbor 1234:1::4 route-reflector-client
     neighbor 1234:1::6 remote-as 1
     neighbor 1234:1::6 local-as 1
     neighbor 1234:1::6 address-family unicast
     neighbor 1234:1::6 distance 200
     neighbor 1234:1::6 route-reflector-client
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
    logging file debug ../binTmp/zzz63r2-log.run
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
     ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 4.4.4.2 255.255.255.255
     ipv6 address 4444::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.2
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
    logging file debug ../binTmp/zzz63r3-log.run
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
     ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 4.4.4.3 255.255.255.255
     ipv6 address 4444::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234:1::3 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
    logging file debug ../binTmp/zzz63r4-log.run
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
     ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 4.4.4.4 255.255.255.255
     ipv6 address 4444::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.0
     ipv6 address 1234:1::4 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.4
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
    
    **r5:**
    ```
    hostname r5
    buggy
    !
    logging file debug ../binTmp/zzz63r5-log.run
    !
    route-map all
     sequence 10 action permit
     !
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.0
     ipv6 address 1234:1::5 ffff:ffff::
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
    
    **r6:**
    ```
    hostname r6
    buggy
    !
    logging file debug ../binTmp/zzz63r6-log.run
    !
    route-map all
     sequence 10 action permit
     !
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.0
     ipv6 address 1234:1::6 ffff:ffff::
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

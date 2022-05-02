# Example: bgp prefix packing
    
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
    logging file debug ../binTmp/zzz50r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 2222::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback5
     vrf forwarding v1
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 2222::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback6
     vrf forwarding v1
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 2222::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback7
     vrf forwarding v1
     ipv4 address 2.2.2.7 255.255.255.255
     ipv6 address 2222::7 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback8
     vrf forwarding v1
     ipv4 address 2.2.2.8 255.255.255.255
     ipv6 address 2222::8 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.0.0.0
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.2 remote-as 2
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 2
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
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
    logging file debug ../binTmp/zzz50r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.255
     ipv6 address 3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.255
     ipv6 address 3333::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.255
     ipv6 address 3333::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v1
     ipv4 address 3.3.3.4 255.255.255.255
     ipv6 address 3333::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback5
     vrf forwarding v1
     ipv4 address 3.3.3.5 255.255.255.255
     ipv6 address 3333::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback6
     vrf forwarding v1
     ipv4 address 3.3.3.6 255.255.255.255
     ipv6 address 3333::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback7
     vrf forwarding v1
     ipv4 address 3.3.3.7 255.255.255.255
     ipv6 address 3333::7 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback8
     vrf forwarding v1
     ipv4 address 3.3.3.8 255.255.255.255
     ipv6 address 3333::8 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.0.0.0
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
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

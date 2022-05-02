# Example: ebgp prefix withdraw with soft-reconfig
    
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
    logging file debug ../binTmp/zzz36r1-log.run
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
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 resend-packet
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 resend-packet
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
     neighbor 1.1.1.2 soft-reconfiguration
     neighbor 1.1.1.3 remote-as 3
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family unicast
     neighbor 1.1.1.3 distance 20
     neighbor 1.1.1.3 soft-reconfiguration
     neighbor 1.1.1.4 remote-as 4
     neighbor 1.1.1.4 local-as 1
     neighbor 1.1.1.4 address-family unicast
     neighbor 1.1.1.4 distance 20
     neighbor 1.1.1.4 soft-reconfiguration
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
     neighbor 1234:1::2 soft-reconfiguration
     neighbor 1234:1::3 remote-as 3
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family unicast
     neighbor 1234:1::3 distance 20
     neighbor 1234:1::3 soft-reconfiguration
     neighbor 1234:1::4 remote-as 4
     neighbor 1234:1::4 local-as 1
     neighbor 1234:1::4 address-family unicast
     neighbor 1234:1::4 distance 20
     neighbor 1234:1::4 soft-reconfiguration
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
    logging file debug ../binTmp/zzz36r2-log.run
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
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
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
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 soft-reconfiguration
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
     neighbor 1234:1::1 soft-reconfiguration
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
    logging file debug ../binTmp/zzz36r3-log.run
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
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234:1::3 ffff:ffff::
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
     local-as 3
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 3
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 3
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 soft-reconfiguration
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
    logging file debug ../binTmp/zzz36r4-log.run
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
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     local-as 4
     router-id 4.4.4.4
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     neighbor 1.1.1.1 local-as 4
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 4
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     neighbor 1234:1::1 local-as 4
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 soft-reconfiguration
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

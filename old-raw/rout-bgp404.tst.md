# Example: confed bgp with labels
    
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
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     no description
     mtu 1500
     macaddr 0014.5938.356f
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.3 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     no description
     mtu 1500
     macaddr 007a.2311.1d28
     vrf forwarding v1
     ipv4 address 3.3.4.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::3 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family labeled
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family labeled
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 confederation-peer
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family labeled
     neighbor 1234::2 remote-as 2
     no neighbor 1234::2 description
     neighbor 1234::2 local-as 1
     neighbor 1234::2 address-family labeled
     neighbor 1234::2 distance 20
     neighbor 1234::2 confederation-peer
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
    logging file debug ../binTmp/zzz79r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff:ffff::
     mpls enable
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
     local-as 2
     router-id 4.4.4.2
     address-family labeled
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family labeled
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 confederation-peer
     neighbor 1.1.1.3 remote-as 3
     no neighbor 1.1.1.3 description
     neighbor 1.1.1.3 local-as 2
     neighbor 1.1.1.3 address-family labeled
     neighbor 1.1.1.3 distance 20
     neighbor 1.1.1.3 confederation-peer
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     address-family labeled
     neighbor 1234::1 remote-as 1
     no neighbor 1234::1 description
     neighbor 1234::1 local-as 2
     neighbor 1234::1 address-family labeled
     neighbor 1234::1 distance 20
     neighbor 1234::1 confederation-peer
     neighbor 1234::3 remote-as 3
     no neighbor 1234::3 description
     neighbor 1234::3 local-as 2
     neighbor 1234::3 address-family labeled
     neighbor 1234::3 distance 20
     neighbor 1234::3 confederation-peer
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
    logging file debug ../binTmp/zzz79r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234::3 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     no description
     mtu 1500
     macaddr 007b.164c.715c
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
     macaddr 004c.0b11.0243
     vrf forwarding v1
     ipv4 address 3.3.4.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 4321::1 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 3
     router-id 4.4.4.3
     address-family labeled
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 3
     neighbor 1.1.1.2 address-family labeled
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 confederation-peer
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     address-family labeled
     neighbor 1234::2 remote-as 2
     no neighbor 1234::2 description
     neighbor 1234::2 local-as 3
     neighbor 1234::2 address-family labeled
     neighbor 1234::2 distance 20
     neighbor 1234::2 confederation-peer
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

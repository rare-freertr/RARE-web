# Example: unified mpls with sr
    
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
    logging file debug ../binTmp/zzz42r1-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 002a.3602.690b
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.6 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0035.1a06.5943
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
     address-family labeled
     neighbor 2.2.2.3 remote-as 1
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
     address-family labeled
     neighbor 4321::3 remote-as 1
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
    !
    !
    !
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
    logging file debug ../binTmp/zzz42r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
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
    logging file debug ../binTmp/zzz42r3-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
     address-family labeled
     neighbor 1.1.1.10 remote-as 1
     neighbor 1.1.1.10 local-as 1
     neighbor 1.1.1.10 address-family labeled
     neighbor 1.1.1.10 distance 200
     neighbor 1.1.1.10 route-reflector-client
     neighbor 1.1.1.10 next-hop-self
     neighbor 2.2.2.1 remote-as 1
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
     address-family labeled
     neighbor 1234:3::2 remote-as 1
     neighbor 1234:3::2 local-as 1
     neighbor 1234:3::2 address-family labeled
     neighbor 1234:3::2 distance 200
     neighbor 1234:3::2 route-reflector-client
     neighbor 1234:3::2 next-hop-self
     neighbor 4321::1 remote-as 1
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
    !
    !
    !
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
    logging file debug ../binTmp/zzz42r4-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.4
     segrout 10 4
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.4
     segrout 10 4
     redistribute connected
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
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.13 255.255.255.252
     ipv6 address 1234:4::1 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     address-family labeled
     neighbor 1.1.1.9 remote-as 1
     neighbor 1.1.1.9 local-as 1
     neighbor 1.1.1.9 address-family labeled
     neighbor 1.1.1.9 distance 200
     neighbor 1.1.1.9 route-reflector-client
     neighbor 1.1.1.9 next-hop-self
     neighbor 2.2.2.6 remote-as 1
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
     address-family labeled
     neighbor 1234:3::1 remote-as 1
     neighbor 1234:3::1 local-as 1
     neighbor 1234:3::1 address-family labeled
     neighbor 1234:3::1 distance 200
     neighbor 1234:3::1 route-reflector-client
     neighbor 1234:3::1 next-hop-self
     neighbor 4321::6 remote-as 1
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
    !
    !
    !
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
    logging file debug ../binTmp/zzz42r5-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.5
     segrout 10 5
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.5
     segrout 10 5
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.14 255.255.255.252
     ipv6 address 1234:4::2 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.17 255.255.255.252
     ipv6 address 1234:5::1 ffff:ffff::
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
    
    **r6:**
    ```
    hostname r6
    buggy
    !
    logging file debug ../binTmp/zzz42r6-log.run
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.6
     segrout 10 6
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.6
     segrout 10 6
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.18 255.255.255.252
     ipv6 address 1234:5::2 ffff:ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface pwether1
     mtu 1500
     macaddr 0026.2552.1d61
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback0 pweompls 2.2.2.1 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0053.027e.5877
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
     address-family labeled
     neighbor 2.2.2.4 remote-as 1
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
     address-family labeled
     neighbor 4321::4 remote-as 1
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
    !
    !
    !
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

# Example: multicast between pim and pim over bier
    
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
    logging file debug ../binTmp/zzz15r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     bier 256 10 1
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     bier 256 10 1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv4 pim enable
     ipv4 pim bier-tunnel 1
     ipv4 pim join-source loopback1
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     ipv6 pim enable
     ipv6 pim bier-tunnel 1
     ipv6 pim join-source loopback1
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 pim enable
     ipv4 pim bier-tunnel 1
     ipv4 pim join-source loopback1
     ipv6 address 1234::1 ffff::
     ipv6 pim enable
     ipv6 pim bier-tunnel 1
     ipv6 pim join-source loopback1
     mpls enable
     mpls ldp4
     mpls ldp6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.2 255.255.255.252
     ipv4 pim enable
     ipv6 address 4444::2 ffff:ffff::
     ipv6 pim enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast multicast
     neighbor 2.2.2.4 remote-as 1
     no neighbor 2.2.2.4 description
     neighbor 2.2.2.4 local-as 1
     neighbor 2.2.2.4 address-family unicast multicast
     neighbor 2.2.2.4 distance 200
     neighbor 2.2.2.4 update-source loopback1
     redistribute connected
     redistribute static
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast multicast
     neighbor 4321::4 remote-as 1
     no neighbor 4321::4 description
     neighbor 4321::4 local-as 1
     neighbor 4321::4 address-family unicast multicast
     neighbor 4321::4 distance 200
     neighbor 4321::4 update-source loopback1
     redistribute connected
     redistribute static
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
    logging file debug ../binTmp/zzz15r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     bier 256 10 2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     bier 256 10 2
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1235::2 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
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
    logging file debug ../binTmp/zzz15r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.3
     bier 256 10 3
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     bier 256 10 3
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv4 address 1.1.2.3 255.255.255.0
     ipv6 address 1235::3 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.3.3 255.255.255.0
     ipv6 address 1236::3 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz15r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.4
     bier 256 10 4
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.4
     bier 256 10 4
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv4 pim enable
     ipv4 pim bier-tunnel 4
     ipv4 pim join-source loopback1
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     ipv6 pim enable
     ipv6 pim bier-tunnel 4
     ipv6 pim join-source loopback1
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.14 255.255.255.255
     ipv6 address 4321::14 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.3.4 255.255.255.0
     ipv4 pim enable
     ipv4 pim bier-tunnel 4
     ipv4 pim join-source loopback1
     ipv6 address 1236::4 ffff::
     ipv6 pim enable
     ipv6 pim bier-tunnel 4
     ipv6 pim join-source loopback1
     mpls enable
     mpls ldp4
     mpls ldp6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 5.5.5.2 255.255.255.252
     ipv4 pim enable
     ipv6 address 5555::2 ffff:ffff::
     ipv6 pim enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     no safe-ebgp
     address-family unicast multicast
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family unicast multicast
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback1
     redistribute connected
     redistribute static
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast multicast
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family unicast multicast
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback1
     redistribute connected
     redistribute static
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
    logging file debug ../binTmp/zzz15r5-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.252
     ipv4 pim enable
     ipv6 address 4444::1 ffff:ffff::
     ipv6 pim enable
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
    ipv4 route v1 0.0.0.0 0.0.0.0 4.4.4.2
    !
    ipv6 route v1 :: :: 4444::2
    !
    !
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
    logging file debug ../binTmp/zzz15r6-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 5.5.5.1 255.255.255.252
     ipv4 pim enable
     ipv6 address 5555::1 ffff:ffff::
     ipv6 pim enable
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
    ipv4 route v1 0.0.0.0 0.0.0.0 5.5.5.2
    !
    ipv6 route v1 :: :: 5555::2
    !
    ipv4 mroute v1 0.0.0.0 0.0.0.0 5.5.5.2
    !
    ipv6 mroute v1 :: :: 5555::2
    !
    !
    !
    !
    !
    ipv4 multicast v1 join-group 232.2.2.2 4.4.4.1
    !
    ipv6 multicast v1 join-group ff06::1 4444::1
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

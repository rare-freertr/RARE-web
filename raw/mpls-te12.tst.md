# Example: ldp and te
    
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.2
     tunnel mode pweompls
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     ipv6 address 3333::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 4321
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::2
     tunnel mode pweompls
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.252
     ipv6 address 4444::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel3
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.2
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 5.5.5.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel4
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::2
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 5555::1 ffff::
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
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
    !
    !
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 2345::1 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     mpls rsvp4
     mpls rsvp6
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.2.2
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 2345::2
    !
    !
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
     label4mode per-prefix
     label6mode per-prefix
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 2345::2 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.1
     tunnel mode pweompls
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     ipv6 address 3333::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 4321
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::1
     tunnel mode pweompls
     vrf forwarding v1
     ipv4 address 4.4.4.2 255.255.255.252
     ipv6 address 4444::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel3
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.1
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 5.5.5.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel4
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::1
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 5555::2 ffff::
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.2.1
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 2345::1
    !
    !
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

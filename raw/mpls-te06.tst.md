# Example: te over framerelay
    
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
    logging file debug ../binTmp/zzz46r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface serial1
     encapsulation framerelay
     framerelay mode dce
     framerelay dlci 123
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source serial1
     tunnel destination 1.1.1.2
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source serial1
     tunnel destination 1234::2
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 4321::1 ffff::
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz46r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface serial1
     encapsulation framerelay
     framerelay mode dte
     framerelay dlci 123
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source serial1
     tunnel destination 1.1.1.1
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source serial1
     tunnel destination 1234::1
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 4321::2 ffff::
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

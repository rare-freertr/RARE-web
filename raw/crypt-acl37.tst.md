# Example: ingress destination port matching access list
    
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
    logging file debug ../binTmp/zzz39r1-log.run
    !
    access-list test4
     sequence 10 deny all any all any 123
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all any all any 123
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff:ffff::
     ipv6 access-group-in test6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 123
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.2
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.1.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 123
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::2
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel3
     tunnel key 321
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.2
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.3.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel4
     tunnel key 321
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::2
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.4.1 255.255.255.0
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
    logging file debug ../binTmp/zzz39r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 123
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.1
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.1.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 123
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::1
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel3
     tunnel key 321
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.1
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.3.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel4
     tunnel key 321
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::1
     tunnel mode pckoudp
     vrf forwarding v1
     ipv4 address 2.2.4.2 255.255.255.0
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

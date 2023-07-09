# Example: egress source matching access list
    
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
    logging file debug ../binTmp/zzz29r1-log.run
    !
    access-list test4
     sequence 10 deny all 2.2.2.102 255.255.255.255 all any all
     sequence 20 deny all 2.2.2.202 255.255.255.255 all any all
     sequence 30 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
     sequence 20 deny all 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
     sequence 30 permit all any all any all
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
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.102 255.255.255.255
     ipv6 address 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-out test4
     ipv6 address 1234::1 ffff:ffff::
     ipv6 access-group-out test6
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
    !
    ipv6 route v1 :: :: 1234::2
    !
    !
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
    logging file debug ../binTmp/zzz29r2-log.run
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
     ipv4 address 2.2.2.201 255.255.255.255
     ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.202 255.255.255.255
     ipv6 address 4321::202 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1
    !
    ipv6 route v1 :: :: 1234::1
    !
    !
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

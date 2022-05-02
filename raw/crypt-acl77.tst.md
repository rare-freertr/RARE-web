# Example: egress sgt matching access list
    
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
    logging file debug ../binTmp/zzz44r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     sgt enable
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234::1 ffff:ffff::
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
    logging file debug ../binTmp/zzz44r2-log.run
    !
    access-list test4
     sequence 10 deny all any all any all sgt 123
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all any all any all sgt 123
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
     sgt enable
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv4 access-group-out test4
     ipv6 address 1234::2 ffff:ffff::
     ipv6 access-group-out test6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     sgt assign 123
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.252
     ipv6 address 4321::1 ffff:ffff::
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
    logging file debug ../binTmp/zzz44r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.252
     ipv6 address 4321::2 ffff:ffff::
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
    ipv4 route v1 0.0.0.0 0.0.0.0 2.2.2.1
    !
    ipv6 route v1 :: :: 4321::1
    !
    !
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

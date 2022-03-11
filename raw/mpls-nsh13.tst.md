# Example: nsh mix of ip and ethernet
    
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
    logging file debug ../binTmp/zzz56r1-log.run
    !
    access-list test4
     sequence 10 permit all 1.1.1.1 255.255.255.255 all any all
     exit
    !
    access-list test6
     sequence 10 permit all 1111::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1111::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     nsh enable
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
    ipv4 pbr v1 sequence 10 test4 v1 nsh 2 255
    !
    ipv6 pbr v1 sequence 10 test6 v1 nsh 2 255
    !
    !
    !
    !
    !
    nsh 2 255 interface ethernet1 0000.1111.2222
    !
    nsh 3 253 route v1
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
    logging file debug ../binTmp/zzz56r2-log.run
    !
    vrf definition tester
     exit
    !
    interface ethernet1
     no description
     nsh enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     nsh enable
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
    nsh 2 254 interface ethernet2 0000.1111.2222
    !
    nsh 3 254 interface ethernet1 0000.1111.2222
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
    logging file debug ../binTmp/zzz56r3-log.run
    !
    vrf definition tester
     exit
    !
    interface ethernet1
     no description
     nsh enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     nsh enable
     nsh xconnect 3 255
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
    nsh 2 253 interface ethernet2 0000.1111.2222 rawpack keephdr
    !
    nsh 3 255 interface ethernet1 0000.1111.2222
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
    logging file debug ../binTmp/zzz56r4-log.run
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 host-static 1.1.1.1 0000.1111.2222
     ipv6 address 1111::2 ffff::
     ipv6 host-static 1111::1 0000.1111.2222
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

# Example: gre over gre
    
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
    logging file debug ../binTmp/zzz28r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.2
     tunnel mode gre
     vrf forwarding v1
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel vrf v1
     tunnel source tunnel1
     tunnel destination 1234::2
     tunnel mode gre
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.0
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
    logging file debug ../binTmp/zzz28r2-log.run
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
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.1
     tunnel mode gre
     vrf forwarding v1
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel vrf v1
     tunnel source tunnel1
     tunnel destination 1234::1
     tunnel mode gre
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.0
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

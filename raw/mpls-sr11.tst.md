# Example: sr te over exthdr
    
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
    logging file debug ../binTmp/zzz67r1-log.run
    !
    access-list all
     sequence 10 permit all any all any all
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
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 srh enable
     ipv6 address 1234::1 ffff::
     ipv6 srh enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.2.3
     tunnel domain-name 1.1.1.2
     tunnel mode srext
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1235::3
     tunnel domain-name 1234::2
     tunnel mode srext
     vrf forwarding v1
     ipv6 address 3333::1 ffff::
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
    logging file debug ../binTmp/zzz67r2-log.run
    !
    access-list all
     sequence 10 permit all any all any all
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 srh enable
     ipv6 address 1234::2 ffff::
     ipv6 srh enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv4 srh enable
     ipv6 address 1235::2 ffff::
     ipv6 srh enable
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
    logging file debug ../binTmp/zzz67r3-log.run
    !
    access-list all
     sequence 10 permit all any all any all
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
     ipv4 address 1.1.2.3 255.255.255.0
     ipv4 srh enable
     ipv6 address 1235::3 ffff::
     ipv6 srh enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.1
     tunnel domain-name 1.1.2.2
     tunnel mode srext
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::1
     tunnel domain-name 1235::2
     tunnel mode srext
     vrf forwarding v1
     ipv6 address 3333::2 ffff::
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

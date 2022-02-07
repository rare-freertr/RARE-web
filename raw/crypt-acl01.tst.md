# Example: ingress protocol matching access list
    
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
    logging file debug ../binTmp/zzz72r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
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
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff:ffff::
     ipv6 access-group-in test6
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
    logging file debug ../binTmp/zzz72r2-log.run
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
    !
    !
    !
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
    
=== "Verification"
    
    ```
    r1#
    r1#
    r1#show access-list test4
    r1#show access-list test4
     sequence 10 deny 1 any all any all
      match=tx=0(0) rx=256(4) drp=0(0) accessed=00:00:06 ago, 00:00:00 timeout
     sequence 20 permit all any all any all
      match=tx=0(0) rx=0(0) drp=0(0) accessed=never ago, 00:00:00 timeout
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show access-list test6
    r1#show access-list test6
     sequence 10 deny 58 any all any all
      match=tx=0(0) rx=608(8) drp=0(0) accessed=00:00:01 ago, 00:00:00 timeout
     sequence 20 permit all any all any all
      match=tx=0(0) rx=0(0) drp=0(0) accessed=never ago, 00:00:00 timeout
    r1#
    r1#
    ```

# Example: ppp routes with radius authentication
    
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
    logging file debug ../binTmp/zzz40r1-log.run
    !
    prefix-list p4
     sequence 10 permit 0.0.0.0/0 ge 0 le 0
     exit
    !
    prefix-list p6
     sequence 10 permit ::/0 ge 0 le 0
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
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation ppp
     ppp username c
     ppp password $v10$Yw==
     ppp ip4cp open
     ppp ip4cp local 0.0.0.0
     ppp ip6cp open
     vrf forwarding v1
     ipv4 address dynamic dynamic
     ipv4 gateway-prefix p4
     ipv6 address dynamic dynamic
     ipv6 gateway-prefix p6
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
    logging file debug ../binTmp/zzz40r2-log.run
    !
    aaa radius usr
     secret $v10$Yw==
     server 3.3.3.3
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
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation ppp
     ppp authentication usr
     ppp ip4cp local 1.1.1.2
     ppp ip6cp open
     vrf forwarding v1
     ipv4 address dynamic dynamic
     ipv6 address dynamic dynamic
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
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
    client proxy p1
    !
    end
    ```
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz40r3-log.run
    !
    aaa userlist usr
     username c
     username c password $v10$Yw==
     username c ipv4addr 1.1.1.1
     username c ipv4route 2.2.2.1/32 dist 123
     username c ipv6addr 1234::1
     username c ipv6ifid 1234-1234-1234-1234
     username c ipv6route 4321::1/128 dist 222
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
     ipv4 address 3.3.3.3 255.255.255.0
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
    server radius rad
     authentication usr
     secret $v10$Yw==
     logging
     vrf v1
     exit
    !
    !
    end
    ```

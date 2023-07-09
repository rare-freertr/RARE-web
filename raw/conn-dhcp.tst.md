# Example: dhcp
    
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
    logging file debug ../binTmp/zzz20r1-log.run
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
     ipv4 address 4.4.4.4 255.255.255.255
     ipv6 address 4444::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
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
    server dhcp4 dh4
     pool 1.1.1.2 1.1.1.199
     gateway 1.1.1.1
     netmask 255.255.255.0
     no dns-server
     domain-name 
     interface ethernet1
     vrf v1
     exit
    !
    server dhcp6 dh6
     gateway 1234::1
     netmask ffff:ffff:ffff:ffff::
     no dns-server
     domain-name 
     interface ethernet1
     vrf v1
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
    logging file debug ../binTmp/zzz20r2-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 0.0.0.0 255.255.255.255
     ipv4 gateway-prefix p4
     ipv4 dhcp-client enable
     ipv6 address fe80::200:ff:fe00:2222 ffff:ffff:ffff:ffff::
     ipv6 gateway-prefix p6
     ipv6 dhcp-client enable
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

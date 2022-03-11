# Example: policy routing with interface and nexthop between vrfs
    
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
    logging file debug ../binTmp/zzz98r1-log.run
    !
    access-list a2b4
     sequence 10 permit all 2.2.2.101 255.255.255.255 all 2.2.2.201 255.255.255.255 all
     exit
    !
    access-list a2b6
     sequence 10 permit all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
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
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
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
    ipv4 pbr v1 sequence 10 a2b4 v1 interface ethernet1 nexthop 1.1.1.2
    !
    ipv6 pbr v1 sequence 10 a2b6 v1 interface ethernet1 nexthop 1234:1::2
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
    logging file debug ../binTmp/zzz98r2-log.run
    !
    access-list a2b4
     sequence 10 permit all 2.2.2.101 255.255.255.255 all 2.2.2.201 255.255.255.255 all
     exit
    !
    access-list a2b6
     sequence 10 permit all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
     exit
    !
    access-list b2a4
     sequence 10 permit all 2.2.2.201 255.255.255.255 all 2.2.2.101 255.255.255.255 all
     exit
    !
    access-list b2a6
     sequence 10 permit all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    vrf definition v2
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v2
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
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
    ipv4 pbr v1 sequence 10 a2b4 v2 interface ethernet2 nexthop 1.1.1.5
    !
    ipv6 pbr v1 sequence 10 a2b6 v2 interface ethernet2 nexthop 1234:2::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 pbr v2 sequence 10 b2a4 v1 interface ethernet1 nexthop 1.1.1.1
    !
    ipv6 pbr v2 sequence 10 b2a6 v1 interface ethernet1 nexthop 1234:1::1
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
    logging file debug ../binTmp/zzz98r3-log.run
    !
    access-list b2a4
     sequence 10 permit all 2.2.2.201 255.255.255.255 all 2.2.2.101 255.255.255.255 all
     exit
    !
    access-list b2a6
     sequence 10 permit all 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
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
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.201 255.255.255.255
     ipv6 address 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
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
    ipv4 pbr v1 sequence 10 b2a4 v1 interface ethernet1 nexthop 1.1.1.6
    !
    ipv6 pbr v1 sequence 10 b2a6 v1 interface ethernet1 nexthop 1234:2::2
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

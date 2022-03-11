# Example: ldp over ethernet
    
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
    logging file debug ../binTmp/zzz79r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     no ipv4 unreachables
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     no ipv6 unreachables
     ipv6 access-group-in test6
     mpls enable
     mpls ldp4
     mpls ldp6
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
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
    !
    !
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
    logging file debug ../binTmp/zzz79r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     no ipv4 unreachables
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     no ipv6 unreachables
     ipv6 access-group-in test6
     mpls enable
     mpls ldp4
     mpls ldp6
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
    !
    !
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
    r1#show mpls forw
    r1#show mpls forw
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface     | hop     | label      | targets | bytes |
     |---------|----------|-----------|---------|------------|---------|-------|
     | 101818  | v1:6     | null      | null    | unlabelled | local   | 640   |
     | 421149  | v1:4     | null      | null    | unlabelled | local   | 640   |
     | 573127  | v1:6     | ethernet1 | 1234::2 | 942483     |         | 0     |
     | 642799  | v1:4     | ethernet1 | 1.1.1.2 | 600697     |         | 0     |
     | 847440  | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 1034741 | tester:4 | null      | null    | unlabelled | local   | 0     |
     |_________|__________|___________|_________|____________|_________|_______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 ldp v1 sum
    r1#show ipv4 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                     |
     | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
     |-------|--------|-------|--------|-------|--------|----------|----------|
     | 4     | 4      | 0     | 0      | 0     | 0      | 1.1.1.2  | 00:00:19 |
     |_______|________|_______|________|_______|________|__________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 ldp v1 sum
    r1#show ipv6 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                     |
     | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
     |-------|--------|-------|--------|-------|--------|----------|----------|
     | 4     | 4      | 0     | 0      | 0     | 0      | 1234::2  | 00:00:19 |
     |_______|________|_______|________|_______|________|__________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 ldp v1 dat
    r1#show ipv4 ldp v1 dat
     |~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~|
     | prefix     | local  | remote | hop     |
     |------------|--------|--------|---------|
     | 1.1.1.0/24 | 421149 |        | null    |
     | 1.1.1.1/32 | 421149 |        | null    |
     | 2.2.2.1/32 | 421149 |        | null    |
     | 2.2.2.2/32 | 642799 | 600697 | 1.1.1.2 |
     |____________|________|________|_________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 ldp v1 dat
    r1#show ipv6 ldp v1 dat
     |~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~~|
     | prefix      | local  | remote | hop     |
     |-------------|--------|--------|---------|
     | 1234::/16   | 101818 |        | null    |
     | 1234::1/128 | 101818 |        | null    |
     | 4321::1/128 | 101818 |        | null    |
     | 4321::2/128 | 573127 | 942483 | 1234::2 |
     |_____________|________|________|_________|
    r1#
    r1#
    ```

# Example: mpls inspection with selective egress drop
    
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
    logging file debug ../binTmp/zzz11r1-log.run
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
     ipv6 address 1234:1::1 ffff:ffff::
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
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    !
    !
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
    logging file debug ../binTmp/zzz11r2-log.run
    !
    access-list test
     sequence 10 permit all 2.2.2.3 255.255.255.255 all any all
     sequence 20 permit all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all any all
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
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     mpls inspect mac drop-tx allow-list test
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1234:2::2 ffff:ffff::
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
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.2.3
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::3
    !
    !
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
    logging file debug ../binTmp/zzz11r3-log.run
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
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.3 255.255.255.0
     no ipv4 unreachables
     ipv4 access-group-in test4
     ipv6 address 1234:2::3 ffff:ffff::
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.2.2
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.2.2
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    !
    !
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
    r2#
    r2#
    r2#show mpls insp eth1 sess
    r2#show mpls insp eth1 sess
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
     | tx  | 1   | 0   | 2.2.2.3 | 658242198 | 2.2.2.1 | 658242198 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 658242199 | 2.2.2.1 | 658242199 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 658242200 | 2.2.2.1 | 658242200 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 658242201 | 2.2.2.1 | 658242201 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 658242202 | 2.2.2.1 | 658242202 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873684 | 2.2.2.2 | 914873684 | 1  | 1  | 44 | 44 | 00:00:17 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873685 | 2.2.2.2 | 914873685 | 1  | 1  | 44 | 44 | 00:00:17 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873686 | 2.2.2.2 | 914873686 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873687 | 2.2.2.2 | 914873687 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873688 | 2.2.2.2 | 914873688 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873689 | 2.2.2.2 | 914873689 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873690 | 2.2.2.2 | 914873690 | 1  | 1  | 44 | 44 | 00:00:16 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873691 | 2.2.2.3 | 914873691 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873692 | 2.2.2.3 | 914873692 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873693 | 2.2.2.3 | 914873693 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873694 | 2.2.2.3 | 914873694 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 914873695 | 2.2.2.3 | 914873695 | 1  | 1  | 44 | 44 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772454 | 4321::2 | 276772454 | 1  | 1  | 24 | 24 | 00:00:11 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772455 | 4321::2 | 276772455 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772456 | 4321::2 | 276772456 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772457 | 4321::2 | 276772457 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772458 | 4321::2 | 276772458 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772459 | 4321::2 | 276772459 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772460 | 4321::3 | 276772460 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772461 | 4321::3 | 276772461 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772462 | 4321::3 | 276772462 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772463 | 4321::3 | 276772463 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 276772464 | 4321::3 | 276772464 | 1  | 1  | 24 | 24 | 00:00:10 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::3 | 370704120 | 4321::1 | 370704120 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 370704121 | 4321::1 | 370704121 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 370704122 | 4321::1 | 370704122 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 370704123 | 4321::1 | 370704123 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 370704124 | 4321::1 | 370704124 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show mpls insp eth1 top
    r2#show mpls insp eth1 top
     |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
     |         | packet  | byte      |          |
     | addr    | rx | tx | rx  | tx  | time     |
     |---------|----|----|-----|-----|----------|
     | 2.2.2.1 | 17 | 17 | 748 | 748 | 00:00:17 |
     | 2.2.2.2 | 7  | 7  | 308 | 308 | 00:00:17 |
     | 2.2.2.3 | 10 | 10 | 440 | 440 | 00:00:10 |
     | 4321::1 | 16 | 16 | 384 | 384 | 00:00:12 |
     | 4321::2 | 6  | 6  | 144 | 144 | 00:00:12 |
     | 4321::3 | 10 | 10 | 240 | 240 | 00:00:10 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

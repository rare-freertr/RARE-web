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
    logging file debug ../binTmp/zzz20r1-log.run
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
    logging file debug ../binTmp/zzz20r2-log.run
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
    logging file debug ../binTmp/zzz20r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|----------------|----------------|
     | rx  | 1   | 0   | 2.2.2.1 | 328611411 | 2.2.2.2 | 328611411 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611412 | 2.2.2.2 | 328611412 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611413 | 2.2.2.2 | 328611413 | null | 1  | 1  | 64 | 64 | 00:00:19 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611414 | 2.2.2.2 | 328611414 | null | 1  | 1  | 64 | 64 | 00:00:19 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611415 | 2.2.2.2 | 328611415 | null | 1  | 1  | 64 | 64 | 00:00:19 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611416 | 2.2.2.2 | 328611416 | null | 1  | 1  | 64 | 64 | 00:00:19 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611417 | 2.2.2.2 | 328611417 | null | 1  | 1  | 64 | 64 | 00:00:19 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611418 | 2.2.2.3 | 328611418 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611419 | 2.2.2.3 | 328611419 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611420 | 2.2.2.3 | 328611420 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611421 | 2.2.2.3 | 328611421 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 328611422 | 2.2.2.3 | 328611422 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 1   | 0   | 2.2.2.3 | 704622171 | 2.2.2.1 | 704622171 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 704622172 | 2.2.2.1 | 704622172 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 704622173 | 2.2.2.1 | 704622173 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 704622174 | 2.2.2.1 | 704622174 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 704622175 | 2.2.2.1 | 704622175 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 210829562 | 4321::1 | 210829562 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 210829563 | 4321::1 | 210829563 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 210829564 | 4321::1 | 210829564 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 210829565 | 4321::1 | 210829565 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 210829566 | 4321::1 | 210829566 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 58  | 0   | 4321::1 | 986049558 | 4321::2 | 986049558 | null | 1  | 1  | 64 | 64 | 00:00:15 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049559 | 4321::2 | 986049559 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049560 | 4321::2 | 986049560 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049561 | 4321::2 | 986049561 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049562 | 4321::2 | 986049562 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049563 | 4321::2 | 986049563 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049564 | 4321::3 | 986049564 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049565 | 4321::3 | 986049565 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049566 | 4321::3 | 986049566 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049567 | 4321::3 | 986049567 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 986049568 | 4321::3 | 986049568 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show mpls insp eth1 top
    r2#show mpls insp eth1 top
     |~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
     |         | packet  | byte        |          |
     | addr    | rx | tx | rx   | tx   | time     |
     |---------|----|----|------|------|----------|
     | 2.2.2.1 | 17 | 17 | 1088 | 1088 | 00:00:20 |
     | 2.2.2.2 | 7  | 7  | 448  | 448  | 00:00:20 |
     | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:12 |
     | 4321::1 | 16 | 16 | 1024 | 1024 | 00:00:15 |
     | 4321::2 | 6  | 6  | 384  | 384  | 00:00:15 |
     | 4321::3 | 10 | 10 | 640  | 640  | 00:00:12 |
     |_________|____|____|______|______|__________|
    r2#
    r2#
    ```

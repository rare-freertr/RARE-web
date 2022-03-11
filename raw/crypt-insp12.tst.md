# Example: mpls inspection with selective ingress drop
    
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
    logging file debug ../binTmp/zzz2r1-log.run
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
    logging file debug ../binTmp/zzz2r2-log.run
    !
    access-list test
     sequence 10 permit all any all 2.2.2.3 255.255.255.255 all
     sequence 20 permit all any all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
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
     mpls inspect mac drop-rx allow-list test
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
    logging file debug ../binTmp/zzz2r3-log.run
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
     | tx  | 1   | 0   | 2.2.2.2 | 486067442 | 2.2.2.1 | 486067442 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067443 | 2.2.2.1 | 486067443 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067444 | 2.2.2.1 | 486067444 | null | 1  | 1  | 64 | 64 | 00:00:12 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067445 | 2.2.2.1 | 486067445 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067446 | 2.2.2.1 | 486067446 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067447 | 2.2.2.1 | 486067447 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067448 | 2.2.2.1 | 486067448 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 486067449 | 2.2.2.1 | 486067449 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 801142584 | 2.2.2.1 | 801142584 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 801142585 | 2.2.2.1 | 801142585 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 801142586 | 2.2.2.1 | 801142586 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 801142587 | 2.2.2.1 | 801142587 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 801142588 | 2.2.2.1 | 801142588 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 1   | 0   | 2.2.2.1 | 872031803 | 2.2.2.3 | 872031803 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 872031804 | 2.2.2.3 | 872031804 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 872031805 | 2.2.2.3 | 872031805 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 872031806 | 2.2.2.3 | 872031806 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 872031807 | 2.2.2.3 | 872031807 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::2 | 634111588 | 4321::1 | 634111588 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 634111589 | 4321::1 | 634111589 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 634111590 | 4321::1 | 634111590 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 634111591 | 4321::1 | 634111591 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 634111592 | 4321::1 | 634111592 | null | 1  | 1  | 64 | 64 | 00:00:11 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 58  | 0   | 4321::1 | 901309658 | 4321::3 | 901309658 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901309659 | 4321::3 | 901309659 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901309660 | 4321::3 | 901309660 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901309661 | 4321::3 | 901309661 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901309662 | 4321::3 | 901309662 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::3 | 934325566 | 4321::1 | 934325566 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 934325567 | 4321::1 | 934325567 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 934325568 | 4321::1 | 934325568 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 934325569 | 4321::1 | 934325569 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 934325570 | 4321::1 | 934325570 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
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
     | 2.2.2.1 | 18 | 18 | 1152 | 1152 | 00:00:12 |
     | 2.2.2.2 | 8  | 8  | 512  | 512  | 00:00:12 |
     | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:00 |
     | 4321::1 | 15 | 15 | 960  | 960  | 00:00:11 |
     | 4321::2 | 5  | 5  | 320  | 320  | 00:00:11 |
     | 4321::3 | 10 | 10 | 640  | 640  | 00:00:00 |
     |_________|____|____|______|______|__________|
    r2#
    r2#
    ```

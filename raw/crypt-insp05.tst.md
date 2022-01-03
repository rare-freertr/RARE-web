# Example: mpls inspection
    
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
    logging file debug ../binTmp/zzz1r1-log.run
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
    logging file debug ../binTmp/zzz1r2-log.run
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
     mpls inspect mac
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
    logging file debug ../binTmp/zzz1r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source               | target               | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port       | addr    | port       | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|------------|---------|------------|----|----|----|----|----------|----------------|----------------|
     | tx  | 1   | 0   | 2.2.2.2 | 11799384   | 2.2.2.1 | 11799384   | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 11799385   | 2.2.2.1 | 11799385   | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 11799386   | 2.2.2.1 | 11799386   | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 11799387   | 2.2.2.1 | 11799387   | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 11799388   | 2.2.2.1 | 11799388   | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286584  | 2.2.2.2 | 690286584  | 1  | 1  | 44 | 44 | 00:00:05 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286585  | 2.2.2.2 | 690286585  | 1  | 1  | 44 | 44 | 00:00:05 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286586  | 2.2.2.2 | 690286586  | 1  | 1  | 44 | 44 | 00:00:05 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286587  | 2.2.2.2 | 690286587  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286588  | 2.2.2.2 | 690286588  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286589  | 2.2.2.2 | 690286589  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286590  | 2.2.2.2 | 690286590  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286591  | 2.2.2.2 | 690286591  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286592  | 2.2.2.3 | 690286592  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286593  | 2.2.2.3 | 690286593  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286594  | 2.2.2.3 | 690286594  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286595  | 2.2.2.3 | 690286595  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 690286596  | 2.2.2.3 | 690286596  | 1  | 1  | 44 | 44 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 1   | 0   | 2.2.2.3 | 961287685  | 2.2.2.1 | 961287685  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 961287686  | 2.2.2.1 | 961287686  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 961287687  | 2.2.2.1 | 961287687  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 961287688  | 2.2.2.1 | 961287688  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 961287689  | 2.2.2.1 | 961287689  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 292073856  | 4321::1 | 292073856  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 292073857  | 4321::1 | 292073857  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 292073858  | 4321::1 | 292073858  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 292073859  | 4321::1 | 292073859  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 292073860  | 4321::1 | 292073860  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 956668924  | 4321::1 | 956668924  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 956668925  | 4321::1 | 956668925  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 956668926  | 4321::1 | 956668926  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 956668927  | 4321::1 | 956668927  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 956668928  | 4321::1 | 956668928  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 58  | 0   | 4321::1 | 1069515906 | 4321::2 | 1069515906 | 1  | 1  | 24 | 24 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515907 | 4321::2 | 1069515907 | 1  | 1  | 24 | 24 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515908 | 4321::2 | 1069515908 | 1  | 1  | 24 | 24 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515909 | 4321::2 | 1069515909 | 1  | 1  | 24 | 24 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515910 | 4321::2 | 1069515910 | 1  | 1  | 24 | 24 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515911 | 4321::3 | 1069515911 | 1  | 0  | 24 | 0  | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515912 | 4321::3 | 1069515912 | 1  | 0  | 24 | 0  | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515913 | 4321::3 | 1069515913 | 1  | 1  | 24 | 24 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515914 | 4321::3 | 1069515914 | 1  | 1  | 24 | 24 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515915 | 4321::3 | 1069515915 | 1  | 1  | 24 | 24 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515916 | 4321::3 | 1069515916 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515917 | 4321::3 | 1069515917 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515918 | 4321::3 | 1069515918 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515919 | 4321::3 | 1069515919 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 1069515920 | 4321::3 | 1069515920 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|____________|_________|____________|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.1 | 23 | 23 | 1012 | 1012 | 00:00:05 |
     | 2.2.2.2 | 13 | 13 | 572  | 572  | 00:00:05 |
     | 2.2.2.3 | 10 | 10 | 440  | 440  | 00:00:04 |
     | 4321::1 | 25 | 23 | 600  | 552  | 00:00:04 |
     | 4321::2 | 10 | 10 | 240  | 240  | 00:00:04 |
     | 4321::3 | 15 | 13 | 360  | 312  | 00:00:04 |
     |_________|____|____|______|______|__________|
    r2#
    r2#
    ```

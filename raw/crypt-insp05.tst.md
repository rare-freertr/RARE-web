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
    logging file debug ../binTmp/zzz44r1-log.run
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
    logging file debug ../binTmp/zzz44r2-log.run
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
    logging file debug ../binTmp/zzz44r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source               | target               |      | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port       | addr    | port       | url  | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|------------|---------|------------|------|----|----|----|----|----------|----------------|----------------|
     | rx  | 1   | 0   | 2.2.2.1 | 40705578   | 2.2.2.2 | 40705578   | null | 1  | 1  | 64 | 64 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705579   | 2.2.2.2 | 40705579   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705580   | 2.2.2.2 | 40705580   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705581   | 2.2.2.2 | 40705581   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705582   | 2.2.2.2 | 40705582   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705583   | 2.2.2.2 | 40705583   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705584   | 2.2.2.3 | 40705584   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705585   | 2.2.2.3 | 40705585   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705586   | 2.2.2.3 | 40705586   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705587   | 2.2.2.3 | 40705587   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 40705588   | 2.2.2.3 | 40705588   | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 1   | 0   | 2.2.2.3 | 455454486  | 2.2.2.1 | 455454486  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 455454487  | 2.2.2.1 | 455454487  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 455454488  | 2.2.2.1 | 455454488  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 455454489  | 2.2.2.1 | 455454489  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 455454490  | 2.2.2.1 | 455454490  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 1017813087 | 2.2.2.1 | 1017813087 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 1017813088 | 2.2.2.1 | 1017813088 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 1017813089 | 2.2.2.1 | 1017813089 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 1017813090 | 2.2.2.1 | 1017813090 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 1017813091 | 2.2.2.1 | 1017813091 | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 558889665  | 4321::1 | 558889665  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 558889666  | 4321::1 | 558889666  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 558889667  | 4321::1 | 558889667  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 558889668  | 4321::1 | 558889668  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 558889669  | 4321::1 | 558889669  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | rx  | 58  | 0   | 4321::1 | 654129173  | 4321::2 | 654129173  | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129174  | 4321::2 | 654129174  | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129175  | 4321::2 | 654129175  | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129176  | 4321::2 | 654129176  | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129177  | 4321::2 | 654129177  | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129178  | 4321::3 | 654129178  | null | 1  | 0  | 64 | 0  | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129179  | 4321::3 | 654129179  | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129180  | 4321::3 | 654129180  | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129181  | 4321::3 | 654129181  | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129182  | 4321::3 | 654129182  | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129183  | 4321::3 | 654129183  | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129184  | 4321::3 | 654129184  | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129185  | 4321::3 | 654129185  | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129186  | 4321::3 | 654129186  | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 654129187  | 4321::3 | 654129187  | null | 1  | 1  | 64 | 64 | 00:00:01 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::2 | 683972202  | 4321::1 | 683972202  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 683972203  | 4321::1 | 683972203  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 683972204  | 4321::1 | 683972204  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 683972205  | 4321::1 | 683972205  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 683972206  | 4321::1 | 683972206  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     |_____|_____|_____|_________|____________|_________|____________|______|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.1 | 21 | 21 | 1344 | 1344 | 00:00:04 |
     | 2.2.2.2 | 11 | 11 | 704  | 704  | 00:00:04 |
     | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:03 |
     | 4321::1 | 25 | 24 | 1600 | 1536 | 00:00:03 |
     | 4321::2 | 10 | 10 | 640  | 640  | 00:00:03 |
     | 4321::3 | 15 | 14 | 960  | 896  | 00:00:03 |
     |_________|____|____|______|______|__________|
    r2#
    r2#
    ```

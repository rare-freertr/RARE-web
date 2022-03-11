# Example: mpls inspection with ingress drop
    
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
    logging file debug ../binTmp/zzz87r1-log.run
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
    logging file debug ../binTmp/zzz87r2-log.run
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
     mpls inspect mac drop-rx
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
    logging file debug ../binTmp/zzz87r3-log.run
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
     | tx  | 1   | 0   | 2.2.2.2 | 429144145 | 2.2.2.1 | 429144145 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 429144146 | 2.2.2.1 | 429144146 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 429144147 | 2.2.2.1 | 429144147 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 429144148 | 2.2.2.1 | 429144148 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.2 | 429144149 | 2.2.2.1 | 429144149 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 899564629 | 2.2.2.1 | 899564629 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 899564630 | 2.2.2.1 | 899564630 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 899564631 | 2.2.2.1 | 899564631 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 899564632 | 2.2.2.1 | 899564632 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 1   | 0   | 2.2.2.3 | 899564633 | 2.2.2.1 | 899564633 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 336550758 | 4321::1 | 336550758 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 336550759 | 4321::1 | 336550759 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 336550760 | 4321::1 | 336550760 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 336550761 | 4321::1 | 336550761 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::3 | 336550762 | 4321::1 | 336550762 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 516088847 | 4321::1 | 516088847 | 1  | 1  | 24 | 24 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 516088848 | 4321::1 | 516088848 | 1  | 1  | 24 | 24 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 516088849 | 4321::1 | 516088849 | 1  | 1  | 24 | 24 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 516088850 | 4321::1 | 516088850 | 1  | 1  | 24 | 24 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
     | tx  | 58  | 0   | 4321::2 | 516088851 | 4321::1 | 516088851 | 1  | 1  | 24 | 24 | 00:00:24 | 0000.0000.1111 | 0000.0000.2222 |
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
     | 2.2.2.1 | 10 | 10 | 440 | 440 | 00:00:24 |
     | 2.2.2.2 | 5  | 5  | 220 | 220 | 00:00:24 |
     | 2.2.2.3 | 5  | 5  | 220 | 220 | 00:00:00 |
     | 4321::1 | 10 | 10 | 240 | 240 | 00:00:24 |
     | 4321::2 | 5  | 5  | 120 | 120 | 00:00:24 |
     | 4321::3 | 5  | 5  | 120 | 120 | 00:00:00 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

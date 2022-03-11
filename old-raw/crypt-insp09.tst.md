# Example: mpls inspection with egress drop
    
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
    logging file debug ../binTmp/zzz58r1-log.run
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
    logging file debug ../binTmp/zzz58r2-log.run
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
     mpls inspect mac drop-tx
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
    logging file debug ../binTmp/zzz58r3-log.run
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
     | rx  | 1   | 0   | 2.2.2.1 | 392293453 | 2.2.2.2 | 392293453 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293454 | 2.2.2.2 | 392293454 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293455 | 2.2.2.2 | 392293455 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293456 | 2.2.2.2 | 392293456 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293457 | 2.2.2.2 | 392293457 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293458 | 2.2.2.2 | 392293458 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293459 | 2.2.2.3 | 392293459 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293460 | 2.2.2.3 | 392293460 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293461 | 2.2.2.3 | 392293461 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293462 | 2.2.2.3 | 392293462 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 392293463 | 2.2.2.3 | 392293463 | 1  | 1  | 44 | 44 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146189 | 4321::2 | 200146189 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146190 | 4321::2 | 200146190 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146191 | 4321::2 | 200146191 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146192 | 4321::2 | 200146192 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146193 | 4321::2 | 200146193 | 1  | 1  | 24 | 24 | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146194 | 4321::3 | 200146194 | 1  | 0  | 24 | 0  | 00:00:22 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146195 | 4321::3 | 200146195 | 1  | 1  | 24 | 24 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146196 | 4321::3 | 200146196 | 1  | 1  | 24 | 24 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146197 | 4321::3 | 200146197 | 1  | 1  | 24 | 24 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146198 | 4321::3 | 200146198 | 1  | 1  | 24 | 24 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146199 | 4321::3 | 200146199 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146200 | 4321::3 | 200146200 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146201 | 4321::3 | 200146201 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146202 | 4321::3 | 200146202 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 200146203 | 4321::3 | 200146203 | 1  | 1  | 24 | 24 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
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
     | 2.2.2.1 | 11 | 11 | 484 | 484 | 00:00:24 |
     | 2.2.2.2 | 6  | 6  | 264 | 264 | 00:00:24 |
     | 2.2.2.3 | 5  | 5  | 220 | 220 | 00:00:23 |
     | 4321::1 | 15 | 14 | 360 | 336 | 00:00:23 |
     | 4321::2 | 5  | 5  | 120 | 120 | 00:00:23 |
     | 4321::3 | 10 | 9  | 240 | 216 | 00:00:22 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

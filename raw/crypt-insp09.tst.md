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
    logging file debug ../binTmp/zzz77r1-log.run
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
    logging file debug ../binTmp/zzz77r2-log.run
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
    logging file debug ../binTmp/zzz77r3-log.run
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
     | rx  | 1   | 0   | 2.2.2.1 | 170560187 | 2.2.2.2 | 170560187 | null | 1  | 1  | 64 | 64 | 00:00:21 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560188 | 2.2.2.2 | 170560188 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560189 | 2.2.2.2 | 170560189 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560190 | 2.2.2.2 | 170560190 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560191 | 2.2.2.2 | 170560191 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560192 | 2.2.2.2 | 170560192 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560193 | 2.2.2.3 | 170560193 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560194 | 2.2.2.3 | 170560194 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560195 | 2.2.2.3 | 170560195 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560196 | 2.2.2.3 | 170560196 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 170560197 | 2.2.2.3 | 170560197 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602766 | 4321::2 | 901602766 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602767 | 4321::2 | 901602767 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602768 | 4321::2 | 901602768 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602769 | 4321::2 | 901602769 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602770 | 4321::2 | 901602770 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602771 | 4321::3 | 901602771 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602772 | 4321::3 | 901602772 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602773 | 4321::3 | 901602773 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602774 | 4321::3 | 901602774 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 901602775 | 4321::3 | 901602775 | null | 1  | 1  | 64 | 64 | 00:00:20 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.1 | 11 | 11 | 704 | 704 | 00:00:22 |
     | 2.2.2.2 | 6  | 6  | 384 | 384 | 00:00:22 |
     | 2.2.2.3 | 5  | 5  | 320 | 320 | 00:00:20 |
     | 4321::1 | 10 | 10 | 640 | 640 | 00:00:21 |
     | 4321::2 | 5  | 5  | 320 | 320 | 00:00:21 |
     | 4321::3 | 5  | 5  | 320 | 320 | 00:00:20 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

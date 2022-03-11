# Example: interface inspection with ingress drop
    
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
    logging file debug ../binTmp/zzz56r1-log.run
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
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 host-static 1234:1::2 0000.0000.2222
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
    logging file debug ../binTmp/zzz56r2-log.run
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
     ipv4 inspect mac drop-rx
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect mac drop-rx
     ipv6 host-static 1234:1::1 0000.0000.1111
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
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
    logging file debug ../binTmp/zzz56r3-log.run
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
     ipv6 address 1234:2::3 ffff:ffff::
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
    r2#show ipv4 insp eth1
    r2#show ipv4 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|----------------|----------------|
     | tx  | 1   | 0   | 2.2.2.2 | 209205309 | 2.2.2.1 | 209205309 | null | 0  | 1  | 0  | 64 | 00:00:25 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205310 | 2.2.2.1 | 209205310 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205311 | 2.2.2.1 | 209205311 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205312 | 2.2.2.1 | 209205312 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205313 | 2.2.2.1 | 209205313 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205314 | 2.2.2.1 | 209205314 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205315 | 2.2.2.1 | 209205315 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205316 | 2.2.2.1 | 209205316 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205317 | 2.2.2.1 | 209205317 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 209205318 | 2.2.2.1 | 209205318 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.3 | 771721745 | 2.2.2.1 | 771721745 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 771721746 | 2.2.2.1 | 771721746 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 771721747 | 2.2.2.1 | 771721747 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 771721748 | 2.2.2.1 | 771721748 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 771721749 | 2.2.2.1 | 771721749 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|----------------|----------------|
     | tx  | 58  | 0   | 4321::2 | 208371861 | 4321::1 | 208371861 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 208371862 | 4321::1 | 208371862 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 208371863 | 4321::1 | 208371863 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 208371864 | 4321::1 | 208371864 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 208371865 | 4321::1 | 208371865 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::3 | 358854584 | 4321::1 | 358854584 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 358854585 | 4321::1 | 358854585 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 358854586 | 4321::1 | 358854586 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 358854587 | 4321::1 | 358854587 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 358854588 | 4321::1 | 358854588 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 top eth1
    r2#show ipv4 top eth1
     |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
     |         | packet  | byte      |          |
     | addr    | rx | tx | rx  | tx  | time     |
     |---------|----|----|-----|-----|----------|
     | 2.2.2.1 | 14 | 15 | 896 | 960 | 00:00:25 |
     | 2.2.2.2 | 9  | 10 | 576 | 640 | 00:00:25 |
     | 2.2.2.3 | 5  | 5  | 320 | 320 | 00:00:01 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 top eth1
    r2#show ipv6 top eth1
     |~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
     |         | packet  | byte      |          |
     | addr    | rx | tx | rx  | tx  | time     |
     |---------|----|----|-----|-----|----------|
     | 4321::1 | 10 | 10 | 640 | 640 | 00:00:23 |
     | 4321::2 | 5  | 5  | 320 | 320 | 00:00:23 |
     | 4321::3 | 5  | 5  | 320 | 320 | 00:00:01 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

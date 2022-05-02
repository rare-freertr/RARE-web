# Example: interface inspection with member ingress drop
    
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
    logging file debug ../binTmp/zzz19r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    logging file debug ../binTmp/zzz19r2-log.run
    !
    session ins4
     drop-rx
     exit
    !
    session ins6
     drop-rx
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 inspect member ins4
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect member ins6
     ipv6 host-static 1234:1::1 0000.0000.1111
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
    logging file debug ../binTmp/zzz19r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|
     | tx  | 1   | 0   | 2.2.2.2 | 201441569 | 2.2.2.1 | 201441569 | null | 0  | 1  | 0  | 64 | 00:00:25 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441570 | 2.2.2.1 | 201441570 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441571 | 2.2.2.1 | 201441571 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441572 | 2.2.2.1 | 201441572 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441573 | 2.2.2.1 | 201441573 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441574 | 2.2.2.1 | 201441574 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441575 | 2.2.2.1 | 201441575 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441576 | 2.2.2.1 | 201441576 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441577 | 2.2.2.1 | 201441577 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 201441578 | 2.2.2.1 | 201441578 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.3 | 948556782 | 2.2.2.1 | 948556782 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 948556783 | 2.2.2.1 | 948556783 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 948556784 | 2.2.2.1 | 948556784 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 948556785 | 2.2.2.1 | 948556785 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 948556786 | 2.2.2.1 | 948556786 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|
     | tx  | 58  | 0   | 4321::3 | 356798497 | 4321::1 | 356798497 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 356798498 | 4321::1 | 356798498 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 356798499 | 4321::1 | 356798499 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 356798500 | 4321::1 | 356798500 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 356798501 | 4321::1 | 356798501 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::2 | 868666089 | 4321::1 | 868666089 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 868666090 | 4321::1 | 868666090 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 868666091 | 4321::1 | 868666091 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 868666092 | 4321::1 | 868666092 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 868666093 | 4321::1 | 868666093 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|
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
     | 2.2.2.3 | 5  | 5  | 320 | 320 | 00:00:00 |
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
     | 4321::3 | 5  | 5  | 320 | 320 | 00:00:00 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

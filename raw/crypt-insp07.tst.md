# Example: interface inspection with egress drop
    
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
    logging file debug ../binTmp/zzz15r1-log.run
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
    logging file debug ../binTmp/zzz15r2-log.run
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
     ipv4 inspect mac drop-tx
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect mac drop-tx
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
    logging file debug ../binTmp/zzz15r3-log.run
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
     | rx  | 1   | 0   | 2.2.2.1 | 808053980 | 2.2.2.2 | 808053980 | null | 1  | 1  | 64 | 64 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053981 | 2.2.2.2 | 808053981 | null | 1  | 1  | 64 | 64 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053982 | 2.2.2.2 | 808053982 | null | 1  | 1  | 64 | 64 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053983 | 2.2.2.2 | 808053983 | null | 1  | 1  | 64 | 64 | 00:00:04 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053984 | 2.2.2.2 | 808053984 | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053985 | 2.2.2.2 | 808053985 | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053986 | 2.2.2.2 | 808053986 | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053987 | 2.2.2.2 | 808053987 | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053988 | 2.2.2.2 | 808053988 | null | 1  | 1  | 64 | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053989 | 2.2.2.3 | 808053989 | null | 1  | 0  | 64 | 0  | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053990 | 2.2.2.3 | 808053990 | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053991 | 2.2.2.3 | 808053991 | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053992 | 2.2.2.3 | 808053992 | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053993 | 2.2.2.3 | 808053993 | null | 1  | 1  | 64 | 64 | 00:00:02 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053994 | 2.2.2.3 | 808053994 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053995 | 2.2.2.3 | 808053995 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053996 | 2.2.2.3 | 808053996 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053997 | 2.2.2.3 | 808053997 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 808053998 | 2.2.2.3 | 808053998 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source                               | target                |      | packet  | byte     |          | mac                             |
     | dir | prt | tos | addr                   | port        | addr    | port        | url  | rx | tx | rx  | tx | time     | src            | trg            |
     |-----|-----|-----|------------------------|-------------|---------|-------------|------|----|----|-----|----|----------|----------------|----------------|
     | rx  | 58  | 0   | 1234:1::1              | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:06 | 3333.0000.0001 | 0000.0000.1111 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:06 | 3333.0000.0001 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392670   | 4321::2 | 240392670   | null | 1  | 1  | 64  | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392671   | 4321::2 | 240392671   | null | 1  | 1  | 64  | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392672   | 4321::2 | 240392672   | null | 1  | 1  | 64  | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392673   | 4321::2 | 240392673   | null | 1  | 1  | 64  | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392674   | 4321::2 | 240392674   | null | 1  | 1  | 64  | 64 | 00:00:03 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392675   | 4321::3 | 240392675   | null | 1  | 1  | 64  | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392676   | 4321::3 | 240392676   | null | 1  | 1  | 64  | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392677   | 4321::3 | 240392677   | null | 1  | 1  | 64  | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392678   | 4321::3 | 240392678   | null | 1  | 1  | 64  | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1                | 240392679   | 4321::3 | 240392679   | null | 1  | 1  | 64  | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | 1073743624  | ff02::1 | 1073743624  | null | 1  | 0  | 104 | 0  | 00:00:06 | 3333.0000.0001 | 0000.0000.1111 |
     |_____|_____|_____|________________________|_____________|_________|_____________|______|____|____|_____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 top eth1
    r2#show ipv4 top eth1
     |~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|
     |         | packet  | byte        |          |
     | addr    | rx | tx | rx   | tx   | time     |
     |---------|----|----|------|------|----------|
     | 2.2.2.1 | 19 | 18 | 1216 | 1152 | 00:00:04 |
     | 2.2.2.2 | 9  | 9  | 576  | 576  | 00:00:04 |
     | 2.2.2.3 | 10 | 9  | 640  | 576  | 00:00:03 |
     |_________|____|____|______|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 top eth1
    r2#show ipv6 top eth1
     |~~~~~~~~~~~~~~~~~~~~~~~~|~~~~|~~~~|~~~~~|~~~~~|~~~~~~~~~~|
     |                        | packet  | byte      |          |
     | addr                   | rx | tx | rx  | tx  | time     |
     |------------------------|----|----|-----|-----|----------|
     | 1234:1::1              | 1  | 0  | 72  | 0   | 00:00:06 |
     | 4321::1                | 10 | 10 | 640 | 640 | 00:00:03 |
     | 4321::2                | 5  | 5  | 320 | 320 | 00:00:03 |
     | 4321::3                | 5  | 5  | 320 | 320 | 00:00:01 |
     | fe80::200:ff:fe00:1111 | 2  | 0  | 176 | 0   | 00:00:06 |
     | ff02::1                | 3  | 0  | 248 | 0   | 00:00:06 |
     |________________________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

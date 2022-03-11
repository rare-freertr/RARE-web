# Example: interface inspection with member egress drop
    
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
    logging file debug ../binTmp/zzz17r1-log.run
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
    logging file debug ../binTmp/zzz17r2-log.run
    !
    session ins4
     drop-tx
     exit
    !
    session ins6
     drop-tx
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
     ipv4 inspect member ins4
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect member ins6
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
    logging file debug ../binTmp/zzz17r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|
     |                 | source             | target             |      | packet  | byte    |          |
     | dir | prt | tos | addr    | port     | addr    | port     | url  | rx | tx | rx | tx | time     |
     |-----|-----|-----|---------|----------|---------|----------|------|----|----|----|----|----------|
     | rx  | 1   | 0   | 2.2.2.1 | 71142353 | 2.2.2.2 | 71142353 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142354 | 2.2.2.2 | 71142354 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142355 | 2.2.2.2 | 71142355 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142356 | 2.2.2.2 | 71142356 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142357 | 2.2.2.2 | 71142357 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142358 | 2.2.2.2 | 71142358 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142359 | 2.2.2.2 | 71142359 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142360 | 2.2.2.2 | 71142360 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142361 | 2.2.2.2 | 71142361 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142362 | 2.2.2.3 | 71142362 | null | 1  | 0  | 64 | 0  | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142363 | 2.2.2.3 | 71142363 | null | 1  | 1  | 64 | 64 | 00:00:02 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142364 | 2.2.2.3 | 71142364 | null | 1  | 1  | 64 | 64 | 00:00:02 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142365 | 2.2.2.3 | 71142365 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142366 | 2.2.2.3 | 71142366 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142367 | 2.2.2.3 | 71142367 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142368 | 2.2.2.3 | 71142368 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142369 | 2.2.2.3 | 71142369 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142370 | 2.2.2.3 | 71142370 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 71142371 | 2.2.2.3 | 71142371 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     |_____|_____|_____|_________|__________|_________|__________|______|____|____|____|____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~~|~~~~|~~~~~~~~~~|
     |                 | source                               | target                |      | packet  | byte     |          |
     | dir | prt | tos | addr                   | port        | addr    | port        | url  | rx | tx | rx  | tx | time     |
     |-----|-----|-----|------------------------|-------------|---------|-------------|------|----|----|-----|----|----------|
     | rx  | 58  | 0   | 1234:1::1              | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:06 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:06 |
     | rx  | 58  | 0   | 4321::1                | 806665372   | 4321::2 | 806665372   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 806665373   | 4321::2 | 806665373   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 806665374   | 4321::2 | 806665374   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 806665375   | 4321::2 | 806665375   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 806665376   | 4321::2 | 806665376   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 806665377   | 4321::3 | 806665377   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 806665378   | 4321::3 | 806665378   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 806665379   | 4321::3 | 806665379   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 806665380   | 4321::3 | 806665380   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 806665381   | 4321::3 | 806665381   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | 1073743624  | ff02::1 | 1073743624  | null | 1  | 0  | 104 | 0  | 00:00:06 |
     |_____|_____|_____|________________________|_____________|_________|_____________|______|____|____|_____|____|__________|
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
     | 1234:1::1              | 1  | 0  | 72  | 0   | 00:00:07 |
     | 4321::1                | 10 | 10 | 640 | 640 | 00:00:03 |
     | 4321::2                | 5  | 5  | 320 | 320 | 00:00:03 |
     | 4321::3                | 5  | 5  | 320 | 320 | 00:00:01 |
     | fe80::200:ff:fe00:1111 | 2  | 0  | 176 | 0   | 00:00:07 |
     | ff02::1                | 3  | 0  | 248 | 0   | 00:00:07 |
     |________________________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

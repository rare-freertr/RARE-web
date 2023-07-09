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
    logging file debug ../binTmp/zzz44r1-log.run
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
    logging file debug ../binTmp/zzz44r2-log.run
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
    logging file debug ../binTmp/zzz44r3-log.run
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
     | rx  | 1   | 0   | 2.2.2.1 | 278653213 | 2.2.2.2 | 278653213 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653214 | 2.2.2.2 | 278653214 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653215 | 2.2.2.2 | 278653215 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653216 | 2.2.2.2 | 278653216 | null | 1  | 1  | 64 | 64 | 00:00:04 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653217 | 2.2.2.2 | 278653217 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653218 | 2.2.2.2 | 278653218 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653219 | 2.2.2.2 | 278653219 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653220 | 2.2.2.2 | 278653220 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653221 | 2.2.2.2 | 278653221 | null | 1  | 1  | 64 | 64 | 00:00:03 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653222 | 2.2.2.3 | 278653222 | null | 1  | 0  | 64 | 0  | 00:00:02 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653223 | 2.2.2.3 | 278653223 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653224 | 2.2.2.3 | 278653224 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653225 | 2.2.2.3 | 278653225 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653226 | 2.2.2.3 | 278653226 | null | 1  | 1  | 64 | 64 | 00:00:01 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653227 | 2.2.2.3 | 278653227 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653228 | 2.2.2.3 | 278653228 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653229 | 2.2.2.3 | 278653229 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653230 | 2.2.2.3 | 278653230 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | rx  | 1   | 0   | 2.2.2.1 | 278653231 | 2.2.2.3 | 278653231 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|
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
     | rx  | 58  | 0   | 1234:1::1              | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:05 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | -2147483648 | ff02::1 | -2147483648 | null | 1  | 0  | 72  | 0  | 00:00:05 |
     | rx  | 58  | 0   | 4321::1                | 861186317   | 4321::2 | 861186317   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 861186318   | 4321::2 | 861186318   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 861186319   | 4321::2 | 861186319   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 861186320   | 4321::2 | 861186320   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 861186321   | 4321::2 | 861186321   | null | 1  | 1  | 64  | 64 | 00:00:03 |
     | rx  | 58  | 0   | 4321::1                | 861186322   | 4321::3 | 861186322   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 861186323   | 4321::3 | 861186323   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 861186324   | 4321::3 | 861186324   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 861186325   | 4321::3 | 861186325   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | 4321::1                | 861186326   | 4321::3 | 861186326   | null | 1  | 1  | 64  | 64 | 00:00:00 |
     | rx  | 58  | 0   | fe80::200:ff:fe00:1111 | 1073743624  | ff02::1 | 1073743624  | null | 1  | 0  | 104 | 0  | 00:00:05 |
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
     | 1234:1::1              | 1  | 0  | 72  | 0   | 00:00:05 |
     | 4321::1                | 10 | 10 | 640 | 640 | 00:00:03 |
     | 4321::2                | 5  | 5  | 320 | 320 | 00:00:03 |
     | 4321::3                | 5  | 5  | 320 | 320 | 00:00:01 |
     | fe80::200:ff:fe00:1111 | 2  | 0  | 176 | 0   | 00:00:05 |
     | ff02::1                | 3  | 0  | 248 | 0   | 00:00:05 |
     |________________________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

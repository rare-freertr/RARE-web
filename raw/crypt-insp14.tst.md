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
    logging file debug ../binTmp/zzz47r1-log.run
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
    logging file debug ../binTmp/zzz47r2-log.run
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
    logging file debug ../binTmp/zzz47r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|
     |                 | source              | target              |      | packet  | byte    |          |
     | dir | prt | tos | addr    | port      | addr    | port      | url  | rx | tx | rx | tx | time     |
     |-----|-----|-----|---------|-----------|---------|-----------|------|----|----|----|----|----------|
     | tx  | 1   | 0   | 2.2.2.3 | 112155159 | 2.2.2.1 | 112155159 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 112155160 | 2.2.2.1 | 112155160 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 112155161 | 2.2.2.1 | 112155161 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 112155162 | 2.2.2.1 | 112155162 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.3 | 112155163 | 2.2.2.1 | 112155163 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064434 | 2.2.2.1 | 800064434 | null | 0  | 1  | 0  | 64 | 00:00:25 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064435 | 2.2.2.1 | 800064435 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064436 | 2.2.2.1 | 800064436 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064437 | 2.2.2.1 | 800064437 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064438 | 2.2.2.1 | 800064438 | null | 1  | 1  | 64 | 64 | 00:00:24 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064439 | 2.2.2.1 | 800064439 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064440 | 2.2.2.1 | 800064440 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064441 | 2.2.2.1 | 800064441 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064442 | 2.2.2.1 | 800064442 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 1   | 0   | 2.2.2.2 | 800064443 | 2.2.2.1 | 800064443 | null | 1  | 1  | 64 | 64 | 00:00:23 |
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
     | tx  | 58  | 0   | 4321::3 | 205588949 | 4321::1 | 205588949 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 205588950 | 4321::1 | 205588950 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 205588951 | 4321::1 | 205588951 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 205588952 | 4321::1 | 205588952 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::3 | 205588953 | 4321::1 | 205588953 | null | 1  | 1  | 64 | 64 | 00:00:00 |
     | tx  | 58  | 0   | 4321::2 | 480114920 | 4321::1 | 480114920 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 480114921 | 4321::1 | 480114921 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 480114922 | 4321::1 | 480114922 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 480114923 | 4321::1 | 480114923 | null | 1  | 1  | 64 | 64 | 00:00:23 |
     | tx  | 58  | 0   | 4321::2 | 480114924 | 4321::1 | 480114924 | null | 1  | 1  | 64 | 64 | 00:00:23 |
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

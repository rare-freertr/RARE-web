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
    logging file debug ../binTmp/zzz43r1-log.run
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
    logging file debug ../binTmp/zzz43r2-log.run
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
     ipv4 inspect mac drop-rx
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect mac drop-rx
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
    logging file debug ../binTmp/zzz43r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source               | target               |      | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port       | addr    | port       | url  | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|------------|---------|------------|------|----|----|----|----|----------|----------------|----------------|
     | tx  | 1   | 0   | 2.2.2.3 | 459602362  | 2.2.2.1 | 459602362  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 459602363  | 2.2.2.1 | 459602363  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 459602364  | 2.2.2.1 | 459602364  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 459602365  | 2.2.2.1 | 459602365  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 459602366  | 2.2.2.1 | 459602366  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920992 | 2.2.2.1 | 1044920992 | null | 0  | 1  | 0  | 64 | 00:00:25 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920993 | 2.2.2.1 | 1044920993 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920994 | 2.2.2.1 | 1044920994 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920995 | 2.2.2.1 | 1044920995 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920996 | 2.2.2.1 | 1044920996 | null | 1  | 1  | 64 | 64 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920997 | 2.2.2.1 | 1044920997 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920998 | 2.2.2.1 | 1044920998 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044920999 | 2.2.2.1 | 1044920999 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044921000 | 2.2.2.1 | 1044921000 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 1044921001 | 2.2.2.1 | 1044921001 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     |_____|_____|_____|_________|____________|_________|____________|______|____|____|____|____|__________|________________|________________|
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
     | tx  | 58  | 0   | 4321::2 | 800732713 | 4321::1 | 800732713 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 800732714 | 4321::1 | 800732714 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 800732715 | 4321::1 | 800732715 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 800732716 | 4321::1 | 800732716 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 800732717 | 4321::1 | 800732717 | null | 1  | 1  | 64 | 64 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::3 | 889938616 | 4321::1 | 889938616 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 889938617 | 4321::1 | 889938617 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 889938618 | 4321::1 | 889938618 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 889938619 | 4321::1 | 889938619 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 889938620 | 4321::1 | 889938620 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
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

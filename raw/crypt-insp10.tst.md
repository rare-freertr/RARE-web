# Example: interface inspection with selective ingress drop
    
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
    logging file debug ../binTmp/zzz60r1-log.run
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
    logging file debug ../binTmp/zzz60r2-log.run
    !
    access-list test4
     sequence 10 permit all any all 2.2.2.3 255.255.255.255 all
     exit
    !
    access-list test6
     sequence 10 permit all any all 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff all
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
     ipv4 inspect mac drop-rx allow-list test4
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 inspect mac drop-rx allow-list test6
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
    logging file debug ../binTmp/zzz60r3-log.run
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
     | tx  | 1   | 0   | 2.2.2.2 | 430088559 | 2.2.2.1 | 430088559 | null | 0  | 1  | 0  | 64 | 00:00:15 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088560 | 2.2.2.1 | 430088560 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088561 | 2.2.2.1 | 430088561 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088562 | 2.2.2.1 | 430088562 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088563 | 2.2.2.1 | 430088563 | null | 1  | 1  | 64 | 64 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088564 | 2.2.2.1 | 430088564 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088565 | 2.2.2.1 | 430088565 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088566 | 2.2.2.1 | 430088566 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088567 | 2.2.2.1 | 430088567 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 430088568 | 2.2.2.1 | 430088568 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.3 | 741171646 | 2.2.2.1 | 741171646 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 741171647 | 2.2.2.1 | 741171647 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 741171648 | 2.2.2.1 | 741171648 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 741171649 | 2.2.2.1 | 741171649 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 741171650 | 2.2.2.1 | 741171650 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | rx  | 1   | 0   | 2.2.2.1 | 888427603 | 2.2.2.3 | 888427603 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 888427604 | 2.2.2.3 | 888427604 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 888427605 | 2.2.2.3 | 888427605 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 888427606 | 2.2.2.3 | 888427606 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 888427607 | 2.2.2.3 | 888427607 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
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
     | tx  | 58  | 0   | 4321::3 | 20628470  | 4321::1 | 20628470  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 20628471  | 4321::1 | 20628471  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 20628472  | 4321::1 | 20628472  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 20628473  | 4321::1 | 20628473  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 20628474  | 4321::1 | 20628474  | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::2 | 687907641 | 4321::1 | 687907641 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 687907642 | 4321::1 | 687907642 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 687907643 | 4321::1 | 687907643 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 687907644 | 4321::1 | 687907644 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 687907645 | 4321::1 | 687907645 | null | 1  | 1  | 64 | 64 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | rx  | 58  | 0   | 4321::1 | 997947369 | 4321::3 | 997947369 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 997947370 | 4321::3 | 997947370 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 997947371 | 4321::3 | 997947371 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 997947372 | 4321::3 | 997947372 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 997947373 | 4321::3 | 997947373 | null | 1  | 1  | 64 | 64 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|___________|_________|___________|______|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.1 | 19 | 20 | 1216 | 1280 | 00:00:15 |
     | 2.2.2.2 | 9  | 10 | 576  | 640  | 00:00:15 |
     | 2.2.2.3 | 10 | 10 | 640  | 640  | 00:00:00 |
     |_________|____|____|______|______|__________|
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
     | 4321::1 | 15 | 15 | 960 | 960 | 00:00:13 |
     | 4321::2 | 5  | 5  | 320 | 320 | 00:00:13 |
     | 4321::3 | 10 | 10 | 640 | 640 | 00:00:01 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

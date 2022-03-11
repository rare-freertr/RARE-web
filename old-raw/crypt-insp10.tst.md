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
    logging file debug ../binTmp/zzz23r1-log.run
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
    logging file debug ../binTmp/zzz23r2-log.run
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
    logging file debug ../binTmp/zzz23r3-log.run
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
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
     | rx  | 1   | 0   | 2.2.2.1 | 374036449 | 2.2.2.3 | 374036449 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 374036450 | 2.2.2.3 | 374036450 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 374036451 | 2.2.2.3 | 374036451 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 374036452 | 2.2.2.3 | 374036452 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 374036453 | 2.2.2.3 | 374036453 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 1   | 0   | 2.2.2.3 | 417653275 | 2.2.2.1 | 417653275 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 417653276 | 2.2.2.1 | 417653276 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 417653277 | 2.2.2.1 | 417653277 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 417653278 | 2.2.2.1 | 417653278 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 417653279 | 2.2.2.1 | 417653279 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038200 | 2.2.2.1 | 757038200 | 0  | 1  | 0  | 44 | 00:00:15 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038201 | 2.2.2.1 | 757038201 | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038202 | 2.2.2.1 | 757038202 | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038203 | 2.2.2.1 | 757038203 | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038204 | 2.2.2.1 | 757038204 | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038205 | 2.2.2.1 | 757038205 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038206 | 2.2.2.1 | 757038206 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038207 | 2.2.2.1 | 757038207 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038208 | 2.2.2.1 | 757038208 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 757038209 | 2.2.2.1 | 757038209 | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source              | target              | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port      | addr    | port      | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|-----------|---------|-----------|----|----|----|----|----------|----------------|----------------|
     | rx  | 58  | 0   | 4321::1 | 151036361 | 4321::3 | 151036361 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 151036362 | 4321::3 | 151036362 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 151036363 | 4321::3 | 151036363 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 151036364 | 4321::3 | 151036364 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 151036365 | 4321::3 | 151036365 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::2 | 563735532 | 4321::1 | 563735532 | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 563735533 | 4321::1 | 563735533 | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 563735534 | 4321::1 | 563735534 | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 563735535 | 4321::1 | 563735535 | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 563735536 | 4321::1 | 563735536 | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::3 | 597931739 | 4321::1 | 597931739 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 597931740 | 4321::1 | 597931740 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 597931741 | 4321::1 | 597931741 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 597931742 | 4321::1 | 597931742 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 597931743 | 4321::1 | 597931743 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.1 | 19 | 20 | 836 | 880 | 00:00:15 |
     | 2.2.2.2 | 9  | 10 | 396 | 440 | 00:00:15 |
     | 2.2.2.3 | 10 | 10 | 440 | 440 | 00:00:01 |
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
     | 4321::1 | 15 | 15 | 360 | 360 | 00:00:14 |
     | 4321::2 | 5  | 5  | 120 | 120 | 00:00:14 |
     | 4321::3 | 10 | 10 | 240 | 240 | 00:00:01 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

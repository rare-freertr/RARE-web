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
    logging file debug ../binTmp/zzz1r1-log.run
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
    logging file debug ../binTmp/zzz1r2-log.run
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
    logging file debug ../binTmp/zzz1r3-log.run
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
     | tx  | 1   | 0   | 2.2.2.2 | 95466773  | 2.2.2.1 | 95466773  | 0  | 1  | 0  | 44 | 00:00:15 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466774  | 2.2.2.1 | 95466774  | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466775  | 2.2.2.1 | 95466775  | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466776  | 2.2.2.1 | 95466776  | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466777  | 2.2.2.1 | 95466777  | 1  | 1  | 44 | 44 | 00:00:14 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466778  | 2.2.2.1 | 95466778  | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466779  | 2.2.2.1 | 95466779  | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466780  | 2.2.2.1 | 95466780  | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466781  | 2.2.2.1 | 95466781  | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 95466782  | 2.2.2.1 | 95466782  | 1  | 1  | 44 | 44 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.3 | 930341996 | 2.2.2.1 | 930341996 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 930341997 | 2.2.2.1 | 930341997 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 930341998 | 2.2.2.1 | 930341998 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 930341999 | 2.2.2.1 | 930341999 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 930342000 | 2.2.2.1 | 930342000 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | rx  | 1   | 0   | 2.2.2.1 | 984728902 | 2.2.2.3 | 984728902 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 984728903 | 2.2.2.3 | 984728903 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 984728904 | 2.2.2.3 | 984728904 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 984728905 | 2.2.2.3 | 984728905 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 1   | 0   | 2.2.2.1 | 984728906 | 2.2.2.3 | 984728906 | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     |_____|_____|_____|_________|___________|_________|___________|____|____|____|____|__________|________________|________________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 insp eth1
    r2#show ipv6 insp eth1
     |~~~~~|~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~|~~~~|~~~~|~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~|
     |                 | source               | target               | packet  | byte    |          | mac                             |
     | dir | prt | tos | addr    | port       | addr    | port       | rx | tx | rx | tx | time     | src            | trg            |
     |-----|-----|-----|---------|------------|---------|------------|----|----|----|----|----------|----------------|----------------|
     | tx  | 58  | 0   | 4321::2 | 554562877  | 4321::1 | 554562877  | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 554562878  | 4321::1 | 554562878  | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 554562879  | 4321::1 | 554562879  | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 554562880  | 4321::1 | 554562880  | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 554562881  | 4321::1 | 554562881  | 1  | 1  | 24 | 24 | 00:00:13 | 0000.0000.0000 | 0000.0000.0000 |
     | rx  | 58  | 0   | 4321::1 | 712359856  | 4321::3 | 712359856  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 712359857  | 4321::3 | 712359857  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 712359858  | 4321::3 | 712359858  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 712359859  | 4321::3 | 712359859  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | rx  | 58  | 0   | 4321::1 | 712359860  | 4321::3 | 712359860  | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.1111 |
     | tx  | 58  | 0   | 4321::3 | 1047210759 | 4321::1 | 1047210759 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 1047210760 | 4321::1 | 1047210760 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 1047210761 | 4321::1 | 1047210761 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 1047210762 | 4321::1 | 1047210762 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 1047210763 | 4321::1 | 1047210763 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     |_____|_____|_____|_________|____________|_________|____________|____|____|____|____|__________|________________|________________|
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
     | 2.2.2.3 | 10 | 10 | 440 | 440 | 00:00:00 |
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
     | 4321::1 | 15 | 15 | 360 | 360 | 00:00:13 |
     | 4321::2 | 5  | 5  | 120 | 120 | 00:00:13 |
     | 4321::3 | 10 | 10 | 240 | 240 | 00:00:00 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

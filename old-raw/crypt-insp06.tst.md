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
    logging file debug ../binTmp/zzz83r1-log.run
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
    logging file debug ../binTmp/zzz83r2-log.run
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
    logging file debug ../binTmp/zzz83r3-log.run
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
     | tx  | 1   | 0   | 2.2.2.3 | 70544974  | 2.2.2.1 | 70544974  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 70544975  | 2.2.2.1 | 70544975  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 70544976  | 2.2.2.1 | 70544976  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 70544977  | 2.2.2.1 | 70544977  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.3 | 70544978  | 2.2.2.1 | 70544978  | 1  | 1  | 44 | 44 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424907 | 2.2.2.1 | 947424907 | 0  | 1  | 0  | 44 | 00:00:25 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424908 | 2.2.2.1 | 947424908 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424909 | 2.2.2.1 | 947424909 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424910 | 2.2.2.1 | 947424910 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424911 | 2.2.2.1 | 947424911 | 1  | 1  | 44 | 44 | 00:00:24 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424912 | 2.2.2.1 | 947424912 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424913 | 2.2.2.1 | 947424913 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424914 | 2.2.2.1 | 947424914 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424915 | 2.2.2.1 | 947424915 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 1   | 0   | 2.2.2.2 | 947424916 | 2.2.2.1 | 947424916 | 1  | 1  | 44 | 44 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
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
     | tx  | 58  | 0   | 4321::3 | 279206053 | 4321::1 | 279206053 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 279206054 | 4321::1 | 279206054 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 279206055 | 4321::1 | 279206055 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 279206056 | 4321::1 | 279206056 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::3 | 279206057 | 4321::1 | 279206057 | 1  | 1  | 24 | 24 | 00:00:00 | 0000.0000.2222 | 0000.0000.3333 |
     | tx  | 58  | 0   | 4321::2 | 524892622 | 4321::1 | 524892622 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 524892623 | 4321::1 | 524892623 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 524892624 | 4321::1 | 524892624 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 524892625 | 4321::1 | 524892625 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
     | tx  | 58  | 0   | 4321::2 | 524892626 | 4321::1 | 524892626 | 1  | 1  | 24 | 24 | 00:00:23 | 0000.0000.0000 | 0000.0000.0000 |
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
     | 2.2.2.1 | 14 | 15 | 616 | 660 | 00:00:25 |
     | 2.2.2.2 | 9  | 10 | 396 | 440 | 00:00:25 |
     | 2.2.2.3 | 5  | 5  | 220 | 220 | 00:00:00 |
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
     | 4321::1 | 10 | 10 | 240 | 240 | 00:00:23 |
     | 4321::2 | 5  | 5  | 120 | 120 | 00:00:23 |
     | 4321::3 | 5  | 5  | 120 | 120 | 00:00:00 |
     |_________|____|____|_____|_____|__________|
    r2#
    r2#
    ```

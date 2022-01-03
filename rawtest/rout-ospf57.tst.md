# Example: ospf dynamic twamp cost
    
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
    router ospf4 1
     vrf v1
     router-id 4.4.4.1
     traffeng-id 0.0.0.0
     area 0 enable
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.1
     traffeng-id ::
     area 0 enable
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv6 address 1234::1 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 cost 100
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 cost 100
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1235::1 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 cost 1
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 cost 1
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
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    server twamp t
     vrf v1
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
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router ospf4 1
     vrf v1
     router-id 4.4.4.2
     traffeng-id 0.0.0.0
     area 0 enable
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.2
     traffeng-id ::
     area 0 enable
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv6 address 1234::2 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 cost 2
     router ospf4 1 dynamic-metric twamp
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 cost 2
     router ospf6 1 dynamic-metric twamp
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1235::2 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 cost 200
     router ospf4 1 dynamic-metric twamp
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 cost 200
     router ospf6 1 dynamic-metric twamp
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
    r2#show ipv4 ospf 1 nei
    r2#show ipv4 ospf 1 nei
     |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | area | address | routerid | state | uptime   |
     |-----------|------|---------|----------|-------|----------|
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:03 |
     | ethernet2 | 0    | 1.1.2.1 | 4.4.4.1  | full  | 00:00:03 |
     |___________|______|_________|__________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 nei
    r2#show ipv6 ospf 1 nei
     |~~~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | area | address | routerid | state | uptime   |
     |-----------|------|---------|----------|-------|----------|
     | ethernet1 | 0    | 1234::1 | 6.6.6.1  | full  | 00:00:03 |
     | ethernet2 | 0    | 1235::1 | 6.6.6.1  | full  | 00:00:03 |
     |___________|______|_________|__________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 ospf 1 dat 0
    r2#show ipv4 ospf 1 dat 0
     |~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | routerid | lsaid   | sequence | type        | len | time     |
     |----------|---------|----------|-------------|-----|----------|
     | 4.4.4.1  | 4.4.4.1 | 80000008 | router      | 52  | 00:00:03 |
     | 4.4.4.2  | 4.4.4.2 | 8000000a | router      | 52  | 00:00:03 |
     | 4.4.4.1  | 0.0.0.0 | 80000006 | asExternal  | 16  | 01:00:03 |
     | 4.4.4.2  | 0.0.0.0 | 80000006 | asExternal  | 16  | 01:00:04 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:04 |
     | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:04 |
     | 4.4.4.1  | 1.1.2.0 | 80000001 | asExternal  | 16  | 00:00:03 |
     | 4.4.4.2  | 1.1.2.0 | 80000001 | asExternal  | 16  | 00:00:04 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:04 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:04 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:04 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:05 |
     |__________|_________|__________|_____________|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 dat 0
    r2#show ipv6 ospf 1 dat 0
     |~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | routerid | lsaid     | sequence | type       | len | time     |
     |----------|-----------|----------|------------|-----|----------|
     | 6.6.6.1  | 421475686 | 80000001 | link       | 24  | 00:00:04 |
     | 6.6.6.1  | 421475687 | 80000001 | link       | 24  | 00:00:04 |
     | 6.6.6.2  | 925927523 | 80000001 | link       | 24  | 00:00:04 |
     | 6.6.6.2  | 925927524 | 80000001 | link       | 24  | 00:00:04 |
     | 6.6.6.1  | 0         | 80000004 | router     | 36  | 00:00:01 |
     | 6.6.6.2  | 0         | 80000005 | router     | 36  | 00:00:01 |
     | 6.6.6.1  | 421475686 | 80000002 | prefix     | 20  | 00:00:04 |
     | 6.6.6.1  | 421475687 | 80000002 | prefix     | 20  | 00:00:04 |
     | 6.6.6.2  | 925927523 | 80000002 | prefix     | 20  | 00:00:04 |
     | 6.6.6.2  | 925927524 | 80000002 | prefix     | 20  | 00:00:04 |
     | 6.6.6.1  | 0         | 80000006 | asExternal | 16  | 00:00:04 |
     | 6.6.6.2  | 0         | 80000005 | asExternal | 16  | 00:00:04 |
     | 6.6.6.1  | 1         | 80000003 | asExternal | 16  | 00:00:04 |
     | 6.6.6.2  | 1         | 80000003 | asExternal | 16  | 00:00:04 |
     | 6.6.6.1  | 2         | 80000001 | asExternal | 28  | 00:00:04 |
     | 6.6.6.2  | 2         | 80000001 | asExternal | 28  | 00:00:04 |
     | 6.6.6.1  | 0         | 80000001 | rtrInfo    | 16  | 00:00:05 |
     | 6.6.6.2  | 0         | 80000001 | rtrInfo    | 16  | 00:00:05 |
     |__________|___________|__________|____________|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 ospf 1 tre 0
    r2#show ipv4 ospf 1 tre 0
    `--r2
      |`--r1
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 tre 0
    r2#show ipv6 ospf 1 tre 0
    `--r2
      |`--r1
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:05 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:05 |
     | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:04 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:04 |
     | O E2 | 2.2.2.1/32 | 110/0  | ethernet2 | 1.1.2.1 | 00:00:04 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:05 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:05 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:05 |
     | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:04 |
     | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:04 |
     | O E2 | 4321::1/128 | 110/0  | ethernet1 | 1234::1 | 00:00:01 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:05 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

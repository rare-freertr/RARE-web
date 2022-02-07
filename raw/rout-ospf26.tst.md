# Example: ospf with bfd
    
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
    logging file debug ../binTmp/zzz28r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bfd
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bfd
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bfd
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz28r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bfd
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bfd
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bfd
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
     | ethernet2 | 0    | 1.1.1.5 | 4.4.4.1  | full  | 00:00:10 |
     |___________|______|_________|__________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 nei
    r2#show ipv6 ospf 1 nei
     |~~~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | area | address   | routerid | state | uptime   |
     |-----------|------|-----------|----------|-------|----------|
     | ethernet2 | 0    | 1234:2::1 | 6.6.6.1  | full  | 00:00:10 |
     |___________|______|___________|__________|_______|__________|
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
     | 4.4.4.1  | 4.4.4.1 | 80000007 | router      | 40  | 00:00:02 |
     | 4.4.4.2  | 4.4.4.2 | 80000007 | router      | 28  | 00:00:03 |
     | 4.4.4.1  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:10 |
     | 4.4.4.2  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:11 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:10 |
     | 4.4.4.2  | 1.1.1.0 | 80000002 | asExternal  | 16  | 01:00:03 |
     | 4.4.4.1  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:10 |
     | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:11 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:10 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:11 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:10 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:11 |
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
     | 6.6.6.2  | 127508795 | 80000002 | link       | 24  | 01:00:03 |
     | 6.6.6.2  | 127508796 | 80000001 | link       | 24  | 00:00:11 |
     | 6.6.6.1  | 188346452 | 80000001 | link       | 24  | 00:00:11 |
     | 6.6.6.1  | 188346453 | 80000001 | link       | 24  | 00:00:11 |
     | 6.6.6.1  | 0         | 80000005 | router     | 20  | 00:00:03 |
     | 6.6.6.2  | 0         | 80000005 | router     | 20  | 00:00:03 |
     | 6.6.6.2  | 127508795 | 80000002 | prefix     | 20  | 01:00:03 |
     | 6.6.6.2  | 127508796 | 80000001 | prefix     | 20  | 00:00:11 |
     | 6.6.6.1  | 188346452 | 80000001 | prefix     | 20  | 00:00:11 |
     | 6.6.6.1  | 188346453 | 80000001 | prefix     | 20  | 00:00:11 |
     | 6.6.6.1  | 0         | 80000005 | asExternal | 16  | 00:00:11 |
     | 6.6.6.2  | 0         | 80000004 | asExternal | 16  | 00:00:03 |
     | 6.6.6.1  | 1         | 80000003 | asExternal | 16  | 00:00:11 |
     | 6.6.6.2  | 1         | 80000003 | asExternal | 28  | 00:00:03 |
     | 6.6.6.1  | 2         | 80000001 | asExternal | 28  | 00:00:11 |
     | 6.6.6.2  | 2         | 80000002 | asExternal | 28  | 01:00:03 |
     | 6.6.6.1  | 0         | 80000001 | rtrInfo    | 16  | 00:00:11 |
     | 6.6.6.2  | 0         | 80000001 | rtrInfo    | 16  | 00:00:11 |
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
     | O    | 1.1.1.0/30 | 110/20 | ethernet2 | 1.1.1.5 | 00:00:04 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:12 |
     | LOC  | 1.1.1.6/32 | 0/1    | ethernet2 | null    | 00:00:12 |
     | O E2 | 2.2.2.1/32 | 110/0  | ethernet2 | 1.1.1.5 | 00:00:04 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:12 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | O    | 1234:1::/32   | 110/20 | ethernet2 | 1234:2::1 | 00:00:04 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:12 |
     | LOC  | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:12 |
     | O E2 | 4321::1/128   | 110/0  | ethernet2 | 1234:2::1 | 00:00:04 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:12 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

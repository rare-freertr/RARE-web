# Example: ospf broadcast chain with bidir check
    
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
     area 0 spf-bidir
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.1
     traffeng-id ::
     area 0 enable
     area 0 spf-bidir
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
     ipv6 address 1234:1::1 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
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
     area 0 spf-bidir
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.2
     traffeng-id ::
     area 0 enable
     area 0 spf-bidir
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
     ipv6 address 1234:1::2 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf4 1 priority 1
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
     router ospf6 1 priority 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf4 1 priority 1
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
     router ospf6 1 priority 1
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
    router ospf4 1
     vrf v1
     router-id 4.4.4.3
     traffeng-id 0.0.0.0
     area 0 enable
     area 0 spf-bidir
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.3
     traffeng-id ::
     area 0 enable
     area 0 spf-bidir
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz1r4-log.run
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
     router-id 4.4.4.4
     traffeng-id 0.0.0.0
     area 0 enable
     area 0 spf-bidir
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.4
     traffeng-id ::
     area 0 enable
     area 0 spf-bidir
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network broadcast
     router ospf4 1 priority 1
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network broadcast
     router ospf6 1 priority 1
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
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:25 |
     | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:15 |
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
     | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:25 |
     | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:15 |
     |___________|______|___________|__________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 ospf 1 dat 0
    r2#show ipv4 ospf 1 dat 0
     |~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | routerid | lsaid    | sequence | type        | len | time     |
     |----------|----------|----------|-------------|-----|----------|
     | 4.4.4.1  | 4.4.4.1  | 80000005 | router      | 16  | 00:00:15 |
     | 4.4.4.2  | 4.4.4.2  | 80000008 | router      | 28  | 00:00:25 |
     | 4.4.4.3  | 4.4.4.3  | 80000008 | router      | 28  | 00:00:13 |
     | 4.4.4.4  | 4.4.4.4  | 80000005 | router      | 16  | 00:00:25 |
     | 4.4.4.2  | 1.1.1.2  | 80000002 | network     | 12  | 00:00:05 |
     | 4.4.4.2  | 1.1.1.5  | 80000002 | network     | 12  | 00:00:05 |
     | 4.4.4.4  | 1.1.1.10 | 80000002 | network     | 12  | 00:00:05 |
     | 4.4.4.1  | 0.0.0.0  | 80000004 | asExternal  | 16  | 01:00:25 |
     | 4.4.4.2  | 0.0.0.0  | 80000006 | asExternal  | 16  | 01:00:26 |
     | 4.4.4.3  | 0.0.0.0  | 80000006 | asExternal  | 16  | 01:00:24 |
     | 4.4.4.4  | 0.0.0.0  | 80000004 | asExternal  | 16  | 01:00:25 |
     | 4.4.4.1  | 1.1.1.0  | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.2  | 1.1.1.0  | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.2  | 1.1.1.4  | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.3  | 1.1.1.4  | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.3  | 1.1.1.8  | 80000001 | asExternal  | 16  | 00:00:24 |
     | 4.4.4.4  | 1.1.1.8  | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.1  | 2.2.2.1  | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.2  | 2.2.2.2  | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.3  | 2.2.2.3  | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.4  | 2.2.2.4  | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.1  | 4.0.0.0  | 80000001 | opaque-area | 16  | 00:00:26 |
     | 4.4.4.2  | 4.0.0.0  | 80000001 | opaque-area | 16  | 00:00:27 |
     | 4.4.4.3  | 4.0.0.0  | 80000001 | opaque-area | 16  | 00:00:26 |
     | 4.4.4.4  | 4.0.0.0  | 80000001 | opaque-area | 16  | 00:00:26 |
     |__________|__________|__________|_____________|_____|__________|
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
     | 6.6.6.4  | 471433435 | 80000002 | link       | 24  | 00:00:25 |
     | 6.6.6.1  | 797500525 | 80000001 | link       | 24  | 00:00:25 |
     | 6.6.6.2  | 857211112 | 80000002 | link       | 24  | 00:00:26 |
     | 6.6.6.2  | 857211113 | 80000002 | link       | 24  | 00:00:25 |
     | 6.6.6.3  | 861621269 | 80000001 | link       | 24  | 00:00:25 |
     | 6.6.6.3  | 861621270 | 80000001 | link       | 24  | 00:00:24 |
     | 6.6.6.1  | 0         | 80000003 | router     | 20  | 00:00:25 |
     | 6.6.6.2  | 0         | 80000004 | router     | 36  | 00:00:25 |
     | 6.6.6.3  | 0         | 80000004 | router     | 36  | 00:00:14 |
     | 6.6.6.4  | 0         | 80000003 | router     | 20  | 00:00:25 |
     | 6.6.6.4  | 471433435 | 80000002 | network    | 12  | 00:00:02 |
     | 6.6.6.2  | 857211112 | 80000002 | network    | 12  | 00:00:10 |
     | 6.6.6.2  | 857211113 | 80000002 | network    | 12  | 00:00:05 |
     | 6.6.6.4  | 471433435 | 80000001 | prefix     | 20  | 00:00:26 |
     | 6.6.6.1  | 797500525 | 80000001 | prefix     | 20  | 00:00:25 |
     | 6.6.6.2  | 857211112 | 80000001 | prefix     | 20  | 00:00:26 |
     | 6.6.6.2  | 857211113 | 80000001 | prefix     | 20  | 00:00:26 |
     | 6.6.6.3  | 861621269 | 80000001 | prefix     | 20  | 00:00:25 |
     | 6.6.6.3  | 861621270 | 80000001 | prefix     | 20  | 00:00:24 |
     | 6.6.6.1  | 0         | 80000004 | asExternal | 16  | 00:00:25 |
     | 6.6.6.2  | 0         | 80000006 | asExternal | 16  | 00:00:26 |
     | 6.6.6.3  | 0         | 80000006 | asExternal | 16  | 00:00:24 |
     | 6.6.6.4  | 0         | 80000004 | asExternal | 16  | 00:00:26 |
     | 6.6.6.1  | 1         | 80000001 | asExternal | 28  | 00:00:25 |
     | 6.6.6.2  | 1         | 80000003 | asExternal | 16  | 00:00:26 |
     | 6.6.6.3  | 1         | 80000003 | asExternal | 16  | 00:00:24 |
     | 6.6.6.4  | 1         | 80000001 | asExternal | 28  | 00:00:26 |
     | 6.6.6.2  | 2         | 80000001 | asExternal | 28  | 00:00:26 |
     | 6.6.6.3  | 2         | 80000001 | asExternal | 28  | 00:00:24 |
     | 6.6.6.1  | 0         | 80000001 | rtrInfo    | 16  | 00:00:26 |
     | 6.6.6.2  | 0         | 80000001 | rtrInfo    | 16  | 00:00:27 |
     | 6.6.6.3  | 0         | 80000001 | rtrInfo    | 16  | 00:00:26 |
     | 6.6.6.4  | 0         | 80000001 | rtrInfo    | 16  | 00:00:26 |
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
      |`--1.1.1.2
      |   `--r1
       `--1.1.1.5
          `--r3
             `--1.1.1.10
                `--r4
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 tre 0
    r2#show ipv6 ospf 1 tre 0
    `--r2
      |`--6.6.6.2/331800e8
      |   `--r1
       `--6.6.6.2/331800e9
          `--r3
             `--6.6.6.4/1c1980db
                `--r4
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:27 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:27 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:26 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:26 |
     | O    | 1.1.1.8/30 | 110/20 | ethernet2 | 1.1.1.6 | 00:00:05 |
     | O E2 | 2.2.2.1/32 | 110/0  | ethernet1 | 1.1.1.1 | 00:00:05 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:27 |
     | O E2 | 2.2.2.3/32 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:05 |
     | O E2 | 2.2.2.4/32 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:05 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:27 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:27 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:26 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:26 |
     | O    | 1234:3::/32   | 110/20 | ethernet2 | 1234:2::2 | 00:00:05 |
     | O E2 | 4321::1/128   | 110/0  | ethernet1 | 1234:1::1 | 00:00:11 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:27 |
     | O E2 | 4321::3/128   | 110/0  | ethernet2 | 1234:2::2 | 00:00:05 |
     | O E2 | 4321::4/128   | 110/0  | ethernet2 | 1234:2::2 | 00:00:02 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

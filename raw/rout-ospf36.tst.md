# Example: ospf triangle connection
    
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
    logging file debug ../binTmp/zzz26r1-log.run
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
     ipv6 address 1234:1::1 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz26r2-log.run
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
     ipv6 address 1234:1::2 ffff:ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
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
     router ospf6 1 enable
     router ospf6 1 area 0
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
    logging file debug ../binTmp/zzz26r3-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
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
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.3
     traffeng-id ::
     area 0 enable
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
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:3::1 ffff:ffff::
     ipv6 access-group-in test6
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:01 |
     | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:01 |
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
     | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:02 |
     | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:02 |
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
     | 4.4.4.1  | 4.4.4.1 | 80000007 | router      | 52  | 00:00:02 |
     | 4.4.4.2  | 4.4.4.2 | 80000006 | router      | 52  | 00:00:02 |
     | 4.4.4.3  | 4.4.4.3 | 80000007 | router      | 52  | 00:00:02 |
     | 4.4.4.1  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:02 |
     | 4.4.4.2  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:02 |
     | 4.4.4.3  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:02 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.1  | 1.1.1.8 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.3  | 1.1.1.8 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal  | 16  | 00:00:02 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:02 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:02 |
     | 4.4.4.3  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:02 |
     |__________|_________|__________|_____________|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 ospf 1 dat 0
    r2#show ipv6 ospf 1 dat 0
     |~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | routerid | lsaid      | sequence | type       | len | time     |
     |----------|------------|----------|------------|-----|----------|
     | 6.6.6.1  | 149281591  | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.1  | 149281592  | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.2  | 361064672  | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.2  | 361064673  | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.3  | 1050907844 | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.3  | 1050907845 | 80000001 | link       | 24  | 00:00:02 |
     | 6.6.6.1  | 0          | 80000004 | router     | 36  | 00:00:02 |
     | 6.6.6.2  | 0          | 80000004 | router     | 36  | 00:00:02 |
     | 6.6.6.3  | 0          | 80000004 | router     | 36  | 00:00:02 |
     | 6.6.6.1  | 149281591  | 80000001 | prefix     | 20  | 00:00:02 |
     | 6.6.6.1  | 149281592  | 80000002 | prefix     | 20  | 00:00:02 |
     | 6.6.6.2  | 361064672  | 80000001 | prefix     | 20  | 00:00:02 |
     | 6.6.6.2  | 361064673  | 80000001 | prefix     | 20  | 00:00:02 |
     | 6.6.6.3  | 1050907844 | 80000001 | prefix     | 20  | 00:00:02 |
     | 6.6.6.3  | 1050907845 | 80000002 | prefix     | 20  | 00:00:02 |
     | 6.6.6.1  | 0          | 80000005 | asExternal | 16  | 00:00:02 |
     | 6.6.6.2  | 0          | 80000005 | asExternal | 16  | 00:00:02 |
     | 6.6.6.3  | 0          | 80000005 | asExternal | 16  | 00:00:02 |
     | 6.6.6.1  | 1          | 80000003 | asExternal | 16  | 00:00:02 |
     | 6.6.6.2  | 1          | 80000003 | asExternal | 16  | 00:00:02 |
     | 6.6.6.3  | 1          | 80000003 | asExternal | 16  | 00:00:02 |
     | 6.6.6.1  | 2          | 80000001 | asExternal | 28  | 00:00:02 |
     | 6.6.6.2  | 2          | 80000001 | asExternal | 28  | 00:00:02 |
     | 6.6.6.3  | 2          | 80000001 | asExternal | 28  | 00:00:02 |
     | 6.6.6.1  | 0          | 80000001 | rtrInfo    | 16  | 00:00:02 |
     | 6.6.6.2  | 0          | 80000001 | rtrInfo    | 16  | 00:00:02 |
     | 6.6.6.3  | 0          | 80000001 | rtrInfo    | 16  | 00:00:02 |
     |__________|____________|__________|____________|_____|__________|
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
       `--r3
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
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric  | iface     | hop     | time     |
     |------|------------|---------|-----------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0     | ethernet1 | null    | 00:00:03 |
     | LOC  | 1.1.1.2/32 | 0/1     | ethernet1 | null    | 00:00:03 |
     | C    | 1.1.1.4/30 | 0/0     | ethernet2 | null    | 00:00:03 |
     | LOC  | 1.1.1.5/32 | 0/1     | ethernet2 | null    | 00:00:03 |
     | O    | 1.1.1.8/30 | 110/110 | ethernet2 | 1.1.1.6 | 00:00:02 |
     | O E2 | 2.2.2.1/32 | 110/0   | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0     | loopback1 | null    | 00:00:03 |
     | O E2 | 2.2.2.3/32 | 110/0   | ethernet2 | 1.1.1.6 | 00:00:02 |
     |______|____________|_________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric  | iface     | hop       | time     |
     |------|---------------|---------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0     | ethernet1 | null      | 00:00:03 |
     | LOC  | 1234:1::2/128 | 0/1     | ethernet1 | null      | 00:00:03 |
     | C    | 1234:2::/32   | 0/0     | ethernet2 | null      | 00:00:03 |
     | LOC  | 1234:2::1/128 | 0/1     | ethernet2 | null      | 00:00:03 |
     | O    | 1234:3::/32   | 110/110 | ethernet2 | 1234:2::2 | 00:00:02 |
     | O E2 | 4321::1/128   | 110/0   | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0     | loopback1 | null      | 00:00:03 |
     | O E2 | 4321::3/128   | 110/0   | ethernet2 | 1234:2::2 | 00:00:02 |
     |______|_______________|_________|___________|___________|__________|
    r2#
    r2#
    ```

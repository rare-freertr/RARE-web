# Example: ospf peer template
    
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
    interface template1
     no description
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
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
     template template1
     no shutdown
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
    interface template1
     no description
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
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
     template template1
     no shutdown
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
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:04 |
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
     | ethernet1 | 0    | 1234::1 | 6.6.6.1  | full  | 00:00:04 |
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
     | 4.4.4.1  | 4.4.4.1 | 80000005 | router      | 40  | 00:00:01 |
     | 4.4.4.2  | 4.4.4.2 | 80000005 | router      | 40  | 00:00:01 |
     | 4.4.4.1  | 0.0.0.0 | 80000006 | asExternal  | 16  | 01:00:05 |
     | 4.4.4.2  | 0.0.0.0 | 80000006 | asExternal  | 16  | 01:00:05 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:05 |
     | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:05 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:05 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:06 |
     | 4.4.4.1  | 9.9.9.0 | 80000001 | asExternal  | 16  | 00:00:05 |
     | 4.4.4.2  | 9.9.9.0 | 80000001 | asExternal  | 16  | 00:00:06 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:06 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:06 |
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
     | 6.6.6.1  | 20017138   | 80000001 | link       | 24  | 00:00:05 |
     | 6.6.6.1  | 20017139   | 80000001 | link       | 24  | 00:00:04 |
     | 6.6.6.2  | 1033414662 | 80000001 | link       | 24  | 00:00:05 |
     | 6.6.6.2  | 1033414663 | 80000001 | link       | 24  | 00:00:05 |
     | 6.6.6.1  | 0          | 80000003 | router     | 20  | 00:00:01 |
     | 6.6.6.2  | 0          | 80000003 | router     | 20  | 00:00:01 |
     | 6.6.6.1  | 20017138   | 80000001 | prefix     | 20  | 00:00:05 |
     | 6.6.6.1  | 20017139   | 80000001 | prefix     | 20  | 00:00:04 |
     | 6.6.6.2  | 1033414662 | 80000001 | prefix     | 20  | 00:00:05 |
     | 6.6.6.2  | 1033414663 | 80000001 | prefix     | 20  | 00:00:05 |
     | 6.6.6.1  | 0          | 80000005 | asExternal | 16  | 00:00:05 |
     | 6.6.6.2  | 0          | 80000006 | asExternal | 16  | 00:00:05 |
     | 6.6.6.1  | 1          | 80000003 | asExternal | 28  | 00:00:05 |
     | 6.6.6.2  | 1          | 80000003 | asExternal | 28  | 00:00:05 |
     | 6.6.6.1  | 2          | 80000001 | asExternal | 16  | 00:00:05 |
     | 6.6.6.2  | 2          | 80000001 | asExternal | 16  | 00:00:05 |
     | 6.6.6.1  | 0          | 80000001 | rtrInfo    | 16  | 00:00:06 |
     | 6.6.6.2  | 0          | 80000001 | rtrInfo    | 16  | 00:00:06 |
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
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:06 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:06 |
     | O E2 | 2.2.2.1/32 | 110/0  | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:06 |
     | C    | 9.9.9.0/24 | 0/0    | template1 | null    | 00:00:06 |
     | LOC  | 9.9.9.9/32 | 0/1    | template1 | null    | 00:00:06 |
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
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:06 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:06 |
     | O E2 | 4321::1/128 | 110/0  | ethernet1 | 1234::1 | 00:00:02 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:06 |
     | C    | 9999::/16   | 0/0    | template1 | null    | 00:00:06 |
     | LOC  | 9999::9/128 | 0/1    | template1 | null    | 00:00:06 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

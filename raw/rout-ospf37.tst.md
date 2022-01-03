# Example: ospf prefix movement
    
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
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 10
     !
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
     router-id 4.4.4.1
     traffeng-id 0.0.0.0
     area 0 enable
     advertise 2.2.2.1/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.1
     traffeng-id ::
     area 0 enable
     advertise 4321::1/128 route-map rm1
     advertise 4321::222/128 route-map rm1
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
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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
     advertise 2.2.2.2/32
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.2
     traffeng-id ::
     area 0 enable
     advertise 4321::2/128
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
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
    logging file debug ../binTmp/zzz1r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 20
     !
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
     advertise 2.2.2.3/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.3
     traffeng-id ::
     area 0 enable
     advertise 4321::3/128 route-map rm1
     advertise 4321::222/128 route-map rm1
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
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.103 255.255.255.255
     ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:24 |
     | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:24 |
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
     | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:24 |
     | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:24 |
     |___________|______|___________|__________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 ospf 1 dat 0
    r2#show ipv4 ospf 1 dat 0
     |~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | routerid | lsaid     | sequence | type        | len | time     |
     |----------|-----------|----------|-------------|-----|----------|
     | 4.4.4.1  | 4.4.4.1   | 80000004 | router      | 28  | 00:00:23 |
     | 4.4.4.2  | 4.4.4.2   | 80000007 | router      | 64  | 00:00:24 |
     | 4.4.4.3  | 4.4.4.3   | 80000004 | router      | 28  | 00:00:24 |
     | 4.4.4.1  | 2.2.2.1   | 80000003 | asExternal  | 16  | 00:00:07 |
     | 4.4.4.2  | 2.2.2.2   | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.3  | 2.2.2.3   | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.1  | 2.2.2.222 | 80000003 | asExternal  | 16  | 00:00:07 |
     | 4.4.4.3  | 2.2.2.222 | 80000001 | asExternal  | 16  | 00:00:25 |
     | 4.4.4.1  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:25 |
     | 4.4.4.2  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:26 |
     | 4.4.4.3  | 4.0.0.0   | 80000001 | opaque-area | 16  | 00:00:25 |
     |__________|___________|__________|_____________|_____|__________|
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
     | 6.6.6.1  | 107253210 | 80000001 | link       | 24  | 00:00:23 |
     | 6.6.6.2  | 561169097 | 80000001 | link       | 24  | 00:00:25 |
     | 6.6.6.2  | 561169098 | 80000001 | link       | 24  | 00:00:25 |
     | 6.6.6.2  | 561169099 | 80000001 | link       | 24  | 00:00:25 |
     | 6.6.6.3  | 852363941 | 80000001 | link       | 24  | 00:00:24 |
     | 6.6.6.1  | 0         | 80000003 | router     | 20  | 00:00:23 |
     | 6.6.6.2  | 0         | 80000004 | router     | 36  | 00:00:23 |
     | 6.6.6.3  | 0         | 80000003 | router     | 20  | 00:00:24 |
     | 6.6.6.1  | 107253210 | 80000001 | prefix     | 20  | 00:00:23 |
     | 6.6.6.2  | 561169097 | 80000001 | prefix     | 32  | 00:00:25 |
     | 6.6.6.2  | 561169098 | 80000001 | prefix     | 20  | 00:00:25 |
     | 6.6.6.2  | 561169099 | 80000001 | prefix     | 20  | 00:00:25 |
     | 6.6.6.3  | 852363941 | 80000001 | prefix     | 20  | 00:00:24 |
     | 6.6.6.1  | 0         | 80000003 | asExternal | 28  | 00:00:07 |
     | 6.6.6.2  | 0         | 80000001 | asExternal | 28  | 00:00:25 |
     | 6.6.6.3  | 0         | 80000001 | asExternal | 28  | 00:00:25 |
     | 6.6.6.1  | 1         | 80000003 | asExternal | 28  | 00:00:07 |
     | 6.6.6.3  | 1         | 80000001 | asExternal | 28  | 00:00:25 |
     | 6.6.6.1  | 0         | 80000001 | rtrInfo    | 16  | 00:00:24 |
     | 6.6.6.2  | 0         | 80000001 | rtrInfo    | 16  | 00:00:26 |
     | 6.6.6.3  | 0         | 80000001 | rtrInfo    | 16  | 00:00:25 |
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
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:26 |
     | LOC  | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:26 |
     | C    | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:25 |
     | LOC  | 1.1.1.5/32   | 0/1    | ethernet2 | null    | 00:00:25 |
     | O E2 | 2.2.2.1/32   | 110/10 | ethernet1 | 1.1.1.1 | 00:00:07 |
     | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:26 |
     | O E2 | 2.2.2.3/32   | 110/20 | ethernet2 | 1.1.1.6 | 00:00:24 |
     | O E2 | 2.2.2.222/32 | 110/10 | ethernet1 | 1.1.1.1 | 00:00:07 |
     |______|______________|________|___________|_________|__________|
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:26 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:26 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:25 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:25 |
     | O E2 | 4321::1/128   | 110/10 | ethernet1 | 1234:1::1 | 00:00:07 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:26 |
     | O E2 | 4321::3/128   | 110/20 | ethernet2 | 1234:2::2 | 00:00:24 |
     | O E2 | 4321::222/128 | 110/10 | ethernet1 | 1234:1::1 | 00:00:07 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

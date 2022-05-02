# Example: ospf nonbroadcast connection
    
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
    logging file debug ../binTmp/zzz72r1-log.run
    !
    bridge 1
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
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network nonbroadcast
     router ospf4 1 hello-time 30000
     router ospf4 1 dead-time 120000
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network nonbroadcast
     router ospf6 1 hello-time 30000
     router ospf6 1 dead-time 120000
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
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
    logging file debug ../binTmp/zzz72r2-log.run
    !
    bridge 1
     mac-learn
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
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network nonbroadcast
     router ospf4 1 hello-time 30000
     router ospf4 1 dead-time 120000
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network nonbroadcast
     router ospf6 1 hello-time 30000
     router ospf6 1 dead-time 120000
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     bridge-group 1
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
    logging file debug ../binTmp/zzz72r3-log.run
    !
    bridge 1
     mac-learn
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
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234::3 ffff::
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network nonbroadcast
     router ospf4 1 hello-time 30000
     router ospf4 1 dead-time 120000
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network nonbroadcast
     router ospf6 1 hello-time 30000
     router ospf6 1 dead-time 120000
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     bridge-group 1
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
    logging file debug ../binTmp/zzz72r4-log.run
    !
    bridge 1
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
     router-id 4.4.4.4
     traffeng-id 0.0.0.0
     area 0 enable
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.4
     traffeng-id ::
     area 0 enable
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.0
     ipv4 resend-packet
     ipv6 address 1234::4 ffff::
     ipv6 resend-packet
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 network nonbroadcast
     router ospf4 1 priority 1
     router ospf4 1 hello-time 30000
     router ospf4 1 dead-time 120000
     router ospf4 1 neighbor 1.1.1.1
     router ospf4 1 neighbor 1.1.1.2
     router ospf4 1 neighbor 1.1.1.3
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 network nonbroadcast
     router ospf6 1 priority 1
     router ospf6 1 hello-time 30000
     router ospf6 1 dead-time 120000
     router ospf6 1 neighbor 1234::1
     router ospf6 1 neighbor 1234::2
     router ospf6 1 neighbor 1234::3
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
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
     | bvi1      | 0    | 1.1.1.4 | 4.4.4.4  | full  | 00:00:16 |
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
     | bvi1      | 0    | 1234::4 | 6.6.6.4  | full  | 00:00:16 |
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
     | 4.4.4.1  | 4.4.4.1 | 80000005 | router      | 16  | 00:00:06 |
     | 4.4.4.2  | 4.4.4.2 | 80000005 | router      | 16  | 00:00:06 |
     | 4.4.4.3  | 4.4.4.3 | 80000005 | router      | 16  | 00:00:16 |
     | 4.4.4.4  | 4.4.4.4 | 80000005 | router      | 16  | 00:00:26 |
     | 4.4.4.4  | 1.1.1.4 | 80000003 | network     | 20  | 00:00:06 |
     | 4.4.4.2  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:27 |
     | 4.4.4.3  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:26 |
     | 4.4.4.4  | 0.0.0.0 | 80000004 | asExternal  | 16  | 01:00:26 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:27 |
     | 4.4.4.3  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.4  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:27 |
     | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.4  | 2.2.2.4 | 80000001 | asExternal  | 16  | 00:00:26 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:26 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:27 |
     | 4.4.4.3  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:26 |
     | 4.4.4.4  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:26 |
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
     | 6.6.6.2  | 9006506   | 80000001 | link       | 24  | 00:00:27 |
     | 6.6.6.4  | 59169497  | 80000002 | link       | 24  | 00:00:26 |
     | 6.6.6.3  | 273401038 | 80000001 | link       | 24  | 00:00:26 |
     | 6.6.6.1  | 426008503 | 80000001 | link       | 24  | 00:00:27 |
     | 6.6.6.1  | 0         | 80000003 | router     | 20  | 00:00:07 |
     | 6.6.6.2  | 0         | 80000003 | router     | 20  | 00:00:06 |
     | 6.6.6.3  | 0         | 80000003 | router     | 20  | 00:00:16 |
     | 6.6.6.4  | 0         | 80000003 | router     | 20  | 00:00:26 |
     | 6.6.6.4  | 59169497  | 80000004 | network    | 20  | 00:00:04 |
     | 6.6.6.2  | 9006506   | 80000001 | prefix     | 20  | 00:00:27 |
     | 6.6.6.4  | 59169497  | 80000001 | prefix     | 20  | 00:00:27 |
     | 6.6.6.3  | 273401038 | 80000001 | prefix     | 20  | 00:00:26 |
     | 6.6.6.1  | 426008503 | 80000001 | prefix     | 20  | 00:00:27 |
     | 6.6.6.1  | 0         | 80000003 | asExternal | 16  | 00:00:27 |
     | 6.6.6.2  | 0         | 80000003 | asExternal | 16  | 00:00:27 |
     | 6.6.6.3  | 0         | 80000004 | asExternal | 16  | 00:00:25 |
     | 6.6.6.4  | 0         | 80000004 | asExternal | 16  | 00:00:27 |
     | 6.6.6.1  | 1         | 80000001 | asExternal | 28  | 00:00:26 |
     | 6.6.6.2  | 1         | 80000001 | asExternal | 28  | 00:00:27 |
     | 6.6.6.3  | 1         | 80000001 | asExternal | 28  | 00:00:25 |
     | 6.6.6.4  | 1         | 80000001 | asExternal | 28  | 00:00:27 |
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
       `--1.1.1.4
         |`--r4
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
    `--6.6.6.2/00000000
       `--6.6.6.4/0386dad9
         |`--6.6.6.4/00000000
         |`--6.6.6.1/00000000
          `--6.6.6.3/00000000
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
     | C    | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:27 |
     | LOC  | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:27 |
     | O E2 | 2.2.2.1/32 | 110/0  | bvi1      | 1.1.1.4 | 00:00:07 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:27 |
     | O E2 | 2.2.2.3/32 | 110/0  | bvi1      | 1.1.1.4 | 00:00:07 |
     | O E2 | 2.2.2.4/32 | 110/0  | bvi1      | 1.1.1.4 | 00:00:07 |
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
     | C    | 1234::/16   | 0/0    | bvi1      | null    | 00:00:27 |
     | LOC  | 1234::2/128 | 0/1    | bvi1      | null    | 00:00:27 |
     | O E2 | 4321::1/128 | 110/0  | bvi1      | 1234::4 | 00:00:04 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:27 |
     | O E2 | 4321::3/128 | 110/0  | bvi1      | 1234::4 | 00:00:04 |
     | O E2 | 4321::4/128 | 110/0  | bvi1      | 1234::4 | 00:00:04 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

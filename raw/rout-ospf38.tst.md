# Example: ospf with bier
    
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
    logging file debug ../binTmp/zzz49r1-log.run
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
     router-id 4.4.4.1
     traffeng-id 0.0.0.0
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.1
     traffeng-id ::
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bier index 1
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bier index 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.3
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9999::9
     tunnel domain-name 4321::3
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
    logging file debug ../binTmp/zzz49r2-log.run
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
     router-id 4.4.4.2
     traffeng-id 0.0.0.0
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.2
     traffeng-id ::
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bier index 2
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bier index 2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
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
    logging file debug ../binTmp/zzz49r3-log.run
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
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.3
     traffeng-id ::
     bier 256 10
     area 0 enable
     area 0 bier
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf4 1 bier index 3
     router ospf6 1 enable
     router ospf6 1 area 0
     router ospf6 1 bier index 3
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 access-group-in test6
     mpls enable
     router ospf4 1 enable
     router ospf4 1 area 0
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel key 3
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.1
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel key 3
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9999::9
     tunnel domain-name 4321::1
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1112 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
     | ethernet1 | 0    | 1.1.1.1 | 4.4.4.1  | full  | 00:00:12 |
     | ethernet2 | 0    | 1.1.1.6 | 4.4.4.3  | full  | 00:00:11 |
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
     | ethernet1 | 0    | 1234:1::1 | 6.6.6.1  | full  | 00:00:12 |
     | ethernet2 | 0    | 1234:2::2 | 6.6.6.3  | full  | 00:00:12 |
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
     | 4.4.4.1  | 4.4.4.1 | 80000005 | router      | 40  | 00:00:12 |
     | 4.4.4.2  | 4.4.4.2 | 80000007 | router      | 64  | 00:00:12 |
     | 4.4.4.3  | 4.4.4.3 | 80000005 | router      | 40  | 00:00:09 |
     | 4.4.4.1  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:12 |
     | 4.4.4.2  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:13 |
     | 4.4.4.3  | 0.0.0.0 | 80000002 | asExternal  | 16  | 01:00:13 |
     | 4.4.4.1  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:12 |
     | 4.4.4.2  | 1.1.1.0 | 80000001 | asExternal  | 16  | 00:00:13 |
     | 4.4.4.2  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:12 |
     | 4.4.4.3  | 1.1.1.4 | 80000001 | asExternal  | 16  | 00:00:13 |
     | 4.4.4.1  | 2.2.2.1 | 80000001 | asExternal  | 16  | 00:00:13 |
     | 4.4.4.2  | 2.2.2.2 | 80000001 | asExternal  | 16  | 00:00:13 |
     | 4.4.4.3  | 2.2.2.3 | 80000001 | asExternal  | 16  | 00:00:13 |
     | 4.4.4.1  | 3.3.3.0 | 80000001 | asExternal  | 16  | 00:00:12 |
     | 4.4.4.3  | 3.3.3.0 | 80000001 | asExternal  | 16  | 00:00:12 |
     | 4.4.4.1  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:13 |
     | 4.4.4.2  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:13 |
     | 4.4.4.3  | 4.0.0.0 | 80000001 | opaque-area | 16  | 00:00:13 |
     | 4.4.4.1  | 7.0.0.1 | 80000001 | opaque-area | 36  | 00:00:13 |
     | 4.4.4.2  | 7.0.0.1 | 80000001 | opaque-area | 36  | 00:00:13 |
     | 4.4.4.3  | 7.0.0.1 | 80000001 | opaque-area | 36  | 00:00:13 |
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
     | 6.6.6.2  | 88519091  | 80000001 | link       | 24  | 00:00:13 |
     | 6.6.6.2  | 88519092  | 80000001 | link       | 24  | 00:00:13 |
     | 6.6.6.2  | 88519093  | 80000001 | link       | 24  | 00:00:12 |
     | 6.6.6.1  | 142428202 | 80000001 | link       | 24  | 00:00:13 |
     | 6.6.6.1  | 142428203 | 80000001 | link       | 24  | 00:00:12 |
     | 6.6.6.3  | 371400890 | 80000001 | link       | 24  | 00:00:13 |
     | 6.6.6.3  | 371400891 | 80000001 | link       | 24  | 00:00:12 |
     | 6.6.6.1  | 0         | 80000003 | router     | 20  | 00:00:12 |
     | 6.6.6.2  | 0         | 80000004 | router     | 36  | 00:00:12 |
     | 6.6.6.3  | 0         | 80000003 | router     | 20  | 00:00:09 |
     | 6.6.6.2  | 88519091  | 80000001 | prefix     | 32  | 00:00:13 |
     | 6.6.6.2  | 88519092  | 80000001 | prefix     | 20  | 00:00:13 |
     | 6.6.6.2  | 88519093  | 80000001 | prefix     | 20  | 00:00:12 |
     | 6.6.6.1  | 142428202 | 80000001 | prefix     | 32  | 00:00:13 |
     | 6.6.6.1  | 142428203 | 80000001 | prefix     | 20  | 00:00:12 |
     | 6.6.6.3  | 371400890 | 80000001 | prefix     | 32  | 00:00:13 |
     | 6.6.6.3  | 371400891 | 80000001 | prefix     | 20  | 00:00:12 |
     | 6.6.6.1  | 0         | 80000005 | asExternal | 16  | 00:00:12 |
     | 6.6.6.2  | 0         | 80000004 | asExternal | 16  | 00:00:13 |
     | 6.6.6.3  | 0         | 80000005 | asExternal | 16  | 00:00:12 |
     | 6.6.6.1  | 1         | 80000003 | asExternal | 28  | 00:00:12 |
     | 6.6.6.2  | 1         | 80000002 | asExternal | 16  | 00:00:12 |
     | 6.6.6.3  | 1         | 80000003 | asExternal | 28  | 00:00:12 |
     | 6.6.6.1  | 2         | 80000002 | asExternal | 28  | 00:00:12 |
     | 6.6.6.2  | 2         | 80000001 | asExternal | 28  | 00:00:12 |
     | 6.6.6.3  | 2         | 80000002 | asExternal | 28  | 00:00:12 |
     | 6.6.6.1  | 1         | 80000001 | ext-prefix | 64  | 00:00:13 |
     | 6.6.6.2  | 1         | 80000001 | ext-prefix | 64  | 00:00:13 |
     | 6.6.6.3  | 1         | 80000001 | ext-prefix | 64  | 00:00:13 |
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
    r2#show ipv6 ospf 1 tre
    r2#show ipv6 ospf 1 tre
    r2#show ipv6 ospf 1 tre 0
    r2#show ipv6 ospf 1 tre 0
    `--6.6.6.2/00000000
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:13 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:13 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:13 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:13 |
     | O    | 2.2.2.1/32 | 110/20 | ethernet1 | 1.1.1.1 | 00:00:12 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:13 |
     | O    | 2.2.2.3/32 | 110/20 | ethernet2 | 1.1.1.6 | 00:00:09 |
     | O E2 | 3.3.3.0/30 | 110/0  | ethernet2 | 1.1.1.6 | 00:00:09 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix         | metric | iface     | hop       | time     |
     |------|----------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32    | 0/0    | ethernet1 | null      | 00:00:13 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1 | null      | 00:00:13 |
     | C    | 1234:2::/32    | 0/0    | ethernet2 | null      | 00:00:13 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2 | null      | 00:00:13 |
     | O    | 4321::1/128    | 110/20 | ethernet1 | 1234:1::1 | 00:00:12 |
     | C    | 4321::2/128    | 0/0    | loopback1 | null      | 00:00:13 |
     | O    | 4321::3/128    | 110/20 | ethernet2 | 1234:2::2 | 00:00:09 |
     | O E2 | 4321::1110/124 | 110/0  | ethernet2 | 1234:2::2 | 00:00:09 |
     |______|________________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 bier v1
    r2#show ipv4 bier v1
     |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | prefix     | index | base   | oldbase | size  |
     |------------|-------|--------|---------|-------|
     | 2.2.2.1/32 | 1     | 73     | 73      | 3-256 |
     | 2.2.2.3/32 | 3     | 987754 | 987754  | 3-256 |
     |____________|_______|________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bier v1
    r2#show ipv6 bier v1
     |~~~~~~~~~~~~~|~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~~|
     | prefix      | index | base  | oldbase | size  |
     |-------------|-------|-------|---------|-------|
     | 4321::1/128 | 1     | 49461 | 49461   | 3-256 |
     | 4321::3/128 | 3     | 21495 | 21495   | 3-256 |
     |_____________|_______|_______|_________|_______|
    r2#
    r2#
    ```

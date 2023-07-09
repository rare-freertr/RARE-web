# Example: olsr triangle connection
    
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
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router olsr4 1 enable
     router olsr4 1 metric-in 200
     router olsr6 1 enable
     router olsr6 1 metric-in 200
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
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
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
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234:3::1 ffff:ffff::
     ipv6 access-group-in test6
     router olsr4 1 enable
     router olsr4 1 metric-in 200
     router olsr6 1 enable
     router olsr6 1 metric-in 200
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
    r2#show ipv4 olsr 1 sum
    r2#show ipv4 olsr 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor | uptime   |
     |-----------|-------|----------|----------|
     | ethernet1 | 3     | 1.1.1.1  | 00:01:01 |
     | ethernet2 | 3     | 1.1.1.6  | 00:01:01 |
     |___________|_______|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 sum
    r2#show ipv6 olsr 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor  | uptime   |
     |-----------|-------|-----------|----------|
     | ethernet1 | 3     | 1234:1::1 | 00:01:02 |
     | ethernet2 | 3     | 1234:2::2 | 00:01:02 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 olsr 1 dat
    r2#show ipv4 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | N   | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:01:07 |
     | N   | 1.1.1.4/30 | 1/0    | ethernet2 | null    | 00:01:07 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet1 | 1.1.1.1 | 00:00:37 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2 | 1.1.1.6 | 00:00:36 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1 | 1.1.1.1 | 00:00:37 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2 | 1.1.1.6 | 00:00:36 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 dat
    r2#show ipv6 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop       | time     |
     |-----|-------------|--------|-----------|-----------|----------|
     | N   | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:01:07 |
     | N   | 1234:2::/32 | 1/0    | ethernet2 | null      | 00:01:07 |
     | N   | 1234:3::/32 | 140/1  | ethernet1 | 1234:1::1 | 00:00:37 |
     | N   | 1234:3::/32 | 140/1  | ethernet2 | 1234:2::2 | 00:00:37 |
     | N   | 4321::1/128 | 140/1  | ethernet1 | 1234:1::1 | 00:00:37 |
     | N   | 4321::3/128 | 140/1  | ethernet2 | 1234:2::2 | 00:00:37 |
     |_____|_____________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:01:07 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:01:07 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:01:07 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:01:07 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2 | 1.1.1.6 | 00:00:37 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1 | 1.1.1.1 | 00:00:37 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:01:07 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2 | 1.1.1.6 | 00:00:37 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface     | hop       | time     |
     |-----|---------------|--------|-----------|-----------|----------|
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:01:07 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:01:07 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:01:07 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:01:07 |
     | N   | 1234:3::/32   | 140/1  | ethernet2 | 1234:2::2 | 00:00:37 |
     | N   | 4321::1/128   | 140/1  | ethernet1 | 1234:1::1 | 00:00:37 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:01:07 |
     | N   | 4321::3/128   | 140/1  | ethernet2 | 1234:2::2 | 00:00:37 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

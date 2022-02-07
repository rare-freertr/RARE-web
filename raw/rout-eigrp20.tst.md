# Example: eigrp triangle connection
    
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
    logging file debug ../binTmp/zzz59r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router eigrp4 1
     vrf v1
     router-id 4.4.4.1
     as 1
     redistribute connected
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.1
     as 1
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
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router eigrp4 1 enable
     router eigrp4 1 delay-in 100
     router eigrp6 1 enable
     router eigrp6 1 delay-in 100
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
    logging file debug ../binTmp/zzz59r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router eigrp4 1
     vrf v1
     router-id 4.4.4.2
     as 1
     redistribute connected
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.2
     as 1
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
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router eigrp4 1 enable
     router eigrp6 1 enable
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
    logging file debug ../binTmp/zzz59r3-log.run
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
    router eigrp4 1
     vrf v1
     router-id 4.4.4.3
     as 1
     redistribute connected
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.3
     as 1
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
     router eigrp4 1 enable
     router eigrp6 1 enable
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
     router eigrp4 1 enable
     router eigrp4 1 delay-in 100
     router eigrp6 1 enable
     router eigrp6 1 delay-in 100
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
    r2#show ipv4 eigrp 1 sum
    r2#show ipv4 eigrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | peer    | learned | adverted | uptime   |
     |-----------|---------|---------|----------|----------|
     | ethernet1 | 1.1.1.1 | 2       | 4        | 00:00:16 |
     | ethernet2 | 1.1.1.6 | 2       | 3        | 00:00:16 |
     |___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 sum
    r2#show ipv6 eigrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | peer      | learned | adverted | uptime   |
     |-----------|-----------|---------|----------|----------|
     | ethernet1 | 1234:1::1 | 2       | 4        | 00:00:16 |
     | ethernet2 | 1234:2::2 | 2       | 3        | 00:00:16 |
     |___________|___________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 eigrp 1 rou
    r2#show ipv4 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:17 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:17 |
     | null | 1.1.1.8/30 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | null | 1.1.1.8/30 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:01 |
     | null | 2.2.2.1/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:17 |
     | null | 2.2.2.3/32 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:01 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 rou
    r2#show ipv6 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop       | time     |
     |------|-------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32 | 0/0    | ethernet1 | null      | 00:00:17 |
     | C    | 1234:2::/32 | 0/0    | ethernet2 | null      | 00:00:17 |
     | null | 1234:3::/32 | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | null | 1234:3::/32 | 90/10  | ethernet2 | 1234:2::2 | 00:00:01 |
     | null | 4321::1/128 | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null      | 00:00:17 |
     | null | 4321::3/128 | 90/10  | ethernet2 | 1234:2::2 | 00:00:01 |
     |______|_____________|________|___________|___________|__________|
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:17 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:17 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:17 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:17 |
     | D   | 1.1.1.8/30 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:01 |
     | D   | 2.2.2.1/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:17 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:17 |
     | D   | 2.2.2.3/32 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:01 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:18 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:18 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:17 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:17 |
     | D   | 1234:3::/32   | 90/10  | ethernet2 | 1234:2::2 | 00:00:02 |
     | D   | 4321::1/128   | 90/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:18 |
     | D   | 4321::3/128   | 90/10  | ethernet2 | 1234:2::2 | 00:00:02 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

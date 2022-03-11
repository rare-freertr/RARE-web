# Example: eigrp egress delay
    
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
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.1
     as 1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router eigrp4 1 enable
     router eigrp4 1 passive
     router eigrp6 1 enable
     router eigrp6 1 passive
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router eigrp4 1 enable
     router eigrp4 1 passive
     router eigrp6 1 enable
     router eigrp6 1 passive
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
     router eigrp4 1 delay-out 100
     router eigrp6 1 enable
     router eigrp6 1 delay-out 100
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
    logging file debug ../binTmp/zzz49r3-log.run
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
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.3
     as 1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router eigrp4 1 enable
     router eigrp4 1 passive
     router eigrp6 1 enable
     router eigrp6 1 passive
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router eigrp4 1 enable
     router eigrp4 1 passive
     router eigrp6 1 enable
     router eigrp6 1 passive
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    r2#show ipv4 eigrp 1 sum
    r2#show ipv4 eigrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | peer    | learned | adverted | uptime   |
     |-----------|---------|---------|----------|----------|
     | ethernet1 | 1.1.1.1 | 2       | 4        | 00:00:22 |
     | ethernet2 | 1.1.1.6 | 2       | 3        | 00:00:21 |
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
     | ethernet1 | 1234:1::1 | 2       | 4        | 00:00:22 |
     | ethernet2 | 1234:2::2 | 2       | 3        | 00:00:21 |
     |___________|___________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 eigrp 1 rou
    r2#show ipv4 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:22 |
     | C    | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:22 |
     | null | 2.2.2.1/32   | 90/110 | ethernet1 | 1.1.1.1 | 00:00:22 |
     | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:22 |
     | null | 2.2.2.3/32   | 90/10  | ethernet2 | 1.1.1.6 | 00:00:06 |
     | null | 2.2.2.111/32 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:06 |
     |______|______________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 rou
    r2#show ipv6 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:23 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:23 |
     | null | 4321::1/128   | 90/110 | ethernet1 | 1234:1::1 | 00:00:22 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:23 |
     | null | 4321::3/128   | 90/10  | ethernet2 | 1234:2::2 | 00:00:06 |
     | null | 4321::111/128 | 90/10  | ethernet2 | 1234:2::2 | 00:00:06 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop     | time     |
     |-----|--------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:23 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:23 |
     | C   | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:23 |
     | LOC | 1.1.1.5/32   | 0/1    | ethernet2 | null    | 00:00:23 |
     | D   | 2.2.2.1/32   | 90/110 | ethernet1 | 1.1.1.1 | 00:00:22 |
     | C   | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:23 |
     | D   | 2.2.2.3/32   | 90/10  | ethernet2 | 1.1.1.6 | 00:00:07 |
     | D   | 2.2.2.111/32 | 90/10  | ethernet2 | 1.1.1.6 | 00:00:07 |
     |_____|______________|________|___________|_________|__________|
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:23 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:23 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:23 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:23 |
     | D   | 4321::1/128   | 90/110 | ethernet1 | 1234:1::1 | 00:00:22 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:23 |
     | D   | 4321::3/128   | 90/10  | ethernet2 | 1234:2::2 | 00:00:07 |
     | D   | 4321::111/128 | 90/10  | ethernet2 | 1234:2::2 | 00:00:07 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

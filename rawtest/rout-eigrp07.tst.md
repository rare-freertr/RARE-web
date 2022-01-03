# Example: eigrp ingress route filtering with prefixlist
    
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
    prefix-list p4
     sequence 10 deny 2.2.2.12/32 ge 32 le 32
     sequence 20 permit 0.0.0.0/0 ge 0 le 32
     exit
    !
    prefix-list p6
     sequence 10 deny 4321::12/128 ge 128 le 128
     sequence 20 permit ::/0 ge 0 le 128
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.21 255.255.255.255
     ipv6 address 4321::21 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     router eigrp4 1 prefix-list-in p4
     router eigrp6 1 enable
     router eigrp6 1 prefix-list-in p6
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.22 255.255.255.255
     ipv6 address 4321::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
     | ethernet1 | 1.1.1.1 | 3       | 3        | 00:00:16 |
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
     | ethernet1 | 1234:1::1 | 3       | 3        | 00:00:16 |
     |___________|___________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 eigrp 1 rou
    r2#show ipv4 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30  | 0/0    | ethernet1 | null    | 00:00:17 |
     | null | 2.2.2.1/32  | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C    | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:17 |
     | null | 2.2.2.11/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C    | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:17 |
     | null | 2.2.2.21/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C    | 2.2.2.22/32 | 0/0    | loopback2 | null    | 00:00:17 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 rou
    r2#show ipv6 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop       | time     |
     |------|--------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32  | 0/0    | ethernet1 | null      | 00:00:17 |
     | null | 4321::1/128  | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128  | 0/0    | loopback0 | null      | 00:00:17 |
     | null | 4321::11/128 | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::12/128 | 0/0    | loopback1 | null      | 00:00:17 |
     | null | 4321::21/128 | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::22/128 | 0/0    | loopback2 | null      | 00:00:17 |
     |______|______________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30  | 0/0    | ethernet1 | null    | 00:00:18 |
     | LOC | 1.1.1.2/32  | 0/1    | ethernet1 | null    | 00:00:18 |
     | D   | 2.2.2.1/32  | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C   | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:18 |
     | D   | 2.2.2.11/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C   | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:18 |
     | D   | 2.2.2.21/32 | 90/10  | ethernet1 | 1.1.1.1 | 00:00:16 |
     | C   | 2.2.2.22/32 | 0/0    | loopback2 | null    | 00:00:18 |
     |_____|_____________|________|___________|_________|__________|
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
     | D   | 4321::1/128   | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null      | 00:00:18 |
     | D   | 4321::11/128  | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C   | 4321::12/128  | 0/0    | loopback1 | null      | 00:00:18 |
     | D   | 4321::21/128  | 90/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C   | 4321::22/128  | 0/0    | loopback2 | null      | 00:00:18 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

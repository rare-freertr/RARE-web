# Example: eigrp over point2point ethernet
    
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
     ipv4 address 1.1.1.3 255.255.255.254
     ipv6 address 1234::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
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
     ipv4 address 1.1.1.2 255.255.255.254
     ipv6 address 1234::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
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
     | ethernet1 | 1.1.1.3 | 1       | 1        | 00:00:15 |
     |___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 sum
    r2#show ipv6 eigrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | peer    | learned | adverted | uptime   |
     |-----------|---------|---------|----------|----------|
     | ethernet1 | 1234::3 | 1       | 1        | 00:00:15 |
     |___________|_________|_________|__________|__________|
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
     | C    | 1.1.1.2/31 | 0/0    | ethernet1 | null    | 00:00:16 |
     | null | 2.2.2.1/32 | 90/10  | ethernet1 | 1.1.1.3 | 00:00:15 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:16 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 rou
    r2#show ipv6 eigrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | C    | 1234::2/127 | 0/0    | ethernet1 | null    | 00:00:16 |
     | null | 4321::1/128 | 90/10  | ethernet1 | 1234::3 | 00:00:00 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:16 |
     |______|_____________|________|___________|_________|__________|
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
     | C   | 1.1.1.2/31 | 0/0    | ethernet1 | null    | 00:00:16 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:16 |
     | D   | 2.2.2.1/32 | 90/10  | ethernet1 | 1.1.1.3 | 00:00:16 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:16 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 1234::2/127 | 0/0    | ethernet1 | null    | 00:00:16 |
     | LOC | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:16 |
     | D   | 4321::1/128 | 90/10  | ethernet1 | 1234::3 | 00:00:01 |
     | C   | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:16 |
     |_____|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

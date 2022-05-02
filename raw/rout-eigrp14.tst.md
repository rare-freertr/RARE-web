# Example: eigrp with bfd
    
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
    logging file debug ../binTmp/zzz32r1-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router eigrp4 1 enable
     router eigrp4 1 bfd
     router eigrp6 1 enable
     router eigrp6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router eigrp4 1 enable
     router eigrp4 1 bfd
     router eigrp4 1 delay-in 100
     router eigrp6 1 enable
     router eigrp6 1 bfd
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
    logging file debug ../binTmp/zzz32r2-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router eigrp4 1 enable
     router eigrp4 1 bfd
     router eigrp6 1 enable
     router eigrp6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router eigrp4 1 enable
     router eigrp4 1 bfd
     router eigrp4 1 delay-in 100
     router eigrp6 1 enable
     router eigrp6 1 bfd
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
     | ethernet2 | 1.1.1.5 | 2       | 1        | 00:00:07 |
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
     | ethernet2 | 1234:2::1 | 2       | 1        | 00:00:07 |
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
     | null | 1.1.1.0/30 | 90/100 | ethernet2 | 1.1.1.5 | 00:00:02 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:02 |
     | null | 2.2.2.1/32 | 90/100 | ethernet2 | 1.1.1.5 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:02 |
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
     | null | 1234:1::/32 | 90/100 | ethernet2 | 1234:2::1 | 00:00:02 |
     | C    | 1234:2::/32 | 0/0    | ethernet2 | null      | 00:00:02 |
     | null | 4321::1/128 | 90/100 | ethernet2 | 1234:2::1 | 00:00:02 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null      | 00:00:02 |
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
     | D   | 1.1.1.0/30 | 90/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:07 |
     | LOC | 1.1.1.6/32 | 0/1    | ethernet2 | null    | 00:00:07 |
     | D   | 2.2.2.1/32 | 90/100 | ethernet2 | 1.1.1.5 | 00:00:07 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:08 |
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
     | D   | 1234:1::/32   | 90/100 | ethernet2 | 1234:2::1 | 00:00:07 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:08 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:08 |
     | D   | 4321::1/128   | 90/100 | ethernet2 | 1234:2::1 | 00:00:07 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:08 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

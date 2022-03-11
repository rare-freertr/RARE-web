# Example: eigrp point2multipoint connection
    
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
    logging file debug ../binTmp/zzz14r1-log.run
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
    logging file debug ../binTmp/zzz14r2-log.run
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
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
    logging file debug ../binTmp/zzz14r3-log.run
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234::3 ffff::
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
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
    logging file debug ../binTmp/zzz14r4-log.run
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
    router eigrp4 1
     vrf v1
     router-id 4.4.4.4
     as 1
     redistribute connected
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.4
     as 1
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.0
     ipv6 address 1234::4 ffff::
     router eigrp4 1 enable
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
    r2#show ipv4 eigrp 1 sum
    r2#show ipv4 eigrp 1 sum
     |~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface | peer    | learned | adverted | uptime   |
     |-------|---------|---------|----------|----------|
     | bvi1  | 1.1.1.1 | 1       | 1        | 00:00:05 |
     | bvi1  | 1.1.1.3 | 1       | 1        | 00:00:04 |
     | bvi1  | 1.1.1.4 | 1       | 1        | 00:00:04 |
     |_______|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 sum
    r2#show ipv6 eigrp 1 sum
     |~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface | peer    | learned | adverted | uptime   |
     |-------|---------|---------|----------|----------|
     | bvi1  | 1234::1 | 1       | 1        | 00:00:05 |
     | bvi1  | 1234::3 | 1       | 1        | 00:00:05 |
     | bvi1  | 1234::4 | 1       | 1        | 00:00:05 |
     |_______|_________|_________|__________|__________|
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
     | C    | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:06 |
     | null | 2.2.2.1/32 | 90/10  | bvi1      | 1.1.1.1 | 00:00:05 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:06 |
     | null | 2.2.2.3/32 | 90/10  | bvi1      | 1.1.1.3 | 00:00:05 |
     | null | 2.2.2.4/32 | 90/10  | bvi1      | 1.1.1.4 | 00:00:05 |
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
     | C    | 1234::/16   | 0/0    | bvi1      | null    | 00:00:06 |
     | null | 4321::1/128 | 90/10  | bvi1      | 1234::1 | 00:00:05 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:06 |
     | null | 4321::3/128 | 90/10  | bvi1      | 1234::3 | 00:00:05 |
     | null | 4321::4/128 | 90/10  | bvi1      | 1234::4 | 00:00:05 |
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
     | C   | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:06 |
     | LOC | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:06 |
     | D   | 2.2.2.1/32 | 90/10  | bvi1      | 1.1.1.1 | 00:00:05 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:06 |
     | D   | 2.2.2.3/32 | 90/10  | bvi1      | 1.1.1.3 | 00:00:05 |
     | D   | 2.2.2.4/32 | 90/10  | bvi1      | 1.1.1.4 | 00:00:05 |
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
     | C   | 1234::/16   | 0/0    | bvi1      | null    | 00:00:06 |
     | LOC | 1234::2/128 | 0/1    | bvi1      | null    | 00:00:06 |
     | D   | 4321::1/128 | 90/10  | bvi1      | 1234::1 | 00:00:06 |
     | C   | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:06 |
     | D   | 4321::3/128 | 90/10  | bvi1      | 1234::3 | 00:00:05 |
     | D   | 4321::4/128 | 90/10  | bvi1      | 1234::4 | 00:00:05 |
     |_____|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

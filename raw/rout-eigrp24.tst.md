# Example: eigrp default address suppression
    
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
    logging file debug ../binTmp/zzz36r1-log.run
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
     suppress-prefix
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.1
     as 1
     suppress-prefix
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
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz36r2-log.run
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
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.2
     as 1
     exit
    !
    interface loopback1
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
     | ethernet1 | 1.1.1.1 | 0       | 1        | 00:00:15 |
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
     | ethernet1 | 1234:1::1 | 0       | 1        | 00:00:16 |
     |___________|___________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 eigrp 1 rou
    r2#show ipv4 eigrp 1 rou
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop  | time     |
     |-----|--------------|--------|-----------|------|----------|
     | C   | 1.1.1.0/30   | 1/0    | ethernet1 | null | 00:00:16 |
     | C   | 2.2.2.111/32 | 1/0    | loopback1 | null | 00:00:16 |
     |_____|______________|________|___________|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 eigrp 1 rou
    r2#show ipv6 eigrp 1 rou
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface     | hop  | time     |
     |-----|---------------|--------|-----------|------|----------|
     | C   | 1234:1::/32   | 1/0    | ethernet1 | null | 00:00:17 |
     | C   | 4321::111/128 | 1/0    | loopback1 | null | 00:00:17 |
     |_____|_______________|________|___________|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop  | time     |
     |-----|--------------|--------|-----------|------|----------|
     | C   | 1.1.1.0/30   | 0/0    | ethernet1 | null | 00:00:17 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null | 00:00:17 |
     | C   | 2.2.2.111/32 | 0/0    | loopback1 | null | 00:00:17 |
     |_____|______________|________|___________|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface     | hop  | time     |
     |-----|---------------|--------|-----------|------|----------|
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null | 00:00:17 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null | 00:00:17 |
     | C   | 4321::111/128 | 0/0    | loopback1 | null | 00:00:17 |
     |_____|_______________|________|___________|______|__________|
    r2#
    r2#
    ```

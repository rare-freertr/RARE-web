# Example: pvrp autoroute
    
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
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
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
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::1 ffff::
     ipv6 access-group-in test6
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface serial2
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.8.1 255.255.255.0
     ipv4 autoroute pvrp4 1 2.2.2.2 9.9.8.2
     ipv6 address 9998::1 ffff::
     ipv6 autoroute pvrp6 1 4321::2 9998::2
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
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.2
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
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
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::2 ffff::
     ipv6 access-group-in test6
     router pvrp4 1 enable
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface serial2
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.8.2 255.255.255.0
     ipv4 autoroute pvrp4 1 2.2.2.1 9.9.8.1
     ipv6 address 9998::2 ffff::
     ipv6 autoroute pvrp6 1 4321::1 9998::1
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
    r2#show ipv4 pvrp 1 sum
    r2#show ipv4 pvrp 1 sum
     |~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface   | router  | name | peerif  | peer    | learned | adverted | uptime   |
     |---------|---------|------|---------|---------|---------|----------|----------|
     | serial1 | 4.4.4.1 | r1   | serial1 | 9.9.9.1 | 3       | 3        | 00:00:25 |
     |_________|_________|______|_________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 sum
    r2#show ipv6 pvrp 1 sum
     |~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface   | router  | name | peerif  | peer    | learned | adverted | uptime   |
     |---------|---------|------|---------|---------|---------|----------|----------|
     | serial1 | 6.6.6.1 | r1   | serial1 | 9999::1 | 3       | 3        | 00:00:25 |
     |_________|_________|______|_________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 pvrp 1 rou
    r2#show ipv4 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | null | 2.2.2.1/32  | 80/10  | serial1   | 9.9.9.1 | 00:00:22 |
     | C    | 2.2.2.2/32  | 2/0    | loopback0 | null    | 00:00:26 |
     | null | 2.2.2.11/32 | 80/10  | serial1   | 9.9.9.1 | 00:00:22 |
     | C    | 2.2.2.12/32 | 2/0    | loopback1 | null    | 00:00:26 |
     | C    | 9.9.8.0/24  | 2/0    | serial2   | null    | 00:00:26 |
     | C    | 9.9.9.0/24  | 1/0    | serial1   | null    | 00:00:22 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 rou
    r2#show ipv6 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | null | 4321::1/128  | 80/10  | serial1   | 9999::1 | 00:00:21 |
     | C    | 4321::2/128  | 2/0    | loopback0 | null    | 00:00:27 |
     | null | 4321::11/128 | 80/10  | serial1   | 9999::1 | 00:00:21 |
     | C    | 4321::12/128 | 2/0    | loopback1 | null    | 00:00:27 |
     | C    | 9998::/16    | 2/0    | serial2   | null    | 00:00:27 |
     | C    | 9999::/16    | 1/0    | serial1   | null    | 00:00:21 |
     |______|______________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | P EX | 2.2.2.1/32  | 80/10  | serial2   | 9.9.8.1 | 00:00:22 |
     | C    | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:30 |
     | P EX | 2.2.2.11/32 | 80/10  | serial2   | 9.9.8.1 | 00:00:22 |
     | C    | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:30 |
     | C    | 9.9.8.0/24  | 0/0    | serial2   | null    | 00:00:27 |
     | LOC  | 9.9.8.2/32  | 0/1    | serial2   | null    | 00:00:27 |
     | C    | 9.9.9.0/24  | 0/0    | serial1   | null    | 00:00:27 |
     | LOC  | 9.9.9.2/32  | 0/1    | serial1   | null    | 00:00:27 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | P EX | 4321::1/128  | 80/10  | serial2   | 9998::1 | 00:00:21 |
     | C    | 4321::2/128  | 0/0    | loopback0 | null    | 00:00:30 |
     | P EX | 4321::11/128 | 80/10  | serial2   | 9998::1 | 00:00:21 |
     | C    | 4321::12/128 | 0/0    | loopback1 | null    | 00:00:30 |
     | C    | 9998::/16    | 0/0    | serial2   | null    | 00:00:27 |
     | LOC  | 9998::2/128  | 0/1    | serial2   | null    | 00:00:27 |
     | C    | 9999::/16    | 0/0    | serial1   | null    | 00:00:27 |
     | LOC  | 9999::2/128  | 0/1    | serial1   | null    | 00:00:27 |
     |______|______________|________|___________|_________|__________|
    r2#
    r2#
    ```

# Example: babel max metric
    
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
    router babel4 1
     vrf v1
     router-id 1111-2222-3333-0001
     redistribute connected
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0001
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router babel4 1 enable
     router babel6 1 enable
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
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric add 40000
     !
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router babel4 1
     vrf v1
     router-id 1111-2222-3333-0002
     redistribute connected
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0002
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router babel4 1 enable
     router babel4 1 route-map-in rm1
     router babel4 1 route-map-out rm1
     router babel6 1 enable
     router babel6 1 route-map-in rm1
     router babel6 1 route-map-out rm1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router babel4 1 enable
     router babel4 1 route-map-in rm1
     router babel4 1 route-map-out rm1
     router babel6 1 enable
     router babel6 1 route-map-in rm1
     router babel6 1 route-map-out rm1
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
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router babel4 1
     vrf v1
     router-id 1111-2222-3333-0003
     redistribute connected
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0003
     redistribute connected
     exit
    !
    interface loopback0
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
     router babel4 1 enable
     router babel6 1 enable
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
    r2#show ipv4 babel 1 sum
    r2#show ipv4 babel 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor | uptime   |
     |-----------|-------|----------|----------|
     | ethernet1 | 2     | 1.1.1.1  | 00:00:07 |
     | ethernet2 | 2     | 1.1.1.6  | 00:00:06 |
     |___________|_______|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 babel 1 sum
    r2#show ipv6 babel 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor  | uptime   |
     |-----------|-------|-----------|----------|
     | ethernet1 | 2     | 1234:1::1 | 00:00:07 |
     | ethernet2 | 2     | 1234:2::2 | 00:00:26 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 babel 1 dat
    r2#show ipv4 babel 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric    | iface     | hop     | time     |
     |-----|------------|-----------|-----------|---------|----------|
     | A   | 1.1.1.0/30 | 1/0       | ethernet1 | null    | 00:00:27 |
     | A   | 1.1.1.4/30 | 1/0       | ethernet2 | null    | 00:00:27 |
     | A   | 2.2.2.1/32 | 130/40100 | ethernet1 | 1.1.1.1 | 00:00:07 |
     | A   | 2.2.2.3/32 | 130/40100 | ethernet2 | 1.1.1.6 | 00:00:07 |
     |_____|____________|___________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 babel 1 dat
    r2#show ipv6 babel 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric    | iface     | hop       | time     |
     |-----|-------------|-----------|-----------|-----------|----------|
     | A   | 1234:1::/32 | 1/0       | ethernet1 | null      | 00:00:27 |
     | A   | 1234:2::/32 | 1/0       | ethernet2 | null      | 00:00:27 |
     | A   | 4321::1/128 | 130/40100 | ethernet1 | 1234:1::1 | 00:00:07 |
     | A   | 4321::3/128 | 130/40100 | ethernet2 | 1234:2::2 | 00:00:27 |
     |_____|_____________|___________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric    | iface     | hop     | time     |
     |-----|------------|-----------|-----------|---------|----------|
     | C   | 1.1.1.0/30 | 0/0       | ethernet1 | null    | 00:00:27 |
     | LOC | 1.1.1.2/32 | 0/1       | ethernet1 | null    | 00:00:27 |
     | C   | 1.1.1.4/30 | 0/0       | ethernet2 | null    | 00:00:27 |
     | LOC | 1.1.1.5/32 | 0/1       | ethernet2 | null    | 00:00:27 |
     | A   | 2.2.2.1/32 | 130/40100 | ethernet1 | 1.1.1.1 | 00:00:08 |
     | C   | 2.2.2.2/32 | 0/0       | loopback0 | null    | 00:00:28 |
     | A   | 2.2.2.3/32 | 130/40100 | ethernet2 | 1.1.1.6 | 00:00:07 |
     |_____|____________|___________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric    | iface     | hop       | time     |
     |-----|---------------|-----------|-----------|-----------|----------|
     | C   | 1234:1::/32   | 0/0       | ethernet1 | null      | 00:00:27 |
     | LOC | 1234:1::2/128 | 0/1       | ethernet1 | null      | 00:00:27 |
     | C   | 1234:2::/32   | 0/0       | ethernet2 | null      | 00:00:27 |
     | LOC | 1234:2::1/128 | 0/1       | ethernet2 | null      | 00:00:27 |
     | A   | 4321::1/128   | 130/40100 | ethernet1 | 1234:1::1 | 00:00:08 |
     | C   | 4321::2/128   | 0/0       | loopback0 | null      | 00:00:28 |
     | A   | 4321::3/128   | 130/40100 | ethernet2 | 1234:2::2 | 00:00:27 |
     |_____|_______________|___________|___________|___________|__________|
    r2#
    r2#
    ```

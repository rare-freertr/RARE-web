# Example: babel default address suppression
    
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
     suppress-prefix
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0001
     suppress-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router babel4 1 enable
     router babel6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router babel4 1 enable
     router babel6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.21 255.255.255.255
     ipv6 address 4321::21 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router babel4 1 enable
     router babel6 1 enable
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
     | ethernet1 | 0     | 1.1.1.1  | 00:00:03 |
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
     | ethernet1 | 0     | 1234:1::1 | 00:00:03 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 babel 1 dat
    r2#show ipv4 babel 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop  | time     |
     |-----|------------|--------|-----------|------|----------|
     | A   | 1.1.1.0/30 | 1/0    | ethernet1 | null | 00:00:23 |
     |_____|____________|________|___________|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 babel 1 dat
    r2#show ipv6 babel 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop  | time     |
     |-----|-------------|--------|-----------|------|----------|
     | A   | 1234:1::/32 | 1/0    | ethernet1 | null | 00:00:23 |
     |_____|_____________|________|___________|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop  | time     |
     |-----|-------------|--------|-----------|------|----------|
     | C   | 1.1.1.0/30  | 0/0    | ethernet1 | null | 00:00:24 |
     | LOC | 1.1.1.2/32  | 0/1    | ethernet1 | null | 00:00:24 |
     | C   | 2.2.2.2/32  | 0/0    | loopback0 | null | 00:00:24 |
     | C   | 2.2.2.12/32 | 0/0    | loopback1 | null | 00:00:24 |
     | C   | 2.2.2.22/32 | 0/0    | loopback2 | null | 00:00:24 |
     |_____|_____________|________|___________|______|__________|
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null | 00:00:24 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null | 00:00:24 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null | 00:00:24 |
     | C   | 4321::12/128  | 0/0    | loopback1 | null | 00:00:24 |
     | C   | 4321::22/128  | 0/0    | loopback2 | null | 00:00:24 |
     |_____|_______________|________|___________|______|__________|
    r2#
    r2#
    ```

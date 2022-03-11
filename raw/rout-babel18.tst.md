# Example: babel with bfd
    
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
    logging file debug ../binTmp/zzz45r1-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router babel4 1 enable
     router babel4 1 bfd
     router babel6 1 enable
     router babel6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::1 ffff:ffff::
     ipv6 bfd 100 100 3
     router babel4 1 enable
     router babel4 1 bfd
     router babel4 1 distance 140
     router babel6 1 enable
     router babel6 1 bfd
     router babel6 1 distance 140
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
    logging file debug ../binTmp/zzz45r2-log.run
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
     ipv4 bfd 100 100 3
     ipv6 address 1234:1::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router babel4 1 enable
     router babel4 1 bfd
     router babel6 1 enable
     router babel6 1 bfd
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv4 bfd 100 100 3
     ipv6 address 1234:2::2 ffff:ffff::
     ipv6 bfd 100 100 3
     router babel4 1 enable
     router babel4 1 bfd
     router babel4 1 distance 140
     router babel6 1 enable
     router babel6 1 bfd
     router babel6 1 distance 140
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
     | ethernet2 | 4     | 1.1.1.5  | 00:00:08 |
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
     | ethernet2 | 4     | 1234:2::1 | 00:00:08 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 babel 1 dat
    r2#show ipv4 babel 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric  | iface     | hop     | time     |
     |-----|------------|---------|-----------|---------|----------|
     | A   | 1.1.1.0/30 | 140/100 | ethernet2 | 1.1.1.5 | 00:00:08 |
     | A   | 1.1.1.4/30 | 1/0     | ethernet2 | null    | 00:00:29 |
     | A   | 2.2.2.1/32 | 140/100 | ethernet2 | 1.1.1.5 | 00:00:08 |
     | A   | 2.2.2.2/32 | 140/200 | ethernet2 | 1.1.1.5 | 00:00:08 |
     |_____|____________|_________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 babel 1 dat
    r2#show ipv6 babel 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric  | iface     | hop       | time     |
     |-----|-------------|---------|-----------|-----------|----------|
     | A   | 1234:1::/32 | 140/100 | ethernet2 | 1234:2::1 | 00:00:09 |
     | A   | 1234:2::/32 | 1/0     | ethernet2 | null      | 00:00:29 |
     | A   | 4321::1/128 | 140/100 | ethernet2 | 1234:2::1 | 00:00:09 |
     | A   | 4321::2/128 | 140/200 | ethernet2 | 1234:2::1 | 00:00:09 |
     |_____|_____________|_________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric  | iface     | hop     | time     |
     |-----|------------|---------|-----------|---------|----------|
     | A   | 1.1.1.0/30 | 140/100 | ethernet2 | 1.1.1.5 | 00:00:09 |
     | C   | 1.1.1.4/30 | 0/0     | ethernet2 | null    | 00:00:30 |
     | LOC | 1.1.1.6/32 | 0/1     | ethernet2 | null    | 00:00:30 |
     | A   | 2.2.2.1/32 | 140/100 | ethernet2 | 1.1.1.5 | 00:00:09 |
     | C   | 2.2.2.2/32 | 0/0     | loopback1 | null    | 00:00:30 |
     |_____|____________|_________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric  | iface     | hop       | time     |
     |-----|---------------|---------|-----------|-----------|----------|
     | A   | 1234:1::/32   | 140/100 | ethernet2 | 1234:2::1 | 00:00:09 |
     | C   | 1234:2::/32   | 0/0     | ethernet2 | null      | 00:00:30 |
     | LOC | 1234:2::2/128 | 0/1     | ethernet2 | null      | 00:00:30 |
     | A   | 4321::1/128   | 140/100 | ethernet2 | 1234:2::1 | 00:00:09 |
     | C   | 4321::2/128   | 0/0     | loopback1 | null      | 00:00:31 |
     |_____|_______________|_________|___________|___________|__________|
    r2#
    r2#
    ```

# Example: olsr with bfd
    
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
    logging file debug ../binTmp/zzz48r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
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
     router olsr4 1 enable
     router olsr4 1 bfd
     router olsr6 1 enable
     router olsr6 1 bfd
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
     router olsr4 1 enable
     router olsr4 1 bfd
     router olsr4 1 distance 150
     router olsr6 1 enable
     router olsr6 1 bfd
     router olsr6 1 distance 150
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
    logging file debug ../binTmp/zzz48r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
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
     router olsr4 1 enable
     router olsr4 1 bfd
     router olsr6 1 enable
     router olsr6 1 bfd
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
     router olsr4 1 enable
     router olsr4 1 bfd
     router olsr4 1 distance 150
     router olsr6 1 enable
     router olsr6 1 bfd
     router olsr6 1 distance 150
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
    r2#show ipv4 olsr 1 sum
    r2#show ipv4 olsr 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor | uptime   |
     |-----------|-------|----------|----------|
     | ethernet2 | 4     | 1.1.1.5  | 00:00:31 |
     |___________|_______|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 sum
    r2#show ipv6 olsr 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor  | uptime   |
     |-----------|-------|-----------|----------|
     | ethernet2 | 4     | 1234:2::1 | 00:00:31 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 olsr 1 dat
    r2#show ipv4 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | N   | 1.1.1.0/30 | 150/1  | ethernet2 | 1.1.1.5 | 00:00:06 |
     | N   | 1.1.1.4/30 | 1/0    | ethernet2 | null    | 00:00:36 |
     | N   | 2.2.2.1/32 | 150/1  | ethernet2 | 1.1.1.5 | 00:00:06 |
     | N   | 2.2.2.2/32 | 150/2  | ethernet2 | 1.1.1.5 | 00:00:06 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1
    r2#show ipv6 olsr 1
    r2#show ipv6 olsr 1 dat
    r2#show ipv6 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop       | time     |
     |-----|-------------|--------|-----------|-----------|----------|
     | N   | 1234:1::/32 | 150/1  | ethernet2 | 1234:2::1 | 00:00:06 |
     | N   | 1234:2::/32 | 1/0    | ethernet2 | null      | 00:00:36 |
     | N   | 4321::1/128 | 150/1  | ethernet2 | 1234:2::1 | 00:00:06 |
     | N   | 4321::2/128 | 150/2  | ethernet2 | 1234:2::1 | 00:00:06 |
     |_____|_____________|________|___________|___________|__________|
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
     | N   | 1.1.1.0/30 | 150/1  | ethernet2 | 1.1.1.5 | 00:00:06 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:36 |
     | LOC | 1.1.1.6/32 | 0/1    | ethernet2 | null    | 00:00:36 |
     | N   | 2.2.2.1/32 | 150/1  | ethernet2 | 1.1.1.5 | 00:00:06 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:37 |
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
     | N   | 1234:1::/32   | 150/1  | ethernet2 | 1234:2::1 | 00:00:06 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:36 |
     | LOC | 1234:2::2/128 | 0/1    | ethernet2 | null      | 00:00:36 |
     | N   | 4321::1/128   | 150/1  | ethernet2 | 1234:2::1 | 00:00:06 |
     | C   | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:37 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

# Example: olsr ecmp connection
    
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
    router olsr4 1
     vrf v1
     redistribute connected
     ecmp
     exit
    !
    router olsr6 1
     vrf v1
     redistribute connected
     ecmp
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:21::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.10 255.255.255.252
     ipv6 address 1234:23::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
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
    router olsr4 1
     vrf v1
     redistribute connected
     ecmp
     exit
    !
    router olsr6 1
     vrf v1
     redistribute connected
     ecmp
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:21::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.252
     ipv6 address 1234:22::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
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
    router olsr4 1
     vrf v1
     redistribute connected
     ecmp
     exit
    !
    router olsr6 1
     vrf v1
     redistribute connected
     ecmp
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
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.252
     ipv6 address 1234:22::2 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.9 255.255.255.252
     ipv6 address 1234:23::1 ffff:ffff::
     router olsr4 1 enable
     router olsr6 1 enable
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
     |~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | interface    | learn | neighbor | uptime   |
     |--------------|-------|----------|----------|
     | ethernet1.11 | 7     | 1.1.1.1  | 00:00:39 |
     | ethernet1.22 | 9     | 1.1.2.1  | 00:00:39 |
     | ethernet2.11 | 8     | 1.1.1.6  | 00:00:39 |
     | ethernet2.22 | 7     | 1.1.2.6  | 00:00:39 |
     |______________|_______|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 sum
    r2#show ipv6 olsr 1 sum
     |~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | interface    | learn | neighbor   | uptime   |
     |--------------|-------|------------|----------|
     | ethernet1.11 | 6     | 1234:1::1  | 00:00:39 |
     | ethernet1.22 | 9     | 1234:21::1 | 00:00:39 |
     | ethernet2.11 | 8     | 1234:2::2  | 00:00:39 |
     | ethernet2.22 | 8     | 1234:22::2 | 00:00:39 |
     |______________|_______|____________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 olsr 1 dat
    r2#show ipv4 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface        | hop     | time     |
     |-----|------------|--------|--------------|---------|----------|
     | N   | 1.1.1.0/30 | 1/0    | ethernet1.11 | null    | 00:00:45 |
     | N   | 1.1.1.4/30 | 1/0    | ethernet2.11 | null    | 00:00:44 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     | N   | 1.1.2.0/30 | 1/0    | ethernet1.22 | null    | 00:00:44 |
     | N   | 1.1.2.4/30 | 1/0    | ethernet2.22 | null    | 00:00:43 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 2.2.2.2/32 | 140/2  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 2.2.2.2/32 | 140/2  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     |_____|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 dat
    r2#show ipv6 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface        | hop        | time     |
     |-----|--------------|--------|--------------|------------|----------|
     | N   | 1234:1::/32  | 1/0    | ethernet1.11 | null       | 00:00:45 |
     | N   | 1234:2::/32  | 1/0    | ethernet2.11 | null       | 00:00:44 |
     | N   | 1234:3::/32  | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:14 |
     | N   | 1234:3::/32  | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 1234:3::/32  | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 1234:3::/32  | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     | N   | 1234:21::/32 | 1/0    | ethernet1.22 | null       | 00:00:44 |
     | N   | 1234:22::/32 | 1/0    | ethernet2.22 | null       | 00:00:43 |
     | N   | 1234:23::/32 | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:14 |
     | N   | 1234:23::/32 | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 1234:23::/32 | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 1234:23::/32 | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     | N   | 4321::1/128  | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:14 |
     | N   | 4321::1/128  | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 4321::2/128  | 140/2  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 4321::2/128  | 140/2  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 4321::3/128  | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 4321::3/128  | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     |_____|______________|________|______________|____________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface        | hop     | time     |
     |-----|------------|--------|--------------|---------|----------|
     | C   | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:45 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:45 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:44 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:44 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 1.1.1.8/30 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     | C   | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:44 |
     | LOC | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:44 |
     | C   | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:44 |
     | LOC | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:44 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 1.1.2.8/30 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1.11 | 1.1.1.1 | 00:00:14 |
     | N   | 2.2.2.1/32 | 140/1  | ethernet1.22 | 1.1.2.1 | 00:00:14 |
     | C   | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:45 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2.11 | 1.1.1.6 | 00:00:14 |
     | N   | 2.2.2.3/32 | 140/1  | ethernet2.22 | 1.1.2.6 | 00:00:14 |
     |_____|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix         | metric | iface        | hop        | time     |
     |-----|----------------|--------|--------------|------------|----------|
     | C   | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:45 |
     | LOC | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:45 |
     | C   | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:44 |
     | LOC | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:44 |
     | N   | 1234:3::/32    | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:14 |
     | N   | 1234:3::/32    | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 1234:3::/32    | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 1234:3::/32    | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     | C   | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:44 |
     | LOC | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:44 |
     | C   | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:44 |
     | LOC | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:44 |
     | N   | 1234:23::/32   | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:15 |
     | N   | 1234:23::/32   | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | N   | 1234:23::/32   | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 1234:23::/32   | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     | N   | 4321::1/128    | 140/1  | ethernet1.11 | 1234:1::1  | 00:00:14 |
     | N   | 4321::1/128    | 140/1  | ethernet1.22 | 1234:21::1 | 00:00:14 |
     | C   | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:45 |
     | N   | 4321::3/128    | 140/1  | ethernet2.11 | 1234:2::2  | 00:00:14 |
     | N   | 4321::3/128    | 140/1  | ethernet2.22 | 1234:22::2 | 00:00:14 |
     |_____|________________|________|______________|____________|__________|
    r2#
    r2#
    ```

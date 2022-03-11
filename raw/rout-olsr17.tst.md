# Example: olsr outgoing metric with routepolicy
    
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
    logging file debug ../binTmp/zzz83r1-log.run
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
     exit
    !
    router olsr6 1
     vrf v1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    logging file debug ../binTmp/zzz83r2-log.run
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
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz83r3-log.run
    !
    route-policy rm1
     sequence 10 set metric add 200
     sequence 20 pass
     exit
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
     exit
    !
    router olsr6 1
     vrf v1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.111 255.255.255.255
     ipv6 address 4321::111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router olsr4 1 enable
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router olsr4 1 enable
     router olsr4 1 route-policy-out rm1
     router olsr6 1 enable
     router olsr6 1 route-policy-out rm1
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
     | ethernet1 | 2     | 1.1.1.1  | 00:01:06 |
     | ethernet2 | 2     | 1.1.1.6  | 00:01:06 |
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
     | ethernet1 | 2     | 1234:1::1 | 00:01:06 |
     | ethernet2 | 2     | 1234:2::2 | 00:01:06 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 olsr 1 dat
    r2#show ipv4 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric  | iface     | hop     | time     |
     |-----|--------------|---------|-----------|---------|----------|
     | N   | 1.1.1.0/30   | 1/0     | ethernet1 | null    | 00:01:12 |
     | N   | 1.1.1.4/30   | 1/0     | ethernet2 | null    | 00:01:11 |
     | N   | 2.2.2.1/32   | 140/1   | ethernet1 | 1.1.1.1 | 00:00:41 |
     | N   | 2.2.2.3/32   | 140/201 | ethernet2 | 1.1.1.6 | 00:00:41 |
     | N   | 2.2.2.111/32 | 140/1   | ethernet1 | 1.1.1.1 | 00:00:41 |
     |_____|______________|_________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 olsr 1 dat
    r2#show ipv6 olsr 1 dat
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric  | iface     | hop       | time     |
     |-----|---------------|---------|-----------|-----------|----------|
     | N   | 1234:1::/32   | 1/0     | ethernet1 | null      | 00:01:12 |
     | N   | 1234:2::/32   | 1/0     | ethernet2 | null      | 00:01:12 |
     | N   | 4321::1/128   | 140/1   | ethernet1 | 1234:1::1 | 00:00:41 |
     | N   | 4321::3/128   | 140/201 | ethernet2 | 1234:2::2 | 00:00:42 |
     | N   | 4321::111/128 | 140/1   | ethernet1 | 1234:1::1 | 00:00:41 |
     |_____|_______________|_________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric  | iface     | hop     | time     |
     |-----|--------------|---------|-----------|---------|----------|
     | C   | 1.1.1.0/30   | 0/0     | ethernet1 | null    | 00:01:12 |
     | LOC | 1.1.1.2/32   | 0/1     | ethernet1 | null    | 00:01:12 |
     | C   | 1.1.1.4/30   | 0/0     | ethernet2 | null    | 00:01:12 |
     | LOC | 1.1.1.5/32   | 0/1     | ethernet2 | null    | 00:01:12 |
     | N   | 2.2.2.1/32   | 140/1   | ethernet1 | 1.1.1.1 | 00:00:41 |
     | C   | 2.2.2.2/32   | 0/0     | loopback0 | null    | 00:01:12 |
     | N   | 2.2.2.3/32   | 140/201 | ethernet2 | 1.1.1.6 | 00:00:42 |
     | N   | 2.2.2.111/32 | 140/1   | ethernet1 | 1.1.1.1 | 00:00:41 |
     |_____|______________|_________|___________|_________|__________|
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
     | C   | 1234:1::/32   | 0/0     | ethernet1 | null      | 00:01:12 |
     | LOC | 1234:1::2/128 | 0/1     | ethernet1 | null      | 00:01:12 |
     | C   | 1234:2::/32   | 0/0     | ethernet2 | null      | 00:01:12 |
     | LOC | 1234:2::1/128 | 0/1     | ethernet2 | null      | 00:01:12 |
     | N   | 4321::1/128   | 140/1   | ethernet1 | 1234:1::1 | 00:00:41 |
     | C   | 4321::2/128   | 0/0     | loopback0 | null      | 00:01:12 |
     | N   | 4321::3/128   | 140/201 | ethernet2 | 1234:2::2 | 00:00:42 |
     | N   | 4321::111/128 | 140/1   | ethernet1 | 1234:1::1 | 00:00:41 |
     |_____|_______________|_________|___________|___________|__________|
    r2#
    r2#
    ```

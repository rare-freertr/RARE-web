# Example: lsrp prefix movement
    
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
    logging file debug ../binTmp/zzz38r1-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 10
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     advertise 2.2.2.1/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     advertise 4321::1/128 route-map rm1
     advertise 4321::222/128 route-map rm1
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
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    logging file debug ../binTmp/zzz38r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     advertise 2.2.2.2/32
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     advertise 4321::2/128
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    logging file debug ../binTmp/zzz38r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 20
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.3
     advertise 2.2.2.3/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     advertise 4321::3/128 route-map rm1
     advertise 4321::222/128 route-map rm1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.103 255.255.255.255
     ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:27 |
     | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.1.6 | true  | 00:00:27 |
     |___________|_________|______|___________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer      | ready | uptime   |
     |-----------|---------|------|-----------|-----------|-------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:27 |
     | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1234:2::2 | true  | 00:00:27 |
     |___________|_________|______|___________|___________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 dat
    r2#show ipv4 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 4.4.4.1 | r1   | 1   | 3   | 7   | a0e2bfb9 | 00:59:52 |
     | 4.4.4.2 | r2   | 2   | 3   | 7   | 5c38b927 | 00:59:38 |
     | 4.4.4.3 | r3   | 1   | 3   | 5   | 7b7cad5a | 00:59:38 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 dat
    r2#show ipv6 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 6.6.6.1 | r1   | 1   | 3   | 7   | a0e2bfb9 | 00:59:52 |
     | 6.6.6.2 | r2   | 2   | 3   | 7   | 5c38b927 | 00:59:38 |
     | 6.6.6.3 | r3   | 1   | 3   | 5   | 7b7cad5a | 00:59:38 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 tre
    r2#show ipv4 lsrp 1 tre
    `--r2
      |`--r1
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 tre
    r2#show ipv6 lsrp 1 tre
    `--r2
      |`--r1
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30   | 0/0    | ethernet1 | null    | 00:00:33 |
     | LOC  | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:33 |
     | C    | 1.1.1.4/30   | 0/0    | ethernet2 | null    | 00:00:33 |
     | LOC  | 1.1.1.5/32   | 0/1    | ethernet2 | null    | 00:00:33 |
     | L EX | 2.2.2.1/32   | 70/20  | ethernet1 | 1.1.1.1 | 00:00:07 |
     | C    | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:33 |
     | L EX | 2.2.2.3/32   | 70/30  | ethernet2 | 1.1.1.6 | 00:00:22 |
     | L EX | 2.2.2.222/32 | 70/20  | ethernet1 | 1.1.1.1 | 00:00:07 |
     |______|______________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:33 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:33 |
     | C    | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:33 |
     | LOC  | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:33 |
     | L EX | 4321::1/128   | 70/20  | ethernet1 | 1234:1::1 | 00:00:07 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:33 |
     | L EX | 4321::3/128   | 70/30  | ethernet2 | 1234:2::2 | 00:00:22 |
     | L EX | 4321::222/128 | 70/20  | ethernet1 | 1234:1::1 | 00:00:07 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

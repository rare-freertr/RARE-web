# Example: lsrp ecmp connection
    
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
    logging file debug ../binTmp/zzz31r1-log.run
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
     spf-ecmp
     redistribute connected
     ecmp
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     spf-ecmp
     redistribute connected
     ecmp
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
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.252
     ipv6 address 1234:21::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.10 255.255.255.252
     ipv6 address 1234:23::2 ffff:ffff::
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz31r2-log.run
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
     spf-ecmp
     redistribute connected
     ecmp
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     spf-ecmp
     redistribute connected
     ecmp
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.252
     ipv6 address 1234:21::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.5 255.255.255.252
     ipv6 address 1234:22::1 ffff:ffff::
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
    logging file debug ../binTmp/zzz31r3-log.run
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
     spf-ecmp
     redistribute connected
     ecmp
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     spf-ecmp
     redistribute connected
     ecmp
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
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     vrf forwarding v1
     ipv4 address 1.1.2.6 255.255.255.252
     ipv6 address 1234:22::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     vrf forwarding v1
     ipv4 address 1.1.2.9 255.255.255.252
     ipv6 address 1234:23::1 ffff:ffff::
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface        | router  | name | peerif       | peer    | ready | uptime   |
     |--------------|---------|------|--------------|---------|-------|----------|
     | ethernet1.11 | 4.4.4.1 | r1   | ethernet1.11 | 1.1.1.1 | true  | 00:00:07 |
     | ethernet1.22 | 4.4.4.1 | r1   | ethernet1.22 | 1.1.2.1 | true  | 00:00:07 |
     | ethernet2.11 | 4.4.4.3 | r3   | ethernet1.11 | 1.1.1.6 | true  | 00:00:07 |
     | ethernet2.22 | 4.4.4.3 | r3   | ethernet1.22 | 1.1.2.6 | true  | 00:00:07 |
     |______________|_________|______|______________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface        | router  | name | peerif       | peer       | ready | uptime   |
     |--------------|---------|------|--------------|------------|-------|----------|
     | ethernet1.11 | 6.6.6.1 | r1   | ethernet1.11 | 1234:1::1  | true  | 00:00:07 |
     | ethernet1.22 | 6.6.6.1 | r1   | ethernet1.22 | 1234:21::1 | true  | 00:00:07 |
     | ethernet2.11 | 6.6.6.3 | r3   | ethernet1.11 | 1234:2::2  | true  | 00:00:07 |
     | ethernet2.22 | 6.6.6.3 | r3   | ethernet1.22 | 1234:22::2 | true  | 00:00:07 |
     |______________|_________|______|______________|____________|_______|__________|
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
     | 4.4.4.1 | r1   | 4   | 5   | 17  | 7ed99fe9 | 00:59:59 |
     | 4.4.4.2 | r2   | 4   | 5   | 17  | 8a96e185 | 00:59:57 |
     | 4.4.4.3 | r3   | 4   | 5   | 17  | 7ed99fe9 | 00:59:59 |
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
     | 6.6.6.1 | r1   | 4   | 5   | 17  | e41afac4 | 00:59:59 |
     | 6.6.6.2 | r2   | 4   | 5   | 17  | 3242c0f0 | 00:59:59 |
     | 6.6.6.3 | r3   | 4   | 5   | 17  | 370dd675 | 00:59:59 |
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
      |`--r1
      |`--r3
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
      |`--r1
      |`--r3
       `--r3
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface        | hop     | time     |
     |------|------------|--------|--------------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:14 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:14 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:13 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:13 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:03 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:03 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:03 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet2.22 | 1.1.2.6 | 00:00:03 |
     | C    | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:13 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:13 |
     | C    | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:13 |
     | LOC  | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:13 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:03 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:03 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:03 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet2.22 | 1.1.2.6 | 00:00:03 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:03 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:03 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:14 |
     | L EX | 2.2.2.3/32 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:03 |
     | L EX | 2.2.2.3/32 | 70/10  | ethernet2.22 | 1.1.2.6 | 00:00:03 |
     |______|____________|________|______________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix         | metric | iface        | hop        | time     |
     |------|----------------|--------|--------------|------------|----------|
     | C    | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:14 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:14 |
     | C    | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:14 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:14 |
     | L    | 1234:3::/32    | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:04 |
     | L    | 1234:3::/32    | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:04 |
     | L    | 1234:3::/32    | 70/10  | ethernet2.11 | 1234:2::2  | 00:00:04 |
     | L    | 1234:3::/32    | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:04 |
     | C    | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:14 |
     | LOC  | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:14 |
     | C    | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:13 |
     | LOC  | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:13 |
     | L    | 1234:23::/32   | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:01 |
     | L    | 1234:23::/32   | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:01 |
     | L    | 1234:23::/32   | 70/10  | ethernet2.11 | 1234:2::2  | 00:00:01 |
     | L    | 1234:23::/32   | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:01 |
     | L EX | 4321::1/128    | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:04 |
     | L EX | 4321::1/128    | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:04 |
     | C    | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:14 |
     | L EX | 4321::3/128    | 70/10  | ethernet2.11 | 1234:2::2  | 00:00:03 |
     | L EX | 4321::3/128    | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:03 |
     |______|________________|________|______________|____________|__________|
    r2#
    r2#
    ```

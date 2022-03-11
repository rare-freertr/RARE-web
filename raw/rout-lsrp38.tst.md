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
    logging file debug ../binTmp/zzz61r1-log.run
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
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
    logging file debug ../binTmp/zzz61r2-log.run
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
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
    logging file debug ../binTmp/zzz61r3-log.run
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.22
     no description
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.22
     no description
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
     | ethernet1.11 | 4.4.4.1 | r1   | ethernet1.11 | 1.1.1.1 | true  | 00:00:06 |
     | ethernet1.22 | 4.4.4.1 | r1   | ethernet1.22 | 1.1.2.1 | true  | 00:00:06 |
     | ethernet2.11 | 4.4.4.3 | r3   | ethernet1.11 | 1.1.1.6 | true  | 00:00:05 |
     | ethernet2.22 | 4.4.4.3 | null | null         | 1.1.2.6 | false | 00:00:04 |
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
     | ethernet1.11 | 6.6.6.1 | null | null         | 1234:1::1  | false | 00:00:06 |
     | ethernet1.22 | 6.6.6.1 | r1   | ethernet1.22 | 1234:21::1 | true  | 00:00:06 |
     | ethernet2.11 | 6.6.6.3 | null | null         | 1234:2::2  | false | 00:00:05 |
     | ethernet2.22 | 6.6.6.3 | r3   | ethernet1.22 | 1234:22::2 | true  | 00:00:09 |
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
     | 4.4.4.1 | r1   | 4   | 5   | 18  | 4c9c4b55 | 00:59:58 |
     | 4.4.4.2 | r2   | 3   | 5   | 18  | 8f3467aa | 00:59:59 |
     | 4.4.4.3 | r3   | 3   | 5   | 18  | 8f3467aa | 00:59:59 |
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
     | 6.6.6.1 | r1   | 4   | 5   | 18  | 5c234b1b | 00:59:59 |
     | 6.6.6.2 | r2   | 3   | 5   | 18  | 8ef60d9d | 00:59:59 |
     | 6.6.6.3 | r3   | 3   | 5   | 16  | 5de1212c | 00:59:57 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1.11 | null    | 00:00:11 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1.11 | null    | 00:00:11 |
     | C    | 1.1.1.4/30 | 0/0    | ethernet2.11 | null    | 00:00:10 |
     | LOC  | 1.1.1.5/32 | 0/1    | ethernet2.11 | null    | 00:00:10 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:01 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:01 |
     | L    | 1.1.1.8/30 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:01 |
     | C    | 1.1.2.0/30 | 0/0    | ethernet1.22 | null    | 00:00:11 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet1.22 | null    | 00:00:11 |
     | C    | 1.1.2.4/30 | 0/0    | ethernet2.22 | null    | 00:00:10 |
     | LOC  | 1.1.2.5/32 | 0/1    | ethernet2.22 | null    | 00:00:10 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:01 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:01 |
     | L    | 1.1.2.8/30 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:01 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1.11 | 1.1.1.1 | 00:00:02 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1.22 | 1.1.2.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1    | null    | 00:00:11 |
     | L EX | 2.2.2.3/32 | 70/10  | ethernet2.11 | 1.1.1.6 | 00:00:01 |
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
     | C    | 1234:1::/32    | 0/0    | ethernet1.11 | null       | 00:00:11 |
     | LOC  | 1234:1::2/128  | 0/1    | ethernet1.11 | null       | 00:00:11 |
     | C    | 1234:2::/32    | 0/0    | ethernet2.11 | null       | 00:00:10 |
     | LOC  | 1234:2::1/128  | 0/1    | ethernet2.11 | null       | 00:00:10 |
     | L    | 1234:3::/32    | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:00 |
     | L    | 1234:3::/32    | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:00 |
     | L    | 1234:3::/32    | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:00 |
     | C    | 1234:21::/32   | 0/0    | ethernet1.22 | null       | 00:00:11 |
     | LOC  | 1234:21::2/128 | 0/1    | ethernet1.22 | null       | 00:00:11 |
     | C    | 1234:22::/32   | 0/0    | ethernet2.22 | null       | 00:00:10 |
     | LOC  | 1234:22::1/128 | 0/1    | ethernet2.22 | null       | 00:00:10 |
     | L    | 1234:23::/32   | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:05 |
     | L    | 1234:23::/32   | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:05 |
     | L    | 1234:23::/32   | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:05 |
     | L EX | 4321::1/128    | 70/10  | ethernet1.11 | 1234:1::1  | 00:00:04 |
     | L EX | 4321::1/128    | 70/10  | ethernet1.22 | 1234:21::1 | 00:00:04 |
     | C    | 4321::2/128    | 0/0    | loopback1    | null       | 00:00:11 |
     | L EX | 4321::3/128    | 70/10  | ethernet2.22 | 1234:22::2 | 00:00:05 |
     |______|________________|________|______________|____________|__________|
    r2#
    r2#
    ```

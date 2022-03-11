# Example: lsrp tag
    
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
    logging file debug ../binTmp/zzz2r1-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set tag set 1234
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
     redistribute connected route-map rm1
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected route-map rm1
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
    logging file debug ../binTmp/zzz2r2-log.run
    !
    route-map rm1
     sequence 10 action deny
     sequence 10 match tag 1234
     !
     sequence 20 action permit
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
     router-id 4.4.4.2
     route-map rm1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     route-map rm1
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
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz2r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set tag set 1234
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
     redistribute connected route-map rm1
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     redistribute connected route-map rm1
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
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:09 |
     | ethernet2 | 4.4.4.3 | r3   | ethernet1 | 1.1.1.6 | true  | 00:00:09 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:09 |
     | ethernet2 | 6.6.6.3 | r3   | ethernet1 | 1234:2::2 | true  | 00:00:09 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 6   | b8f557ab | 00:59:58 |
     | 4.4.4.2 | r2   | 2   | 3   | 11  | dc37d88d | 00:59:58 |
     | 4.4.4.3 | r3   | 1   | 2   | 7   | bbedb4c9 | 00:59:55 |
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
     | 6.6.6.1 | r1   | 1   | 2   | 7   | bf1864f4 | 00:59:53 |
     | 6.6.6.2 | r2   | 2   | 3   | 11  | 1b1999af | 00:59:58 |
     | 6.6.6.3 | r3   | 1   | 2   | 7   | 8571e860 | 00:59:58 |
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
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop  | time     |
     |-----|------------|--------|-----------|------|----------|
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null | 00:00:15 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null | 00:00:15 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null | 00:00:14 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null | 00:00:14 |
     | C   | 2.2.2.2/32 | 0/0    | loopback0 | null | 00:00:15 |
     |_____|____________|________|___________|______|__________|
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null | 00:00:15 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null | 00:00:15 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null | 00:00:14 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null | 00:00:14 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null | 00:00:15 |
     |_____|_______________|________|___________|______|__________|
    r2#
    r2#
    ```

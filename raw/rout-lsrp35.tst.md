# Example: lsrp peer metric
    
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
     segrout 10 1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     segrout 10 1
     redistribute connected
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     router lsrp4 1 enable
     router lsrp4 1 metric 100
     router lsrp6 1 enable
     router lsrp6 1 metric 100
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1235::1 ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp4 1 metric 1
     router lsrp6 1 enable
     router lsrp6 1 metric 1
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
     segrout 10 2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     segrout 10 2
     redistribute connected
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
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp4 1 accept-metric
     router lsrp4 1 metric 2
     router lsrp6 1 enable
     router lsrp6 1 accept-metric
     router lsrp6 1 metric 2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1235::2 ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp4 1 accept-metric
     router lsrp4 1 metric 200
     router lsrp6 1 enable
     router lsrp6 1 accept-metric
     router lsrp6 1 metric 200
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
     | ethernet1 | 4.4.4.1 | null | null      | 1.1.1.1 | false | 00:00:04 |
     | ethernet2 | 4.4.4.1 | r1   | ethernet2 | 1.1.2.1 | true  | 00:00:04 |
     |___________|_________|______|___________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234::1 | true  | 00:00:04 |
     | ethernet2 | 6.6.6.1 | r1   | ethernet2 | 1235::1 | true  | 00:00:04 |
     |___________|_________|______|___________|_________|_______|__________|
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
     | 4.4.4.1 | r1   | 1   | 3   | 11  | b2f83345 | 00:59:58 |
     | 4.4.4.2 | r2   | 1   | 3   | 10  | 5bd02654 | 00:59:58 |
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
     | 6.6.6.1 | r1   | 2   | 3   | 11  | c68f402a | 00:59:58 |
     | 6.6.6.2 | r2   | 2   | 3   | 11  | c68f402a | 00:59:58 |
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
       `--r1
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
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:10 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:10 |
     | C    | 1.1.2.0/24 | 0/0    | ethernet2 | null    | 00:00:10 |
     | LOC  | 1.1.2.2/32 | 0/1    | ethernet2 | null    | 00:00:10 |
     | L EX | 2.2.2.1/32 | 70/1   | ethernet2 | 1.1.2.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:10 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | C    | 1234::/16   | 0/0    | ethernet1 | null    | 00:00:10 |
     | LOC  | 1234::2/128 | 0/1    | ethernet1 | null    | 00:00:10 |
     | C    | 1235::/16   | 0/0    | ethernet2 | null    | 00:00:10 |
     | LOC  | 1235::2/128 | 0/1    | ethernet2 | null    | 00:00:10 |
     | L EX | 4321::1/128 | 70/1   | ethernet2 | 1235::1 | 00:00:03 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:10 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 segrou v1
    r2#show ipv4 segrou v1
     |~~~~~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|
     | prefix     | index | base   | oldbase |
     |------------|-------|--------|---------|
     | 2.2.2.1/32 | 1     | 155937 | 155937  |
     |____________|_______|________|_________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 segrou v1
    r2#show ipv6 segrou v1
     |~~~~~~~~~~~~~|~~~~~~~|~~~~~~~|~~~~~~~~~|
     | prefix      | index | base  | oldbase |
     |-------------|-------|-------|---------|
     | 4321::1/128 | 1     | 46945 | 46945   |
     |_____________|_______|_______|_________|
    r2#
    r2#
    ```

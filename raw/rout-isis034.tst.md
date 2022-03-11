# Example: isis broadcast subnet with narrow metric
    
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
    logging file debug ../binTmp/zzz23r1-log.run
    !
    bridge 1
     exit
    !
    bridge 2
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.1111.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     no metric-wide
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 network broadcast
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 1234::1 ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 network broadcast
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
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     bridge-group 2
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
    logging file debug ../binTmp/zzz23r2-log.run
    !
    bridge 1
     mac-learn
     exit
    !
    bridge 2
     mac-learn
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.2222.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     no metric-wide
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 network broadcast
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 1234::2 ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 network broadcast
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
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     bridge-group 2
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
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     bridge-group 2
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
    logging file debug ../binTmp/zzz23r3-log.run
    !
    bridge 1
     exit
    !
    bridge 2
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.3333.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.3333.00
     traffeng-id ::
     is-type level2
     no metric-wide
     redistribute connected
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     router isis4 1 enable
     router isis4 1 circuit level2
     router isis4 1 network broadcast
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 1234::3 ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     router isis6 1 network broadcast
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
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     bridge-group 2
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
    r2#show ipv4 isis 1 nei
    r2#show ipv4 isis 1 nei
     |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
     |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
     | bvi1      | 001e.0a7b.6000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:11 |
     | bvi1      | 006e.3844.1f16 | 2     | 4444.0000.3333 | 1.1.1.3    | ::            | up    | 00:00:11 |
     |___________|________________|_______|________________|____________|_______________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 isis 1 nei
    r2#show ipv6 isis 1 nei
     |~~~~~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | interface | mac address    | level | routerid       | ip address | other address | state | uptime   |
     |-----------|----------------|-------|----------------|------------|---------------|-------|----------|
     | bvi2      | 0035.373b.0058 | 2     | 6666.0000.1111 | 1234::1    | ::            | up    | 00:00:11 |
     | bvi2      | 003a.163f.701c | 2     | 6666.0000.3333 | 1234::3    | ::            | up    | 00:00:11 |
     |___________|________________|_______|________________|____________|_______________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 dat 2
    r2#show ipv4 isis 1 dat 2
     |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
     | lspid                | sequence | flags | len | time      |
     |----------------------|----------|-------|-----|-----------|
     | 4444.0000.1111.00-00 | 0000000a | apo   | 53  | 00:19:46  |
     | 4444.0000.1111.7d-00 | 00000002 | apo   | 14  | -00:00:12 |
     | 4444.0000.2222.00-00 | 00000009 | apo   | 53  | 00:19:47  |
     | 4444.0000.2222.3a-00 | 00000002 | apo   | 14  | -00:00:12 |
     | 4444.0000.3333.00-00 | 00000008 | apo   | 53  | 00:19:46  |
     | 4444.0000.3333.72-00 | 00000002 | apo   | 42  | 00:19:47  |
     |______________________|__________|_______|_____|___________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 isis 1 dat 2
    r2#show ipv6 isis 1 dat 2
     |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~|
     | lspid                | sequence | flags | len | time      |
     |----------------------|----------|-------|-----|-----------|
     | 6666.0000.1111.00-00 | 00000008 | apo   | 59  | 00:19:46  |
     | 6666.0000.1111.0c-00 | 00000002 | apo   | 14  | -00:00:12 |
     | 6666.0000.2222.00-00 | 00000007 | apo   | 59  | 00:19:47  |
     | 6666.0000.2222.1b-00 | 00000002 | apo   | 42  | 00:19:47  |
     | 6666.0000.3333.00-00 | 00000007 | apo   | 59  | 00:19:47  |
     | 6666.0000.3333.49-00 | 00000002 | apo   | 14  | -00:00:11 |
     |______________________|__________|_______|_____|___________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 tre 2
    r2#show ipv4 isis 1 tre 2
    `--r2
       `--4444.0000.3333.72
         |`--r3
          `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 isis 1 tre 2
    r2#show ipv6 isis 1 tre 2
    `--r2
       `--6666.0000.2222.1b
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
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/24 | 0/0    | bvi1      | null    | 00:00:13 |
     | LOC  | 1.1.1.2/32 | 0/1    | bvi1      | null    | 00:00:13 |
     | I EX | 2.2.2.1/32 | 115/10 | bvi1      | 1.1.1.1 | 00:00:12 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:13 |
     | I EX | 2.2.2.3/32 | 115/10 | bvi1      | 1.1.1.3 | 00:00:12 |
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
     | C    | 1234::/16   | 0/0    | bvi2      | null    | 00:00:13 |
     | LOC  | 1234::2/128 | 0/1    | bvi2      | null    | 00:00:13 |
     | I EX | 4321::1/128 | 115/10 | bvi2      | 1234::1 | 00:00:12 |
     | C    | 4321::2/128 | 0/0    | loopback1 | null    | 00:00:13 |
     | I EX | 4321::3/128 | 115/10 | bvi2      | 1234::3 | 00:00:12 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```

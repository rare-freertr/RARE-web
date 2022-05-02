# Example: rip egress route filtering with prefixlist
    
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
    logging file debug ../binTmp/zzz50r1-log.run
    !
    prefix-list p4
     sequence 10 deny 2.2.2.11/32 ge 32 le 32
     sequence 20 permit 0.0.0.0/0 ge 0 le 32
     exit
    !
    prefix-list p6
     sequence 10 deny 4321::11/128 ge 128 le 128
     sequence 20 permit ::/0 ge 0 le 128
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router rip4 1
     vrf v1
     redistribute connected
     exit
    !
    router rip6 1
     vrf v1
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.21 255.255.255.255
     ipv6 address 4321::21 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router rip4 1 enable
     router rip4 1 prefix-list-out p4
     router rip6 1 enable
     router rip6 1 prefix-list-out p6
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
    logging file debug ../binTmp/zzz50r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router rip4 1
     vrf v1
     redistribute connected
     exit
    !
    router rip6 1
     vrf v1
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.22 255.255.255.255
     ipv6 address 4321::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router rip4 1 enable
     router rip6 1 enable
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
    r2#show ipv4 rip 1 sum
    r2#show ipv4 rip 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor | uptime   |
     |-----------|-------|----------|----------|
     | ethernet1 | 3     | 1.1.1.1  | 00:00:03 |
     |___________|_______|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 rip 1 sum
    r2#show ipv6 rip 1 sum
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | interface | learn | neighbor  | uptime   |
     |-----------|-------|-----------|----------|
     | ethernet1 | 3     | 1234:1::1 | 00:00:04 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 rip 1 dat
    r2#show ipv4 rip 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | R   | 1.1.1.0/30  | 1/0    | ethernet1 | null    | 00:00:34 |
     | R   | 2.2.2.1/32  | 120/1  | ethernet1 | 1.1.1.1 | 00:00:04 |
     | R   | 2.2.2.21/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:04 |
     |_____|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 rip 1 dat
    r2#show ipv6 rip 1 dat
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop       | time     |
     |-----|--------------|--------|-----------|-----------|----------|
     | R   | 1234:1::/32  | 1/0    | ethernet1 | null      | 00:00:34 |
     | R   | 4321::1/128  | 120/1  | ethernet1 | 1234:1::1 | 00:00:04 |
     | R   | 4321::21/128 | 120/1  | ethernet1 | 1234:1::1 | 00:00:04 |
     |_____|______________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30  | 0/0    | ethernet1 | null    | 00:00:34 |
     | LOC | 1.1.1.2/32  | 0/1    | ethernet1 | null    | 00:00:34 |
     | R   | 2.2.2.1/32  | 120/1  | ethernet1 | 1.1.1.1 | 00:00:04 |
     | C   | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:34 |
     | C   | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:34 |
     | R   | 2.2.2.21/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:04 |
     | C   | 2.2.2.22/32 | 0/0    | loopback2 | null    | 00:00:34 |
     |_____|_____________|________|___________|_________|__________|
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:34 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:34 |
     | R   | 4321::1/128   | 120/1  | ethernet1 | 1234:1::1 | 00:00:04 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null      | 00:00:35 |
     | C   | 4321::12/128  | 0/0    | loopback1 | null      | 00:00:35 |
     | R   | 4321::21/128  | 120/1  | ethernet1 | 1234:1::1 | 00:00:04 |
     | C   | 4321::22/128  | 0/0    | loopback2 | null      | 00:00:35 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

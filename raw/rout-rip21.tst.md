# Example: rip peer template
    
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
    interface template1
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router rip4 1 enable
     router rip6 1 enable
     no shutdown
     no log-link-change
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     template template1
     no shutdown
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
    interface template1
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.0
     ipv6 address 9999::9 ffff::
     router rip4 1 enable
     router rip6 1 enable
     no shutdown
     no log-link-change
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     template template1
     no shutdown
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
     | ethernet1 | 3     | 1.1.1.1  | 00:00:33 |
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
     | ethernet1 | 3     | 1234:1::1 | 00:00:03 |
     |___________|_______|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 rip 1 dat
    r2#show ipv4 rip 1 dat
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | R   | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:33 |
     | R   | 2.2.2.1/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:33 |
     | R   | 9.9.9.0/24 | 1/0    | template1 | null    | 00:00:33 |
     |_____|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 rip 1 dat
    r2#show ipv6 rip 1 dat
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop       | time     |
     |-----|-------------|--------|-----------|-----------|----------|
     | R   | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:33 |
     | R   | 4321::1/128 | 120/1  | ethernet1 | 1234:1::1 | 00:00:03 |
     | R   | 9999::/16   | 1/0    | template1 | null      | 00:00:33 |
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:34 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:34 |
     | R   | 2.2.2.1/32 | 120/1  | ethernet1 | 1.1.1.1 | 00:00:33 |
     | C   | 2.2.2.2/32 | 0/0    | loopback0 | null    | 00:00:34 |
     | C   | 9.9.9.0/24 | 0/0    | template1 | null    | 00:00:34 |
     | LOC | 9.9.9.9/32 | 0/1    | template1 | null    | 00:00:34 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:34 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:34 |
     | R   | 4321::1/128   | 120/1  | ethernet1 | 1234:1::1 | 00:00:03 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null      | 00:00:34 |
     | C   | 9999::/16     | 0/0    | template1 | null      | 00:00:34 |
     | LOC | 9999::9/128   | 0/1    | template1 | null      | 00:00:34 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

# Example: ebgp in chain with soft-reconfig
    
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
    logging file debug ../binTmp/zzz84r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 2
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
     neighbor 1234:1::2 soft-reconfiguration
     redistribute connected
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
    logging file debug ../binTmp/zzz84r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 soft-reconfiguration
     neighbor 1.1.1.6 remote-as 3
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 2
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     neighbor 1.1.1.6 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:1::1 soft-reconfiguration
     neighbor 1234:2::2 remote-as 3
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 2
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
     neighbor 1234:2::2 soft-reconfiguration
     redistribute connected
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
    logging file debug ../binTmp/zzz84r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 3
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.5 remote-as 2
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 3
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     neighbor 1.1.1.5 soft-reconfiguration
     neighbor 1.1.1.10 remote-as 4
     no neighbor 1.1.1.10 description
     neighbor 1.1.1.10 local-as 3
     neighbor 1.1.1.10 address-family unicast
     neighbor 1.1.1.10 distance 20
     neighbor 1.1.1.10 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 3
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:2::1 remote-as 2
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 3
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 20
     neighbor 1234:2::1 soft-reconfiguration
     neighbor 1234:3::2 remote-as 4
     no neighbor 1234:3::2 description
     neighbor 1234:3::2 local-as 3
     neighbor 1234:3::2 address-family unicast
     neighbor 1234:3::2 distance 20
     neighbor 1234:3::2 soft-reconfiguration
     redistribute connected
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz84r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 4
     router-id 4.4.4.4
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.9 remote-as 3
     no neighbor 1.1.1.9 description
     neighbor 1.1.1.9 local-as 4
     neighbor 1.1.1.9 address-family unicast
     neighbor 1.1.1.9 distance 20
     neighbor 1.1.1.9 soft-reconfiguration
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 4
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast
     neighbor 1234:3::1 remote-as 3
     no neighbor 1234:3::1 description
     neighbor 1234:3::1 local-as 4
     neighbor 1234:3::1 address-family unicast
     neighbor 1234:3::1 distance 20
     neighbor 1234:3::1 soft-reconfiguration
     redistribute connected
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
    r2#show ipv4 bgp 1 sum
    r2#show ipv4 bgp 1 sum
     |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
     | neighbor | as | ready | learn | sent | uptime   |
     |----------|----|-------|-------|------|----------|
     | 1.1.1.1  | 1  | true  | 2     | 7    | 00:00:06 |
     | 1.1.1.6  | 3  | true  | 4     | 7    | 00:00:05 |
     |__________|____|_______|_______|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bgp 1 sum
    r2#show ipv6 bgp 1 sum
     |~~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
     | neighbor  | as | ready | learn | sent | uptime   |
     |-----------|----|-------|-------|------|----------|
     | 1234:1::1 | 1  | true  | 2     | 7    | 00:00:06 |
     | 1234:2::2 | 3  | true  | 4     | 7    | 00:00:06 |
     |___________|____|_______|_______|______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 bgp 1 nei 1.1.1.1 uni learn
    r2#show ipv4 bgp 1 nei 1.1.1.1 uni learn
     |~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix     | hop     | metric     | aspath |
     |------------|---------|------------|--------|
     | 1.1.1.0/30 | 1.1.1.1 | 20/100/0/0 | 1      |
     | 2.2.2.1/32 | 1.1.1.1 | 20/100/0/0 | 1      |
     |____________|_________|____________|________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bgp 1 nei 1234:1::1 uni learn
    r2#show ipv6 bgp 1 nei 1234:1::1 uni learn
     |~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix      | hop       | metric     | aspath |
     |-------------|-----------|------------|--------|
     | 1234:1::/32 | 1234:1::1 | 20/100/0/0 | 1      |
     | 4321::1/128 | 1234:1::1 | 20/100/0/0 | 1      |
     |_____________|___________|____________|________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 bgp 1 nei 1.1.1.1 uni accept
    r2#show ipv4 bgp 1 nei 1.1.1.1 uni accept
     |~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix     | hop     | metric     | aspath |
     |------------|---------|------------|--------|
     | 1.1.1.0/30 | 1.1.1.1 | 20/100/0/0 | 1      |
     | 2.2.2.1/32 | 1.1.1.1 | 20/100/0/0 | 1      |
     |____________|_________|____________|________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 bgp 1 nei 1234:1::1 uni accept
    r2#show ipv6 bgp 1 nei 1234:1::1 uni accept
     |~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix      | hop       | metric     | aspath |
     |-------------|-----------|------------|--------|
     | 1234:1::/32 | 1234:1::1 | 20/100/0/0 | 1      |
     | 4321::1/128 | 1234:1::1 | 20/100/0/0 | 1      |
     |_____________|___________|____________|________|
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:09 |
     | LOC | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:09 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:09 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:09 |
     | B   | 1.1.1.8/30 | 20/0   | ethernet2 | 1.1.1.6 | 00:00:06 |
     | B   | 2.2.2.1/32 | 20/0   | ethernet1 | 1.1.1.1 | 00:00:06 |
     | C   | 2.2.2.2/32 | 0/0    | loopback0 | null    | 00:00:09 |
     | B   | 2.2.2.3/32 | 20/0   | ethernet2 | 1.1.1.6 | 00:00:06 |
     | B   | 2.2.2.4/32 | 20/0   | ethernet2 | 1.1.1.6 | 00:00:06 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:09 |
     | LOC | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:09 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:09 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:09 |
     | B   | 1234:3::/32   | 20/0   | ethernet2 | 1234:2::2 | 00:00:06 |
     | B   | 4321::1/128   | 20/0   | ethernet1 | 1234:1::1 | 00:00:06 |
     | C   | 4321::2/128   | 0/0    | loopback0 | null      | 00:00:09 |
     | B   | 4321::3/128   | 20/0   | ethernet2 | 1234:2::2 | 00:00:06 |
     | B   | 4321::4/128   | 20/0   | ethernet2 | 1234:2::2 | 00:00:06 |
     |_____|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

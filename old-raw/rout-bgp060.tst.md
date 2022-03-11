# Example: ebgp with nexthop tracking routemap
    
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
    logging file debug ../binTmp/zzz10r1-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 match distance 0
     !
     exit
    !
    route-map rm2
     sequence 10 action permit
     sequence 10 set aspath 3 3 3
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
     local-as 1
     router-id 4.4.4.1
     address-family unicast
     nexthop route-map rm1
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 route-map-in rm2
     neighbor 1.1.1.2 route-map-out rm2
     neighbor 1.1.1.6 remote-as 2
     no neighbor 1.1.1.6 description
     neighbor 1.1.1.6 local-as 1
     neighbor 1.1.1.6 address-family unicast
     neighbor 1.1.1.6 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast
     nexthop route-map rm1
     neighbor 1234:1::2 remote-as 2
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 20
     neighbor 1234:1::2 route-map-in rm2
     neighbor 1234:1::2 route-map-out rm2
     neighbor 1234:2::2 remote-as 2
     no neighbor 1234:2::2 description
     neighbor 1234:2::2 local-as 1
     neighbor 1234:2::2 address-family unicast
     neighbor 1234:2::2 distance 20
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
    logging file debug ../binTmp/zzz10r2-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 match distance 0
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
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     address-family unicast
     nexthop route-map rm1
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.5 remote-as 1
     no neighbor 1.1.1.5 description
     neighbor 1.1.1.5 local-as 2
     neighbor 1.1.1.5 address-family unicast
     neighbor 1.1.1.5 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     address-family unicast
     nexthop route-map rm1
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 2
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 20
     neighbor 1234:2::1 remote-as 1
     no neighbor 1234:2::1 description
     neighbor 1234:2::1 local-as 2
     neighbor 1234:2::1 address-family unicast
     neighbor 1234:2::1 distance 20
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
    r1#
    r1#
    r1#show ipv4 bgp 1 sum
    r1#show ipv4 bgp 1 sum
     |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
     | neighbor | as | ready | learn | sent | uptime   |
     |----------|----|-------|-------|------|----------|
     | 1.1.1.2  | 2  | true  | 3     | 4    | 00:00:05 |
     | 1.1.1.6  | 2  | true  | 3     | 4    | 00:00:05 |
     |__________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 sum
    r1#show ipv6 bgp 1 sum
     |~~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
     | neighbor  | as | ready | learn | sent | uptime   |
     |-----------|----|-------|-------|------|----------|
     | 1234:1::2 | 2  | true  | 3     | 4    | 00:00:04 |
     | 1234:2::2 | 2  | true  | 3     | 4    | 00:00:06 |
     |___________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 next
    r1#show ipv4 bgp 1 next
     |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | neighbor | as | reach | chg      | num | uptime   |
     |----------|----|-------|----------|-----|----------|
     | 1.1.1.2  | 2  | true  | 00:00:07 | 1   | 00:00:05 |
     | 1.1.1.6  | 2  | true  | 00:00:07 | 1   | 00:00:05 |
     |__________|____|_______|__________|_____|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 next
    r1#show ipv6 bgp 1 next
     |~~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~~~~|~~~~~|~~~~~~~~~~|
     | neighbor  | as | reach | chg      | num | uptime   |
     |-----------|----|-------|----------|-----|----------|
     | 1234:1::2 | 2  | true  | 00:00:07 | 1   | 00:00:04 |
     | 1234:2::2 | 2  | true  | 00:00:07 | 1   | 00:00:06 |
     |___________|____|_______|__________|_____|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 route v1
    r1#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:08 |
     | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:08 |
     | C   | 1.1.1.4/30 | 0/0    | ethernet2 | null    | 00:00:08 |
     | LOC | 1.1.1.5/32 | 0/1    | ethernet2 | null    | 00:00:08 |
     | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:08 |
     | B   | 2.2.2.2/32 | 20/0   | ethernet2 | 1.1.1.6 | 00:00:04 |
     |_____|____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 route v1
    r1#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix        | metric | iface     | hop       | time     |
     |-----|---------------|--------|-----------|-----------|----------|
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:08 |
     | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:08 |
     | C   | 1234:2::/32   | 0/0    | ethernet2 | null      | 00:00:08 |
     | LOC | 1234:2::1/128 | 0/1    | ethernet2 | null      | 00:00:08 |
     | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:08 |
     | B   | 4321::2/128   | 20/0   | ethernet2 | 1234:2::2 | 00:00:04 |
     |_____|_______________|________|___________|___________|__________|
    r1#
    r1#
    ```

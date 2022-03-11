# Example: othervpns over ebgp
    
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
    logging file debug ../binTmp/zzz1r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     exit
    !
    vrf definition v3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     exit
    !
    vrf definition v4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
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
    interface loopback2
     no description
     vrf forwarding v2
     ipv4 address 9.9.2.1 255.255.255.255
     ipv6 address 9992::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     no description
     vrf forwarding v3
     ipv4 address 9.9.3.1 255.255.255.255
     ipv6 address 9993::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     no description
     vrf forwarding v4
     ipv4 address 9.9.4.1 255.255.255.255
     ipv6 address 9994::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     no safe-ebgp
     address-family ovpnuni
     neighbor 2.2.2.2 remote-as 2
     no neighbor 2.2.2.2 description
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family ovpnuni
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family ovpnuni
     neighbor 4321::2 remote-as 2
     no neighbor 4321::2 description
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family ovpnuni
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
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
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    vrf definition v2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     exit
    !
    vrf definition v3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     exit
    !
    vrf definition v4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
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
    interface loopback2
     no description
     vrf forwarding v2
     ipv4 address 9.9.2.2 255.255.255.255
     ipv6 address 9992::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     no description
     vrf forwarding v3
     ipv4 address 9.9.3.2 255.255.255.255
     ipv6 address 9993::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     no description
     vrf forwarding v4
     ipv4 address 9.9.4.2 255.255.255.255
     ipv6 address 9994::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     no safe-ebgp
     address-family ovpnuni
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 2
     neighbor 2.2.2.1 address-family ovpnuni
     neighbor 2.2.2.1 distance 20
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family ovpnuni
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 2
     neighbor 4321::1 address-family ovpnuni
     neighbor 4321::1 distance 20
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
     afi-ovrf v2 enable
     afi-ovrf v2 redistribute connected
     afi-ovrf v3 enable
     afi-ovrf v3 redistribute connected
     afi-ovrf v4 enable
     afi-ovrf v4 redistribute connected
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
     | 2.2.2.2  | 2  | true  | 3     | 6    | 00:00:16 |
     |__________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 sum
    r1#show ipv6 bgp 1 sum
     |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~|
     | neighbor | as | ready | learn | sent | uptime   |
     |----------|----|-------|-------|------|----------|
     | 4321::2  | 2  | true  | 3     | 6    | 00:00:16 |
     |__________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 ovpnuni dat
    r1#show ipv4 bgp 1 ovpnuni dat
     |~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix          | hop     | metric     | aspath |
     |-----------------|---------|------------|--------|
     | 9992::1/128 1:2 | null    | 0/0/0/0    |        |
     | 9992::2/128 1:2 | 2.2.2.2 | 20/100/0/0 | 2      |
     | 9993::1/128 1:3 | null    | 0/0/0/0    |        |
     | 9993::2/128 1:3 | 2.2.2.2 | 20/100/0/0 | 2      |
     | 9994::1/128 1:4 | null    | 0/0/0/0    |        |
     | 9994::2/128 1:4 | 2.2.2.2 | 20/100/0/0 | 2      |
     |_________________|_________|____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 ovpnuni dat
    r1#show ipv6 bgp 1 ovpnuni dat
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix         | hop     | metric     | aspath |
     |----------------|---------|------------|--------|
     | 9.9.2.1/32 1:2 | null    | 0/0/0/0    |        |
     | 9.9.2.2/32 1:2 | 4321::2 | 20/100/0/0 | 2      |
     | 9.9.3.1/32 1:3 | null    | 0/0/0/0    |        |
     | 9.9.3.2/32 1:3 | 4321::2 | 20/100/0/0 | 2      |
     | 9.9.4.1/32 1:4 | null    | 0/0/0/0    |        |
     | 9.9.4.2/32 1:4 | 4321::2 | 20/100/0/0 | 2      |
     |________________|_________|____________|________|
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:18 |
     | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:18 |
     | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:19 |
     | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:09 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:18 |
     | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:18 |
     | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:19 |
     | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:02 |
     |_____|_______________|________|___________|___________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 route v2
    r1#show ipv4 route v2
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | C   | 9.9.2.1/32 | 0/0    | loopback2 | null    | 00:00:19 |
     | B   | 9.9.2.2/32 | 20/0   | null@v1:6 | 4321::2 | 00:00:15 |
     |_____|____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 route v2
    r1#show ipv6 route v2
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 9992::1/128 | 0/0    | loopback2 | null    | 00:00:19 |
     | B   | 9992::2/128 | 20/0   | null@v1:4 | 2.2.2.2 | 00:00:14 |
     |_____|_____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 route v3
    r1#show ipv4 route v3
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | C   | 9.9.3.1/32 | 0/0    | loopback3 | null    | 00:00:19 |
     | B   | 9.9.3.2/32 | 20/0   | null@v1:6 | 4321::2 | 00:00:15 |
     |_____|____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 route v3
    r1#show ipv6 route v3
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 9993::1/128 | 0/0    | loopback3 | null    | 00:00:19 |
     | B   | 9993::2/128 | 20/0   | null@v1:4 | 2.2.2.2 | 00:00:15 |
     |_____|_____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 route v4
    r1#show ipv4 route v4
     |~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix     | metric | iface     | hop     | time     |
     |-----|------------|--------|-----------|---------|----------|
     | C   | 9.9.4.1/32 | 0/0    | loopback4 | null    | 00:00:19 |
     | B   | 9.9.4.2/32 | 20/0   | null@v1:6 | 4321::2 | 00:00:15 |
     |_____|____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 route v4
    r1#show ipv6 route v4
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 9994::1/128 | 0/0    | loopback4 | null    | 00:00:19 |
     | B   | 9994::2/128 | 20/0   | null@v1:4 | 2.2.2.2 | 00:00:16 |
     |_____|_____________|________|___________|_________|__________|
    r1#
    r1#
    ```

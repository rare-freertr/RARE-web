# Example: vpls/ldp over ebgp
    
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
    logging file debug ../binTmp/zzz77r1-log.run
    !
    bridge 1
     rd 1:1
     rt-import 1:1
     rt-export 1:1
     mac-learn
     private-bridge
     exit
    !
    bridge 2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mac-learn
     private-bridge
     exit
    !
    bridge 3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     mac-learn
     private-bridge
     exit
    !
    bridge 4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
     mac-learn
     private-bridge
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 4444::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi3
     no description
     vrf forwarding v1
     ipv6 address 3333::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi4
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.1 255.255.255.252
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
     address-family vpls
     neighbor 2.2.2.2 remote-as 2
     no neighbor 2.2.2.2 description
     neighbor 2.2.2.2 local-as 1
     neighbor 2.2.2.2 address-family vpls
     neighbor 2.2.2.2 distance 20
     neighbor 2.2.2.2 update-source loopback0
     neighbor 2.2.2.2 send-community standard extended
     afi-vpls 1:1 bridge-group 1
     afi-vpls 1:1 update-source loopback0
     afi-vpls 1:2 bridge-group 3
     afi-vpls 1:2 update-source loopback0
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family vpls
     neighbor 4321::2 remote-as 2
     no neighbor 4321::2 description
     neighbor 4321::2 local-as 1
     neighbor 4321::2 address-family vpls
     neighbor 4321::2 distance 20
     neighbor 4321::2 update-source loopback0
     neighbor 4321::2 send-community standard extended
     afi-vpls 1:1 bridge-group 2
     afi-vpls 1:1 update-source loopback0
     afi-vpls 1:2 bridge-group 4
     afi-vpls 1:2 update-source loopback0
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
    logging file debug ../binTmp/zzz77r2-log.run
    !
    bridge 1
     rd 1:1
     rt-import 1:1
     rt-export 1:1
     mac-learn
     private-bridge
     exit
    !
    bridge 2
     rd 1:2
     rt-import 1:2
     rt-export 1:2
     mac-learn
     private-bridge
     exit
    !
    bridge 3
     rd 1:3
     rt-import 1:3
     rt-export 1:3
     mac-learn
     private-bridge
     exit
    !
    bridge 4
     rd 1:4
     rt-import 1:4
     rt-export 1:4
     mac-learn
     private-bridge
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
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
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     no description
     vrf forwarding v1
     ipv6 address 4444::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi3
     no description
     vrf forwarding v1
     ipv6 address 3333::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi4
     no description
     vrf forwarding v1
     ipv4 address 4.4.4.2 255.255.255.252
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
     address-family vpls
     neighbor 2.2.2.1 remote-as 1
     no neighbor 2.2.2.1 description
     neighbor 2.2.2.1 local-as 2
     neighbor 2.2.2.1 address-family vpls
     neighbor 2.2.2.1 distance 20
     neighbor 2.2.2.1 update-source loopback0
     neighbor 2.2.2.1 send-community standard extended
     afi-vpls 1:1 bridge-group 1
     afi-vpls 1:1 update-source loopback0
     afi-vpls 1:2 bridge-group 3
     afi-vpls 1:2 update-source loopback0
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     no safe-ebgp
     address-family vpls
     neighbor 4321::1 remote-as 1
     no neighbor 4321::1 description
     neighbor 4321::1 local-as 2
     neighbor 4321::1 address-family vpls
     neighbor 4321::1 distance 20
     neighbor 4321::1 update-source loopback0
     neighbor 4321::1 send-community standard extended
     afi-vpls 1:1 bridge-group 2
     afi-vpls 1:1 update-source loopback0
     afi-vpls 1:2 bridge-group 4
     afi-vpls 1:2 update-source loopback0
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
     | 2.2.2.2  | 2  | true  | 2     | 4    | 00:00:27 |
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
     | 4321::2  | 2  | true  | 2     | 4    | 00:00:26 |
     |__________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 vpls dat
    r1#show ipv4 bgp 1 vpls dat
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix         | hop     | metric     | aspath |
     |----------------|---------|------------|--------|
     | 2.2.2.1/32 1:1 | null    | 0/0/0/0    |        |
     | 2.2.2.2/32 1:1 | 2.2.2.2 | 20/100/0/0 | 2      |
     | 2.2.2.1/32 1:3 | null    | 0/0/0/0    |        |
     | 2.2.2.2/32 1:3 | 2.2.2.2 | 20/100/0/0 | 2      |
     |________________|_________|____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 vpls dat
    r1#show ipv6 bgp 1 vpls dat
     |~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix          | hop     | metric     | aspath |
     |-----------------|---------|------------|--------|
     | 4321::1/128 1:2 | null    | 0/0/0/0    |        |
     | 4321::2/128 1:2 | 4321::2 | 20/100/0/0 | 2      |
     | 4321::1/128 1:4 | null    | 0/0/0/0    |        |
     | 4321::2/128 1:4 | 4321::2 | 20/100/0/0 | 2      |
     |_________________|_________|____________|________|
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
     | C   | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:30 |
     | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:30 |
     | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:30 |
     | S   | 2.2.2.2/32 | 1/0    | ethernet1 | 1.1.1.2 | 00:00:14 |
     | C   | 3.3.3.0/30 | 0/0    | bvi1      | null    | 00:00:30 |
     | LOC | 3.3.3.1/32 | 0/1    | bvi1      | null    | 00:00:30 |
     | C   | 4.4.4.0/30 | 0/0    | bvi4      | null    | 00:00:29 |
     | LOC | 4.4.4.1/32 | 0/1    | bvi4      | null    | 00:00:29 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:30 |
     | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:30 |
     | C   | 3333::/16     | 0/0    | bvi3      | null      | 00:00:30 |
     | LOC | 3333::1/128   | 0/1    | bvi3      | null      | 00:00:30 |
     | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:30 |
     | S   | 4321::2/128   | 1/0    | ethernet1 | 1234:1::2 | 00:00:16 |
     | C   | 4444::/16     | 0/0    | bvi2      | null      | 00:00:30 |
     | LOC | 4444::1/128   | 0/1    | bvi2      | null      | 00:00:30 |
     |_____|_______________|________|___________|___________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show bridge 1
    r1#show bridge 1
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|
     |                                             | packet         | byte             |     |
     | iface                        | fwd  | phys  | tx | rx | drop | tx  | rx  | drop | grp |
     |------------------------------|------|-------|----|----|------|-----|-----|------|-----|
     | brprt bvi                    |      |       |    |    |      |     |     |      |     |
     | pwe 2.2.2.2 2814754062073857 | true | false | 18 | 12 | 0    | 936 | 900 | 0    |     |
     |______________________________|______|_______|____|____|______|_____|_____|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |                                                        | packet             | byte             |  |
     | addr           | iface                        | static | time     | tx | rx | drop | tx  | rx  | drop |
     |----------------|------------------------------|--------|----------|----|----|------|-----|-----|------|
     | 0003.7d5f.6142 | pwe 2.2.2.2 2814754062073857 | false  | 00:00:31 | 11 | 12 | 0    | 726 | 756 | 0    |
     | 0009.3645.1f65 | bvi                          | false  | 00:00:31 | 12 | 20 | 0    | 756 | 996 | 0    |
     |________________|______________________________|________|__________|____|____|______|_____|_____|______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show bridge 2
    r1#show bridge 2
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                                             | packet         | byte               |     |
     | iface                        | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
     |------------------------------|------|-------|----|----|------|------|------|------|-----|
     | brprt bvi                    |      |       |    |    |      |      |      |      |     |
     | pwe 4321::2 2814754062073857 | true | false | 16 | 15 | 0    | 1072 | 1186 | 0    |     |
     |______________________________|______|_______|____|____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
     |                                                        | packet             | byte              |  |
     | addr           | iface                        | static | time     | tx | rx | drop | tx  | rx   | drop |
     |----------------|------------------------------|--------|----------|----|----|------|-----|------|------|
     | 0053.6554.3a14 | bvi                          | false  | 00:00:31 | 14 | 19 | 0    | 932 | 1326 | 0    |
     | 0077.4c7d.0638 | pwe 4321::2 2814754062073857 | false  | 00:00:31 | 15 | 15 | 0    | 998 | 1006 | 0    |
     |________________|______________________________|________|__________|____|____|______|_____|______|______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show bridge 3
    r1#show bridge 3
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                                             | packet         | byte               |     |
     | iface                        | fwd  | phys  | tx | rx | drop | tx   | rx   | drop | grp |
     |------------------------------|------|-------|----|----|------|------|------|------|-----|
     | brprt bvi                    |      |       |    |    |      |      |      |      |     |
     | pwe 2.2.2.2 2814754062073858 | true | false | 16 | 15 | 0    | 1072 | 1186 | 0    |     |
     |______________________________|______|_______|____|____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
     |                                                        | packet             | byte              |  |
     | addr           | iface                        | static | time     | tx | rx | drop | tx  | rx   | drop |
     |----------------|------------------------------|--------|----------|----|----|------|-----|------|------|
     | 0058.352c.6057 | bvi                          | false  | 00:00:31 | 14 | 19 | 0    | 932 | 1326 | 0    |
     | 0064.660a.7b5b | pwe 2.2.2.2 2814754062073858 | false  | 00:00:31 | 15 | 15 | 0    | 998 | 1006 | 0    |
     |________________|______________________________|________|__________|____|____|______|_____|______|______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show bridge 4
    r1#show bridge 4
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|
     |                                             | packet         | byte             |     |
     | iface                        | fwd  | phys  | tx | rx | drop | tx  | rx  | drop | grp |
     |------------------------------|------|-------|----|----|------|-----|-----|------|-----|
     | brprt bvi                    |      |       |    |    |      |     |     |      |     |
     | pwe 4321::2 2814754062073858 | true | false | 15 | 12 | 0    | 846 | 900 | 0    |     |
     |______________________________|______|_______|____|____|______|_____|_____|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |                                                        | packet             | byte             |  |
     | addr           | iface                        | static | time     | tx | rx | drop | tx  | rx  | drop |
     |----------------|------------------------------|--------|----------|----|----|------|-----|-----|------|
     | 0048.257d.6f78 | bvi                          | false  | 00:00:31 | 12 | 15 | 0    | 756 | 846 | 0    |
     | 006f.107e.105e | pwe 4321::2 2814754062073858 | false  | 00:00:31 | 11 | 12 | 0    | 726 | 756 | 0    |
     |________________|______________________________|________|__________|____|____|______|_____|_____|______|
    r1#
    r1#
    ```

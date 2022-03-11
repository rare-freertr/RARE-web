# Example: ibgp rr in subnet
    
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
    logging file debug ../binTmp/zzz60r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.0
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
     neighbor 1.1.1.2 remote-as 1
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast
     neighbor 1.1.1.2 distance 200
     neighbor 1.1.1.2 route-reflector-client
     neighbor 1.1.1.3 remote-as 1
     no neighbor 1.1.1.3 description
     neighbor 1.1.1.3 local-as 1
     neighbor 1.1.1.3 address-family unicast
     neighbor 1.1.1.3 distance 200
     neighbor 1.1.1.3 route-reflector-client
     neighbor 1.1.1.4 remote-as 1
     no neighbor 1.1.1.4 description
     neighbor 1.1.1.4 local-as 1
     neighbor 1.1.1.4 address-family unicast
     neighbor 1.1.1.4 distance 200
     neighbor 1.1.1.4 route-reflector-client
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::2 remote-as 1
     no neighbor 1234:1::2 description
     neighbor 1234:1::2 local-as 1
     neighbor 1234:1::2 address-family unicast
     neighbor 1234:1::2 distance 200
     neighbor 1234:1::2 route-reflector-client
     neighbor 1234:1::3 remote-as 1
     no neighbor 1234:1::3 description
     neighbor 1234:1::3 local-as 1
     neighbor 1234:1::3 address-family unicast
     neighbor 1234:1::3 distance 200
     neighbor 1234:1::3 route-reflector-client
     neighbor 1234:1::4 remote-as 1
     no neighbor 1234:1::4 description
     neighbor 1234:1::4 local-as 1
     neighbor 1234:1::4 address-family unicast
     neighbor 1234:1::4 distance 200
     neighbor 1234:1::4 route-reflector-client
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
    logging file debug ../binTmp/zzz60r2-log.run
    !
    bridge 1
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.2
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.2
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
    logging file debug ../binTmp/zzz60r3-log.run
    !
    bridge 1
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
    interface loopback0
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
     ipv6 address 1234:1::3 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
    logging file debug ../binTmp/zzz60r4-log.run
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
     ipv4 address 1.1.1.4 255.255.255.0
     ipv6 address 1234:1::4 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.4
     no safe-ebgp
     address-family unicast
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 1
     neighbor 1.1.1.1 address-family unicast
     neighbor 1.1.1.1 distance 200
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.4
     no safe-ebgp
     address-family unicast
     neighbor 1234:1::1 remote-as 1
     no neighbor 1234:1::1 description
     neighbor 1234:1::1 local-as 1
     neighbor 1234:1::1 address-family unicast
     neighbor 1234:1::1 distance 200
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
     | 1.1.1.2  | 1  | true  | 2     | 5    | 00:00:15 |
     | 1.1.1.3  | 1  | true  | 2     | 5    | 00:00:15 |
     | 1.1.1.4  | 1  | true  | 2     | 5    | 00:00:15 |
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
     | 1234:1::2 | 1  | true  | 2     | 5    | 00:00:15 |
     | 1234:1::3 | 1  | true  | 2     | 5    | 00:00:15 |
     | 1234:1::4 | 1  | true  | 2     | 5    | 00:00:15 |
     |___________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 group
    r1#show ipv4 bgp 1 group
     |~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~~~~|
     | neighbor | as | group | uptime   |
     |----------|----|-------|----------|
     | 1.1.1.2  | 1  | 0     | 00:00:15 |
     | 1.1.1.3  | 1  | 0     | 00:00:15 |
     | 1.1.1.4  | 1  | 0     | 00:00:15 |
     |__________|____|_______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 group
    r1#show ipv6 bgp 1 group
     |~~~~~~~~~~~|~~~~|~~~~~~~|~~~~~~~~~~|
     | neighbor  | as | group | uptime   |
     |-----------|----|-------|----------|
     | 1234:1::2 | 1  | 0     | 00:00:16 |
     | 1234:1::3 | 1  | 0     | 00:00:15 |
     | 1234:1::4 | 1  | 0     | 00:00:15 |
     |___________|____|_______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 group 0 uni
    r1#show ipv4 bgp 1 group 0 uni
     |~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|
     | prefix     | hop     | metric      | aspath |
     |------------|---------|-------------|--------|
     | 1.1.1.0/24 | 1.1.1.1 | 0/100/0/0   |        |
     | 2.2.2.1/32 | 1.1.1.1 | 0/100/0/0   |        |
     | 2.2.2.2/32 | 1.1.1.2 | 200/100/0/0 |        |
     | 2.2.2.3/32 | 1.1.1.3 | 200/100/0/0 |        |
     | 2.2.2.4/32 | 1.1.1.4 | 200/100/0/0 |        |
     |____________|_________|_____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 group 0 uni
    r1#show ipv6 bgp 1 group 0 uni
     |~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|
     | prefix      | hop       | metric      | aspath |
     |-------------|-----------|-------------|--------|
     | 1234:1::/32 | 1234:1::1 | 0/100/0/0   |        |
     | 4321::1/128 | 1234:1::1 | 0/100/0/0   |        |
     | 4321::2/128 | 1234:1::2 | 200/100/0/0 |        |
     | 4321::3/128 | 1234:1::3 | 200/100/0/0 |        |
     | 4321::4/128 | 1234:1::4 | 200/100/0/0 |        |
     |_____________|___________|_____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 best
    r1#show ipv4 bgp 1 best
     |~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|
     | category        | value    | addition            |
     |-----------------|----------|---------------------|
     | version         | 6        |                     |
     | full run        | 3        | times               |
     | full last       | 00:00:15 | 2022-03-10 20:48:25 |
     | full time       | 1        | ms                  |
     | incr run        | 2        | times               |
     | incr last       | 00:00:13 | 2022-03-10 20:48:27 |
     | incr time       | 0        | ms                  |
     | changes all     | 4        |                     |
     | changes now     | 0        |                     |
     | static peers    | 3        |                     |
     | dynamic peers   | 0        |                     |
     | groups          | 1        | 5..5                |
     | rpki table      | 0        |                     |
     | unicast table   | 3        | 0                   |
     | multicast table | 0        | 0                   |
     | ouni table      | 0        | 0                   |
     | omlt table      | 0        | 0                   |
     | oflw table      | 0        | 0                   |
     | osrt table      | 0        | 0                   |
     | flowspec table  | 0        | 0                   |
     | vpnuni table    | 0        | 0                   |
     | vpnmlt table    | 0        | 0                   |
     | vpnflw table    | 0        | 0                   |
     | ovpnuni table   | 0        | 0                   |
     | ovpnmlt table   | 0        | 0                   |
     | ovpnflw table   | 0        | 0                   |
     | vpls table      | 0        | 0                   |
     | mspw table      | 0        | 0                   |
     | evpn table      | 0        | 0                   |
     | mdt table       | 0        | 0                   |
     | nsh table       | 0        | 0                   |
     | srte table      | 0        | 0                   |
     | linkstate table | 0        | 0                   |
     | mvpn table      | 0        | 0                   |
     | omvpn table     | 0        | 0                   |
     |_________________|__________|_____________________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 best
    r1#show ipv6 bgp 1 best
     |~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|
     | category        | value    | addition            |
     |-----------------|----------|---------------------|
     | version         | 6        |                     |
     | full run        | 3        | times               |
     | full last       | 00:00:15 | 2022-03-10 20:48:26 |
     | full time       | 1        | ms                  |
     | incr run        | 2        | times               |
     | incr last       | 00:00:13 | 2022-03-10 20:48:28 |
     | incr time       | 47       | ms                  |
     | changes all     | 5        |                     |
     | changes now     | 0        |                     |
     | static peers    | 3        |                     |
     | dynamic peers   | 0        |                     |
     | groups          | 1        | 5..5                |
     | rpki table      | 0        |                     |
     | unicast table   | 3        | 0                   |
     | multicast table | 0        | 0                   |
     | ouni table      | 0        | 0                   |
     | omlt table      | 0        | 0                   |
     | oflw table      | 0        | 0                   |
     | osrt table      | 0        | 0                   |
     | flowspec table  | 0        | 0                   |
     | vpnuni table    | 0        | 0                   |
     | vpnmlt table    | 0        | 0                   |
     | vpnflw table    | 0        | 0                   |
     | ovpnuni table   | 0        | 0                   |
     | ovpnmlt table   | 0        | 0                   |
     | ovpnflw table   | 0        | 0                   |
     | vpls table      | 0        | 0                   |
     | mspw table      | 0        | 0                   |
     | evpn table      | 0        | 0                   |
     | mdt table       | 0        | 0                   |
     | nsh table       | 0        | 0                   |
     | srte table      | 0        | 0                   |
     | linkstate table | 0        | 0                   |
     | mvpn table      | 0        | 0                   |
     | omvpn table     | 0        | 0                   |
     |_________________|__________|_____________________|
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
     | C   | 1.1.1.0/24 | 0/0    | ethernet1 | null    | 00:00:19 |
     | LOC | 1.1.1.1/32 | 0/1    | ethernet1 | null    | 00:00:19 |
     | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:19 |
     | B   | 2.2.2.2/32 | 200/0  | ethernet1 | 1.1.1.2 | 00:00:15 |
     | B   | 2.2.2.3/32 | 200/0  | ethernet1 | 1.1.1.3 | 00:00:15 |
     | B   | 2.2.2.4/32 | 200/0  | ethernet1 | 1.1.1.4 | 00:00:15 |
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
     | C   | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:19 |
     | LOC | 1234:1::1/128 | 0/1    | ethernet1 | null      | 00:00:19 |
     | C   | 4321::1/128   | 0/0    | loopback0 | null      | 00:00:19 |
     | B   | 4321::2/128   | 200/0  | ethernet1 | 1234:1::2 | 00:00:15 |
     | B   | 4321::3/128   | 200/0  | ethernet1 | 1234:1::3 | 00:00:15 |
     | B   | 4321::4/128   | 200/0  | ethernet1 | 1234:1::4 | 00:00:15 |
     |_____|_______________|________|___________|___________|__________|
    r1#
    r1#
    ```

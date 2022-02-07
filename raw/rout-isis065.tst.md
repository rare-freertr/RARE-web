# Example: isis with bgp linkstate
    
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
    logging file debug ../binTmp/zzz27r1-log.run
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
     justadvert loopback1
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     justadvert loopback1
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
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv6 address 1234::1 ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family unicast linkstate
     neighbor 1.1.1.2 remote-as 2
     no neighbor 1.1.1.2 description
     neighbor 1.1.1.2 local-as 1
     neighbor 1.1.1.2 address-family unicast linkstate
     neighbor 1.1.1.2 distance 20
     neighbor 1.1.1.2 linkstate
     afi-links isis4 1 2
     justadvert loopback2
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast linkstate
     neighbor 1234::2 remote-as 2
     no neighbor 1234::2 description
     neighbor 1234::2 local-as 1
     neighbor 1234::2 address-family unicast linkstate
     neighbor 1234::2 distance 20
     neighbor 1234::2 linkstate
     afi-links isis6 1 2
     justadvert loopback2
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
    logging file debug ../binTmp/zzz27r2-log.run
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
     justadvert loopback1
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     justadvert loopback1
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
    interface loopback2
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.102 255.255.255.255
     ipv6 address 4321::102 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv6 address 1234::2 ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     address-family unicast linkstate
     neighbor 1.1.1.1 remote-as 1
     no neighbor 1.1.1.1 description
     neighbor 1.1.1.1 local-as 2
     neighbor 1.1.1.1 address-family unicast linkstate
     neighbor 1.1.1.1 distance 20
     neighbor 1.1.1.1 linkstate
     afi-links isis4 1 2
     justadvert loopback2
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     address-family unicast linkstate
     neighbor 1234::1 remote-as 1
     no neighbor 1234::1 description
     neighbor 1234::1 local-as 2
     neighbor 1234::1 address-family unicast linkstate
     neighbor 1234::1 distance 20
     neighbor 1234::1 linkstate
     afi-links isis6 1 2
     justadvert loopback2
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
     | ethernet1 | 0000.0000.0000 | 2     | 4444.0000.1111 | 1.1.1.1    | ::            | up    | 00:00:01 |
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
     | ethernet2 | 0000.0000.0000 | 2     | 6666.0000.1111 | 1234::1    | ::            | up    | 00:00:01 |
     |___________|________________|_______|________________|____________|_______________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 dat 2
    r2#show ipv4 isis 1 dat 2
     |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
     | lspid                | sequence | flags | len | time     |
     |----------------------|----------|-------|-----|----------|
     | 4444.0000.1111.00-00 | 00000004 | apo   | 45  | 00:19:58 |
     | 4444.0000.2222.00-00 | 00000004 | apo   | 45  | 00:19:58 |
     |______________________|__________|_______|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 isis 1 dat 2
    r2#show ipv6 isis 1 dat 2
     |~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~|
     | lspid                | sequence | flags | len | time     |
     |----------------------|----------|-------|-----|----------|
     | 6666.0000.1111.00-00 | 00000004 | apo   | 58  | 00:19:58 |
     | 6666.0000.2222.00-00 | 00000004 | apo   | 58  | 00:19:58 |
     |______________________|__________|_______|_____|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 isis 1 tre 2
    r2#show ipv4 isis 1 tre 2
    `--r2
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
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix       | metric | iface     | hop     | time     |
     |-----|--------------|--------|-----------|---------|----------|
     | C   | 1.1.1.0/24   | 0/0    | ethernet1 | null    | 00:00:11 |
     | LOC | 1.1.1.2/32   | 0/1    | ethernet1 | null    | 00:00:11 |
     | I   | 2.2.2.1/32   | 115/10 | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C   | 2.2.2.2/32   | 0/0    | loopback1 | null    | 00:00:12 |
     | B   | 2.2.2.101/32 | 20/0   | ethernet1 | 1.1.1.1 | 00:00:09 |
     | C   | 2.2.2.102/32 | 0/0    | loopback2 | null    | 00:00:12 |
     |_____|______________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop     | time     |
     |------|---------------|--------|-----------|---------|----------|
     | C    | 1234::/16     | 0/0    | ethernet2 | null    | 00:00:11 |
     | LOC  | 1234::2/128   | 0/1    | ethernet2 | null    | 00:00:11 |
     | I EX | 4321::1/128   | 115/10 | ethernet2 | 1234::1 | 00:00:01 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null    | 00:00:12 |
     | B    | 4321::101/128 | 20/0   | ethernet2 | 1234::1 | 00:00:09 |
     | C    | 4321::102/128 | 0/0    | loopback2 | null    | 00:00:12 |
     |______|_______________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 uni dat
    r1#show ipv4 bgp 1 uni dat
     |~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix       | hop     | metric     | aspath |
     |--------------|---------|------------|--------|
     | 2.2.2.102/32 | 1.1.1.2 | 20/100/0/0 | 2      |
     |______________|_________|____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 uni dat
    r1#show ipv6 bgp 1 uni dat
     |~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix        | hop     | metric     | aspath |
     |---------------|---------|------------|--------|
     | 4321::102/128 | 1234::2 | 20/100/0/0 | 2      |
     |_______________|_________|____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 bgp 1 links dat
    r1#show ipv4 bgp 1 links dat
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix                                      | hop     | metric     | aspath |
     |---------------------------------------------|---------|------------|--------|
     | 1d4:702e:190a:8fc0:1e3c:6166:8a78:ced0/128  | 1.1.1.2 | 20/100/0/0 | 2      |
     | 2b6:2ea2:3603:cfea:35c2:a008:e7b3:6960/128  | 1.1.1.2 | 20/100/0/0 | 2      |
     | 1d72:9f37:cbcf:4f3a:438c:e354:5299:e403/128 | null    | 0/0/0/0    |        |
     | 2ee1:c3cf:9707:f8d0:c5ae:4a4c:9414:fc61/128 | 1.1.1.2 | 20/100/0/0 | 2      |
     | 5e8b:231c:78a9:9a6a:b8da:9630:6e19:374c/128 | null    | 0/0/0/0    |        |
     | 767f:b83c:37f3:ea74:a114:7909:3973:3f02/128 | null    | 0/0/0/0    |        |
     | 7b08:4c2a:b040:7586:ab01:e688:e6af:3e53/128 | 1.1.1.2 | 20/100/0/0 | 2      |
     | 9154:8159:3cb8:9a1e:fba0:1f8b:fef0:152/128  | null    | 0/0/0/0    |        |
     | 982c:56b0:f106:51e3:f4ab:3da5:be22:ab3c/128 | 1.1.1.2 | 20/100/0/0 | 2      |
     | bcc7:2cf9:bc82:eb5e:b16d:2a88:a914:7dee/128 | 1.1.1.2 | 20/100/0/0 | 2      |
     | c73d:a710:62c1:aa0d:7023:8573:6ba7:a388/128 | null    | 0/0/0/0    |        |
     | d616:ed58:b691:2b31:1914:2d6e:4f64:8fa3/128 | null    | 0/0/0/0    |        |
     | dc39:8741:3c1:2ef3:ad2:aa2d:2f67:bd8d/128   | 1.1.1.2 | 20/100/0/0 | 2      |
     | e2d6:3f2a:c19a:be9d:92de:40e0:b7d1:caa0/128 | null    | 0/0/0/0    |        |
     | e87b:488c:9be3:6fe9:53e9:dd21:328b:9239/128 | 1.1.1.2 | 20/100/0/0 | 2      |
     | f031:74d0:931e:51c:23cc:617c:4334:24f/128   | null    | 0/0/0/0    |        |
     |_____________________________________________|_________|____________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 bgp 1 links dat
    r1#show ipv6 bgp 1 links dat
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~|
     | prefix                                      | hop     | metric     | aspath |
     |---------------------------------------------|---------|------------|--------|
     | 8e7:7942:82cd:471c:e268:7fa:5cc6:c137/128   | null    | 0/0/0/0    |        |
     | 1918:dd25:fc92:3340:a6a3:3569:fdd9:c7f1/128 | 1234::2 | 20/100/0/0 | 2      |
     | 1939:ecc4:6810:3c5b:755b:e5b0:48eb:1638/128 | null    | 0/0/0/0    |        |
     | 42e5:b076:cff:b68:2956:91a9:c788:ebc6/128   | 1234::2 | 20/100/0/0 | 2      |
     | 5260:60b4:b265:153c:2b55:7163:cfc1:e41a/128 | 1234::2 | 20/100/0/0 | 2      |
     | 6bde:c2d0:f10d:4013:f6e:eea1:e849:9896/128  | null    | 0/0/0/0    |        |
     | 709d:a86d:d031:197b:f09f:17f1:3da:3bf4/128  | null    | 0/0/0/0    |        |
     | 88a5:fc31:e5c0:4de1:ad7:8cf5:6bcd:2fac/128  | null    | 0/0/0/0    |        |
     | 9194:8c9e:b5b6:2a6e:eab8:49d0:7f07:c988/128 | 1234::2 | 20/100/0/0 | 2      |
     | a112:69e9:9e0c:60f:503b:8d21:e8a7:9e64/128  | null    | 0/0/0/0    |        |
     | b215:f745:2344:87a6:cd2f:e4ac:728:840e/128  | 1234::2 | 20/100/0/0 | 2      |
     | d11d:59ed:4da5:2594:4280:f79b:7b57:eecb/128 | null    | 0/0/0/0    |        |
     | ee4f:41b8:8f25:ea98:e2b3:8d52:767f:c02d/128 | null    | 0/0/0/0    |        |
     | f21b:b63:9d73:a09c:b6f4:96d0:e682:c90b/128  | 1234::2 | 20/100/0/0 | 2      |
     | f92d:1bcb:c056:5f66:22e4:5bc5:2e2c:db4d/128 | 1234::2 | 20/100/0/0 | 2      |
     | fc03:ef3d:978a:1ba9:b846:e272:5133:29a0/128 | 1234::2 | 20/100/0/0 | 2      |
     |_____________________________________________|_________|____________|________|
    r1#
    r1#
    ```

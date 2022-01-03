# Example: bgp auto mesh tunnel
    
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
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
     exit
    !
    prefix-list all
     sequence 10 permit 0.0.0.0/0 ge 0 le 32
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family unicast
     neighbor 9.9.9.2 remote-as 2
     no neighbor 9.9.9.2 description
     neighbor 9.9.9.2 local-as 1
     neighbor 9.9.9.2 address-family unicast
     neighbor 9.9.9.2 distance 20
     redistribute connected
     automesh all
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast
     neighbor 9999::2 remote-as 2
     no neighbor 9999::2 description
     neighbor 9999::2 local-as 1
     neighbor 9999::2 address-family unicast
     neighbor 9999::2 distance 20
     redistribute connected
     automesh all
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
     exit
    !
    prefix-list all
     sequence 10 permit 0.0.0.0/0 ge 0 le 32
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.2
     address-family unicast
     neighbor 9.9.9.1 remote-as 1
     no neighbor 9.9.9.1 description
     neighbor 9.9.9.1 local-as 2
     neighbor 9.9.9.1 address-family unicast
     neighbor 9.9.9.1 distance 20
     redistribute connected
     automesh all
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.2
     address-family unicast
     neighbor 9999::1 remote-as 1
     no neighbor 9999::1 description
     neighbor 9999::1 local-as 2
     neighbor 9999::1 address-family unicast
     neighbor 9999::1 distance 20
     redistribute connected
     automesh all
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
     | 9.9.9.2  | 2  | true  | 2     | 3    | 00:00:07 |
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
     | 9999::2  | 2  | true  | 2     | 3    | 00:00:07 |
     |__________|____|_______|_______|______|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 rsvp v1 sum
    r1#show ipv4 rsvp v1 sum
     |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
     | source  | id    | subgroup | id | target  | id         | description |
     |---------|-------|----------|----|---------|------------|-------------|
     | 9.9.9.2 | 8281  | ::       | 0  | 9.9.9.1 | 2122673283 | r2:automesh |
     | 9.9.9.1 | 18883 | ::       | 0  | 9.9.9.2 | 1408494903 | r1:automesh |
     |_________|_______|__________|____|_________|____________|_____________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 rsvp v1 sum
    r1#show ipv6 rsvp v1 sum
     |~~~~~~~~~|~~~~~~~|~~~~~~~~~~|~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~|
     | source  | id    | subgroup | id | target  | id         | description |
     |---------|-------|----------|----|---------|------------|-------------|
     | 9999::2 | 547   | ::       | 0  | 9999::1 | 1959859930 | r2:automesh |
     | 9999::1 | 32520 | ::       | 0  | 9999::2 | 1028235547 | r1:automesh |
     |_________|_______|__________|____|_________|____________|_____________|
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
     | C   | 2.2.2.1/32 | 0/0    | loopback0 | null    | 00:00:12 |
     | B   | 2.2.2.2/32 | 20/0   | serial1   | 9.9.9.2 | 00:00:07 |
     | C   | 9.9.9.0/24 | 0/0    | serial1   | null    | 00:00:08 |
     | LOC | 9.9.9.1/32 | 0/1    | serial1   | null    | 00:00:08 |
     | MSH | 9.9.9.2/32 | 0/3    | serial1   | 9.9.9.2 | never    |
     |_____|____________|________|___________|_________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 route v1
    r1#show ipv6 route v1
     |~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ | prefix      | metric | iface     | hop     | time     |
     |-----|-------------|--------|-----------|---------|----------|
     | C   | 4321::1/128 | 0/0    | loopback0 | null    | 00:00:12 |
     | B   | 4321::2/128 | 20/0   | serial1   | 9999::2 | 00:00:07 |
     | C   | 9999::/16   | 0/0    | serial1   | null    | 00:00:08 |
     | LOC | 9999::1/128 | 0/1    | serial1   | null    | 00:00:08 |
     | MSH | 9999::2/128 | 0/3    | serial1   | 9999::2 | never    |
     |_____|_____________|________|___________|_________|__________|
    r1#
    r1#
    ```

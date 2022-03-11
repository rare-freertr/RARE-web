# Example: source interface translation to address
    
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
    logging file debug ../binTmp/zzz28r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    logging file debug ../binTmp/zzz28r2-log.run
    !
    access-list test4
     sequence 10 permit all 1.1.1.4 255.255.255.252 all 1.1.1.0 255.255.255.252 all
     exit
    !
    access-list test6
     sequence 10 permit all 1234:2:: ffff:ffff:: all 1234:1:: ffff:ffff:: all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 8.8.8.8 255.255.255.255 1.1.1.6
    !
    ipv6 route v1 8888::8 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    !
    !
    !
    ipv4 nat v1 sequence 10 source interface ethernet2 1.1.1.2
    !
    ipv6 nat v1 sequence 10 source interface ethernet2 1234:1::2
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
    logging file debug ../binTmp/zzz28r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 8.8.8.8 255.255.255.255
     ipv6 address 8888::8 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    r2#show ipv4 nat v1 tran
    r2#show ipv4 nat v1 tran
     |~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|
     |       | original        | translated      |                                    |
     | proto | source | target | source | target | age | last | timeout | pack | byte |
     |-------|--------|--------|--------|--------|-----|------|---------|------|------|
     |_______|________|________|________|________|_____|______|_________|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 nat v1 tran
    r2#show ipv6 nat v1 tran
     |~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|
     |       | original        | translated      |                                    |
     | proto | source | target | source | target | age | last | timeout | pack | byte |
     |-------|--------|--------|--------|--------|-----|------|---------|------|------|
     |_______|________|________|________|________|_____|______|_________|______|______|
    r2#
    r2#
    ```

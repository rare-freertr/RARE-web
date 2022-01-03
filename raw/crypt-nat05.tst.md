# Example: target address translation to address
    
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
    !
    ipv6 route v1 :: :: 1234:1::2
    !
    !
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
    !
    !
    !
    !
    ipv4 nat v1 sequence 10 target 8.8.8.8 1.1.1.1
    !
    ipv6 nat v1 sequence 10 target 8888::1 1234:1::1
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
    logging file debug ../binTmp/zzz1r3-log.run
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.5
    !
    ipv6 route v1 :: :: 1234:2::1
    !
    !
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
     |~~~~~~~|~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|
     |       | original                              | translated                            |                                              |
     | proto | source            | target            | source            | target            | age      | last     | timeout  | pack | byte |
     |-------|-------------------|-------------------|-------------------|-------------------|----------|----------|----------|------|------|
     | 1     | 1.1.1.1 762666525 | 1.1.1.6 762666525 | 8.8.8.8 762666525 | 1.1.1.6 762666525 | 00:00:05 | 00:00:05 | 00:05:00 | 0    | 0    |
     | 1     | 1.1.1.6 762666525 | 8.8.8.8 762666525 | 1.1.1.6 762666525 | 1.1.1.1 762666525 | 00:00:05 | 00:00:05 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666526 | 1.1.1.6 762666526 | 8.8.8.8 762666526 | 1.1.1.6 762666526 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666526 | 8.8.8.8 762666526 | 1.1.1.6 762666526 | 1.1.1.1 762666526 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666527 | 1.1.1.6 762666527 | 8.8.8.8 762666527 | 1.1.1.6 762666527 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666527 | 8.8.8.8 762666527 | 1.1.1.6 762666527 | 1.1.1.1 762666527 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666528 | 1.1.1.6 762666528 | 8.8.8.8 762666528 | 1.1.1.6 762666528 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666528 | 8.8.8.8 762666528 | 1.1.1.6 762666528 | 1.1.1.1 762666528 | 00:00:04 | 00:00:04 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666529 | 1.1.1.6 762666529 | 8.8.8.8 762666529 | 1.1.1.6 762666529 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666529 | 8.8.8.8 762666529 | 1.1.1.6 762666529 | 1.1.1.1 762666529 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666530 | 1.1.1.6 762666530 | 8.8.8.8 762666530 | 1.1.1.6 762666530 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666530 | 8.8.8.8 762666530 | 1.1.1.6 762666530 | 1.1.1.1 762666530 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666531 | 1.1.1.6 762666531 | 8.8.8.8 762666531 | 1.1.1.6 762666531 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666531 | 8.8.8.8 762666531 | 1.1.1.6 762666531 | 1.1.1.1 762666531 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666532 | 1.1.1.6 762666532 | 8.8.8.8 762666532 | 1.1.1.6 762666532 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666532 | 8.8.8.8 762666532 | 1.1.1.6 762666532 | 1.1.1.1 762666532 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.1 762666533 | 1.1.1.6 762666533 | 8.8.8.8 762666533 | 1.1.1.6 762666533 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 1     | 1.1.1.6 762666533 | 8.8.8.8 762666533 | 1.1.1.6 762666533 | 1.1.1.1 762666533 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     |_______|___________________|___________________|___________________|___________________|__________|__________|__________|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 nat v1 tran
    r2#show ipv6 nat v1 tran
     |~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~|~~~~~~|
     |       | original                                  | translated                                |                                              |
     | proto | source              | target              | source              | target              | age      | last     | timeout  | pack | byte |
     |-------|---------------------|---------------------|---------------------|---------------------|----------|----------|----------|------|------|
     | 58    | 1234:1::1 245391361 | 1234:2::2 245391361 | 8888::1 245391361   | 1234:2::2 245391361 | 00:00:03 | 00:00:03 | 00:05:00 | 0    | 0    |
     | 58    | 1234:2::2 245391361 | 8888::1 245391361   | 1234:2::2 245391361 | 1234:1::1 245391361 | 00:00:03 | 00:00:03 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391362 | 1234:2::2 245391362 | 8888::1 245391362   | 1234:2::2 245391362 | 00:00:02 | 00:00:02 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391362 | 8888::1 245391362   | 1234:2::2 245391362 | 1234:1::1 245391362 | 00:00:02 | 00:00:02 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391363 | 1234:2::2 245391363 | 8888::1 245391363   | 1234:2::2 245391363 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391363 | 8888::1 245391363   | 1234:2::2 245391363 | 1234:1::1 245391363 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391364 | 1234:2::2 245391364 | 8888::1 245391364   | 1234:2::2 245391364 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391364 | 8888::1 245391364   | 1234:2::2 245391364 | 1234:1::1 245391364 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391365 | 1234:2::2 245391365 | 8888::1 245391365   | 1234:2::2 245391365 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391365 | 8888::1 245391365   | 1234:2::2 245391365 | 1234:1::1 245391365 | 00:00:01 | 00:00:01 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391366 | 1234:2::2 245391366 | 8888::1 245391366   | 1234:2::2 245391366 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391366 | 8888::1 245391366   | 1234:2::2 245391366 | 1234:1::1 245391366 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391367 | 1234:2::2 245391367 | 8888::1 245391367   | 1234:2::2 245391367 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391367 | 8888::1 245391367   | 1234:2::2 245391367 | 1234:1::1 245391367 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391368 | 1234:2::2 245391368 | 8888::1 245391368   | 1234:2::2 245391368 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391368 | 8888::1 245391368   | 1234:2::2 245391368 | 1234:1::1 245391368 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391369 | 1234:2::2 245391369 | 8888::1 245391369   | 1234:2::2 245391369 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391369 | 8888::1 245391369   | 1234:2::2 245391369 | 1234:1::1 245391369 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:1::1 245391370 | 1234:2::2 245391370 | 8888::1 245391370   | 1234:2::2 245391370 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     | 58    | 1234:2::2 245391370 | 8888::1 245391370   | 1234:2::2 245391370 | 1234:1::1 245391370 | 00:00:00 | 00:00:00 | 00:05:00 | 1    | 64   |
     |_______|_____________________|_____________________|_____________________|_____________________|__________|__________|__________|______|______|
    r2#
    r2#
    ```
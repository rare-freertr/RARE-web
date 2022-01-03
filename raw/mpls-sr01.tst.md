# Example: sr in chain
    
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
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     segrout 10 1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     segrout 10 1
     redistribute connected
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     segrout 10 2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     segrout 10 2
     redistribute connected
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz1r3-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.3
     segrout 10 3
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     segrout 10 3
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv4 address 1.1.2.3 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1235::3 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.3.3 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1236::3 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz1r4-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.4
     segrout 10 4
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.4
     segrout 10 4
     redistribute connected
     exit
    !
    interface loopback1
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
     ipv4 address 1.1.3.4 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1236::4 ffff::
     ipv6 access-group-in test6
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
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
    r1#
    r1#
    r1#show mpls forw
    r1#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface     | hop     | label      | targets | bytes |
     |--------|----------|-----------|---------|------------|---------|-------|
     | 40610  | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 72305  | v1:4     | ethernet1 | 1.1.1.2 | 3          |         | 0     |
     | 272087 | v1:6     | ethernet1 | 1234::2 | 3          |         | 0     |
     | 344135 | null     | null      | null    | unlabelled |         | 0     |
     | 344136 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 344137 | v1:6     | ethernet1 | 1234::2 | 869200     |         | 0     |
     | 344138 | v1:6     | ethernet1 | 1234::2 | 869201     |         | 0     |
     | 344139 | v1:6     | ethernet1 | 1234::2 | 869202     |         | 0     |
     | 344140 | null     | null      | null    | unlabelled |         | 0     |
     | 344141 | null     | null      | null    | unlabelled |         | 0     |
     | 344142 | null     | null      | null    | unlabelled |         | 0     |
     | 344143 | null     | null      | null    | unlabelled |         | 0     |
     | 344144 | null     | null      | null    | unlabelled |         | 0     |
     | 576729 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 873795 | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 885493 | null     | null      | null    | unlabelled |         | 0     |
     | 885494 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 885495 | v1:4     | ethernet1 | 1.1.1.2 | 356410     |         | 0     |
     | 885496 | v1:4     | ethernet1 | 1.1.1.2 | 356411     |         | 0     |
     | 885497 | v1:4     | ethernet1 | 1.1.1.2 | 356412     |         | 0     |
     | 885498 | null     | null      | null    | unlabelled |         | 0     |
     | 885499 | null     | null      | null    | unlabelled |         | 0     |
     | 885500 | null     | null      | null    | unlabelled |         | 0     |
     | 885501 | null     | null      | null    | unlabelled |         | 0     |
     | 885502 | null     | null      | null    | unlabelled |         | 0     |
     | 903174 | tester:6 | null      | null    | unlabelled | local   | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r1#
    r1#
    ```
    
    ```
    r2#
    r2#
    r2#show mpls forw
    r2#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface     | hop     | label      | targets | bytes |
     |--------|----------|-----------|---------|------------|---------|-------|
     | 3154   | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 34014  | v1:4     | ethernet2 | 1.1.2.3 | 3          |         | 0     |
     | 162538 | v1:6     | ethernet1 | 1234::1 | 3          |         | 0     |
     | 356408 | null     | null      | null    | unlabelled |         | 0     |
     | 356409 | v1:4     | ethernet1 | 1.1.1.1 | 885494     |         | 1280  |
     | 356410 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 356411 | v1:4     | ethernet2 | 1.1.2.3 | 562120     |         | 640   |
     | 356412 | v1:4     | ethernet2 | 1.1.2.3 | 562121     |         | 640   |
     | 356413 | null     | null      | null    | unlabelled |         | 0     |
     | 356414 | null     | null      | null    | unlabelled |         | 0     |
     | 356415 | null     | null      | null    | unlabelled |         | 0     |
     | 356416 | null     | null      | null    | unlabelled |         | 0     |
     | 356417 | null     | null      | null    | unlabelled |         | 0     |
     | 501047 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 573517 | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 711246 | v1:4     | ethernet1 | 1.1.1.1 | 3          |         | 0     |
     | 776227 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 836902 | v1:6     | ethernet2 | 1235::3 | 3          |         | 0     |
     | 869198 | null     | null      | null    | unlabelled |         | 0     |
     | 869199 | v1:6     | ethernet1 | 1234::1 | 344136     |         | 1280  |
     | 869200 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 869201 | v1:6     | ethernet2 | 1235::3 | 113746     |         | 640   |
     | 869202 | v1:6     | ethernet2 | 1235::3 | 113747     |         | 640   |
     | 869203 | null     | null      | null    | unlabelled |         | 0     |
     | 869204 | null     | null      | null    | unlabelled |         | 0     |
     | 869205 | null     | null      | null    | unlabelled |         | 0     |
     | 869206 | null     | null      | null    | unlabelled |         | 0     |
     | 869207 | null     | null      | null    | unlabelled |         | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r3#
    r3#
    r3#show mpls forw
    r3#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface     | hop     | label      | targets | bytes |
     |--------|----------|-----------|---------|------------|---------|-------|
     | 113743 | null     | null      | null    | unlabelled |         | 0     |
     | 113744 | v1:6     | ethernet1 | 1235::2 | 869199     |         | 640   |
     | 113745 | v1:6     | ethernet1 | 1235::2 | 869200     |         | 640   |
     | 113746 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 113747 | v1:6     | ethernet2 | 1236::4 | 802040     |         | 1280  |
     | 113748 | null     | null      | null    | unlabelled |         | 0     |
     | 113749 | null     | null      | null    | unlabelled |         | 0     |
     | 113750 | null     | null      | null    | unlabelled |         | 0     |
     | 113751 | null     | null      | null    | unlabelled |         | 0     |
     | 113752 | null     | null      | null    | unlabelled |         | 0     |
     | 230658 | v1:4     | ethernet2 | 1.1.3.4 | 3          |         | 0     |
     | 294635 | v1:6     | ethernet2 | 1236::4 | 3          |         | 0     |
     | 422941 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 479853 | v1:4     | ethernet1 | 1.1.2.2 | 3          |         | 0     |
     | 496555 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 532959 | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 538825 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 562117 | null     | null      | null    | unlabelled |         | 0     |
     | 562118 | v1:4     | ethernet1 | 1.1.2.2 | 356409     |         | 640   |
     | 562119 | v1:4     | ethernet1 | 1.1.2.2 | 356410     |         | 640   |
     | 562120 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 562121 | v1:4     | ethernet2 | 1.1.3.4 | 119681     |         | 1280  |
     | 562122 | null     | null      | null    | unlabelled |         | 0     |
     | 562123 | null     | null      | null    | unlabelled |         | 0     |
     | 562124 | null     | null      | null    | unlabelled |         | 0     |
     | 562125 | null     | null      | null    | unlabelled |         | 0     |
     | 562126 | null     | null      | null    | unlabelled |         | 0     |
     | 669077 | v1:6     | ethernet1 | 1235::2 | 3          |         | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r3#
    r3#
    ```
    
    ```
    r4#
    r4#
    r4#show mpls forw
    r4#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface     | hop     | label      | targets | bytes |
     |--------|----------|-----------|---------|------------|---------|-------|
     | 69346  | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 119677 | null     | null      | null    | unlabelled |         | 0     |
     | 119678 | v1:4     | ethernet1 | 1.1.3.3 | 562118     |         | 0     |
     | 119679 | v1:4     | ethernet1 | 1.1.3.3 | 562119     |         | 0     |
     | 119680 | v1:4     | ethernet1 | 1.1.3.3 | 562120     |         | 0     |
     | 119681 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 119682 | null     | null      | null    | unlabelled |         | 0     |
     | 119683 | null     | null      | null    | unlabelled |         | 0     |
     | 119684 | null     | null      | null    | unlabelled |         | 0     |
     | 119685 | null     | null      | null    | unlabelled |         | 0     |
     | 119686 | null     | null      | null    | unlabelled |         | 0     |
     | 338958 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 384951 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 485172 | v1:4     | ethernet1 | 1.1.3.3 | 3          |         | 0     |
     | 647325 | v1:6     | ethernet1 | 1236::3 | 3          |         | 0     |
     | 727110 | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 802036 | null     | null      | null    | unlabelled |         | 0     |
     | 802037 | v1:6     | ethernet1 | 1236::3 | 113744     |         | 0     |
     | 802038 | v1:6     | ethernet1 | 1236::3 | 113745     |         | 0     |
     | 802039 | v1:6     | ethernet1 | 1236::3 | 113746     |         | 0     |
     | 802040 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 802041 | null     | null      | null    | unlabelled |         | 0     |
     | 802042 | null     | null      | null    | unlabelled |         | 0     |
     | 802043 | null     | null      | null    | unlabelled |         | 0     |
     | 802044 | null     | null      | null    | unlabelled |         | 0     |
     | 802045 | null     | null      | null    | unlabelled |         | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r4#
    r4#
    ```

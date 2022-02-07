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
    logging file debug ../binTmp/zzz95r1-log.run
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
    logging file debug ../binTmp/zzz95r2-log.run
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
    logging file debug ../binTmp/zzz95r3-log.run
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
    logging file debug ../binTmp/zzz95r4-log.run
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
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface     | hop     | label      | targets | bytes |
     |---------|----------|-----------|---------|------------|---------|-------|
     | 56223   | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 197984  | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 304954  | v1:6     | ethernet1 | 1234::2 | 3          |         | 0     |
     | 466489  | v1:4     | ethernet1 | 1.1.1.2 | 3          |         | 0     |
     | 534977  | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 590765  | null     | null      | null    | unlabelled |         | 0     |
     | 590766  | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 590767  | v1:6     | ethernet1 | 1234::2 | 785802     |         | 0     |
     | 590768  | v1:6     | ethernet1 | 1234::2 | 785803     |         | 0     |
     | 590769  | v1:6     | ethernet1 | 1234::2 | 785804     |         | 0     |
     | 590770  | null     | null      | null    | unlabelled |         | 0     |
     | 590771  | null     | null      | null    | unlabelled |         | 0     |
     | 590772  | null     | null      | null    | unlabelled |         | 0     |
     | 590773  | null     | null      | null    | unlabelled |         | 0     |
     | 590774  | null     | null      | null    | unlabelled |         | 0     |
     | 999164  | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 1020630 | null     | null      | null    | unlabelled |         | 0     |
     | 1020631 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 1020632 | v1:4     | ethernet1 | 1.1.1.2 | 1640       |         | 0     |
     | 1020633 | v1:4     | ethernet1 | 1.1.1.2 | 1641       |         | 0     |
     | 1020634 | v1:4     | ethernet1 | 1.1.1.2 | 1642       |         | 0     |
     | 1020635 | null     | null      | null    | unlabelled |         | 0     |
     | 1020636 | null     | null      | null    | unlabelled |         | 0     |
     | 1020637 | null     | null      | null    | unlabelled |         | 0     |
     | 1020638 | null     | null      | null    | unlabelled |         | 0     |
     | 1020639 | null     | null      | null    | unlabelled |         | 0     |
     |_________|__________|___________|_________|____________|_________|_______|
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
     | 1638   | null     | null      | null    | unlabelled |         | 0     |
     | 1639   | v1:4     | ethernet1 | 1.1.1.1 | 1020631    |         | 1280  |
     | 1640   | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 1641   | v1:4     | ethernet2 | 1.1.2.3 | 389008     |         | 640   |
     | 1642   | v1:4     | ethernet2 | 1.1.2.3 | 389009     |         | 640   |
     | 1643   | null     | null      | null    | unlabelled |         | 0     |
     | 1644   | null     | null      | null    | unlabelled |         | 0     |
     | 1645   | null     | null      | null    | unlabelled |         | 0     |
     | 1646   | null     | null      | null    | unlabelled |         | 0     |
     | 1647   | null     | null      | null    | unlabelled |         | 0     |
     | 41911  | v1:4     | ethernet1 | 1.1.1.1 | 3          |         | 0     |
     | 237642 | v1:6     | ethernet1 | 1234::1 | 3          |         | 0     |
     | 314935 | v1:4     | ethernet2 | 1.1.2.3 | 3          |         | 0     |
     | 527924 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 547679 | v1:6     | ethernet2 | 1235::3 | 3          |         | 0     |
     | 626356 | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 644914 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 785800 | null     | null      | null    | unlabelled |         | 0     |
     | 785801 | v1:6     | ethernet1 | 1234::1 | 590766     |         | 1280  |
     | 785802 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 785803 | v1:6     | ethernet2 | 1235::3 | 228673     |         | 640   |
     | 785804 | v1:6     | ethernet2 | 1235::3 | 228674     |         | 640   |
     | 785805 | null     | null      | null    | unlabelled |         | 0     |
     | 785806 | null     | null      | null    | unlabelled |         | 0     |
     | 785807 | null     | null      | null    | unlabelled |         | 0     |
     | 785808 | null     | null      | null    | unlabelled |         | 0     |
     | 785809 | null     | null      | null    | unlabelled |         | 0     |
     | 855214 | tester:4 | null      | null    | unlabelled | local   | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r3#
    r3#
    r3#show mpls forw
    r3#show mpls forw
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface     | hop     | label      | targets | bytes |
     |---------|----------|-----------|---------|------------|---------|-------|
     | 55771   | v1:4     | ethernet1 | 1.1.2.2 | 3          |         | 0     |
     | 153401  | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 228670  | null     | null      | null    | unlabelled |         | 0     |
     | 228671  | v1:6     | ethernet1 | 1235::2 | 785801     |         | 640   |
     | 228672  | v1:6     | ethernet1 | 1235::2 | 785802     |         | 640   |
     | 228673  | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 228674  | v1:6     | ethernet2 | 1236::4 | 602056     |         | 1280  |
     | 228675  | null     | null      | null    | unlabelled |         | 0     |
     | 228676  | null     | null      | null    | unlabelled |         | 0     |
     | 228677  | null     | null      | null    | unlabelled |         | 0     |
     | 228678  | null     | null      | null    | unlabelled |         | 0     |
     | 228679  | null     | null      | null    | unlabelled |         | 0     |
     | 389005  | null     | null      | null    | unlabelled |         | 0     |
     | 389006  | v1:4     | ethernet1 | 1.1.2.2 | 1639       |         | 640   |
     | 389007  | v1:4     | ethernet1 | 1.1.2.2 | 1640       |         | 640   |
     | 389008  | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 389009  | v1:4     | ethernet2 | 1.1.3.4 | 661162     |         | 1280  |
     | 389010  | null     | null      | null    | unlabelled |         | 0     |
     | 389011  | null     | null      | null    | unlabelled |         | 0     |
     | 389012  | null     | null      | null    | unlabelled |         | 0     |
     | 389013  | null     | null      | null    | unlabelled |         | 0     |
     | 389014  | null     | null      | null    | unlabelled |         | 0     |
     | 490126  | v1:6     | ethernet1 | 1235::2 | 3          |         | 0     |
     | 782559  | v1:4     | ethernet2 | 1.1.3.4 | 3          |         | 0     |
     | 798272  | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 888787  | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 1023424 | v1:6     | ethernet2 | 1236::4 | 3          |         | 0     |
     | 1030998 | v1:6     | null      | null    | unlabelled | local   | 0     |
     |_________|__________|___________|_________|____________|_________|_______|
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
     | 77969  | v1:6     | ethernet1 | 1236::3 | 3          |         | 0     |
     | 520648 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 602052 | null     | null      | null    | unlabelled |         | 0     |
     | 602053 | v1:6     | ethernet1 | 1236::3 | 228671     |         | 0     |
     | 602054 | v1:6     | ethernet1 | 1236::3 | 228672     |         | 0     |
     | 602055 | v1:6     | ethernet1 | 1236::3 | 228673     |         | 0     |
     | 602056 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 602057 | null     | null      | null    | unlabelled |         | 0     |
     | 602058 | null     | null      | null    | unlabelled |         | 0     |
     | 602059 | null     | null      | null    | unlabelled |         | 0     |
     | 602060 | null     | null      | null    | unlabelled |         | 0     |
     | 602061 | null     | null      | null    | unlabelled |         | 0     |
     | 644966 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 661158 | null     | null      | null    | unlabelled |         | 0     |
     | 661159 | v1:4     | ethernet1 | 1.1.3.3 | 389006     |         | 0     |
     | 661160 | v1:4     | ethernet1 | 1.1.3.3 | 389007     |         | 0     |
     | 661161 | v1:4     | ethernet1 | 1.1.3.3 | 389008     |         | 0     |
     | 661162 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 661163 | null     | null      | null    | unlabelled |         | 0     |
     | 661164 | null     | null      | null    | unlabelled |         | 0     |
     | 661165 | null     | null      | null    | unlabelled |         | 0     |
     | 661166 | null     | null      | null    | unlabelled |         | 0     |
     | 661167 | null     | null      | null    | unlabelled |         | 0     |
     | 714696 | v1:4     | ethernet1 | 1.1.3.3 | 3          |         | 0     |
     | 920687 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 949393 | v1:4     | null      | null    | unlabelled | local   | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r4#
    r4#
    ```

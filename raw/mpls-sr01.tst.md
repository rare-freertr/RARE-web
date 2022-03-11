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
    logging file debug ../binTmp/zzz52r1-log.run
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
    logging file debug ../binTmp/zzz52r2-log.run
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
    logging file debug ../binTmp/zzz52r3-log.run
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
    logging file debug ../binTmp/zzz52r4-log.run
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
     | 24588   | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 108284  | null     | null      | null    | unlabelled |         | 0     |
     | 108285  | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 108286  | v1:4     | ethernet1 | 1.1.1.2 | 952392     |         | 0     |
     | 108287  | v1:4     | ethernet1 | 1.1.1.2 | 952393     |         | 0     |
     | 108288  | v1:4     | ethernet1 | 1.1.1.2 | 952394     |         | 0     |
     | 108289  | null     | null      | null    | unlabelled |         | 0     |
     | 108290  | null     | null      | null    | unlabelled |         | 0     |
     | 108291  | null     | null      | null    | unlabelled |         | 0     |
     | 108292  | null     | null      | null    | unlabelled |         | 0     |
     | 108293  | null     | null      | null    | unlabelled |         | 0     |
     | 178602  | v1:6     | ethernet1 | 1234::2 | 3          |         | 0     |
     | 573709  | null     | null      | null    | unlabelled |         | 0     |
     | 573710  | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 573711  | v1:6     | ethernet1 | 1234::2 | 168949     |         | 0     |
     | 573712  | v1:6     | ethernet1 | 1234::2 | 168950     |         | 0     |
     | 573713  | v1:6     | ethernet1 | 1234::2 | 168951     |         | 0     |
     | 573714  | null     | null      | null    | unlabelled |         | 0     |
     | 573715  | null     | null      | null    | unlabelled |         | 0     |
     | 573716  | null     | null      | null    | unlabelled |         | 0     |
     | 573717  | null     | null      | null    | unlabelled |         | 0     |
     | 573718  | null     | null      | null    | unlabelled |         | 0     |
     | 632674  | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 785360  | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 960848  | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 1000362 | v1:4     | ethernet1 | 1.1.1.2 | 3          |         | 0     |
     |_________|__________|___________|_________|____________|_________|_______|
    r1#
    r1#
    ```
    
    ```
    r2#
    r2#
    r2#show mpls forw
    r2#show mpls forw
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface     | hop     | label      | targets | bytes |
     |---------|----------|-----------|---------|------------|---------|-------|
     | 93298   | v1:4     | ethernet2 | 1.1.2.3 | 3          |         | 0     |
     | 168947  | null     | null      | null    | unlabelled |         | 0     |
     | 168948  | v1:6     | ethernet1 | 1234::1 | 573710     |         | 1280  |
     | 168949  | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 168950  | v1:6     | ethernet2 | 1235::3 | 918932     |         | 640   |
     | 168951  | v1:6     | ethernet2 | 1235::3 | 918933     |         | 640   |
     | 168952  | null     | null      | null    | unlabelled |         | 0     |
     | 168953  | null     | null      | null    | unlabelled |         | 0     |
     | 168954  | null     | null      | null    | unlabelled |         | 0     |
     | 168955  | null     | null      | null    | unlabelled |         | 0     |
     | 168956  | null     | null      | null    | unlabelled |         | 0     |
     | 627016  | v1:6     | ethernet1 | 1234::1 | 3          |         | 0     |
     | 708470  | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 747962  | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 766231  | v1:6     | ethernet2 | 1235::3 | 3          |         | 0     |
     | 947016  | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 952390  | null     | null      | null    | unlabelled |         | 0     |
     | 952391  | v1:4     | ethernet1 | 1.1.1.1 | 108285     |         | 1280  |
     | 952392  | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 952393  | v1:4     | ethernet2 | 1.1.2.3 | 876032     |         | 640   |
     | 952394  | v1:4     | ethernet2 | 1.1.2.3 | 876033     |         | 640   |
     | 952395  | null     | null      | null    | unlabelled |         | 0     |
     | 952396  | null     | null      | null    | unlabelled |         | 0     |
     | 952397  | null     | null      | null    | unlabelled |         | 0     |
     | 952398  | null     | null      | null    | unlabelled |         | 0     |
     | 952399  | null     | null      | null    | unlabelled |         | 0     |
     | 988979  | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 1008134 | v1:4     | ethernet1 | 1.1.1.1 | 3          |         | 0     |
     |_________|__________|___________|_________|____________|_________|_______|
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
     | 174577 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 255011 | v1:4     | ethernet2 | 1.1.3.4 | 3          |         | 0     |
     | 481546 | v1:6     | ethernet2 | 1236::4 | 3          |         | 0     |
     | 486092 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 588640 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 763732 | v1:4     | ethernet1 | 1.1.2.2 | 3          |         | 0     |
     | 766237 | v1:6     | ethernet1 | 1235::2 | 3          |         | 0     |
     | 876029 | null     | null      | null    | unlabelled |         | 0     |
     | 876030 | v1:4     | ethernet1 | 1.1.2.2 | 952391     |         | 640   |
     | 876031 | v1:4     | ethernet1 | 1.1.2.2 | 952392     |         | 640   |
     | 876032 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 876033 | v1:4     | ethernet2 | 1.1.3.4 | 451460     |         | 1280  |
     | 876034 | null     | null      | null    | unlabelled |         | 0     |
     | 876035 | null     | null      | null    | unlabelled |         | 0     |
     | 876036 | null     | null      | null    | unlabelled |         | 0     |
     | 876037 | null     | null      | null    | unlabelled |         | 0     |
     | 876038 | null     | null      | null    | unlabelled |         | 0     |
     | 918929 | null     | null      | null    | unlabelled |         | 0     |
     | 918930 | v1:6     | ethernet1 | 1235::2 | 168948     |         | 640   |
     | 918931 | v1:6     | ethernet1 | 1235::2 | 168949     |         | 640   |
     | 918932 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 918933 | v1:6     | ethernet2 | 1236::4 | 643118     |         | 1280  |
     | 918934 | null     | null      | null    | unlabelled |         | 0     |
     | 918935 | null     | null      | null    | unlabelled |         | 0     |
     | 918936 | null     | null      | null    | unlabelled |         | 0     |
     | 918937 | null     | null      | null    | unlabelled |         | 0     |
     | 918938 | null     | null      | null    | unlabelled |         | 0     |
     | 944181 | v1:4     | null      | null    | unlabelled | local   | 0     |
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
     | 54004  | v1:4     | null      | null    | unlabelled | local   | 0     |
     | 304712 | v1:4     | ethernet1 | 1.1.3.3 | 3          |         | 0     |
     | 451456 | null     | null      | null    | unlabelled |         | 0     |
     | 451457 | v1:4     | ethernet1 | 1.1.3.3 | 876030     |         | 0     |
     | 451458 | v1:4     | ethernet1 | 1.1.3.3 | 876031     |         | 0     |
     | 451459 | v1:4     | ethernet1 | 1.1.3.3 | 876032     |         | 0     |
     | 451460 | v1:4     | null      | null    | unlabelled | local   | 1920  |
     | 451461 | null     | null      | null    | unlabelled |         | 0     |
     | 451462 | null     | null      | null    | unlabelled |         | 0     |
     | 451463 | null     | null      | null    | unlabelled |         | 0     |
     | 451464 | null     | null      | null    | unlabelled |         | 0     |
     | 451465 | null     | null      | null    | unlabelled |         | 0     |
     | 571085 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 573116 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 628205 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 643114 | null     | null      | null    | unlabelled |         | 0     |
     | 643115 | v1:6     | ethernet1 | 1236::3 | 918930     |         | 0     |
     | 643116 | v1:6     | ethernet1 | 1236::3 | 918931     |         | 0     |
     | 643117 | v1:6     | ethernet1 | 1236::3 | 918932     |         | 0     |
     | 643118 | v1:6     | null      | null    | unlabelled | local   | 1920  |
     | 643119 | null     | null      | null    | unlabelled |         | 0     |
     | 643120 | null     | null      | null    | unlabelled |         | 0     |
     | 643121 | null     | null      | null    | unlabelled |         | 0     |
     | 643122 | null     | null      | null    | unlabelled |         | 0     |
     | 643123 | null     | null      | null    | unlabelled |         | 0     |
     | 934855 | v1:6     | ethernet1 | 1236::3 | 3          |         | 0     |
     |________|__________|___________|_________|____________|_________|_______|
    r4#
    r4#
    ```

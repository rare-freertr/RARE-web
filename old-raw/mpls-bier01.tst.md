# Example: bier in chain
    
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
    logging file debug ../binTmp/zzz18r1-log.run
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
     bier 256 10 1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     bier 256 10 1
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
     ipv6 address 1234::1 ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.4
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel key 1
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9999::9
     tunnel domain-name 4321::4
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1111 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
    logging file debug ../binTmp/zzz18r2-log.run
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
     bier 256 10 2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     bier 256 10 2
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
     ipv6 address 1234::2 ffff::
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
     ipv6 address 1235::2 ffff::
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
    logging file debug ../binTmp/zzz18r3-log.run
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
     bier 256 10 3
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     bier 256 10 3
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
     ipv6 address 1235::3 ffff::
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
     ipv6 address 1236::3 ffff::
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
    logging file debug ../binTmp/zzz18r4-log.run
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
     bier 256 10 4
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.4
     bier 256 10 4
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
     ipv6 address 1236::4 ffff::
     mpls enable
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel key 4
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.1
     tunnel mode bier
     vrf forwarding v1
     ipv4 address 3.3.3.4 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel key 4
     tunnel vrf v1
     tunnel source loopback1
     tunnel destination 9999::9
     tunnel domain-name 4321::1
     tunnel mode bier
     vrf forwarding v1
     ipv6 address 4321::1114 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0
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
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface | hop  | label      | targets | bytes |
     |--------|----------|-------|------|------------|---------|-------|
     | 125648 | v1:6     | null  | null | unlabelled | local   | 0     |
     | 569592 | tester:4 | null  | null | unlabelled | local   | 0     |
     | 654896 | tester:6 | null  | null | unlabelled | local   | 0     |
     | 772155 | v1:4     | null  | null | unlabelled | bier    | 520   |
     | 841965 | v1:6     | null  | null | unlabelled | bier    | 520   |
     | 886732 | v1:4     | null  | null | unlabelled | local   | 0     |
     |________|__________|_______|______|____________|_________|_______|
    r1#
    r1#
    ```
    
    ```
    r2#
    r2#
    r2#show mpls forw
    r2#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface | hop  | label      | targets | bytes |
     |--------|----------|-------|------|------------|---------|-------|
     | 213753 | tester:4 | null  | null | unlabelled | local   | 0     |
     | 360163 | v1:4     | null  | null | unlabelled | bier    | 1040  |
     | 393019 | v1:4     | null  | null | unlabelled | local   | 0     |
     | 611558 | v1:6     | null  | null | unlabelled | bier    | 1040  |
     | 713774 | tester:6 | null  | null | unlabelled | local   | 0     |
     | 864808 | v1:6     | null  | null | unlabelled | local   | 0     |
     |________|__________|_______|______|____________|_________|_______|
    r2#
    r2#
    ```
    
    ```
    r3#
    r3#
    r3#show mpls forw
    r3#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface | hop  | label      | targets | bytes |
     |--------|----------|-------|------|------------|---------|-------|
     | 131601 | tester:6 | null  | null | unlabelled | local   | 0     |
     | 205451 | v1:6     | null  | null | unlabelled | bier    | 1040  |
     | 309158 | v1:4     | null  | null | unlabelled | local   | 0     |
     | 342667 | v1:6     | null  | null | unlabelled | local   | 0     |
     | 402628 | tester:4 | null  | null | unlabelled | local   | 0     |
     | 428717 | v1:4     | null  | null | unlabelled | bier    | 1040  |
     |________|__________|_______|______|____________|_________|_______|
    r3#
    r3#
    ```
    
    ```
    r4#
    r4#
    r4#show mpls forw
    r4#show mpls forw
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface | hop  | label      | targets | bytes |
     |---------|----------|-------|------|------------|---------|-------|
     | 511709  | tester:6 | null  | null | unlabelled | local   | 0     |
     | 536126  | v1:4     | null  | null | unlabelled | local   | 0     |
     | 626443  | v1:4     | null  | null | unlabelled | bier    | 520   |
     | 787599  | tester:4 | null  | null | unlabelled | local   | 0     |
     | 800433  | v1:6     | null  | null | unlabelled | bier    | 520   |
     | 1047068 | v1:6     | null  | null | unlabelled | local   | 0     |
     |_________|__________|_______|______|____________|_________|_______|
    r4#
    r4#
    ```

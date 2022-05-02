# Example: te over ethernet
    
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
    logging file debug ../binTmp/zzz23r1-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.2
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::2
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 4321::1 ffff::
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
    logging file debug ../binTmp/zzz23r2-log.run
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
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 1234::2 ffff::
     ipv6 access-group-in test6
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1.1.1.1
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     tunnel vrf v1
     tunnel source ethernet1
     tunnel destination 1234::1
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 4321::2 ffff::
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
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label   | vrf      | iface | hop  | label      | targets | bytes |
     |---------|----------|-------|------|------------|---------|-------|
     | 53685   | tester:4 | null  | null | unlabelled | local   | 0     |
     | 55674   | tester:6 | null  | null | unlabelled | local   | 0     |
     | 374980  | v1:4     | null  | null | unlabelled | local   | 704   |
     | 380178  | tester:6 | null  | null | unlabelled | local   | 0     |
     | 709900  | tester:4 | null  | null | unlabelled | local   | 0     |
     | 922677  | tester:6 | null  | null | unlabelled | local   | 0     |
     | 956785  | v1:4     | null  | null | unlabelled | local   | 0     |
     | 969364  | v1:6     | null  | null | unlabelled | local   | 640   |
     | 997018  | v1:6     | null  | null | unlabelled | local   | 0     |
     | 1006830 | tester:4 | null  | null | unlabelled | local   | 0     |
     |_________|__________|_______|______|____________|_________|_______|
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
     | 1.1.1.2 | 19077 | ::       | 0  | 1.1.1.1 | 1095340475 | r2:tunnel1  |
     | 1.1.1.1 | 25422 | ::       | 0  | 1.1.1.2 | 321589599  | r1:tunnel1  |
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
     | 1234::2 | 300   | ::       | 0  | 1234::1 | 232677510  | r2:tunnel2  |
     | 1234::1 | 13824 | ::       | 0  | 1234::2 | 1276375965 | r1:tunnel2  |
     |_________|_______|__________|____|_________|____________|_____________|
    r1#
    r1#
    ```

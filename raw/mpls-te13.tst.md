# Example: p2mp te
    
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
    logging file debug ../binTmp/zzz10r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.11.1 255.255.255.0
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 9.9.9.9
     tunnel domain-name 2.2.2.2 2.2.2.3
     tunnel mode p2mpte
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 9999::9
     tunnel domain-name 4321::2 4321::3
     tunnel mode p2mpte
     vrf forwarding v1
     ipv6 address 3333::1 ffff:ffff::
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.11.2
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
    logging file debug ../binTmp/zzz10r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.12.1 255.255.255.0
     ipv6 address 1234:2::1 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.1
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::1
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 3333::2 ffff:ffff::
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.12.2
    !
    ipv6 route v1 :: :: 1234:2::2
    !
    !
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
    logging file debug ../binTmp/zzz10r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.13.1 255.255.255.0
     ipv6 address 1234:3::1 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.1
     tunnel mode p2pte
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::1
     tunnel mode p2pte
     vrf forwarding v1
     ipv6 address 3333::3 ffff:ffff::
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.13.2
    !
    ipv6 route v1 :: :: 1234:3::2
    !
    !
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
    logging file debug ../binTmp/zzz10r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.11.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.12.2 255.255.255.0
     ipv6 address 1234:2::2 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     vrf forwarding v1
     ipv4 address 1.1.13.2 255.255.255.0
     ipv6 address 1234:3::2 ffff:ffff::
     mpls enable
     mpls rsvp4
     mpls rsvp6
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
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.11.1
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.12.1
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.13.1
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
    !
    !
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
     |~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|
     | label   | vrf      | iface     | hop       | label      | targets | bytes   |
     |---------|----------|-----------|-----------|------------|---------|---------|
     | 200108  | v1:4     | null      | null      | unlabelled | local   | 1810560 |
     | 237020  | v1:4     | null      | null      | unlabelled | local   | 703680  |
     | 285238  | v1:4     | ethernet1 | 1.1.11.2  | unlabelled |         | 0       |
     | 291722  | tester:4 | null      | null      | unlabelled | local   | 0       |
     | 295911  | v1:6     | null      | null      | unlabelled | local   | 1060864 |
     | 386842  | tester:6 | null      | null      | unlabelled | local   | 0       |
     | 504515  | v1:6     | null      | null      | unlabelled | local   | 0       |
     | 561712  | v1:4     | null      | null      | unlabelled | local   | 0       |
     | 787163  | v1:6     | ethernet1 | 1234:1::2 | unlabelled |         | 0       |
     | 1021945 | v1:6     | null      | null      | unlabelled | local   | 330944  |
     |_________|__________|___________|___________|____________|_________|_________|
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
     | 2.2.2.1 | 400   | 2.2.2.2  | 1  | 2.2.2.2 | 26214400   | r1:tunnel1  |
     | 2.2.2.1 | 400   | 2.2.2.3  | 2  | 2.2.2.3 | 26214401   | r1:tunnel1  |
     | 2.2.2.3 | 1449  | ::       | 0  | 2.2.2.1 | 1755653850 | r3:tunnel1  |
     | 2.2.2.2 | 28689 | ::       | 0  | 2.2.2.1 | 885979655  | r2:tunnel1  |
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
     | 4321::2 | 1640  | ::       | 0  | 4321::1 | 1768845825 | r2:tunnel2  |
     | 4321::3 | 15789 | ::       | 0  | 4321::1 | 1012161185 | r3:tunnel2  |
     | 4321::1 | 29753 | 4321::2  | 1  | 4321::2 | 1949892608 | r1:tunnel2  |
     | 4321::1 | 29753 | 4321::3  | 2  | 4321::3 | 1949892609 | r1:tunnel2  |
     |_________|_______|__________|____|_________|____________|_____________|
    r1#
    r1#
    ```

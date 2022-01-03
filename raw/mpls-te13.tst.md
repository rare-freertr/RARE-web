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
    logging file debug ../binTmp/zzz1r1-log.run
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
    logging file debug ../binTmp/zzz1r2-log.run
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
    logging file debug ../binTmp/zzz1r3-log.run
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
    logging file debug ../binTmp/zzz1r4-log.run
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
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|
     | label  | vrf      | iface     | hop       | label      | targets | bytes   |
     |--------|----------|-----------|-----------|------------|---------|---------|
     | 69934  | v1:6     | null      | null      | unlabelled | local   | 220864  |
     | 138162 | v1:4     | ethernet1 | 1.1.11.2  | unlabelled |         | 0       |
     | 239173 | tester:6 | null      | null      | unlabelled | local   | 0       |
     | 339748 | v1:4     | null      | null      | unlabelled | local   | 451904  |
     | 590057 | tester:4 | null      | null      | unlabelled | local   | 0       |
     | 601997 | v1:6     | null      | null      | unlabelled | local   | 433024  |
     | 668518 | v1:4     | null      | null      | unlabelled | local   | 1262912 |
     | 852460 | v1:6     | ethernet1 | 1234:1::2 | unlabelled |         | 0       |
     | 884215 | v1:6     | null      | null      | unlabelled | local   | 0       |
     | 913242 | v1:4     | null      | null      | unlabelled | local   | 0       |
     |________|__________|___________|___________|____________|_________|_________|
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
     | 2.2.2.1 | 3434  | 2.2.2.2  | 1  | 2.2.2.2 | 225050624  | r1:tunnel1  |
     | 2.2.2.1 | 3434  | 2.2.2.3  | 2  | 2.2.2.3 | 225050625  | r1:tunnel1  |
     | 2.2.2.3 | 4007  | ::       | 0  | 2.2.2.1 | 1934900783 | r3:tunnel1  |
     | 2.2.2.2 | 23362 | ::       | 0  | 2.2.2.1 | 287938838  | r2:tunnel1  |
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
     | 4321::2 | 12001 | ::       | 0  | 4321::1 | 301905321  | r2:tunnel2  |
     | 4321::1 | 14434 | 4321::2  | 1  | 4321::2 | 945946624  | r1:tunnel2  |
     | 4321::1 | 14434 | 4321::3  | 2  | 4321::3 | 945946625  | r1:tunnel2  |
     | 4321::3 | 15484 | ::       | 0  | 4321::1 | 2000963083 | r3:tunnel2  |
     |_________|_______|__________|____|_________|____________|_____________|
    r1#
    r1#
    ```

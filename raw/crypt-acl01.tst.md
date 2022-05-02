# Example: ingress protocol matching access list
    
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
    logging file debug ../binTmp/zzz65r1-log.run
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
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv4 access-group-in test4
     ipv6 address 1234::1 ffff:ffff::
     ipv6 access-group-in test6
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
    logging file debug ../binTmp/zzz65r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234::2 ffff:ffff::
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
    r1#show access-list test4
    r1#show access-list test4
     |~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|
     |     | tx          | rx          | timers              |                     |
     | seq | byte | pack | byte | pack | last     | timout   | cfg                 |
     |-----|------|------|------|------|----------|----------|---------------------|
     | 10  | 0    | 0    | 256  | 4    | 00:00:06 | 00:00:00 | 1 any all any all   |
     | 20  | 0    | 0    | 0    | 0    | never    | 00:00:00 | all any all any all |
     |_____|______|______|______|______|__________|__________|_____________________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show access-list test6
    r1#show access-list test6
     |~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~|
     |     | tx          | rx          | timers              |                     |
     | seq | byte | pack | byte | pack | last     | timout   | cfg                 |
     |-----|------|------|------|------|----------|----------|---------------------|
     | 10  | 0    | 0    | 608  | 8    | 00:00:01 | 00:00:00 | 58 any all any all  |
     | 20  | 0    | 0    | 0    | 0    | never    | 00:00:00 | all any all any all |
     |_____|______|______|______|______|__________|__________|_____________________|
    r1#
    r1#
    ```

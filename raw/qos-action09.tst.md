# Example: qos ingress bandwidth action
    
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
    logging file debug ../binTmp/zzz63r1-log.run
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
     ipv6 address 1234::1 ffff::
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
    logging file debug ../binTmp/zzz63r2-log.run
    !
    policy-map p1
     sequence 10 action bandwidth
     sequence 10 access-rate 81920
     !
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
     service-policy-in p1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
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
    r2#show policy int eth1 in
    r2#show policy int eth1 in
     |~~~~~|~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
     | seq | chld | queue | intrvl | byt/int | rxb   | rxp | trnsmt                               |
     |-----|------|-------|--------|---------|-------|-----|--------------------------------------|
     | 10  | 0    | 0/128 | 100    | 1024    | 42014 | 418 | tx=42014(418) rx=42014(418) drp=0(0) |
     |_____|______|_______|________|_________|_______|_____|______________________________________|
    r2#
    r2#
    ```

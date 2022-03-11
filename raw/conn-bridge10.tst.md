# Example: bridge with spantree
    
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
    logging file debug ../binTmp/zzz70r1-log.run
    !
    bridge 1
     mac-learn
     stp-priority 40960
     stp-mode ieee
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4
     no description
     bridge-group 1
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
    logging file debug ../binTmp/zzz70r2-log.run
    !
    bridge 1
     mac-learn
     stp-priority 20480
     stp-mode ieee
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4
     no description
     bridge-group 1
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

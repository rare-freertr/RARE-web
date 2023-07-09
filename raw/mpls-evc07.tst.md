# Example: xconnect evcs terminated on pwhes
    
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
    logging file debug ../binTmp/zzz49r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1111::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1112::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.13
     vrf forwarding v1
     ipv4 address 1.1.3.1 255.255.255.0
     ipv6 address 1113::1 ffff::
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
    logging file debug ../binTmp/zzz49r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     service-instance 11 xconnect v1 ethernet2 vxlan 2.2.2.2 123
     service-instance 12 xconnect v1 ethernet2 geneve 2.2.2.2 123
     service-instance 13 xconnect v1 ethernet2 etherip 2.2.2.2 123
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.0
     ipv6 address 2222::1 ffff::
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
    logging file debug ../binTmp/zzz49r3-log.run
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
     ipv4 address 2.2.2.2 255.255.255.0
     ipv6 address 2222::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface pwether11
     mtu 1500
     macaddr 0064.7a45.4132
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1111::2 ffff::
     pseudowire v1 ethernet1 vxlan 2.2.2.1 123
     no shutdown
     no log-link-change
     exit
    !
    interface pwether12
     mtu 1500
     macaddr 0044.474e.262e
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1112::2 ffff::
     pseudowire v1 ethernet1 geneve 2.2.2.1 123
     no shutdown
     no log-link-change
     exit
    !
    interface pwether13
     mtu 1500
     macaddr 005d.702c.4475
     vrf forwarding v1
     ipv4 address 1.1.3.2 255.255.255.0
     ipv6 address 1113::2 ffff::
     pseudowire v1 ethernet1 etherip 2.2.2.1 123
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

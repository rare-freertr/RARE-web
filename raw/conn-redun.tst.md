# Example: process redundancy
    
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
    logging file debug ../binTmp/zzz89r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
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
    ipv4 route v1 2.2.2.0 255.255.255.0 1.1.1.3
    !
    ipv6 route v1 4321:: ffff:: 1234::3
    !
    !
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
    logging file debug ../binTmp/zzz89r2-log.run
    !
    bridge 1
     exit
    !
    bridge 34
     mac-learn
     block-unicast
     exit
    !
    bridge 35
     mac-learn
     block-unicast
     exit
    !
    bridge 45
     mac-learn
     block-unicast
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
     no shutdown
     no log-link-change
     exit
    !
    interface bvi34
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface bvi35
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface bvi45
     no description
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
     shutdown
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
    interface ethernet31
     no description
     bridge-group 34
     shutdown
     no log-link-change
     exit
    !
    interface ethernet32
     no description
     bridge-group 35
     shutdown
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
    interface ethernet41
     no description
     bridge-group 34
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet42
     no description
     bridge-group 45
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet51
     no description
     bridge-group 35
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet52
     no description
     bridge-group 45
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
    logging file debug ../binTmp/zzz89r3-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.3 255.255.255.0
     ipv6 addr 4321::3 ffff::
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.3 255.255.255.0
     ipv6 addr 1234::3 ffff::
     exit
    ```
    
    **r4:**
    ```
    hostname r4
    logging file debug ../binTmp/zzz89r4-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.4 255.255.255.0
     ipv6 addr 4321::4 ffff::
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.3 255.255.255.0
     ipv6 addr 1234::3 ffff::
     exit
    ```
    
    **r5:**
    ```
    hostname r5
    logging file debug ../binTmp/zzz89r5-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.5 255.255.255.0
     ipv6 addr 4321::5 ffff::
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.3 255.255.255.0
     ipv6 addr 1234::3 ffff::
     exit
    ```

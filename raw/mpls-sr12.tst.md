# Example: bgp with php labels over sr
    
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
    logging file debug ../binTmp/zzz48r1-log.run
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
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     segrout 10 1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    interface pwether1
     mtu 1500
     macaddr 0057.5f00.1529
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     pseudowire v1 loopback2 pweompls 2.2.2.13 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0026.6100.305c
     vrf forwarding v1
     ipv4 address 3.3.4.1 255.255.255.0
     pseudowire v1 loopback2 pweompls 4321::13 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family labeled
     neighbor 2.2.2.3 remote-as 1
     neighbor 2.2.2.3 local-as 1
     neighbor 2.2.2.3 address-family labeled
     neighbor 2.2.2.3 distance 200
     neighbor 2.2.2.3 update-source loopback1
     neighbor 2.2.2.3 label-pop
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family labeled
     neighbor 4321::3 remote-as 1
     neighbor 4321::3 local-as 1
     neighbor 4321::3 address-family labeled
     neighbor 4321::3 distance 200
     neighbor 4321::3 update-source loopback1
     neighbor 4321::3 label-pop
     redistribute connected
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
    logging file debug ../binTmp/zzz48r2-log.run
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
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    logging file debug ../binTmp/zzz48r3-log.run
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
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.3
     segrout 10 3
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.13 255.255.255.255
     ipv6 address 4321::13 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    interface pwether1
     mtu 1500
     macaddr 0006.4c6c.6a59
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     pseudowire v1 loopback2 pweompls 2.2.2.11 1234
     no shutdown
     no log-link-change
     exit
    !
    interface pwether2
     mtu 1500
     macaddr 0034.3938.1022
     vrf forwarding v1
     ipv4 address 3.3.4.2 255.255.255.0
     pseudowire v1 loopback2 pweompls 4321::11 1234
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.3
     address-family labeled
     neighbor 2.2.2.1 remote-as 1
     neighbor 2.2.2.1 local-as 1
     neighbor 2.2.2.1 address-family labeled
     neighbor 2.2.2.1 distance 200
     neighbor 2.2.2.1 update-source loopback1
     neighbor 2.2.2.1 label-pop
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.3
     address-family labeled
     neighbor 4321::1 remote-as 1
     neighbor 4321::1 local-as 1
     neighbor 4321::1 address-family labeled
     neighbor 4321::1 distance 200
     neighbor 4321::1 update-source loopback1
     neighbor 4321::1 label-pop
     redistribute connected
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

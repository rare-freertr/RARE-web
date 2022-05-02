# Example: vrf route limit
    
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
    logging file debug ../binTmp/zzz41r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.1111.00
     traffeng-id ::
     is-type level2
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.21 255.255.255.255
     ipv6 address 4321::21 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
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
    logging file debug ../binTmp/zzz41r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.1111.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.1111.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.22 255.255.255.255
     ipv6 address 4321::22 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.32 255.255.255.255
     ipv6 address 4321::32 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback4
     vrf forwarding v1
     ipv4 address 2.2.2.42 255.255.255.255
     ipv6 address 4321::42 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback5
     vrf forwarding v1
     ipv4 address 2.2.2.52 255.255.255.255
     ipv6 address 4321::52 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback6
     vrf forwarding v1
     ipv4 address 2.2.2.62 255.255.255.255
     ipv6 address 4321::62 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback7
     vrf forwarding v1
     ipv4 address 2.2.2.72 255.255.255.255
     ipv6 address 4321::72 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback8
     vrf forwarding v1
     ipv4 address 2.2.2.82 255.255.255.255
     ipv6 address 4321::82 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback9
     vrf forwarding v1
     ipv4 address 9.9.9.9 255.255.255.255
     ipv6 address 9999::9 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:1::2 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
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

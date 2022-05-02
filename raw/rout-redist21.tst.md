# Example: redistribution prefix movement
    
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
    logging file debug ../binTmp/zzz68r1-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 10
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
    router isis4 1
     vrf v1
     net-id 11.4444.0000.1111.00
     traffeng-id ::
     is-type level2
     advertise 2.2.2.1/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router isis6 1
     vrf v1
     net-id 11.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     advertise 4321::1/128 route-map rm1
     advertise 4321::222/128 route-map rm1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.101 255.255.255.255
     ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    logging file debug ../binTmp/zzz68r2-log.run
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
     net-id 22.4444.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis4 2
     exit
    !
    router isis4 2
     vrf v1
     net-id 22.4444.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis4 1
     exit
    !
    router isis6 1
     vrf v1
     net-id 22.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis6 2
     exit
    !
    router isis6 2
     vrf v1
     net-id 22.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis6 1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 enable
     router isis6 1 circuit level2
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
    interface ethernet2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     router isis4 2 enable
     router isis4 2 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     vrf forwarding v1
     ipv6 address 1234:2::1 ffff:ffff::
     router isis6 2 enable
     router isis6 2 circuit level2
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
    logging file debug ../binTmp/zzz68r3-log.run
    !
    route-map rm1
     sequence 10 action permit
     sequence 10 set metric set 20
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
    router isis4 1
     vrf v1
     net-id 33.4444.0000.3333.00
     traffeng-id ::
     is-type level2
     advertise 2.2.2.3/32 route-map rm1
     advertise 2.2.2.222/32 route-map rm1
     exit
    !
    router isis6 1
     vrf v1
     net-id 33.6666.0000.3333.00
     traffeng-id ::
     is-type level2
     advertise 4321::3/128 route-map rm1
     advertise 4321::222/128 route-map rm1
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback2
     vrf forwarding v1
     ipv4 address 2.2.2.222 255.255.255.255
     ipv6 address 4321::222 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface loopback3
     vrf forwarding v1
     ipv4 address 2.2.2.103 255.255.255.255
     ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     ipv4 address 1.1.1.6 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv6 address 1234:2::2 ffff:ffff::
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
    server telnet tel
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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

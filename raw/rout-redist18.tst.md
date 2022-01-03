# Example: redistribution with everything
    
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
     rt-import 1:2
     rt-export 1:2
     exit
    !
    vrf definition v2
     rd 1:2
     label-mode per-prefix
     exit
    !
    router rip4 1
     vrf v1
     redistribute connected
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router rip6 1
     vrf v1
     redistribute connected
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router babel4 1
     vrf v1
     router-id 1111-2222-3333-0001
     redistribute connected
     redistribute rip4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0001
     redistribute connected
     redistribute rip6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router olsr4 1
     vrf v1
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router olsr6 1
     vrf v1
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router ospf4 1
     vrf v1
     router-id 4.4.4.1
     traffeng-id 0.0.0.0
     area 0 enable
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.1
     traffeng-id ::
     area 0 enable
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.1111.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.1111.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute eigrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute eigrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    router eigrp4 1
     vrf v1
     router-id 4.4.4.1
     as 1
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute bgp4 1
     redistribute bgp4 2
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.1
     as 1
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute bgp6 1
     redistribute bgp6 2
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:1::1 ffff:ffff::
     router isis6 1 enable
     router isis6 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet10
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet10.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.37 255.255.255.252
     router olsr4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet10.12
     no description
     vrf forwarding v1
     ipv6 address 1234:10::1 ffff:ffff::
     router olsr6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     router ospf4 1 enable
     router ospf4 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2.12
     no description
     vrf forwarding v1
     ipv6 address 1234:2::1 ffff:ffff::
     router ospf6 1 enable
     router ospf6 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     router rip4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3.12
     no description
     vrf forwarding v1
     ipv6 address 1234:3::1 ffff:ffff::
     router rip6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.13 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet4.12
     no description
     vrf forwarding v1
     ipv6 address 1234:4::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet5
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet5.11
     no description
     vrf forwarding v2
     ipv4 address 1.1.1.17 255.255.255.252
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet5.12
     no description
     vrf forwarding v2
     ipv6 address 1234:5::1 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet6
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet6.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.21 255.255.255.252
     router pvrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet6.12
     no description
     vrf forwarding v1
     ipv6 address 1234:6::1 ffff:ffff::
     router pvrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet7
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet7.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.25 255.255.255.252
     router eigrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet7.12
     no description
     vrf forwarding v1
     ipv6 address 1234:7::1 ffff:ffff::
     router eigrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet8
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet8.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.29 255.255.255.252
     router babel4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet8.12
     no description
     vrf forwarding v1
     ipv6 address 1234:8::1 ffff:ffff::
     router babel6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet9
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet9.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.33 255.255.255.252
     router lsrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet9.12
     no description
     vrf forwarding v1
     ipv6 address 1234:9::1 ffff:ffff::
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 1
     router-id 4.4.4.1
     address-family unicast
     neighbor 1.1.1.14 remote-as 2
     no neighbor 1.1.1.14 description
     neighbor 1.1.1.14 local-as 1
     neighbor 1.1.1.14 address-family unicast
     neighbor 1.1.1.14 distance 20
     redistribute connected
     redistribute rip4 1
     redistribute babel4 1
     redistribute olsr4 1
     redistribute ospf4 1
     redistribute isis4 1
     redistribute pvrp4 1
     redistribute lsrp4 1
     redistribute eigrp4 1
     redistribute bgp4 2
     exit
    !
    router bgp4 2
     vrf v2
     local-as 1
     router-id 4.4.4.1
     address-family vpnuni
     neighbor 1.1.1.18 remote-as 3
     no neighbor 1.1.1.18 description
     neighbor 1.1.1.18 local-as 1
     neighbor 1.1.1.18 address-family vpnuni
     neighbor 1.1.1.18 distance 20
     neighbor 1.1.1.18 send-community standard extended
     afi-vrf v1 enable
     afi-vrf v1 redistribute connected
     afi-vrf v1 redistribute rip4 1
     afi-vrf v1 redistribute babel4 1
     afi-vrf v1 redistribute olsr4 1
     afi-vrf v1 redistribute ospf4 1
     afi-vrf v1 redistribute isis4 1
     afi-vrf v1 redistribute pvrp4 1
     afi-vrf v1 redistribute lsrp4 1
     afi-vrf v1 redistribute eigrp4 1
     afi-vrf v1 redistribute bgp4 1
     exit
    !
    router bgp6 1
     vrf v1
     local-as 1
     router-id 6.6.6.1
     address-family unicast
     neighbor 1234:4::2 remote-as 2
     no neighbor 1234:4::2 description
     neighbor 1234:4::2 local-as 1
     neighbor 1234:4::2 address-family unicast
     neighbor 1234:4::2 distance 20
     redistribute connected
     redistribute rip6 1
     redistribute babel6 1
     redistribute olsr6 1
     redistribute ospf6 1
     redistribute isis6 1
     redistribute pvrp6 1
     redistribute lsrp6 1
     redistribute eigrp6 1
     redistribute bgp6 2
     exit
    !
    router bgp6 2
     vrf v2
     local-as 1
     router-id 6.6.6.2
     address-family vpnuni
     neighbor 1234:5::2 remote-as 3
     no neighbor 1234:5::2 description
     neighbor 1234:5::2 local-as 1
     neighbor 1234:5::2 address-family vpnuni
     neighbor 1234:5::2 distance 20
     neighbor 1234:5::2 send-community standard extended
     afi-vrf v1 enable
     afi-vrf v1 redistribute connected
     afi-vrf v1 redistribute rip6 1
     afi-vrf v1 redistribute babel6 1
     afi-vrf v1 redistribute olsr6 1
     afi-vrf v1 redistribute ospf6 1
     afi-vrf v1 redistribute isis6 1
     afi-vrf v1 redistribute pvrp6 1
     afi-vrf v1 redistribute lsrp6 1
     afi-vrf v1 redistribute eigrp6 1
     afi-vrf v1 redistribute bgp6 1
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
    !
    !
    !
    !
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
     exit
    !
    router isis4 1
     vrf v1
     net-id 48.4444.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis4 2
     exit
    !
    router isis6 1
     vrf v1
     net-id 48.6666.0000.2222.00
     traffeng-id ::
     is-type level2
     redistribute connected
     redistribute isis6 2
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     router isis4 1 enable
     router isis4 1 circuit level2
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
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
     exit
    !
    router ospf4 1
     vrf v1
     router-id 4.4.4.3
     traffeng-id 0.0.0.0
     area 0 enable
     redistribute connected
     exit
    !
    router ospf6 1
     vrf v1
     router-id 6.6.6.3
     traffeng-id ::
     area 0 enable
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     router ospf4 1 enable
     router ospf4 1 area 0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:2::2 ffff:ffff::
     router ospf6 1 enable
     router ospf6 1 area 0
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
     exit
    !
    router rip4 1
     vrf v1
     redistribute connected
     exit
    !
    router rip6 1
     vrf v1
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     router rip4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:3::2 ffff:ffff::
     router rip6 1 enable
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
    
    **r5:**
    ```
    hostname r5
    buggy
    !
    logging file debug ../binTmp/zzz1r5-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.5 255.255.255.255
     ipv6 address 4321::5 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.14 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:4::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 1
     vrf v1
     local-as 2
     router-id 4.4.4.5
     address-family unicast
     neighbor 1.1.1.13 remote-as 1
     no neighbor 1.1.1.13 description
     neighbor 1.1.1.13 local-as 2
     neighbor 1.1.1.13 address-family unicast
     neighbor 1.1.1.13 distance 20
     redistribute connected
     exit
    !
    router bgp6 1
     vrf v1
     local-as 2
     router-id 6.6.6.5
     address-family unicast
     neighbor 1234:4::1 remote-as 1
     no neighbor 1234:4::1 description
     neighbor 1234:4::1 local-as 2
     neighbor 1234:4::1 address-family unicast
     neighbor 1234:4::1 distance 20
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
    
    **r6:**
    ```
    hostname r6
    buggy
    !
    logging file debug ../binTmp/zzz1r6-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     rt-import 1:2
     rt-export 1:2
     exit
    !
    vrf definition v2
     rd 1:2
     label-mode per-prefix
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.6 255.255.255.255
     ipv6 address 4321::6 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v2
     ipv4 address 1.1.1.18 255.255.255.252
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v2
     ipv6 address 1234:5::2 ffff:ffff::
     mpls enable
     no shutdown
     no log-link-change
     exit
    !
    router bgp4 2
     vrf v2
     local-as 3
     router-id 4.4.4.6
     address-family vpnuni
     neighbor 1.1.1.17 remote-as 1
     no neighbor 1.1.1.17 description
     neighbor 1.1.1.17 local-as 3
     neighbor 1.1.1.17 address-family vpnuni
     neighbor 1.1.1.17 distance 20
     neighbor 1.1.1.17 send-community standard extended
     afi-vrf v1 enable
     afi-vrf v1 redistribute connected
     exit
    !
    router bgp6 2
     vrf v2
     local-as 3
     router-id 6.6.6.6
     address-family vpnuni
     neighbor 1234:5::1 remote-as 1
     no neighbor 1234:5::1 description
     neighbor 1234:5::1 local-as 3
     neighbor 1234:5::1 address-family vpnuni
     neighbor 1234:5::1 distance 20
     neighbor 1234:5::1 send-community standard extended
     afi-vrf v1 enable
     afi-vrf v1 redistribute connected
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
    !
    !
    !
    !
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
    
    **r7:**
    ```
    hostname r7
    buggy
    !
    logging file debug ../binTmp/zzz1r7-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.7
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.7
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.7 255.255.255.255
     ipv6 address 4321::7 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.22 255.255.255.252
     router pvrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:6::2 ffff:ffff::
     router pvrp6 1 enable
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
    
    **r8:**
    ```
    hostname r8
    buggy
    !
    logging file debug ../binTmp/zzz1r8-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router eigrp4 1
     vrf v1
     router-id 4.4.4.8
     as 1
     redistribute connected
     exit
    !
    router eigrp6 1
     vrf v1
     router-id 6.6.6.8
     as 1
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.8 255.255.255.255
     ipv6 address 4321::8 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.26 255.255.255.252
     router eigrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:7::2 ffff:ffff::
     router eigrp6 1 enable
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
    
    **r9:**
    ```
    hostname r9
    buggy
    !
    logging file debug ../binTmp/zzz1r9-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router babel4 1
     vrf v1
     router-id 1111-2222-3333-0009
     redistribute connected
     exit
    !
    router babel6 1
     vrf v1
     router-id 1111-2222-3333-0009
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.9 255.255.255.255
     ipv6 address 4321::9 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.30 255.255.255.252
     router babel4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:8::2 ffff:ffff::
     router babel6 1 enable
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
    
    **r10:**
    ```
    hostname r10
    buggy
    !
    logging file debug ../binTmp/zzz1r10-log.run
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
     router-id 4.4.4.10
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.10
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.10 255.255.255.255
     ipv6 address 4321::10 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.34 255.255.255.252
     router lsrp4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:9::2 ffff:ffff::
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
    
    **r11:**
    ```
    hostname r11
    buggy
    !
    logging file debug ../binTmp/zzz1r11-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router olsr4 1
     vrf v1
     redistribute connected
     exit
    !
    router olsr6 1
     vrf v1
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.38 255.255.255.252
     router olsr4 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     no description
     vrf forwarding v1
     ipv6 address 1234:10::2 ffff:ffff::
     router olsr6 1 enable
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

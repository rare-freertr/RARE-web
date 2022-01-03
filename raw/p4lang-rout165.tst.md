# Example: p4lang: bier vlan egress edge
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz1r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    vrf def v9
     rd 1:1
     exit
    int lo9
     vrf for v9
     ipv4 addr 10.10.10.227 255.255.255.255
     exit
    int eth1
     vrf for v9
     ipv4 addr 10.11.12.254 255.255.255.0
     exit
    int eth2
     exit
    server dhcp4 eth1
     pool 10.11.12.1 10.11.12.99
     gateway 10.11.12.254
     netmask 255.255.255.0
     dns-server 10.10.10.227
     domain-name p4l
     static 0000.0000.2222 10.11.12.111
     interface eth1
     vrf v9
     exit
    router lsrp4 1
     vrf v1
     router 4.4.4.1
     bier 256 10 1
     red conn
     exit
    router lsrp6 1
     vrf v1
     router 6.6.6.1
     bier 256 10 1
     red conn
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.101 255.255.255.255
     ipv6 addr 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     ipv4 pim ena
     ipv6 pim ena
     ipv4 pim join lo0
     ipv6 pim join lo0
     ipv4 pim bier 1
     ipv6 pim bier 1
     exit
    int sdn1
     exit
    int sdn1.111
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234:1::1 ffff:ffff::
     ipv6 ena
     router lsrp4 1 ena
     router lsrp6 1 ena
     ipv4 multi static 232.2.2.2 2.2.2.106
     ipv6 multi static ff06::1 4321::106
     exit
    int sdn2
     exit
    int sdn2.222
     vrf for v1
     ipv4 addr 1.1.2.1 255.255.255.0
     ipv6 addr 1234:2::1 ffff:ffff::
     ipv6 ena
     mpls enable
     router lsrp4 1 ena
     router lsrp6 1 ena
     ipv4 pim ena
     ipv6 pim ena
     ipv4 pim join lo0
     ipv6 pim join lo0
     ipv4 pim bier 1
     ipv6 pim bier 1
     exit
    int sdn3
     exit
    int sdn3.333
     vrf for v1
     ipv4 addr 1.1.3.1 255.255.255.0
     ipv6 addr 1234:3::1 ffff:ffff::
     ipv6 ena
     mpls enable
     router lsrp4 1 ena
     router lsrp6 1 ena
     ipv4 pim ena
     ipv6 pim ena
     ipv4 pim join lo0
     ipv6 pim join lo0
     ipv4 pim bier 1
     ipv6 pim bier 1
     exit
    int sdn4
     exit
    int sdn4.444
     vrf for v1
     ipv4 addr 1.1.4.1 255.255.255.0
     ipv6 addr 1234:4::1 ffff:ffff::
     ipv6 ena
     mpls enable
     router lsrp4 1 ena
     router lsrp6 1 ena
     ipv4 pim ena
     ipv6 pim ena
     ipv4 pim join lo0
     ipv6 pim join lo0
     ipv4 pim bier 1
     ipv6 pim bier 1
     exit
    ipv4 mroute v1 0.0.0.0 0.0.0.0 1.1.4.2
    ipv6 mroute v1 :: :: 1234:4::2
    server p4lang p4
     interconnect eth2
     export-vrf v1 1
     export-port sdn1 1
     export-port sdn2 2
     export-port sdn3 3
     export-port sdn4 4
     export-port sdn1.111 111
     export-port sdn2.222 222
     export-port sdn3.333 333
     export-port sdn4.444 444
     vrf v9
     exit
    ```
# Example: interop9: ospf te
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz74r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    router ospf4 1
     vrf v1
     router 4.4.4.1
     traffeng 2.2.2.1
     area 0 ena
     area 0 traff
     red conn
     exit
    router ospf6 1
     vrf v1
     router 6.6.6.1
     traffeng 6.6.6.1
     area 0 ena
     area 0 traff
     red conn
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr fe80::1 ffff::
     router ospf4 1 ena
     router ospf6 1 ena
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int tun1
     bandwidth 11
     tun sou eth1
     tun dest 2.2.2.2
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 3.3.3.1 255.255.255.252
     exit
    int tun2
     bandwidth 11
     tun sou eth1
     tun dest 2.2.2.3
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 3.3.3.9 255.255.255.252
     exit
    ```

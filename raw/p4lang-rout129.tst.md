# Example: p4lang: p2p te tail+head
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz67r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     label-mode per-prefix
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
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.101 255.255.255.255
     ipv6 addr 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     mpls rsvp4
     mpls rsvp6
     exit
    int lo1
     vrf for v1
     ipv4 addr 2.2.2.201 255.255.255.255
     ipv6 addr 4321::201 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int sdn1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234:1::1 ffff:ffff::
     ipv6 ena
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int sdn2
     vrf for v1
     ipv4 addr 1.1.2.1 255.255.255.0
     ipv6 addr 1234:2::1 ffff:ffff::
     ipv6 ena
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int sdn3
     vrf for v1
     ipv4 addr 1.1.3.1 255.255.255.0
     ipv6 addr 1234:3::1 ffff:ffff::
     ipv6 ena
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int sdn4
     vrf for v1
     ipv4 addr 1.1.4.1 255.255.255.0
     ipv6 addr 1234:4::1 ffff:ffff::
     ipv6 ena
     mpls enable
     mpls rsvp4
     mpls rsvp6
     exit
    int tun11
     tun sou lo0
     tun dest 2.2.2.103
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 1.1.11.1 255.255.255.0
     exit
    int tun12
     tun sou lo0
     tun dest 4321::103
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv6 addr 1234:11::1 ffff:ffff::
     exit
    int tun21
     tun sou lo0
     tun dest 2.2.2.104
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 1.1.12.1 255.255.255.0
     exit
    int tun22
     tun sou lo0
     tun dest 4321::104
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv6 addr 1234:12::1 ffff:ffff::
     exit
    int tun31
     tun sou lo0
     tun dest 2.2.2.105
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 1.1.13.1 255.255.255.0
     exit
    int tun32
     tun sou lo0
     tun dest 4321::105
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv6 addr 1234:13::1 ffff:ffff::
     exit
    int tun41
     tun sou lo0
     tun dest 2.2.2.106
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv4 addr 1.1.14.1 255.255.255.0
     exit
    int tun42
     tun sou lo0
     tun dest 4321::106
     tun vrf v1
     tun mod p2pte
     vrf for v1
     ipv6 addr 1234:14::1 ffff:ffff::
     exit
    server p4lang p4
     interconnect eth2
     export-vrf v1 1
     export-port sdn1 1 10
     export-port sdn2 2 10
     export-port sdn3 3 10
     export-port sdn4 4 10
     export-port tun11 dynamic
     export-port tun12 dynamic
     export-port tun21 dynamic
     export-port tun22 dynamic
     export-port tun31 dynamic
     export-port tun32 dynamic
     export-port tun41 dynamic
     export-port tun42 dynamic
     vrf v9
     exit
    ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
    ipv4 route v1 2.2.2.104 255.255.255.255 1.1.2.2
    ipv4 route v1 2.2.2.105 255.255.255.255 1.1.3.2
    ipv4 route v1 2.2.2.106 255.255.255.255 1.1.4.2
    ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
    ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
    ipv4 route v1 2.2.2.203 255.255.255.255 1.1.11.2
    ipv4 route v1 2.2.2.204 255.255.255.255 1.1.12.2
    ipv4 route v1 2.2.2.205 255.255.255.255 1.1.13.2
    ipv4 route v1 2.2.2.206 255.255.255.255 1.1.14.2
    ipv6 route v1 4321::203 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:11::2
    ipv6 route v1 4321::204 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:12::2
    ipv6 route v1 4321::205 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:13::2
    ipv6 route v1 4321::206 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:14::2
    ```

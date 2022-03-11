# Example: p4lang: pckoudp over ipv6
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz77r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    vrf def v2
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
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.101 255.255.255.255
     ipv6 addr 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    bridge 1
     mac-learn
     exit
    int sdn1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234:1::1 ffff:ffff::
     ipv6 ena
     exit
    int sdn2
     bridge-gr 1
     exit
    int sdn3
     vrf for v2
     ipv6 addr 9999::1 ffff:ffff::
     ipv6 ena
     exit
    proxy-profile p2
     vrf v2
     exit
    vpdn vx
     bridge-group 1
     proxy p2
     target 9999::2
     vcid 2554
     protocol pckoudp
     exit
    int sdn4
     bridge-gr 1
     exit
    server p4lang p4
     interconnect eth2
     export-vrf v1 1
     export-vrf v2 2
     export-br 1
     export-port sdn1 1
     export-port sdn2 2
     export-port sdn3 3
     export-port sdn4 4
     vrf v9
     exit
    ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
    ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ```

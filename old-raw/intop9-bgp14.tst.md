# Example: interop9: vpls/ldp over bgp
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz40r1-log.run
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
    bridge 1
     rd 1:1
     rt-both 1:1
     mac-learn
     private
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234::1 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     exit
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int bvi1
     vrf for v1
     ipv4 addr 3.3.3.1 255.255.255.252
     ipv6 addr 3333::1 ffff::
     exit
    router bgp4 1
     vrf v1
     address vpls
     local-as 1
     router-id 4.4.4.1
     neigh 2.2.2.2 remote-as 1
     neigh 2.2.2.2 update lo0
     neigh 2.2.2.2 send-comm both
     afi-vpls 1:1 bridge 1
     afi-vpls 1:1 update lo0
     exit
    router bgp6 1
     vrf v1
     address vpls
     local-as 1
     router-id 6.6.6.1
     neigh 4321::2 remote-as 1
     neigh 4321::2 update lo0
     neigh 4321::2 send-comm both
     exit
    ```

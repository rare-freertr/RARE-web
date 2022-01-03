# Example: interop9: mpls over pppoe
    
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
     label-mode per-prefix
     exit
    int di1
     enc ppp
     ppp ip4cp open
     ppp ip6cp open
     ppp mplscp open
     ppp ip4cp local 1.1.1.1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234:1::1 ffff:ffff:ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     exit
    int eth1
     p2poe server di1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.1.2
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
    int pweth1
     vrf for v1
     ipv4 addr 3.3.3.1 255.255.255.252
     pseudo v1 lo0 pweompls 2.2.2.3 1234
     exit
    ```

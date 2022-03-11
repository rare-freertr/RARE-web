# Example: interop1: pppoe with eap
    
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
    int di1
     enc ppp
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.0
     ipv6 addr fe80::1234 ffff::
     ppp ip4cp local 2.2.2.1
     ppp ip4cp open
     ppp ip6cp open
     ppp user usr
     ppp pass pwd
     exit
    int eth1
     p2poe server di1
     exit
    ```

# Example: interop1: l2tp2 client
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz7r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    proxy-profile p1
     vrf v1
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     exit
    prefix-list p1
     permit 0.0.0.0/0
     exit
    int di1
     enc ppp
     ppp ip4cp open
     vrf for v1
     ipv4 addr 3.3.3.3 255.255.255.0
     ppp ip4cp local 0.0.0.0
     ipv4 gateway-prefix p1
     exit
    vpdn l2tp
     int di1
     proxy p1
     tar 1.1.1.2
     called 1234
     calling 4321
     dir in
     prot l2tp2
     exit
    ```

# Example: interop8: bgp addpath
    
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
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234::1 ffff::
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    router bgp4 1
     vrf v1
     address uni
     local-as 1
     router-id 4.4.4.1
     neigh 1.1.1.2 remote-as 1
     neigh 1.1.1.2 additional-path-tx uni
     neigh 1.1.1.2 additional-path-rx uni
     red conn
     exit
    router bgp6 1
     vrf v1
     address uni
     local-as 1
     router-id 6.6.6.1
     neigh 1234::2 remote-as 1
     neigh 1234::2 additional-path-tx uni
     neigh 1234::2 additional-path-rx uni
     red conn
     exit
    ```

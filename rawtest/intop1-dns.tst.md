# Example: interop1: dns
    
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
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234::1 ffff::
     exit
    server dns dns
     zone test.corp defttl 43200
     rr ip4.test.corp ip4a 2.2.2.2
     rr ip6.test.corp ip6a 1234::1
     vrf v1
     exit
    int lo1
     vrf for v1
     ipv4 addr 4.4.4.4 255.255.255.255
     exit
    server tel tel
     vrf v1
     security protocol tel
     exit
    ```

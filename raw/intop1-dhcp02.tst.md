# Example: interop1: dhcp client
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz32r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    prefix-list p4
     permit 0.0.0.0/0
     exit
    prefix-list p6
     permit ::/0
     exit
    int eth1
     vrf for v1
     ipv4 addr 3.3.3.3 255.255.255.128
     ipv4 dhcp-client enable
     ipv4 dhcp-client early
     ipv4 gateway-prefix p4
     ipv6 addr 3333::3 ffff::
     ipv6 dhcp-client enable
     ipv6 dhcp-client prefix
     ipv6 gateway-prefix p6
     exit
    ```

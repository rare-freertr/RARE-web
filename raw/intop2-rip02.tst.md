# Example: interop2: rip prefix withdraw
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz52r1-log.run
    vrf definition tester
     exit
    server telnet tester
     security protocol telnet
     vrf tester
     exit
    vrf def v1
     rd 1:1
     exit
    router rip4 1
     vrf v1
     red conn
     exit
    router rip6 1
     vrf v1
     red conn
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr fe80::1 ffff::
     router rip4 1 ena
     router rip4 1 update-time 5000
     router rip4 1 hold-time 15000
     router rip4 1 flush-time 15000
     router rip6 1 ena
     router rip6 1 update-time 5000
     router rip6 1 hold-time 15000
     router rip6 1 flush-time 15000
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    ```

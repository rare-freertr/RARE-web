# Example: interop1: isis php sr
    
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
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    access-list test6
     sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
     sequence 20 permit all any all any all
     exit
    router isis4 1
     vrf v1
     net 48.4444.0000.1111.00
     traffeng 2.2.2.1
     segrout 10
     both segrout
     red conn
     exit
    router isis6 1
     vrf v1
     net 48.6666.0000.1111.00
     traffeng 6.6.6.1
     segrout 10
     both segrout
     red conn
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     router isis4 1 ena
     mpls enable
     ipv4 access-group-in test4
    ! ipv4 access-group-out test4
     exit
    int eth2
     vrf for v1
     ipv6 addr fe80::1 ffff::
     router isis6 1 ena
     mpls enable
     ipv6 access-group-in test6
     ipv6 access-group-out test6
     exit
    int lo1
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     router isis4 1 ena
     router isis4 1 segrout index 1
     router isis4 1 segrout node
     router isis4 1 segrout pop
     exit
    int lo2
     vrf for v1
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     router isis6 1 ena
     router isis6 1 segrout index 2
     router isis6 1 segrout node
     router isis6 1 segrout pop
     exit
    int pweth1
     vrf for v1
     ipv4 addr 3.3.3.1 255.255.255.252
     pseudo v1 lo1 pweompls 2.2.2.3 1234
     exit
    ```

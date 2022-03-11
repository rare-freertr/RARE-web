# Example: addressed demo network
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    logging file debug ../binTmp/zzz9r1-log.run
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
    server telnet tel
     security protocol tel
     vrf v1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.1 255.255.255.255
     ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int eth1
     desc r2 e1
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.252
     ipv6 addr 1234:1::1 ffff:ffff::
     exit
    int eth2
     desc r3 e2
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.5 255.255.255.252
     ipv6 addr 1234:2::1 ffff:ffff::
     exit
    ```
    
    **r2:**
    ```
    hostname r2
    logging file debug ../binTmp/zzz9r2-log.run
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
    server telnet tel
     security protocol tel
     vrf v1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.2 255.255.255.255
     ipv6 addr 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int eth1
     desc r1 e1
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.2 255.255.255.252
     ipv6 addr 1234:1::2 ffff:ffff::
     exit
    int eth2
     desc r4 e2
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.9 255.255.255.252
     ipv6 addr 1234:3::1 ffff:ffff::
     exit
    ```
    
    **r3:**
    ```
    hostname r3
    logging file debug ../binTmp/zzz9r3-log.run
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
    server telnet tel
     security protocol tel
     vrf v1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.3 255.255.255.255
     ipv6 addr 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int eth1
     desc r4 e1
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.13 255.255.255.252
     ipv6 addr 1234:4::1 ffff:ffff::
     exit
    int eth2
     desc r1 e2
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.6 255.255.255.252
     ipv6 addr 1234:2::2 ffff:ffff::
     exit
    ```
    
    **r4:**
    ```
    hostname r4
    logging file debug ../binTmp/zzz9r4-log.run
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
    server telnet tel
     security protocol tel
     vrf v1
     exit
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.4 255.255.255.255
     ipv6 addr 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     exit
    int eth1
     desc r3 e1
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.14 255.255.255.252
     ipv6 addr 1234:4::2 ffff:ffff::
     exit
    int eth2
     desc r2 e2
     lldp ena
     vrf for v1
     ipv4 addr 1.1.1.10 255.255.255.252
     ipv6 addr 1234:3::2 ffff:ffff::
     exit
    ```

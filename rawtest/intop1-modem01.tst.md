# Example: interop1: modem with alaw
    
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
    int lo0
     vrf for v1
     ipv4 addr 2.2.2.2 255.255.255.255
     exit
    int eth1
     vrf for v1
     ipv4 addr 1.1.1.1 255.255.255.0
     ipv6 addr 1234::1 ffff::
     exit
    server modem sm
     codec alaw
     vrf v1
     exit
    ```
    
    **r2:**
    ```
    hostname r2
    logging file debug ../binTmp/zzz1r2-log.run
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
     ipv4 addr 1.1.1.2 255.255.255.0
     ipv6 addr 1234::2 ffff::
     exit
    int eth2
     vrf for v1
     ipv4 addr 1.1.2.2 255.255.255.0
     ipv6 addr 4321::2 ffff::
     exit
    dial-peer 1
     codec alaw
     match-calling .*
     match-called .*
     vrf v1
     myname 99
     port-local 5060
     target 1.1.1.1
     direction both
     exit
    dial-peer 2
     codec alaw
     match-calling .*
     match-called .*
     vrf v1
     myname 99
     port-local 5060
     target 1.1.2.1
     direction both
     exit
    ```

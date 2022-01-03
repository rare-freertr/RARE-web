# Example: ethernet over mpls
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    buggy
    !
    logging file debug ../binTmp/zzz1r1-log.run
    !
    bridge 1
     mac-learn
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source loopback0
     exit
    !
    vpdn eompls
     bridge-group 1
     proxy p1
     target 2.2.2.2
     mtu 1500
     vcid 1234
     pwtype ethernet
     protocol pweompls
     exit
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 2.2.2.2 255.255.255.255 1.1.1.2
    !
    ipv6 route v1 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::2
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    !
    end
    ```
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz1r2-log.run
    !
    bridge 1
     mac-learn
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     label-mode per-prefix
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source loopback0
     exit
    !
    vpdn eompls
     bridge-group 1
     proxy p1
     target 2.2.2.1
     mtu 1500
     vcid 1234
     pwtype ethernet
     protocol pweompls
     exit
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    ipv4 route v1 2.2.2.1 255.255.255.255 1.1.1.1
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234::1
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    !
    end
    ```
    
=== "Verification"
    
    ```
    r1#
    r1#
    r1#show mpls forw
    r1#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|
     | label  | vrf      | iface     | hop     | label      | targets | bytes |
     |--------|----------|-----------|---------|------------|---------|-------|
     | 95882  | v1:6     | ethernet1 | 1234::2 | 758970     |         | 0     |
     | 199865 | tester:6 | null      | null    | unlabelled | local   | 0     |
     | 260595 | v1:4     | null      | null    | unlabelled | pwe     | 978   |
     | 745686 | tester:4 | null      | null    | unlabelled | local   | 0     |
     | 795900 | v1:4     | ethernet1 | 1.1.1.2 | 98601      |         | 0     |
     | 851191 | v1:6     | null      | null    | unlabelled | local   | 0     |
     | 937725 | v1:4     | null      | null    | unlabelled | local   | 1636  |
     |________|__________|___________|_________|____________|_________|_______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 ldp v1 sum
    r1#show ipv4 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                     |
     | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
     |-------|--------|-------|--------|-------|--------|----------|----------|
     | 6     | 6      | 0     | 0      | 0     | 0      | 1.1.1.2  | 00:00:15 |
     | 6     | 6      | 1     | 1      | 0     | 0      | 2.2.2.2  | 00:00:18 |
     |_______|________|_______|________|_______|________|__________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 ldp v1 sum
    r1#show ipv6 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                     |
     | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
     |-------|--------|-------|--------|-------|--------|----------|----------|
     | 4     | 4      | 0     | 0      | 0     | 0      | 1234::2  | 00:00:15 |
     |_______|________|_______|________|_______|________|__________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show bridge 1
    r1#show bridge 1
     |~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~|
     |                                 | packet         | byte              |     |
     | iface            | fwd  | phys  | tx | rx | drop | tx   | rx  | drop | grp |
     |------------------|------|-------|----|----|------|------|-----|------|-----|
     | bvi              | true | true  | 0  | 0  | 0    | 0    | 0   | 0    |     |
     | pwe 2.2.2.2 1234 | true | false | 25 | 13 | 0    | 1182 | 978 | 0    |     |
     |__________________|______|_______|____|____|______|______|_____|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~~|~~~~~~|
     |                                              | packet         | byte              |
     | addr           | iface            | time     | tx | rx | drop | tx  | rx   | drop |
     |----------------|------------------|----------|----|----|------|-----|------|------|
     | 0057.3036.2e48 | pwe 2.2.2.2 1234 | 00:00:21 | 12 | 13 | 0    | 792 | 822  | 0    |
     | 005b.036f.1f76 | bvi              | 00:00:21 | 13 | 25 | 0    | 822 | 1182 | 0    |
     |________________|__________________|__________|____|____|______|_____|______|______|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show inter bvi1 full
    r1#show inter bvi1 full
    bvi1 is up (since 00:00:21, 3 changes)
     description:
     type is bridged, hwaddr=005b.036f.1f76, mtu=1500, bw=8000kbps, vrf=v1
     ip4 address=3.3.3.1/24, netmask=255.255.255.0, ifcid=209229136
     received 13 packets (822 bytes) dropped 0 packets (0 bytes)
     transmitted 25 packets (1182 bytes) promisc=false macsec=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |       | packet         | byte             |
     | time  | tx | rx | drop | tx  | rx  | drop |
     |-------|----|----|------|-----|-----|------|
     | 1sec  | 10 | 10 | 0    | 660 | 660 | 0    |
     | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
     |_______|____|____|______|_____|_____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |                          | packet         | byte             |
     | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
     |--------|-------|---------|----|----|------|-----|-----|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
     | ethtyp | 0800  | ip4     | 12 | 12 | 0    | 792 | 792 | 0    |
     | ethtyp | 0806  | arp4    | 13 | 1  | 0    | 390 | 30  | 0    |
     |________|_______|_________|____|____|______|_____|_____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 0     | 13   | 390  |
     | 1     | 12   | 792  |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~~|
     |            | packet         | byte              |
     | size       | tx | rx | drop | tx   | rx  | drop |
     |------------|----|----|------|------|-----|------|
     | 0-255      | 25 | 13 | 0    | 1182 | 822 | 0    |
     | 256-511    | 0  | 0  | 0    | 0    | 0   | 0    |
     | 512-767    | 0  | 0  | 0    | 0    | 0   | 0    |
     | 768-1023   | 0  | 0  | 0    | 0    | 0   | 0    |
     | 1024-1279  | 0  | 0  | 0    | 0    | 0   | 0    |
     | 1280-1535  | 0  | 0  | 0    | 0    | 0   | 0    |
     | 1536-1791  | 0  | 0  | 0    | 0    | 0   | 0    |
     | 1792-65535 | 0  | 0  | 0    | 0    | 0   | 0    |
     |____________|____|____|______|______|_____|______|
     |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |       | packet           | byte               |
     | class | cos | exp | prec | cos  | exp  | prec |
     |-------|-----|-----|------|------|------|------|
     | 0     | 25  | 25  | 25   | 1182 | 1182 | 1182 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
             10k|
            9504|#
            8448|#
            7392|#
            6336|#
            5280|#
            4224|#
            3168|#
            2112|#
            1056|##
               0|##### ##### #####
             bps|0---------10--------20--------30--------40--------50-------- seconds
               1|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
             bps|0---------10--------20--------30--------40--------50-------- minutes
               1|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
               0|
             bps|0---------10--------20--------30--------40--------50-------- hours
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv4 arp bvi1
    r1#show ipv4 arp bvi1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
     | mac            | address | time     | static |
     |----------------|---------|----------|--------|
     | 0057.3036.2e48 | 3.3.3.2 | 00:00:20 | false  |
     |________________|_________|__________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 neigh bvi1
    r1#show ipv6 neigh bvi1
    % protocol not enabled
    r1#
    r1#
    ```

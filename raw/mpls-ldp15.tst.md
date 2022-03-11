# Example: mp2mp ldp tunnel
    
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
    logging file debug ../binTmp/zzz92r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234:1::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv6 address 3333::1 ffff:ffff::
     no shutdown
     no log-link-change
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.2
    !
    ipv6 route v1 :: :: 1234:1::2
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
    logging file debug ../binTmp/zzz92r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
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
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234:1::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1234:2::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     vrf forwarding v1
     ipv4 address 1.1.3.1 255.255.255.0
     ipv6 address 1234:3::1 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
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
    ipv4 route v1 2.2.2.3 255.255.255.255 1.1.2.2
    ipv4 route v1 2.2.2.4 255.255.255.255 1.1.3.2
    !
    ipv6 route v1 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
    ipv6 route v1 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
    ipv6 route v1 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz92r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1234:2::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv6 address 3333::3 ffff:ffff::
     no shutdown
     no log-link-change
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.2.1
    !
    ipv6 route v1 :: :: 1234:2::1
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz92r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.3.2 255.255.255.0
     ipv6 address 1234:3::2 ffff:ffff::
     mpls enable
     mpls ldp4
     mpls ldp6
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 2.2.2.2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv4 address 3.3.3.4 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel2
     no description
     tunnel key 1234
     tunnel vrf v1
     tunnel source loopback0
     tunnel destination 4321::2
     tunnel mode mp2mpldp
     vrf forwarding v1
     ipv6 address 3333::4 ffff:ffff::
     no shutdown
     no log-link-change
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.3.1
    !
    ipv6 route v1 :: :: 1234:3::1
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
    r3#
    r3#
    r3#show mpls forw
    r3#show mpls forw
     |~~~~~~~~|~~~~~~~~~~|~~~~~~~|~~~~~~|~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~|~~~~~~~~|
     | label  | vrf      | iface | hop  | label      | targets         | bytes  |
     |--------|----------|-------|------|------------|-----------------|--------|
     | 208790 | v1:6     | null  | null | unlabelled | local           | 0      |
     | 673627 | tester:4 | null  | null | unlabelled | local           | 0      |
     | 736235 | tester:6 | null  | null | unlabelled | local           | 0      |
     | 899924 | v1:4     | null  | null | unlabelled | local           | 0      |
     | 939286 | v1:6     | null  | null | unlabelled | local duplicate | 238272 |
     | 943919 | v1:4     | null  | null | unlabelled | local duplicate | 373504 |
     |________|__________|_______|______|____________|_________________|________|
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show ipv4 ldp v1 sum
    r3#show ipv4 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                     |
     | learn | advert | learn | advert | learn | advert | neighbor | uptime   |
     |-------|--------|-------|--------|-------|--------|----------|----------|
     | 0     | 0      | 0     | 0      | 1     | 1      | 1.1.2.1  | 00:00:06 |
     |_______|________|_______|________|_______|________|__________|__________|
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show ipv6 ldp v1 sum
    r3#show ipv6 ldp v1 sum
     |~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | prefix         | layer2         | p2mp           |                      |
     | learn | advert | learn | advert | learn | advert | neighbor  | uptime   |
     |-------|--------|-------|--------|-------|--------|-----------|----------|
     | 0     | 0      | 0     | 0      | 1     | 1      | 1234:2::1 | 00:00:11 |
     |_______|________|_______|________|_______|________|___________|__________|
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show ipv4 ldp v1 mpdat
    r3#show ipv4 ldp v1 mpdat
     |~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
     | type  | local      | root    | opaque               | uplink  | peers                       |
     |-------|------------|---------|----------------------|---------|-----------------------------|
     | mp2mp | false true | 2.2.2.2 | 01 00 04 00 00 04 d2 | 1.1.2.1 | local 943919/1.1.2.1/543553 |
     |_______|____________|_________|______________________|_________|_____________________________|
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show ipv6 ldp v1 mpdat
    r3#show ipv6 ldp v1 mpdat
     |~~~~~~~|~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
     | type  | local      | root    | opaque               | uplink    | peers                         |
     |-------|------------|---------|----------------------|-----------|-------------------------------|
     | mp2mp | false true | 4321::2 | 01 00 04 00 00 04 d2 | 1234:2::1 | local 939286/1234:2::1/969189 |
     |_______|____________|_________|______________________|___________|_______________________________|
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show inter tun1 full
    r3#show inter tun1 full
    tunnel1 is up (since 00:00:17, 15 changes)
     description:
     type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
     ip4 address=3.3.3.3/24, netmask=255.255.255.0, ifcid=394622628
     received 0 packets (0 bytes) dropped 0 packets (0 bytes)
     transmitted 2690 packets (177540 bytes) promisc=false macsec=false sgt=false
     |~~~~~~~|~~~~~|~~~~|~~~~~~|~~~~~~~|~~~~|~~~~~~|
     |       | packet          | byte              |
     | time  | tx  | rx | drop | tx    | rx | drop |
     |-------|-----|----|------|-------|----|------|
     | 1sec  | 677 | 0  | 0    | 44682 | 0  | 0    |
     | 1min  | 0   | 0  | 0    | 0     | 0  | 0    |
     | 1hour | 0   | 0  | 0    | 0     | 0  | 0    |
     |_______|_____|____|______|_______|____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
     |                          | packet           | byte               |
     | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
     |--------|-------|---------|------|----|------|--------|----|------|
     | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
     | ethtyp | 0800  | ip4     | 2690 | 0  | 0    | 177540 | 0  | 0    |
     |________|_______|_________|______|____|______|________|____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~~~|
     | proto | pack | byte   |
     |-------|------|--------|
     | 1     | 2690 | 177540 |
     |_______|______|________|
     |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
     |            | packet           | byte               |
     | size       | tx   | rx | drop | tx     | rx | drop |
     |------------|------|----|------|--------|----|------|
     | 0-255      | 2690 | 0  | 0    | 177540 | 0  | 0    |
     | 256-511    | 0    | 0  | 0    | 0      | 0  | 0    |
     | 512-767    | 0    | 0  | 0    | 0      | 0  | 0    |
     | 768-1023   | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1024-1279  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1280-1535  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1536-1791  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1792-65535 | 0    | 0  | 0    | 0      | 0  | 0    |
     |____________|______|____|______|________|____|______|
     |~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|
     |       | packet             | byte                     |
     | class | cos  | exp  | prec | cos    | exp    | prec   |
     |-------|------|------|------|--------|--------|--------|
     | 0     | 2690 | 2690 | 2690 | 177540 | 177540 | 177540 |
     | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
     |_______|______|______|______|________|________|________|
            485k|
            436k| #
            388k| ##
            339k|###
            291k|###
            242k|###
            194k|###
            145k|###
             97k|####
             48k|####
               0|####
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
    r3#
    r3#
    ```
    
    ```
    r3#
    r3#
    r3#show inter tun2 full
    r3#show inter tun2 full
    tunnel2 is up (since 00:00:17, 15 changes)
     description:
     type is mp2mpldp, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
     ip6 address=3333::3/32, netmask=ffff:ffff::, ifcid=826467895
     received 0 packets (0 bytes) dropped 0 packets (0 bytes)
     transmitted 1750 packets (115532 bytes) promisc=false macsec=false sgt=false
     |~~~~~~~|~~~~~|~~~~|~~~~~~|~~~~~~~|~~~~|~~~~~~|
     |       | packet          | byte              |
     | time  | tx  | rx | drop | tx    | rx | drop |
     |-------|-----|----|------|-------|----|------|
     | 1sec  | 685 | 0  | 0    | 45210 | 0  | 0    |
     | 1min  | 0   | 0  | 0    | 0     | 0  | 0    |
     | 1hour | 0   | 0  | 0    | 0     | 0  | 0    |
     |_______|_____|____|______|_______|____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
     |                          | packet           | byte               |
     | type   | value | handler | tx   | rx | drop | tx     | rx | drop |
     |--------|-------|---------|------|----|------|--------|----|------|
     | ethtyp | 0000  | null    | 0    | 0  | 0    | 0      | 0  | 0    |
     | ethtyp | 86dd  | ip6     | 1750 | 0  | 0    | 115532 | 0  | 0    |
     |________|_______|_________|______|____|______|________|____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~~~|
     | proto | pack | byte   |
     |-------|------|--------|
     | 58    | 1750 | 115532 |
     |_______|______|________|
     |~~~~~~~~~~~~|~~~~~~|~~~~|~~~~~~|~~~~~~~~|~~~~|~~~~~~|
     |            | packet           | byte               |
     | size       | tx   | rx | drop | tx     | rx | drop |
     |------------|------|----|------|--------|----|------|
     | 0-255      | 1750 | 0  | 0    | 115532 | 0  | 0    |
     | 256-511    | 0    | 0  | 0    | 0      | 0  | 0    |
     | 512-767    | 0    | 0  | 0    | 0      | 0  | 0    |
     | 768-1023   | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1024-1279  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1280-1535  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1536-1791  | 0    | 0  | 0    | 0      | 0  | 0    |
     | 1792-65535 | 0    | 0  | 0    | 0      | 0  | 0    |
     |____________|______|____|______|________|____|______|
     |~~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~~~|~~~~~~~~|~~~~~~~~|
     |       | packet             | byte                     |
     | class | cos  | exp  | prec | cos    | exp    | prec   |
     |-------|------|------|------|--------|--------|--------|
     | 0     | 1750 | 1750 | 1750 | 115532 | 115532 | 115532 |
     | 1     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 2     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 3     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 4     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 5     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 6     | 0    | 0    | 0    | 0      | 0      | 0      |
     | 7     | 0    | 0    | 0    | 0      | 0      | 0      |
     |_______|______|______|______|________|________|________|
            430k|
            387k| #
            344k|##
            301k|##
            258k|##
            215k|##
            172k|##
            129k|##
             86k|##
             43k|###
               0|###             #
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
    r3#
    r3#
    ```

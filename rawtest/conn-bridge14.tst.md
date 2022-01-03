# Example: bridged mac rewrite
    
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
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
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
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     bridge-macrewrite 0000.1234.1234
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
     bridge-macrewrite 0000.1234.1234
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
    logging file debug ../binTmp/zzz1r3-log.run
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
     exit
    !
    interface bvi1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234::3 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     bridge-group 1
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
    logging file debug ../binTmp/zzz1r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.4 255.255.255.0
     ipv6 address 1234::4 ffff::
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
    r2#
    r2#
    r2#show bridge 1
    r2#show bridge 1
     |~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                         | packet           | byte               |     |
     | iface     | fwd  | phys | tx  | rx  | drop | tx   | rx   | drop | grp |
     |-----------|------|------|-----|-----|------|------|------|------|-----|
     | bvi       | true | true | 0   | 0   | 0    | 0    | 0    | 0    |     |
     | ethernet1 | true | true | 90  | 83  | 0    | 5908 | 5452 | 0    |     |
     | ethernet2 | true | true | 117 | 114 | 0    | 7688 | 7484 | 0    |     |
     |___________|______|______|_____|_____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                                       | packet         | byte               |
     | addr           | iface     | time     | tx | rx | drop | tx   | rx   | drop |
     |----------------|-----------|----------|----|----|------|------|------|------|
     | 0000.0000.4444 | ethernet2 | 00:00:23 | 56 | 60 | 0    | 3696 | 3916 | 0    |
     | 0052.7204.0d40 | bvi       | 00:00:23 | 79 | 83 | 0    | 5162 | 5434 | 0    |
     | 006d.3530.484a | ethernet1 | 00:00:23 | 80 | 83 | 0    | 5192 | 5452 | 0    |
     | 007a.4a0a.4f38 | ethernet2 | 00:00:23 | 48 | 54 | 0    | 3168 | 3568 | 0    |
     |________________|___________|__________|____|____|______|______|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show inter bvi1 full
    r2#show inter bvi1 full
    bvi1 is up (since 00:00:24, 3 changes)
     description:
     type is bridged, hwaddr=0052.7204.0d40, mtu=1500, bw=100mbps, vrf=v1
     ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=269995449
     ip6 address=1234::2/16, netmask=ffff::, ifcid=582774257
     received 90 packets (5926 bytes) dropped 0 packets (0 bytes)
     transmitted 83 packets (5434 bytes) promisc=false macsec=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |       | packet         | byte             |
     | time  | tx | rx | drop | tx  | rx  | drop |
     |-------|----|----|------|-----|-----|------|
     | 1sec  | 10 | 10 | 0    | 660 | 660 | 0    |
     | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
     |_______|____|____|______|_____|_____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                          | packet         | byte               |
     | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
     |--------|-------|---------|----|----|------|------|------|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
     | ethtyp | 0800  | ip4     | 42 | 42 | 0    | 2772 | 2772 | 0    |
     | ethtyp | 0806  | arp4    | 3  | 5  | 0    | 90   | 180  | 0    |
     | ethtyp | 86dd  | ip6     | 38 | 43 | 0    | 2572 | 2974 | 0    |
     |________|_______|_________|____|____|______|______|______|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 0     | 3    | 90   |
     | 1     | 42   | 2772 |
     | 58    | 38   | 2572 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 83 | 90 | 0    | 5434 | 5926 | 0    |
     | 256-511    | 0  | 0  | 0    | 0    | 0    | 0    |
     | 512-767    | 0  | 0  | 0    | 0    | 0    | 0    |
     | 768-1023   | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1024-1279  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1280-1535  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1536-1791  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1792-65535 | 0  | 0  | 0    | 0    | 0    | 0    |
     |____________|____|____|______|______|______|______|
     |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |       | packet           | byte               |
     | class | cos | exp | prec | cos  | exp  | prec |
     |-------|-----|-----|------|------|------|------|
     | 0     | 83  | 83  | 83   | 5434 | 5434 | 5434 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
             17k|
             15k|     #
             13k|     #
             11k|     #
             10k|#  # #
            8512|#  # #
            6809|#  # #
            5107|# ## # #  # #   #     #
            3404|# ###### ## #   # #   #
            1702|# ###### ## #   # #   #
               0|# ###### ## # # # ##  #
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
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 arp bvi1
    r2#show ipv4 arp bvi1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
     | mac            | address | time     | static |
     |----------------|---------|----------|--------|
     | 006d.3530.484a | 1.1.1.1 | 00:00:23 | false  |
     | 007a.4a0a.4f38 | 1.1.1.3 | 00:00:23 | false  |
     | 0000.0000.4444 | 1.1.1.4 | 00:00:23 | false  |
     |________________|_________|__________|________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 neigh bvi1
    r2#show ipv6 neigh bvi1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
     | mac            | address                  | time     | static | router |
     |----------------|--------------------------|----------|--------|--------|
     | 006d.3530.484a | 1234::1                  | 00:00:23 | false  | false  |
     | 007a.4a0a.4f38 | 1234::3                  | 00:00:23 | false  | false  |
     | 0000.0000.4444 | 1234::4                  | 00:00:23 | false  | false  |
     | 006d.3530.484a | fe80::26d:35ff:fe30:484a | 00:00:23 | false  | false  |
     | 007a.4a0a.4f38 | fe80::27a:4aff:fe0a:4f38 | 00:00:23 | false  | false  |
     |________________|__________________________|__________|________|________|
    r2#
    r2#
    ```

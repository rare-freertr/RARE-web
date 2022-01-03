# Example: chain bridged ethernet
    
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
     | ethernet1 | true | true | 98  | 93  | 0    | 6382 | 6088 | 0    |     |
     | ethernet2 | true | true | 127 | 121 | 0    | 8332 | 7884 | 0    |     |
     |___________|______|______|_____|_____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                                       | packet         | byte               |
     | addr           | iface     | time     | tx | rx | drop | tx   | rx   | drop |
     |----------------|-----------|----------|----|----|------|------|------|------|
     | 0000.0000.4444 | ethernet2 | 00:00:31 | 57 | 60 | 0    | 3770 | 3924 | 0    |
     | 0024.6d0f.1520 | ethernet1 | 00:00:31 | 87 | 93 | 0    | 5662 | 6088 | 0    |
     | 003d.134b.2c11 | bvi       | 00:00:31 | 90 | 93 | 0    | 5904 | 6110 | 0    |
     | 0067.6f38.062d | ethernet2 | 00:00:31 | 57 | 61 | 0    | 3770 | 3960 | 0    |
     |________________|___________|__________|____|____|______|______|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show inter bvi1 full
    r2#show inter bvi1 full
    bvi1 is up (since 00:00:31, 3 changes)
     description:
     type is bridged, hwaddr=003d.134b.2c11, mtu=1500, bw=100mbps, vrf=v1
     ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=681632588
     ip6 address=1234::2/16, netmask=ffff::, ifcid=183653917
     received 98 packets (6344 bytes) dropped 0 packets (0 bytes)
     transmitted 93 packets (6110 bytes) promisc=false macsec=false
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
     | ethtyp | 0806  | arp4    | 3  | 6  | 0    | 90   | 216  | 0    |
     | ethtyp | 86dd  | ip6     | 48 | 50 | 0    | 3248 | 3356 | 0    |
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
     | 58    | 48   | 3248 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 93 | 98 | 0    | 6110 | 6344 | 0    |
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
     | 0     | 93  | 93  | 93   | 6110 | 6110 | 6110 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
             11k|
             10k|       #
            9395|#      #
            8220|# #    #
            7046|# #    #
            5872|# #  # #
            4697|# #  # # # #      #     #
            3523|# # ########      ##    ##
            2348|# # ########      ##    ##
            1174|# ##########     ####   ##   #
               0|# ########## ##  #### # ###  #
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
     | 0024.6d0f.1520 | 1.1.1.1 | 00:00:30 | false  |
     | 0067.6f38.062d | 1.1.1.3 | 00:00:30 | false  |
     | 0000.0000.4444 | 1.1.1.4 | 00:00:30 | false  |
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
     | 0024.6d0f.1520 | 1234::1                  | 00:00:30 | false  | false  |
     | 0067.6f38.062d | 1234::3                  | 00:00:30 | false  | false  |
     | 0000.0000.4444 | 1234::4                  | 00:00:30 | false  | false  |
     | 0000.0000.4444 | fe80::200:ff:fe00:4444   | 00:00:30 | false  | false  |
     | 0024.6d0f.1520 | fe80::224:6dff:fe0f:1520 | 00:00:30 | false  | false  |
     | 0067.6f38.062d | fe80::267:6fff:fe38:62d  | 00:00:30 | false  | false  |
     |________________|__________________________|__________|________|________|
    r2#
    r2#
    ```

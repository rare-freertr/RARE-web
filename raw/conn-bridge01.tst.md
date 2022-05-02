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
    logging file debug ../binTmp/zzz39r1-log.run
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    logging file debug ../binTmp/zzz39r2-log.run
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
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
    logging file debug ../binTmp/zzz39r3-log.run
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
     vrf forwarding v1
     ipv4 address 1.1.1.3 255.255.255.0
     ipv6 address 1234::3 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     bridge-group 1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
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
    logging file debug ../binTmp/zzz39r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
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
     | brprt bvi |      |      |     |     |      |      |      |      |     |
     | ethernet1 | true | true | 87  | 78  | 0    | 5712 | 5114 | 0    |     |
     | ethernet2 | true | true | 107 | 107 | 0    | 7012 | 7024 | 0    |     |
     |___________|______|______|_____|_____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                                     | packet             | byte               |  |
     | addr           | iface     | static | time     | tx | rx | drop | tx   | rx   | drop |
     |----------------|-----------|--------|----------|----|----|------|------|------|------|
     | 0000.0000.4444 | ethernet2 | false  | 00:00:15 | 48 | 53 | 0    | 3168 | 3494 | 0    |
     | 0032.2d1d.1468 | ethernet2 | false  | 00:00:15 | 48 | 54 | 0    | 3168 | 3530 | 0    |
     | 0041.6c33.6571 | ethernet1 | false  | 00:00:15 | 75 | 78 | 0    | 4854 | 5114 | 0    |
     | 0055.0741.1a19 | bvi       | false  | 00:00:15 | 74 | 78 | 0    | 4824 | 5096 | 0    |
     |________________|___________|________|__________|____|____|______|______|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show inter bvi1 full
    r2#show inter bvi1 full
    bvi1 is up
     description:
     state changed 3 times, last at 2022-05-02 21:08:49, 00:00:15 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is bridged, hwaddr=0055.0741.1a19, mtu=1500, bw=100mbps, vrf=v1
     ipv4 address=1.1.1.2/24, mask=255.255.255.0, ifcid=478129220
     ipv6 address=1234::2/16, mask=ffff::, ifcid=329230637
     received 87 packets (5730 bytes) dropped 0 packets (0 bytes)
     transmitted 78 packets (5096 bytes) macsec=false sgt=false
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
     | ethtyp | 86dd  | ip6     | 33 | 39 | 0    | 2234 | 2742 | 0    |
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
     | 58    | 33   | 2234 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 78 | 87 | 0    | 5096 | 5730 | 0    |
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
     | 0     | 78  | 78  | 78   | 5096 | 5096 | 5096 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
           21.1k|   #
           19.0k|   #
           16.8k|   #
           14.7k|   #
           12.6k|   #
           10.5k|#  #
            8448|#  #          #
            6336|#  #          #
            4224|# #######   ###
            2112|# #######   ###
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- seconds
              10|
               9|
               8|
               7|
               6|
               5|
               4|
               3|
               2|
               1|
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- minutes
              10|
               9|
               8|
               7|
               6|
               5|
               4|
               3|
               2|
               1|
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- hours
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv
    r2#show ipv
    r2#show ipv4 arp bvi1
    r2#show ipv4 arp bvi1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
     | mac            | address | time     | static |
     |----------------|---------|----------|--------|
     | 0041.6c33.6571 | 1.1.1.1 | 00:00:15 | false  |
     | 0032.2d1d.1468 | 1.1.1.3 | 00:00:15 | false  |
     | 0000.0000.4444 | 1.1.1.4 | 00:00:15 | false  |
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
     | 0041.6c33.6571 | 1234::1                  | 00:00:15 | false  | false  |
     | 0032.2d1d.1468 | 1234::3                  | 00:00:15 | false  | false  |
     | 0000.0000.4444 | 1234::4                  | 00:00:15 | false  | false  |
     | 0000.0000.4444 | fe80::200:ff:fe00:4444   | 00:00:15 | false  | true   |
     | 0032.2d1d.1468 | fe80::232:2dff:fe1d:1468 | 00:00:15 | false  | true   |
     | 0041.6c33.6571 | fe80::241:6cff:fe33:6571 | 00:00:15 | false  | true   |
     |________________|__________________________|__________|________|________|
    r2#
    r2#
    ```

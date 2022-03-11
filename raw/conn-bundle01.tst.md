# Example: bundle of ethernet port
    
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
    logging file debug ../binTmp/zzz67r1-log.run
    !
    bundle 1
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface bundle1
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
     bundle-group 1
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
    logging file debug ../binTmp/zzz67r2-log.run
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
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
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
    r1#
    r1#
    r1#show bundle 1
    r1#show bundle 1
     |~~~~~~~~~~~|~~~~~~~|
     | parameter | state |
     |-----------|-------|
     | backup    | 0     |
     | selected  | null  |
     | replicate | false |
     | sequence  | null  |
     | dejitter  | 0     |
     | reporter  | 0     |
     | dynamic   | 0     |
     |___________|_______|
     |~~~~~~~~~~~|~~~~~~~|~~~~~~~|~~~~~~~~|~~~~~~~~~~|
     | interface | state | quota | report | priority |
     |-----------|-------|-------|--------|----------|
     | ethernet1 | up    | 2000  | 0      | 0        |
     |___________|_______|_______|________|__________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show inter bun1 full
    r1#show inter bun1 full
    bundle1 is up (since 00:00:03, 3 changes)
     description:
     type is bundle, hwaddr=005d.556f.156f, mtu=1500, bw=100mbps, vrf=v1
     ip4 address=1.1.1.1/24, netmask=255.255.255.0, ifcid=446363586
     ip6 address=1234::1/16, netmask=ffff::, ifcid=187265078
     received 28 packets (1874 bytes) dropped 0 packets (0 bytes)
     transmitted 28 packets (1868 bytes) promisc=false macsec=false sgt=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |       | packet         | byte               |
     | time  | tx | rx | drop | tx   | rx   | drop |
     |-------|----|----|------|------|------|------|
     | 1sec  | 20 | 20 | 0    | 1320 | 1320 | 0    |
     | 1min  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1hour | 0  | 0  | 0    | 0    | 0    | 0    |
     |_______|____|____|______|______|______|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |                          | packet         | byte             |
     | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
     |--------|-------|---------|----|----|------|-----|-----|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
     | ethtyp | 0800  | ip4     | 14 | 14 | 0    | 924 | 924 | 0    |
     | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30  | 36  | 0    |
     | ethtyp | 86dd  | ip6     | 13 | 13 | 0    | 914 | 914 | 0    |
     |________|_______|_________|____|____|______|_____|_____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 0     | 1    | 30   |
     | 1     | 14   | 924  |
     | 58    | 13   | 914  |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 28 | 28 | 0    | 1868 | 1874 | 0    |
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
     | 0     | 28  | 28  | 28   | 1868 | 1868 | 1868 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
             21k|
             19k|#
             16k|#
             14k|#
             12k|#
             10k|#
            8448|#
            6336|#
            4224|# #
            2112|###
               0|###
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
    r1#show ipv4 arp bun1
    r1#show ipv4 arp bun1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|
     | mac            | address | time     | static |
     |----------------|---------|----------|--------|
     | 0000.0000.2222 | 1.1.1.2 | 00:00:03 | false  |
     |________________|_________|__________|________|
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show ipv6 neigh bun1
    r1#show ipv6 neigh bun1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
     | mac            | address                | time     | static | router |
     |----------------|------------------------|----------|--------|--------|
     | 0000.0000.2222 | 1234::2                | 00:00:03 | false  | false  |
     | 0000.0000.2222 | fe80::200:ff:fe00:2222 | 00:00:03 | false  | true   |
     |________________|________________________|__________|________|________|
    r1#
    r1#
    ```

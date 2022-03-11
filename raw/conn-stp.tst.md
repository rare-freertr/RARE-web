# Example: spantree over ethernet
    
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
    logging file debug ../binTmp/zzz72r1-log.run
    !
    bridge 1
     mac-learn
     stp-mode ieee
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz72r2-log.run
    !
    bridge 1
     mac-learn
     stp-mode ieee
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show bridge 1
    r2#show bridge 1
     |~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                         | packet         | byte               |     |
     | iface     | fwd  | phys | tx | rx | drop | tx   | rx   | drop | grp |
     |-----------|------|------|----|----|------|------|------|------|-----|
     | brprt bvi |      |      |    |    |      |      |      |      |     |
     | ethernet1 | true | true | 33 | 36 | 0    | 2028 | 2172 | 0    |     |
     | ethernet2 | true | true | 8  | 5  | 0    | 384  | 200  | 0    |     |
     |___________|______|______|____|____|______|______|______|______|_____|
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                                     | packet             | byte               |  |
     | addr           | iface     | static | time     | tx | rx | drop | tx   | rx   | drop |
     |----------------|-----------|--------|----------|----|----|------|------|------|------|
     | 003e.186a.197d | bvi       | false  | 00:00:09 | 27 | 31 | 0    | 1790 | 2082 | 0    |
     | 0053.2436.0005 | ethernet1 | false  | 00:00:09 | 27 | 29 | 0    | 1754 | 1900 | 0    |
     |________________|___________|________|__________|____|____|______|______|______|______|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show inter bvi1 full
    r2#show inter bvi1 full
    bvi1 is up (since 00:00:10, 3 changes)
     description:
     type is bridged, hwaddr=003e.186a.197d, mtu=1500, bw=100mbps, vrf=v1
     ip4 address=1.1.1.2/24, netmask=255.255.255.0, ifcid=790313893
     ip6 address=1234::2/16, netmask=ffff::, ifcid=48323572
     received 29 packets (1900 bytes) dropped 0 packets (0 bytes)
     transmitted 31 packets (2082 bytes) promisc=false macsec=false sgt=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |       | packet         | byte             |
     | time  | tx | rx | drop | tx  | rx  | drop |
     |-------|----|----|------|-----|-----|------|
     | 1sec  | 3  | 3  | 0    | 198 | 198 | 0    |
     | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
     |_______|____|____|______|_____|_____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                          | packet         | byte               |
     | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
     |--------|-------|---------|----|----|------|------|------|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
     | ethtyp | 0800  | ip4     | 12 | 12 | 0    | 792  | 792  | 0    |
     | ethtyp | 0806  | arp4    | 1  | 1  | 0    | 30   | 36   | 0    |
     | ethtyp | 86dd  | ip6     | 18 | 16 | 0    | 1260 | 1072 | 0    |
     |________|_______|_________|____|____|______|______|______|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 0     | 1    | 30   |
     | 1     | 12   | 792  |
     | 58    | 18   | 1260 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 31 | 29 | 0    | 2082 | 1900 | 0    |
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
     | 0     | 31  | 31  | 31   | 2082 | 2082 | 2082 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
            6464|
            5817|  #
            5171|  #
            4524|  #
            3878|  #
            3232|  #
            2585|# #
            1939|# ##    #
            1292|####    #
             646|####    #
               0|#####   #
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
     | 0053.2436.0005 | 1.1.1.1 | 00:00:09 | false  |
     |________________|_________|__________|________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 neigh bvi1
    r2#show ipv6 neigh bvi1
     |~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~|~~~~~~~~|~~~~~~~~|
     | mac            | address               | time     | static | router |
     |----------------|-----------------------|----------|--------|--------|
     | 0053.2436.0005 | 1234::1               | 00:00:09 | false  | false  |
     | 0053.2436.0005 | fe80::253:24ff:fe36:5 | 00:00:09 | false  | false  |
     |________________|_______________________|__________|________|________|
    r2#
    r2#
    ```

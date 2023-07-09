# Example: bridged evcs over ethernet
    
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
    logging file debug ../binTmp/zzz28r1-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.11
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1111::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.12
     vrf forwarding v1
     ipv4 address 1.1.2.1 255.255.255.0
     ipv6 address 1112::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1.13
     vrf forwarding v1
     ipv4 address 1.1.3.1 255.255.255.0
     ipv6 address 1113::1 ffff::
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
    logging file debug ../binTmp/zzz28r2-log.run
    !
    bridge 1
     exit
    !
    bridge 2
     exit
    !
    bridge 3
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
     ipv6 address 1111::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi2
     vrf forwarding v1
     ipv4 address 1.1.2.2 255.255.255.0
     ipv6 address 1112::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface bvi3
     vrf forwarding v1
     ipv4 address 1.1.3.2 255.255.255.0
     ipv6 address 1113::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     service-instance 11 bridge-group 1
     service-instance 12 bridge-group 2
     service-instance 13 bridge-group 3
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
    r2#show inter eth1 full
    r2#show inter eth1 full
    ethernet1 is up, promisc
     description:
     state changed 3 times, last at 2022-05-02 21:10:19, 00:00:08 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is ethernet, hwaddr=0000.0000.2222, mtu=1500, bw=100mbps
     received 84 packets (5946 bytes) dropped 0 packets (0 bytes)
     transmitted 84 packets (5940 bytes) macsec=false sgt=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |       | packet         | byte               |
     | time  | tx | rx | drop | tx   | rx   | drop |
     |-------|----|----|------|------|------|------|
     | 1sec  | 35 | 35 | 0    | 2450 | 2450 | 0    |
     | 1min  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1hour | 0  | 0  | 0    | 0    | 0    | 0    |
     |_______|____|____|______|______|______|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |                          | packet         | byte               |
     | type   | value | handler | tx | rx | drop | tx   | rx   | drop |
     |--------|-------|---------|----|----|------|------|------|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0    | 0    |
     | ethtyp | 8100  | dot1q   | 84 | 84 | 0    | 5940 | 5946 | 0    |
     |________|_______|_________|____|____|______|______|______|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 0     | 3    | 102  |
     | 1     | 42   | 2940 |
     | 58    | 39   | 2898 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 84 | 84 | 0    | 5940 | 5946 | 0    |
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
     | 0     | 84  | 84  | 84   | 5940 | 5940 | 5940 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
           39.2k|#
           35.3k|#
           31.4k|#
           27.6k|#
           23.7k|#
           19.8k|#
           16.0k|#
           12.1k|#      #
            8288|# #  # #
            4424|#### ###
             560|########
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
    r2#show bridge 1
    r2#show bridge 1
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                                            | packet         | byte               |     |
     | iface                        | fwd  | phys | tx | rx | drop | tx   | rx   | drop | grp |
     |------------------------------|------|------|----|----|------|------|------|------|-----|
     | brprt bvi                    |      |      |    |    |      |      |      |      |     |
     | vlan11 on dot1q on ethernet1 | true | true | 28 | 28 | 0    | 1868 | 1870 | 0    |     |
     |______________________________|______|______|____|____|______|______|______|______|_____|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show bridge 2
    r2#show bridge 2
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                                            | packet         | byte               |     |
     | iface                        | fwd  | phys | tx | rx | drop | tx   | rx   | drop | grp |
     |------------------------------|------|------|----|----|------|------|------|------|-----|
     | brprt bvi                    |      |      |    |    |      |      |      |      |     |
     | vlan12 on dot1q on ethernet1 | true | true | 28 | 28 | 0    | 1868 | 1870 | 0    |     |
     |______________________________|______|______|____|____|______|______|______|______|_____|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show bridge 3
    r2#show bridge 3
     |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~|~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~|
     |                                            | packet         | byte               |     |
     | iface                        | fwd  | phys | tx | rx | drop | tx   | rx   | drop | grp |
     |------------------------------|------|------|----|----|------|------|------|------|-----|
     | brprt bvi                    |      |      |    |    |      |      |      |      |     |
     | vlan13 on dot1q on ethernet1 | true | true | 28 | 28 | 0    | 1868 | 1870 | 0    |     |
     |______________________________|______|______|____|____|______|______|______|______|_____|
    r2#
    r2#
    ```

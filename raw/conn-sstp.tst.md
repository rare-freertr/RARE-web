# Example: ppp over sstp
    
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
    logging file debug ../binTmp/zzz18r1-log.run
    !
    ipv4 pool p4 2.2.2.1 0.0.0.1 254
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 4.4.4.4 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 2.2.2.0
     vrf forwarding v1
     ipv4 address 2.2.2.0 255.255.255.255
     ipv4 pool p4
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
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
    server http h
     host * path /
     host * sstp dialer1
     vrf v1
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
    logging file debug ../binTmp/zzz18r2-log.run
    !
    prefix-list p1
     sequence 10 permit 0.0.0.0/0 ge 0 le 0
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 0.0.0.0
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     exit
    !
    vpdn sstp
     interface dialer1
     proxy p1
     target http://1.1.1.1/
     protocol sstp
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
    r2#show inter dia1 full
    r2#show inter dia1 full
    dialer1 is up
     description:
     state changed 3 times, last at 2022-05-02 21:11:46, 00:00:01 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is dialer, hwaddr=none, mtu=1500, bw=8000kbps, vrf=v1
     ipv4 address=2.2.2.236/25, mask=255.255.255.128, ifcid=781786563
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) macsec=false sgt=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~|~~~~|~~~~~~|
     |       | packet         | byte           |
     | time  | tx | rx | drop | tx | rx | drop |
     |-------|----|----|------|----|----|------|
     | 1sec  | 0  | 0  | 0    | 0  | 0  | 0    |
     | 1min  | 0  | 0  | 0    | 0  | 0  | 0    |
     | 1hour | 0  | 0  | 0    | 0  | 0  | 0    |
     |_______|____|____|______|____|____|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |                          | packet         | byte             |
     | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
     |--------|-------|---------|----|----|------|-----|-----|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
     | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 660 | 660 | 0    |
     |________|_______|_________|____|____|______|_____|_____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 1     | 10   | 660  |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |            | packet         | byte             |
     | size       | tx | rx | drop | tx  | rx  | drop |
     |------------|----|----|------|-----|-----|------|
     | 0-255      | 10 | 10 | 0    | 660 | 660 | 0    |
     | 256-511    | 0  | 0  | 0    | 0   | 0   | 0    |
     | 512-767    | 0  | 0  | 0    | 0   | 0   | 0    |
     | 768-1023   | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1024-1279  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1280-1535  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1536-1791  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1792-65535 | 0  | 0  | 0    | 0   | 0   | 0    |
     |____________|____|____|______|_____|_____|______|
     |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |       | packet           | byte             |
     | class | cos | exp | prec | cos | exp | prec |
     |-------|-----|-----|------|-----|-----|------|
     | 0     | 10  | 10  | 10   | 660 | 660 | 660  |
     | 1     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 2     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 3     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 4     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 5     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 6     | 0   | 0   | 0    | 0   | 0   | 0    |
     | 7     | 0   | 0   | 0    | 0   | 0   | 0    |
     |_______|_____|_____|______|_____|_____|______|
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

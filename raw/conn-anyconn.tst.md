# Example: ip over anyconnect
    
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
    logging file debug ../binTmp/zzz27r1-log.run
    !
    aaa userlist usr
     username c
     username c password $v10$Yw==
     exit
    !
    ipv4 pool p4 2.2.2.1 0.0.0.1 254
    !
    ipv6 pool p6 2222::1 ::1 254
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
     ipv6 address 4444::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
     encapsulation raw
     vrf forwarding v1
     ipv4 address 2.2.2.0 255.255.255.255
     ipv4 pool p4
     ipv6 address 2222:: ffff:ffff:ffff:ffff::
     ipv6 pool p6
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
     host * anyconn dialer1
     host * authentication usr
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
    logging file debug ../binTmp/zzz27r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     encapsulation raw
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.0
     ipv6 address 3333::1 ffff:ffff:ffff:ffff::
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
    vpdn anyconn
     interface dialer1
     proxy p1
     target http://1.1.1.1/
     username c
     password $v10$Yw==
     protocol anyconn
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
    ipv4 route v1 0.0.0.0 0.0.0.0 2.2.2.0
    !
    ipv6 route v1 :: :: 2222::
    !
    !
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
     state changed 3 times, last at 2022-05-02 21:13:09, 00:00:03 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is dialer, hwaddr=none, mtu=1504, bw=8000kbps, vrf=v1
     ipv4 address=2.2.2.89/24, mask=255.255.255.0, ifcid=313932548
     ipv6 address=2222::fb/64, mask=ffff:ffff:ffff:ffff::, ifcid=357408012
     received 23 packets (1550 bytes) dropped 0 packets (0 bytes)
     transmitted 26 packets (1780 bytes) macsec=false sgt=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |       | packet         | byte               |
     | time  | tx | rx | drop | tx   | rx   | drop |
     |-------|----|----|------|------|------|------|
     | 1sec  | 23 | 23 | 0    | 1550 | 1550 | 0    |
     | 1min  | 0  | 0  | 0    | 0    | 0    | 0    |
     | 1hour | 0  | 0  | 0    | 0    | 0    | 0    |
     |_______|____|____|______|______|______|______|
     |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~|~~~~~~|
     |                          | packet         | byte              |
     | type   | value | handler | tx | rx | drop | tx   | rx  | drop |
     |--------|-------|---------|----|----|------|------|-----|------|
     | ethtyp | 0000  | null    | 0  | 0  | 0    | 0    | 0   | 0    |
     | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 660  | 660 | 0    |
     | ethtyp | 86dd  | ip6     | 16 | 13 | 0    | 1120 | 890 | 0    |
     |________|_______|_________|____|____|______|______|_____|______|
     |~~~~~|~~~~|~~~~|
     | who | tx | rx |
     |-----|----|----|
     |_____|____|____|
     |~~~~~~~|~~~~~~|~~~~~~|
     | proto | pack | byte |
     |-------|------|------|
     | 1     | 10   | 660  |
     | 58    | 16   | 1120 |
     |_______|______|______|
     |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~~|~~~~~~|~~~~~~|
     |            | packet         | byte               |
     | size       | tx | rx | drop | tx   | rx   | drop |
     |------------|----|----|------|------|------|------|
     | 0-255      | 26 | 23 | 0    | 1780 | 1550 | 0    |
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
     | 0     | 26  | 26  | 26   | 1780 | 1780 | 1780 |
     | 1     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 2     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 3     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 4     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 5     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 6     | 0   | 0   | 0    | 0    | 0    | 0    |
     | 7     | 0   | 0   | 0    | 0    | 0    | 0    |
     |_______|_____|_____|______|______|______|______|
           24.8k|#
           22.3k|#
           19.8k|#
           17.3k|#
           14.8k|#
           12.4k|#
            9920|#
            7440|#
            4960|#
            2480|#
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

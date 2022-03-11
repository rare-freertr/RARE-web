# Example: lsrp autoroute
    
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
    logging file debug ../binTmp/zzz61r1-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.11 255.255.255.255
     ipv6 address 4321::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.1 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::1 ffff::
     ipv6 access-group-in test6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface serial2
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.8.1 255.255.255.0
     ipv4 autoroute lsrp4 1 2.2.2.2 9.9.8.2
     ipv6 address 9998::1 ffff::
     ipv6 autoroute lsrp6 1 4321::2 9998::2
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
    logging file debug ../binTmp/zzz61r2-log.run
    !
    access-list test4
     sequence 10 deny 1 any all any all
     sequence 20 permit all any all any all
     exit
    !
    access-list test6
     sequence 10 deny 58 any all any all
     sequence 20 permit all any all any all
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
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     redistribute connected
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
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.12 255.255.255.255
     ipv6 address 4321::12 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.9.2 255.255.255.0
     ipv4 access-group-in test4
     ipv6 address 9999::2 ffff::
     ipv6 access-group-in test6
     router lsrp4 1 enable
     router lsrp6 1 enable
     no shutdown
     no log-link-change
     exit
    !
    interface serial2
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 9.9.8.2 255.255.255.0
     ipv4 autoroute lsrp4 1 2.2.2.1 9.9.8.1
     ipv6 address 9998::2 ffff::
     ipv6 autoroute lsrp6 1 4321::1 9998::1
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
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface   | router  | name | peerif  | peer    | ready | uptime   |
     |---------|---------|------|---------|---------|-------|----------|
     | serial1 | 4.4.4.1 | r1   | serial1 | 9.9.9.1 | true  | 00:00:29 |
     |_________|_________|______|_________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface   | router  | name | peerif  | peer    | ready | uptime   |
     |---------|---------|------|---------|---------|-------|----------|
     | serial1 | 6.6.6.1 | r1   | serial1 | 9999::1 | true  | 00:00:29 |
     |_________|_________|______|_________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 dat
    r2#show ipv4 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 4.4.4.1 | r1   | 1   | 4   | 11  | 49510c26 | 00:59:34 |
     | 4.4.4.2 | r2   | 1   | 4   | 10  | b8c7b5af | 00:59:34 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 dat
    r2#show ipv6 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 6.6.6.1 | r1   | 1   | 4   | 13  | 49510c26 | 00:59:37 |
     | 6.6.6.2 | r2   | 1   | 4   | 12  | b8c7b5af | 00:59:37 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 tre
    r2#show ipv4 lsrp 1 tre
    `--r2
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 tre
    r2#show ipv6 lsrp 1 tre
    `--r2
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop     | time     |
     |------|-------------|--------|-----------|---------|----------|
     | L EX | 2.2.2.1/32  | 70/10  | serial2   | 9.9.8.1 | 00:00:25 |
     | C    | 2.2.2.2/32  | 0/0    | loopback0 | null    | 00:00:34 |
     | L EX | 2.2.2.11/32 | 70/10  | serial2   | 9.9.8.1 | 00:00:25 |
     | C    | 2.2.2.12/32 | 0/0    | loopback1 | null    | 00:00:34 |
     | C    | 9.9.8.0/24  | 0/0    | serial2   | null    | 00:00:30 |
     | LOC  | 9.9.8.2/32  | 0/1    | serial2   | null    | 00:00:30 |
     | C    | 9.9.9.0/24  | 0/0    | serial1   | null    | 00:00:30 |
     | LOC  | 9.9.9.2/32  | 0/1    | serial1   | null    | 00:00:30 |
     |______|_____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix       | metric | iface     | hop     | time     |
     |------|--------------|--------|-----------|---------|----------|
     | L EX | 4321::1/128  | 70/10  | serial2   | 9998::1 | 00:00:22 |
     | C    | 4321::2/128  | 0/0    | loopback0 | null    | 00:00:34 |
     | L EX | 4321::11/128 | 70/10  | serial2   | 9998::1 | 00:00:22 |
     | C    | 4321::12/128 | 0/0    | loopback1 | null    | 00:00:34 |
     | C    | 9998::/16    | 0/0    | serial2   | null    | 00:00:30 |
     | LOC  | 9998::2/128  | 0/1    | serial2   | null    | 00:00:30 |
     | C    | 9999::/16    | 0/0    | serial1   | null    | 00:00:30 |
     | LOC  | 9999::2/128  | 0/1    | serial1   | null    | 00:00:30 |
     |______|______________|________|___________|_________|__________|
    r2#
    r2#
    ```

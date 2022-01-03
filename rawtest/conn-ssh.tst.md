# Example: ppp over ssh
    
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
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFCdjdrRjhyNEpmKzRYTXVCVEFRT2pLQldKc0d4R2w0aWR2QjJ6VWRxNHEwazRQNk82SUovbERpNFJSWXdRUzFvdU1Zd2hwKzJUS2ljeklVUjZndGh6Z3RDNGlBM0ZibWF4aG5uaDU5dVpvM3hyU3NqRU1QK1cxd0wrN3BjMm5IL1F1bWZsVHVKais4aUhyRzZCTmRGRFdseWozUVIrZVpIMEhUbDdjSGZkNlRiZnV0dDV2N1ZhaUcyQ0c4Yml1aXdnSHlsQWZ1dkkwNEVYQ0J4bFFxWklETkRMeEdWTENMSHltUlowMUs5RCsvTkZJcHVJcVNmRGg3N1dmNkVBUnlkWnVQN2QxZDlyVldZWDdRWTVlT3R3NDZ5b1RqRXpIc214YW1zMFBzYTBnQnBMMGxKRWdYT1ZXVnJkOTFGZnlaaXlwU3hmOVJqUWFQczRac3hPb0IzOS9BZ01CQUFFQ2dnRUFLd29DUkY5NFVrLzA4dk1WaDVkdDY4Q0dSK3RncmRoNE1VazVuN2pDMzlSZUQrQVJXR21HZjJKMlRwVTBTOG9UZnJmVjFHckdKdHMxMHhEZUpnM2dyTWFidHBoOFRpeVpEREJUUXhLZEpsWWppa0RhZTB0V21MeTAvUUtVUVY4WUZaTS9PK0lQY25qSWNnNzlaTXNGQ242MVVkM0l1cThKSkhZT0k3V2lJM1NjUFdXeUw1OXVVS2ZlSDBsV21WTjRqbGF2UVdyWG9JNDA3YTRSVzJ1TC9ZTlU3dG5FWXZqY1dVenc3Mnk3dzkwUnR6eE5EOEpLVVlJemJRRThmbklSZUFsKzgwTG1JbWEyUHZLWWVKci9Ud09aRzhNemsxR3F5czBOak90RVpjSmNOY0VQcEVnMjJjUHZjc21nRkI0WjFwL1dmUzU4b2IxcGRXYlJRYWlLQVFLQmdRQzVZUHI1TEhZMnBRZ3p2dWhyRXY0NUJmZEprWXR6R0hQOFVtUXhjMGw4USswVlpRQUtjZXQ3RXkxMUVEekNocDFna0NMaTdiaUZKdWRUWllnYUt4QWIzdmJkSWNGN2M4UU1uVldOUmxtZCtlRXQwQUJwNTI5Q2x1ek5rUktJVnJYNkRpQThkeHR3RTkyMFdvZGsxNUNOT1hqNUxieU9lT2VETGh4dFliM05VUUtCZ1FDYWtrUHlETlhvRXZSM283YlY4NHRUbndJR0plVWZ2enArZHo3S2d0OUhPdENaWVYwdzhOOEFhalBZM0tDWlJlVlErMWJ1RENOSGNoWjVlckdsZjRjRWFhQmtCL002d1lPclh5SGtYMXl4WXBzTkF3NC84ZTBKU3RVL2J4Yy9SUm4yeEFZUzhOc2JoSVJMNHlyeklMUlNxNGwrazZ3ckVyRVFOd0VMblB3THp3S0JnUUNQL3dnVVkzZ1Q3RStadWxKWlVmQ05wTmU0bXNqQ2g1MFl3M3MyZWtIN3Q5dkNnYWp0ZEI0aGhQMExjS2h4eGhVYk8vc05ZUEN5NVV4TkdKSUhHYW95ckJnQUgwZG11TDd4dVlrSjZ6cVRudFZPTzhNR2dKS0pIQ2tuYU9nSFphdUhhRStjQ0QwVTZ5bU0vY0VzRU5JbEVSNnFGOS9lbjRYZC9RUng1cm1EY1FLQmdRQ1lXMCtweUVrWUJZYitYbHFiclFGS0hWTkxhQkxlSmdtc0dqSEVQeGVDQ0ZFUXZrMnpMZGxCZVcwOWRzcStDWTB0TTNET0Z4eTNFWmRoaWpTTVlwVmRIaGhBUVMzWVhtSkFpdmJIT2RBTjhKblFTNURDS3Q1djZGa2x1NFI0a3M0eTA2a0JCbk9TUGg2QkJwdVJKazFYcDBsUmdKR1ZxMGpvS0s5WkdSVy9OUUtCZ0hXdVhJeGRrbDQ4MjFHeXVhR1lqY0Y2TmwvUHNzQkJsUGpCbml0SXhjYzdMak16M0ZDTml0bXdzSGlrN3dGV0x4S3lYRm14MVRZaXlFTnBENlZCazBoWUlBcFBTTExGaFhKV0U0VnBDLytycHZVRUpCbUJKNkExV041b1lUNlVlUnRZak5qTHhxbFBGbGljRVZaQzIyQS9MVHpKbXlrUTBDTXdKSmZzUnpGdQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0ZQcWdQUDYzVzcxa3h4YUNrbjdIaHZQeG9qT2hZR2VQRUxKK2ZkMmkxd01VeDdrbVdDQzg4OTJKQzR4YnE2dE5JRnp2Z2RqbkMyQzNqRjdpdEQ0bGNneEpWMlRwajNzeC9IRUZwa1M1WE9DS1pNNTZFM1pqUFNrMWVFU0NlZDhxNVlTRER4UTVkdnhWWmlPc3J0VGNVV2xBVGlJLzhqRm1nL0MwTlMwQjRnckFoVUFwa093R2IxclVQS3BpVVRrS0FGYmxRdjhrcGtDZ1lBRXY2dXhtaUlHMGx1NXhyT0xKMHJ5TlVYdml4UkhvTnlueEpIVG1iemsxSFpuNTl0L1dPQnN3RTNJNXA2bDM4QzQzR1V0SzEyem9NOEI2Tk5TcTNMeFFDaXV1YkJlaW9xOURCOGx3ZkJSeUN2bFdXWTdYRjVZYzdkQ3FjcWEyR3lMNXFrZnF3OXovVkVpcUJ4UVNlWXczVytsTUFPaDk4STRUTCt1L2VidzRBS0JnRU9kK3dPTHNESmg4S3I0L1BRdHFaK3M1cmUzajVodWkvZSswVk9TN3lOeUllTWNHUnoySThVd2g2L3l1OEVZKzRsY3VVUHNBa09CUlBmZk5WbEs1Y2NpQ3V0WCs0N0ZEUC9JTXpuT1BYME9TODdNYUpmSXlVcWlvZnJCWHZ2eGJ4ajNPcmxHbG5XaDBpQUVLblVGMlgzSTZlaUZHRXZsU1hTQ0NPUjdZeCtrQWhVQWo5MkNPTGtIajdwbk9qMmdwcE5xbXF2WWFTUT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURQSE1ralM2SVc2bmc0aWZiVHQ3TUxyMXpQQ3V0R2VPOHpCaXlrSklobW9BY0dCU3VCQkFBS29VUURRZ0FFekVaNXVPNWdEQ3hRN2g1dmt5Q0hxQVhJdEZJS0MxSjRBR3VaUUR5a0c1OU5wcWFDVkQxbE0rUmYxNzhIbjJpU0xGb0k3SWFWRGpkTkgwdjFRdEIvNGc9PQ==
    !
    aaa userlist usr
     username u
     username u password $v10$cA==
     username u privilege 14
     exit
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
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
     no description
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
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.1 255.255.255.252
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
    server telnet tel
     security protocol ssh
     security authentication usr
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     exec interface dialer1
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    chat-script login
     sequence 10 send ppp
     sequence 20 binsend 13
     exit
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
     no description
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 0.0.0.0
     vrf forwarding v1
     ipv4 address 4.4.4.4 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 3.3.3.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     exit
    !
    vpdn tel
     interface dialer1
     proxy p1
     script login
     target 3.3.3.1
     username u
     password $v10$cA==
     vcid 23
     protocol ssh
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
    dialer1 is up (since 00:00:00, 3 changes)
     description:
     type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
     ip4 address=2.2.2.79/25, netmask=255.255.255.128, ifcid=63278296
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) promisc=false macsec=false
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

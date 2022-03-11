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
    logging file debug ../binTmp/zzz98r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQTVuWXVuRytiVnpva0tWMUt2K3Z3ZDRMZldZangyRkN4ckMwa0dqRUd1NGZRbU02c2Uza3NwWDJRVjIxQTJVMXdiMzlzcUNqWmFIKzZWclRZWlE0MkYxM3JEOHhIaGl3eHAwcDVnY01GODRqYjNXUGN1MGJDOVVMSGtQcldvL3JrazhNYW9CYTNXQy9FTnlkTkJTQm5UZXdqallJQ05DZnNYVnBCY1pnSHBLRTBKc0pYN0xiTDRVSDdZcEdPbmk4NTB6eTVKdk9PdHZ6dWl4a0JWVDR1UVdhdW5tQm1wVmQrN3ozc253Qlk4Qk4rMzBUZVhjcUlsdHZnNGFzRHlxeHdiOC8wTVZ2MzlPWlBPdG85ZXNoRjJHZFhhUFhvUUlrSGZWdU8vdThHMHJZaHBCSWhGVXhPRUcxRkcrSi9CSjU0NUNJeldxZUVpbm9lQVNrTFRsR2svd0lEQVFBQkFvSUJBUURPa3ZDRTJLVnRNbmhuZTNBZFIrZHJ1S3RySGcxcDBDcnlJaVJTTmMvTEdKb3AzbGRNOWZqRy9oMzd2N3A1RGFqU3lHMGs3aml5S290a1hRWDZ6eG85Sjdvamx3QWxqRWVWcEhQMWxGSXBVV3VDcnBpVVpZRXJSb2lMczh2aGdHcVM2RGRkZC84djFPRVVidTNpd29EV24rdmVVOEtWN1pNNHVrWWZCQjhWdUpXbVViOXNTOGN0WTdUTEp6aTdwMlNrNlEwN0kyTXlKTmhYYWp3L1h0NE1vaTFtbzdUQ2UzUDlKY3BhQ2RORFR3Q2tGL21BTm03WHhJZGxNNFRja015b2p3cWxYdXhsaTU1L04zdkpTT0x2dDFPTjY0U1RUMDgxVlR2RFhja3Q3d01EdUVsZnpTUnJObEhxY3JKTEZmcU9UUXJ6dzVKNXZoNkd2TTkzWUQ4QkFvR0JBUDJJTXJkeWViYmtBMzlJcFVjc3FpTHFsZ1BzdmgweFVLSzIxY0FJOTRnOXI4Yy84dmMxeGh5Q0dndnZHVkFNaHFBRVZrTHNQRjhKdTBEcWFhc1pSejZoUk1mRWgzQ0FvakhuOWp0RGRoMHRzZUJjNzRxY2ZGbzkrbEVNaVBUdEpDcTFBRmg3WEE3Z2pPRXJGRjRrZ2RCR2t4LzkzUWp2ZjBjM0ZBa3k2YlZ2QW9HQkFPaTBmaG05Y05hdkNKT3NlRmViZnBxSWdqdFQzWWFnQjRXdThxdWZuc0pGOUJSb2tWMUhydjFzMm40ekV3SkhBVUxtSHRWWnRZL1FETXFZamVXYi8rQ0FCQWV4N0EzVkF0NDFpM0YyQlBRWE1XeVFydUlnTnc4eFdIT2lMQUREUTVhUGJPMnlBQ0JEQ2hCNWxva3lFdkV1am5GUXFqMzZwRVhPcTJGNWJ1RnhBb0dBZENjVzNUYkVEb2RPRnQxb1kwQlNQaWJ0VGFVRHdJb2NZRCtWbENKSGpaSjlXckt3bEpOOVRRaEorSmUxS0JobEFTQ2JpSk9FWVNJck9PVnNQZWdaM05hemxUWXp1dFlqK090Rnd3YjRNUXdEUjBBc3VudFErV01Wc0ZZbTFOZGtUM0NYVlBKSFRjV1FwWVJBRTVWMEo4QjluUldJVTVTdDRpbVlzMUl4QWw4Q2dZRUE1VTJ1RUtrbS9yVjlpeDdoZXRxRGQ3MWFMeUhsNFpuaHI2NkQrL0FQSGJxVzJHRnVGRy9sbEYzbU00TWFrUnpzdGtKU1VjUFRjRUgveU1kbzA3L1Q5U0hRVnREUkhaUXYva3plK2sva2M2NURDb3JMZVpGckQvSjlDWHpkUldja084RmJBaUpyazE3Y0ZQM3JBNGd2T0MrN054ZlltYmhZbFYwZ2JhMmVRRkVDZ1lFQXNQRWZFQjBHQzZPTGFnMkR3cjl6TGZIeUl3V2lCNWZGMDUxMVVYU0JWbU43eHNiODB6bGgwVDNvdDhGM3NBQmpPLzdiYW9TcW5WcktkVlRpb3Fwdk9aSTQ1VHJhUXUvaFdaeWtZSXNVRlBtR1loMlhMcUY5dk5kNkN5WWtKWUdWODB5NnF3Rk1LTGdBU0tZZEJOR1dXQjhUYVdnTitOSW12UDZ2eUNad1Z2TT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0U2WFRMRTd4dlBYUUtncGY1U1FoSFlETmF5enQrRTM5c0hVcm9MaGQxbDl4WG4wRE0zS0NiQk9LQWx0R3FGQVRpNFR1RlpSTkVraGdIZDlMTEVBVldwZWdnOGc0VDlydkJ0cUlWczRTNUpPc3Z1UFJvZGJZS1FZSXNFN2ZoVVdsRHdLZEYrK0xZTXBQZTI0R29Mc0d3THR6b3J4REpBQkc5K2szeDBnV1JncEFoVUE4Mm5kbHBtOElaVE5QbllYeHJsa0dzSmg1SzhDZ1lBVmpERjYzeVBtcCtWcDVWcWVjNTBZNWNSUmJEUXR5cVJON2RpazZEQ1VBK2ZNQmhNZzlQNFR4U3htTGoyaE9YS3MxYllhZ0FwTDJzVXJIV0gyRGtBdEpyTmNwNHdueGQ3WGtBY2hWTGxCNWhOY3A5Smxrd3c1aFRUMC9hLzQ1WE9EeXB5VldpbHkyUERQM2hRaHZLRzZJdEhyVnc0L1B1ZGsyejc0SWN5UGp3S0JnRVgzV1pjVzdBeCtDZXhYVnpxWjYxbUpyVjdTRmhIYy8wQzZIRWVzTEFHNVdtYytTSHJPWVdneGNjUFQxRXFqZU52dEpFcmVsdDJvR0MzZzlxZG9hNnNHUmJJZHZ3amtPYk8rMit0VnhaSHRWRXF2T2dzOHNEMWNIYW43U0NiY1FBUk51aE1RSmNmVGRTc3hkUlJuTmNiWFhFelNVVEtOVUdLSGZjWFkrL0RIQWhRSklLVGlNWmMzSHJKcXd5RU85bFhHYUs0WG1nPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMEVxZ0FKV2dvNExzTzhXNDRMZFJBejViZTZtcUNwZkNVZGJYZGxhZitDZ0J3WUZLNEVFQUFxaFJBTkNBQVNWVHpWS2Vlc3cwY1BERmRKb3Z1N3pWY2tYemtmZHpWUG8wVUZVMWUycy9sK0RBcUkvelJlRWZMWlJtcUE0MDhGa2hYclQ0OHFLS0o5TEhGUkp2YnZF
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
    logging file debug ../binTmp/zzz98r2-log.run
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
     ip4 address=2.2.2.61/25, netmask=255.255.255.128, ifcid=898191263
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) promisc=false macsec=false
     |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
     |       | packet         | byte             |
     | time  | tx | rx | drop | tx  | rx  | drop |
     |-------|----|----|------|-----|-----|------|
     | 1sec  | 10 | 10 | 0    | 660 | 660 | 0    |
     | 1min  | 0  | 0  | 0    | 0   | 0   | 0    |
     | 1hour | 0  | 0  | 0    | 0   | 0   | 0    |
     |_______|____|____|______|_____|_____|______|
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
             10k|
            9504|#
            8448|#
            7392|#
            6336|#
            5280|#
            4224|#
            3168|#
            2112|#
            1056|#
               0|#
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

# Example: ppp over tls
    
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
    logging file debug ../binTmp/zzz99r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXFUWklMZHFkWXpPVEo5Yktsa1ZvOXg3T3Y4aHNwZlNCY3JWNFIzbjM3OG1oaFdpdmdWdHkzQit4TzQzSHRiZnFIV1lUcUJrRzg4U05DQ0F4OEphczloODFxMjUzQit4bHdjTjcwZzhGcngzQjBZSGxOa1RTMEljRE83N2FiS2tRSWM4NjluVk5TUm1zOHdjcE92U0NTMUlsSUtiUlNoZDE0NDlWVjZJdGYxVnZiM3UrcG5tdHRNM0t3NnFPKzJpL3RIaDVNTHZEYit5S0RyRm4yc1B6aGY2MVNuWlNGTk9UaEEyVmhkZ0lvc3lVTFNvcUFBaEJkNXZ5TkhoVEpidXZoUHNNZGZkUVdIQ29VWWtqYTFXZmdmUFVKbHF0cDM1cGo0dHZCcEZmTmZyTGhpSDMrdHFwZ2RwbkNpcExzY3RWSEp2L3B5MGt5V1RwWFZzRnFnN2ozd0lEQVFBQkFvSUJBREV5TlA0UDUxNW1La3lVNkVXVVhKWXNnTlBGZzhFa08xYU1hREh2eGlRVExVREtWT3g1R0FYanVQV2xuUUM2UGZqYUtyRGV4ZVN0cW90SVFQeS84ZjJFeVdmVU1Bcy9zYjRLQmIvbTJqSTFwcG93OStFMVZVMkhVMnRWYTgvWHYzYjA5eUdjclNHcHMxemRJaUdmNFJuaEFpWmlHY3MrMHVtY1RLV3o0eUozelUvZDlZYWhCaC9uTXg5RU1SbGxqaVhDa0tXZlJvQTMxRXhzV1doWmdURTJxcGcvb3N6WWdKRU5hSlV3WG5xUzlRSmJmbm9tN2FsNG44MFR0SlR6SXIvTTFkdkxzZFdjQzBUdEdyYVpFQlRkVlJXRTBhbHQ0aFBab0krK2FWT0FHdnJYalF4N2ZzY1JvY2gwb0hYN0IyUzBJNHgyT1ZBOHVnN2lveDRaQlhFQ2dZRUEyWWxZTFdxNkgrSDk5blVhNWpZZ25SUjU0VjYwUnowZnFIYkZOelZibWxtS2lsbm8yQXF1bzhZSWp0NHZjbmMwY0JvRHA4Z2N3b3ZIQ01VdWpheW9jSWlYb3NYMU1HZG5Yd2NyMWxDSEpERGExT0ZnOEJiSzNGUlZ1WkVGWUxYTnBFSXFCRlF5WFBtWTU5elVTWWxtbEk1Q05TWGtETjR4bXVoeVBvK2pEN01DZ1lFQXh5R1BmVW1HazgyaWd0UG5mdUpmMEpIMVVTeVBCVlAwWnNvaXhHMWVpK3hlVEJ6d3dEOUFNUXQyVWF1MENjRzBDZUtCMVB4aHV3MmF6TGF3NkNlVVNOeWg1SHJCaUNnWXVhM0lPY25ZNWdYQ1hhRUNrSy8xWFlueUgydUN5algrUWMwalM5QjJIU2F1aHlFMkxreDJGNllIeHdEejQzWGFycFJXeVo2RVpTVUNnWUIyUWFhdzBlTXFyK1VxbE5DeHMxMFpaMmMyY0JCYTVjeU8vVG9LNERQUy9iaEZxOGpib1RyOUJ3dmg5c0VlWGRVZzE5T0M0MU5YSXp0bzlpQnZuaHZYU1RuOW45WEJvWVRkY1AyUXZTZ3FNWERVNTB5V1dCMmhseXNlL01wS242cVNEL0hkZHBRR1hSMlZka1BsVWc5MDFMMERQWHp5emR0emxjZDlZUUpJNXdLQmdRQzZpV1d4Sjc4NWxkZzJWZXIxb1huQUYvcUdJQWVhSmhzOGJ2NUNvM0YrQWQ0VHpzaDRUc2dES1ltYzJBdS9XQVVmZlYvQjlPcFlIMVp6am5BS0NZbU85NTl3T000eWpkMGJrditOb3RmY0lta0E3R05LeG9wREpZWDZpT3ZzSU1nZE85MWtsOU1OVzc4Q05zcGFkS1hyWVV6SHpzeW90eTR6ZkNJUW5MM0pRUUtCZ0gwR2FHa3MyNXJWN2JKeFdORk9yZjQwVWJKSkJpYS90R2phNGExNzkvWWNYaHg2cHdkZkRHdm0rcGNkdVMzOHkzdy9MUElHb2JEeG9OUXZGbjBnVkMyYmVYa0hZSHZoSFVHaFNuZm1ZZjRzSTB0MlFLSmhYSEpIbTRicm94QlBmcWVWWFlJclEwZzA5bEtEd005OGlSdmFvUzliYkhoYWg3U3BZQnFNNHJTTQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0NWZ1JsQ3o0ZHVuSmQ0S2tqZHFCV0hHUGdGRVZpZExXcmlwcXJRSTNsNDQ0ZEZLT1E3NDc4Mkx1OWY4N2hkYWJoQ1R2eHMzbUcvcjlTN2NqY1JJcnV5K1JXZy9jQlZFTnhMR3FrV1dMNEFGejI1RDRMdWtFK3VweHE2UnMrOTFEWkZwM0VhVUFsdExkV25VOUN1SlBRbDN5L29LbGJ0ZXhLbE84SlBIZmppM0FoVUE1eTVxTUN5ellCVFRSdDhRTjlER1NUYTVhc1VDZ1lBUEg0eHB6MzBTaHhybGNpMnJaTGN2YWNzaUcvcjdlWVRIalRWN3EyY0t0Y2I1eXF4VkE3RnNJTzFub3hZOVZhblA5SUdBTzZHUDhKV1JjNy9vTzBXN21VSnVpcXAyNjR2ZEVwUzNTZUh4Tm9LaWZORk1aUklxZ2ZPVFhzN2JQVFZGS3ZEa2hPcHZQaFhmUlRCc2xwUUZ3d3RGWlpCaHF4TFdNN01Ib1RxeWd3S0JnQWxkSVlWOE0rRWliZHF4dUd4cWFVYktBRWlobnpNbDF6MThUaFBDbXZSb1NsbzhWUlVtQjR2MzRMcm1wa2txeCs5UDdIbnpyTDBzWWR1QXBPYjV3QVNIN01UTTRnMjVWVnAyZUhnc3FYVW1MeVNTNjIrOFZ4blpVbFZWaHJTSmlVLzRsK2pydEhGSFNSK0NQMlIxQzBTb3loNXlDaUtQSzRhUThOVEJFUWQzQWhRL2dBVEQvcTg3SDhZQzJUV1RjTXNvK3NBa3pnPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIekVpMW5nNmdVQmg5bnhoTTZKUkM5NldwcDNXV3pMVzk4cDFEU3pNK2FlZ0J3WUZLNEVFQUFxaFJBTkNBQVFNTmEvc1FOZzZJRkNyN1NBV0lmVEVRYTBnSklzRG13U0N3MkFSb2g4NVVEL1ZKY0R1cjNOYmVjYVBpait6L21vOHZZRkRVMWZnOWllMDlUc2labnAr
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVDNW1YRVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBPREE0V2hjTk16SXdNekEzTWpBME9EQTRXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NWZ1JsQ3o0ZHVuSmQ0S2tqZHFCV0hHUGdGRVZpZExXcmlwcXJRSTNsNDQ0ZEZLT1E3NDc4Mkx1OWY4N2hkYWJoQ1R2eHMzbUcvcjlTN2NqY1JJcnV5K1JXZy9jQlZFTnhMR3FrV1dMNEFGejI1RDRMdWtFK3VweHE2UnMrOTFEWkZwM0VhVUFsdExkV25VOUN1SlBRbDN5L29LbGJ0ZXhLbE84SlBIZmppM0FoVUE1eTVxTUN5ellCVFRSdDhRTjlER1NUYTVhc1VDZ1lBUEg0eHB6MzBTaHhybGNpMnJaTGN2YWNzaUcvcjdlWVRIalRWN3EyY0t0Y2I1eXF4VkE3RnNJTzFub3hZOVZhblA5SUdBTzZHUDhKV1JjNy9vTzBXN21VSnVpcXAyNjR2ZEVwUzNTZUh4Tm9LaWZORk1aUklxZ2ZPVFhzN2JQVFZGS3ZEa2hPcHZQaFhmUlRCc2xwUUZ3d3RGWlpCaHF4TFdNN01Ib1RxeWd3T0JoQUFDZ1lBSlhTR0ZmRFBoSW0zYXNiaHNhbWxHeWdCSW9aOHpKZGM5ZkU0VHdwcjBhRXBhUEZVVkpnZUw5K0M2NXFaSktzZnZUK3g1ODZ5OUxHSGJnS1RtK2NBRWgrekV6T0lOdVZWYWRuaDRMS2wxSmk4a2t1dHZ2RmNaMlZKVlZZYTBpWWxQK0pmbzY3UnhSMGtmZ2o5a2RRdEVxTW9lY2dvaWp5dUdrUERVd1JFSGR6QUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRHNzODA3TWVlU1NWUmdkL0RYODM0QnViV1BxQWhRVVN2MlJiM09kQmdDQVBWbTlFUGp6amdZV1pnPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUmhuUFVzTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBPREE0V2hjTk16SXdNekEzTWpBME9EQTRXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRTU5hL3NRTmc2SUZDcjdTQVdJZlRFUWEwZ0pJc0Rtd1NDdzJBUm9oODVVRC9WSmNEdXIzTmJlY2FQaWorei9tbzh2WUZEVTFmZzlpZTA5VHNpWm5wK01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUl2bTVDR0h6cmpGNFRpSk1GOGo4QTZBdEpMWnc2K0h4RjdDc2FzV0FEeHJBbDhBenpIa2UrSWVJd3FlcStlbzlRZmoxeHl0THJjTUVOdWcvSXdKNzEwTXkzN3FjaldBa0ZZTzNyc0NvTGpYZEpxWklDQUZGUTdENDd0MDN3WlVOcVpPMnduWjN4TjI5OHpGcEVOWnBqQ2E1ZTNDTlQ1amI2Qm5qRjl5eURjQnB3PT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVQTUpWcXpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFE0TURoYUZ3MHpNakF6TURjeU1EUTRNRGhhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXFUWklMZHFkWXpPVEo5Yktsa1ZvOXg3T3Y4aHNwZlNCY3JWNFIzbjM3OG1oaFdpdmdWdHkzQit4TzQzSHRiZnFIV1lUcUJrRzg4U05DQ0F4OEphczloODFxMjUzQit4bHdjTjcwZzhGcngzQjBZSGxOa1RTMEljRE83N2FiS2tRSWM4NjluVk5TUm1zOHdjcE92U0NTMUlsSUtiUlNoZDE0NDlWVjZJdGYxVnZiM3UrcG5tdHRNM0t3NnFPKzJpL3RIaDVNTHZEYit5S0RyRm4yc1B6aGY2MVNuWlNGTk9UaEEyVmhkZ0lvc3lVTFNvcUFBaEJkNXZ5TkhoVEpidXZoUHNNZGZkUVdIQ29VWWtqYTFXZmdmUFVKbHF0cDM1cGo0dHZCcEZmTmZyTGhpSDMrdHFwZ2RwbkNpcExzY3RWSEp2L3B5MGt5V1RwWFZzRnFnN2ozd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQU5mdFc2T0VTTmxHQlZBSlFWenptT1ZETzdvZEF4MmF1NzF2Zko4aXZKRVYvWXd3MlJXa2hYM21udmhkbmdrSVRKMGludVorMThjalBwZWNMT3JDMkFIMDVNTlRkTEcxcDgxVlY1am5SQ3hmQzB4b2w0dEh6Z1FKQTh5Y0xHQlJnS1Qvb2Z0WlhYWlBYcjdvbGFzRWpFM2l2Q09WWi9VblpnWEd5dHZIOWx5ZjVrQWYyRUZJSURQK0ttd2xGeTBZUFd0cmgweVd1eWtVdU5DL1FySm9GS3hTVGlXaFhGM2IxWjh1dmtTcEI0Z2JVYUdoUGRtQmU5U2hiakpDemsrU2E3ZGF5aWhzM2VqYVVETEZkN0Zvc3k2K0hKMU01RXYzbTVQa21WN3o4YXpXSXUxM2YrQjFCSlNzaUwyVGQvVUt0K1hWYTVwanhzNndDUkFMc0ZpRE5p
    !
    aaa userlist usr
     username c
     username c password $v10$Yw==
     username c privilege 14
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
     security protocol tls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     exec interface dialer1
     no exec authorization
     login authentication usr
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
    logging file debug ../binTmp/zzz99r2-log.run
    !
    chat-script login
     sequence 10 recv 5000 .*ser
     sequence 20 send c
     sequence 30 binsend 13
     sequence 40 recv 5000 .*ass
     sequence 50 send c
     sequence 60 binsend 13
     sequence 70 send ppp
     sequence 80 binsend 13
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
     vcid 23
     protocol tls
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
     ip4 address=2.2.2.167/25, netmask=255.255.255.128, ifcid=565763274
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) promisc=false macsec=false sgt=false
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

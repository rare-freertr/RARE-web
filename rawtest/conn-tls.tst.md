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
    logging file debug ../binTmp/zzz1r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCL0FNamp2MHFEWjdTVlZWQU9HZG9JV0tkeHRibk5FQVBMZk11OHFsQnNVMldlZWMxNm53Z1cyQ3FsWXphQVFEV0kyTDhFd3ZWQUZSUS80d0MrWFF1N2QyTFVpcHJiTERJNXBmeWRWN09QWk52MDJlWWF4Yi95S3ptQW9TQURGdW5ud3BNdDF6VVR5TmpNYjVKUXNDWDNjVWhFUnRuUjRLM2dZejZSNVIwb0NieitOenJxalZmL2FHa1dkZU54UzhCZGlxVHl1cDlyV3RENFBwMTRKaDh2YmsyeTdRbXM3WjZpYkhpUkhQUkd1d0grNjNwUjBPSFlNRXhPVVlCRzJPT2NxNm8vWSt5ekVDemNmaTVYRVR6eUNwOFUwRjFLYU1NNmpRdGRyUG5jQlp1elYxUnUxRGpoWUpsZ1FMSzBxQ2Rjcmg5S1dJR2tsWXdONkt1aE01QXhBZ01CQUFFQ2dnRUFPVFpPU1NKOFc3UFZDc3l5MHBkY3ZCUEw0cEtkejczZUo4WGhOZTEzYTBVcWF2aXQwd1pmSzROWHVzZDEzdEtPQzBhd3ptRlEvL3crOGdTOTZnT2FiR244c0loNytDM3h0anlMRHdwYURrZStPcEFLYzVjUHYvVXU0ejR5WUpIcTd3ZWRLN0pkNjdxM3gyaWZmZy9NR3FzQ2hoZHd1blkvZmV6WFcvdmRaWkpTL0ZSdlJ0a1dKai9RbGxBekxEajdoMVp6NFRSWXRwbTFMc3Y5SjdKcDZHZlRZRkhFWGJob0t3bzRPZzJwVGlCYWlzSDVuR2o2S2oyclRFc2RJYlgyMWFIQlMrZ0pRbGRSbHR1QlY2ODRFWVVlOVBUSVJUb3p4UTNrRFRJazZwSThwWmtUd3R0MHA3Qnl5c1laUmtJc0xTOVI3WS81LzVHalNiNzk3eXEwVVFLQmdRQzRmVThvUVVVd1Z0NVRLS2dQdUVZY0ovMkIwV0xhandwdTJwWTVEc01tZG1iSEI5U1RBbVY0enh6aW5WdE9ob1owZDdpblFDVVdsRG81L3NvSGpWSFYwUzdteEt4MEFIVEhXMWt5dFMweXlRdDROVHJ3WG1STEluWEJyRG5kY3dDWVBuaDZRb3U1R240b1luWjd6OXUwNXUrZmJucm43clBJSk45M29YTDVOUUtCZ1FDd095a083aURKcEdtRzFlaHp2TTBrVzYvOEk0amlKd05GcVVldy9XUDJxUnlESTAyaElpdWdnSFJEUERTUVYrdHVjeFhrNXdEdWZHdSthSXo3bDVIK0FoTis2MGlNU0Z6R0RvdUVxV3ZUQVQ4Smd4S25Md1pCWXA5MzNkZ3k3Rk9KdllDL3k3WEpYQWREaVBSOGMzaUR4ZkxQMVpzWW1hU1hWa1BETmhiV2pRS0JnQnU3MnJaMmVXdzI0dDBsYzM1SmVXQ3FNbFhkb0RxeTNpS2tBWWs2U3VQeFVLb0M1MVhpT2xiYTY4QzFYeENDOEp0NWsreXdtK0sxRGJ2Q0xhVE0vY3hpMGVZbkVyV3RpK0NjUHVCOGsvcmFkanJ2NVpoVTJFYmpPMGlPRjNUTzRQd0NDQ0o0OW9BeEYxNEN6MFQxamxXM2tiWXA2WmdNTGtLY0tHdlhmVzB4QW9HQWJISXJaUFdpbFpNb0lRSTNCaW16cjJFQW5jOGNKOWJNQzYwTTRkdzhESWlxZEFSZ2UveTBEaE9kOTlYdm5yZUx1QzczMVNGV0VHdmVQWkRHMlBlL3JpaUc2TDVPcVl6S0VsTFhCaTdmbkR3VEYzNWlGeUUzM3pxYVdUL2FFQlFmb0E1T1VUaEJTSVRxTDJQeTF6YVRmYnR0SFBvY2MvbndML1MweEViZnJPMENnWUFFM3VlaEFnMkFNYkdIM2pDTlgyY0l2NUhPNUkvZVRBOGQzeGFTKzlqWWFOTDBZU1NuZkhmSHpOSUVhMmdhczhnTldtTnhaME9wNmg2MkN5N2p3eC95elZjTGZMbUJMV2YzOTJ1L09oR1c3MHFBbUFndjB1YkkrSTBjUlVtT3k4d3dXTUQyMlhNZEVQdmo2dWZyQUpNZVZRdkR5STd0WjlVOHZldDE1aFJad1E9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVBSUJBQUtCZ0FHN0hSSzNvZGR1RWhpV09aL1A2RlFTLzFsOWsxeTBaT3MweUFqczZnbnd6S2pzYUVEUDlnV1o2aGtlY0xRblRLQ29FS1RsNmE0Z0RVVnhBN0RCNnFjRXIwQ3UyNmk4T1BQN3g3M1dCSHZWWDRpY0tRRnhpSFkvbUY1YjlMWWRySUtkdnZtNThUNWxUTVZFVTFuTTFJajR0b1lUMzJ3V3dVekRlN3hLVXBvREFoVUFvUFFLRjU2YkNCR2poTXVoK3lXbTZza2d2ODhDZnpTa2F3MERSZ0tVRExEQWVnbWVzTm1DeFNHRTNDZGN3MXdXZ0dqbXJmRVlUQklYRkErREd0YUVUNEg2em4wK2R4Z0pzL1JPTk83Y2tjT1lQY1VINmw0akxTbTRSLzU2cks3MFlmZzE0cGRKNFJaUDFFaWJ0NFpnMm5HSUJPMVRGeVFDNmQ3Y01ZYjZtM05qbWREaDhDR0RFWGpWQkZuaThkakorMVd2SmdnQ2dZQUJNMUduQTZuN00zdFVwdU1GODlVMUlucDYwTHlXd0UzT0lDaHVBYmZnMCtZNEE4emNLZG5ZRmVjSkhrTUl4V1QyRklJWVhaS2UzRXJrNlhXdkl2dlB3MWpuS2ZEbHF1UzM0VWxucWlFRTFNQlY4TzlxY3kxWjc5ZUJxUGlLYldYV0thR2tray9tQnFJSGZiWkZNaysvSXpvVk9IZmZHdUgzZFFKQ3hkWlZJQUlWQUlRL3JJNmFEVHdnd01mZ2R3NnpjS09TKzlTbg==
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeVZhb3FTR3JxWStiQzMvUThxTlZScGMzN3NuWlByRGJ0eVVhVkJ4eEw2Z0J3WUZLNEVFQUFxaFJBTkNBQVJBeUhMYmJNWmx5UFVnSVNndnp6R1l3TFdmTk8vNHU2WFFmczVxcjEvZnJPaW5vNE9pVmNBam82ajZsSFZYVGc4RWQyOUdTSzc0Y0tIbWZTZC9zTVNQ
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VEQ0NBZzJnQXdJQkFnSUVEdUZjcERBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01UazBPVFF3V2hjTk16RXhNakk0TVRrME9UUXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYk13Z2dFb0JnY3Foa2pPT0FRQk1JSUJHd0tCZ0FHN0hSSzNvZGR1RWhpV09aL1A2RlFTLzFsOWsxeTBaT3MweUFqczZnbnd6S2pzYUVEUDlnV1o2aGtlY0xRblRLQ29FS1RsNmE0Z0RVVnhBN0RCNnFjRXIwQ3UyNmk4T1BQN3g3M1dCSHZWWDRpY0tRRnhpSFkvbUY1YjlMWWRySUtkdnZtNThUNWxUTVZFVTFuTTFJajR0b1lUMzJ3V3dVekRlN3hLVXBvREFoVUFvUFFLRjU2YkNCR2poTXVoK3lXbTZza2d2ODhDZnpTa2F3MERSZ0tVRExEQWVnbWVzTm1DeFNHRTNDZGN3MXdXZ0dqbXJmRVlUQklYRkErREd0YUVUNEg2em4wK2R4Z0pzL1JPTk83Y2tjT1lQY1VINmw0akxTbTRSLzU2cks3MFlmZzE0cGRKNFJaUDFFaWJ0NFpnMm5HSUJPMVRGeVFDNmQ3Y01ZYjZtM05qbWREaDhDR0RFWGpWQkZuaThkakorMVd2SmdnRGdZUUFBb0dBQVROUnB3T3Arek43VktiakJmUFZOU0o2ZXRDOGxzQk56aUFvYmdHMzROUG1PQVBNM0NuWjJCWG5DUjVEQ01WazloU0NHRjJTbnR4SzVPbDFyeUw3ejhOWTV5bnc1YXJrdCtGSlo2b2hCTlRBVmZEdmFuTXRXZS9YZ2FqNGltMWwxaW1ocEpKUDVnYWlCMzIyUlRKUHZ5TTZGVGgzM3hyaDkzVUNRc1hXVlNBd0N3WUhLb1pJempnRUF3VUFBekFBQURBc0FoUWpHRzc4R01WeUQwU2toUWFhc0dCWGhUUkhYUUlVZHlZZVVnbmtWOXhxZlRENk0vYStCQVJRQjhNPQ==
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUnFpTnlrTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01UazBPVFF3V2hjTk16RXhNakk0TVRrME9UUXdXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSQXlITGJiTVpseVBVZ0lTZ3Z6ekdZd0xXZk5PLzR1NlhRZnM1cXIxL2ZyT2lubzRPaVZjQWpvNmo2bEhWWFRnOEVkMjlHU0s3NGNLSG1mU2Qvc01TUE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnQjk0akY1NHh1R3NFNWU1S0pqV0QxNm5oMUU4NkRnTmxMWWFKN1hIaTBMQUNYd0M3UWVZVWJXNy9HTlNWUUx0ZEJXUmxKcnJvYk1FaitCekI4Q2k3em4wblN5L3RkRll6cWgzejBkcmZRZVozMVJUZENmVnBSNXFwMjdBS2crVE9udWszODVLUDh1Q3AwazhYaEVZenhSNEN1dkVlL2Rhd1hVeTE1amI4bFdpTQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVEUTJpTURBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXhPVFE1TkRCYUZ3MHpNVEV5TWpneE9UUTVOREJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCL0FNamp2MHFEWjdTVlZWQU9HZG9JV0tkeHRibk5FQVBMZk11OHFsQnNVMldlZWMxNm53Z1cyQ3FsWXphQVFEV0kyTDhFd3ZWQUZSUS80d0MrWFF1N2QyTFVpcHJiTERJNXBmeWRWN09QWk52MDJlWWF4Yi95S3ptQW9TQURGdW5ud3BNdDF6VVR5TmpNYjVKUXNDWDNjVWhFUnRuUjRLM2dZejZSNVIwb0NieitOenJxalZmL2FHa1dkZU54UzhCZGlxVHl1cDlyV3RENFBwMTRKaDh2YmsyeTdRbXM3WjZpYkhpUkhQUkd1d0grNjNwUjBPSFlNRXhPVVlCRzJPT2NxNm8vWSt5ekVDemNmaTVYRVR6eUNwOFUwRjFLYU1NNmpRdGRyUG5jQlp1elYxUnUxRGpoWUpsZ1FMSzBxQ2Rjcmg5S1dJR2tsWXdONkt1aE01QXhBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCTVlLeDJGUnU3YmVSSGN6b2w4R3l2Q0kvbWJiajVvNXBYRCtYeUZuRDgzdlNjVzd0ZWt3bGU3NVNCbDRxTkNuLy8zSGRualV3bjlhQ3VidmlsSUtmNmp5bDBpVzNKQWZOSkRRTHZmM3JBUFVDSC91VFcyQkxKY2ZjMEFJVmRsWTJrQVAzYnlXejhmd1RxY05PRjRnL3hTcy9CdXdkUWZVWlkyd1hFWis3NVozTEZmaUpwUmpSR3NPR29QdHp3NTI5Slc2OWhqUkRhZUw5YXdxMUZLeVBYWVRMRTRaclNoTE1kdVFmSEo3NW5Vdkl2REJRZno5UzZxOHBsRjNvRkJseU9UdHBOTkVKM3V2V1d6SWpJM1VPcjEvK2RrM0N6ZUxXVndYUUFqcXYrTzkra3BmdGY5dk10QkZkeHRWT1A1RDhrazgveHJCOFFuQTd1R2pEckp5ak09
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
    logging file debug ../binTmp/zzz1r2-log.run
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
    dialer1 is up (since 00:00:01, 3 changes)
     description:
     type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
     ip4 address=2.2.2.240/25, netmask=255.255.255.128, ifcid=277007140
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

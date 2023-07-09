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
    logging file debug ../binTmp/zzz4r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCVnVjbTZkL2ZCZDd4YWVpRnVlWDNRUDh1MTRhTktjdTIvdlppeHgzTVlVa0o5T2JKVHFGV0IxZ3dCMlhDUXBKK0VSR3g4akk2K3JQOGRIaTVQVGh1VVR1b2UrWUFyOEE0WFBIRit3UlNraU9HK29qemdjd3gxYkFpNEhlekEvSXE2cXN5S3RNby9SbU4vU3dIRlpOYVNyM1JNRHAwMHdNVERGNEtBNW1FTEFJeUZCTDRPS2VWc0Q0di81VlU2ODFicjNKdmd6T0p4MGV6bTZyOWErNmc3ZnNUTjNPbUVlNTNCb0k1R3h1OUNIc0tERHNsdGNLRXpuOWRDKzZPaEhmc3dROE9oMlpjbENyYVg5ZndYTU1UMFpvTVBaSTBFWm9jTjA3QUdzRFJqeW4vRzlpMFVHWTRYL3plMklUWWVHUDQxNjFES2hxVmlHOGl2NzlHRWxBMmhBZ01CQUFFQ2dnRUFIWW9xdUVXVXF5Y09VWU1hT0E1SFMxWmdaT2src20zTi9TOWhDWW0zNEY2Z0tMU1QvWDNaRVNkbjljOHVtYmtRZXF4MVVhbkJtblRVWi8wNWFmeDVSbTYzQUR0cmJqaUhNbnlTZzJJWE1lYzFHdEtlOVp6UFl6cjUraS9kb0ZhbG0xTTFybXBEOHUvWFkwcStibjJqN3VIa3lqeVM4VldudDY1SE94R255UGxlVGsybzhXdFdDUVY3aGJMMStJeWpDWFB0Mm5Tc2NsVmtnUzBiYzduSDFaR2sxenR6MHZsUkNIS2ZpNDJoSjFDTjJmYXFGZUV4L1Jvb3M2R3pOOGVLeGpPOEhhcEFCem11N0QzMWIxWmhUSE1YVnFId0Zjeit2NHAzV3Z0TDF3NFlHdEMyd0pTaFNlVG5IeUNPRnNieVZUQkJNbFQxWTRYNisxNDk2Wk1rWFFLQmdRQ1lwcWUyT2Q3aGZDcGNzSGp5TnlNWTRGbFcwQjdRYVRXaHpxOSt4QjRrTzBjM1l0VW9IWEZOY3Z3dzVIR25CZ3BkYlZKY2JQZTc5OGdUb3lmY3Q3MnRMQkJtL3ZvQnAzYlpNaEhMREZNRS9LMHRLajFBUGw0bWYxUDlsaS9mcWlKOU5mamlyK3ZLMVFmY3haSGhSMlNaMEtmRzBwNDlqYUJKNlpLT3JvRE5Od0tCZ1FDUHc3T2Nvckh0N2hCMWwxVlBmUlFqVys0eXpHNTNLV0oxaDdEbXI0cUI0MjM0d252aFkwT0puUGRTU01IWm1LbnM5cFEzY2RFODhyT1g1SDcyaWphcFY0QzU1MnJ6cEVKWXBMZHp3emExRUgwV1dVOWFZVExOSy9iVzBxUUIydmt5Uk9TbXIzVGY3SjQ0YTkxamJKOVJQMkk3ZTU1Y3ZPd09PanpxbVdTbjV3S0JnUUNTdnhOWEVNYjhpVHJJSkRZQTA1Ui80NXkrNGcvZFZtYmlpQ2taZWp0bnBUelBOOG1tYUxkMU51Yk5zYTY0WEF3MnlGTjIycUpGSnV4R1JJQ2JwRjlKVEtUdi9vb2tjUExGMVdaWmhoMkJHODczTGpYM3ZuMFFFVE9UQW9BL1NmVWgzWExIcVVySmtJV2diS1hTcGFsR1hOb05Qb2cwc0NPNUtqdGp3c203ZlFLQmdEdFhFUTBuVG9BaUVxTW0rdXliZVRON0g1L1NLQXFCaDRWeG84QWtWdXgwSHBGZVhWblQ2aTJrSDZYVUtFZVRyeGdEVTN4ck8yMkgxRDl1N2tUL0diN2VRbUQ1dDNpbnBVY0hmajJISjA2blpxcFI1T0l1V3BTN2YrQitBM3BNa3kxL3FFMXhBTEhvN2dubDQvVEZBaUc4SXVUZ2lxWkd5THk2cHloQ2RueWpBb0dBQ3F0UUtzb1dIYUpYWmtoczhGbmFFcmxmS2RZdXdpQk1HcmZvUzg4b2w4TEQ5cnF6WW9ZMnRXSFh5NlZMYnQ4dTdabjFFTG1qTEpDbC8rT2dQM3QrU0U5bFI5RmpmMHhJTWkxRENrRm02WkVqaTAzSFAwZXZuSWFQMlp5Zmw3SFZoVlZiWnBsY0dLZ3JjZUN0OXdFOW9SMXFCTzRNQk5wU1NEYnBLQ0EvK0g0PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0VkZkxKbFNNMVNqT1B4Vlc0djEzTGV0MWZiS3R1T1N3SXVxNkxVbjJ6dG02aDcxcG9ZUnpmNm9TZis3TjExenJKdVZDMXlWSUNIbzlSSmhnWVFwV0FOa05yV2I3SnlBZTU1SER5ZnpEYTBZdHBnNE1laThWY0hsdU50OUlOMEU5ZDFXMjZlSmhZQlREOUFMOEozWHV5aEhMeGNBM1dnSE4vZXhQeElQRkh2VkFoVUFtU0JLWWR0WklHRjNqNkZYbFh5d25ObENCWDBDZ1lBQlVIa1Fvd3BkZGUzcUMreDYyMlgrVS8veC9JUVoyWEIxckhscU9BMHp3c0l2U1FxWTBxOHUyTXRIaVJRRDJRSnR1WStCeW9TVkI1Und1czBxamJ0QmNRNHRUZG84VUxySDI4cGxMSE11eGlqUTVaTmZlem9lRGtDNjVudkxYSXNTcnZ5SjdhVnR3LzVSSDEwK0EwWTBHTVBlT3RuTlNYYTlLQ0xldFBVeU5BS0JnQnVkOEpiSHUrS2tuYVRDb2c5WTVzRG5GOXgvUklDRk1JNlNrSzNJT1JwblB0WDlEN2JoMWlDWUl3bFQySENDbFFjUUdGYzlnM2lzQSs0c21uRU9jQ0RpeUFkdldNT3FJRGdKL0ZqUzBSYkY0VGhhTkdxcEZueFNyeENrV01vMnE5aWU4WnA4Q1dGeDZiOE9ZbUZyUkpTM3orR0k3NlJIcTRVMUZLempQdVpFQWhRWld6SU9pMjYyNFNlQ3JhcTJoQ2N6VFVsd3JRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUN4Zms5bzYzamlCRmxLU25FMm5xSjhOWXVxUWRVNUxUQTVESU12K3p5d29BY0dCU3VCQkFBS29VUURRZ0FFaXhVbzc4S0xqZFM0bTZIK1ZQSGF3NzVMeVltcE4vL3duYkQxbGlqZUR1aWl4QWd1WnNmUnlGSjc5bzNtbVBmQjh4Slp0Vjdwd3o5T1lDeWZpQXJOcXc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVRQzBMYWpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNalF5V2hjTk16SXdOREk1TWpFeE1qUXlXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0VkZkxKbFNNMVNqT1B4Vlc0djEzTGV0MWZiS3R1T1N3SXVxNkxVbjJ6dG02aDcxcG9ZUnpmNm9TZis3TjExenJKdVZDMXlWSUNIbzlSSmhnWVFwV0FOa05yV2I3SnlBZTU1SER5ZnpEYTBZdHBnNE1laThWY0hsdU50OUlOMEU5ZDFXMjZlSmhZQlREOUFMOEozWHV5aEhMeGNBM1dnSE4vZXhQeElQRkh2VkFoVUFtU0JLWWR0WklHRjNqNkZYbFh5d25ObENCWDBDZ1lBQlVIa1Fvd3BkZGUzcUMreDYyMlgrVS8veC9JUVoyWEIxckhscU9BMHp3c0l2U1FxWTBxOHUyTXRIaVJRRDJRSnR1WStCeW9TVkI1Und1czBxamJ0QmNRNHRUZG84VUxySDI4cGxMSE11eGlqUTVaTmZlem9lRGtDNjVudkxYSXNTcnZ5SjdhVnR3LzVSSDEwK0EwWTBHTVBlT3RuTlNYYTlLQ0xldFBVeU5BT0JoQUFDZ1lBYm5mQ1d4N3ZpcEoya3dxSVBXT2JBNXhmY2YwU0FoVENPa3BDdHlEa2FaejdWL1ErMjRkWWdtQ01KVTlod2dwVUhFQmhYUFlONHJBUHVMSnB4RG5BZzRzZ0hiMWpEcWlBNENmeFkwdEVXeGVFNFdqUnFxUlo4VXE4UXBGaktOcXZZbnZHYWZBbGhjZW0vRG1KaGEwU1V0OC9oaU8ra1I2dUZOUlNzNHo3bVJEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQk1KRldueXpPejNqWFJseEt3U2ZNQnlaOWo2QWhRdHRyVllxZTZHbkNtZWdidTk5eThxRWo5LzRRPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlN6Q0JzS0FEQWdFQ0FnUWRZak9tTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNalF5V2hjTk16SXdOREk1TWpFeE1qUXlXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTTEZTanZ3b3VOMUxpYm9mNVU4ZHJEdmt2SmlhazMvL0Nkc1BXV0tONE82S0xFQ0M1bXg5SElVbnYyamVhWTk4SHpFbG0xWHVuRFAwNWdMSitJQ3Myck1Bd0dDQ3FHU000OUJBTUNCUUFEZ1ljQUFEQ0JnZ0lnQUsyblpXZHZnbW01di9MRFhQTFN6YXBPZ253UG9JMjJVeEdxVm0zUkNEc0NYamdhTzYyV1llL3Fla3dFVzVnQ3pUOTdHT243K0dmOGcwVStkc01CYVFZUVVUNUI0dW1RZkJqV3hYZ2UxWTdWZVBrbm5pNUNxUTZrczZja08yUVJ4RFhBMmRWUFI4ZzZlaFNEeDM1eHIxak43T0JFdjRZV21yK0t2eER0T0hVPQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVQRVp1WmpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEV5TkRKYUZ3MHpNakEwTWpreU1URXlOREphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCVnVjbTZkL2ZCZDd4YWVpRnVlWDNRUDh1MTRhTktjdTIvdlppeHgzTVlVa0o5T2JKVHFGV0IxZ3dCMlhDUXBKK0VSR3g4akk2K3JQOGRIaTVQVGh1VVR1b2UrWUFyOEE0WFBIRit3UlNraU9HK29qemdjd3gxYkFpNEhlekEvSXE2cXN5S3RNby9SbU4vU3dIRlpOYVNyM1JNRHAwMHdNVERGNEtBNW1FTEFJeUZCTDRPS2VWc0Q0di81VlU2ODFicjNKdmd6T0p4MGV6bTZyOWErNmc3ZnNUTjNPbUVlNTNCb0k1R3h1OUNIc0tERHNsdGNLRXpuOWRDKzZPaEhmc3dROE9oMlpjbENyYVg5ZndYTU1UMFpvTVBaSTBFWm9jTjA3QUdzRFJqeW4vRzlpMFVHWTRYL3plMklUWWVHUDQxNjFES2hxVmlHOGl2NzlHRWxBMmhBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFELzdwL2hOcmR5NDlEOEZsenczWDFoSXJINVZOQ09aODB4eG5Rc1NjZXFDbmFWMmZHWnQ1QnZyZENCeFhROFZoZGJBTDVRaVpDUkhyRGVmaE50Tkhld1p1cE1UN3d3b3VnajFHUDF1NERvbnlmUjViNDJPRGF3VVRGazFrdEVvY2FaQStkZFhMSVRWSytWc0FHcDFlQ083bFUxVC9XWjkyT085QW91WGlrY1AzTnNHM0dzWmo1a3ltdFBseS9TQWpydkwxMlk5d0tBZHh2bEo1M3hvMkp6ektwNysyeWU5cmNuU0ZLVXZXZUJ6V0c5VUNQS1N5YWNTM2VZK1BCaXZUQktMbkJ3bVFsc2tFUjVUSUN2SmV6QnYzQURydXpTbUh6dUVmZTFKenBOSCtjRUtCL28rR3pXNnBPNFg2eDY4Q0FPeVVHckQwZlZ5SzN4MHpjbUlCNlk9
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.255
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
    logging file debug ../binTmp/zzz4r2-log.run
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
    dialer1 is up
     description:
     state changed 3 times, last at 2022-05-02 21:12:56, 00:00:00 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
     ipv4 address=2.2.2.69/25, mask=255.255.255.128, ifcid=154123256
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

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
    logging file debug ../binTmp/zzz52r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCUVBnSFpHQ040MWhOOUFwMUNiNE5lek93VERFN094alF0VHkwQWZVOUgvZzZvcU5rZWlRNHpENC9YZjlpTGdVRFM0bFVQQTc5NjVoN3FKMXdDWHVMUzcvMThvak9mdThXemlCMm1yMmg3V2dNRFRwMjZPM2Q3WFF3cHNPeHZac3haMHZpTFlzRTE2b3d1NGJxeXRZZ2h5cFdrNVRiS3FXc1BZOTdvcmtCdFNhZ3MvVDc2UUpGcFVaNGdWMnpDc1FxcURyT01GSUtMaFNHOVV6Q2N3V3d4enR6djI1ZGZpajN6azVuNVlDYjkvNGlPOG1YbHF0TDNNTmlpVS9jdzNodW8rNEh0WmllL21tWk0ra0VtWG1QeFN4eEZ1b0VKQ3ZEYUdUc2k2Y1hsYUhtSUR3TUpnYUl4QmJLLzhCNm01OGpjMXpTYUNjMDA5QkVDWjM0SmpveTNBZ01CQUFFQ2dnRUFTZ1I0cGUzN1FvcU9YWUVjMk55T1hOTkFiRzJ0QUZXYWFiVWdPTlJlWG5VK3hsdENORVdPb0pFWlNWcTN3QytSUVRYZjZrSzF6VU1hZnptaFNOcUg5clhEcU1UaVE5VHNrQ2ZkMmhUeGx0ODM2a1FKZ0hFOFRNSk81dUk1cHFVM21SL2Zmb3V3MS9Bc01VNnRiZzIvcmhQMko2Mzc5Y09EYXlYZng5aDh1NUh1c2hjQVNabzVNa244Zm40SStDZDVIZm9PS0Zaeno0U1ZHYW9Db0FMdUxIK1FsZDhRSVpaeXZudWlmb1BHMk55dlFSb092S2REMEpCYnRWUzlGYWx6aXc0NXo3cGhZNmpKTG9kZDFWUnBFTXg4WkUrY2RYUVdYOU5KNDVEa3RNbW5YQjdCUjVlVFp3MWYzTWpYenViUFVaQzEzL3M4WUNROU9Ockc1bUtPY1FLQmdRQ1BaY3JNZmdIaWgrMjJRbzdLQVFSSFZOM3puMnEzTy93VDRFMFAzRUNmVm5SRzhIbTF1V2oyL0d5N0ZqUjlqeUtFMlh5eW14VEtqYVBqZ20ybm5oUVZBOG04a0ppeUp5NlZjUXAycWhoR283L05XYkgyK3QxMStHaDhTZ1c5ZXIxMmxmWi9wMFV1OHM4SmlkTEhoVTZ3di9jRy8xUTRBdkI3RzZWU2VZcm1xUUtCZ1FDUFFJZmptSUExR004V05vcHE3TzlEZGNSbmkzTHpOTFBpcmwvRE12R0NsQmZ3b0czbEw3ZU5heGllK2d1VUNXT3JONklKelp1RjlZTENYRU5wdnhDYTBLczBvMFYxR0hUWE5iZm1ZWE5HbTNPbDh6ZzVFUXJQc0xFekoxczRzSFoxVkhuSE9lOW1ZUzBWSEZrRmlja3NpaFJ6Q0pDMnlyWFRtS1V5aW1mVVh3S0JnSHBGcDlrYWtPemlUdFdjaHpqRUNTdnh0NWZtbFE1TS9iTE5EYWk2ZS9maHRpQlBLTmpGa2pVWUpIYWFob09ScXpOd1o1MjhFc3hzWGhTK3dGV3V1eHo0TCtxenVTQWZ2Tjc4bHBsOGpGcWZnZ3JOc3F3UVdRb2dtS2R5VHRhMGRCMUwzZllYWVN5WktlVE9Pb2FhcXZDWG4wRytNY2ZZNmNsdlYxYXVBTHlSQW9HQU5mWVoraXJsQ0p0S3p0Ukd1ZFo4bm8zTEtUSUhZQVBYU3lsaVcxWmlVVXpWNDhlYS9mMUdpRmZ5VTFoZmFpbExTU0RRd2g2WVdoTE1hY2gxZ0d6L3BVRzdiRDJnbVdaWUJRVndPN0V6eWtJZWcwR21TU0RaVUxqL1Z3U1pRVFovdU56VWJxNnROb1NlaGRoQzFHbzl4TEJTMmE0OVRRMzVCamIyNjUzbFZNTUNnWUExZG1aQklhVExKcjMwVGMrODE3ZHNZZ04xdUlvbzRlakpreGo5aXJJVE0yZ09VSVRIeUxTR1FMNHgrOHRYbiszdlRQVmhkNS9mU3F1MDBOaUJxV1gvSStEeGVkeEdNcURnV1plQjh4cUhoeXNGa3h3elVxdTFuV3VjTi96cmdFU2hJYmFBMmJLOGEvbjVGdGt0RVNkZ0QrcXVJaDlSMEFUVG5sTFNuYXhSYXc9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0JDd282aGhVaHJKVnVIeUVGWFlTUjUrZGozQ3BWNGV1Z1lyVDdwN1FvY0dveGNWNm5EYTRrZ1dQa1BmUWdWejBXc2d2QWZ4SDdqK3NWeHczV1B3V2QyTXBTTUE4K3Rpa3JycndVT3dCOWQvWHp5UHQzbGN0RHFsNTlhZDFwTUlYZGd3cEoxU2IvT01BRThHaTQ4RzFLRHo4V3FicElCMG96MFkzVXpuN1A4VEFoVUExaU9FUnpKb1VwMTJrWlRvakxEWHhzVHdXczBDZ1lBUW40akpYdG9PNWdjSEgyamVVUkdDYUp0WVVBTlBxdXVmZlhrL3ZNTWpORGVqWmIwRkxSUTVMV2w0WU95SDZERWZRYTFtUWVTNTJJaW4xdVNBRTRLek5lM3BxcmNlOWp2WTZ2Yk8wUDhFcnBaL1F0ZklIU3lHaFY1L1dVc2lZZFYxaStIUTNoZ0pZRjhXb0toOG92czd4by9wS1FEM2s2eEpTejJhSXJTNWF3S0JnQW84cEt4N3VlcThWOXU4VXFEMWQxOGZvUXFBYTM0WHVjVk50djUwWnlmRW5YZElFYThkRUlVVUVQT1BVNTh2RW5LU1ZwQTlwQUtJWVBnWE5JbEZUaS9aUW0rQVR3c3dVM0hLelU4QzR2SFdSa3VSN0FCV1JlamtkN2RmNUdOYXJ5cGJkUm5VYzRUTlN2TFJHQkZFSDdMS0dSdytucFM5RS9IOGFUODd5eTJ0QWhVQXhDVXNXNnhxaEJnY2k0eUdHZU85WWpuTU9kVT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMjQwbVZVY2diRThlaUsxOGRHWHdoYU9qMEkxSDBnU0g5Si85WndrU2JHZ0J3WUZLNEVFQUFxaFJBTkNBQVQyTU5oT1ZSOGZrN3hNM1NJSHNmK2M4OXloTXJObmZLcEFEMUtxQXFQemNuR0c0ODRaZG9OcFEwUVAyNUhzck1pYzRJQ1V3RXNLREJqNXZZOGVkRTRU
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVacEMyR0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNREU1V2hjTk16SXdNakF6TVRVek1ERTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0JDd282aGhVaHJKVnVIeUVGWFlTUjUrZGozQ3BWNGV1Z1lyVDdwN1FvY0dveGNWNm5EYTRrZ1dQa1BmUWdWejBXc2d2QWZ4SDdqK3NWeHczV1B3V2QyTXBTTUE4K3Rpa3JycndVT3dCOWQvWHp5UHQzbGN0RHFsNTlhZDFwTUlYZGd3cEoxU2IvT01BRThHaTQ4RzFLRHo4V3FicElCMG96MFkzVXpuN1A4VEFoVUExaU9FUnpKb1VwMTJrWlRvakxEWHhzVHdXczBDZ1lBUW40akpYdG9PNWdjSEgyamVVUkdDYUp0WVVBTlBxdXVmZlhrL3ZNTWpORGVqWmIwRkxSUTVMV2w0WU95SDZERWZRYTFtUWVTNTJJaW4xdVNBRTRLek5lM3BxcmNlOWp2WTZ2Yk8wUDhFcnBaL1F0ZklIU3lHaFY1L1dVc2lZZFYxaStIUTNoZ0pZRjhXb0toOG92czd4by9wS1FEM2s2eEpTejJhSXJTNWF3T0JoQUFDZ1lBS1BLU3NlN25xdkZmYnZGS2c5WGRmSDZFS2dHdCtGN25GVGJiK2RHY254SjEzU0JHdkhSQ0ZGQkR6ajFPZkx4SnlrbGFRUGFRQ2lHRDRGelNKUlU0djJVSnZnRThMTUZOeHlzMVBBdUx4MWtaTGtld0FWa1hvNUhlM1grUmpXcThxVzNVWjFIT0V6VXJ5MFJnUlJCK3l5aGtjUHA2VXZSUHgvR2svTzhzdHJUQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGSER1eklTQk1Wd3U0RkpWNGZDVjlnL044d3VUQWhVQXhQZGpsMHhScGtOV2p2dG5uV1JpK05CRlE1az0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUTV3Y2VnTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNREU1V2hjTk16SXdNakF6TVRVek1ERTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUMk1OaE9WUjhmazd4TTNTSUhzZitjODl5aE1yTm5mS3BBRDFLcUFxUHpjbkdHNDg0WmRvTnBRMFFQMjVIc3JNaWM0SUNVd0VzS0RCajV2WThlZEU0VE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBkWlVhYTdGSjJLR3hVSEFoaTZvOWQwMmFwTHNucThFOVpUTURlTmJCRjRBbDg1M2w0SmZMNm4wZU1DWHRkUjVNWVJyWDdpV3Nnb0FGK0VSZFU0cTJKa1JHc21GUnRuK2w0V0IwNjdtOXp2T25NaUk1VFBQdFF0bm5BK1VqeFhRS3VrQjJCR0dwQnlWTXBwdDNLeUxhTDJHUk1MMXNwbmxNQ3F2VDB3d2tMRHp3PT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVQRVJ4V2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVE13TVRsYUZ3MHpNakF5TURNeE5UTXdNVGxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCUVBnSFpHQ040MWhOOUFwMUNiNE5lek93VERFN094alF0VHkwQWZVOUgvZzZvcU5rZWlRNHpENC9YZjlpTGdVRFM0bFVQQTc5NjVoN3FKMXdDWHVMUzcvMThvak9mdThXemlCMm1yMmg3V2dNRFRwMjZPM2Q3WFF3cHNPeHZac3haMHZpTFlzRTE2b3d1NGJxeXRZZ2h5cFdrNVRiS3FXc1BZOTdvcmtCdFNhZ3MvVDc2UUpGcFVaNGdWMnpDc1FxcURyT01GSUtMaFNHOVV6Q2N3V3d4enR6djI1ZGZpajN6azVuNVlDYjkvNGlPOG1YbHF0TDNNTmlpVS9jdzNodW8rNEh0WmllL21tWk0ra0VtWG1QeFN4eEZ1b0VKQ3ZEYUdUc2k2Y1hsYUhtSUR3TUpnYUl4QmJLLzhCNm01OGpjMXpTYUNjMDA5QkVDWjM0SmpveTNBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFBdWs5ejJ5R20vYmJxbks4NHluTzA4eml5QTArblRsbE85WnVDRFJLMjJhaGdxZ0dhbGhIQm1RdUhiNk5mYjkwdER1OWxvWGo0UTljMDh4ZVRvRWU4aEJZSFVzNEM4bUZLdnRVd2tIa0pham54K0tNSGc1Z2NEZmZTZkVqbSsrR0hxVEtkRCtrVW5Qd3hoN3dPZVcwbEFwVE5NQVVHVkM4UVdVUDd0ZXB3K25EYkk1d3VMditQTHJWMDRZMXFnSkhFNmhCeEk5TjBMYjRnWkV1QTJsbE1tUWxqTXhnemN6ekphaWdHdjJoZWRGeGphYlRBUjc5a0JSMnJoQ0wxWklROG13RkJLNmFvdWtlemNobGliRWgwV0E2eGU3dVhPK1pQWnlKN1Z0UFNUaWJ5R1krWGRDWHl3dzhWU0IzQjRIaldNb3I3enRoZzZTMVJoUXd3SFRod1U9
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
    logging file debug ../binTmp/zzz52r2-log.run
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
     ip4 address=2.2.2.95/25, netmask=255.255.255.128, ifcid=1036262254
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

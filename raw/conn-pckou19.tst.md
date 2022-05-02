# Example: ppp with packet over tls
    
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
    logging file debug ../binTmp/zzz43r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQWtWeUtUaEZnQ1lrOHdzMENVL2ROV2hWaHZDbEE0cm9qNGRHQkRtSENoUWJCZDVMcVhNK3JTZW1pR0xReGszNTArMkdmUnpuKzNDckNQRHJTUFRCT2pDTW9VNVdRdFVDWWwxeXNKK20wb3MwNTRuRU9LWHp6UlZZUTJjQmNsR0wzYUJkQ251allVSjh2czhwek0zeDRwSnFEUlVkMFlIVFNtcUZ0ZDZYc2ZXeEpDRUNJRVgrS2xMUkhVbG9pbE8xcGN6ZXFXTUVLV3hIZGhaVTFpWS83MUdDZVRJNjYwTnZYUVZPSUd4UE1GWjdiN2tZTEVSNDIwSkxJMVhlUG4vblo4N3ZzUHdGdmR1Q3c4OGFtejJYcUkyWnIrWWpiNTJicDlTMWd0a3hRSVJ3RGltYmFxUEx6M3U3a3NnaFVIQ2dYUXFqTVlIVnRUcWlLa0FQMUUxcHdCUUlEQVFBQkFvSUJBRlVpemg1TEx1Um03SjlyVXlHNmhpTnN3b0ZoNkE3aTFvRThJMG81RjZTeUFEMzRYaXRkdGdUa1FYd1dqYkxGTGQ3Tm5td3BHNHYzdnl0bmlCc3VYOUxVQkpwdnp3RlpoQVdpMFhITy8yMGFwZnhxR3RGUnpXbWVydC9hT2w3dVY5a3ZSbVdzR29XZHRtS25BREgzaFBGalRkOFZxcU9UeUlXb1ptVGRXVlZiWkNjK3J0ZmFpMEFpR2dxMHFYYUt1blJXYmx4V0FralQwaDc2YmVzaTFwNTdtbEwrczBqMFlWL1Q2TUhOWlExWGxZOGpQc3FsQ3E4M2xlWkhHTld3anNpaktuby8zK1g5ZGxPRGsrNERCaThJczRISzF2NGtNakdkYzNRbFpzMmVFSnFEOTZtUEtuMzh1ME5uQVdZYncrL1dhQlptRW9ZUjFRSHd2Yno5U2dFQ2dZRUF6czViQnFlcFZpd0tiR2xpRHRVRlNwQm11c3kzR3Vlb1RBWUlTUmd3ekZYOE5JTnNnMkJ1am9lZVJOeGdYT2t6Vkw5dVNRRGIzblkvRS9FUDVzYnhONWZ3QjBYK3YzTGswVXczMEJna2d5VExSREMwbk5YMDJ0dllCQmhqY2VGYy9XelVXdi9mdFFMYlZ3cU9EUHhwaFlhdmVEZyt0bjZWRmFHUnp6K0JNWDBDZ1lFQXMvQjEyRmJpNGZUbVN0OE50aklxbUZSWjAvOUI5OGcwL2xNdWdVU01VQWdrT0pub093UXJzYzdOTnlZQ2RpVVVVMkljdFE4UFRUbjZka1JidHIzZDBDN2Jxcm5FdWppQTNEdTJzdlQrcmd6cHJZZS9EeGhPb084dlZyeXdxa0t6bmg4a2R3aUpQYlJ3T1Q2c0ZIU1pRcFY5Szd3Z3JBK0tRbE0vNDVNMi95a0NnWUJ5YzhYd3d1MTJvVjBMYnE4MElqU1JkYVZGRUhMdDB2TlRUNnRhT0tjWkR5VkxNc2psVklNYkluYzNDUGZUczhRU3pQY09OQWw2N3RvdUFTV1p4TlJPdmltNi9NUGwxSUpLU3ZKQW1udnFrSHhtT3NaYVhoYnE0T3lHSjdFeG4xWEZjMnQ3Q1UwWGNvTk5ncXZuQi9LbVVVbmZNTkdVVWkzVUVOMFBZOGZ1U1FLQmdHUDVLY0IxSmNGZEM4WjFmMnpIR3B0ZjRqakREYWZaZUhnRlIwVlRESkk2czhVdTNiUk1jT3B0ZDk4NEl3MzVNLzNQK1JzdnJ0UzliY2JmM0FVQUlJbFdQMzN2a0xuV1F1SVoyenc2bW5XaGZ3T0c5RVF5d1J6eFIxL3Rua282blFreFRGVkdUTm9Yc25KYnU4ZnhzR1VxSVUxM1RML01Nb2ovTC9RRkN2MWhBb0dBVEYzUW8yU1BBTjdQQ0tNd2JUOWtFZDg4T3d0MGFqL1IrZmYwM3FnVlRZN3kzTlVORGtqZVZ3U0NsbU8yQlhod2dSVGZZa0d1OW9JT3oxUzIwdnBjOEQrR1Z0NXdvOUw2VWhIU1NwMGNBajdWZVhlLzBWcEg5eTBVUFFIU2tHOWpxRzNoLzl3Qk9IWExwREtGQnpUNHRBc3BoSlgzZU03d1lxTUdUTWp6SlFVPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0hIUGp6bWx4YjZMd1ROalpxM2hwNEk1bjVtU2FGek9wUzFwbnBsU0FWTG4rcVdLbEo2anQ3ME15UUhIb09hOEFnUXptakhRS2dRb2U0R05na2ltMjJKM1NDYlZaSlZTNk1DeU1xSU9ua2hYWTQrZjlzenJkL21nc1NlSWpqVlNKSDdNWm5hTVlhS1dRazY2TDNpbFp0cmk0dkNVa29qeUdiZ3lRZWpTdmx1bEFoVUFuek4xUCt0b1I1YW5CNnVwQUEwZjR1a0dsRWtDZ1lCRm9uZjRsTHpHdk9lSGJnYlY5NWlBaVBrSGJmajNvQmxCb052SVkzMFZINzFFVndZeDB5TnZ3Rnk4UlkrSE1GdUhsSkx3MThEbHVpYkFhZFRPRCtPUVU0QTd4Zkg2NktRd3NUbW5LbHN5cG1hYzFIVVQwWHFaNzNUWG1CbmFQL1JqTkE5M0N4RjRkZ0V4WGRyQ2FMUWpSQVlPanY5ZVVvNk0xL0NGUUlNOEtBS0JnQUlBRFdEYWdWbkpNQU1qOVhCT3hPUVBpdEQxYWxBSDdDUlBpMDN6RzVPMElxUXFQeXFvM0xkb0VqQjVhSUpEbE9TaDkwL2ptZ05WQWptdW5XVVFVOUZPYjJ5ek5qRSttdjdHejZHcDkreUp6cHVhT1loWFBwU0dVUTBKelhScG51Ky9vbkxPZC96MDU2cXk5YWd6RUl5SXdFSWdMNE5LR0RBK2VNNUFlRGo1QWhSMVhXZzFldzZacGxUUkp0cWJhc2JaMURNT0Z3PT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMlNDNzNpQ0J0aDNhUXpzV3JjYTE4T1Rtem5vV3dYUjVwcDRJeGVNTk5HZ0J3WUZLNEVFQUFxaFJBTkNBQVFvRktiTi9PcDZ1TTJ3Y3dBZzcwR21wZldEWXFnMTRjYk5sZkorcUYvendHU29neXV1RkJSR2Fyb01qWEhMNjNVK2s2TXJCNW90N29LMUJKSnArcnZJ
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVOQmdXYlRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNalV5V2hjTk16SXdOREk1TWpFeE1qVXlXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0hIUGp6bWx4YjZMd1ROalpxM2hwNEk1bjVtU2FGek9wUzFwbnBsU0FWTG4rcVdLbEo2anQ3ME15UUhIb09hOEFnUXptakhRS2dRb2U0R05na2ltMjJKM1NDYlZaSlZTNk1DeU1xSU9ua2hYWTQrZjlzenJkL21nc1NlSWpqVlNKSDdNWm5hTVlhS1dRazY2TDNpbFp0cmk0dkNVa29qeUdiZ3lRZWpTdmx1bEFoVUFuek4xUCt0b1I1YW5CNnVwQUEwZjR1a0dsRWtDZ1lCRm9uZjRsTHpHdk9lSGJnYlY5NWlBaVBrSGJmajNvQmxCb052SVkzMFZINzFFVndZeDB5TnZ3Rnk4UlkrSE1GdUhsSkx3MThEbHVpYkFhZFRPRCtPUVU0QTd4Zkg2NktRd3NUbW5LbHN5cG1hYzFIVVQwWHFaNzNUWG1CbmFQL1JqTkE5M0N4RjRkZ0V4WGRyQ2FMUWpSQVlPanY5ZVVvNk0xL0NGUUlNOEtBT0JoQUFDZ1lBQ0FBMWcyb0ZaeVRBREkvVndUc1RrRDRyUTlXcFFCK3drVDR0Tjh4dVR0Q0trS2o4cXFOeTNhQkl3ZVdpQ1E1VGtvZmRQNDVvRFZRSTVycDFsRUZQUlRtOXNzell4UHByK3hzK2hxZmZzaWM2Ym1qbUlWejZVaGxFTkNjMTBhWjd2djZKeXpuZjg5T2Vxc3ZXb014Q01pTUJDSUMrRFNoZ3dQbmpPUUhnNCtUQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNWZlVoZnhxb1FmMUtnRHk4ZDVJRHdzVE5IeWdJVUgwQlppTE9EMVdydDh0cTM0aG02ZTRDNlpLND0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUndEa29qTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNalV5V2hjTk16SXdOREk1TWpFeE1qVXlXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRb0ZLYk4vT3A2dU0yd2N3QWc3MEdtcGZXRFlxZzE0Y2JObGZKK3FGL3p3R1NvZ3l1dUZCUkdhcm9NalhITDYzVStrNk1yQjVvdDdvSzFCSkpwK3J2SU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtHYXN4c3NTdUxNVFV4NFZ3T3dIZDUyeGV4SDRJbStaQ1duc0hXSmxnWDdBbDhsZWNnVHAwSDJNRnYrNlJoMlNlRW9xRnA4WnVHWGR5QmlnTE53SVdDTkFMbjF3dHIrNWVlMUlIN0dyOGs4cE1lTXVLQ1hXS1RCTjBlWk44c3BXZ28rMVpkYXF0OUdwejJPS2JEY01vaGRKSzl1amdKcWd1M3lycUVza1ZxSjNBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVjbytMb0RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEV5TlRKYUZ3MHpNakEwTWpreU1URXlOVEphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWtWeUtUaEZnQ1lrOHdzMENVL2ROV2hWaHZDbEE0cm9qNGRHQkRtSENoUWJCZDVMcVhNK3JTZW1pR0xReGszNTArMkdmUnpuKzNDckNQRHJTUFRCT2pDTW9VNVdRdFVDWWwxeXNKK20wb3MwNTRuRU9LWHp6UlZZUTJjQmNsR0wzYUJkQ251allVSjh2czhwek0zeDRwSnFEUlVkMFlIVFNtcUZ0ZDZYc2ZXeEpDRUNJRVgrS2xMUkhVbG9pbE8xcGN6ZXFXTUVLV3hIZGhaVTFpWS83MUdDZVRJNjYwTnZYUVZPSUd4UE1GWjdiN2tZTEVSNDIwSkxJMVhlUG4vblo4N3ZzUHdGdmR1Q3c4OGFtejJYcUkyWnIrWWpiNTJicDlTMWd0a3hRSVJ3RGltYmFxUEx6M3U3a3NnaFVIQ2dYUXFqTVlIVnRUcWlLa0FQMUUxcHdCUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQWxLRW1SdjFiSEh0RnFNNjI3NzNvWTh5dllIZ3RSSFRpdHFGZUlhSGNTQXFOdmhXaGRQeFRVL21WOC9iTWZOci9RM2l4SWlBOEJtOGJ6blNXdHVXUFFQdjN4a0Z2aFZGZEwyZGdKc3ZKZ3NJSmVROTRRT29PckZyeEE0MTBkOTdjNHhCQTNkNmNsMTJQWUtaazdSczd6MnhHdHp5c2Qxc0NnejJNdlhyR1RSRmJvaEorUmtPSFBzTDF0ODAxYVBjT1NXSDBhRGRHUTNzamhFcTVETTdWc2M1N1I5clA4RVdJWE45L3c4VnlEdFROYVJQRlVRbDlKdjZoRXpEUllrRkZBMm5OSi9ScUFZcFk3Y3hIM3N2dU5TbUkrczIzU2VQem51eU1lVEs5NXlWN01KbEw5VnhSaHNlWkdLN0dmZkxpdmZNYUpWZHRXYTJLYVNQcFY1TXRy
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
    interface serial1
     encapsulation hdlc
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
    server pckotcp pou
     security protocol tls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     clone dialer1
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
    logging file debug ../binTmp/zzz43r2-log.run
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
    interface serial1
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     security tls
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target 1.1.1.1
     vcid 2554
     protocol pckotcp
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

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
    logging file debug ../binTmp/zzz25r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCNUVkUXdEbHcyeWtqYTFONjZWNjRGOEplWWtVazYzWXlWSjJEd3Z0UU93V1FodHk3K3hHaUFjaXZkbldiNllRRlZiYU9IbVIrSStySVBaanM3c09CM2JMWFUyaDhPMGlXVlBFa1BIRDBYTldJT0puZGtienVoNmg4MmJ2T3I4ZkI5ZzIwOHArVW1yUVh6MVIybzlGT0o5UWZzaWFxa1pNSVAvUkdJY1V4bDRFSjJQSTVHZ21wa3hZZXpQWWhRTXFDY2pQb2JQZVNuSmJOd3FERUx3TE80YmZmbWJ3YnpOK3REcXQxczNGcWdyOTBTTFJjYVZzZ0NhTkV1Ylh5Zzh3TThGOGJvdmRueldRYW4yaDloT3RsZkVMOHJLYytONlFENU5EaXJaMUJFanRiOUJ4dnJUbGpFUjNDNzhHMVBoMHJRenlndExKVUs2Snp2NFduNkx3aFJBZ01CQUFFQ2dnRUFNZXRHQUNLTHB4TzFBbld1K0VwYXVKeEJCV2t5TnBGTys5am13WjBOTnFCS3R4UWV6bkVSWFpTMXZZUy9CeEdrU1NNUndFRkVuV2d3cnVUS0c0eU1vUEV6Ny9XWHhMYWxSR2s4L252NFBHK0laS2s3cFMrditNemQzY1hWdHRuay9QdUp1TzdKTHk4OE94TnVUVkdnZUV1TjN0dk1ma2dGTkM1MllqbkU5R1AzNi9aRisrL2t0L1V6UnJVQStIQzhYbFpUYzRiUUc3Q2lyeU9ZdU5HVDBNWFF5ZkRlZHVLaGo5VUZZUlppTFdZci9sZkw3ZE5maXl6UHZZMDkyTGp0L1I1blBnV29yT1FrVk93ekpMY3UrNDFtSStHNEpjN3RlNUl4TVZMa0FlRHFsZGp4RXFnZ3ZVc0dHNlBZZFRpUUtUVzVVWkVuRlFFczZORmtwZC81ZVFLQmdRQzRrV3lDYm1xeUxac1RQK0xPakt2RGxWSVo2eHNDaHkzUS9ycGx5cjhIeDQ0cnBHSStNOGFVTWM4QWJaQzdBMFp1blNGZUlvM1Z0WFRvejBuN3FDcy9UUjRjOHp2MXdiWTRPdkgwSnJsRHc5bXRWMGFlRnQ2T2F1eSt1ZjFqSG9kWWNyTW9zdFNUdmV2dFR4QVFmSCtoN2FFWkZDZTF6WXB2U1hzRXFpdjhad0tCZ1FDbjdTRDR2allrb25kb2RTdXpjTWtuTXBnak1CaUttZnU2TTkrQ1E1NVM0bDBvcXRvWWdCSmp6RkRmSi84M0VJUEdONTZ5Sm45STFDaXYxQ3NSenBpRnYweXdRN2JYMWJ1VUFBZUd3VjhmS0lxRWQ0NjVrYzJ3Z212UGVnc29QUlJrcHBva1ZoMytXTGwvcjdSc0g3TnN4T0pJWnRuYTRWczBVZEM3L0ViaWh3S0JnUUNMV1FCYjJaR2t4Tm40UnB1dTVuWW9UR3lZTlBGSGoxZ0FHdElRV0dxeUxQQWg4eEpaZEMzUlpXbXNJUXpNcFVSZjd6SnFLQng5NVdwRyszb1lEbmZZYXhqNU1vdHFtTDVDNWY0WEg4VndiRVhFb2NnblE0ejBhYllrcWJldFJqZFpoLy9NRW5oOHN6K1ZBOFJWTGlvT3o2SjVsTVlHZFJDM3hQcWtJdmJpc1FLQmdEck15WkxQNTkyRUZoTzVrNGZOb21IYlVYSmcwUGNYWEJHalFFdzRxU09VcDlJcG9SeWJHOVZlSWFOQ09oZHA3UHBuVjJaQ0hLZS93azl2RjNXd3hhOXZnTWJucndwOGlLWVdMSXgvQVhQRG1sMHdFQVhpakFlV1kzSE81a0U4d2Z0TWF3VDJNcUp4SnVNUy96WXRFNEt1bmgyRUJoeWlkSEVwaE5HT1VMUFpBb0dBTGFZVzdId0krRjZMaVRaejdOdGg2eDUxRjVNaXVIZGU3TVZYQ3JRamxESWhCZGZUSGNyMmRyUC9xVjJMWnEvQklkcXIvS3pGMCt1MXhaTjgwR1Y3Y3BWK1B0VGJucGVvSVN6dHQxV1NBbmRRamgzVWVqQ1A0WWtRQnRITlhLaGEvUURWSkxVbmdDekxTd2VGRjRoZzg5TGRYWDNBektWZnJvL1RUcStzM3pFPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0hGMnU3Mm5TVjdhOURDdHlxcG1aRHRvbDJEWk1pMzBHVjBUM0lwQ1dzbDRsNU1KcXB6eXFRVWV3eWRkd3hRNm40ZWVITHFEODRCVW44U0JWV1JYSStFekVsUDJhTEFjSkZXTzF0UE90UG9PMDBVNVJVMEkrbnpqMEhiR3VXWlAyZHZaVzJ1ZnlqV2ZEOWlQanhZU2FWWFVpdVp6RGJnSDFkQUtwUXM5dUpEcEFoVUFwZXZBMFpxam80S3UrNkhzS0Y1a3lCZlBZZ0VDZ1lBWTFsRFJ5MjJrbUxoVWpOSGVLRHdUMkErZ3RXVTM1c0thbkp2cWNwaGpHcWZqNXYzaEE0Y1ZPM2hvOFc2SnpBZTFKcldGMVVjMER6QjQ0TkZtWC9oZVpnNWZVUE1oaVJOdWFERDVWWWltTjIvbXdLejd3TU5ITEwrNVg5MTdBeGlyblhvTVYyU3VUYkpIUE9PZnZXQi8rVUQyV2FoSWR1TDM1U3hnVGZuWGt3S0JnREFHTkNWeDUwZ0lGdEpPTElqbFV5a3hXQjBXeCtSZVd0RHFNV09CNEpDN3lhM21xTHRuMTBrV0U1MnRzOWhEaEw4VXdZbUl0UUFFNkMzTk16YldWMDdjUndHOXhqbWJUcHJhc3hQV2oxbDhVUGdIVFQ5YWVEMHdzVWJLK29CdU5HcWNLbXlIQ255RUs0OEIvOEFtaDg1Ujg3TEJFNzE2Q2ZsMXVDejVZZ2ErQWhVQStPZzV1UDFPcXNvWVp6TFJXaWpHT2hBYkxSWT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNHTGlqeEdodmF0UzlIaUFIQkZ4U2QwcEZyNGp4ZThrRkZ6RG9zU2c0SW9BY0dCU3VCQkFBS29VUURRZ0FFRENkNWFpUTkrV09lRmNiL050bVNYK2E3bWRQZ2w3eWZmU3lORlpGekZvV0FXNFJoL3BqazhwZXhMS3pJakxEUnVUcUQrNE9ZRXdLM1pPaFlEUFd0S2c9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVCcHgwWERBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOekUzV2hjTk16SXdNakF6TVRVeU56RTNXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0hGMnU3Mm5TVjdhOURDdHlxcG1aRHRvbDJEWk1pMzBHVjBUM0lwQ1dzbDRsNU1KcXB6eXFRVWV3eWRkd3hRNm40ZWVITHFEODRCVW44U0JWV1JYSStFekVsUDJhTEFjSkZXTzF0UE90UG9PMDBVNVJVMEkrbnpqMEhiR3VXWlAyZHZaVzJ1ZnlqV2ZEOWlQanhZU2FWWFVpdVp6RGJnSDFkQUtwUXM5dUpEcEFoVUFwZXZBMFpxam80S3UrNkhzS0Y1a3lCZlBZZ0VDZ1lBWTFsRFJ5MjJrbUxoVWpOSGVLRHdUMkErZ3RXVTM1c0thbkp2cWNwaGpHcWZqNXYzaEE0Y1ZPM2hvOFc2SnpBZTFKcldGMVVjMER6QjQ0TkZtWC9oZVpnNWZVUE1oaVJOdWFERDVWWWltTjIvbXdLejd3TU5ITEwrNVg5MTdBeGlyblhvTVYyU3VUYkpIUE9PZnZXQi8rVUQyV2FoSWR1TDM1U3hnVGZuWGt3T0JoQUFDZ1lBd0JqUWxjZWRJQ0JiU1RpeUk1Vk1wTVZnZEZzZmtYbHJRNmpGamdlQ1F1OG10NXFpN1o5ZEpGaE9kcmJQWVE0Uy9GTUdKaUxVQUJPZ3R6VE0yMWxkTzNFY0J2Y1k1bTA2YTJyTVQxbzlaZkZENEIwMC9Xbmc5TUxGR3l2cUFialJxbkNwc2h3cDhoQ3VQQWYvQUpvZk9VZk95d1JPOWVnbjVkYmdzK1dJR3ZqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGSDRPcERCOGVYZHBiQXZmbTZoQW5ubFphMHRBQWhRWWx1YmppZWNxUDBaVGxINkpZK09HdGNvNkJBPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUVZ6VUk3TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOekUzV2hjTk16SXdNakF6TVRVeU56RTNXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRTUozbHFKRDM1WTU0Vnh2ODIyWkpmNXJ1WjArQ1h2Sjk5TEkwVmtYTVdoWUJiaEdIK21PVHlsN0Vzck1pTXNORzVPb1A3ZzVnVEFyZGs2RmdNOWEwcU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU5tTDdraVl0R1Avbit1WmRzNlkzbHVKQTlIQmtKdUpDUkt0dlNLaGFCNUVBbDlVN015N0FPWDQ3Q09LbEpVdS9NZkpzdUNPcGZxc3NNMmt2MjYyeExuZG9sYkZzZ25HZU1hVHFJZUxNREJPK0lmbkE2N1phK1VQb1NRRisrc0VJaE96YXBUQ0c2RWg4ZWZXcmRkRFRiZmZ4d3JmMTlTbjBaaUgzVWtLQ1B2TTFnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVYdkl1L3pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEkzTVRkYUZ3MHpNakF5TURNeE5USTNNVGRhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCNUVkUXdEbHcyeWtqYTFONjZWNjRGOEplWWtVazYzWXlWSjJEd3Z0UU93V1FodHk3K3hHaUFjaXZkbldiNllRRlZiYU9IbVIrSStySVBaanM3c09CM2JMWFUyaDhPMGlXVlBFa1BIRDBYTldJT0puZGtienVoNmg4MmJ2T3I4ZkI5ZzIwOHArVW1yUVh6MVIybzlGT0o5UWZzaWFxa1pNSVAvUkdJY1V4bDRFSjJQSTVHZ21wa3hZZXpQWWhRTXFDY2pQb2JQZVNuSmJOd3FERUx3TE80YmZmbWJ3YnpOK3REcXQxczNGcWdyOTBTTFJjYVZzZ0NhTkV1Ylh5Zzh3TThGOGJvdmRueldRYW4yaDloT3RsZkVMOHJLYytONlFENU5EaXJaMUJFanRiOUJ4dnJUbGpFUjNDNzhHMVBoMHJRenlndExKVUs2Snp2NFduNkx3aFJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFEZG43Ti9EODBhRGJZMUZJazQyYWxIbEVUVXlNRTNNRTMvUCtZNTRJZk9QczJOeWxIaUR2Rzd6bVdQTVBiUEhpOE1vNDMwUVN6Tlo4eXZ0MkUwQkoxbk9JZFo0YjBKSUhHcVBkK3pHS2dRbHFNYVFIQnNHQ3RPTE5zS080cldnOXhURktZTnpoTlpBejMxdVduck1SNFcwaXNiYTdoTSt4L1hjS1lGOGIrYUpWT2pqd1Q1U2FqNExSUDEyYUxLVGNEc0J5TjYraVM4V3ZxaFp0ZjNkS1lxSUY3UUV2U2k4aVlESnJsbTZkRlorZG5tNml1OE9UK0hPanRvSG1xUys2U1dMNW9COGN2R2pyTVBrcmJxcEg3MzQxUTZFUWtya3hWTTlKWVJBS2hPamlGRzlPZTJDWE85Z0lhU2tDSnA1TkVoTmdZbkxCeTI3WkhHbWFGOC9tMHc9
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
     ipv4 address 4.4.4.4 255.255.255.255
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
    interface serial1
     no description
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
    logging file debug ../binTmp/zzz25r2-log.run
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
     ipv4 address 3.3.3.3 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
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

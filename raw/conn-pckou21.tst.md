# Example: ppp with packet over txtls
    
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
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWsvM1I4MHppaHo0dFRlSkxEc3BxbHBGM04rVDVjMXVQTHZKSWgrbUxUWlhWa2pCNnY1bHFOS0VySTJKMzh0d3VMMUFNdnhuRW12bUdJQVY5cXdxcGsvRzBBTjFod2N1NUNyUjhodmtLbEVtS25ETlhRaDVtTFFBckxtV2hCT1A3NUJFN0krQnZhSFkvT0U2Q1E0MlRkeDVnZWhwbkFRc3ZTdmVQZXdQUjZrWndUMGI1OUNQNmMwbUJmSFcvRUVyWE5DMktlc3NXOXJyUzJpc1dsMmZGazVEc2RQM3JHbTZwTC9tN05yN0traVNrN2ZIeGJ5SlV2THUvSDlYVWxIamJwVCt6WURrcStRUTlzZkwwY3I3VHZ1S01EQStvUmdpRGhXUElPTGJ3OEF0TzNvSUc4eEIvbEpvcm1xNEdrd1dUK2R6MUVsYWhZbHhueWtUVXpmdmpIUUlEQVFBQkFvSUJBQ2EvNXlGVm1GcmhKT3VudlE5NllMNWNDR05TU1I2emNxSlFQajJZSVNtSGVneDFOUzdGOU5FakFqQ1pyOTZmV0ZoN0ZWdFVXKzVZTjQ1YTRiVFBiZWVXK2hMZjVLRGh2dW5XcUdTUEFQNGk0M0JTNFI0bTU0b1E2VDJVenJ5QkZZdDZGNG9sVWdhQUw3MkdrUVV2Sk5XajFvOGlLcVpUVDJiSnUzL3lXQnlIUGRQUDlVcGJobnpTMVJnL1pKRS82bVBuRjUxTURGaVlJZWNiWUhHV0NxVlRBRS8xd0lSaktSc1NHR0tqR3EvS1lSUXZXOGJMMDNVMVhpSjRkWWJzaWJlWnJxbnpFbUFXcWF2bmNTZHZHSVJMcUtzRlZ5LytZNlE4Y1BJQXVHcFZ6MDF6bi9nWU81NDFzdGU0TVZad242ckxkNGFIaDY1WGpwcW1uK0R3RXVFQ2dZRUE1R3pwT1o5Qk14cC93empJU2l3RUJ5VGVKWFp1am84UGJuNHBBOWV6TnR5SHVpMDVFcktzZ3VPQ1hkQ05SUE9JQkt3SGxrcVFSZ0tVbzR1Q3VUaHh5MTI5emo2NHEzV2k1V3VHRmNVQXNzVzNrZXZSNk1kcTJxR3pYLzdldmtyVmJRSHhqNUFudEpQbE9ZVkExM2k1dENBdzVjMFo2NkV2WDNzWGdFMEV3cHNDZ1lFQXBkczlDSjhiazA1aW1UaUM1YXBUaDFJQXo4UjB2RjhDZW5NenVub2wvbCsxY3lrK3NSdXQ1ZUNsMjlZMVlZaVRpdXB0Wm1PWGc0MkJLa0x6WSs2T0o3cWdlVTVadzlvaFdURUxwVW9WZmVUdmxsOE1MNW43aUNZcUVHalhyekxJYXBXL2FJZ2toOVZkTmF3OGVYbjcwaE1JQ3JTYUw0VkdZVENxWGt2NTBLY0NnWUJCMHBSK1UwTFJmQkJXN0JUak1yM1NaVEJTY1VjNGMwY0tHdmFzc2NwbHc3U2sxSVUrdXhmMCs2UkVibVZXK2lvMjFtKzFRalZDeDFtWHF3cjNYcW1ENWJaZEtUdkR4TGsxRFAvdFpBQm9nNHI3VkkzL1d2K1Nrc2dDb0lvRkljRlFrUi9QczhXTlJwVG1OMXpRK212ZzJPbmVQblQ2cms3ZFg3WU05YVNxZ3dLQmdEY1FTSDBhUmM5c0VMUUozUHRleHdpQUl5RFhlbUluc096eVhsUWt4WVJrUmh1THIvS2cyK1ViNWpUTU0wREVWU2VqbU5xTGFmd1UrTE1OTXowVU1FSGtaZTZnSXBFeFZDMEdhWFZnMlMzSTJmbzBhQmxOcUFLVm1SV0ZtVVhqT0VLYW9NZVZtM3MxVFJMS3NmRXFuSDRzTDFsT2lIb0taMGxSSE43ZG5ueTFBb0dCQUltbk9sZW9GVGU3MXNScCtUT0hhZlNRbU0vdHgzdWFNK0dmYnlOUTcyWGxiNVlGV3ZnQjloN1ljQUZ5ZStoR1lVc2FueTlaNXRJT2JDVlVnZ2hwZUs3Szg5azIxNUQ0Y25FMVVkMEY0Snh2cEJQODRQdG1NV3c0bkpTUjV5MXVEbG1SUVQyU0FXKzloZDJ6by9LNVVXZFJUaGVmT2tFUU9EZ0oxbWRzbDJjbA==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0NiUlVLZ3l0NVFqNHc4eW11dU1zOCtqYmZCZThTZ2wwOWgyUlFUSzF6ZjduOXFrejh0bXUxNnBKL0lQcmtHVW0rRU1sb0Q3bDY5VTEveFNyeGdUa25WYi9ucWo2K2o2SmJXNDlDRUkyazRmTE5CRmlubFhteFhqZjFlZXlZaTRDaXJsOWRQOGJHaExpL0pHdFpHNUticUpwTk1XZnFoSmg2SjBIQWt6VmNIUEFoVUFnU3ZYTkZqTzBiNHZTWnRsMHBTVnIxMHJ4aUVDZ1lBU0JSdWZNMkYyQVZMd0REQ1E4WDlIRGtOWUlnQnFpL2t0TzhPbkg1ckNhTkR1MnZCcWc3dm1TVUFhU3BIWWpDTDhKOW84cXdYeE9ST2FTN085NEQvNG1lREdOS21xWStwUlkxUk9QL1NEM3JFM2RoTHdmanNpUXVpNHo1QnFCdzVDbkF3Y3p1VjJtU1NidzJ6TzFTZFpyRW8xRHdLdnpqOC9ZTHNERTFTL05BS0JnQTdCSGFES240RE9PVmpCbTRVYTF2eVYxWlJFc2h0cVBXaVRzS0E3K0ltMFdvU3c4UGtiMzFoQ3hVOHVncWJoWmNEaWdaalpianliYU9PY3BhMFNVcSthSzVnd0RKSXBweUVoWlc4eVRLWUJweUN0TmpVeFF5OE1CSTlrK0dRRWgrcFEySXREWndYVVRsTGViU0FBdlB2UG82TEU1ZWFWTzhLVXczWE5Ga01HQWhVQXp5Y3BzVWRzL0JpUnRlamZHU1RxdElnUE12Yz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNKR1h0ZEc1Rm1yckdBcDQ1VkJBcVdQT2ZlRzd5dlNqNkM5RC9DR0ZCWm9BY0dCU3VCQkFBS29VUURRZ0FFb2JzZW5obG1lY2czWEFyVDc4K25KcVp3NkJDNlBCQmpLWVFYZncxaWhjdk43NGExSXV6WDNvOUpBa3ArdW9KUWFLbWxWUTVBVHByZ3p0RlR2MnlJOEE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVYSTA2R0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pPREU1V2hjTk16RXhNakk0TVRrek9ERTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NiUlVLZ3l0NVFqNHc4eW11dU1zOCtqYmZCZThTZ2wwOWgyUlFUSzF6ZjduOXFrejh0bXUxNnBKL0lQcmtHVW0rRU1sb0Q3bDY5VTEveFNyeGdUa25WYi9ucWo2K2o2SmJXNDlDRUkyazRmTE5CRmlubFhteFhqZjFlZXlZaTRDaXJsOWRQOGJHaExpL0pHdFpHNUticUpwTk1XZnFoSmg2SjBIQWt6VmNIUEFoVUFnU3ZYTkZqTzBiNHZTWnRsMHBTVnIxMHJ4aUVDZ1lBU0JSdWZNMkYyQVZMd0REQ1E4WDlIRGtOWUlnQnFpL2t0TzhPbkg1ckNhTkR1MnZCcWc3dm1TVUFhU3BIWWpDTDhKOW84cXdYeE9ST2FTN085NEQvNG1lREdOS21xWStwUlkxUk9QL1NEM3JFM2RoTHdmanNpUXVpNHo1QnFCdzVDbkF3Y3p1VjJtU1NidzJ6TzFTZFpyRW8xRHdLdnpqOC9ZTHNERTFTL05BT0JoQUFDZ1lBT3dSMmd5cCtBempsWXdadUZHdGI4bGRXVVJMSWJhajFvazdDZ08vaUp0RnFFc1BENUc5OVlRc1ZQTG9LbTRXWEE0b0dZMlc0OG0yampuS1d0RWxLdm1pdVlNQXlTS2FjaElXVnZNa3ltQWFjZ3JUWTFNVU12REFTUFpQaGtCSWZxVU5pTFEyY0YxRTVTM20wZ0FMejd6Nk9peE9YbWxUdkNsTU4xelJaREJqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRU5taEg4Tm4vN1hRQjlTWk5rS0JFRHJXNW5QQWhRTUswZXF0QjRKaEJyRkF6K1BMQ0dONUh6NUt3PT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUUdDU3RKTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pPREU1V2hjTk16RXhNakk0TVRrek9ERTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTaHV4NmVHV1o1eURkY0N0UHZ6NmNtcG5Eb0VMbzhFR01waEJkL0RXS0Z5ODN2aHJVaTdOZmVqMGtDU242NmdsQm9xYVZWRGtCT211RE8wVk8vYklqd01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU1ISVU4TDZBY0l5TlYwT3hwb2JicTFVdENDVEtUQzczbFVOK3hZWktodFVBbDlmelhSMTNoOFpoVEhkc2c5cmN2Q2NrT05rNndXdVY5VWlrbEhJdC9ZMVgyU0dBQXlkUzB6WnAvRU1jNklocjZmTmRNdjlZeHNsUWhRallQd01hN3d1VkxwYmtTSzBPTmJxWVRRL3phQVd0ci9HMlgxQ3NBK2dtMDFsSndCdFJnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVNdzJBbURBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXhPVE00TVRsYUZ3MHpNVEV5TWpneE9UTTRNVGxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWsvM1I4MHppaHo0dFRlSkxEc3BxbHBGM04rVDVjMXVQTHZKSWgrbUxUWlhWa2pCNnY1bHFOS0VySTJKMzh0d3VMMUFNdnhuRW12bUdJQVY5cXdxcGsvRzBBTjFod2N1NUNyUjhodmtLbEVtS25ETlhRaDVtTFFBckxtV2hCT1A3NUJFN0krQnZhSFkvT0U2Q1E0MlRkeDVnZWhwbkFRc3ZTdmVQZXdQUjZrWndUMGI1OUNQNmMwbUJmSFcvRUVyWE5DMktlc3NXOXJyUzJpc1dsMmZGazVEc2RQM3JHbTZwTC9tN05yN0traVNrN2ZIeGJ5SlV2THUvSDlYVWxIamJwVCt6WURrcStRUTlzZkwwY3I3VHZ1S01EQStvUmdpRGhXUElPTGJ3OEF0TzNvSUc4eEIvbEpvcm1xNEdrd1dUK2R6MUVsYWhZbHhueWtUVXpmdmpIUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQkFrbU1nRi92NVdMamhicTVPR0JpSUxuVk56VGYxVU9XVWo5UFhDUTUyK0o5V2lRMHNDZ3FHZzNaR1BhRWwyN3lrRXZwOVdVNFVQS1drWHo2bUZTUXpudWQ3V005MGpVRExNNzhTN2p2OHJIbW82VTBtRktCNloybjBoM0p2a2pmSEVENmdsSGJ0MDJsVUlhQ3c2Wi95V3VTNVgxRDJCd25DRCtBMy93Qy85c3BKdGE4L1U5d0NpRTNUWFl2aTZ6N21pemdYWDdHelZvN21zL3NsZGtlVjN1b1NlMDdLYStKcWd5WmRxTklucXVWY1hTamlZWlZLdVkwZHdwNnZSWjI5KzA2KzZicWthd0Q5c3BDakJaRHRLclYvZVFWdzBYVmo5OERFN2FpbmwyL1VNNjFLamJDZVpGYnhySWRIN01yQUNOZmdKSHdkclQxL20vNWVudHVR
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
    server pckotxt pou
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
    logging file debug ../binTmp/zzz1r2-log.run
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
     protocol pckotxt
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

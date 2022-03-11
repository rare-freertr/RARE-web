# Example: ppp with packet over dtls
    
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
    logging file debug ../binTmp/zzz86r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCNEpXcCtKd2FZb3ZkZytTZjdxaWVtNXRiOGNXOURpaHNXdzJRVGFBbndDQUc0ZDNtQUFMMUhaNkRObWZXTDduMUhsR2FDNFlVb3JGYzJyekJnZi95NTViNTE5UnpUcWlPcVJpR29La3lNTFRMY2djWTNwb255Q3ZENGZvMC85K3k0a045OU9vVFY3OGVEZ0RCTi9DbXRSR3A5NUtjR2MrVlJOMldJWFdlOUtQVmtiRG00TmF4SWRoK2pNVlNMdXJxRUYxcHZDQ094S2dPdUE5WHBMV2JkRjJQcEUvNWNlNmxYWThWekVYQXd3aUZOYUN6b3BrdHlCa05mOGt6a0RJN0FGNjFOSVpncHkrVG5seEliZ21TMUxVZWFWbGMvclRBRnVSYnZTZmYvSHNzNHBLdnA4bzgxMGZvMXZ4Rmt5UXpha1d2aytFNFM2M2Y1SWZzNHF0MUxBZ01CQUFFQ2dnRUFCWXVzazdBWGROb28wdmdOS1dlY051NzJ3MlkwL1lnVllnS1l6dkNCYk92aHNITUxUNlk1RmwrcEkzUlV5aVd5OEtmZjUzQ2paZEkyb0ZhTHhCaUVRTXhpOHl6aUxMN3dzSDVXTlYzbWRKM3RlQkloWlJZeHpkTkZkaUxaUURlZ1hKQ0xVRXR3TURQR0lNSzgrQXlJbSsvSmZwQWNTWWIxOGI2OTJBSi90RkpzZGNBaXJTS0Y0bXRIV3JLcFc1WXZObVFMQzJURXlwMzhCb3NJaEdBcEw3YTgxQlRESHQ5cTNZaFZ3TGZvaWhWNDhpSFJwNGVhVmF3Z0lDazVPVU5MclVGdzNhS1pNZ2NqYUUreHN6Q2JsbldoU21sdGphZUxnaDI1M2JNQ2pNY3FzeFBXeC93WHJFSXdkSWdobXczYmZTZFVEOUpkNVdJMStwTHJia2Iva1FLQmdRQzE4OUIrY1VHQkJJK25QZWJXaGF1SjU0NVR5U3R2NDlFY1U0UDZ0UnVCdEp6R2Y4akxtalhZY2NaNGZxcnpJQXA3OTl3cDBvbjcwRUlHNFhQM2tUZUhSS0VDeEFLajUvRWhlZlEvdkNEMmppVDN0NmtkMm1aUzdXRjI3bFBMSzBKS29Rc0E4eE1aT0lnTmc1Yjk2dzdpdVlNdEdKdEduZVRNcHlZV3ZlKzZNd0tCZ1FDcENuOFhWR1NOc1UrRFVJNUdVVDl4NVVzMTZ3VGlrWjVwNDlpS21sUHhMNWdhclIyUkVNTVdkeWhuc1ZHbDhQc1hoK3VvN1kxTkVkd2VWNTZnOEo2ZVU5aitaVWl3cThmYXYyRFBsdlNJWWFsTHZESFc0YXY2LzF0dlRuM1FGOWQ0QmluaTFYU2F4ZDU0bkJxR0lZRnE5QXlJMWM0elpuWUNWZzRBcE5ib2lRS0JnRHhubGZiMEtIZnBpTHRQM0p1cFFycUVpZ2FjeVhQYTRPZ1RmY1EwYmM1UXBKOXRlcjdGRWswcDhHYStQb2g2UWFESU4yb1hBRUg5OEgyU1NVcU9CaTQ5QldzQ29aSENoWlhFZytiSTBQU3BXZkozSVlqTW9aMjBPdUFkM09tZEVlUHV0TlY2M1FOSmRqbHVUeWs2NlBVeCt5OTBkTkFyeVBKOEp6UHptR3RyQW9HQUl3cEMrQUlOYWZXMFJzTWZDdUp5cFZoamM4VEkyWEpZQlJrdTNPUkt2RGNpYjMwdElOSDVycUY2cGF2ekFkUG5LS1NMTEJRNTh4emRwUWlDb0ZmZ2VXOW1EcTNPR0prekwxdjJaSEdsTk5RUnROcEk5b01IRkZ0MGg2a2NtVk1uM2dCaEZGMHM4NXhLbG5POVo4cHdPa3htZ01MWklIeC92OUk0eXRkZ21Ra0NnWUVBaUoyQmN3ckRpZTZBVEZML0JYVXN6OHM5VVBsa0lTbHFaeDFwNGxkb0F6SmcyQ292SWZFeEFtY0RxRUpENzJtcFNhVG81NXBqYU1zNkNsWUUrZWhYejN4S295MkZza204SDVEWlQ3SHNNUm9uMVNvK3ZQUTdNMG5wOG5ERE1Zd0w2TmdWUXgwN0pXT2c4dzBhQ3grR25jTGNJWFo5ZUUwWGFwUXhIUWt5RFJZPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0R3N2p4MW5Bb0NaU3A3TDM1R21CSkt1VFVkcG4rcitxUXBxMkppaDJsYTdpbHQ1N0ZDRGZaL2FIQmN6TFlkYkNFOVZUUnB0cVh1c1pvclhRa3k2VDBVZll1MzZCSTg5em1zNGF2UmRacWs4ZXF5em5SZXBQUGtsbmJzWkhEMlFmTUZ5QlQ1bXREZWx3UGhYaEs5WC9qMHZzSjlNVUlRZW9iYkdQYXBuUVJLaEFoVUF1d1pQM3YxVmJOTytrejYrMXhyekVxVmtwSTBDZ1lBeERUU3FjRTRtM0pFdlkyVnN0ditoS2FWVnBjeSttUlZUNTdPcnI4bTh4Vmg1R1pxS3ZyU2JXa1d3TWQ5aUYxUm16QzFzb0J4Z1FWNGJtS1RnYXdROHZrUHM2V3hrQUVUSWJiMFJ4VjltV1lUUGp0Q25RQXh2bTJEeU11WmxSMWhlaGpXK25QblYyeE5LZy8vY1FZSldwckpHRXZmOWNQRFZHbmFFYzZ2d2VnS0JnQXVxU243WS9ldXZrSi9WN1VmMXdxV2lJT2pXSEtsZTR5c1YzOUliTGtEa0xDOFdZdE1aRFZxVk1YTFNUQ1AxaU4rTVdZOUw0dE1vNG1kdFZyZ0gvM2dRMXNEUW5hZ2NwUGdDTXE0d1BzV28yMlRlT0ZxbGc2WWk0Z0x0dmlOZ3p0Qi8vbHBYcWt4VGoxZ1FLMnk3MlBlZXNpUzVQdXlIU0ZoK2dlUS9sdWtJQWhVQWoyM0h4UzVCZlMzdXRFMUtKRVdieWh5aFlwVT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMU0vcnByaCtDVDRCOEZtRlVOdVlRQ3hjNU9GSWZiUWUvQzVIYmdERENHZ0J3WUZLNEVFQUFxaFJBTkNBQVM2cVVsd1lkUEIwNThUVUtXMzlqRFBBdmRWUldneEJKcmJ2RFhvTjFPcUhRZFZSNTNWV28vNnppRjlORFlPTTVXbjN3NU9DeHd6MnhJWXlUMmk2TmdK
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVIalJLV2pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNRFEyV2hjTk16SXdNekEzTWpBMU1EUTJXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0R3N2p4MW5Bb0NaU3A3TDM1R21CSkt1VFVkcG4rcitxUXBxMkppaDJsYTdpbHQ1N0ZDRGZaL2FIQmN6TFlkYkNFOVZUUnB0cVh1c1pvclhRa3k2VDBVZll1MzZCSTg5em1zNGF2UmRacWs4ZXF5em5SZXBQUGtsbmJzWkhEMlFmTUZ5QlQ1bXREZWx3UGhYaEs5WC9qMHZzSjlNVUlRZW9iYkdQYXBuUVJLaEFoVUF1d1pQM3YxVmJOTytrejYrMXhyekVxVmtwSTBDZ1lBeERUU3FjRTRtM0pFdlkyVnN0ditoS2FWVnBjeSttUlZUNTdPcnI4bTh4Vmg1R1pxS3ZyU2JXa1d3TWQ5aUYxUm16QzFzb0J4Z1FWNGJtS1RnYXdROHZrUHM2V3hrQUVUSWJiMFJ4VjltV1lUUGp0Q25RQXh2bTJEeU11WmxSMWhlaGpXK25QblYyeE5LZy8vY1FZSldwckpHRXZmOWNQRFZHbmFFYzZ2d2VnT0JoQUFDZ1lBTHFrcCsyUDNycjVDZjFlMUg5Y0tsb2lEbzFoeXBYdU1yRmQvU0d5NUE1Q3d2Rm1MVEdRMWFsVEZ5MGt3ajlZamZqRm1QUytMVEtPSm5iVmE0Qi85NEVOYkEwSjJvSEtUNEFqS3VNRDdGcU50azNqaGFwWU9tSXVJQzdiNGpZTTdRZi81YVY2cE1VNDlZRUN0c3U5ajNucklrdVQ3c2gwaFlmb0hrUDVicENEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQVpFV003clNuSWJ1aWlROC8vRVRSNnVZRXVDQWhSRkg2K1ErVCtpV1pCQjZncWNWa2Y0M05OSnhBPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUXdHRXN1TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNRFEyV2hjTk16SXdNekEzTWpBMU1EUTJXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTNnFVbHdZZFBCMDU4VFVLVzM5akRQQXZkVlJXZ3hCSnJidkRYb04xT3FIUWRWUjUzVldvLzZ6aUY5TkRZT001V24zdzVPQ3h3ejJ4SVl5VDJpNk5nSk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnZTR6ZUlOMFp4TG42NC8zMk1iNnhDOHlEam13ekR0Q01hQ0F4Y0k5bnVwd0NYd01VT01HZjQxZk5OV1FWRnBFV1RvN0ZpcC9vZ1hQZzNGWHpHUFUya2pIWENrZ25EWVdDalRVa3lRelN2TjQ2dGlndWd4dDZibHZ4UCtvaVhVd0d1TmRRb01PWklkM1JwNnFOQzVDMVBzZE4vcGhRSndCOThReUZYN2hqUitvdA==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVMNDR4Z2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFV3TkRaYUZ3MHpNakF6TURjeU1EVXdORFphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCNEpXcCtKd2FZb3ZkZytTZjdxaWVtNXRiOGNXOURpaHNXdzJRVGFBbndDQUc0ZDNtQUFMMUhaNkRObWZXTDduMUhsR2FDNFlVb3JGYzJyekJnZi95NTViNTE5UnpUcWlPcVJpR29La3lNTFRMY2djWTNwb255Q3ZENGZvMC85K3k0a045OU9vVFY3OGVEZ0RCTi9DbXRSR3A5NUtjR2MrVlJOMldJWFdlOUtQVmtiRG00TmF4SWRoK2pNVlNMdXJxRUYxcHZDQ094S2dPdUE5WHBMV2JkRjJQcEUvNWNlNmxYWThWekVYQXd3aUZOYUN6b3BrdHlCa05mOGt6a0RJN0FGNjFOSVpncHkrVG5seEliZ21TMUxVZWFWbGMvclRBRnVSYnZTZmYvSHNzNHBLdnA4bzgxMGZvMXZ4Rmt5UXpha1d2aytFNFM2M2Y1SWZzNHF0MUxBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFBNzJwcFhTOEVYSzRlOTJUVURTRWtHRkFVRzIxdjJRR1VsdkhiTEZLOHF3WDArdDlCdER1VVBObEkvMVo2T0xlbmtUSUg4YWhUWXBPMDFOYlFOUmUrN2tnVyt6bDNWcU5Ldm9iRDdtRDh5Y3ZxSktxVGY5QVlIbVBReTVZWk8zdDlvTmNzcjJXMHVJWk9oWVBxUGFQRmZhVVdpZnk1V3I3ZTZyMXo5S1lJaXhKNENKRCtnNlhwQjdXbUpjY3FvSnJaN3FUQTBaTUJtOVV2UXdFbDhFM1BVOTFvSWR0OGY1WisrdTE2VmN4OVkvUkUrVmk4MkdGczFIVFhBWU8zdEVubzArbTBnTlpyQWE3TkNtUFNwd0pLK3NrQXJKYnZjMUJXZVBIUklFc0RQZkt0eWhXWW41ZFpQamRrVmFJeWh3aS82dWluNTF6MVloc2dVY1BzZ2pZN009
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
    server dns dns
     zone test.corp defttl 43200
     zone test.corp axfr enable
     zone test.corp rr www.test.corp ip4a 1.1.1.1
     vrf v1
     exit
    !
    server pckodtls pou
     security protocol dtls
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
    logging file debug ../binTmp/zzz86r2-log.run
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
     security dtls
     vrf v1
     exit
    !
    proxy-profile p2
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target www.test.corp
     vcid 2554
     protocol pckodtls
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
    client proxy p2
    client name-server 1.1.1.1
    !
    end
    ```

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
    logging file debug ../binTmp/zzz76r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWt4YStvV0J3UHR3WkZnQm1tOHBBSzgra282TVYybWVmN3dXWVBXV0pzVVZxL2ZORXFVUWdQMzN2VGdvMS9WUjJZNk53VE5qVkt0dUVKLytpQjFQRkxKMTlOSkQ3KzMvVWVyYTZuNkNyQ0pmU0lFT1VVWFBwd0pKS25wRm0yd3NhQmtrMnk5TEpOR29nNmdIRVJiSDZmeEhqa1QyazhKWUNzTGtBM2R2T0h3N3hmNGNJQ0lSd1hJazNseXV5WmxsYVZxcjRjVzFITUh5VDkrdGhXY0s5djN2bk82V0ZPZVZ3THhOVzRVNnRVeHhjWTBZWHdJeXpjV242b3lUS2NrOUI1M2ZtZnplVVg1UTZ6dVlCaXZsdGsrOVh3Y3AyUjRxc3hPeTlVb01HZXBjOHplaDNzOFQ2U0FVYXdjZFBwVjl5TVBVNXQyY1I0UEJZd2FENmhCMnFVd0lEQVFBQkFvSUJBSGtDWkZEbHcxS2p4dXVuNXNMU3NOcWFXTXZiVnhZNDNJWkxwd1VUN1NUdmhHZHE1UmtRbUN0RUUwV3o5dGowelBXS045Q3hMeWEwTkZTbjVnaDdMYU5YNmZMK09LQ2ZlUktBRktkUkNvVG1TcFFLcFJJaDk3UmJacEp2OHh2UVZWZklraEU3MkJhTUhZb0hiQThlcm9RdUZuZWVMSDFXSE42QlJhcEF0S0l0WjkyZktXbnVNa3lXZlRxdlc3a3hlNW16U0pOVDRPMTRLT1JyTDZlTlhUdHV3TExNTGdRVVFlNkRKQ2k4LzBlS1Y0anhIN0dlSVJheXcxUnQ0ZStwN1RGaFQvU1NsTWhOWGZ1MVplbkJtWFZ3VTZmL3pTYkd4ZHBFNERpODdlelo5VVlrNDRFb21YQkpaS0E4N21oWUYxZ0t4MklHRmpHd2I0M3JUeTVFNFJFQ2dZRUE1MHdIb3ZFS2ZNSUpaekNuU21ZZE1Ibmg5UDdibHBHazhObWxhcnlZYTFXdVZHSllFbTFzSWV5U3Z0bVJOTDlpSi9nSFVVY1BOWWsxSDYrNkErdjkydEppbWIvTS90QWJlQ2xEOTAxcGhtUEt5b1BESWhGVjc5ZDArTU5lMGVLSC9TRk56dEQ1YndBMEJLQTh5b2xkWGc3WnRiWjJIUk1Qci9GVDlBQ1ovN3NDZ1lFQW9zeFo0cDE3YkNEMXdaY3E1aWRYK0JHaTNKWXhCTVhuYnFQak1iemM5cEYxYmkvR1BvSGhnRmtSeEVjY2lBbnpXTmd6T0dVKzB1aENaL0tiNGZtcHFPNXpaUlBFZDdnMWpPMWwwOEdKUW5IM1FuNE1pOXhhdjNCcVVIVUtiaEMyYUZjNEtjOG01eXBGUDJTcWpVbjU3RWw4dExxZTNKU3VBWllJbWRva1dra0NnWUJTbjVzK3ZxSkRiTUVWSnBFc0I0dzN5K0pHdFYvVnlwTkVJa3R2OUl6eUVycGlsSHJub2tUMVhXQVNZdi8yK3NMaWlqeDY4VXBpa20veXNNQmZORWNMaXdvRDZEc2ZiMUhRdTlUMm02V3RoeXBpNjJ5aVY5VCtCMVpXb3R2VlYvbkNGOHFHcmFuYzJCSzg4RXluQVNqa042UFh3S1V5djZOajgyNU5CSVgrandLQmdRQ1lJNTFFdUtPbE0xQTM4TXU0ZHNBeEpsb3JCM2tiMnM4amlLbER6Qm83bTBoQkJ3aWZWY1dscXBkOTlHN25lMVVkakQ2aHo0eGNrWTJ0a3Y2MnVoa2h0R1hHNmloTE1hMXAzRm16QVVVREFYcHZlMWpDUTlYUzNuMmNYeVMySTR3MENuNkVKQUZaT3htbjJxM0FpSWUxbUIrZ3psNjBDWVpzR1FoRXI2WVZjUUtCZ0M5a0NDSkVPV2xFWDk0dU9NemloNmd0WjVyaXpCelBKaHRsTm5ZdjlvNE43QVN0MEd5RkxsUHg4WEpuTzJ2TXM0RG56dCtEUzRZVCtDU2NybjdYRVcrUDhscUtucTkyQnZhTmhCVXRpZTJTOGo3SUQvSHNEUGhOMTVVV29mWHJUMHo0TTRUOFBnKzJnRDhyT01sNVQ1bWI2cjg3cXdtWHBZSGZaZUlyd3BUdg==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDRytCMlR2M205eHJoajllZG5WNGdPSHhXTzFRaW9zWnltYUhrdDh6MDAxcC9ENEpaREdydGhmaXRlMlZkdElUU3U2aW45VjhHNStDR3o2Q1drd1RuOVI5SzZ2Zm1CK1dvQ2lBM0ZhaUhLSDIvd0V0dDRLR1FrcGlkbmovaFFoUXdBZkkzbC9wdzJqSkQySGhKMmp4T2lLdW84Y1ZZR3dYYUUrYWluZHk3elV3SVZBSlhvTW9HbW8rd3BFR2lYSmNLYjI3RFFybWEvQW9HQUkvYi9odWFvTWt5NkZUTkJ2bGVKaXRtbzUzRytYT3JTVEFUaEJ0aEJlSUZsaGFqMzZEN2d6dTYvQlRsR0RkZEJJZWc2N1NuZUc2Tm1yRUpZa213WmZaYU51UlJ0WnROVDV0SFIyNElkK042M3kwMC8xS0tiVnRiVmpJc2VpNnBlbGtEaU1TMDlkK3UxTzA4MEpQR0kzNWxGdWhjemt2b0hJZ3VuV3YzVHRaTUNnWUFpYlc4aUM3WTFEMXNJVi9oWWVraTdtb2oxVEdnTG1tUXpVUjAvQjgvZkVUbkVOVWRLaEsxQ0ZRTm5aeTZBTDlWbEZ4NzR4RG54bUU2cllUaVVvWG9xaVoyVGZLWGZiQ2VoOEsydU11WFNQVFR1bnZjTmY3czg4dlNuaXFHTFdoVERVdkpCUHlrRlF2Z3haekJiUVM2UHlYc25LUU1STGNIYjJRbHNyNUtUY3dJVVlDSTY3L1VSSCs5WW9KdGV4RVhxSk9UeGNzdz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMnhyZXNFWml3d2d6LzhDcnU5NGNsVG56bWhaWnpLOVFBNFNRcVJ0c3FlZ0J3WUZLNEVFQUFxaFJBTkNBQVRQK2lMYXNiVnIwbVZlU3hCd3ZDdWJKTFlkMXF0Rkp0SHJrRUt1QXdKcmVNaXdqV0JtbUU0dVhkNUhkQlZTaStsQVQ4aGRvN1RJcUpYOElPOUsrVStm
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBaENnQXdJQkFnSUVGNzdlWURBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNekkzV2hjTk16SXdOREk1TWpFeE16STNXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDRytCMlR2M205eHJoajllZG5WNGdPSHhXTzFRaW9zWnltYUhrdDh6MDAxcC9ENEpaREdydGhmaXRlMlZkdElUU3U2aW45VjhHNStDR3o2Q1drd1RuOVI5SzZ2Zm1CK1dvQ2lBM0ZhaUhLSDIvd0V0dDRLR1FrcGlkbmovaFFoUXdBZkkzbC9wdzJqSkQySGhKMmp4T2lLdW84Y1ZZR3dYYUUrYWluZHk3elV3SVZBSlhvTW9HbW8rd3BFR2lYSmNLYjI3RFFybWEvQW9HQUkvYi9odWFvTWt5NkZUTkJ2bGVKaXRtbzUzRytYT3JTVEFUaEJ0aEJlSUZsaGFqMzZEN2d6dTYvQlRsR0RkZEJJZWc2N1NuZUc2Tm1yRUpZa213WmZaYU51UlJ0WnROVDV0SFIyNElkK042M3kwMC8xS0tiVnRiVmpJc2VpNnBlbGtEaU1TMDlkK3UxTzA4MEpQR0kzNWxGdWhjemt2b0hJZ3VuV3YzVHRaTURnWVFBQW9HQUltMXZJZ3UyTlE5YkNGZjRXSHBJdTVxSTlVeG9DNXBrTTFFZFB3ZlAzeEU1eERWSFNvU3RRaFVEWjJjdWdDL1ZaUmNlK01RNThaaE9xMkU0bEtGNktvbWRrM3lsMzJ3bm9mQ3RyakxsMGowMDdwNzNEWCs3UFBMMHA0cWhpMW9VdzFMeVFUOHBCVUw0TVdjd1cwRXVqOGw3SnlrREVTM0IyOWtKYksrU2szTXdDd1lIS29aSXpqZ0VBd1VBQXpFQUFEQXRBaFI1eFdFN1VCaXhVcmJKVy9TSGQxNSsyczFZbUFJVkFKVG5BY0g3a1RUV3NmaDlKUlJ2RDlLYjZDV1c=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUktZejB1TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNekkzV2hjTk16SXdOREk1TWpFeE16STNXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUUCtpTGFzYlZyMG1WZVN4Qnd2Q3ViSkxZZDFxdEZKdEhya0VLdUF3SnJlTWl3aldCbW1FNHVYZDVIZEJWU2krbEFUOGhkbzdUSXFKWDhJTzlLK1UrZk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnS3FyOGp0M1dCZTFYQVd1L3MvN21QN0FoNytHMmlZVUFkaExmd2tSRzB0QUNYd3NhZ0VORFZOdE1yOU9hOTl6N0t2MUhhUkphVkZ5bHQwcVZvWEFtOVJRL2g5L1JWaWFvSEw0NWwyTEZSblRLd3JLUTloWWpNUDMyek5CbEVJWllHNExXcnVIaDFrYWpVUDJtZG4wTDNhUVZMdUt5T2dwa2ErbS9KYWJ4UG0rNg==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVTUm9IN0RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEV6TWpkYUZ3MHpNakEwTWpreU1URXpNamRhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWt4YStvV0J3UHR3WkZnQm1tOHBBSzgra282TVYybWVmN3dXWVBXV0pzVVZxL2ZORXFVUWdQMzN2VGdvMS9WUjJZNk53VE5qVkt0dUVKLytpQjFQRkxKMTlOSkQ3KzMvVWVyYTZuNkNyQ0pmU0lFT1VVWFBwd0pKS25wRm0yd3NhQmtrMnk5TEpOR29nNmdIRVJiSDZmeEhqa1QyazhKWUNzTGtBM2R2T0h3N3hmNGNJQ0lSd1hJazNseXV5WmxsYVZxcjRjVzFITUh5VDkrdGhXY0s5djN2bk82V0ZPZVZ3THhOVzRVNnRVeHhjWTBZWHdJeXpjV242b3lUS2NrOUI1M2ZtZnplVVg1UTZ6dVlCaXZsdGsrOVh3Y3AyUjRxc3hPeTlVb01HZXBjOHplaDNzOFQ2U0FVYXdjZFBwVjl5TVBVNXQyY1I0UEJZd2FENmhCMnFVd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQk52L2FUNG5SbzVyL1cyeC8wSDFqaHQ3ZzJXelJMYmVvMy9HRmVuTVpoZ3cvREovOElVMFMxbXBwRzdxRWFxRXRoNHpaWjNUZTBIWFpBWkNCZTBwUjBIWEVYZVBoc25Sc3F2a0JqUExGOVVTWlB0dVBvZWVxMGpWaUljRnEyVkdKYWZTZnBMMlZpQWhDWUpoNHBjdzIrY090Qkx6Vzl4MzFtUWlWQU5IOUtiY3o5ekYwQlh5VGJJMHYvTmRMdGlZNGFZVUpDaVJsNFNPM000UXJOeU1pYzUrKzhJZ1JWS2NvbXRQNCt3cFhpM3pseFpHQlJCL0hrTmV3Z2JLUk0xVk4wZTcrM2xqQmc5RmhGczRoaWNCME9VUmRGTEo4elEyMndXL3pFdGw5b3J6dEVvOFVBVkpDQlAyakgrTjRQZWl1MVQ5VjBhODBNWXBZVFZhZGdlZktv
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
    logging file debug ../binTmp/zzz76r2-log.run
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

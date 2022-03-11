# Example: lsrp tls encryption
    
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
    logging file debug ../binTmp/zzz75r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQTJJbFlmdUkzR05xcEZnZnhaOTlodG9GMU1RUXhDTWhJVmFqVWExNER3c1l6Mkhpb050R3B1alZIT01kMmcrTUZFeW1ZZXBkUVV5ZmI2dlI2c3NMeWFSVHROQk9Fc0paSUFTZTFKN2J5VDdrdHFEN0lJWmdkLzA3TUhKNUs2bGhkN3JKUDdEcXJ0Uk9NZlR0OUptWFdoWGFkMlBqL2wzODQrS21HbzNDZkRCMkVCWVBTb0dBVTkrQ3MrZ3JXNS9HWEFDTGx3SFFOdnlYQmVWWE1hOWRZZjY2NzZYTHpnOVZVWmZSV2YxM2hnUDY3d3VWdkNuamlXRDdtc25ia2l0NG55TElkOTRvK0ptSng3NmlBTnZoWWhWVzl5dVNaSWhFVDlzNVBxR0t6NlNQQjBKS3hFd1VmOWU2NU9IMEhsaG91UE5rOVNtS21wWHArR1ZHRUp1TlJDUUlEQVFBQkFvSUJBRHRZMldKZFNkQ01EWSsyT1puSWhaVnB3ZDdmVVRrZys0Sk90WGwvMlBRSE1xcC8xMHEvQ0ErN0Rud25Ydm9pdkg5V0JTNkVUa1djUlJBT1ZacXRCNWQ1WHRISkQ3TCtYVm5Ec2tqaVFXTk1VNUVyTTlyUlFGZDdGMEk0dUR1bVlJaE5ZczVSL2tHd3krNSs0WHdtcVRjSEhaZ2NGcUZGQXk1VCtFelBUeWdZWmFRMk5nbWxrZ0luby9EUVhXL2VGVUZPQm9aOUxGa2IrK3VWc2pLTmJpY0ViTy9pRFlVUy9yZjBhekxNUy9CblZ3UWtYNFROQTR1dWhIVXpHQy9oTWl5bU84MmFPbkxkaGEwTjBIbEozNm1oRTIwSTR0OEJlSXFLbCtwcWl1Qm1PTmdFbWNWWXlTb09FeU9UYThhMDZCSGVYTTZaeUVwRVk5c2psdmREaGtrQ2dZRUE5dVpkeU9uVGlwYUgyTEtvSHpLN3YrRXRjNkdOZ2ZXbHp2ZzVDUlZ2QlNyL1k5bXpVZXpjRmRSRWZ3RUJ0WnFHSmR4Q1c0aUtHYWdqbFF4ZGIwbU8vc3BKdEIwLzhLRnhnS1lUWkR2MHJzN0tRdEc3dGlka0lFejdZQUVpejZBbVpwbklFd3VkZDJZczcxQ2lsZm9MQjQvU0hUMDRrZFhON09DUHBOQkxRdWNDZ1lFQTRJUjhEN041My92S1Aydldzd2VmdjF0WGdReS9WeHRHV25BMjd2SXd5ZGk5RlhoblJvQmNzekpMVVd0RTVyV25KRkZBeE1MVWhyZmpPRWlqb1BCV0hVOGdqQURwM3ZaNXVuNUxkY2hwNVR6Z2FMcVBJbEZwQ0NFb0dmZmg4MW5EWTRGbFh6U2E5YUJGb2xGWFJsWjRQSTV2cTZkQWdIR24rZTBIUjVpVFBvOENnWUVBOUJFYjZxMkM2WUFPd0I4ejVNdFJIOGdvRnlNL2NKWDFsNWgzUVV5SDEvTCtUYVY2QjJWKzFyRmtHS3hWRlVHd2xLS2Nra0Z5U3hTVVFCWGVFMUlDNGtueisvSGlNQ3hYdUZYejIyVU5adlNTcXVVTGkzQjdJUmNZYzNvTUFIVVBJT09xRFhHdzhzUDFiWWtuZjl5U3BLSCtrZHJnSGdIZHMrajA5bmJWdjBjQ2dZQVFORCtuK25JZllsTFVoUG4zN2VMdnNxMzhHR2x1NWY4TDQvRnpDWFBQL1o2WUFCcWtFZnVleTFCNFRkK3BMdzhqSmVJZzBWYjVhaWd5RmJ3Smo0OEhpb0IwMmxRR3pZODNrSW50dEV0QVNrYUFDSWJ3R1NRVmZCOGkwS3MwSHhSbENCL0M0VThWenoxM1c1dUs3ZzY3Z0NRN0pWVVljQnVKaER2MFJPVExyUUtCZ1FDNW5MZ09PN3NZYWx1ck1nU3lIaE9xNytIM21paUtzMU9DQmhaeVU1RzF4L0N5aFlHdkdpSkM3NHZGSVEzZXdiNk5IU2NSUGMwNmMxM0pIZThRZGNUcE1zdkFxNXpzRFR2a1d4b01MYTJxWFUva0VkWW45YytWQVQwbGd4TkdCbmxOMm1ucWdGSG5oT0drNSt6OWVnTmg1cGtTdkVXYytnR3gzVUZuZHNRQ0tBPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDZnpaSkMwZG1JRXFoaE1nNkUzQUtxMzZHR0lKRW1FdUJSR3A3eERBY3hVdS9wVGhGbXlzZm5DU2FTRnpkbzJVYXdoNHAyUElLbUZmSUdlNEdFNDZGS2RVZndmd1ZiTEFHaFg2bGlFVVFaWFcyS3YvV2JYOGhwbkkwejkyOStPRTNuRGVrLzFXdG9pSnI3bjZSWUZTY1JibU5sdWJzMzloYVFrcjdJbWo3SGt3SVZBTXY5dFVEOFRuajF4Z0dtSjR4bXlqT3htZ1BoQW9HQUl1L1hibkNXdVFqbG9qdWJXMDZ2WjBxbFZsNWl1dGNGSE9GMFNJWGVMQzk3UzFUaXkxYTJMMzNldFFMY2VNenFsTUZUOWROMkRXclZsTjdJSVRoVS81YTlFREtIZXVzUWJJOGRKMVFsNUNadHE0TnFBT0V1Q093MTBmVWNWRE9yVTNZT1V5alFiVUxhVXhCbS90UE4xMHp2VHdYSk1oS1lvMlova1pzM20vMENnWUFlZUpLYzlISWhkZWJoZHdHRXlLNm9pNGRSQ3g1WDA0RzBoMTV4UVNVdFM0K29ZeTlLaUR3dXNUNlY0UGt4Z0dPcSsra28vcHp1b2RBTTVleHh0ZDlDUlBwZGt0YXJZYlpBY1FPUzdqUFhSek5pNVowMEhhcGNxdUhpOXFpTG9pUXAzWWpHdXBPZHAxNWtEQ1IvREpqQmFpRm5pTVk3bjZxdnpreGNvaWNzQndJVUdKYWhPVHRsTllqakFaUzRkdjhHRkNwbVVZOD0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeVhacFVab05uSmt1TDdST240U3RBMVZmbVJ6YW5ldG9ubWtkTkFxS0Y2Z0J3WUZLNEVFQUFxaFJBTkNBQVRJeWdGd0FMOUhvMCt0TUQ4a1JHR1lzZnFWc1A2Rld5THFIMlZTaTZyUTJjSzBoQnpUS1JuSnVuTlRQSlJvejRUeTRnZTJFMmw5UHZkYnlxNzIzVlMw
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBaENnQXdJQkFnSUVVcDkwZURBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBPVFV4V2hjTk16SXdNekEzTWpBME9UVXhXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDZnpaSkMwZG1JRXFoaE1nNkUzQUtxMzZHR0lKRW1FdUJSR3A3eERBY3hVdS9wVGhGbXlzZm5DU2FTRnpkbzJVYXdoNHAyUElLbUZmSUdlNEdFNDZGS2RVZndmd1ZiTEFHaFg2bGlFVVFaWFcyS3YvV2JYOGhwbkkwejkyOStPRTNuRGVrLzFXdG9pSnI3bjZSWUZTY1JibU5sdWJzMzloYVFrcjdJbWo3SGt3SVZBTXY5dFVEOFRuajF4Z0dtSjR4bXlqT3htZ1BoQW9HQUl1L1hibkNXdVFqbG9qdWJXMDZ2WjBxbFZsNWl1dGNGSE9GMFNJWGVMQzk3UzFUaXkxYTJMMzNldFFMY2VNenFsTUZUOWROMkRXclZsTjdJSVRoVS81YTlFREtIZXVzUWJJOGRKMVFsNUNadHE0TnFBT0V1Q093MTBmVWNWRE9yVTNZT1V5alFiVUxhVXhCbS90UE4xMHp2VHdYSk1oS1lvMlova1pzM20vMERnWVFBQW9HQUhuaVNuUFJ5SVhYbTRYY0JoTWl1cUl1SFVRc2VWOU9CdElkZWNVRWxMVXVQcUdNdlNvZzhMckUrbGVENU1ZQmpxdnZwS1A2YzdxSFFET1hzY2JYZlFrVDZYWkxXcTJHMlFIRURrdTR6MTBjell1V2ROQjJxWEtyaDR2YW9pNklrS2QySXhycVRuYWRlWkF3a2Z3eVl3V29oWjRqR081K3FyODVNWEtJbkxBY3dDd1lIS29aSXpqZ0VBd1VBQXpBQUFEQXNBaFFuU1BDMmdDU0dTNnE1Y0Fob1h6Y01vN3ZPZGdJVVBha1FxUkdoOURLWHBkSkhybGFmaU1qRXNzZz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUmFmUzlGTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBPVFV4V2hjTk16SXdNekEzTWpBME9UVXhXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUSXlnRndBTDlIbzArdE1EOGtSR0dZc2ZxVnNQNkZXeUxxSDJWU2k2clEyY0swaEJ6VEtSbkp1bk5UUEpSb3o0VHk0Z2UyRTJsOVB2ZGJ5cTcyM1ZTME1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUl3VmlUbXNKWTBoa29wOGJQbXUyLzNRMlpHYmQyMC8xam1XQ0hPS1NMWnNBbDhRYTgxc0hBVmtFQm10VG5hbC9pMFFrd3BDSU5IZWhuMTd6ME1Wa2lKTHNzTXZNclA5dWZlYVMrWXhnblJ1V1k1SStJZnBRM002T3NmZzJ6bnVZRUMvbGlFWXFyaXRJK3lhVnVyQXlOT0gya0YyaVQ1bHJvRno0VzYwcEIwLzBBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVCN2h2N0RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFE1TlRGYUZ3MHpNakF6TURjeU1EUTVOVEZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTJJbFlmdUkzR05xcEZnZnhaOTlodG9GMU1RUXhDTWhJVmFqVWExNER3c1l6Mkhpb050R3B1alZIT01kMmcrTUZFeW1ZZXBkUVV5ZmI2dlI2c3NMeWFSVHROQk9Fc0paSUFTZTFKN2J5VDdrdHFEN0lJWmdkLzA3TUhKNUs2bGhkN3JKUDdEcXJ0Uk9NZlR0OUptWFdoWGFkMlBqL2wzODQrS21HbzNDZkRCMkVCWVBTb0dBVTkrQ3MrZ3JXNS9HWEFDTGx3SFFOdnlYQmVWWE1hOWRZZjY2NzZYTHpnOVZVWmZSV2YxM2hnUDY3d3VWdkNuamlXRDdtc25ia2l0NG55TElkOTRvK0ptSng3NmlBTnZoWWhWVzl5dVNaSWhFVDlzNVBxR0t6NlNQQjBKS3hFd1VmOWU2NU9IMEhsaG91UE5rOVNtS21wWHArR1ZHRUp1TlJDUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUEwMFRkbi8wVnQyM2lzUFZ4MkgwblhsNXJqWWZuRi9ZRVdSa2s0U2F1VW9UOVhVMWdQbWxPN3BFQ2dIcFkxaGc5MkxOSVJVTEZZMXNUM25idExYcnczeU9RQmtLQ0l5aXdjL3hHV1ZsL1k1ajlPR2k0S1hPZ2YzRzVNM2lTdWVHRUx5L3AwT3htaHZXLzRwUFJaSit6c0JSbUg0Q1V2SHU0eXhaU2lBVHlrZDVlaHMvdG9CYTVVRU9mN0phU1RtYkxMajViTGdJSnBrektGamdoTEtoNk5zaFp5bWh6UitBZldPaS9YSEM2NEtVelJOUURacjZZb0RnTmVveWV6UkRXWmU1ZEd6elZqVGU4WTlGWDlkMEZFTzZuWUJLRjJzOGdZSmx1RzZoT2s2ZDdYc0Y0TTR2L3A3OFZrdk5Ha0dSM001QUtrWTgvTXRvWDhlSGF1dW11d1E9PQ==
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router lsrp4 1 enable
     router lsrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
    !
    end
    ```
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz75r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQXhtMmFsWnd0MkNvZEp3Yy9qQ01ZQWRQM1hrVEdxeUY2dWhpMjgvTXAwbHpvTWpLaEZTWmNUa2RrUHRIREdXUGJ4T21qY2hXUGxTamRyNXJLcHJtdnhKMy9TUUpYcWhFeUg1NDRFQUhXMjBVYmRLMlUvcFVGTjRNRUV6amQ3Ykp1UDgyajFMQzlMajRML29VcFlsL2pxeGgwajBmY1R2ZWZQelk2UkxJUjV1dVAzYUtjcVlNUGVZd0JVbEVCRG93Smw5NUdTRjgwR2VsNWZhREZ2SkRnVENIcEQ4RUJ5VlZsMUFISkhGZGRsalhMU3hJUExlR25nYmZteGk2L0o0Y3M4emphNVMrOGRQQzVCQ0g3aTZ2QVVrTVdyRk13eHRFa3hQaTdBOEkxUDNWNFp5a1A3bmJtaHhvWU03RGg5Zm1MN3NrTzl0MWJGM1lpcUFmWFk3ZFJ5UUlEQVFBQkFvSUJBUUNIUVM2ZHpGZHpnVUZkMlJMMzh2UHFTeEhTc0E2N2w1YVFRMGh5QU00QkZsTXY1RkxvbDcxVG5sWTJlOFVCQ1pCRUtQM0FSZklaT2tIaDhTRXhoR0RMSk9kZVhMcGtzbFA0T1dEOWlFTnNNeThEMlU0Mk9sM1QrUHBPSC9VbWtQbVZoQmFvWTlDUU5McjRRc3h5d2VudU5qMDliVDQrbFl0M0N2K3MwN1JnTWYyK21rTXQzZ2k0N1JEZlJ4SWVEN3lOaklDN3FydE56Rzg4SEpkeU83SnZVaEZlaDVxMFAwYzh6WTdnRDVUSVl6WFUrMTAxelkxQjFqcWlxL0ZWc1pLaVl4QmJaMWt0ak5lQkVTN1dSK1ZxamI2ZUFuejN5RmM5cHlRY1pqQVJwQXl2dHdLQmRVWmFzWHN3bXJLMUpQZlhiRkY2bTBSTVlJam12cFA0OG9BQkFvR0JBT3lnaTRFRjJSZkxmRzYwZ0FocksrTFh0NGtBVzJvd0FCS2ZxcXFzdGxtbkpCTDduY2dVUExrcXVla1hmT1lKL2JlZERoelZpcXlUVk56Q2JEQWJPNGdZYnFPNi9lQTgzMy9PMFNZaCtaRGU4NEVPYkZ0MXZzbWJXMWNOSExucjhXWmxhSitsSHFEUWY0dm4zSGp5THhSOE5KeitXTlpFOHd2U0twTnFjd0RwQW9HQkFOYXNjc25PQkp5WFlVMzJFWnJtcW5PYVVxdERYVlNYdG5CYWw3eGFNbGE0Q1pHVkdFTG1kZHVoRjhNbWE4VE1GT0MrbXNQWjdiT3c3eW1ZejZYSEpPY2Z6TnZaamZ1a0MxT0pFaldsS2lRb2tLSFdBbzEyMFZwbENpQVhtSkxZaVFmOXNqYS9mVVZCU1Y1QmIxa25PeXZxVGNyZTlHTTRRc2lzWUppK2pEM2hBb0dBRUdZNEJPTWczcE5OdG1ad0VTVk1UMVpmOC9EQVpTV2FlNi94Smc3K1BFeG5KYUdtbDcwL1VCM3o4SUdlT0ZzczZGTE1MWmRuR3ZyREFPSEFtYnpwYlU4MEs4akQyNHljZU1FZW9hUHRKZXN0dVI0RXlIbnFsUkpkVERVdWJudzVxTDBTZVMzNloyN0x5Q2h6a1RaSHFRWEtwNjdBL1dpZDU0M1RRWkE1RkRFQ2dZRUF5QldGQzVpc2JiTWVhMGFORkI0b0FvVjB4ZEdNdkpxRzNXTmloNWhkMEx2Smwxb3FlYmhKWTBKYlhuV0IvclBrUmJFQm1NZVhLR01pRmxncU9hNUtNKzFNeUNDV21GTkdoejU3cldwYXc4YlhQeSt6dzF4YU5uRjBKWU00bnEyWjBzdmZmZTJ1ZVkwbkwrVzNQWlkyTFhFOXZuZGR1dGltVGxsejB3bk90cUVDZ1lFQTVsNFllWkNLSjlQVEJDNkdxU1BIdnI0cVFBUTdGaWZrQjVpOWxkS2MyNE0yMkhKS2prSXhGV1VBa2hrVlc2NkRmY2tLQ21TcDcydVNhNmpLTWtHTFc0MGp6cjNDL2l3L3FFemJRRzBSS21TbFJPMkNoLzM3SmlSb1JWZUVGdDVRY085NnpUVGNYenh2dFQyR0FtVFVhcDVDdkZLRnIrcllBWEZvdUFQbnIwTT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0FvcmZvUERDOFNYZnlqWTZWZjU5Zmh2YThCUDllU1krSmg3RmROV1dJZitjYUplUGNleUxMZWp4NWV0dFVSUEJkbkRSbGZkQWsrNEtacndoS1d0cnB3dXhEWW16OTFJL044TXJVVUVoL0lQb0Fzck9Gb3lBeGRGenhmdENVdXVDM0xyU1B3VEZ2citBSDl3bi82bUtjbDIzNEpoY2hHRzNJekw1N3pkU005TEFoVUFxbzhobENCY2VMWmNiRVlKOE5IT1RLRmRVTEVDZ1lBSGpQbVlDZk1oZEg5c0MxUXZOUUJaUmNBNldUaUV3RTV5NFpxU0JpVmNHWlJzNmpmbHhQMTc4TjV3VFVVZGpQYU9uUWZWZExFZ3FhN0FieFpzWXlSQUN2ZWZZK3ZPZFBYMC9leThDQWJ0ei9xYzlxemdERjBsaVg4Z0RCS29KK29NSGs4Q3ZrYWRzZWVlaWExYzZkMzNxWWgyNUE0RkRkcXpyL0dBdzhxOGlBS0JnQURtK21zc05kTVhRQ2FRUnV5dlVHdkY3RnNTUTFUT1kxTmZlWERDc0dvOFFoREJuUnBHVWJkNkd1amJwKysybTA2UkZoL1Byc0lnbTUrMDFwa0lIaXlSdzF4Nk8wTTZLODRFcVRTYUF3VGhIZzJ2anVqU1BKdkRhWjBMWHhrR3kwZDdSRlh4aDM3WEk5MjlhSGNYNjJsNW1jaVNzcUZHTkZnUy9qMEpacWtxQWhVQXNjR05oRkdpVlBuczd4K1U0STZwUkxJaUQwbz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMXlqOHhsWFphOE9vOEFodmd0SXJtNkNQcjdLNHVtRU8zM2Y1VWIzeVI2Z0J3WUZLNEVFQUFxaFJBTkNBQVN1d3VveS9HQUlCNzVQNy9MR2JuTSs4QWUrWS82cVJ5RVE1dkwwcGhNV0RhTmNnNjFFcDJvbkEzT1cxenhhVEowREJOKzlzVk0wcTJQNTkxcm15MklK
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVWbG1xUHpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBPVFV4V2hjTk16SXdNekEzTWpBME9UVXhXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0FvcmZvUERDOFNYZnlqWTZWZjU5Zmh2YThCUDllU1krSmg3RmROV1dJZitjYUplUGNleUxMZWp4NWV0dFVSUEJkbkRSbGZkQWsrNEtacndoS1d0cnB3dXhEWW16OTFJL044TXJVVUVoL0lQb0Fzck9Gb3lBeGRGenhmdENVdXVDM0xyU1B3VEZ2citBSDl3bi82bUtjbDIzNEpoY2hHRzNJekw1N3pkU005TEFoVUFxbzhobENCY2VMWmNiRVlKOE5IT1RLRmRVTEVDZ1lBSGpQbVlDZk1oZEg5c0MxUXZOUUJaUmNBNldUaUV3RTV5NFpxU0JpVmNHWlJzNmpmbHhQMTc4TjV3VFVVZGpQYU9uUWZWZExFZ3FhN0FieFpzWXlSQUN2ZWZZK3ZPZFBYMC9leThDQWJ0ei9xYzlxemdERjBsaVg4Z0RCS29KK29NSGs4Q3ZrYWRzZWVlaWExYzZkMzNxWWgyNUE0RkRkcXpyL0dBdzhxOGlBT0JoQUFDZ1lBQTV2cHJMRFhURjBBbWtFYnNyMUJyeGV4YkVrTlV6bU5UWDNsd3dyQnFQRUlRd1owYVJsRzNlaHJvMjZmdnRwdE9rUllmejY3Q0lKdWZ0TmFaQ0I0c2tjTmNlanRET2l2T0JLazBtZ01FNFI0TnI0N28wanlidzJtZEMxOFpCc3RIZTBSVjhZZCsxeVBkdldoM0YrdHBlWm5Ja3JLaFJqUllFdjQ5Q1dhcEtqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNVV1NrLy8zeGs5M2cwS1BJYldRMUU1ZmhpYWdJVUw2V2RmTGZ2c1loOE4wZzhhZHBFWS9sQitZRT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUS93UFc4TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBPVFV4V2hjTk16SXdNekEzTWpBME9UVXhXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTdXd1b3kvR0FJQjc1UDcvTEdibk0rOEFlK1kvNnFSeUVRNXZMMHBoTVdEYU5jZzYxRXAyb25BM09XMXp4YVRKMERCTis5c1ZNMHEyUDU5MXJteTJJSk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU1zdTNHMEVxYUt1aXo5VFh2MHh4Z0x3dUh5YkxLSEZIMTZsdmE1emNQeW1BbDhCbmFwTkhMZmorNmU1NURQVjhRR2czRHNpYUR5V2ZhUjd2d2NxR2FiVU9yMWY2RFZBMHRBTHkxYit1UU5LcytTckZ4TUxtc3pQbkVBdmdjNWV0aHdNeW9sdUdqRmRpM3EweFNxRjJrNGd5aUlmQmIvY0drVUxPZ1ZONVVTT3JnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVCaVVvVFRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBek1UQXlNRFE1TlRGYUZ3MHpNakF6TURjeU1EUTVOVEZhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXhtMmFsWnd0MkNvZEp3Yy9qQ01ZQWRQM1hrVEdxeUY2dWhpMjgvTXAwbHpvTWpLaEZTWmNUa2RrUHRIREdXUGJ4T21qY2hXUGxTamRyNXJLcHJtdnhKMy9TUUpYcWhFeUg1NDRFQUhXMjBVYmRLMlUvcFVGTjRNRUV6amQ3Ykp1UDgyajFMQzlMajRML29VcFlsL2pxeGgwajBmY1R2ZWZQelk2UkxJUjV1dVAzYUtjcVlNUGVZd0JVbEVCRG93Smw5NUdTRjgwR2VsNWZhREZ2SkRnVENIcEQ4RUJ5VlZsMUFISkhGZGRsalhMU3hJUExlR25nYmZteGk2L0o0Y3M4emphNVMrOGRQQzVCQ0g3aTZ2QVVrTVdyRk13eHRFa3hQaTdBOEkxUDNWNFp5a1A3bmJtaHhvWU03RGg5Zm1MN3NrTzl0MWJGM1lpcUFmWFk3ZFJ5UUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFnRFNPMysrRlNIdFFiQVZqVU5hRUl3Z3puU3ZsYU5wOHVZUEJzbElUNHpyLzJ5QjYrNEovWGZSUnRzM0hKMjdJYVphSHVrL213S0lNVnJOZEJ2ZGRnaE8vTlpJV3FzOU4rV1BLVzMxUXF2Z01oS3BuRGZ1bGRTam5EUE1lak5WMDYzbnhydWxWdFlQUmc5eWlQRnNYZ2pwSXUvaHl1NXE4aFpxNlZ4dnN2N2JpclMwSDVQeHcrTkdiR3hWc3VRU0tUZ2ZpUk92ZFIwVno5NGtYQmh0N0lwVHBFRlB3MS9BNkd0aTdxMDNqdWJKNkZBeDM3M0N0YkVOK254UFpWcDFGUUx3YlFaWTdIbnJsVUpXYVpRS3RKNlJNZmd2REFudzc0anlFRjZCNDExSFBUbE53RFd0dkx3NWI0Umx0eGNLRTV3WTlYN0xlV0QrbnQ0VmNON2t5MGc9PQ==
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     redistribute connected
     exit
    !
    router lsrp6 1
     vrf v1
     router-id 6.6.6.2
     redistribute connected
     exit
    !
    interface loopback1
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router lsrp4 1 enable
     router lsrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
    !
    end
    ```
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:05 |
     |___________|_________|______|___________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer      | ready | uptime   |
     |-----------|---------|------|-----------|-----------|-------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:06 |
     |___________|_________|______|___________|___________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 dat
    r2#show ipv4 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 4.4.4.1 | r1   | 1   | 2   | 7   | bf1864f4 | 00:59:58 |
     | 4.4.4.2 | r2   | 1   | 2   | 6   | f141cf47 | 00:59:58 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 dat
    r2#show ipv6 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 6.6.6.1 | r1   | 1   | 2   | 6   | 58f0e2a5 | 00:59:58 |
     | 6.6.6.2 | r2   | 1   | 2   | 7   | 542fdff7 | 00:59:58 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 tre
    r2#show ipv4 lsrp 1 tre
    `--r2
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 tre
    r2#show ipv6 lsrp 1 tre
    `--r2
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:11 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:11 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:11 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:11 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:11 |
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:11 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

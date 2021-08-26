# Example: lsrp tls encryption

## **Topology diagram**

![topology](/img/rout-lsrp14.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz74r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXV4VVp6ejVLSU04SVY3d3g5WnVsQUpDS040V21tQXdrYUdYWmlJT1MrNGhvSjlKLzRPbDVqMlpCQUhaYUFzOSt1a2IyVU90VXk5MlFucjd2aWlueUlPUEV6RGRZa1V1dGI4SFl0YUxTZ3RrSVhsQ0doeXVlUWRFZTArZnpiVjRSWDd3MXJ4SXpqbVg3Z3RaUW9Pd1hoZFR5N1NHcHdmZUZZYUZGSDRtZXVzUFJubUtoM2pJV2VwOGFyakg4U0ZINm1sRndYVjV4eXJUanVFTjhkdkxLZzBrcGJyNzA0N2ZqZDVIZjhaZnFTaGFacm5INE1LSmZ4QUhXMFZWNUVQbkZNM3dCcHlwaldhTHBueVZhWUtPNkVxNGs3TjRiREM4L0ZsQ01JZlo0VlVxTWdKbWpuR2RWVHVHNUdkSGRwN1plcmFSTXFreWNPUXAySTNPeVZjZmc0d0lEQVFBQkFvSUJBQk45dzA2Z1FzRGdVUkl5L1ZHRmdjOXBQNzFCSTNZNzdaOGkzV01uc2l5YXJaOVlneEkvd1BaN3hOSHpnclZBUVFmUFZPSmhZbGhMSVVJb3luUXVvcGRpbzZKVE1kc1JjMlJ0WWRLcXdCdjUyTEZhMm1sQzFoNHRWM1RrZWF3dlhNZ0lwOTh4bWtWL3dwQ0RHNnRvYlpyMzhNZGI5bi9LOWc2UjZzMjZYTnRBVmZCL3hwZDhQcjcvRzdKMmdLN1NKUGxlaW8rckFGZ2Y3L05pR1dZYmltRUd5ZUxuZzVmSzdXWkhtRHNaOFJFdmwyZUE5QzNLbnZQblNpcWV0a3dNbUtZWnVWZERjZGk1KzJiZGpIRkN1Q1czWmNSRWlqY3JVVTAyM3VkRFdIOXUydFJxaE1rMlgyQ0hDdkJZUUNFTTVPYTM2YzdFZENwTXdub0pjZmlXc3FFQ2dZRUE1cUw4aWRuY1poUHFaZjl4UHVxMmpCbk8wOHdsM25lclB2U2JPaFI1Ni9ZL01WWmxCRnNGQVdDazI5NlB5ZVh4M2ZqdkUxSEw3cUpqZDcwVFlSN2FEU3JYa29rSUJoajJ2UnYxeGliczFyNjlaNGt0NVd6dVhSZmFBM2lsSjVqY2hwcHdnVXF1b2hSait6S2pWTFJLbVFKYWFDRmxRU0pGTS95Rm55RzNQTFVDZ1lFQXo2ZnpabnEwaVcvdlBrdjlYQ0tRQ3FQRmdFbzU3TDFiT1krS1lzVkVndVhISDNsVWNtOUNYRVU2d2ErcmNEVlQ4NjZaWnNySlhkY21LdEZXbXVxcXR5N0x2MUNsR053TWMwUlAvNllzdGxJQ0FYMFl5OER3ZXhnWi8xdXl6aWhJY2c0bS9VbGF5OTFyS2xyVzd5NmUvU3c3b0RLVjlqU1VmU0s3MWFPZVBqY0NnWUJvVXBrQWtiY0x4VDVsWEtJUTM0SXE1UkdVNCtiTk5qd1RnZmtrMEZaRjBXRE1KRlFWSUVhblZOdTlTSEtwMUlVTzdxYlZpazVBWnR1dk1hc3VaeElpbXBwZ0FmUExMa2VOU3JSbEtQNUFOSTdmNGtFTVliV0FEbVhpNUJOd1VjaU9haFV4cG1KUGxnR1RnbGcyM0VaUjU2cVZKMlh4akZyWkpRUWI4dGc3Y1FLQmdCWHdYSnJiSSsvUlQ2bDVSYzlTSjMyNFI4bUNEaFNnL041YjkvYnZlSW1MMVRuU0M4WDdVenVFWk96SnJvY3dXeXBIckJWY0gySTJ0T1daTUZrMXFjdW91Z1lBY3pEcExyZU81QlRTYmE3bGd5aTlHcjJNS053WWM4YXkzWFZDZEVUNGtjMzR6Z3J6M2JxZjFrMTIwMzFVQ3dpbHo0b3ZpL0NjbHRPL2NaeUpBb0dCQU03YnZhWE10WUs0dEVzVEI5Z3hoY09lZGVIc1dHT1hLWXEvQjdZZ3kwUVNidndaMVQrd2xuTXQyYmtUeFdFcXFaSG56ODdPd2N1YW1EVUF1QWFwZlNsMzgyeGZVcHRmaW5tQ1JSRUhZSkxIN0ZxZFlpbnBPZzNaWS9HbWVaMStYYTNlYzg4VVNCV29ncmloSDk1dmZJSk1GTUhVRTloVUh0MlR1TElmY1VQYw==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0VLcmFXNGZkR2R1T0ZiRC9naFZ6b0ZndHRwUkUrcndVS3hJYlhGdGloLzJiU01zWTR5ZzA2YUJhbE5NQmNzdUh5MWdCcEE5V3NZODhEeEY0TzVQSVJBdE02eUtyalBSNnd2VHlnWlIrcHd3eFVJOFczUkFiRXNzaVkvYWlaMXN5dGN3QkFxS3B6TXpUMUNRSFVUSThXU2QxVGNvWm5lTm1FakhiVGZYWEZuZkFoVUE1Y0tGU1BzOWZKa1dZNUV4M2IyTUVraWU2NkVDZ1lBcW5wOVJnbnNrS2F6YnpacG0xb29ZY3RuVURSUUYyZFRwc1FSVWxDWXMzY1FXL2gvT2JYRzVOcVRBQ25mNGJCYXIrMEU5ZzFNb2xKWE9lU1daS2dQYU5kQUpqazM4dEdTMnJ2UWVjSkczS1JBUDVmTkdqZSt2RTNIQjVVRUtManJ4YWRRQkl4Q2NRWTdKOURnbWF3RVdoK1o5eWVNeGxkalIwbkFhd1hwUzFRS0JnQ1cvc3JRMlhRY3dxbkFNdHFqTDhDaXM5WGU4cFRpQ0I5TjVXTm51cU1Jc3Q5SG9LS1A5SmlhbmZQcjZYcVY5SkZFNnp6cDlkQXo3QW9GY2hyRzg4U1dhNkJXZ0Q1Qnd0WlRhZy80SFZyTHliYkI5Q3E3eFJGOGp2eWpxaEtDMzd2dmkxY1IvdkdJaElPeitTNDl2WnB5bDFIb0ZzdjZQMW1aS24xN1lsK09XQWhVQWtnZHpoY3BLNlF2RW80TXJ1a2JnVXNyeHM0UT0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMjFFVjNqdmtaejJsQ3pxZEkyWWUxOFRGd1JnTmFqVzFVanhJQ1NJS29DZ0J3WUZLNEVFQUFxaFJBTkNBQVN4c0dCN1RXMXVFRVJKczB1MUVSRkdHVkU2QVc0OTAyVFBGOXNrTUFLR3ZSajdaeGgrYTBLQnZzVE9TcnNleFFnSVg1SUxLT01hUlVJMVJKd1I1SjFS
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVKeGlFbERBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFOekF5V2hjTk16RXdPREUxTURnMU56QXlXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0VLcmFXNGZkR2R1T0ZiRC9naFZ6b0ZndHRwUkUrcndVS3hJYlhGdGloLzJiU01zWTR5ZzA2YUJhbE5NQmNzdUh5MWdCcEE5V3NZODhEeEY0TzVQSVJBdE02eUtyalBSNnd2VHlnWlIrcHd3eFVJOFczUkFiRXNzaVkvYWlaMXN5dGN3QkFxS3B6TXpUMUNRSFVUSThXU2QxVGNvWm5lTm1FakhiVGZYWEZuZkFoVUE1Y0tGU1BzOWZKa1dZNUV4M2IyTUVraWU2NkVDZ1lBcW5wOVJnbnNrS2F6YnpacG0xb29ZY3RuVURSUUYyZFRwc1FSVWxDWXMzY1FXL2gvT2JYRzVOcVRBQ25mNGJCYXIrMEU5ZzFNb2xKWE9lU1daS2dQYU5kQUpqazM4dEdTMnJ2UWVjSkczS1JBUDVmTkdqZSt2RTNIQjVVRUtManJ4YWRRQkl4Q2NRWTdKOURnbWF3RVdoK1o5eWVNeGxkalIwbkFhd1hwUzFRT0JoQUFDZ1lBbHY3SzBObDBITUtwd0RMYW95L0FvclBWM3ZLVTRnZ2ZUZVZqWjdxakNMTGZSNkNpai9TWW1wM3o2K2w2bGZTUlJPczg2ZlhRTSt3S0JYSWF4dlBFbG11Z1ZvQStRY0xXVTJvUCtCMWF5OG0yd2ZRcXU4VVJmSTc4bzZvU2d0Kzc3NHRYRWY3eGlJU0RzL2t1UGIyYWNwZFI2QmJMK2o5Wm1TcDllMkpmamxqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGSGxEdFhWWmoyNDNaYkNNQkhqek1WYnM1L1V5QWhVQXFpT09LaXhJREFZUHZQdFZRSHAyNUY4Sk5Qdz0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUXBQV2htTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFOekF5V2hjTk16RXdPREUxTURnMU56QXlXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTeHNHQjdUVzF1RUVSSnMwdTFFUkZHR1ZFNkFXNDkwMlRQRjlza01BS0d2Umo3WnhoK2EwS0J2c1RPU3JzZXhRZ0lYNUlMS09NYVJVSTFSSndSNUoxUk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUlVdjBUNUFuRkgzNVFzcmFaNmNaNWpwTmV4eW9kU0NkZ3VxYnoxZERCN3BBbDh2UTYvT3FoZ2Jwc0VtQUhFZlFiVWVLZzdDTUJLeElPL2RicnN6TjUvWStkU1N0djZPWWJGdmY1dWZTUm1lVWZxWFh5WEZmaUp3V3FDYUZ4QVorWlFFNEg1Qm1OQ1pqNnRFbUZIbDR3QlhXaW1SYnVBNGwyeDVkQ1lqY0l2SzhnPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVFMktONVRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRBNE1UY3dPRFUzTURKYUZ3MHpNVEE0TVRVd09EVTNNREphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXV4VVp6ejVLSU04SVY3d3g5WnVsQUpDS040V21tQXdrYUdYWmlJT1MrNGhvSjlKLzRPbDVqMlpCQUhaYUFzOSt1a2IyVU90VXk5MlFucjd2aWlueUlPUEV6RGRZa1V1dGI4SFl0YUxTZ3RrSVhsQ0doeXVlUWRFZTArZnpiVjRSWDd3MXJ4SXpqbVg3Z3RaUW9Pd1hoZFR5N1NHcHdmZUZZYUZGSDRtZXVzUFJubUtoM2pJV2VwOGFyakg4U0ZINm1sRndYVjV4eXJUanVFTjhkdkxLZzBrcGJyNzA0N2ZqZDVIZjhaZnFTaGFacm5INE1LSmZ4QUhXMFZWNUVQbkZNM3dCcHlwaldhTHBueVZhWUtPNkVxNGs3TjRiREM4L0ZsQ01JZlo0VlVxTWdKbWpuR2RWVHVHNUdkSGRwN1plcmFSTXFreWNPUXAySTNPeVZjZmc0d0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUhSaGRQa2xpUnhScVhQZEhydlphRkRNVmhJNnpmQjlVOTdPQUY1REZTbEdrNjlXRVAwaU1zTUpGQStyMGZPMlkxbVN4VEk0UkJFQXFMNTZ4eXJHQTJYYThCLzFSKzFJcG5IUFdEYmozQWZmWnJCYUM0aldOV0JNMnVxUTlybTI0YzZ0ZGlubXN2K2pjQjJWTzhrU25WVVNJMEY2a3ZlamlWM0kwVG8xWk5VNTRKVVlGOG5idWRDUVJMSEdwcGRiMGpGbmc0NlJycDEwRUh2dEIzZ3Vya2s3NU9nL0JQSjhVZGFSUG1hUEU3T056WW9jTjBoY0hVK29Ud0RlVVU2VmM3N085THUrbEdPM1RvOEx0UjFYWFQyMDR6S0ZtMWJGTVNOQys5OGN4L0xPU25HK2kydkQydEJmdVd6YnNmL0tPUDkyTFp0SEdkL2VsTzhaakY2Sklv
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
logging file debug ../binTmp/zzz74r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXFqdy8rdDVtZ1F3TFNpTlJaNWN3VWNENE5OS01ESm44ZXJjdGxqZElIK1ZibFYreDA4MGZMZkpMUjBnUWlod2pPdXovc25xNDU3WEJsSDZUdHc3TG9GVTFMajIzamRTbU9qdEdrT3BmUFVQR3Nsa1N3RXdPWi9iRnNRWUNzMyt5T0F2alcxUTZQbGErNzlhWEs0V0xYc3RzM0hSYnVFRDUrMmdlZWxaYnk0L2kvM3VuM0Q1bi9ibmNOVk50eHl3aXlDNC9IV0xjSVZVZk1mc1ljMmgxTlEwVHJldWFiOWQxbW5ERVVXYzRHSyt1VXdGdnJJbTdPa0pxcFpyNXZCYmpyM1d4SjhzQyt4amg0QmViaitqSW5tdWdHbGRyWXFzWUIzTjhtWU51aFRvYmVXNVpEb1Z3bTlYclp1WGhJdHluUWd1Umw0ZUFDUTZidFlVKzlVby9Dd0lEQVFBQkFvSUJBR0JVZWF2ZS84Z1VaYXNOTXpwWVBscDB4TDgzU1ZLMExEL1F1ZllmMEN0a1lSKzBwKzcvU3A1NFZncS9COFR2U1N4R0FpY2Y5TlFCY01vem1pampNV3pINnJFQThZWkxoOGk1MUNPYXpFdmh0MlVpckU2dWV4UnZlc3pDWnZMbDFwYUtlNXdwbkUrOFRJMXhNOWZIMk9iS1hBNmZ0V3NkTVpnSEFnQWVNQkdPcWpHQUVxWkVWZTl6Wmd3Qldobnp1Z241SFFJNk01WnBtVU9tTHd5SVdkekk1ZnArc0RSZFhuaTBmM1Q3VFoxWDdCME1MOURRYWFER1R4amNoRWVKVUY5U0ZqU0RRMW9Sa1Y3V0k1emRzMlNqUGxoc291bzgxVGpJRHdSb2dNUUhNZnZBekk3ZXFXRHlzcTlSTGNVV1JSalo1TmN1TnBuWE1XTHNDNmlQdFlrQ2dZRUE5QTVvSjlwbTl0eHp1MWY5elNrV01NRkpxYURxRzM5UkRKUWNYMXB4bFVkMVVvbytZcCtKdnNMMFgxdVZUTE1oUDBvZUYxVU8vSFJDOU9iVjhOOHBQNis3NWFFWFdvMlE3bzZuREluMWZLWXRmV0RTSXlLNkt2QkUvTnV5UTJwZ0xVL21iRC9JRWdtUUJTdmxyUmM1NEtDcHJtamRJaFJjeXZzZXJiZG9GOTBDZ1lFQXNwRC9YcUt0RTVFL0JZMmtqbWUzNlhnZHFKZHUvKzRBNWtpVVlSQ1RDamppMlByVllkR0ZmZmxNSFA0VnFYdFllN0F3UmhPQ3B5OHpjcUY0QmVvL1FaSWFIQnUrRnVHbDR0RW9GbFpGc0owdUY5SDFKTnZRWUFJcXNtRU0xbFRtUHN3WHRyQ2JPYVNIOXROSWd5T04veFV4OE43YjNRdzIrVXZ2Vld3cWVBY0NnWUJTa1Qwem5uUVBPRzMvQjduWjJ2aWk3Z0daM2RMV0VyQzg3SzdjbzZDaHZGYzQ0WVJSb1YvY3BlQS9FcURrSGdZMWYwSEc2d1B5N1BKcUlGNW82MWJ0TU9zRXVRZEpuM05WQWZZS0MvSjloVXNHaStjTDlBZS8xeUcvMmlQcEl1Zis3SFVzVWpmQnduSnpEWExhcUd6d1RlcWFFdWdkUzM1SlBjUVhTV0Z5RVFLQmdRQ0o4blFsNHR4OFlsZmliV016MURLQy9aVkQrZ0Q1WEI5N3g1UkJUREdiMHdpRWdYcTQvOGoxNGRLSUQwNGl5VFE1RVlxcGlFY0Y2dlArMlhqRWNRdC9GMlJ1Vkl4TVZ2UDFQb21PZ0FXRWhGam9jLzNEQk1GOGVoQU1EK2QvNk1TYXZNYVJEdXhMNHF4YTVTeCtpc2dXeUlQMVJlVnFaaFpPRHZpTThHdjZud0tCZ0JlVno0QVRvRVpPY01xTjFLais4ZzZQbzBKZ0ZBYTZpY3VDMnlub3JSRWZGaXJrbGxLdWlnYkFDamI1Y3JsZzR3Qnh3NzU2SDZKRXRHL3UzVENLcVFCTDJVbm4vc2liN3BNN1ZIc21nb0JTTFRyQzJHeEp1dE9MWDhXUG9wSE0rK3J0YUFzdVhqNWdYajhEYUdwNXhZVUJzcHplV0w4QTFhcitLditvUEk2MA==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDdlhsZVN4dXBjZEhSMkR2b2t0OURRZFdFTnl2LzVOcVpWbll6bmlpNTVVLytFc1JuaFBXRnByV1Azb3lOM0JUTTNMaDN4cFcxUXpSSEhxL1lYN2QxWU5OeUtFemR4WDE4UE0zMWhhUHU0R3BSWmVzQmFWcWpFSDMwa1lwUHpEdTd0em5CdXFMeG54R2orOVFVejRuRHNVV3B1M2o4S1dMdFhlcVBMWlNlcEtRSVZBTmtGRUY5TXN4K05RTUpwNWhjL2J2SFB4TTluQW9HQU5JZzEyaTQ3VCtsVTdJSHRrdVZnUmQzdnh6YXV1SzRPWmNCZnp2SGdBeTh6Y0hVbklOQzhWMUgxWGszQm1FczVkZ2RRVWcxTzc0SGdOcmZmUGVnQThUS01DRTNOblh2eS90bGNOdERmVGUwZ3pFSk53STQ0T0ZJc0JuOEhKZEl5bGxSWGwvSTZrTk84VFovR1V5bXJOa3Bzc2JyVHBYVFdCR0Fzbjhpa3lDVUNnWUJId29tWGRZR29UQlFpNGFzcHd2eVZjSmdndFErK3hwM0ZwWW5hYXdFb3QycXVBZFozcXhIWDYzQ3p3di9iZG9qcEVOTjljbVBycXFySVlxbGUwU1pqUVJvYXQ3aFo3aXp2YmdCZmI3cUdQUDlIdDlGZk5tN2VSaUl0N09FNkowQU4wcWh2UWFreUR6UU81UlRiMUdwcmg2K3RjZUMyTTZlUFoxRnBZTzZJTEFJVUVxVmZFVTBPNGFqOWYxVUtLdm5uaHNzcHpIWT0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURQL3NIUWFxUmdjaTB3WmxaVzZpa05jT2xYVXVwSk8yWWRwT2k0NUdIT29BY0dCU3VCQkFBS29VUURRZ0FFVUVpTU9OV0F1WTNJUmIxMURJUVBvYnBIY3psdTRlWGUvZTZhK1JPVmx3aC9qanJHUEh5K25pMWkyZHc5ekRvTElxcFBhMDZ6b1VDd0NuSkpYdmNSV1E9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBaENnQXdJQkFnSUVISDUwYnpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFOekExV2hjTk16RXdPREUxTURnMU56QTFXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDdlhsZVN4dXBjZEhSMkR2b2t0OURRZFdFTnl2LzVOcVpWbll6bmlpNTVVLytFc1JuaFBXRnByV1Azb3lOM0JUTTNMaDN4cFcxUXpSSEhxL1lYN2QxWU5OeUtFemR4WDE4UE0zMWhhUHU0R3BSWmVzQmFWcWpFSDMwa1lwUHpEdTd0em5CdXFMeG54R2orOVFVejRuRHNVV3B1M2o4S1dMdFhlcVBMWlNlcEtRSVZBTmtGRUY5TXN4K05RTUpwNWhjL2J2SFB4TTluQW9HQU5JZzEyaTQ3VCtsVTdJSHRrdVZnUmQzdnh6YXV1SzRPWmNCZnp2SGdBeTh6Y0hVbklOQzhWMUgxWGszQm1FczVkZ2RRVWcxTzc0SGdOcmZmUGVnQThUS01DRTNOblh2eS90bGNOdERmVGUwZ3pFSk53STQ0T0ZJc0JuOEhKZEl5bGxSWGwvSTZrTk84VFovR1V5bXJOa3Bzc2JyVHBYVFdCR0Fzbjhpa3lDVURnWVFBQW9HQVI4S0psM1dCcUV3VUl1R3JLY0w4bFhDWUlMVVB2c2FkeGFXSjJtc0JLTGRxcmdIV2Q2c1IxK3R3czhMLzIzYUk2UkRUZlhKajY2cXF5R0twWHRFbVkwRWFHcmU0V2U0czcyNEFYMis2aGp6L1I3ZlJYelp1M2tZaUxlemhPaWRBRGRLb2IwR3BNZzgwRHVVVTI5UnFhNGV2clhIZ3RqT25qMmRSYVdEdWlDd3dDd1lIS29aSXpqZ0VBd1VBQXpBQUFEQXNBaFFseFA5L0JYRG5hOXhVYnVWVzg5NFFVbXJhblFJVUFvYW1CMmVBQ05hYmo4U3dUczMxMjNmRHlpZz0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUU5abEt4TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFOekExV2hjTk16RXdPREUxTURnMU56QTFXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSUVNJdzQxWUM1amNoRnZYVU1oQStodWtkek9XN2g1ZDc5N3ByNUU1V1hDSCtPT3NZOGZMNmVMV0xaM0QzTU9nc2lxazlyVHJPaFFMQUtja2xlOXhGWk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnT0F4bDJQczJDZUIyRG50Y2NnT1RwbGoxSm11dHJxZzVlSUNTdmI1MzdVNENYd1VWcTJNc2VvOTMyRmJmeUV5bGRnSEFwNERuTFk2RENNVm5tSmhZL3ZUM3ZvWUxrZ0p0YW1rUFpuMmU3cWtLK3h1eVpuSXFCeVZKWEhDSDE3YzRObHYwaWpqMUlFTlNoMlRvOGQ4dGgydm1QeWZ2TmViVU5KR0ZnQUJSOXVlcA==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVNYzNCdHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRBNE1UY3dPRFUzTURWYUZ3MHpNVEE0TVRVd09EVTNNRFZhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXFqdy8rdDVtZ1F3TFNpTlJaNWN3VWNENE5OS01ESm44ZXJjdGxqZElIK1ZibFYreDA4MGZMZkpMUjBnUWlod2pPdXovc25xNDU3WEJsSDZUdHc3TG9GVTFMajIzamRTbU9qdEdrT3BmUFVQR3Nsa1N3RXdPWi9iRnNRWUNzMyt5T0F2alcxUTZQbGErNzlhWEs0V0xYc3RzM0hSYnVFRDUrMmdlZWxaYnk0L2kvM3VuM0Q1bi9ibmNOVk50eHl3aXlDNC9IV0xjSVZVZk1mc1ljMmgxTlEwVHJldWFiOWQxbW5ERVVXYzRHSyt1VXdGdnJJbTdPa0pxcFpyNXZCYmpyM1d4SjhzQyt4amg0QmViaitqSW5tdWdHbGRyWXFzWUIzTjhtWU51aFRvYmVXNVpEb1Z3bTlYclp1WGhJdHluUWd1Umw0ZUFDUTZidFlVKzlVby9Dd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQXk3dk1MSlhNZitoL0FKbmRxZzlEQjhtQVVlejE4dHJJajRqejgzdUN1WUNsbmczK0p3eFZQaFZRaDFpTUZtbFNNeS9JczZvWkZ6Z1NBNFhHS283WFU5MlNBV1pqTW5GTFNTL0tuakU1OWVNbWV1d3pJTmtQODBQR1VzcHg0QThEQ3RONEhzazd1dHZBU3l5eEtiNGJUc2YyRmMvdlc1eldnVTEwalIwczNKTlNTTDNxeFJ2RkR4UG5pa0xoVlF1cnU2OVV2YysyR05lQ3F3YmNIZTI4b1JKaC9DaWxURlZjRTFFN1I3enJBTEM4enU0SVBQZTBrd0dicUVKSllWcTVoYVNOVFJlcWphVmpTUjhINzdPdGZtWCtwT2JtZWE4THFmRjhDTEluYm9yZXpXQnhiMzBjRWoyUmNuKzhhVlRyZ3k1UlBMdEVjaFV2eVBKUEVkZGdh
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

## **Verification**

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
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:05 |
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
 | 4.4.4.1 | r1   | 1   | 2   | 6   | 55c2a7bf | 00:59:59 |
 | 4.4.4.2 | r2   | 1   | 2   | 7   | efc4fb78 | 00:59:59 |
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
 | 6.6.6.1 | r1   | 1   | 2   | 6   | 55c2a7bf | 00:59:59 |
 | 6.6.6.2 | r2   | 1   | 2   | 6   | efc4fb78 | 00:59:59 |
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
 | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:08 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:08 |
 | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:08 |
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:08 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:08 |
 | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:08 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

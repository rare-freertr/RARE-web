# Example: pvrp tls encryption

## **Topology diagram**

![topology](/img/rout-pvrp22.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz41r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFCeStHTGdpWitQaDVza1c2LzNHcTR1c2puSmtiUlFuelc5UmRDZEFjTGlyZTd5cWVDMndGdkFrLyt4RmhTY1FyS3k0TGNSeVhzUkpVUEZON2IzdTlBZWprbkdyM1M3bk9xTVZvRGl3VEo2anQyS3BHdnkvNGYza3o1c05obTQvK2pWSHdza2pKK1NQRFJwWDUyZXdoT1RWL2tobytHOU43WC9PSjZhMWpvY0tqYUlOeVNGVmlmSWU4WEVldmgwNlZDZjJkZDNLNURmQ0hTTW1ocGlvUmhqRmlBSWlIRU5pdGlnS3hKWXNEdk50VWhITEtpRWJJUWJMWEJCQVBXWU9NNVBZbUgvMzZlV2NDcTdhV1d3K3hSSmdVQnVpMUliQ2tjVHhIM2IwZWNOMndXUlFVVVp0TlBUd0RoZFh1enY5c2RUem9GOENneUVjem9zY3ZmUFhyMWJBZ01CQUFFQ2dnRUFQTlc5ekQ1R1ZmWlZXMW5BdEtwRGZLWUYrZWpGVnR2SDNjMHhZOExvMG5WaXVMaTNGVHlYMEVEL3pUNTN6VzlsaTAxbzBWcWhhaU1qeHhtQ0VYZ3AyZUZFbklOKzZ6OU94TStKQjNOZk9JYWNKNTUxR0hHcUNwQzVPUjB2WXpyV2d0OFlVRkN3cHZxQWFUbVU5OHFOL1N0UndrRXJVNnBFL1RXQ2h6L1FJOUpkZ3NaTnZoeU9IODB5TFovcThhZ1pLeHZwbi90SkVzNzlyQjNkeXk2QkxDU0Q1eEdvai9ZSmhOUFA5ZU5aZk5yM09KQ0Z0d3dvRENqbTZ6NTFvTTNuRk5vUTlBYWlHZm9uMzczWGJmVXFLMG96VC92aFV0ZlJ0KzBpanhlaU9CUStQSVZKMmx4dnhSNm9LUEhJNzhBeG5OTHFUbGZ6Ty9UR3B2VFRnTkg0SVFLQmdRRGpzaWVzaGU0WFVTdEMwdDJRZm0rNGRTb3o5dWVLWmowQWYwdm13ZHhreFhyenFOUVMxOU1EbHZxNDdyVzI1YjF0Q280U21MS2MzNkNOVU5ldzNLVEZUK1k0K0xMRkJqdGtrTlJzNVFnKzQ4cnlzNU9WMmpyTWZGczlEK1RLd2V5WUNNdk1DdmhhN2RxUWMrZFBObENOSllqTjVqMFJSd2NNY1hjQzFFZ2oyUUtCZ1FDQlF3WHBqL296WGRKR3A1bW0yUGZQSjcxd0h5ZE0vR2QzR1p1TmxHeFJ2TlhOYlZJUnYyK2ZrVTZOS2xsZXpEVXY2Z080UUUvNXI0L2dMUlZ1OXVBbGdLS3lZVzdsVGhNUmE5ZTZWSGg2NDE2R1diaDEwbFd5cXlVVkVCQUEvOVVMcDNlMjNTdURyZWhHUnlYV1F2TXZIVnoyUExYZERDT1FFL3ptQXlkT1V3S0JnUURpN250V0dnRnFvYzR4QW9JcWNha2RPVUMvbTdPMm55RHJMdlBSMzZLdG1KaHE0ZmZEYy9EdUlmcHVlQk1KWHoyRXdNRktUWCt1azc2ck9VaFBFQWowVWlhTTMya2tyb3BoTjJ0UHdKQ1FSVzNPcUNWT2M3cW9kTVJtUGtIenhvVHNIZEFuNDBNVk5QdmhmbktwNHVNeldaWllSOERUU0d3QS9kRDBNK2hXT1FLQmdBUFdFbUhaSlFyTE9RZGh4L3ljcWRZYkR0TTZDWGVPY2grbHdla1V3NVkxYlg3NFJKeEVPekxZSkNXcVlSYWdKdC95S1FRWjNJWERnUmlkSGVxNkp2TFYrMzRoeUNIRURHclM4WWNWSkxJNDkwQXpmM2IzdEJWbVlPWmNJSzEyNmtLN1NLRkR0UnZtV0dObGp5anB1Yi9uTmpBVW95MFpSQ0R0aHU3b253MERBb0dCQUloOEtyc2RaZnhnTDZwVmJvSVVEc3grVi9aS3hDT1pLNU8xNTd4V2pLZ3hlSzYzQXNhcnpYaGFYa2xNeW95MmMwWVo5MTBDdGE4UjUzT2t3dzlQVHFWSEJMTlBUd3NoU24wVG5VckJUR0gzTUF2cnJEb2VBZitMY215VVVxTmFXYktIQ1lxNFFrTnNsVEQxOTZsSFVmcysrcHpxeGVtN01DVGNDaTNORFovOA==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0VVV1JvdHRRdUtHdEs4ZTdPc09GdFM4d0dsYmR4S2cwdGxLWCtKQzE0L1JKN3hoVXpkR0VDRWJodklsZGVGTEdZRWRhNjBGMzBIVzgzc2kzVTVYTVhzeExFdytPaWRuK1QrSlBpNTBHcUhsZ0Znb1FQd1M1SlgxbC81b1A0dXBwYndMcy95YTRxTjl4dUNrTXB1eVVBV3hNTlJEdXQ1dCtWWlNOV1Nna1hpM0FoVUF1QWpsRklReDJBTktwNkpFUWl0NkJFMjVNaDBDZ1lBSUR2VVlRNjBKeGxPU3NsTDlwUGpZeHhrcGI1Y2NmR1h0emZjcFNRUlZveFZsTUNXWDRaZkZlYWtpTHNFTTVadHh4c2ZtNEEzT0xPaUVLZzl4dkx2aHFzV0FjL29qdnF0ejUyeko3TUh1My84YlNiclBpRlhpSFJhVDZ6MHBvMHlvWWE1c3dpR0JJeHBqNnRMN1JnUEpyRHoxdVVZa2NWTlV5MnJlM2VxcHBBS0JnQWN0NWRDMTR6K3VQSTM0cGkvSHZSb2FmT0Z0RytsY3VHUFliV0pCY1RQelhsL2dCeUNqcnYwYUhyU0QzWXo0aDFRRG5QWnVqdWdNclpIY0NuS2o5WnVXRzFXV3RaR0tKeW1YanhBQXRReEs4N2ZrNDlwMkhHTXFlZ0hoRDdmK0FlcnZFUmNITjB1eVR5dzU4TXQxM1JIS3E5YlRrcEk3Mm56clpOZWFFaFpuQWhVQXp6U0ZqMTBsaXhlTVRzMy8rTjBmaEwyNFd1dz0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURMNmF5aVB3ck42a2hJUWwyekMzWXUxNDBuTVYxMDFPL3RQdi9RMFpibG9BY0dCU3VCQkFBS29VUURRZ0FFWHN5K01pK1A1eldnYjRDU2NwbGNXRUVRWTZacXhrTVJSLzZXOXFINWRENWpIVW1jUzZnZ0VUS2N4MTJZOThJRDdxSTZiVnFVOWJTclRZYi9YRjZyeWc9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVEdWtMcmpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPRFEzV2hjTk16RXdPREUxTURnMU9EUTNXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0VVV1JvdHRRdUtHdEs4ZTdPc09GdFM4d0dsYmR4S2cwdGxLWCtKQzE0L1JKN3hoVXpkR0VDRWJodklsZGVGTEdZRWRhNjBGMzBIVzgzc2kzVTVYTVhzeExFdytPaWRuK1QrSlBpNTBHcUhsZ0Znb1FQd1M1SlgxbC81b1A0dXBwYndMcy95YTRxTjl4dUNrTXB1eVVBV3hNTlJEdXQ1dCtWWlNOV1Nna1hpM0FoVUF1QWpsRklReDJBTktwNkpFUWl0NkJFMjVNaDBDZ1lBSUR2VVlRNjBKeGxPU3NsTDlwUGpZeHhrcGI1Y2NmR1h0emZjcFNRUlZveFZsTUNXWDRaZkZlYWtpTHNFTTVadHh4c2ZtNEEzT0xPaUVLZzl4dkx2aHFzV0FjL29qdnF0ejUyeko3TUh1My84YlNiclBpRlhpSFJhVDZ6MHBvMHlvWWE1c3dpR0JJeHBqNnRMN1JnUEpyRHoxdVVZa2NWTlV5MnJlM2VxcHBBT0JoQUFDZ1lBSExlWFF0ZU0vcmp5TitLWXZ4NzBhR256aGJSdnBYTGhqMkcxaVFYRXo4MTVmNEFjZ282NzlHaDYwZzkyTStJZFVBNXoyYm83b0RLMlIzQXB5by9XYmxodFZscldSaWljcGw0OFFBTFVNU3ZPMzVPUGFkaHhqS25vQjRRKzMvZ0hxN3hFWEJ6ZExzazhzT2ZETGRkMFJ5cXZXMDVLU085cDg2MlRYbWhJV1p6QUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGR1VEMk1GdHY3WDdTaHF0bWNxaUlDTzJEMDFsQWhRTmNja2FIUnd6NFF1eU9iSGlpTXJkWjVMRk5nPT0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUVNUenJITUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPRFEzV2hjTk16RXdPREUxTURnMU9EUTNXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSZXpMNHlMNC9uTmFCdmdKSnltVnhZUVJCanBtckdReEZIL3BiMm9mbDBQbU1kU1p4THFDQVJNcHpIWFpqM3dnUHVvanB0V3BUMXRLdE5odjljWHF2S01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtlNW5QSStKckpyYmlZdkpmRTNJejV3d0hhWXc5MkQyK1pLZ2tYVlBVdUVBbDlpdFl0YXdoZS9DRHRibVEwWksycloxV0Y2WmdqN0o3Yy9MQm9ybnQxREptRUNSSkpOUDBxZDRSenA0TlVDM2g1T2IxUnBGbGZMcVJoODdtRGUvaTR2dUUyV293a3dWTzUyT1ZvSDF6ZVRld2hnckMvRkY3d1cwdU5BL09yS3BnPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVkZWRnR1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRBNE1UY3dPRFU0TkRkYUZ3MHpNVEE0TVRVd09EVTRORGRhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCeStHTGdpWitQaDVza1c2LzNHcTR1c2puSmtiUlFuelc5UmRDZEFjTGlyZTd5cWVDMndGdkFrLyt4RmhTY1FyS3k0TGNSeVhzUkpVUEZON2IzdTlBZWprbkdyM1M3bk9xTVZvRGl3VEo2anQyS3BHdnkvNGYza3o1c05obTQvK2pWSHdza2pKK1NQRFJwWDUyZXdoT1RWL2tobytHOU43WC9PSjZhMWpvY0tqYUlOeVNGVmlmSWU4WEVldmgwNlZDZjJkZDNLNURmQ0hTTW1ocGlvUmhqRmlBSWlIRU5pdGlnS3hKWXNEdk50VWhITEtpRWJJUWJMWEJCQVBXWU9NNVBZbUgvMzZlV2NDcTdhV1d3K3hSSmdVQnVpMUliQ2tjVHhIM2IwZWNOMndXUlFVVVp0TlBUd0RoZFh1enY5c2RUem9GOENneUVjem9zY3ZmUFhyMWJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFGY1dXQ2dFUi9xTkpwNGZOdlFxYTZ1VFNQRVd4S245VXlzZFM4enRJa2dvV3BFbHladlZqZkFpWTVQQUNzcTVmZmZ6Sk1qbm5lZ0FSbmZjVnRyTFNZL0ozYXRBaWo0VnN5bytCL2d2aFY0c2lDcnE2d1QzNFlwTUF2ZUpGYWdIRDNhOUIvc1VpTnYwQnRWSXpRZzFuVGZWR2dXUzhMdVBCdm0wbzRuV1cxNm9MUFdMMXJCU081cXJiU0k1a3NxQzRQdUM2SHBlTWpCb2VuckxoQllhcHBSWUZuZkRTdnA2dHJJVTRmcmVQTEI5eDdFdllkSkd4ZEJSWkJtZm5WVGhEYk43RWJ4UVloVVRUeTdqNTFHcDZjSjdUU2FYU1VzYi9CSTdWbG45M3psOGt1RGtzRDBaOWRUMHlESUhNUHJWTDRvbnpYTGN1ZXNzeXNZQ3VYc216NEU9
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.1
 redistribute connected
 exit
!
router pvrp6 1
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
 router pvrp4 1 enable
 router pvrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
logging file debug ../binTmp/zzz41r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCd3JrUGNucXFrM2VtRTV6Mk83SS9vUXZPNmowOEt6QWRZSHIwbS93MWh3Q3BzZnk4NDZOSzhIdmdOb2FJV3JCOUVWSjNpQVZyQjFPMUJQV1dWQmZUQVlsdVB4c1FrYjVsQ3JoU3lvYjhiRVMzOVFRd2Jna2tTamJ4bWt5aG5HZTdVa1hJdXBPVXNpVnhna0lEVFVQejQrYmxvNzFhQnhrNXNtNHA3N2Fld256Q0NaZzV2c1ErNHZ2QmFBZzQveFpMdWpSd1ZJcCtaM0dzZ1VvbXpUcHhXV1lNcVZSODAyM25IRkV6Y3Bxay9vcXpXVnhvUXJEZC85SGVnOXhGUnZHbTF5am1VbXh4bk5RTUhpNVA0aGkrcEs1NTRJb0NYOEt3RE1yWUxETDd4RmR6OTNhemU5eitGc3VBMVpEVUcrNDlZS0FEajNrbHg4VmhzM0pGcTlsZnJBZ01CQUFFQ2dnRUFiRTZFZWYya2hoMnJCSTBEOVduYWxPUXR3MGRXTVVtVlVaVVNPUFowMVYxUktjSkNFSkJ4WmxMYUdMZ2d4V3dpRFpyTHV0MlViN1VMYTJicFNnbFVqTXE5dVgvVExqWjZlTVk4ck1xZGx4VzNQN01UUVNuRXRPbTVpbHF1UGhPR0pabTd4NnZGZ0Q1enBYbWY2ZjN4ZWhzR3BSOVA1aU5IWkV0SkcvOTk3Rng2ZU4wYU1PazdDajNLSGsrRHBmb010SmEyelhaN1IxcG5VVGxCMDRxWDJSRXE5Q041WjNLajVYa2RkWUNxOGorYWVpakZaNmQ0OCtoWkhkUk9Tb1pBSEpjYUU5RGJ0K2QzVnF0QXk5bTBaa1hyVWRobVZFczBQY0x6WHA1Ni9pazNuYVJNU0tVL2dUZVEzcmUwb3RBVnpqdXptNDIwTzE0eXBxME13dW81eVFLQmdRRE5MV1MxeTdJZVNxSVY4MFlaZHJDSml5Q09Rc1g0ZEdadmpDM3NDYTd0ckdPM3Q1UUtNYTc3U1d4cDJFOW9ON1l5dG5jVTZEdm55cGd2N1Z0dU1QUm41dW9qbHhmY0dTVHZFOWNLWTZBekQwRFdDQmd4cWg5UmIvb0krejdENW1EYW5HektZRXNzalcxcVIzYjBqS1BVYTRUaHExamZKK0ZTbW5NQWNudUtyUUtCZ1FDTWw0V0VoZVI4ck5nczBsMThaYlFuVHdCQ3I5Tkw5dHhsUEE4TVhvcHJDNXE4NS81Q0s5ZHRIZlZBbWw1eUJLQXFXYXJiZnlyM1FFZjExQ05iTDB1a3pCcFU2YVBwTXdkWS9GS0x0T2RxalNPSGlwK29WQysxVWF0UXRkcVl3TE9wTmN4eUdUcmJLR1JuTm5RZzczN0E4eXlNaGdrWm00ZmRRcDF3MVVZWDl3S0JnUUNIV01wMm9raDljdjQ1UEtHaGFvcEtNVnpvZTJQYzRld3c2V2ZoclFHWUI0QkFVUGwzUUE4TjlRRnZVU0lRdmErVEJJckpYK2trbnFDRi9TMnpJdGdYTWx5QjNjbi9oeGEySDRCYmVoelRrZHhUVkVPaGYzZnBZTlN2MkEwdmJXbTJ6RGwzeHMzUU5mdFhnSTBZQlM2TmtkKzJmakhDQTZ5L3NPTHNDSmsyZ1FLQmdEWVAyZTdRMGNERGNra2lCNExiVlFBOGw3d05BbkpXbGY5enJkR3kxUVUrckJ6eUZNcDdNMWFwUzNLeEtab3NmeTVwMXBLYS92bWV4VTBaYXhNWVI3MHlJdm45OGVLdGxhaTVOa0MwcXJ4RlU2RStSQkNsZHNjQmhaLytuZlZaUEh6WHpDc2Yyb3NGcUQ0c0tWRzA1b2ZwdW5xNjIrcjE3TE8vZHUwNWhiK1hBb0dBRlo1eGVvUkM1dHhDN2J3KzFYSkJoUkZmYkpzSkRmei9QVysyM2xpQ2RneUVvby9HbGRhbnJ1dHNpNTRhZzF5bWNCS2N6WG1BZGE2bW96TENNOTBHMUVnU01xeW5kODY0ZmZPbDFVWndoemNDZzNQUERKb0lBdEdyQVh5dUNLSW5vNGtqZ3gwZnhxSUpMY0N5ZW1XaFpzZllxRzU0WE94UC9Sa2laenNkdkJRPQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0I0R3hXTUYrSEtGcit6RXlwVEwwTG9paVNzcTEwMWVIWDUwTzVWeG9NakRYZ3V3dFJ4T2wrU1pQRElmQW5ZYW9Lcm81VUxVc0c1MmRYS05wN2puOGxnNDlsT1VyRWhKS2dmcWxRaGRwVC8vR09nMnk4UFhFYlhRam5FV3ZsUG5DUTJRbi9ka2ZGeE45QU13ekhOL09VcThVYzQvNjJrWitaNkFOUmdrZnVacEFoVUFnV2x3YkxLaFk3dEJndVQ1RDk4UldiTHFLVE1DZ1lBSis0RUZYcXU0eU56dTRMWndxY0pCWTVjNC9wbTFDTlFmb1pHZDQ4WlBQODlJSGJ4Z00zMjlsTWhqQy9NOXZoNkRvSkZUcHkvQ09LV1ZBMkZYWDhZdzZ5RnlDZUNRbEpMdlErYzYyOCtrVHlRMG5nYldmMXZ0YmVRaXdzM3RJWTlGMC9pSDJTOWxQdGlMSUhMUzBkSk5hYWozaEdrZ2k4aUdXaVJBSWk4SGtnS0JnQnljNGJ4RmpoZDlIekhkM0s3T3d2a1hNQnRQalg4VVc1eWt1RFVOd2p5Umppa2FxdmNObEI5UldXMHh4QVZ2eGQ5aWpXNFBIWXJ5WExkSWM3UXovNkF0Umw3NVcrbGpmWElLVUNsWEZWNXVHL0RucUpNSXRsM3lXRzVnVFhrVW5SSFc4ZDhQZ01NTUNGcWFRNFVxM29teGpwLzM4bU4wWkQyOG1IeEJadkxhQWhVQXkzQm14SVAxbGZPOVk5aXlCUzNSbS9pT2xubz0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMmxpWEpRYjVBc1ZGakRsZUJCVmVTMHV0OUdEMjR0V2tWUWtmdzRISUQ2Z0J3WUZLNEVFQUFxaFJBTkNBQVJFQ2lSaDZvTFN0a1FmT25rL1JpaThYNGRnc0wzaklReCsycFJNWVZTYUZXMVZyVE1rZ0hEdHEweHRGd01oekRPa05weVlLVUVZN1NlWStYYSt1NnI2
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVhRjJJRVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFPRFE1V2hjTk16RXdPREUxTURnMU9EUTVXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0I0R3hXTUYrSEtGcit6RXlwVEwwTG9paVNzcTEwMWVIWDUwTzVWeG9NakRYZ3V3dFJ4T2wrU1pQRElmQW5ZYW9Lcm81VUxVc0c1MmRYS05wN2puOGxnNDlsT1VyRWhKS2dmcWxRaGRwVC8vR09nMnk4UFhFYlhRam5FV3ZsUG5DUTJRbi9ka2ZGeE45QU13ekhOL09VcThVYzQvNjJrWitaNkFOUmdrZnVacEFoVUFnV2x3YkxLaFk3dEJndVQ1RDk4UldiTHFLVE1DZ1lBSis0RUZYcXU0eU56dTRMWndxY0pCWTVjNC9wbTFDTlFmb1pHZDQ4WlBQODlJSGJ4Z00zMjlsTWhqQy9NOXZoNkRvSkZUcHkvQ09LV1ZBMkZYWDhZdzZ5RnlDZUNRbEpMdlErYzYyOCtrVHlRMG5nYldmMXZ0YmVRaXdzM3RJWTlGMC9pSDJTOWxQdGlMSUhMUzBkSk5hYWozaEdrZ2k4aUdXaVJBSWk4SGtnT0JoQUFDZ1lBY25PRzhSWTRYZlI4eDNkeXV6c0w1RnpBYlQ0MS9GRnVjcExnMURjSThrWTRwR3FyM0RaUWZVVmx0TWNRRmI4WGZZbzF1RHgySzhseTNTSE8wTS8rZ0xVWmUrVnZwWTMxeUNsQXBWeFZlYmh2dzU2aVRDTFpkOGxodVlFMTVGSjBSMXZIZkQ0REREQWhhbWtPRkt0NkpzWTZmOS9KamRHUTl2Smg4UVdieTJqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRDFSbEthS3JDTFdnT2gyZ3hDVlczUjJoKzAxQWhRRGsrdzFoL1RTVGUyeHVxazhsRDNLQ2dKZmZBPT0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUTRuMUxwTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFPRFE1V2hjTk16RXdPREUxTURnMU9EUTVXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSRUNpUmg2b0xTdGtRZk9uay9SaWk4WDRkZ3NMM2pJUXgrMnBSTVlWU2FGVzFWclRNa2dIRHRxMHh0RndNaHpET2tOcHlZS1VFWTdTZVkrWGErdTZyNk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnY2Z4TU54S1dFbjdleXBMY21HZmQvZXg4TWlnNHRVUGJ5SXN6cG5KME9FNENYd1gvYkRjck9BMk9NQWJxQXpJOFF6dVZ0dGhySS9Qb0lVVkplZmYzMVVleU9qN3pPQ1VVSE16akhnNlNPNmJ6Rnc1RWlrbzF3OUNXamxxeThEZVdyL3hCNHJGdzR3WC9iUmNxSHRMcmdQRThZTWYwdDFLSlFmQ09LRWxTLzRMUQ==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVVZmQ5bnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRBNE1UY3dPRFU0TkRsYUZ3MHpNVEE0TVRVd09EVTRORGxhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCd3JrUGNucXFrM2VtRTV6Mk83SS9vUXZPNmowOEt6QWRZSHIwbS93MWh3Q3BzZnk4NDZOSzhIdmdOb2FJV3JCOUVWSjNpQVZyQjFPMUJQV1dWQmZUQVlsdVB4c1FrYjVsQ3JoU3lvYjhiRVMzOVFRd2Jna2tTamJ4bWt5aG5HZTdVa1hJdXBPVXNpVnhna0lEVFVQejQrYmxvNzFhQnhrNXNtNHA3N2Fld256Q0NaZzV2c1ErNHZ2QmFBZzQveFpMdWpSd1ZJcCtaM0dzZ1VvbXpUcHhXV1lNcVZSODAyM25IRkV6Y3Bxay9vcXpXVnhvUXJEZC85SGVnOXhGUnZHbTF5am1VbXh4bk5RTUhpNVA0aGkrcEs1NTRJb0NYOEt3RE1yWUxETDd4RmR6OTNhemU5eitGc3VBMVpEVUcrNDlZS0FEajNrbHg4VmhzM0pGcTlsZnJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCamw1eEpHL2RUamRZbEovNnRGOVpva3BmbTRINkdjSVZkbDA2ZE84d3U2Nk1KWitvY0ZvY01OcWdxMitSUnJSbVpWbnVXL2I2TXVXQ0tZeUhLeUZHNHhtelhQejA4MFhYK1BFc2hNRDdVcGNTbHBEb01WeUU2Sk95UzNQdGJBMjdxTGlocUVzQmk3WTBtVk54bXlTc0FHdUZxLzdBUG02ZkdDM3BGeGRQVXY1ZFFwVStkZGN1djliUjN0YWd3Z29FNGlMVERnQllHYndGNUxweHc5K3NlWFVvN1ZKZDdXZ0RRN1BWQ3gzR01ic2xnaUZxZnd0aWhWMnhDUjdINys3azB4Sk1LNU56Qk8vUzJ0REZ6ZllkV3RKR3NWSUF5b3RvV3ZMdFNZa0ljb3czTndUK0dzR09oR0FCVEtROU9hc3IzR2c0T29pSFN3dTJ4K1REWUZER3c9
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.2
 redistribute connected
 exit
!
router pvrp6 1
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
 router pvrp4 1 enable
 router pvrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
r2#show ip
r2#show ip
r2#show ipv4 pvrp 1 sum
r2#show ipv4 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
 |-----------|---------|------|-----------|---------|---------|----------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:08 |
 |___________|_________|______|___________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 sum
r2#show ipv6 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer      | learned | adverted | uptime   |
 |-----------|---------|------|-----------|-----------|---------|----------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:08 |
 |___________|_________|______|___________|___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 pvrp 1 rou
r2#show ipv4 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:02 |
 | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
 | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:11 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 rou
r2#show ipv6 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop       | time     |
 |------|-------------|--------|-----------|-----------|----------|
 | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:01 |
 | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:11 |
 |______|_____________|________|___________|___________|__________|
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
 | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
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
 | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:02 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:11 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

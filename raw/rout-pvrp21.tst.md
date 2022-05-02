# Example: pvrp ssh encryption

## **Topology diagram**

![topology](/img/rout-pvrp21.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz67r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWpuRlh6STJHaElWNTR0VWhYVlBQazFvWVpUUWNPQ0hqekhjcndoc3U1QktKNlZVcU1rY01ueTIyYmU2QkZQbVJhT05KS2RwcGdOOGd2QzhOZmtaK1Rpek9FcUlYek9YVU5yWm0xVForeWVDdHJESzRmZjFxdmhLWDBsMmpTYk1oSmY1VU9nbnZGbUd4dEsxSkg4TnZKcElCQTExK25UU1VkT2NhTE9hd0o1cllialhUdEpaNkJrc0NtZk8wZTg1UHNvRWJ5OTh1VUdtWTNqTkN4UlRxSU1DMUV1TlgxYk9QTEdZb3R6S2k3YXIzWm1tdU1KTnBuNjQxMjdsdjBleG43NnFNVmhyL1l3Y3RhZ3UrVDdIQXNwem44MUV3dXMwSGY0VkMxd2pRR0RxWGxQSTVmZWFRbmpETFJFNU54WUM1YzVkVkJDdTl4eGd5TW5CdWlQSTluUUlEQVFBQkFvSUJBQU84ZDFnWE1qc1JvVFBROFZJWVc2NTZ3MzhNRWQxckRpV1R6cU1Gd1lJYjltQVhhc2JzMUNqc3N3ZEpKVHVlbkRETEhXVXFwRy9MNm5qbEp3NXozT1pDQ0ptMmhMZE1JL2ZYYXZVV3U5YWh2UXh5UENLWjNnM2tRUFUwblk3V1V2MURJWVJ3TkVRN0JjVStjbGVSOGIxcVFQcU1ua0NUVzMyQmZrOUZNY09vSXRrdEFWQ3krWjVZTjVTczZSUW13ZGJUTmRJbDdiVVhkc1RzNFNlN0ZpWHErNldYWGlPcGViNkt0QUM4TlpZRVQ2Y1MwS3FIVEFXTi9Cb2lGa3E5TCs3bk5zUURZVmFwelpKd3ZPZWFFR25JdG9kNnNvMndNV3h0THB4ZEdWZ1FadE9PZzIzQXQweVcwdXJueE5JNHFOVFQwdFRrb0dBT0Q0RDR6ZFVhaHFVQ2dZRUE3WmduS3pDbmF2SjF2MWQ3NnVGL1lYWHIvUlhTMjVSZnVGYjV3aTlKdWhCN1RqWldvc0MrSDF3VzRKOU15NU1vUjBtQWE2dm5QbWdneVZJSVdGUU1oRW52bXpNTW9PdVVMVk5UdlpqK0FobHg4VHp6dHM3S3c0c1Y3bDNjb2szTHZ2RDhOblFQNE1yV2xGY3BLWXNPZlJYbWg2MHJZczJSTUZleE5wY3I0TzhDZ1lFQW1Yb3hidTBINGNITTd5STZLMis5bFJmd25LVzBMb3NFWXptd0NKeFBjem8vZ25uUG5UL24rUjV0bExsTXN5R2pEYnFOUTRKeHRYQzgrMWFWTGdGTmk4VFZXY3ZwK3E1aGlvMDNSLzlocjI1Q1RGQ2R6blFEbHRBbi9XdXA2Z0dTbXJIQ29xVWxBMU9PdFkxSTdJaERCT1RRM3hxZWVQU3lhT2VvVUR1V2NqTUNnWUF6Sy9rTHFVLzFqY0RrZEJBaFYyM2E3TTNsMVdSem5ISTlQcVpPTjJjV3B1UVh4VVpGaVdPcFYya3ArY1ZOZHlWT3JUcjJkYkM1VlMzeWpqTno2cTVEYzdVaVpRMU1QMURMcmsyejRSYWNGeVRlUXpWdVl2MXl2aXI4Q3NVeFE3WWxLcnYzY21uVkRYckh1am9JVTRYTVZRSXdxSkJXbUZXejVyOHBOY2ZpaXdLQmdEUjhRU042RTlQMGZxell1NlBYRnJKQitacllZQUg2c0lsdVZQRGM0NTY0TUxmaUNFbnliTllZdmNpNmhheE11SUlkWmVuTVZpNkNXMTVvZ2FPMTlscngrVFE0TTgveWlwRGpNaUNCQ1ZzQkRkTWpUcFFud0lKMnRQWkpOMVk3SzNPVGpzZ29TYndWZXh4RE1Na1M0RGh3TjYzVVlKVmt1UTUvQ21SRnZIRlpBb0dCQUxWVlREUWFFd0x1Z1o2T2VUZ3UvRFVBdnd5N01MYmMvQTRwRGFpZUtzdC8zblVTVTlPc2FqZTE3YTRBd3oxWE5XTDVFMDBzMnlXVnhjTXo3T2JIaU53MEJmL0VBWUx6V3VSZTdiT1N4NDUwNjF2T1pONHdaMWpEZFRFQVdhSnlrUnUzM2JXbXNFeUU2emJlb3pTRExsSHc2dytCZVpuL1JjN2I3THliL2NVdA==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0JvcXdTQTQvd1JoL0tSQXRqUGJJM21rRk1GS2FGN05rajRJRWwxKzZpQUZ4OTZISXR4WTlDRS9JYkRucWtzRnkwb3d5VEtGNTVVNnNJME5rTW10VGJUVHdIZ0xLSW1SbUdWVzBGMnNsbTBLczlVZytCNVdxczF3aWswemszanExcXpMbnE1M1lUK0JBb2F3RVFuSVVHZDlmZ0c5SzhUbkY4VWNkQll5ZGRRVkFoVUFveGVhRWlLOHFjdkZuTDZObjRJeFo2Sm9rYThDZ1lBVVgvcnBPWHlXMTBHejdMTjVpTkk1b3VGb0RxVi9vVnQyajNXbnR2UUtDTGluSnUwa1NqU0tqdDZ1RTNvK3Y0MnRUbXBxU1o4VTJ1RElhUkVlcmN6VzRRQnIzZEJhUEdCT2F4dG9XSFV2YzlUbWdZSkVtRDNydmlITEI3S0dEU0pPTXIweWZIdXZKOUREQVBQQTE1SEh6TEpEaFVVV2FEeEtKcmdFaG1ERFV3S0JnQUNab1RjK3JraFJNazh1Q3l1NjNHNktqK1VJNE9ERnNYcnVWWWZtL2J0SGxsMGg3U3l4N1BEODdiNFhLMExLRGs5cWVSQ3JEZDkyMEd6QzhiN0U4NmwwY040UWdoeW9NYW1yUXROcG5xN3RhcXVvZDZGcmxNOHJuNTBVa2lTV2ZhZE80Y0dld25VSTM0MHhXOW5oTThVU1dUMjF4dm5hbzJUVkcyRnhybmFaQWhVQXpjY2ZRK3NEYVJXcnJJY0l6MjdtM3NYd2pHaz0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNVWWtObmhuUTZxQ2xZOW1IdHFxT0ExTTlRV3FJMDRvL3pMQlh4YS9GYW9BY0dCU3VCQkFBS29VUURRZ0FFRzM3VFVRUVkvVjhoT01lSVJYUkxRWUFrakYxbk43eGU1ZW1BRld0Zk5pbHZhVCtleis4TGpuMnVWUjQrL2g0dkMxL1g5dndnSXVseWZYNTR0M1EvbUE9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVMVDdTRVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXdPRFU1V2hjTk16SXdOREk1TWpFd09EVTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0JvcXdTQTQvd1JoL0tSQXRqUGJJM21rRk1GS2FGN05rajRJRWwxKzZpQUZ4OTZISXR4WTlDRS9JYkRucWtzRnkwb3d5VEtGNTVVNnNJME5rTW10VGJUVHdIZ0xLSW1SbUdWVzBGMnNsbTBLczlVZytCNVdxczF3aWswemszanExcXpMbnE1M1lUK0JBb2F3RVFuSVVHZDlmZ0c5SzhUbkY4VWNkQll5ZGRRVkFoVUFveGVhRWlLOHFjdkZuTDZObjRJeFo2Sm9rYThDZ1lBVVgvcnBPWHlXMTBHejdMTjVpTkk1b3VGb0RxVi9vVnQyajNXbnR2UUtDTGluSnUwa1NqU0tqdDZ1RTNvK3Y0MnRUbXBxU1o4VTJ1RElhUkVlcmN6VzRRQnIzZEJhUEdCT2F4dG9XSFV2YzlUbWdZSkVtRDNydmlITEI3S0dEU0pPTXIweWZIdXZKOUREQVBQQTE1SEh6TEpEaFVVV2FEeEtKcmdFaG1ERFV3T0JoQUFDZ1lBQW1hRTNQcTVJVVRKUExnc3J1dHh1aW8vbENPRGd4YkY2N2xXSDV2MjdSNVpkSWUwc3NlencvTzIrRnl0Q3lnNVBhbmtRcXczZmR0QnN3dkcreFBPcGRIRGVFSUljcURHcHEwTFRhWjZ1N1dxcnFIZWhhNVRQSzUrZEZKSWtsbjJuVHVIQm5zSjFDTitOTVZ2WjRUUEZFbGs5dGNiNTJxTmsxUnRoY2E1Mm1UQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNOb1lRUmdHWkpHK1p2Q29QSE15RTB5NHlpQ0FJVUp1YndsQzVnZlllY0ZBanBXWlN4d1NFV3lrND0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUnQwRDlRTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXdPRFU1V2hjTk16SXdOREk1TWpFd09EVTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRYmZ0TlJCQmo5WHlFNHg0aEZkRXRCZ0NTTVhXYzN2RjdsNllBVmExODJLVzlwUDU3UDd3dU9mYTVWSGo3K0hpOExYOWYyL0NBaTZYSjlmbmkzZEQrWU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBTSkhzK3Rvbm5mblVFZUlkU1d0WHpmQ0ZzSGgvRXptYS9Ja1dGQmtnQXBBbDluYjQ4WGgxWFhyckE0VjU3ei9NMFJKSzluRTFtRzdEOGJWcERYd0xNMGpQOVh3d2F5V2YyblRyMnNJMzlObE5mRmNYWnBWKzBNckZ0ZFpDS0ZmbVJ6S0oxQkcranlNbWFwU1o2eWdCQlV3SjdhQ1FCYnpCZXVKbmtwNytLdDBBPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVDUG45N1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEE0TlRsYUZ3MHpNakEwTWpreU1UQTROVGxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWpuRlh6STJHaElWNTR0VWhYVlBQazFvWVpUUWNPQ0hqekhjcndoc3U1QktKNlZVcU1rY01ueTIyYmU2QkZQbVJhT05KS2RwcGdOOGd2QzhOZmtaK1Rpek9FcUlYek9YVU5yWm0xVForeWVDdHJESzRmZjFxdmhLWDBsMmpTYk1oSmY1VU9nbnZGbUd4dEsxSkg4TnZKcElCQTExK25UU1VkT2NhTE9hd0o1cllialhUdEpaNkJrc0NtZk8wZTg1UHNvRWJ5OTh1VUdtWTNqTkN4UlRxSU1DMUV1TlgxYk9QTEdZb3R6S2k3YXIzWm1tdU1KTnBuNjQxMjdsdjBleG43NnFNVmhyL1l3Y3RhZ3UrVDdIQXNwem44MUV3dXMwSGY0VkMxd2pRR0RxWGxQSTVmZWFRbmpETFJFNU54WUM1YzVkVkJDdTl4eGd5TW5CdWlQSTluUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQWlQUk1QM3h0dFMvWDdOblBrT1Y4REhsN1RGN1N5VkFrSnZ0WjVhU2F6U051RFI1L1ZtekIwQld1YXlPN0ZMQzdUL3FsRW40dmJaQkN4WWd3aXRML2VsSS9SY2JVMkVObXo2UCtiUFN6aFRMSHRkU3BldnVLcDdFZ1dvajhJODkxOGlMbGI0RFhzQlJrWENlaWs1Q3JvTi9hWDMzMnJaam5TOG9QeTJPOTVEWDVZYjFLdDBtK3BXQ1NOT0xFSXd5VGRHNWdCVlF5MWd4Wk4rcXBZVFpmaC9tWCtobnJMV0dhVHF1RWFrbTE3Skg2cnV6MEJSNURIYTFjYWVHeUJrZkU4ejZKcmR2enNUa1E5M1lTTDlDckNNRGtNVzdyeXR0eTgxUjVxWGZ4am1XaVlNODZnT1EwR1J2NzRiWFh5NE5BR0tKaWhKc1JXZUx0S3JSdzdSd1hm
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
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 router pvrp4 1 enable
 router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
logging file debug ../binTmp/zzz67r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFCNDVlWWhtUkdPUi9TYng4alFaeEU0Tzl0Y2VadEliOE9wbUdYUnBsRXd2NDExYTg5OWhva09rbm5GSDEwUDlPMnA5UmJhaTFhb2VmaEZVV1dUbTZQV2NKbTJNNGNtbUswL1huRWo2VnJySzEzMFpmeTVTN2FERkM1NFNNL0JNSGw3VE5hUXVxUUVYbVp6T3lZdHk1OEs2SWF0U3V3TUxDbENFUlYvSGRoSjBTcm51bUdTWmxOaVJ1QTR5b2xETitPUE41L2ptS0M3ZjduWWdwMUlKVFN4TlRlZklhMFBMQWZQcGFHMUs2cTBTTHdDc3A1WlI3bWpMT1grOTFDcGtXMlFIRjQyZWdPdmE4b0Z1OTczVkp0ZTVicTg1ejNRSFJUanh5TmlXZHZyUkwrSkIycDh2SFhYeStDTEhoQld0NFNPNHVrL0tNckJIb2d4VHI2a3V3UGpBZ01CQUFFQ2dnRUFCeTd4eTVGQ3Y4ZDZ1ejdWcWJ4V0E1ZGE0MVcrYWtGcHlNdnJVTmVtLzFTQ1hUVzRzR2FzQWhlbDhKWjZleFk4Z05xMUx1c1VqUklpTkV3djB1TnVpckZLRU05aSttSWIrU1h0WndyWWdoeWppbi84MGkyemZIcFlnSUVqQndHUVZra3NmcEQ0YWVJS0NGSzlZLzh6UmZ5bTgrajl1WU51T0NTM3VFUFh0QnNLbTRXN0t6M1poS2hhSkJYbnF3bHp4UXl2NDc2YkRWK2JqaVdNMTJINlZQdFZFdFBwMEI1c2dEMVM5YUQ1cVdYbkN5blEwM29IU3BYVFRPMWI1RXNMaXVPdlNQM1M2ekRiQ2ppR0E4TU1jRWtSYUErSXo2U0E0QVN6aTJBU2VqSzJoWXZYTHU0dWlBcHpoVGJTTHFhUnpvRVdKU3hJNzVUa2pyUDNORC9mQVFLQmdRQzI3Q0U0dE9abmdPRENtSkxJUGVGUmFpOHdWYmZDcjBJWEV0REcyWkZqeWJQckIzcUNDNWRuYWZ3V2dkYVY3U3pPTEZGeTY2N1BLVTRpMldzMm5jODVaZWhhblpBUFJ0bEZlalB0VHRNYllOakVaTHhQdnM0dFAzOTYvdVBUcFpCQUNQaEwrdFp4Q0QxaGlyd0J1UXJLc1BNeFpFdjB3dHMzSEZkWENyTFBRUUtCZ1FDcE1tZXRFeFFONXN4YnFGM21rRDVUSVhQdG5vdFpwUHR3S3J2RDlucDFWQUJ3M3gyWDRZSzBOU2Z6N2s2dllQbHpmS2FZRktoaGJkVG9rZnArcDRHR055T3kwa3kwa21ZeFBxUXlsN3pKUmQrZTFVZG5uUDFadkY2UWxiYVp6c1BWbXYxU0lVeWNxUms5clAvZ3d6clVub0NTTzcwQ2NaWUM0Qk5KRlVzdUl3S0JnUUNTSlh5eGVzN3UrU2dhTVo1c2dBd3FhUVVFd0NlT1Uwb2hkelg0K2RGUWdkSE93TzNmUXZXWGVUVWdvbUhZN1dLejR2SzhONU0yRHBGUUJKZkZUalpIYktWRTZNZzFmR3lSTnY2UDVqK0NpMUVGTUZySDkvRndjMkFkMjlJWXdobkxINStKelFKUjByeC8xMEU0dXlmbEk1Vlo3QUZIci90SFA4eUVUWmJwUVFLQmdFRkNuZGFWNjBCSmF6MVhQWkMyeGpOT1RlYXpKbENYWUJ3dGYycmdZTzlzVFJjOEY3QURYV1NndEI1VUpxbGlvQlM1V1pDRE4wY05FL2Y0aGtQZjNBZW1zUEJDU1MvRTRBSFNoWWEySEMwTjlHalJIcytLTC9ZeXY4N0kwRHVYRXRZTEIvWnJ2WjhYWWhMMTdXUUdLV1RsRmZaUmNGL0c2L09EOWl4VU9FRTlBb0dCQUxQbmpEejFWMzJPc1NHcXJtWDU1TzlQYnZLOFV5RDRzOFhjRi9hMEc5TFlGcTBMUUlFMzRWSVdMRGFSblE0TUxEd3gzTWtPY2tCbitrMXpzc3dad200V3hSUWY3aVVHZGlnb21jcCtCS0tQckJuQklFK2I3WlhaY2FpcmVrd0N6NjBZbDRiMlRjVnBMMGdWbXZSeUtEbG53VVRkWWdaL0dBMytEVVBrZ1RhRg==
!
crypto dsakey dsa import $v10$TUlJQnZBSUJBQUtCZ1FDZTVXUUl5anNMOWRBWldpU1RkNmNCWjIzVm10RE1ZdWtiRTJCZHdCdVhyeDQ2RUtack8wOXZBd3FROVNycUd5TDdCN055L0FtM3R0ZEVCTjhaVnp0VkViQ2ZpejIxV3VRdTFwTzdsNkM0NExJNSs4cC94RzFsYlh4WXBUVkZOZGFQanJSbmMrVmF4RU9hc3F6eXdaak94ak1Fb25yWlhMVTBRc3FUKzFtMkF3SVZBTlJYc2FZVFliQkE1WDhUYnFlMEZuYjJzTVVUQW9HQkFJMElJRFJ6VzVaVVhHRXZZUUVkM2U0Q0FwTWIyck52cmZMam9IcnpuZU9XYStMcFNGY1RJZnlLOGhaQk5naWVOaklva2VxREJRNU1xV29CWUwvUXZkNWdQWXY5c1piSks2aDNwTGZ2TEdVM0M0YythQWNpVmNrQzhvazVicnZJYnhBUGN3cHFycmJsREYxUGRRUk1rdjZwMXZrZXpGZG1pcGNsSjVwUWpNQUhBb0dBYmlqUmw3SzN5UzNDR1BYMEZ2cHJrWUloelVwV1g1YXBUM28rRzdFbXVOME9MWUZ0bGVSZDc0T1BlZWtaT1g0RDBVVGhjUmhYTm1rZXkybThxcmNsbUFvcHd4bmdoN0tJa2xpeFV5eUtuM3A3WURZQmd4RHorWGlNcmtHZFNhWW53dGxJaUwrNWVVcTB3SHoreCtUMUYrek8zKzhsWStTYVBreHBhRDhsQ0tzQ0ZRRGd5STNWUXBnUDlCMnJXQk1rdlVtbE0rRXNHQT09
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeXpBaTFzWVQ2eWhMbFFtMmNseTRaYkFLeWtKSXBzK3BVaWZBR1RES3JHZ0J3WUZLNEVFQUFxaFJBTkNBQVJyQzRtQVVpaXpLY1ZMaEZ0SEZpRlBoQ3N3ekROTE1tRkpYanU2enNtUyt1bXhjMndseEM5eUNLVk5lYXFmU1VwZnpWSVBhQy9yS2dDcnpnYkowVnZS
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1ZUQ0NBaEdnQXdJQkFnSUVkSk4wenpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXdPRFU0V2hjTk16SXdOREk1TWpFd09EVTRXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYmN3Z2dFc0JnY3Foa2pPT0FRQk1JSUJId0tCZ1FDZTVXUUl5anNMOWRBWldpU1RkNmNCWjIzVm10RE1ZdWtiRTJCZHdCdVhyeDQ2RUtack8wOXZBd3FROVNycUd5TDdCN055L0FtM3R0ZEVCTjhaVnp0VkViQ2ZpejIxV3VRdTFwTzdsNkM0NExJNSs4cC94RzFsYlh4WXBUVkZOZGFQanJSbmMrVmF4RU9hc3F6eXdaak94ak1Fb25yWlhMVTBRc3FUKzFtMkF3SVZBTlJYc2FZVFliQkE1WDhUYnFlMEZuYjJzTVVUQW9HQkFJMElJRFJ6VzVaVVhHRXZZUUVkM2U0Q0FwTWIyck52cmZMam9IcnpuZU9XYStMcFNGY1RJZnlLOGhaQk5naWVOaklva2VxREJRNU1xV29CWUwvUXZkNWdQWXY5c1piSks2aDNwTGZ2TEdVM0M0YythQWNpVmNrQzhvazVicnZJYnhBUGN3cHFycmJsREYxUGRRUk1rdjZwMXZrZXpGZG1pcGNsSjVwUWpNQUhBNEdFQUFLQmdHNG8wWmV5dDhrdHdoajE5QmI2YTVHQ0ljMUtWbCtXcVU5NlBodXhKcmpkRGkyQmJaWGtYZStEajNucEdUbCtBOUZFNFhFWVZ6WnBIc3RwdktxM0paZ0tLY01aNElleWlKSllzVk1zaXA5NmUyQTJBWU1ROC9sNGpLNUJuVW1tSjhMWlNJaS91WGxLdE1COC9zZms5UmZzenQvdkpXUGttajVNYVdnL0pRaXJNQXNHQnlxR1NNNDRCQU1GQUFNeEFBQXdMUUlVSitnalRnQXQrR1RwZU1FUytBb1A2ZkxmTDNFQ0ZRQ3U0WnJnRXZoVHBvb21lam1DNnkxZ3gzWlhmZz09
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUTQ5ZUI2TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXdPRFU0V2hjTk16SXdOREk1TWpFd09EVTRXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSckM0bUFVaWl6S2NWTGhGdEhGaUZQaENzd3pETkxNbUZKWGp1NnpzbVMrdW14YzJ3bHhDOXlDS1ZOZWFxZlNVcGZ6VklQYUMvcktnQ3J6Z2JKMFZ2Uk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnWmpRZGgydUVtbk5VVnQ0a0I3b0hZQVhRa2crUkhQQU9YK3pOK2xWQVBWNENYd2diVGYxK3NlVVI5OXFQMGNNUW1rSzZsQmwwMUZHRkhOVDd6OE5nWWluNzVSTkpPZG5jUjZnUHFkc1NGWktRb0hHMlk1VWh5cVdFYkhJSjF4dTRPaE13NDExaWJOZGF5WThUM1N4blY2MFJnbkRlUFBWaVB3YlFVMUtrcXZpSQ==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVjK0tjTnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBMU1ESXlNVEE0TlRoYUZ3MHpNakEwTWpreU1UQTROVGhhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCNDVlWWhtUkdPUi9TYng4alFaeEU0Tzl0Y2VadEliOE9wbUdYUnBsRXd2NDExYTg5OWhva09rbm5GSDEwUDlPMnA5UmJhaTFhb2VmaEZVV1dUbTZQV2NKbTJNNGNtbUswL1huRWo2VnJySzEzMFpmeTVTN2FERkM1NFNNL0JNSGw3VE5hUXVxUUVYbVp6T3lZdHk1OEs2SWF0U3V3TUxDbENFUlYvSGRoSjBTcm51bUdTWmxOaVJ1QTR5b2xETitPUE41L2ptS0M3ZjduWWdwMUlKVFN4TlRlZklhMFBMQWZQcGFHMUs2cTBTTHdDc3A1WlI3bWpMT1grOTFDcGtXMlFIRjQyZWdPdmE4b0Z1OTczVkp0ZTVicTg1ejNRSFJUanh5TmlXZHZyUkwrSkIycDh2SFhYeStDTEhoQld0NFNPNHVrL0tNckJIb2d4VHI2a3V3UGpBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFHVlpMR2xReXZOSzNucnlhMW9kSDRwMTdOVmxHOEsvVGpDK0RQdlhVeUZwSjlBUTZkUlJiZXVZTXZmSGd1UTd5bUhpVGFQdXAyOWpjZnZ1cFZxazZsc05idFZFR25TWVpRVmFhSGFXY1RmS2xWNVQxM2p2NWFkRXF4a0YzbDF1NmhQenV2Q1FuNU9JQUt6M1diNGRmMjZvdU80NmVseUpnK1ZUWUgyL2NaNVlyY0lDTlNFczk3S21QZW1jVnZsa1Y4cnZCdFVnbThQa0I3UXdPeG9lTVphbWNJVEtMV1RGSC9IdTJQYUJWUnNyYUpmczhBNlBWeDBIY05BZ2JUQnhVdXlqc3ZlVlIyVjk3NlJUakh5Y3FDbFBram1vUzdPcitDV1FlanRJUTNPYVMrenA5Mm5lQlJJSzc3d0RSODZ6aytZbzVTQXp3QTNGWU91bXZ6Z2k2R0U9
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
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 router pvrp4 1 enable
 router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
r2#show ipv4 pvrp 1 sum
r2#show ipv4 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
 |-----------|---------|------|-----------|---------|---------|----------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:06 |
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
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:06 |
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
 | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:01 |
 | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
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
 | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:00 |
 | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:00 |
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
 | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
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
 | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:12 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

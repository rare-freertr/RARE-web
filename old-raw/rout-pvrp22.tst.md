# Example: pvrp tls encryption
    
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
    logging file debug ../binTmp/zzz16r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCVXNiL3dnYkpsUHhUTnp3WGhnV1JzU1c3MmFtZkh3RmxlK21WVEEyMDkvS2dHb2o1dk5sQlhDcUwvNFA5SVQwSnBzcnZtYXdnTFR4aDJRdXYyTExSRGM3bW9WZ2E2aWJ2bEw3T2RkNWdDaFZXdVFnNjQxTjFzODM1ZUVIQmpqaHh3MFpxYWtSYVBXM1duREhncFVTWk95YitxUnNSNExMRWdPRUVTS0YydWdFVHdtSUlvMzVhK1dqaEZXYXl5aXFnSEd0VmxFMFBVV2pQaDlJVm5rVlM5bUVjYmQzeGlEM3Z0Y1VqT2dKZnlqU2NCVll1MzRnUkwvZTQ1azN2djVlRjhyd3dyVksrcTNKQW82UjhJNDFncHRuTWFFekg0Q3NocVBZN2hqYjV3Sy8vdU4vVFJuUndKcjZPZFQ0bEd4VlBxNzIvVFJiZDVDQ2VLbXFIQWRaVExBZ01CQUFFQ2dnRUFJbHJYMk45RFZmNTRtZU5ZSjFrdE94K3VleFkrY3JCN2tDTlI1cEtGUlpldk1NR3ZRYjF1YVdCUExpdytZVDZGV2dxK1hZRWRDamxUV3VWYWdja3dkZ3dEUzExWjdXRGhidDRpcGNWVlMvQjZDTzJTdXpiZGVzeHFmZzE5Q1dVajlEK1J6eEQ3YmJ0VHhpY3d0dEhNRURtV0hhUUhIaGhDNFNid2ZrVVJleTdrdXkwUkJSWVRUKzVjVWVtWGliYnRFQWpVVEpqcjhXWmpSNmxhQW9tVDZTU29ZWFIxdlJEcjIzMUlMUytOWGxOaUVpV0FVRncvK3dhNFp5VkFWUDQ5ekcwMHBkTzlyNUZOVU5DeVl4dUMxMzVDRlA3OTRIMDZvOG9kVC8vRW1MRVArdGgzcmJOODFIdzNYc3IzS08zNk9vckd3SkxpS2VuQWRlRWs4Ulk1QVFLQmdRQ2lwcTVZUjJNMStERkxnOXRDNTRTSXh6SXE3RHNXYWVhRTlLV2hoeHI3WVFnU1RyYmNDRWtWdEk1cW5EbDlxdlh2MTlrckZzNFJhOXR6K3h2UUVEWU1XL3R3U0hzb04zbGNwWlJFZE9BWGs3bHM5ZTlxdHRqaU9HOEphcjhEdFE1eTJ6Z0FiTHlTeUtCc3NObkhpV2d3cEY1NEl1R3hwckhLd1RKdVc1QWpjUUtCZ1FDRlRWMDRITHpIVlBsR0hrVEdOVEs5UkNxUnhISS85YmN6aDVLRG5peWpTdXA3SjRqYnArZS9pM1g2RDRrdFo5emEwUGpzNy8rdktsWG9DMzJJQjNQZWsrdzQzSzdRMWp6eFpMQnNFV0FHMnRtNW5EdWgrUTZDSEgrTHdzdkI5OWcxckxBZVBtZDcyWUpadDF1VlUremNvRVN2eDVCTEwvcVdHM0Fiekh1bCt3S0JnUUNGaS9vR2ZjYlYzMDBLUmQ5WDFhUWFjZ09jL28yZFg2Sm9kRDh5bXkzcVRNZEYwTitQVmpZNzNoNDVKc0NGa0VPU2hGWEpiVllSTTgvaU1NR3JXa1FtYmJmTGY1ZXZjNnp3QnZ2d0lVNkZ6VU1vVmQ0WWJyMHhNVWpxSUgxcDI5VmJOT2VNWWJ1TGdiTkd5d1psTVVzYzlUaWp4M0FzWDBRSHlBMVNVMWZMNFFLQmdBTU5Ea0VtaHp1WXVrdmNqWDVyNFVscnNmMjhIVkZSY212L2dsNzQwOVM0OWp6elhyS0lXVW1OQzVvNW1NNHRQbVRUdTU3UXIyMTI3cGh0Q3VaK0pTekcvZlVmTi9FWHRqVmdOSm1FbkVvTDRFZmJSNUloZlMrRkwzWW5jenB4VGNXTXVrczI2bTl2UHdpR3BkWDVJY2E2OUZlQm5jL2F2VVdLUXpxZnA0VFpBb0dBYXRrZFpIWGd6WkNIeW1WTTJYV2RRdXYzRnpSSkZiVkFPTFBZd3dhTDVjZnJyVWdJbmRabnYxUjNPbXhxQVpPaVBPb0NnbXpHbksrT1NFZXl2MUxqNU9WN3U0WXBGWER3NHRkQms3bGVMNVZkOGhUQkMxOHQzZ3JUd0szcExIZmFlYVROemc1VFdpei9tU05YOFFQS1NWMzZ0aHo3eVM5RlZMa0ZuejUwMzVNPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0FOSGFxa0plVzVnWnM0OGxDSE9uKzkvVEJTQWhuQ05xdkxPQis5SWpENWhFSTJVK3lMSHR1NWpSbWNmakEvWkRhcHZUek1HZ1lFajJ3NXZ5eXRBY1YzS2IxQXNNdkJGcHNrUnRaeHV3VjhNdmhMelRLR3NTOEVKMGs3ZnJ0RUdXZzQxS2tBZTFHeHRyL3Rha0ZGVkk2cUF2YUQwd0JrVmYzMUsrZHVkSUIvSEFoVUErVndLMkYyUDl5STU5NkExV3BLNk9GQU1rZ0VDZ1lBQm9UdTdUR0xRQ204UHdGMCt4dTRCK1pXdDY5cDNxUWZhOXVwbTdVbS9FNGozR1NvMHQ5czhMTEpQRHZiY0JJSTlqa0M5S0k2RWY4OWhremRMQk0xeURpVGYxYUVOaGcvVjlKZXVLdUJHTTl0ZHFlc1lJR1p2QU81SUpJTTY5Y09aTFhCS2krK2k5UzIwbGZjUXFIYWtTbVN6ZTFRZHN6N0JJYTZPUmxTK2hRS0JnQUpVckk4Mzk1aG5jOTlGNXI3SWplV2ZSdldOalcyeVN1Ky9haVVUNWR3UjQ0bUNGTlhqS21LS2U1RDdSSjNxR0JzZnlQemMrR0pYM2tFVWFobWRwbDNCbytyL1IwVStEeDQ3VDh0OGxEcjdvOHFMZ2lWNTBiN0k4WGRIZ1B1cnZNQnJOekk3UkYveHQ5aFlveW5pNkw3Z3R3WlhMWjNrZ1F6eGk2S041UnZqQWhRcDRzbnY4OXhtNVlMZW5jL3JDeW1zL2lJYkxBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUR1enFoNTRnTDR6aE1BOFkxVnhVQzA5UmtFd3ZETTd4TDhqeFdvbytXWm9BY0dCU3VCQkFBS29VUURRZ0FFVVNyMUVpUXU3UWZqQXZGcFZwTGZyWWNHL3pYNDA1NXVqUTZMbml2cFA4eGZtNjJ1c3UrSVptajY0Lzd5eWg3Vm15djIydXFFaEtIaCtmMFlJNVdFN3c9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUViaW5WUGpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOVFUxV2hjTk16SXdNakF6TVRVeU5UVTFXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0FOSGFxa0plVzVnWnM0OGxDSE9uKzkvVEJTQWhuQ05xdkxPQis5SWpENWhFSTJVK3lMSHR1NWpSbWNmakEvWkRhcHZUek1HZ1lFajJ3NXZ5eXRBY1YzS2IxQXNNdkJGcHNrUnRaeHV3VjhNdmhMelRLR3NTOEVKMGs3ZnJ0RUdXZzQxS2tBZTFHeHRyL3Rha0ZGVkk2cUF2YUQwd0JrVmYzMUsrZHVkSUIvSEFoVUErVndLMkYyUDl5STU5NkExV3BLNk9GQU1rZ0VDZ1lBQm9UdTdUR0xRQ204UHdGMCt4dTRCK1pXdDY5cDNxUWZhOXVwbTdVbS9FNGozR1NvMHQ5czhMTEpQRHZiY0JJSTlqa0M5S0k2RWY4OWhremRMQk0xeURpVGYxYUVOaGcvVjlKZXVLdUJHTTl0ZHFlc1lJR1p2QU81SUpJTTY5Y09aTFhCS2krK2k5UzIwbGZjUXFIYWtTbVN6ZTFRZHN6N0JJYTZPUmxTK2hRT0JoQUFDZ1lBQ1ZLeVBOL2VZWjNQZlJlYSt5STNsbjBiMWpZMXRza3J2djJvbEUrWGNFZU9KZ2hUVjR5cGlpbnVRKzBTZDZoZ2JIOGo4M1BoaVY5NUJGR29abmFaZHdhUHEvMGRGUGc4ZU8wL0xmSlE2KzZQS2k0SWxlZEcreVBGM1I0RDdxN3pBYXpjeU8wUmY4YmZZV0tNcDR1aSs0TGNHVnkyZDVJRU04WXVpamVVYjR6QUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNsb2ZLV3AxVzZLRy92bVN0RUpWa1Q2T2xhZUFJVVZja2ZVcnFScjZaKzl5TVYveDNoc0xPNW5IUT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUmVDZnkrTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOVFUxV2hjTk16SXdNakF6TVRVeU5UVTFXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSUkt2VVNKQzd0QitNQzhXbFdrdCt0aHdiL05malRubTZORG91ZUsray96RiticmE2eTc0aG1hUHJqL3ZMS0h0V2JLL2JhNm9TRW9lSDUvUmdqbFlUdk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU1VWUZncTBrS3ZPelB6OUt4K1oySjZVekc2QklJUk05cTRJeVpIM3pZSXRBbDl2QVh0c3drYTZTK0VlODFvb0xubEJLUUZPL3diUTU1aDhHRHNjRHd3cGVESTIybzFPWWh3OHVQNm15bUVuNkVKd1h0SXFWZTFuYTJqMnFDY1dBOFh0UlVUWUhielJGSWVZTUxjc3lFMTNKTVltVVdWb0I1Q3hQS1EzeG5zci9nPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVJSVNnV1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEkxTlRWYUZ3MHpNakF5TURNeE5USTFOVFZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCVXNiL3dnYkpsUHhUTnp3WGhnV1JzU1c3MmFtZkh3RmxlK21WVEEyMDkvS2dHb2o1dk5sQlhDcUwvNFA5SVQwSnBzcnZtYXdnTFR4aDJRdXYyTExSRGM3bW9WZ2E2aWJ2bEw3T2RkNWdDaFZXdVFnNjQxTjFzODM1ZUVIQmpqaHh3MFpxYWtSYVBXM1duREhncFVTWk95YitxUnNSNExMRWdPRUVTS0YydWdFVHdtSUlvMzVhK1dqaEZXYXl5aXFnSEd0VmxFMFBVV2pQaDlJVm5rVlM5bUVjYmQzeGlEM3Z0Y1VqT2dKZnlqU2NCVll1MzRnUkwvZTQ1azN2djVlRjhyd3dyVksrcTNKQW82UjhJNDFncHRuTWFFekg0Q3NocVBZN2hqYjV3Sy8vdU4vVFJuUndKcjZPZFQ0bEd4VlBxNzIvVFJiZDVDQ2VLbXFIQWRaVExBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFGT0NqS2hCVTF1TzJ1ODZ3aExobEdlc0xRVkcwVU1zc1NNNGU5K0xnYTZuZHM1a28xNUUrZ0p2M3F0NXJSZVhzd1ZLa1NHTzBSTStqbHlzZEJybUlyeGs2YU0vVDdteTNDcjlpTnNWS2JuUkpZYUVoOW10T0xzVjJMQlQ0d29CdFM3U05paFQ2RkRhWGFuZnRhcXpCaVVhWjBSUCtMZjJ2ZjhtZXNrYnlWbXIzTlBxT1dHZlZmbnNtZkMydXdWeVBjY3JlNVZ4ZXJRQjI2MHNaN1c3N1dzM1hzczZTcno1bFRsMnRBOWJwUVRIYXFGUWl2NmM3dTd6aXQ4ZXFQR05NcFh2YjRZN3BkdEc2cmlxaWp3UkZLQmY2TmN5UmU3Y0R3c3MwNGYzSlNSbE13bDNYNS9FMU5ZSTVIakFZUnBsSTZubUFWTHBTSWZBaFJSYkdVUlpCRUU9
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
    logging file debug ../binTmp/zzz16r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQW9FVWpvMEhTdm1EWXlHRU1senE3eXZGaEpWdmJlVmltMXVseTB5eFU2RDBUb2lnYi82RG04UWc0dkZvTFJSQW5nNElCL3Q0UCszRG5ZU1lIemt1blFHMXM4aVZZTWhYUVZna3BsWWF1TGdPWUREYW5VTCs1bURaUlcwS2s2NXVDRHpuZ296Sm11S2FERE9RNFBmVXB3QUl1VlYvdDF0RFVnZWFlcm9zempBSjc3bERNRTlGbm02ajdCWG0zOFNEU2RWa2FoMTNrRTkyMWZobWEvZ3kxN2Z6SjBHUTdFemgyU3MvYXRYTmtqei94eXFwdFgzQ0NmOWkrQTBjTWpzelVyTUNTcGpFbUlMMllnUUw4QVNvT1ZDYjBMZlJuY3JVaktPcG5vNDB0OVZQVWxxQ29uRG9zeFVtRHY4S1ZRTHp6NzFLOUUxLytiNjY0VEJjVmo5UjlHUUlEQVFBQkFvSUJBQlBySTllNWFZaXhucCtndUNEZmN0RnhHR0s5UE5TaStQRkN5RHVJaWZEbkRsYWI1NGJvcDJzVFc0SEZLeHRsTzVQemgyMzJpVVAxcnp2NnJ3T3JrVmpIZ0wvRGRtZWJJRzVnNnlNalB1aUhGOUdFeFZ5YXgyVXNjd1lGalZ1ZTB4WXpXa0RPRmNnaklheHJmTFh1ajBiR3ZwMXJzN0o3OTcxQlBUMXlIWERyOTJZMUhWaFJycm9oUGRUWjZGOTJKTlJ4bWFkZE1URVZkRmtRZXFWc3JTTVB6Ky8xUC9YcHk4Q2Vwa2ZTb2lsRmhiRTNhS0ZiNjZEZGUvWm94L0FWSTZNL3JVNEszcndvdk0zRGxEMFZVUUduUTh6M1R1d09YMFNVcjVVc0lOQWFJUnk2TUhWOFZ0KzY5S25RRDNpL3I1MnhEUjQ2azdHTUlQY1pnRURUTGZVQ2dZRUE1SHhwOGQwdlBNK3E5RHNSTVZ6SjZJeTRVNUVVZGZ6T1BQbnRhR0lqYjJGRm5RUkVKWHJMZ1k0VC9BOWdXZ2g3bU04RDk1dFF3UE9Ybkw5MlJ4WUdKZDdjbFVnclJBZWlOSTA5cDNQNEM3NEZFSHMvS0lyNlJwUnFPN0FPcldvY2xFNUEvVHYwMGFUVkZJeWk2VDZySU90QlVuQlNtbzZSNzFzSXBJOVVZVGNDZ1lFQXM1SFJucHVlUkxPS1hUaWNlUldRbEVZbXN1RVRnbkxBK2NYZUVpMEwzTnVUYUVWUWxYcnpuVERUS2FoM1BkTGVwK21yUGdRWlVDOTM4eWp6WFlFcVkzd3BidThSaFBnWEhmajU2Y01NcXdYRHJiR0txVUVEcE9NVDg3SUFuOGMvNDBEaVFhK2ppcFdaMndOVHJoNnluRUNkQVMzcnl5Zk9DUzJUbWNIQWZDOENnWUVBdVB1dFBwN25kcUZlODlxNmdhOXczSERKYndhL2ZRTE82bmtoNTJmRTdwRGZMazljNk1jdzZkUGdoQ3JpeENHb0IwQmJJdVZCRE9acWNnSmt2UXFzc1k1c0lnUksyd29mSGRMWC9yR2FPYzkvQkNmMEsxdlJZc0VYL1BqOStSSTJ6eTlIMkgzcEtLMzl3V1JYSk9XUzROVDJqc3JYWmNCVmtHYXdhYUtOR3lNQ2dZQUQ1dGMzS3dwMVU3RmQ5U3p4TkphL29nYVZQRzdBRnQ0Nmp5SVVJd1p1OWhadDNaT3lxOGsvVVNCRmQzT2YxRVVpUU9HSHAyOGxYdUtzVmVkejBLcXJIcmVId1lvUDZaUVhBcUhyZ21GMEZkdjZtakQ1SElDSHhLZGFWRFBQUlBVT2F3cC9ndUY2MFdWV2JPd1VqSFkxRHZKYVpEVUxaUUlGRVFoei90Ry80UUtCZ1FEV2lmdVFEejNXWTh4Und2K0QrbWliQ3Q5NHQxUW53cUM0MUxheURZa1RiZTlodzMrTmlmRDRIM0RLSHpVQjl4a3Q1UlVSVUw2TXRFRG5kaU0yRmc5QWltb3JrZjBrOUovWWh4K0QzZ3FoQUd6WWxOdUxrSE40ZnpWSUsySkd6ZEJiNHFXdER0Z2w4Yzh2b3M4dXpwTStZMWRBekdXWkdvN2N0NDVLM0wrMXpBPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0JFcG1yT3FybkRZNzlqMjg3aGNZaWtkZkN4RTVKaVBaMEtpR2pYZ2IxM3BMTVp4RkVyVURYdjlxMjNoK0p6Y0x2b3NidGFnNGFaR29oQnFjOFE2VFZMeEd3WkhLZTNvdnk3aWM1aVJvekJIa1dLMUpHQTBPTFZJaStpZU5kbTIyMDRzdThKQkIxbkxtbW41ZlNBSzdWTHdPbXQxcG85WFV3bUwxV1diZldMVkFoVUFtcFpibDdITXBiNklra04vOU45N2RHcGF0OXNDZ1lBUTZDQUpXcmh4Nk1waXpxYzVDR094dkx5enFFbjVwSDR0MU0wOFRPNkJyQTlHTXNra1JyZ1lFRGIrcE9GRHI2WlhZZUpxS2k3WHhhWXpXTEJRdS82cDF2dWIzSTZFNFR2QWpCZkM0S0V2WFlZS0dPUUpkWU12Y0ZUUDkzejZ6ZmNlVnJnNWFhbTNwZHpYc0k3UTduS3YreTJVOHAxUVlJNm03MkUrelB5QVJ3S0JnQVRWdXBZNmQ0UlNocU5MdU84eEJWc1MrWVpWemROTkF6Zkp1YVR2M2tXMHllcmxuSmV1WldNb29xdkhGbnhBL0RHNUFUOUpHcVdEL1Z5ZzhwdWZYL1BURVVPY0xvNnBqZTBUSzhtdDNSQ01DRFJkUGg5T1BFNEpzd0ZXZkVPQlFOUmJkMlh0QlJBK3B3VDluMlFuRFVWWEhjREV2bkpreFpuMjlUUWNmcXdBQWhVQXFXWXBBQkUvWFlVN2lQelBHZ3YxZEFPamdQST0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNFbGZKOC9CaWNNZ2Vuam11UkJQZWlnRmMydUtBVjZvTHRqbXoxazQzQW9BY0dCU3VCQkFBS29VUURRZ0FFY2xDZVVwbXljSFpUSFJlRk5vanRzdGpmclhkd2V0TUxyMUVZNGtib0toV0ZsTHY0eG13MGIzUVIybFBWN1NpM2FTQnhhVStJYU1IazJQaFhhSlpxdkE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVVNlNLMFRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlOVFUxV2hjTk16SXdNakF6TVRVeU5UVTFXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0JFcG1yT3FybkRZNzlqMjg3aGNZaWtkZkN4RTVKaVBaMEtpR2pYZ2IxM3BMTVp4RkVyVURYdjlxMjNoK0p6Y0x2b3NidGFnNGFaR29oQnFjOFE2VFZMeEd3WkhLZTNvdnk3aWM1aVJvekJIa1dLMUpHQTBPTFZJaStpZU5kbTIyMDRzdThKQkIxbkxtbW41ZlNBSzdWTHdPbXQxcG85WFV3bUwxV1diZldMVkFoVUFtcFpibDdITXBiNklra04vOU45N2RHcGF0OXNDZ1lBUTZDQUpXcmh4Nk1waXpxYzVDR094dkx5enFFbjVwSDR0MU0wOFRPNkJyQTlHTXNra1JyZ1lFRGIrcE9GRHI2WlhZZUpxS2k3WHhhWXpXTEJRdS82cDF2dWIzSTZFNFR2QWpCZkM0S0V2WFlZS0dPUUpkWU12Y0ZUUDkzejZ6ZmNlVnJnNWFhbTNwZHpYc0k3UTduS3YreTJVOHAxUVlJNm03MkUrelB5QVJ3T0JoQUFDZ1lBRTFicVdPbmVFVW9halM3anZNUVZiRXZtR1ZjM1RUUU0zeWJtazc5NUZ0TW5xNVp5WHJtVmpLS0tyeHhaOFFQd3h1UUUvU1JxbGcvMWNvUEtibjEvejB4RkRuQzZPcVkzdEV5dkpyZDBRakFnMFhUNGZUanhPQ2JNQlZueERnVURVVzNkbDdRVVFQcWNFL1o5a0p3MUZWeDNBeEw1eVpNV1o5dlUwSEg2c0FEQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGQjJIT3NlL1ZFTnJzekIzRml4d2I0WHVQZldpQWhVQWpqb3haVEFYN1kyV0tGVUw5SmxabmZtMW9Ycz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUWRqUmJyTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlOVFUxV2hjTk16SXdNakF6TVRVeU5UVTFXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSeVVKNVNtYkp3ZGxNZEY0VTJpTzJ5Mk4rdGQzQjYwd3V2VVJqaVJ1Z3FGWVdVdS9qR2JEUnZkQkhhVTlYdEtMZHBJSEZwVDRob3dlVFkrRmRvbG1xOE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnZmw3VC81MVEzR1hXK2M0Z2xYOXJPNXdIV294T0g3L1NVRTdRNEZiZnUxSUNYeGpYZDF3T05IaXZ5TlF5dmd3ZEltQWI4OGFnNFIrdThFVWhBeHJ6UUtqd0RackNVRVNuYnYzaC93SWZwd2FsMmpaTDhZVGIxK2htSmNXelIwQmV4aTVsQWhyUUlWRHRMRzVvV0prem5YTmgwM2xBb0k0K1N0UXF0U0JYK1orNA==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVQVUVDcGpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBeU1EVXhOVEkxTlRWYUZ3MHpNakF5TURNeE5USTFOVFZhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQW9FVWpvMEhTdm1EWXlHRU1senE3eXZGaEpWdmJlVmltMXVseTB5eFU2RDBUb2lnYi82RG04UWc0dkZvTFJSQW5nNElCL3Q0UCszRG5ZU1lIemt1blFHMXM4aVZZTWhYUVZna3BsWWF1TGdPWUREYW5VTCs1bURaUlcwS2s2NXVDRHpuZ296Sm11S2FERE9RNFBmVXB3QUl1VlYvdDF0RFVnZWFlcm9zempBSjc3bERNRTlGbm02ajdCWG0zOFNEU2RWa2FoMTNrRTkyMWZobWEvZ3kxN2Z6SjBHUTdFemgyU3MvYXRYTmtqei94eXFwdFgzQ0NmOWkrQTBjTWpzelVyTUNTcGpFbUlMMllnUUw4QVNvT1ZDYjBMZlJuY3JVaktPcG5vNDB0OVZQVWxxQ29uRG9zeFVtRHY4S1ZRTHp6NzFLOUUxLytiNjY0VEJjVmo5UjlHUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQW5zL2F5QXNCcVhJMGt2R3E3eG8vM2k2a3pYcmxHcVJXR2xKM1AvYjg5SjFOZW1jMzB2RmlNNkRSVUpEOW9VMDVFeUIwNnRJa1B4NGhYKzI0STVPZTZiR1hUemc3OVUrVWpjaFZNWXVnZG5jZ1ZtTnYzYTRaZHhtR2FoRnlldmJCRkhkZkNFSHNRY0J4NEowbjdpSGMrdGVsRTdiYTBQMDQ0RmxQdVZnYlZid0Jsam5XNmpzR0tsZDh4S282b0VWSE85bWZuSWRRNXVub29RUU15MjhweThNeGZNa2c1enNZTUlsSnBBWFBPZUFzU1FMWVY4cE1MZ25XY01HbE9yZ2JQVXV3eEU2ZFpmcGRoSzBmdHFUc2puLzlnU3FwaEU4UXpweHNYZXZIZDlqeGNpZ1p1LzkzWnNqOS9pankyWlJJdlVud1pNQ2FRTnlsbEVsU3Ixc2hV
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
    
=== "Verification"
    
    ```
    r2#
    r2#
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
     | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:04 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:04 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:13 |
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
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:13 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:13 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:13 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:05 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:13 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:14 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:14 |
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:14 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

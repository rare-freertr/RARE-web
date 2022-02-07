# Example: pvrp ssh encryption
    
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
    logging file debug ../binTmp/zzz90r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQWtOMWoyYzZvYmxFMk94S1BoVWtodWpRUGJWZzNvYzIwcEpaUEswNEg3LzNjNEJMckVjWTk4aTVzM2IxQXF5QmRCUW9OVGxnSHFVdGdVSnBXWmVDQlFTcUlwWWNSRG1uMDUweHFnWmFYY1ZZcUpiR1RpTXhXOFdqNkcvVXNBR2N5VzdtbGlVMjNwMWZjcUhsMVpTZUprUXZydUUyNENXeXdRSXhDNGtXcklnQVF2T2dIRWhGb0NZMGhJeVo4YUluZ2pjUWFJczU3bG9IRFBFNXExT0FaRkQ5SUo4MFJyZFdxNmhEQ3JDcXdMNWU0TmREdmIwa3ZaNmpiSzRkMGlaUHBjWmNmUUNJVk9YUjFuY0QwNHNGbVZiQnFSSnc1ODhSekVmUzF4bUJnRGtzcU9OeGoxaERJaFVNRTY4ZkJxTWZsVURxTXJZL3daS2tENjRLQ0lVVmJIUUlEQVFBQkFvSUJBRTdWdkc0ZXNiaC9SNlQwSDlpb0NNdTlZeHZkWTBFUm9obmpscWY1YWdabnY5ak5VdEcwY2FlbkxpV3B4VlNiWXlQSDZaL1Y5aTFpVU1Mc2l0SWNVQnIzbTYrQkJuNHltVTE2WDRld1BUQTNkTzVZYWZLTFNWRk5FTGRBUURiajhockt0OVExMEJrb2puTzh6VzlFQ2ZBK2JZUTUvMHBadEwwYjE1WXQxY2pGS05uM2Y2Y05PaEJkMGw4amt4K0lQZ3pDV3JlbWZmVDBBNUI3SXpneEFndGpyS1ZPekFZQWhKT3k1QVFPNFhhNUVnWEtyZExveWs0bncvR2dnR002VTNwVDRPZjA2WVBQcE1tN01hQ0RTZzEvMlVzK2JyU3RLaElSVHdUQTVGRHJHU1lEQzQyRmVIOVZubFhxNVBBQWNNQmFnQ3FHcTNvaWM3d0ZmQXRyNEwwQ2dZRUEvU1JmWlgzbStmMDFlQUtqQzltOEdUTUpQL25xMUlhbmpIUEZDdllUNm9JMnZ5MDAxS3QySW5ETjVGQW5CbEhJOHR0SzlGV2ZaeFphV1RPSWZwQ2RDdmxEMjliUUtpM3NieFJHWW1hdGx2cXExMys3UnJUdnMwd29HZ0ZJdHZuSGpqM29GdWVRVWtrRzF0RVRSQXpBT0FWdi9RN3NQaDFyYkkwbUd4NFlTMU1DZ1lFQWtvQVRlZU5mOG8vOGJKYTl1TzZQeDJ0RHozVWFUdGVlOHhJVGp2bitONmVpT0pDZncvdnFsaVZpVDFOZmMycnR2UHd6WGExb3ArTmlPMXRiUXV2dWFtSmRqOXQyMzdFTHFDYnRJUWFQc2xLTG5YRWkxRkNubSt5dDR1eU16YXJTMmxkVklqS1FBbElaSUNXSTYvd2gyMFNqVXFaK1JWR3ZXUURwQkYvU1ljOENnWUVBOGtqTDNaSUJicWZCYzFuaXdFYm4xNTZYYmRvL3ZxWWEyejA3RE9DMTh6QXFRaFI4aWtpSnl6RDRmMXVQM21hTTFKUzdTdHhnc3dRYitXQnZkZVBueTBjRWdmYzZTZ1NtVlRLc295WHZZNkFMd0RLTEJvUExJR3IxdnQ0WHdMbVZIRGw0VitQT3FGTW83cFl4d0dJTDRCS2tPeXI3UmdCV2Z4RWh0YmE2UGUwQ2dZRUFpa3RSRjF6bTlDbXNGaTN1aHliY24xbkl0NHhKKzJkY2F3VURaWkxrd2xFQ3QvYitlcG5TaDA1ZkVaY1lvZkdzM3h3TXVUKzdiZEVlcC8zRGx0YjFSNFAzNHBkQURrWXBST0VLTklUbkhXVUMydXN6Lzh6cmpDdk9za3F2V0c4TGdJVzBuZ1d4SUIrMERENmlsSEo4MjJwZDZ1VzBpV2RrNmRZTUljNzY0TTBDZ1lFQXN6R3RVeVRpNzVrc09KT3RiZFRVenl4MlZ2N2RtcjVvRi8yYThmYUlndXJKV1JEUG1wV0NBRCtYNmJiM1YrZVNjd0lJTFQ0V3ViaGM3MnBwT0c0TzZsR2R0b1M1K09mMDdGNWtxc0hCeHBWbFN2djdnRnlERjR1bml4WE9qMUtPRnlxZVV3UjJrWG0vc3ZDU0xsV05NYmgxV3JZaGNTS0FURkVmbC8xVlRNbz0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ErOVlLYkRlaHhFQ2FjUzdjU2dURnRYSEVhejU3ZkN1Nko2UVBkUWlTUkFjd1BUMnVqaE04MzZ0RWI1L0RrRHZFZjRPSTNwaGdGUTNMb1B2NWZJVUNlTU95WkIxSllFS1dvWG1tRmVQd1NrcDFIMis4MDJwd1NBeTdyelJzUUtWUElMRC9LdHFkR2MxRHFJUC9UVjFpekRicDZHT25PeCt0cW9GclBTcHdTakFoVUE2UzlITkloZkNDUVZneTduUEFpei9pUVU3WEVDZ1lBTlZVSk51RTFOZ21KRXFCZktqOWY0bkhRWG5iTWhvZkdHTlUreG9MZkw4YlNENDZyQUxqb29wZGlacnRMQy9lYW9JaXYrNWxaM2pHZmJEYUJKc0ZJRDc0ODYwYUtRa3pJM0E1dWE4dGV2L1hPRmpkT0RMcllQOHhTZnRVdlhlU1BrRGh6aTVMREFvL2tEUGtMTmpWOWE4c1JDUEJPME0yWG5GVGxKY3M2QTJnS0JnQWw0TEFpdlpENmJLdlE1ckVVK1JIdkovcWNuUitQUUZBczF6Qjh0N0kwQVRybldPTlVtLzIyQ2RIRE84T3ovcjJWYzVpa2RScTlmcGd5K21MMFN1NHRBRUFRSks1K0NBMk1GOVcyMU1iTnlxRVdVVytaaVFBRVBFTFBWVEswYlFTSitDRXhhbzB6Qm9kNjdjczduMGd3ejd6aThVL0wvMUI1MEpRSnN4RUdEQWhRS0s0b1o1RnB0Q3BCU28rVUFTUzFVUElEdGJBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURHbTdpeGh6cEhVNTR0d1BxWEFVRC9jWHBZSFNqcmczb1VMNnBEcTRpZG9BY0dCU3VCQkFBS29VUURRZ0FFbTJWbDk5akxpRHhHMlI2b3RZQVFMK08rdkw0eTdkN0NnNHZIOFVJZUZHV0tqaVJwU3pYaG1NZjVrcDA4TEF4TVpHWmhacFZEZE1ZcnRSREtjbkk5aEE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVGR3FXZFRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNRFF3V2hjTk16SXdNakF6TVRVek1EUXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ErOVlLYkRlaHhFQ2FjUzdjU2dURnRYSEVhejU3ZkN1Nko2UVBkUWlTUkFjd1BUMnVqaE04MzZ0RWI1L0RrRHZFZjRPSTNwaGdGUTNMb1B2NWZJVUNlTU95WkIxSllFS1dvWG1tRmVQd1NrcDFIMis4MDJwd1NBeTdyelJzUUtWUElMRC9LdHFkR2MxRHFJUC9UVjFpekRicDZHT25PeCt0cW9GclBTcHdTakFoVUE2UzlITkloZkNDUVZneTduUEFpei9pUVU3WEVDZ1lBTlZVSk51RTFOZ21KRXFCZktqOWY0bkhRWG5iTWhvZkdHTlUreG9MZkw4YlNENDZyQUxqb29wZGlacnRMQy9lYW9JaXYrNWxaM2pHZmJEYUJKc0ZJRDc0ODYwYUtRa3pJM0E1dWE4dGV2L1hPRmpkT0RMcllQOHhTZnRVdlhlU1BrRGh6aTVMREFvL2tEUGtMTmpWOWE4c1JDUEJPME0yWG5GVGxKY3M2QTJnT0JoQUFDZ1lBSmVDd0lyMlErbXlyME9heEZQa1I3eWY2bkowZmowQlFMTmN3ZkxleU5BRTY1MWpqVkp2OXRnblJ3enZEcy82OWxYT1lwSFVhdlg2WU12cGk5RXJ1TFFCQUVDU3VmZ2dOakJmVnR0VEd6Y3FoRmxGdm1Za0FCRHhDejFVeXRHMEVpZmdoTVdxTk13YUhldTNMTzU5SU1NKzg0dkZQeS85UWVkQ1VDYk1SQmd6QUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUROWm54STkzdG0zTVYwelR5cnJaVXlmYXhqUWdJVUUyQWxlWWVhNUNkSGJ1MzRKU3BCYUkvSjRIMD0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUmZNWjRRTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNRFF3V2hjTk16SXdNakF6TVRVek1EUXdXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTYlpXWDMyTXVJUEViWkhxaTFnQkF2NDc2OHZqTHQzc0tEaThmeFFoNFVaWXFPSkdsTE5lR1l4L21TblR3c0RFeGtabUZtbFVOMHhpdTFFTXB5Y2oyRU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU1IU0RnUHN6ZGpjbCtWYU9BUGJPcVpZRTg4Ynh0WnVHZ2xjc1ZXcXcyeG5BbDlRVnFhMC9JaDBtSEFTUFdtMTBmQ0lJcDVReW10WHNEWVRUY1c3Y0NVaGtpWHNLcmdKSVI1Y05pVGxDNkEzNWJTejQ5SjBhb21Ed2lZeFM1T20vMUVMZE5UNjFLK0RTOEtiVDh5MUM3SjJ6c0laYXpJU2ZYNFVoUzkzaWxTbFBBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVSVlNzUWpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVE13TkRCYUZ3MHpNakF5TURNeE5UTXdOREJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWtOMWoyYzZvYmxFMk94S1BoVWtodWpRUGJWZzNvYzIwcEpaUEswNEg3LzNjNEJMckVjWTk4aTVzM2IxQXF5QmRCUW9OVGxnSHFVdGdVSnBXWmVDQlFTcUlwWWNSRG1uMDUweHFnWmFYY1ZZcUpiR1RpTXhXOFdqNkcvVXNBR2N5VzdtbGlVMjNwMWZjcUhsMVpTZUprUXZydUUyNENXeXdRSXhDNGtXcklnQVF2T2dIRWhGb0NZMGhJeVo4YUluZ2pjUWFJczU3bG9IRFBFNXExT0FaRkQ5SUo4MFJyZFdxNmhEQ3JDcXdMNWU0TmREdmIwa3ZaNmpiSzRkMGlaUHBjWmNmUUNJVk9YUjFuY0QwNHNGbVZiQnFSSnc1ODhSekVmUzF4bUJnRGtzcU9OeGoxaERJaFVNRTY4ZkJxTWZsVURxTXJZL3daS2tENjRLQ0lVVmJIUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFoUWlqVU5HTDNHdHpUMFB6SFhuQlB1V2dzakFRQW5RQ1hzRlNzbXJwanZMem5xTy95WmRvbnVIUzNKQmdkR0NMUmdvUWJCdDVNWXBZc2VmYXJmT2k3TUpTODlrNzdWdkdpNFdoaVZqN1dQSUZ6eGhBaldiSkYyeTVNS1FTM2lWa2p6Y3NRSnU4QXVTVWtTS2ljSmQ4SG5YZm0yZmIrTmJGdmVGMVdXNk12N29SQW5mbm96Q0FiUkpPRzVFc2NwbkNWWnBhb2VlUURDd2FEM1krOEZ2cWxqSXNFVjJZNkQyV0FFT2lrYUM0VmRERms0U0VvczFsZVJtZHhSQkFWajJJc2lkb2p4Y0xja0VuTFlmM2ZnNlFKc1RiV1luODcxVDJhTnV2eE9vd1VEamFzQXJ5cTdROExTSm5GcTBlUE5RTGw3MUlLbnY5Zjk5bTNxbDZRQkpCNHc9PQ==
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
    logging file debug ../binTmp/zzz90r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCNHBpZWRUZzB2VEQvUytYYVRHYkZFNExhOWF5NGVNczRVbG96VmVOdkN1cEhuWFNNelg3V0lkV0ZDY0pOcXBOVWJxaksrd2Fad1hSbWMvRTl1djVRaFhoaXF6YU1MQ1d0ZWFEVEJPdW5hVWwvOWZ2TTJIQ0o4QXdmbjROT0RaTDU2RlBWNVA2S2hobko1TUZzY2pOQ1VDMjFvTVREUUx1YkVvelpzcmhpUW8wTzBvV2ZlRHBTZjkxOFlzMFRBUTdmWDREb2p4eWN4MElTeE9mak9KWVMrc3NXWHFEZ0FGVnNlcmd1OWdNQlJxa3JZZWQ2d21pMUV3eTFLQjgyUWRsYS9UTFo3Rit3R2J0dUF2clphOE1nQ0tsRXdxT1BydkZUWWxHNkQrc1BBUVhpdVdWOEFXK3FJL2hxazYrU3kyRDdWZUJuamFZR25qOFFZOXZUVnRYd05BZ01CQUFFQ2dnRUFQTnNLaGxVVlgzTWxpbVJjaEF4a2x5cUY0bnVLa3A3cnhnUytXdnNRVm1QSExwMlRJTm00OW5ER3N6MlhqaVpBZkNqWVdkSFNBMEZpcHdXNWgxSkpCSit5NzR5MEhlQU5jVnc4cCs3d2dEZ214UFhnOWIweFE3NC9vWjJNOHV6QkMxRkJGSHlkcXIzblJldTNPV3BwMXhNQWg1cXdWWUlpMHJMRXhBTDR6eE5wQ0k1VnMzelRGdUFLZ1ZDVXFGVWJnSk9qQUJ5ZHB1YkkzaVVHTFdwN1lDTnAvVTNnam5MZVpZdVlLcFpydm5haXE5RUlNQTMvYWFIQ2tGOXNXTWRvT0ZKUXVibWtOMzJPOGg4WjRtUE14Q2RkSE1mVzJqMVBDUUgyVkd0U1hTdThOVXYyYmRXRHpsZ3RVNE0rUHNBb2VsUzNNNEZIeElqNXQ5T2twbmc1QVFLQmdRREF4NFN6VzQyaG9ZampQWXdBUXNWUmFlVXRtaEY2clpkcjdUbkQxZU9CRkhVb1A1K3V0N3dDNGl4UU9wdFJlZk1vNWduVlRHRk1ETkN1Q0pGYk1zd2tVTDAvWEtyS3BBcUdMMEgxKzlMRDZONlpTUkl3L295TmVGcUJjdVA5M05PNDNkTFlNSmVwVmpMUkpobmpLTFlMemNLZGltNThlQ3FNTGRhTVV4MGFUUUtCZ1FDZ053MEhZN3RmN1JWa1A3MzhRTVA3cDdCNXdaNDE5dHRteGdQZ0N5QVlxWmVBSkljWDBkLzhqTEMyQk82cFY5MEtGMlV2NFNaeDZBS2liY2huNFBCTUtRTnJPVFB3b0RjeVd4RUhrMTZyenJ2T1RMeHNmQkxZSjdXSlRaTG9EVTcrZnZCa1ZnTkRwNGZBb25KdDBhdmZ1czY2U3E1WHcxRy9YN0NDTkZ0SXdRS0JnSEtqODdFcFo3OVByWFRkTysxSHg4bVRmTHN5bk9Sa2FPREFzUkpabHJKRE5TeWJNVjJZVzlFbktRMEkzU2FGcSttTmF4bVNFMlpEVkxHNTNKN3NSV1B2TTZ1RGN2bVF0Y1Y0UXZTQ0xhTmRUMHErbm5mT1dFMGsza1dPeWpCRWF3L0xzai9vSGJpUXp5VjdUL2U3VlE4TjdJYjlOSmtHYU43MXYxbXhiMlFkQW9HQVdqL0llaEltK1prK2hKTVhmU0lxZy9icEJSMFk5d01RZ2lzbkFheWlydUhSY3FDZzdMMFB0RjY0S0VCTkJGMTNLUGtXeWNyRmNrS2tRVVVnTDh2WThMM2xyQit6NzJjQTBML1ZydlBIejNZTCt1RGsveU5CSmp2d0dlRDEwUHUyTk12aXRGSnpVa2ZydzRwK2RQZzRIalpIdjA3VU9LSFF5Y0dvVnlBUkQ4RUNnWUJzbG04MXZyRzlrOTZZMDJHdWFnbzZ1OVNYM3VDOVBVYXVhMTdObGtiMDFlZHQ1RzI4WElHcjZFQ29SRkdRcW80a1BzUHJmSmI5UHQ1V1MxaHZDUjhydFdib2xUYlkrNU9PNTlxNXZtVmNPd280TnBpUEpRa0krTDhUSVVXVW9VdXNpOXRoUlplVmJHVG1XR3JoSTQzM0NXREpSd1RMUzYwVHJlMHNqbkpXV2c9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVBSUJBQUtCZ0E5amtRaUs0N3B1ZjkrVks4WWxpNW5wRVNaNDdNYWJuQXRwZFh4Znp3Y3NwZW1kRExabEExMUs2ZEdvZUJZa1plOC83V2paM253SEpGR3FJK25UbEtZMUFPVGt1QnhwZURabnpvSGFEcnFjbmltYzdjTUd5SmpQV1UreGJMRHNFcmVvUU5uaHJ4MnpqelZFMXRscGkwcDNCa0hoekJzMmNvckpqZjNYa3dlNUFoVUE4MFJPQldKWG51ZWhkeGFDanFpUzl3SXFPYTBDZjA4amQ2bDVGRGU5YWNyd0JOSGgwQTZiNHNrNGxBeitIT1l6bmpKUC9UT1ZRR0NIdE5iN0d5bERSaGhPVXhGbFI1V2JUNmozeU9jQzRKazdiZTA4WkNCdjhiUmFZc0tCZWN2Vzc5U29ESVJjV2EvTmZvSU9zamVkMno0YzVFY2hvVWpBM2FRdFNzWXBjK244K3FhRmZ2bFA5RUdtSnYrN051L3U5MGFhbWF3Q2dZQU9MQ1hoN0QxWlpWNERlTUkrRU5TQUZKVzRSaHN5aHBjY3NTdlE4c0RpZENDTllqdjd6UDJGYkRZWHdsU0NzNlN6aGRQODBtK3ZnYnd1bzRXWWNIRzFGZHNnbnJXSG5SNmpsM3BvbUh3a0MwM29UenhVV2swR0tEN2tlS1FwQ0F5UHBNMVhlR1lVcUxyYnRlNGVFTDkwRUlmWjYrT1ZZTzhMdkxCUXdNdm5DZ0lWQVBDTHM3NUFqdG9EaGhvZWlUc2c3K0dzS2IzdQ==
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURyRkx4QmJFZDRITjZ4VU5Jd3JRNmI2YzZnL1BUTS9PTXJaZ09obmEySW9BY0dCU3VCQkFBS29VUURRZ0FFZUQ3aDRCTVFDK0ZHdUZJOVVSb2hlalpwZkN3SFhCNHhKcFI3REN3RVZqbEJmc2JuOFVUUlFHcHc4d3d5empBZ1NXY1dSMEY1TG1iMW16ZkdNNXd6Tnc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZzJnQXdJQkFnSUVCUU9xRmpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXpNRFUwV2hjTk16SXdNakF6TVRVek1EVTBXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYk13Z2dFb0JnY3Foa2pPT0FRQk1JSUJHd0tCZ0E5amtRaUs0N3B1ZjkrVks4WWxpNW5wRVNaNDdNYWJuQXRwZFh4Znp3Y3NwZW1kRExabEExMUs2ZEdvZUJZa1plOC83V2paM253SEpGR3FJK25UbEtZMUFPVGt1QnhwZURabnpvSGFEcnFjbmltYzdjTUd5SmpQV1UreGJMRHNFcmVvUU5uaHJ4MnpqelZFMXRscGkwcDNCa0hoekJzMmNvckpqZjNYa3dlNUFoVUE4MFJPQldKWG51ZWhkeGFDanFpUzl3SXFPYTBDZjA4amQ2bDVGRGU5YWNyd0JOSGgwQTZiNHNrNGxBeitIT1l6bmpKUC9UT1ZRR0NIdE5iN0d5bERSaGhPVXhGbFI1V2JUNmozeU9jQzRKazdiZTA4WkNCdjhiUmFZc0tCZWN2Vzc5U29ESVJjV2EvTmZvSU9zamVkMno0YzVFY2hvVWpBM2FRdFNzWXBjK244K3FhRmZ2bFA5RUdtSnYrN051L3U5MGFhbWF3RGdZUUFBb0dBRGl3bDRldzlXV1ZlQTNqQ1BoRFVnQlNWdUVZYk1vYVhITEVyMFBMQTRuUWdqV0k3Kzh6OWhXdzJGOEpVZ3JPa3M0WFQvTkp2cjRHOExxT0ZtSEJ4dFJYYklKNjFoNTBlbzVkNmFKaDhKQXRONkU4OFZGcE5CaWcrNUhpa0tRZ01qNlROVjNobUZLaTYyN1h1SGhDL2RCQ0gyZXZqbFdEdkM3eXdVTURMNXdvd0N3WUhLb1pJempnRUF3VUFBeklBQURBdUFoVUE3bUJBeFJZQWRuRlllMDByTytELy9OZkdlSFlDRlFDUmgvU1h2WWg5dE1lVmJVMzVYQjJpTk4zNE1BPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUTFGWnJETUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXpNRFUwV2hjTk16SXdNakF6TVRVek1EVTBXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSNFB1SGdFeEFMNFVhNFVqMVJHaUY2Tm1sOExBZGNIakVtbEhzTUxBUldPVUYreHVmeFJORkFhbkR6RERMT01DQkpaeFpIUVhrdVp2V2JOOFl6bkRNM01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUpkcmpOcVZLb3RzTnRCWkQzaUZWOHBrRzRzdkJsSWJOQmtkL3dyMmtVeWlBbDh0U1FhNm9wQm9ESHdmS20vVVhvbERieVVSQ0hWR3BsQ3FlR3JZNmtuUlNzZk9YY29ISWJ4TGFtTjQ5RTZMeHJaM2h5dk5NZy9rNlY4NFpSY0llWmZFWW41UlIybnZ3aXVIRGhlck1TclBLV1hOOVVDc3VFNVV4bTdkQUIrVUFBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUViMnhsdVRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBeU1EVXhOVE13TlRSYUZ3MHpNakF5TURNeE5UTXdOVFJhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCNHBpZWRUZzB2VEQvUytYYVRHYkZFNExhOWF5NGVNczRVbG96VmVOdkN1cEhuWFNNelg3V0lkV0ZDY0pOcXBOVWJxaksrd2Fad1hSbWMvRTl1djVRaFhoaXF6YU1MQ1d0ZWFEVEJPdW5hVWwvOWZ2TTJIQ0o4QXdmbjROT0RaTDU2RlBWNVA2S2hobko1TUZzY2pOQ1VDMjFvTVREUUx1YkVvelpzcmhpUW8wTzBvV2ZlRHBTZjkxOFlzMFRBUTdmWDREb2p4eWN4MElTeE9mak9KWVMrc3NXWHFEZ0FGVnNlcmd1OWdNQlJxa3JZZWQ2d21pMUV3eTFLQjgyUWRsYS9UTFo3Rit3R2J0dUF2clphOE1nQ0tsRXdxT1BydkZUWWxHNkQrc1BBUVhpdVdWOEFXK3FJL2hxazYrU3kyRDdWZUJuamFZR25qOFFZOXZUVnRYd05BZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFBMW9qdDlBdjhwWTEyMDQ4UjR3ZkFGekd4ald4YkE3cW9iYzBSTzJkMU82ZSt0YS9xT0ZZWktJU2d5dThjdkt2Uk1pQUNISnY4SkRTWm9maXNxWThkVjNnQ2hQS0JURFZ5Z09DS0xwRGh6aEh4QmNaQ0hTWEZ6Q2Focm9weER2UmdWbXIzMk04UEZaaXlUdHROVXBTNFpmNmYzL0JNbTFXODE3RGlUNjEzNGh3RlE5c0s2QlFnOW4xN0plWVhHWGJXNFluWWwwdGlnc2hWNlFUQXhpMzJ2M0FMSFF0Rmp5ODFra2JNWW9scEpuQ2dBbWMrcWh5U3p4QTk2VklwMy9rbHBOM0dZZkx1NlJVNVYrSnpxOXVZcUZQaVlKNmUvUWp1bUE4SmdSV3RHaVQ2Y3U4WGk1TTdCU2lrcmJrcWtpdmxyaVVZTnV4dm9oZUpoSTg4MmUxSkk9
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
    
=== "Verification"
    
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
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:07 |
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
     | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:02 |
     | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:07 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:07 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:07 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:07 |
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
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:08 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

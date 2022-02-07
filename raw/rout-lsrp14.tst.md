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
    logging file debug ../binTmp/zzz13r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWdSck9Ja0dGeVBYVjk5NVRudTdvUGJ3U09uZW1waUk0bUZFM2lhSUtSYTdENDZ3Zkl3cVpxNXovTUt5bHA5cmluNjdTbE9GSDV4U0tDdU05VmFGeFA4VC9uelp3QnkzNktEV0hIVHFXTWV4UTZsYWoySTVzcEs4OHlnTWZjL3NYQmNQTkdqdy96K2JyQU1WeXU2QWsxMHZRcm10NXpWTzJDVS8wR3ZsRkNjL0t0RlMxNXJacmJuQVBUd1drTkJrditxN1FZMVNqaHRrbmVCMDlTd0JvbERYWkxhRm5SRUxrUW1PbEdkY0UxaEhLb0wwOUdDVm4yUFVBN2IrejM3bENHajBXUEw2MEVhRnA3RHVhS3ZSQWgwcHNVanhjUENLZlRvMWdJQ3NIZTBwai9yUGEyOExBdlNmeW9BNGdwTitFVkhZU2ZJQUdUTGdJUzB3L3E0N21wUUlEQVFBQkFvSUJBSEFzU0JuL2NDeFJYTjJHY0lWUThyeGc0ajJtcEVjSXlMK2ZJWEFXT0hLZkRGaU92bWNGMk1zQkY4REU0UkhjM3JiN2dNQVdsUkMwQ2RTMzZCeTBydDlIWFFxS2svL0k5T2RteXNTY21NODdrbnBwV09iWnFJL1dLaTBqVlhyQ0dSakxMVE8wVVlWa0Q1K1Y3c0FTdnEvSmtjRmFaSFFBWGRQdGdoekZwRFNHOTl6WmdqdjRDSTVqanlrWk03VHdFczY1MHY5SjNsRTB0Z1g3dlkyV1RYcVdZTUhOTHRScE1YRVlScmV3MDF5VHZQZUd6QWtYSkFhdGt6amVSUmNyc2s3S0NVc0lyNGVtcWg4VnZuYmI5NE50NmpSSEkwVUxDMThWTkxOUGNYSGFWWVRNM2EzT1FzWTlWQ0dmR2x6Nk15aEtST294UDAxZGhYL01NbmlTNXlrQ2dZRUF3dHhxQkp3V0dmcU1vYjRCZjdQZnA5NStrSjVlL3d5WFVZY2hBbTJWMW8xWURDVGlRU3Z2OHpBVU1aOVdheXBIRzFsZDBwVU1GM3FUOVBuVy9LVloySS9LMW56STljME9JRHdka3RybDhFZm5iVWxSTEJQazF5N1dWR2lMRk9lS3Q1L0RvL3k4OUp0MENlb1NiREJYUGNnWTZqT2daUTkyQXdOa1VJQ3VtSzhDZ1lFQXFaeTZWTEIyeGt2MHhsc0p0cmpEMHQ4bzIvZHZQTnpLb3pDSi9CUmRXUlE0TnVhSXJNRlA1emNtZFk1RW1EVkhCY3loSHFRMXJXeHhtY1orcHFRWitQSWI1SzJVeU1KeXJTTGd0VFVvK3h2YXZUVFlmTlBxcVZZSDNRRHFLM3o1VnQxVTVDVTRhdUticzdONlhxWGdMNWNzcEdsbFBRWnNZcHVaNmJKMm91c0NnWUVBdTlINk9tRThpR1BRbzZIaURmWVJrTnZMZ0plMkZ2NUs2Q0ZvZHMrcnluYkl0RVBrOVU1bFpURWxkY01RYUJFREl1QmJwN3RVUVZrOFBiZUhPbFFpcXJQR25rRCs3clZzZFRPY2ljMkdMcmtQMzIzNDJKU0FVY3pxZDhlZ3IxQ1NpM1ZwL0ttQ2MvOVd0S3V5Z0NlRUg1KzhMQm9BOHdnWkJzU0JMM3NwVHk4Q2dZQkJoM1BWMUhlUEZUbDBpU2V2bUtMUGpiaFRnNzFPWGw5THZTMFNYeXZSaHFaUlQ2L3VUcUY0U3k1b3JKYUQxOUdndy9aYnlFV1V3eGtBdUZlbU9qQnVwZHR3OWo5TmNSS3RJWlIvYmhKdk1jdkkzZW5tRUZuUklwUFhKc3RTRWU2alNNL0xkVFhlMWI0aUoyMVhzKzV4ZEk2aTFyVnVabFRwcEFSSzdkQTRFUUtCZ0N0VGUyR3RJdmlXNkxYc3RRSlFFdFZRLzcwVnVxZUZPWDdlaFZUZHYwWnVVU2JrR3VQdkI2d1JOM25hQVJEUEthdkdSbEgvWXNObWVmS2RZbXJydjZhYXVIaGxCcTY0VE5BenlyQ09OSU90N1I4cUpwckxpWTlXS2VoN3A3MTVIdzRsbktQYkVwNmZEYjJybHN3WVUvaEVKbmdVY3ovOUJxZ0VKN1h3QXdHOQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0Z4SDhtK3VzbEs4ckorYTROQUpyamdsdkNCM3RPSjluNTFNYitrUVBoNWcrU1Z3cGFMWEdhWEN2U2hLUDBEYzd6TksvZHRtdnVWM20vUURmL0dGOG5rZjY0M2V5YUkyLzVmRkwyMk5iam1XNWlpcERVc05Fd3ZFQ3I1S2NHYVJEUm12eXpEL2pLUTBDWXFxeS9XSmNmTGFvRXNHSW5vQUl5RmRRbnJad0lFOUFoVUFnNy9VTXJFNCs4NGgvTVhnSWF6ZjdPSmNHMWNDZ1lCV0hLYjFFNThWUnJidmN1R0hNampsQlpWbWVZZHQxeUtVUS9NN0VOaEo3KzNWNHNKQ20vcWU0eU9vdytJYU5XUllpMDNUeExZTTZadXBSdzB4Q0pJY05ldmR1SVBkY1NxcDVoWTM3UWM1VnRTTy9YaGhscHZEQjkvdHhQc2VYWDV1TFlEMEVGMXdFT2FlcE5WenpJTzlUeXJIZEk1MUFQQzNGc0RvTWVKU2tBS0JnREZhSS9kQWh3S3daZVBsM05XNC90NnVoak5yWVlqaUJ5SzNUbkhWWVAwa2JXYmNKYlc2TFZ6MEpBN2lNM3BDV2xWTmRRa0hqVkNIZExRYUtFVzcveGlmZG5ibjExb3dZdFdCdXBXb3lFbzAxb2NDbFVjZHl1aGJJMTBnc1hHc01WaGJzOUYzQXg5RE9vL3RpSUxWdUdYKzlDajQzL2NucnZBeVNad21zaS8xQWhSdWxURW1oWTZoYi9iSUNPMXR6R3hWM2RSbDdBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNLTXUyN3Z4ZytxN2drNlM5eUdVU3Btc2hlMG1SbEtJWGhLdVduQlcrMG9BY0dCU3VCQkFBS29VUURRZ0FFbzczUSszQm93YnNzSzdBVFhHUFpOZFEvV01EWDJMaEUyMWU2ak83MC9vRGYwYlZlQlRiNFowTWN2cC8ySXF6OVBxSUpORGRIK2N0d0ZWT3c5ZlVKWEE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVQN1haSHpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOakU0V2hjTk16SXdNakF6TVRVeU5qRTRXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0Z4SDhtK3VzbEs4ckorYTROQUpyamdsdkNCM3RPSjluNTFNYitrUVBoNWcrU1Z3cGFMWEdhWEN2U2hLUDBEYzd6TksvZHRtdnVWM20vUURmL0dGOG5rZjY0M2V5YUkyLzVmRkwyMk5iam1XNWlpcERVc05Fd3ZFQ3I1S2NHYVJEUm12eXpEL2pLUTBDWXFxeS9XSmNmTGFvRXNHSW5vQUl5RmRRbnJad0lFOUFoVUFnNy9VTXJFNCs4NGgvTVhnSWF6ZjdPSmNHMWNDZ1lCV0hLYjFFNThWUnJidmN1R0hNampsQlpWbWVZZHQxeUtVUS9NN0VOaEo3KzNWNHNKQ20vcWU0eU9vdytJYU5XUllpMDNUeExZTTZadXBSdzB4Q0pJY05ldmR1SVBkY1NxcDVoWTM3UWM1VnRTTy9YaGhscHZEQjkvdHhQc2VYWDV1TFlEMEVGMXdFT2FlcE5WenpJTzlUeXJIZEk1MUFQQzNGc0RvTWVKU2tBT0JoQUFDZ1lBeFdpUDNRSWNDc0dYajVkelZ1UDdlcm9ZemEyR0k0Z2NpdDA1eDFXRDlKRzFtM0NXMXVpMWM5Q1FPNGpONlFscFZUWFVKQjQxUWgzUzBHaWhGdS84WW4zWjI1OWRhTUdMVmdicVZxTWhLTk5hSEFwVkhIY3JvV3lOZElMRnhyREZZVzdQUmR3TWZRenFQN1lpQzFiaGwvdlFvK04vM0o2N3dNa21jSnJJdjlUQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRVdJdmNaMFY4R0VVbUZFYlA2L3Y3b2FGSGZoQWhRZm5hWFN5Z0cxbVhGNW5IdUJhVjNIcm4rWFVBPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUXVLS0VyTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOakU0V2hjTk16SXdNakF6TVRVeU5qRTRXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTanZkRDdjR2pCdXl3cnNCTmNZOWsxMUQ5WXdOZll1RVRiVjdxTTd2VCtnTi9SdFY0Rk52aG5ReHkrbi9ZaXJQMCtvZ2swTjBmNXkzQVZVN0QxOVFsY01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtKSStlSTN2WlhsZDQvUGplZ0tlUld3Lyt4TW1jRlh4dGdnWFlmOWp1MmxBbDhuNjBCbGgzbUJnSStZdlFvaHNSOWJISy82Y2U4VEttcE0zTGQ3WWpWQ2RBMFNPSnJQUDN6MzlEeTMxRHl6N0cveXhRa2FCdUFucDdnbU1oWGR5N1V5bW5wSEdJTFVqTkxUK3pTWElEYnJQaFBJNmoyNTViSEtFdklMZnRmWXdnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVMTnpCdHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEkyTVRoYUZ3MHpNakF5TURNeE5USTJNVGhhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWdSck9Ja0dGeVBYVjk5NVRudTdvUGJ3U09uZW1waUk0bUZFM2lhSUtSYTdENDZ3Zkl3cVpxNXovTUt5bHA5cmluNjdTbE9GSDV4U0tDdU05VmFGeFA4VC9uelp3QnkzNktEV0hIVHFXTWV4UTZsYWoySTVzcEs4OHlnTWZjL3NYQmNQTkdqdy96K2JyQU1WeXU2QWsxMHZRcm10NXpWTzJDVS8wR3ZsRkNjL0t0RlMxNXJacmJuQVBUd1drTkJrditxN1FZMVNqaHRrbmVCMDlTd0JvbERYWkxhRm5SRUxrUW1PbEdkY0UxaEhLb0wwOUdDVm4yUFVBN2IrejM3bENHajBXUEw2MEVhRnA3RHVhS3ZSQWgwcHNVanhjUENLZlRvMWdJQ3NIZTBwai9yUGEyOExBdlNmeW9BNGdwTitFVkhZU2ZJQUdUTGdJUzB3L3E0N21wUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQmU5cVcxWW1qV2ROOWlDTHNGN3FEYmdsL0Jya1BjNjlTUUk0citwNVAxRUxGcW54MVpQMzY4SUFsNm5wdEN2UVg0U2NGNm1jdlR6dGZTZ2VHdkFHUTNzcVZmL2JsRXhDcXV6U3E4eHVTRzB1NEptZ0N1djZuVXRwSnFVQVgrMnFEYTJKU2ZRQXlIdU9ieFEzb21qMllIaXZmN2ZtdjdjTzExWGdCRDFZVDRrc0RObnA4VExiVjNDWjM0YnlvcFE0UXdnU080K0N1YVhnNU45N3d3elhXZWVqNzZ4TGZEZHk2eUU2WHZ6THJkcFN2U2NpTk9jTUNJTHBUT2gzRkZjNFgxUUxZdU9zZ0RUSGlQbTBibWVKSDRaYU5oUlBoYjBGdFFla0h6NzE1RXpza1p4b3hMNzFZWmNJWEdadEt5UnpHSkl2OHU2dDYzSThIcGtrdFFMam94
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
    logging file debug ../binTmp/zzz13r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQTF5aEs1RmZrbWRvVTlSTko4cXFUcmxCd1lBSFkvZzQ3L0tXTGxGaW0vdEUzNEplQmg4ZXRJRlp3YThtRGJGNnBEZ3lOM1hxR1dycmw3VzJNYXQ4ZHFDL1EyS25PQXU2NGZHQnpvRnNxRVB0RWp6S2FsWlR2M2RHUi9wK1hDY0JpeWFLeUZkb2toSUFQejcvb1hQQlJJUnVaQzh1RkF3Z0xjb2FCek5mV0Nid1VldXEvVDREbnpoalRRSG02RDBTajNzRGszNEVOM2tpd2ZxL2ovQUQrcUttS3AvK2c0V3pKRC80Q2NsNTZtY0VORUxuazdVZHA5ajNjRDF0cGkxQ1I1Z05zOXl6VnE1N0ZlNjVQM1dYRzZ0UUtmRWx5OEczSGROZ09PVHIyVEpwTnFmaHppMjBrVWJiZHFzWU1DdEg3V2IzQk1aQ3hyNmtjM3A3Ym5nVzZGd0lEQVFBQkFvSUJBUUN2YnVZcDY5UzA4aElXaG9UTVBmT3V0VjM3bW1ZUk9SQUdnQUVnazJ5TzU0NzFMUFByLzQ4VmlBV2dqYTRBWmVyWVRybzU5ZGFwRWkyNmU1Rjc3ckxpMlNJa0Y4aW5zWGh4eWI5ZDZCZVR3eDF5MldNY1JsV1MrM2RjTTBwWEpDd29sdVU0VmlkaWRuenQrMTkrc0dDbWF6ZE9XOEwzNXM1V3NvQVJ3NGQ5WlFQeWRBYU94NGlSeU5SVnhSdjVrM2pMVGdJNnpIb212SWlHMG5iSE52TTNUbklBRWlsL2VPTFRMTVNpZy9YMEFDSVh6MGptTUJFK3ZxZEZUcHFJMnZreVJOTnFqcFRYSTRiRkZKTHFDbC9HT3BkZ0N6UVovVENMZG5zcUpjdUU2SWhja0RERGFuaFA2djliZUw3a2tDWERMYkE1NTkwMFJVOFFEZUk0Y0NVWkFvR0JBUFlJemh1Y1VWSXdPVlprT2dFOU9RWHNzK0pWTm1XOXBpcFZ3eTIwbTcrOGtLOGIyVmdFNCtOdHdvWWVQTmh6WlUrVGRlaExCYVpFNjZkYjhXazgzUEVsRGR4WFdWWVdlVTYwazFMVTEwWDUwT3FwOVd2WG5JTFhQWW92SXl6Qm04V0tzMmJ6cWRoK2JoN1dTb3ZaaHFGbjZOSjRDeHNuK1BxOHRMT1dEMTg5QW9HQkFOL2ZVTlJEbXdPU0w4VCs0MlJxTkgrNkYzd09rdEd4L0dCL29hRW1FV2JpaTh5UzkwYVJoNmVncDBSNC8yYlU2OGxCYWVnVElDdUlIeWJEMFdkM2lMLzFpWFI2S1dyZWQxQTF0aEFoaGpzbDE1ZmRGZGxEZFQyN3EzakllR05vS213M1J5dCtvVHNkRWFDVEZzdEFaMnNlSWthM211a3NiWUM2U0dOTXlkUGpBb0dBUXhVaGhWdTR2STBUaFIrc3hSdTVTWWxCZnN1M0drUjhZdnloUy92N24ycTlsRkVta0o0OHVJejd4ZS9HclVuQmJOSUxDdnd4blNVYmo3VTgvSEd3MkRzL0xUM1B5TzQxd3lUdktsMklHTGRGcEVZVStZTi9WQmwxMlJDREtiZmNUaDlFVFNUUXdZdXZZTThTNGxDOEtaUVlZaEtERExONGFuMDdVOS90YncwQ2dZQVpzc1hSaCswc2JNU0ZCWWxPeG80K056dG81emRkVU9RYW82d0hGcHFheDlpcVpCaDBobElmSU9ieWlqMHZMYlBmUjE0RDRPWXBlUmV5V0hvYU9YTitMWTVZeTRramxtUDExaVNQRjNvVUloVHNmdGw2Tmk4b0pmbmFCSkVsUUJqV2tVWGZMVXNPd1JoNzZVYU5rRmdPeU1mQWZHVVE3U09veWpsekJLYUtad0tCZ0dGOVllRkM4WEVQWFJ2NzQ4YnpVRmcrMkIrVGNZYUVDSjNKMkpIWmJMWXd6cUp4UTAwMUNiNDFnM2ZJSlBQMFloVmpRU3hlcWZzSHZVcEdQL1VrdStMbldqUGlOTy9HQXhNRXIwS0NFMG44U093c1BEM084a2JJSnZDV0hleGl0bmUvbExWWi9mMmxiSHFYbm4rdU5idlpxT0YxNysvK0lDck1DNnVYbmg1Yg==
    !
    crypto dsakey dsa import $v10$TUlJQnV3SUJBQUtCZ1FDRXo0TXJqRVo0VVJmU0VJYy81WE9PUlBOSVRncHc4bk1peTY4eXVISmgwbUVEQys2dG9oZEU4MGltSnN0Z1g2VTNXNjlMZmJhN0FJckhkSSt6RzRWR29XSE1tZ3hudEgyK0l2MnpVQjRKT3BIVmNCbUpEek5GU0txVFpMVlpoYnc0REUzc3pjU3k5UUtzVkdnaUZkVko1UXdoZUVKZVBvREl2RjQzenQxQkhRSVZBS2VuUDZJMzEzUkRkbnJFdzNZSUZ2L1dLa0k5QW9HQVo0dmRTZUtEMlA0VTF5S2FoclAxRU9ZRXllOTN3M2Jza1RTSTBCZlV3RHZnMVhkZ21LN01hS1cyYmlmQkVwTVlzbWIzZ0VSa1lJZnFvdUhmVzR1dWRjK2Y0SVZidEpwVjM5SG9XZXAybUlLYlNMME80RDFENkZzUWR4eFFZRDdsN2l0RkVsbzBHbGJwd3N6SmVnK05LT3NEQnZ5eS9jVnBKaVZ2MEFkY0FlQUNnWUEzOGpIdDBuWGQ1aGFsYkI5UDU2azU4ZHRRaXpJRWpWQTMxb0VJSm11cml4TWgyL3pQUVBNcHlEL0NlVmo3MjltV1V1UHJsWW1STXlRdWdhRkpTcy92M3ZrUGZ4Nkw2SC92eVhnMWpRR3pucWhJbFZQMHdYOW5PSENsRUVYR0J5a0pwMUMyc3hadWtlb1NXRWFiSVVmOFp4ZlYrcEs0ck9rWkMrd3JhY2JaZHdJVkFLclFoREt2NFlaV1lwaHpjeVBXSDhlazdiSjI=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMkNCSVBkQWJQTkZEMm9BUUtSejNyZVJkcnJ6a29DbG1EZ2F3WStwMVB5Z0J3WUZLNEVFQUFxaFJBTkNBQVJCSk11MWZwdldxSG1UVTJXSUlQYkVTOVRKSk5uTE1OTyt3ak9EQkZMTWJNbW9weEZBcytYTmZrR2xQYTQwSEc0YWx1aUhuczl6cmxiSmY5YkZQOHRv
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBaENnQXdJQkFnSUVUb1R0QVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlOakl3V2hjTk16SXdNakF6TVRVeU5qSXdXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDRXo0TXJqRVo0VVJmU0VJYy81WE9PUlBOSVRncHc4bk1peTY4eXVISmgwbUVEQys2dG9oZEU4MGltSnN0Z1g2VTNXNjlMZmJhN0FJckhkSSt6RzRWR29XSE1tZ3hudEgyK0l2MnpVQjRKT3BIVmNCbUpEek5GU0txVFpMVlpoYnc0REUzc3pjU3k5UUtzVkdnaUZkVko1UXdoZUVKZVBvREl2RjQzenQxQkhRSVZBS2VuUDZJMzEzUkRkbnJFdzNZSUZ2L1dLa0k5QW9HQVo0dmRTZUtEMlA0VTF5S2FoclAxRU9ZRXllOTN3M2Jza1RTSTBCZlV3RHZnMVhkZ21LN01hS1cyYmlmQkVwTVlzbWIzZ0VSa1lJZnFvdUhmVzR1dWRjK2Y0SVZidEpwVjM5SG9XZXAybUlLYlNMME80RDFENkZzUWR4eFFZRDdsN2l0RkVsbzBHbGJwd3N6SmVnK05LT3NEQnZ5eS9jVnBKaVZ2MEFkY0FlQURnWVFBQW9HQU4vSXg3ZEoxM2VZV3BXd2ZUK2VwT2ZIYlVJc3lCSTFRTjlhQkNDWnJxNHNUSWR2OHowRHpLY2cvd25sWSs5dlpsbExqNjVXSmtUTWtMb0doU1VyUDc5NzVEMzhlaStoLzc4bDROWTBCczU2b1NKVlQ5TUYvWnpod3BSQkZ4Z2NwQ2FkUXRyTVdicEhxRWxoR215RkgvR2NYMWZxU3VLenBHUXZzSzJuRzJYY3dDd1lIS29aSXpqZ0VBd1VBQXpFQUFEQXRBaFJpM3g4d2FPVkpPQmthWTNSMWMyVnErTG9DVlFJVkFJbTRLdTJSSEduM1krTForRnVXenpEdytCSUY=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUU45d3h4TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlOakl3V2hjTk16SXdNakF6TVRVeU5qSXdXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSQkpNdTFmcHZXcUhtVFUyV0lJUGJFUzlUSkpObkxNTk8rd2pPREJGTE1iTW1vcHhGQXMrWE5ma0dsUGE0MEhHNGFsdWlIbnM5enJsYkpmOWJGUDh0b01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBDc0tkVHRNY3M0NnpQa25mVFBYQUg3TlljQWNwR1p1ckxrWXIxUlk0RFpBbDhhSVMxc0cwaEEzTENiek81cWZOQVl1WURFZmxHamNkMUFGY3JidlVqWXdhbWgyemx0bWpybGJFSlZUclJmeTVpL24vMXNiM1o3c0hwUk5DQzZnTmpRcmpweEd0aEYxU3lHRVpWR0hESmFBV1RzcFNmcGJNWEp2VkxjcFJrQ1RBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVZN3NqalRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBeU1EVXhOVEkyTWpCYUZ3MHpNakF5TURNeE5USTJNakJhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTF5aEs1RmZrbWRvVTlSTko4cXFUcmxCd1lBSFkvZzQ3L0tXTGxGaW0vdEUzNEplQmg4ZXRJRlp3YThtRGJGNnBEZ3lOM1hxR1dycmw3VzJNYXQ4ZHFDL1EyS25PQXU2NGZHQnpvRnNxRVB0RWp6S2FsWlR2M2RHUi9wK1hDY0JpeWFLeUZkb2toSUFQejcvb1hQQlJJUnVaQzh1RkF3Z0xjb2FCek5mV0Nid1VldXEvVDREbnpoalRRSG02RDBTajNzRGszNEVOM2tpd2ZxL2ovQUQrcUttS3AvK2c0V3pKRC80Q2NsNTZtY0VORUxuazdVZHA5ajNjRDF0cGkxQ1I1Z05zOXl6VnE1N0ZlNjVQM1dYRzZ0UUtmRWx5OEczSGROZ09PVHIyVEpwTnFmaHppMjBrVWJiZHFzWU1DdEg3V2IzQk1aQ3hyNmtjM3A3Ym5nVzZGd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFwSVJJWDR4cFA1QVJFMDRvRStEaVM3cDlRMmlBTXdJVThVUExHazh1MW9EODBIcGRBczdyUVM5bFp6S1dnR0pGRXY3emkwbGxGRU4zMUxjdk45MCtESkNlYml3b0pzSUpHMlNBWHdIbllmdTlRMlVIMXNRZW9YWENLMWd2QzBUaUUvQVdBZVhPT3Rpd2lEcTlza3JzMFVUcmdXT2hmcy91ZlNLenFRU0ZNTVJLclVYakhkUTNOaDJocm1PZFhMMWhxeiswb1VkemlIZU1mNXBLSkJhQTFWQzFMTS8rWFlzTTMwUXJQaHFWWlRZOFp2U0pRVmJrQVd1OG1LUXlmeHlOaHN1MjdVY2NQMnJWV0lXOHRlYWE0cUt0eHljdERneG5QZ20xRkM4SVhOZXJtTTZXVGxzZ1NGdkJlS2pGdXB5L1ZLMitsUXZqcnQvOXJyRlI0MmtjR3c9PQ==
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:06 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:07 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 6   | bf1864f4 | 00:59:56 |
     | 4.4.4.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:56 |
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
     | 6.6.6.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:59 |
     | 6.6.6.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:59 |
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
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:04 |
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

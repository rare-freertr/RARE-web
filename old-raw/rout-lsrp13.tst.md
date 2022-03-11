# Example: lsrp ssh encryption
    
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
    logging file debug ../binTmp/zzz44r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCdkh0UGg2NHdlQ1VOSjR2NW1OQnNhNmNodHVRUlZOUGFCb2dLeEFRaWFGYmJLS25BbC9YSVRSOCt0aFFtSUFXTnJSajBkd0txZUZkT0xHNmt3M0tNeHlqdTFLNEZVUFN2aU5rL0NqcktBaWp1STJaVDIwbnNiOFNLaUdCNUI2VG10WGVESzdHM29TMXd2YnlxN1lNeTNNMVZQSE9VcEF3R1BFUGw1bGwwVy9vV0JHdkpsOVlzTWRSaUdzckUwMVZPSHIxRVhoVys3Rk1rSjd3K1psQXV2dFNYQlB3R3djdVRqN3o4S1ZLRUZpMTNlQ1YwVmdxZTJPMDl2UjBBTTFCeEtQK2l5bkUybVp6cENCVUlHMmMwN3RxUkZyc1h6R3hVSTJmZWdHQVdObWQ1K0pKcjFaSm1meklnODFBelZKcTBLS2NsN09RejlIb3lpY1kvRk5SakZBZ01CQUFFQ2dnRUFWM3JEZjlZNkp1TlA3L2tlSWtQZkd0NzFoVHZrNTFlY3dRMVVaUmpWTnNqbGNGN2NqMnZweExnQ0RTN3hBL3RqMDI0bWF5Zmtxak93cUpFTUw0VmpqSzBUT0Z1Wm8wSE5MSGRwYjFkN3U2b1htSE1DelJXRENjcGFZNVh0TENKNTM3eEtYamFuaC9yY0JoUFVabE9jbHBWNUVhRkQzM2VZWUpNU2MrQW1SUlR0WHNocFF0YWZLc1dyKzEwNHlRTTh6UTZxNzR5SGN5dWlucW1NWmRaT1plU1FseG1DWDRNc1JjaXNXdjFRQkNGYjRoSDRaNU1Mc1BtV3BnT0hGbWtUU2pENnJteXZiaXhRTi9EZVc0ckFjSVcyaVJBYkNuWm5CalVWVVBJNGNqMzkzd3gxU0ZxZTUwTkR6enR0TnZSZFZhZ0xIRzgxck5hb1BRc1RSNWQ2UVFLQmdRQ3FMT2pFK09SdkZXeEdzb3pSN1g1M2pKR05CSkxnQUNLNTE1T2VNOC9SL0pCWVMvVXZxNURCVEhkaERCM0RIbnNZN2xDSklqSXVnY0h3dVUxais4TXcyWEh2NE55N3c5Mkp5SWQyVGllcXhLb1M5d1FsZWNmOTJpMWl6SHV3M0o2ZjAyMUFxV2FOSCthWHRxMERZbTY4Vmc1RkZMVkNGMjVPZ3RLTjNOM2ZMUUtCZ1FDbktXcVN3QVRpSDRUS3Q5NlprdXJtcUVRNFZBeVltbjFvZDk4VnFwK0VSbUErSkllQ0lQV21ZKzRiU0hid1VFNktQdlA0YnBhbHFhcDJ6Q2VLNXN6dk1nYTlvTGdDUHZmRk1hRURacVJJQlFramdpTWhDQ05yZ3FXOGhXQUNFSnA0RE5IVHpEeHBvaXh4RC9uSWJUUDc5MzMzUEFBWWNMVDlvWjA5VEJiZStRS0JnRFNBVkhQb2dibFB0Njc4Q1B2L05HUTNwdlFGdERhTmRDazN2Q0F6eGVyMzY2U0NFcXZaVjNoN1dkMUQrcTZtNmIxZ1VOSnVEV05SdnY3QWZJTGJPbllJcitFYzA1ek9LYndIZE50bjgwNzVDNnQ4TC9oTDRRcU5WREZGK3VjdXVYVi9xaFluN1M2ZTUrcG9mbW9yNVJRUHpLazlZVXA1cGh0c3V2N3ZaRGdsQW9HQVFFWVZlMDJuMHdaSmVlVFBDMy9KSUYxTXRkZmphLzNqQUhzdTVOYlJOUHdXWDI2T1NBUENVSE1XQjVtS1dnYVczR011VGJTLzZmemQxWVhVSW4xeUNQclVTcTkwY1RDaTlraUozNVBrME9oV3hqZHdxRy9IcHJ2NlhBMXdoL3E0V2phYnEzTlpPMGluQytZWHBmQVBUKyt1bUpTU2VOTkZWRXlDK0NHOG5Za0NnWUVBb2xXMUZHYVZSeG9hSnZvT1NteEU0RG54MEJzWnlIRC9SWXVuNVl6YjFvQ05RTXZZRldhbG1uV3h3Y0NOVmxKKzIrelZnb3VicENUSzBOb0cvWE1ZcmpKMFdHakVnQVBYZjVoMGluUldGc0FkZWFuTzFBYnhRMnFvNW5PYVg2Y3hSUmtlc04xeHMxUksyd2crMDhlUGFmRE5xZjV3T2NPSkZpaklmK0tiU2FjPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0NZRVp5Z3JhSzZvOWhHQm5UeDFZbjQrc0NyN0R5SDZqQkhpL290Y0RNdzg5T2NsT1o5dHFMUVE0V3haNVExMnZqUlczTDQyR0JnSnJGVWlvTktKSkdtdE1pMENBSmpLTExZRmZEM0dqSDl1ejIvYlE3dGlzN1VKWGRUOExTeWZpYXBuTmlpaERlcTlXOUo1b1hodnRIWHNqdVVyTlV1NC8wcDVhQmlYd0JLRkFoVUEyU2xRWUZta1ZuM2ZLa09sMnMyN21ndXIwajhDZ1lBVW8yemdhMUpmbVliUEdHaGtjWk1TLy9OOVUydTAwMDlwNVBhdVZUQUFYSE1STStQRjdJNzdqRitGemtiUGVLbjc5a3RsN2Uvb1RXMFpvYSszV1k0dUVHTEVLUXZ2VjhXL0hHNHdSMVlIUVd2MGljOVNqOUJ5Nk0xZHdnMVVqOGFrYjJHRlBrdC9IR0J5U01POUllZ0JqekdpcFdOc0RkeGNyVkRTMTkyVm9BS0JnQldITmFFZWFuSklISGdYQm1uaG94OHJqMzhiaFF0MkVvNks2NCt5eVU4YXJrNktRZWU4L05Mbm1RdDIzbUhnbW11VDlvUXZ2QlVBZFRPUHV2eDcvdWlYdldmdHBYMnE1czJBTk5hVzNwb1hLckhvcmcvMkpRcmNzeWdmRTV0R2Z2clFNWkk1Z1lDbzE4OUppMkFrYXFpZ1cvUmw5cjNJdHVzZCtjS04raUViQWhVQXdGLzRsWVFFckpuYjFTZG5nQ3pFaGhxUzN0dz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeVczc3dPbDFWenF5cGFNV3o1LzJFMnlLU3RIbi8xbGR0SnhQSW02QktpZ0J3WUZLNEVFQUFxaFJBTkNBQVFBRHdhZkVRR3R0Q3lXMXRLN1cwdjhEUlNsVDF2WUpqMENPKzV2YS9ySU9ra21HZUh6ME1tYlhHTHdha3VoYmVLNFJ1RXZRdGNRZDhVNW9va3E5REtW
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVOVjhxN0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPREV6V2hjTk16SXdNakF6TVRVeU9ERXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NZRVp5Z3JhSzZvOWhHQm5UeDFZbjQrc0NyN0R5SDZqQkhpL290Y0RNdzg5T2NsT1o5dHFMUVE0V3haNVExMnZqUlczTDQyR0JnSnJGVWlvTktKSkdtdE1pMENBSmpLTExZRmZEM0dqSDl1ejIvYlE3dGlzN1VKWGRUOExTeWZpYXBuTmlpaERlcTlXOUo1b1hodnRIWHNqdVVyTlV1NC8wcDVhQmlYd0JLRkFoVUEyU2xRWUZta1ZuM2ZLa09sMnMyN21ndXIwajhDZ1lBVW8yemdhMUpmbVliUEdHaGtjWk1TLy9OOVUydTAwMDlwNVBhdVZUQUFYSE1STStQRjdJNzdqRitGemtiUGVLbjc5a3RsN2Uvb1RXMFpvYSszV1k0dUVHTEVLUXZ2VjhXL0hHNHdSMVlIUVd2MGljOVNqOUJ5Nk0xZHdnMVVqOGFrYjJHRlBrdC9IR0J5U01POUllZ0JqekdpcFdOc0RkeGNyVkRTMTkyVm9BT0JoQUFDZ1lBVmh6V2hIbXB5U0J4NEZ3WnA0YU1mSzQ5L0c0VUxkaEtPaXV1UHNzbFBHcTVPaWtIbnZQelM1NWtMZHQ1aDRKcHJrL2FFTDd3VkFIVXpqN3I4ZS83b2w3MW43YVY5cXViTmdEVFdsdDZhRnlxeDZLNFA5aVVLM0xNb0h4T2JSbjc2MERHU09ZR0FxTmZQU1l0Z0pHcW9vRnYwWmZhOXlMYnJIZm5DamZvaEd6QUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRHpMVmE1b1hveVg4bkJMdVB6cmtTTTFMM2E4QWhRM3FYaXErZTJqeEppM25EZjJkS2lNMEFEeVJRPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUStlYVZCTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPREV6V2hjTk16SXdNakF6TVRVeU9ERXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRQUR3YWZFUUd0dEN5VzF0SzdXMHY4RFJTbFQxdllKajBDTys1dmEvcklPa2ttR2VIejBNbWJYR0x3YWt1aGJlSzRSdUV2UXRjUWQ4VTVvb2txOURLVk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnZFZYaE5vLzFJUUtnRUo3QXN2cWtMMlE0cy9GQlplUVNEYTFESUNkcjVxa0NYd2ZPR0MxVDZOMTc3NzFYZ09Ga0hCT29aMGcrR3laYURFQ0loS1JOWFI2aHg5SUV4cXI2ajR1YW8zU1hacmdGaUdJR2lwRXJCS0NLOXUwZWZXcW5ZT0tlVXZDd1ZsYVNEWFhSOXpPck1IQmVncDRubU9BdlFTTXlobDZwb0hYNw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVBZWlJUFRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEk0TVROYUZ3MHpNakF5TURNeE5USTRNVE5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCdkh0UGg2NHdlQ1VOSjR2NW1OQnNhNmNodHVRUlZOUGFCb2dLeEFRaWFGYmJLS25BbC9YSVRSOCt0aFFtSUFXTnJSajBkd0txZUZkT0xHNmt3M0tNeHlqdTFLNEZVUFN2aU5rL0NqcktBaWp1STJaVDIwbnNiOFNLaUdCNUI2VG10WGVESzdHM29TMXd2YnlxN1lNeTNNMVZQSE9VcEF3R1BFUGw1bGwwVy9vV0JHdkpsOVlzTWRSaUdzckUwMVZPSHIxRVhoVys3Rk1rSjd3K1psQXV2dFNYQlB3R3djdVRqN3o4S1ZLRUZpMTNlQ1YwVmdxZTJPMDl2UjBBTTFCeEtQK2l5bkUybVp6cENCVUlHMmMwN3RxUkZyc1h6R3hVSTJmZWdHQVdObWQ1K0pKcjFaSm1meklnODFBelZKcTBLS2NsN09RejlIb3lpY1kvRk5SakZBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFESkF3QmNhZ2F2enpmdmVwZDRmWFpWNGdlTGNKRUdEUk1tQkFFVVdaVWIycHQ2Y3o2MGxLYXdaUFpEOVNSQVRyYnJpb2M5bnBuVzU3cG5YVDRjTUxidWZZNVVnaFZjVEszMkpLaUVEVTBnaDBmTisyM0NCNE9XbHdKN1ZqSHg0QnVZUjN4L2RDS21uYzN3YjQ4WkthUkYzMm5iTWNzeG9xL0JXYTRlbVV5NVF1Q1VQazZIK0hiYzdHdjd1L3loaDFVOTQ4Wnp2YnBlSDV2Z1lXd3R0aWRHQnFBTHc4QmFOTHBvRTY4RFdnanlGZm9Ha0NKVzg4eXNjbGt1Nmw3bFdWUHBOWDZnMTkwQ3FIVjBXQWdZYXVvcHZBbWlnVUFpa2RzMEJoQUtuRVVJbU9iY3RMbjBhbFhYZDNSWDlJMXlJc3Y5WUhMYWhPQ2lwMEVZR1RTZ0VGdHc9
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
     router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
    logging file debug ../binTmp/zzz44r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWx4QmhQUERuSlBwcFFpRVo5ajBncE42RVVKbGVrYWpVTHNQRWxHSXV2WkdQRXBkUXlzbk5EYXdFTnRMNFRoWGdHcTdMeWNGR3BobjlCR1VSTWJQL2dLTk14QnVyOHBZU1ZpWXByckVYb1pBOHY3L3JjQkE4VUxkTjFNQVhGdUZWeUErVkpNTDZucVVlaWNvOFEwbUlKbkY5UEluQWpNbWtuanV0ZEVZOEo2RGlycmFHbzBicXZsVEsvRjMza25jTGVVZGthendmaEZIU0crSXl0UW9RTlRhT1NhRnFHWVpXREd3TUcvbVJKWHVlb0Y0RzZWMjB4czhIcmhCdENYT1h2aGx6MlZ5MXh0eGRsN1gwb2ZyWWVuaE1Ea2d1R0JjdG55NXBQYU5LU1kzbmcvUHNSZzR1RU1WdW9zcFkzcU9mOVdybjgyd1FHcFh5M21JOWpzNU1iUUlEQVFBQkFvSUJBQ01HN1VVUUpzaHdOOC9abFFkL2pQNHRpa2lXQjFPRzdnd1o0STczWlJjWGxURWVYT0ZvZ1Y5V0wzUDIzeFJjQmlhcHVSOEM3YnE5OCtqODlrdXNET1pxOXZYUjVNRFBBMWx1WitQVnRFRUdETS81VkVJYndhQ0ZvRXBnYi9vaUxaM0IzemN5N3FHeWI2NUxja1czMnhYdTRyY1N5YzdiUW94ZUVnNFA2d3JVNnRobCtoQ1RjdXNSQW16Mmg3QjZQYjRkdjBCRVVhT1prRlVmazREbHZwRnNSaVFRbzB1UmpmNDZiUGxNcWMySjlWSm05akZoVnNhSElUQS95eFp4RVlyU1dxallJVHJKUmVyWWJ3dzB0eDk5UE5vM1FPVkI3T280V0NacFU0MkwyVStBcC85VlR2cTd5ak9ML0NIdFdLSHlVOGVFeWpOSG5JaU1pS1FhNjRFQ2dZRUE1dzJ0TVZ5ZHZ5Kzk4OEoyekVMcjJrQ3JwcStVamR4czdhMVBxUnB0SXV1YlhyK2V3NjZTdGM2aERTbHF5OSsxV3NZSG1zSjIzRFcvVkZDbWk2RjNmMmU2d0UyUVFMdjdMTzdFaDdiTmZYYlRMVnZrcmUyRzlsaGd1N3NEUER3WFFZK1IwcWZJaFQ1YzJkTGhIcDFZZjRWTEROMzBmSWZ3YnNBTlZqcFVrOFVDZ1lFQXAxL0s5Wnl2L0JNamxkUVJBVWRLUXhLTE5XQjlCQ1Z5cklZR09wNlJXSElPc1dMeWE3aVE4a0VGT3lEQnpBcWRDejRRZHpLUlEwNzlwVnZxSUtUbU1lRHE2REFzZzlGOTZ4Mk1oRGsyM2tkdDdNWGNpb2o5djh4b3NZSEtyVjlaQklJaGF2UVpuZ29YR0g3eGhYNUF4Z1NHdWJKVkhQalhRQTVHbVFRNTJJa0NnWUVBem8rOWpHbStaVlByUCtkVWlad3llclppUHV5dHBIMnhySExLeXVWak9Gcm1Wamg5V1hmU2xWTWJURWNBd1M5SVZOVEJxNnU2MDNnQml3Rm5RMkdoRVhmTXoyc0lVYmM5QUppZGZxOEEydS9HTDhEOW1qakY5YXBoSUxRNldqbG1tU2dmTi9Ma0k2cnpHNUdaek9MaVlXN3EvNS9XbVJaMjdxd253RFQ1cy9rQ2dZQWR3cTJ1OEhabVJ1enI1akpEM080NmNPQ3AxQWRHcG5YMmNUcElVQXVlQTJIVGJybVdKOUkyRVJPaUNOZ010TkpwdmxabEsydWk0VGUrb0ZKSURhb1VzbDV5ZktaZHBmRlN6Z1UvT1lFbEV1UmIxbTY1ZjFSSE4weGlTNmJESHhJUCtDZURBZlpRSUpFc3ZOMnJFK0RtbE1WejNWNis4UXd0Q3B6STluUm1xUUtCZ0ROanZJVzB5bk9ORmVWM2NFSTFnM3lhUlV3bERUQjJEWk5acnpyYjZNaGNuRHpZa0YrQTF1VlBNMlhROFJ5S3E1Vys3T25KT1NNLzlhdTI4enZoL2FuOTdaQUtLMEVGODZpU1dRTERyc3d6SGFGOU0yRkQwZmpmbktheXpPVm5YRjRMSDZEM3g2bExhVDFkUTR0VFhQV0J6TWUzZVp4UC9vMUZQU1RuWTVaMA==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDdDNLdytTUXYyTW5zc21qT0tJMFlzM2hqS1NBeU01SWVDb0tuTWM4UGNjZHNSZEFkVGZPUUVQZnVBa1pGRVdDcVEzaDFIMlduWUZlcjRVMW9XOXdUSGZiRStreDJkVC9CQWQ5TTRFR0plbUwycm9YUU5tVnEyRy84Y1hCbVJHYmVPQTQ1R3VuTFZCWEkyRTFvK0hFN0pGY3FJM3BEWTV6cVdYSUNqV0FmNjN3SVZBUHE5eHB4UVQ2cjY1S3BBNjIzaWtBbHliOXlKQW9HQWRVTjRFMmRNVUN6MUo1YjU5Tk5VVUcwd1Vqc1dqaVp0TngwMDVzMThYOXVMNEhsNzg1TVJDUS9FUVNWaTB2amhvSmQrSGhrT2FhN3F6bEFmU0pUR2xmYzFNVHBDaFE2a0twUVhOTmpOdVZEeGQ0SE9QUDFFQStoTDUxRFN6L2c1elYwOTdGSHhNWWN6VEdXOXNmNC94WVZHTUFGK0lkSlpZZlREQXUxTFlkd0NnWUFoRnFxamNqNFI3ODBmTVhLTlgyU0N2QWFLdUhVa00wOWhqNmpnL1ovQU81cUVBayt3LzVXL1BxVHRGcmltNXRnd1pLUE81bmgrVHJTTU95YU15ODNjS3VVZzVaUjF1alJZQjE1bjVsNWNLcS9ESmo3ckkwMXNEamliai9MVWdjWXBMd1JPRGpMSmM4VlV5dThrR1lUM3p2QUQ5OFZHMFhXS3c1R00vMmxINHdJVUZFRWo5cGduZTJRemc0N2NBaGF6amk1WEJ5bz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMzhDdHNJZDV5M01zMGp5NlRuQkZUVXBtNVBBWTNWZkdTbFlJV3hkRE5xZ0J3WUZLNEVFQUFxaFJBTkNBQVF4WlZEU3dHU05aTENpL2xXaFNONDY5WGZtZEt1MU1FZ2FJeGoxU3BjT1NvSXJjd1F0MXRlMVN6ODZlYlQzVXBXbmF5ci9wWDRPRVpKSEZNR1hFdlBs
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBaENnQXdJQkFnSUVMUjIzV3pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlPREV5V2hjTk16SXdNakF6TVRVeU9ERXlXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDdDNLdytTUXYyTW5zc21qT0tJMFlzM2hqS1NBeU01SWVDb0tuTWM4UGNjZHNSZEFkVGZPUUVQZnVBa1pGRVdDcVEzaDFIMlduWUZlcjRVMW9XOXdUSGZiRStreDJkVC9CQWQ5TTRFR0plbUwycm9YUU5tVnEyRy84Y1hCbVJHYmVPQTQ1R3VuTFZCWEkyRTFvK0hFN0pGY3FJM3BEWTV6cVdYSUNqV0FmNjN3SVZBUHE5eHB4UVQ2cjY1S3BBNjIzaWtBbHliOXlKQW9HQWRVTjRFMmRNVUN6MUo1YjU5Tk5VVUcwd1Vqc1dqaVp0TngwMDVzMThYOXVMNEhsNzg1TVJDUS9FUVNWaTB2amhvSmQrSGhrT2FhN3F6bEFmU0pUR2xmYzFNVHBDaFE2a0twUVhOTmpOdVZEeGQ0SE9QUDFFQStoTDUxRFN6L2c1elYwOTdGSHhNWWN6VEdXOXNmNC94WVZHTUFGK0lkSlpZZlREQXUxTFlkd0RnWVFBQW9HQUlSYXFvM0krRWUvTkh6RnlqVjlrZ3J3R2lyaDFKRE5QWVkrbzRQMmZ3RHVhaEFKUHNQK1Z2ejZrN1JhNHB1YllNR1NqenVaNGZrNjBqRHNtak12TjNDcmxJT1dVZGJvMFdBZGVaK1plWENxdnd5WSs2eU5OYkE0NG00L3kxSUhHS1M4RVRnNHl5WFBGVk1ydkpCbUU5ODd3QS9mRlJ0RjFpc09SalA5cFIrTXdDd1lIS29aSXpqZ0VBd1VBQXpFQUFEQXRBaFVBaFliMGV4Rm9zaHFJZ0dIdmNRcW5sM2VES1VFQ0ZGZVlNanQxWFJtamhXOEJEQjBRQldXbklCOVg=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUjRCZUhsTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TWpBMU1UVXlPREV5V2hjTk16SXdNakF6TVRVeU9ERXlXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFReFpWRFN3R1NOWkxDaS9sV2hTTjQ2OVhmbWRLdTFNRWdhSXhqMVNwY09Tb0lyY3dRdDF0ZTFTejg2ZWJUM1VwV25heXIvcFg0T0VaSkhGTUdYRXZQbE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnSU5IenpJczZXTGEwWmpqVEpNZTBJUmNnOE5vaXIzc1Vod3hienZ3MFhkZ0NYd0g4L29OdDV0b2I5aE1DbXpZQ0ZDNE1tSlNGNDNXcFcxU0tQK0pFZEpET3Y4Tkp0OVVWTkRVcWVuOWRLQU9tbU42UmJqa3NUK2Q3bUNZeFlWT0JWcUdFK25NWWtjWjhUZVloN0NiNUdnOER2UHQvc2x5Z3FFRTc4NGlkRUxpQQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVURHNXd1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBeU1EVXhOVEk0TVRKYUZ3MHpNakF5TURNeE5USTRNVEphTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWx4QmhQUERuSlBwcFFpRVo5ajBncE42RVVKbGVrYWpVTHNQRWxHSXV2WkdQRXBkUXlzbk5EYXdFTnRMNFRoWGdHcTdMeWNGR3BobjlCR1VSTWJQL2dLTk14QnVyOHBZU1ZpWXByckVYb1pBOHY3L3JjQkE4VUxkTjFNQVhGdUZWeUErVkpNTDZucVVlaWNvOFEwbUlKbkY5UEluQWpNbWtuanV0ZEVZOEo2RGlycmFHbzBicXZsVEsvRjMza25jTGVVZGthendmaEZIU0crSXl0UW9RTlRhT1NhRnFHWVpXREd3TUcvbVJKWHVlb0Y0RzZWMjB4czhIcmhCdENYT1h2aGx6MlZ5MXh0eGRsN1gwb2ZyWWVuaE1Ea2d1R0JjdG55NXBQYU5LU1kzbmcvUHNSZzR1RU1WdW9zcFkzcU9mOVdybjgyd1FHcFh5M21JOWpzNU1iUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUc3YTY4SnFjSnlOVGwzTCtFZ0NmL3NvYm1CazFNcXZ0MlJlY1NLZ25oa3I1K0wrY2E5aUJwRDNpVmROaGlHZ0JzdHhuTmVyb3lUaDg1MTBpcHlYbzZ5KzF3QUpieGhUVjhjSzhMcTkyaUQyaWx1cnFvTThyNHY0bDZZbUsxSHZTZkhEb2ZoenlJUXlHbGxYd1I5SWxNTVVIbWdTREdITzlwSEwxQzV1Qy85REtDY0k4dnh2cVZYRW4zVGE1NEtFRnFZTHgrNkJKdzZQMm9STEJqNFR2M2k5U2ZXT1dvRDJ2R3Q1emtJR1QrWE5lYUEwZ3dXakRpemF3dWNZUU9VMDRNTG1VMkgwOVBjSXBWUUhQaG5wWmZLc08wQk1mWlJUS3Fpa1VzckhwbzZSV2dGMFlnYkY1bzdZNFRKeUdvRzZWRVIxYU1lMG9yL3NpZ3dsNlVOejAr
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
     router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:08 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:09 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:56 |
     | 4.4.4.2 | r2   | 1   | 2   | 5   | f141cf47 | 00:59:56 |
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
     | 6.6.6.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:58 |
     | 6.6.6.2 | r2   | 1   | 2   | 6   | f141cf47 | 00:59:58 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:14 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:14 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:04 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:15 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:15 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:15 |
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:15 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

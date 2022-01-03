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
    logging file debug ../binTmp/zzz1r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCMG5FNC9HKzJBRlU3eXBYTmJHRWhwUXZxZ0JmakR1U01QL2liaWtuLzYzZXI5QkgyZW9LMk1jMEpmWm5zWXVTL3R1SVNQcGg3bnZGbUVaTE5aSTRocmpGMW5PdnBSbHRjWHdHK3BUZ0NvWDh3NW9ydE8wTUxqVW5DbUNPUjZ6VmppSDRsRFJlNXlwMDdUUHVBbVZMQnZLcktmSVVRbzk0YitQMmJRVTVmbTZMdlAvWkNGQkJpSEo5aEhZRFYvTFM4bHVmYWhFb0FFT1dTVDhoUjJ2a1d6YVpaQ0wrVHhGdTFwbUg0dDJDOHZOdEQvOGI0cCtpRXNOeFpCTE13RTdJTExrZVVXOGNPenI2SEFTUkc3OGV5MDJvVXR0OXVYQXRTeThGU3ZUYVJ0OWgvd1l4azhsZ3RLVjZJQ2RVQ3dtNE5uc0VGSVQ0R1VqZldDeFBZN3VxWkRBZ01CQUFFQ2dnRUFBZEdHTHRuQ3BHS3dybndDQm9Pa2JXL0w5TDdqR0RwRTM3VDQ2a09hbDFEcW56TjR1Z2FMYmt0RjE3TURiR2xHNUJBaWtSTG9ISGtGZEZrVnF1Z3c4bXhuOEhvcytTUy9DZkhJUy8yWmFRYkZhb2l0SHhlR1VvRXduSVk2K2VkRjRaRFlWU0k4QzdHc093TVovNzhHV1ZWekg2UW5LZlJpT0lqSWs2c2FEVkhDVm5VT3hibkVoTlQybnIrUUJqVE9PR3Bvek1leGs5TlpwcEhzSTYvdGtGL01KRnlqQS9hNFlwU2xDWmxkSVJkNTYvamtrVUtlNXhZR0VWT1pzeHI1T0gzVkk4SEZORFowM1dZYmpIS29FQXNnbndpVTk1N0hhVVd5ZFN0Y2FyQk1TTFhuWVR1WEZxRlV3dDhISGRBMk0vM2JXWnRYczdFZFNWSnlENWhob1FLQmdRRExFaTdrOC9LRWcvTUZERHJYdVROay9ZNXViNnpqMHFBRng2d1k4VWZ6Z21xRGpDWHJ3TGgwbXFKbndQRjV2TWVmN1dsU1FQWnA4MW5Wall4WWRVZktVTEpXSXUxbnprZ0N2ejVJNkFCaGNROFlCcFVTb0tpRHduSm5MMk53MXVDN1FZUVJDU29Qbk1oNHVyQ1pDRTUwTmx6a1NSUEFsUnNYbFdsUm9SOXorUUtCZ1FDVEFSY0JDYXRSTzNJVTduTlRUNGwyc0VkSVJVLzZmNFQySFFtditLdWN3dkRxbDhrQWpaNENRR3pxUnpvd2t0aWs3OExtbkpGenFkcDFkNWV0ZjNHS0JlR25tcDFxN2dHbkRsTXdaQ3lJRldnUTdybVVUeGJ0TzF4dUNMbzJGU2F2RTRWVmtWemZrV1k3eEJCT1JjYkxBamY1Yjhlek5sb1M2K3dVVDltREd3S0JnQURoUjBxK3MrSlhJQXA1anhlNE9iektUSCsyQkMzSWorRDJpSXhqSDBpeTIvdE45Q3dkWGE5RHJFaCswWTBSZ0Z2MUQydkgxRW1KUUc1b2VwODNndVFoaldSS0tuVTBzNk12YVBtdjU3Q0VhT2hWdnZlaHNway9rbmRZQVRwUDlCRmJxMUxYazFNVi90aG5GclRURUdQNGlGYUU2b3ovR0dyMXZzc1h3NmNoQW9HQUtGM0lQMVMwWWwzOGVacnd1QlBESDRCUVVwd1YxaWRtRDE3eDVneFdzM2trUm9iZmZ2TmtUQ0g4eG1oQXBrM3NoMzMrK3V4TFZJTnpwWVh0ZElybVZvdys1cE1pWHRaMFJiYzlTTEI1T2ZVRzJuOXpIaktKalNNYndtdExGc2JBRkpzN3BiK0F6VE5UNjExdlRNOEVRNEtjZERZcGxDQjhvMjE5S2lhekI3a0NnWUJ0N0dOdSthcXpscWZQdlQvY0x3aFFmNzVDZ3dnUVBXM1FYYWwrZ2xRVy9SN3ppSC9nZXEvaC9GV3laR2pFb2Ntb0lna3N4dS9VV1I0OW9NNkthanh1RXA5bStiOCt3MVlsd2ZFd3drTlpLUVE1d3BNaEpqdnlXVGltbzEvcGdzZVI0VE0zZy95SjB3bmFiSk5wRngvVVRFeVpxSGw5c3FWMVhhejg3c3JyV0E9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnV3SUJBQUtCZ1FDaEt1QlAvSDRGN3JtZ2ZsYjV4aXl6RWg1d2FDQTlHT2RUNWlkbVFJczZON1lSQ1BiSFkrWDRya0h1MFYvMjA3YklqQkVoeEMvZzhua1hic1R5STlJWXpDTUpaOWJZUnFaa0VQYUlDWGxvaUlwam50dEdoZnRvSk04a2lBS3RaN2VkOW5XSTZDZ2MvZGF6Um1GcEhaN1VRMksrTDRWd3VEK2hteUw2QTc2VFdRSVZBSzlVakVmTDVCbExTL3QvUUdlR05hRHFxTTBsQW9HQU1vVUorU3duaGZvVGc4NTV1NElyMnUvT0plUEg2STBsVUwybEVaZVFaTW9PUFBhcTM5OVRKL05mMXAxMzRKS0tOcG9heWdsRHp3UEZCRzlhaXZ6ZjB5ZnZDN1dPbXAyQXQ3OGIxak4ySGk0TDkyUzVDL2QyazVyQ2ZncUVtSXB2S2g5QStYU3V4eVhBZTI0Tk02U1hkWFVqNXQxdGI3ODAxQzVaUTZNaStad0NnWUVBazkxT3VzMjdEMEJwazk1M3VDYjBiUWV5TjdEdU1hU1orMnFvUkIzUG5nQ0Z1bng2MnZVU2R1R3VqZlR5UktRZ242MjZQb0VwbVladU9neFFObE5UazVpK2l0ZDcxRE5DZkdCQW1neGY5SDZNcmZ3c0FvZVJtRFRoWjNRSFlZanhBZzNXaVRqNU42ODE5TEJ0WExPQ0lVTThVbjZvc01hUGcvNUxxRmVwS1VFQ0ZDNkhCem9BRGVPQUhpdngzZTRibThMVm5HUUs=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIem9STHFabDBzRUREUDFHZUZlWFoxeEdTNE4wR3FLRUs0QTdmb01xaGpxZ0J3WUZLNEVFQUFxaFJBTkNBQVNMT3ZST21XU0g4eHlNRm5DNExOZlVlbjVPY1JBUE9lQW9sZlJRamc3RVZzZ0VuOHpjVENjL2RRNElya2RQUTJFaExHdk1vaExmTTF0aVFJaEtFV0Nu
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBaEdnQXdJQkFnSUVQcnlkdkRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1EUTFNRE15V2hjTk16RXhNakk1TURRMU1ETXlXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYmN3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDaEt1QlAvSDRGN3JtZ2ZsYjV4aXl6RWg1d2FDQTlHT2RUNWlkbVFJczZON1lSQ1BiSFkrWDRya0h1MFYvMjA3YklqQkVoeEMvZzhua1hic1R5STlJWXpDTUpaOWJZUnFaa0VQYUlDWGxvaUlwam50dEdoZnRvSk04a2lBS3RaN2VkOW5XSTZDZ2MvZGF6Um1GcEhaN1VRMksrTDRWd3VEK2hteUw2QTc2VFdRSVZBSzlVakVmTDVCbExTL3QvUUdlR05hRHFxTTBsQW9HQU1vVUorU3duaGZvVGc4NTV1NElyMnUvT0plUEg2STBsVUwybEVaZVFaTW9PUFBhcTM5OVRKL05mMXAxMzRKS0tOcG9heWdsRHp3UEZCRzlhaXZ6ZjB5ZnZDN1dPbXAyQXQ3OGIxak4ySGk0TDkyUzVDL2QyazVyQ2ZncUVtSXB2S2g5QStYU3V4eVhBZTI0Tk02U1hkWFVqNXQxdGI3ODAxQzVaUTZNaStad0RnWVVBQW9HQkFKUGRUcnJOdXc5QWFaUGVkN2dtOUcwSHNqZXc3akdrbWZ0cXFFUWR6NTRBaGJwOGV0cjFFbmJocm8zMDhrU2tJSit0dWo2QktabUdiam9NVURaVFU1T1l2b3JYZTlRelFueGdRSm9NWC9SK2pLMzhMQUtIa1pnMDRXZDBCMkdJOFFJTjFvazQrVGV2TmZTd2JWeXpnaUZEUEZKK3FMREdqNFArUzZoWHFTbEJNQXNHQnlxR1NNNDRCQU1GQUFNd0FBQXdMQUlVUmMvWnl1OXlqYmFwbDF1MHBaUEVhN0d2Wm1BQ0ZCdUV5UU9YSXlocHd0VWdYajRoeituUUtYUEM=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUXJOR3NYTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1EUTFNRE15V2hjTk16RXhNakk1TURRMU1ETXlXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTTE92Uk9tV1NIOHh5TUZuQzRMTmZVZW41T2NSQVBPZUFvbGZSUWpnN0VWc2dFbjh6Y1RDYy9kUTRJcmtkUFEyRWhMR3ZNb2hMZk0xdGlRSWhLRVdDbk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnTTFsWjIxUXduMWU4Y3dWd3R6UjhmaGZMQmh0eitGNHVHWEt1VDFWL056UUNYd252Ym1LMXRlM0wzRUphWFpXSTZ3RlJLeWhrZVdGQzVJWnJBMnJ6ZHZjY3pHK0NUMXhoNDRkak0vNkpGY0lWZlhkTjRXbjZxL0hnM3NYb2RBQWhBUDBSZ0tGTlFRKy9ocHNjcVBqdFZvTW9CWjV4Yzk2V2tPSHJZNStuOGt0Vg==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVkKytzdGpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16RXdORFV3TXpKYUZ3MHpNVEV5TWprd05EVXdNekphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCMG5FNC9HKzJBRlU3eXBYTmJHRWhwUXZxZ0JmakR1U01QL2liaWtuLzYzZXI5QkgyZW9LMk1jMEpmWm5zWXVTL3R1SVNQcGg3bnZGbUVaTE5aSTRocmpGMW5PdnBSbHRjWHdHK3BUZ0NvWDh3NW9ydE8wTUxqVW5DbUNPUjZ6VmppSDRsRFJlNXlwMDdUUHVBbVZMQnZLcktmSVVRbzk0YitQMmJRVTVmbTZMdlAvWkNGQkJpSEo5aEhZRFYvTFM4bHVmYWhFb0FFT1dTVDhoUjJ2a1d6YVpaQ0wrVHhGdTFwbUg0dDJDOHZOdEQvOGI0cCtpRXNOeFpCTE13RTdJTExrZVVXOGNPenI2SEFTUkc3OGV5MDJvVXR0OXVYQXRTeThGU3ZUYVJ0OWgvd1l4azhsZ3RLVjZJQ2RVQ3dtNE5uc0VGSVQ0R1VqZldDeFBZN3VxWkRBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFIUEJPMURWQTNlRGY4ZSsrTHJPdWRBcXJtMGRjWEhydjIrWHhoaVNkeGYveHV3T2hKWkoxOER2MnNwYmN6NVVuYzQ0UDB6aG9mVWxJblQxaFFsTjN2S3A0VU9vanpQZ0ZVOUdDeFZ0M2tabUZad1NqMWVnUHBrTDlEODk3Z2JOR0xscmlkd3hBL2NDQVptenpLYXgzbklWNFhFTk5JR00yajhWbHJVU1BNWGRzZjRaUzVHYlNNWk9rMjltU244VkdZUUlPL05Ua1JxOG9DQTFqQ0txd0hpYkZsd1FpUFFhOEd2NDluSTVSd3BMZys1TThRK3lFeHVQMlRNTTVYY2t4RDNVK0dKRUdWRmRic2ZpV2xQR2tUbUxRRHJieklQZDBnVFcwMlNqV0taV1VnWWxFQ0grUmVHSHZQbGpFYXBIWGdoVWZZK2w3bHpsb0dWV041RkZWRDQ9
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQXE4UE9JSGdTcVUweG5xQmNJcWlnc1dCVkVyUmpnQnkzc1FXclZicUVWdHdSSkRwSklQOEtMSk1WZWFMVmorWkxERndDK1ZYc01kYk9QVjZxamFJKy9ZWnRsK1E4Sk1PUXlyR3JYMEsvTVNDTkwwVGU4UG1WSDd6R2ZNMmpUNjdXZW1OZTJZU29IdVdQdXFhR0RZcHBjbDlZbmw5bUZhSkp6OTNDQVZxZm1IWHQxb0gvaU1IN3NYK01qUUcyWHBBN0FwUjRpRlV1cFRYc3VsTUMrRlFnRzR6MEcrdnhrZXpQUkpmMUZ4VVJyeWFMZTFNa21ZRk9KbWUwY0x1YldiVldRLzcrYmN1MHlIMlNmTVEybTh1NnlFRE9rN0M5Qk5RSnljcCtpNlRsbEZPK3hyYSswTDIyNG5QbGNwV0FNdDN5ZUthM3pEbDZnK1dkMkxTZ05CUWZ1d0lEQVFBQkFvSUJBQzQ1ZXE2SVFkVm9IZE5ucW9QMVI1R1VzREJoZFdtVDBPZUY5QThWSytwSVBTQzN3dGhyYW15R2hNQUFUMkx6Z2Z6b2dqQmhyRGZaYkJWZDlaNDZMS09EMnRpR3BwenFPSHdrQmsrVG9lcHhyUzBzWnFjSk05V2ZzdmNCVEZMMFpXbjRkaDBwc3lqbGRLR3hrTi95QU9DendpQ1U0ZDh1bHBpblFEK25DTTQ1ZEtVNnZCRVg3WkVFVFpmeXFZdVBiMnpjZjhBSlN5VHRsSGRja3Qzem9BbEJLOVlMbjVtVEEzMkc1Vys0MEI4ZG54dlVaOVoxeXpxVXZ0SngySXcrUHBITHBTTTFvaUtlYk5nYlhiTGMvMlVnYW9LTmNMcW93dlpzUHptWkxDVVcyMkJTVUFEbWZJR0xTc1NhVTdzWG10WXhUVEtPei93VVcwelZRR0UxdlJrQ2dZRUE3bXRvVlAyTHdtTEFtTFVJWlMrc1ZrZ1hEL1FvS3ZZVnlsbmxiUzBsSGZwNENZcE1YSmRmZzJEa2Y4ekRFUmxSUzJvSjNtakVHV2VuVE9vUllGZUlhR3lLK2VmanNxcHFIODloOUhZQ25VQm1wRnBCWDNMdDk4QlhDWDRFckMvMlpySVU1dDg4Z3NCZzF5VkVLNjFYN0VWY2pFK0ZacjhtVndzQW53RjRHMThDZ1lFQXVHNHNBajdkQVdXWUpTMGhIQ1J3a280YXNyTG5RTUorRWJxWUk3My9OZmE5RmNiVUZtOUI5b1R0WnYrbTM1Z0hTMldyS3ZLaWo2V1JpMWlkSnhRRWN4cEtsODdyZFRQcHJvZDN2a3BoMW5wdHVxWUI2elNMeDB2OEJOY28rU0Z2cTIvelFNdlUwWDAzZUNXQWVFZkI4V09NeGZVSU9ocWtRajQ2dm1oaXRTVUNnWUVBNmZ3alVuWGErWlR0SzNGUG9lNmRsYmYrV2p2bVIvTm5BMFlpY1hsQzJoNzhPM0NzN0pucXRRY2NlWWc5VU1TbUVmc3BZRXMxV1RGdThYOHVPbnp0ZEg1Q0RtelQvSDVlMUlVMHZ6UXA4S1pKbGJhMlBiU1BjdndpN3ovcjJnamdLMzFPSWg2b1JqSURXR0pNZXdrT0p1VVRwT2hPSmI0bkpIbTV6Rk1teXNVQ2dZRUFwRmxCREdzNmhJRWxHSlBqdW5GYWc2N3dhYWYxWFljejB0YWx0c3diL2RtM1hBMkhkOHFEVEl2ZUJuZnhHN1VkWXZuaGsyOE9uOVZhSW9PLzMwLytPeGdGdXN3Z2xKdkROTXp4VHZoM3dTbnVXSEtRcVNsMUdnOURNSWtQc1JvenFlRWtNdXl3NUZHaU9ZV3B1d1d1OVUzUjU2SFlSL2J2d3p3ekd2Um9hYVVDZ1lFQTJoV01rdnpERlpJTDdXcHRYSzNvZkFsRFlRSUR3aWhhYkl5MktCZjUwVzBQYWN4MTVtSkYyWXN0U3F4TTV5V0pxLzVBeUJKK2EvWngyckVSbmo2aGpsWjM3Y3ZDZjFXbXFybSt3UWRIZmltOUlsMGF3TC9QOXJjbW1CSUx2R1QwdlJaYzJLVnJQTEhDQ3pMcW9ZbTFqTDJvMWZXOWJWbmxrZDR4Ri8zU2lJZz0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0E2TUhNMnhEZDNkSFIvdUVHZEtlSHhFWWloZzZwczllVVZIRXZMWHN4dDZSVkU3N1hLOGhZRFJJVFE1ZHV1MkNkQjdxRVdURERnQTJEWkxLOWZnUVhVZW1PNlN4QVhOaTluVno1N2tBQlpTZG1WT3NPb1FpMkpRNmNBdEI1VlZodko2ejhRUHhGaW42K2FrZ2syZEtMUG4zTGx4V2VWcnNUdm9TZm5kTCsrbkFoVUFuNlErbXNrR0sxeWlMb1lJNExmbitvVGk4Q2NDZ1lBR2lOSjRJdnpHK0RrK2YyeDBwSUZvSWZCNXF0VXJaUlozaXFPbTJZOGpYTTFZbFI4STc4b3ZEaFZIYU1HbFUzUHB3Tmx0cWxzbFNvditYVGpTVnpiOTRKZUlrQjBNbHVlQjZLSDVUUnB5UDJIZEN6bzZsTVBUUURmV2E5OG9XZXJTb3dDOWNVR3Y2TkRlRm5tb3BjTTRvSC9wL0wzNnBwbFRaeW5wNzY3N0V3S0JnQVNsNmpONmxpRFpXSUIycWVjakhLRDF4bnFnVktwQkprOUNoNkRzZ1puekZVVzRwU3Awb1B6cVBkRldKOGJPYng4eHJtYmVUNE5ZckJOcFNONS9XeUxsdEYyZ1NOL3d4cWkyUVNOVko5NkNQMXhNV0lYL2Y4UWpNNE0yVFl4MnNFR2krVXFLbzFNd2hqbUUrMmdaUy9VUTRFOXNLSlFoc2ppZ21yUmovUTJaQWhVQWlwYlI0dGhrNGpDZXdKTzA1c1pEcVlrYU1rYz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURDTTR4U1ZBVUFTbEFFRGRaWjFKdTZLTWgrZkR0NHNna2JoNDBrTy9ENm9BY0dCU3VCQkFBS29VUURRZ0FFbUZkYmhMV2lsTnJkbVpaY1R2LytKT2lvUFFzc0FDNU5wZWFRWTBsR0VDUzlMVDFVaW1FVTVGYlJ3NjdYUFJIc2JLUUdJTnI0Zk5nUWVqaVFzMXdUL2c9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVKeSt5N3pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1EUTFNRE16V2hjTk16RXhNakk1TURRMU1ETXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0E2TUhNMnhEZDNkSFIvdUVHZEtlSHhFWWloZzZwczllVVZIRXZMWHN4dDZSVkU3N1hLOGhZRFJJVFE1ZHV1MkNkQjdxRVdURERnQTJEWkxLOWZnUVhVZW1PNlN4QVhOaTluVno1N2tBQlpTZG1WT3NPb1FpMkpRNmNBdEI1VlZodko2ejhRUHhGaW42K2FrZ2syZEtMUG4zTGx4V2VWcnNUdm9TZm5kTCsrbkFoVUFuNlErbXNrR0sxeWlMb1lJNExmbitvVGk4Q2NDZ1lBR2lOSjRJdnpHK0RrK2YyeDBwSUZvSWZCNXF0VXJaUlozaXFPbTJZOGpYTTFZbFI4STc4b3ZEaFZIYU1HbFUzUHB3Tmx0cWxzbFNvditYVGpTVnpiOTRKZUlrQjBNbHVlQjZLSDVUUnB5UDJIZEN6bzZsTVBUUURmV2E5OG9XZXJTb3dDOWNVR3Y2TkRlRm5tb3BjTTRvSC9wL0wzNnBwbFRaeW5wNzY3N0V3T0JoQUFDZ1lBRXBlb3plcFlnMlZpQWRxbm5JeHlnOWNaNm9GU3FRU1pQUW9lZzdJR1o4eFZGdUtVcWRLRDg2ajNSVmlmR3ptOGZNYTVtM2srRFdLd1RhVWplZjFzaTViUmRvRWpmOE1hb3RrRWpWU2ZlZ2o5Y1RGaUYvMy9FSXpPRE5rMk1kckJCb3ZsS2lxTlRNSVk1aFB0b0dVdjFFT0JQYkNpVUliSTRvSnEwWS8wTm1UQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQTlQbG90ODFpditaaGZpcHhpWk1ielUrall5QWhSWXM4bDJYTXVEaDNZRGNERFQrNmNPWmx0NVh3PT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUnY2OFpRTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1EUTFNRE16V2hjTk16RXhNakk1TURRMU1ETXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTWVYxdUV0YUtVMnQyWmxseE8vLzRrNktnOUN5d0FMazJsNXBCalNVWVFKTDB0UFZTS1lSVGtWdEhEcnRjOUVleHNwQVlnMnZoODJCQjZPSkN6WEJQK01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnSElRS0xYa1pSK3ZQaGl6TUNSSmN0MGQvcEZxZm1CZXZRU2g5WGUyMnZERUNYd3oyTUdWNWU3WXlHR3pPT1l0SS9ya0FqKzRxRmFVUkF2cmlBb1hWSXVjS3FGMnI2UitDa2g2TVZnQkN5T0YwRGNwQ0tiTm9hLzVWMERTbHlwTGduS2g1d0FIOUdhQkg2bE5PaWFLVGQvWXJnRVBOaE1Oc3R0ME95MDVDdzVlQQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVBM2N1OERBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRFeU16RXdORFV3TXpOYUZ3MHpNVEV5TWprd05EVXdNek5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXE4UE9JSGdTcVUweG5xQmNJcWlnc1dCVkVyUmpnQnkzc1FXclZicUVWdHdSSkRwSklQOEtMSk1WZWFMVmorWkxERndDK1ZYc01kYk9QVjZxamFJKy9ZWnRsK1E4Sk1PUXlyR3JYMEsvTVNDTkwwVGU4UG1WSDd6R2ZNMmpUNjdXZW1OZTJZU29IdVdQdXFhR0RZcHBjbDlZbmw5bUZhSkp6OTNDQVZxZm1IWHQxb0gvaU1IN3NYK01qUUcyWHBBN0FwUjRpRlV1cFRYc3VsTUMrRlFnRzR6MEcrdnhrZXpQUkpmMUZ4VVJyeWFMZTFNa21ZRk9KbWUwY0x1YldiVldRLzcrYmN1MHlIMlNmTVEybTh1NnlFRE9rN0M5Qk5RSnljcCtpNlRsbEZPK3hyYSswTDIyNG5QbGNwV0FNdDN5ZUthM3pEbDZnK1dkMkxTZ05CUWZ1d0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFrY000Z082L3prVjA3L1EwWXBqczVaaTRkZUo0Tjc3ZlQyVDFORzVZU01vNzE5UDM1dm0wSHJteEZNd2tEQXRUUFZRdUlZRUdaYUdWUDRDNWNaemEwOUZsZkR2NDBwbExrUSt6YlFieWJEcm5iVHIzWHNXVTFBWTlablpINTVRdkwzM1R3RHRveGtHNDNXUU1YV1cwaFM2cUdIMHkxU1lmQUJVS3ZJYXRDandmOFJrK095TzFaSzhJSFR3SGJ6UFFZeTdtY0pTY1B2RHRnemVFTUtveERVQ2ZrMmNpWkxFbGVibnFlTFBqa2xEbkpNMTVQN1ZPL1J3NHlFcTNjbEwxaEo2NHlWU1F2dFM0YTZTYzc5a3F5VkZOdS8rYXdKSEF2dFdodXRLaUN0RFhNOGFPZjZCaXEyS3d5dDNCV0QzRkFWUWxmRVdlMkNVT2gzY1VPQnlBUnc9PQ==
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
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:11 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

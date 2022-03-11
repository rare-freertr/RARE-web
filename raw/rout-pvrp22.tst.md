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
    logging file debug ../binTmp/zzz99r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQXYzQ293amFTcDJzY0JQQ1IrZXQyY1RSQUsvWGdES1N3d1JlU3RvSXZVUlpFa1F6RWZaZm9DNXBXMFVOYi9ZOUwwRXFBR2xmdE9IeUFPNGV3ZkVzbHBGUnMybkVqRUhFUVkzcC9FaTlaUU1TZzVVaTZkNWhWN2xyVU9UTjFRVnpZNm91NHFqcUhXTncrTnRSMVBHNlc3enFFVHhTT1g3aHloYjZVOVR5VzJJWVZ2KzkrSW9DRmVPOXNHREk2VFdXem9GZHdaV2F0S0lWNjN0VjdsL2M1UzlMYXpDcUtDR1R2RmhYV0lzTUFaU0VrQ2ZFM2JqUnhZS0xBdTN4cnpsVjB5M2M3RlJqVC9KeTlIUzAybHBsL0IzUDhldTMxOUNNL3MwT0JWSEpycURUR1lNSUZidVdFOVgvODQzZ1JVbTlHSkxIWC9QL3RCYytENTBBV1NoQXVpUUlEQVFBQkFvSUJBRW5xWGI1ZkE5RFFja2tWK2NiZE95WUtYcHlhbXA5SEYxZjJtaGNOdk9jNkNjOVhkcVpuZUpqQ1JyTVZwdmNIMU9YZlhnYk4zREhySURmYjlEQ0pjMGMzc2EvRjd4dnlDN25kR2lNVFZRckU0THFta2hpTElPS2UvMEgydEZkQVdpQjFRaCszNlhwTnoxZXNRSGZNMjBvUzlmTHlwT1lnZVZkYWRua1pvOFNGbExGM3p0ek95Q3p0WGZVY3lkTWE4M3ludThEeFBPaFhOcjlRRkhnQ0t5cFRTWGRQYXFKb2ZiVzNQZCtGbTlpOWRFUGd6QXlJTFQ3TW95ZEh6WmxNZVorM0drYWMwN1R2bFEyc1RvS2xLUkRVQXVzTnJ3TU5EbVdEaWhETWJhdHQ4djFkWWVNenZROTFxUHhSZjdhWWlWdytKdDdnUHhWd0NXTWdlcjdxYjRFQ2dZRUErbFFXT0N5bGFmc1ZaUFVnWXFkOEdET2hLMGN6ZmNtUzY0T0lFWDJ5dldQT2JLTW9BNzJvc2NKSHlqQlZmMFBtOC91cTdLcjdYWFpreTMxTWlocDJQdVFiVHNhSER3NFRiR3k2WlZHV0p2czZ4VEVRNlF4QmxSeU9VMys5NHgwWDA3VkpndllLZG5GdVJ0Z0lQM3pwSXdvMitRak4wak54YUVnNDVuQ2ZDOVVDZ1lFQXc4Y0VraE1FUU5pdndBemRrWThLVWNic1FBTWQ2N0ZNYUhFQlMrbWpqUzVkdnI3NW1ocE4xNGM2M25rN1NrV2lvQTYxZjZRRkdWa2E1SnlIUGpOOG1lWGxGdEpDMVZnTEhibzZYT1Q4YlVYMTF1ZEhEakY5OEZSU0hpcVg1Y2h0QW1zME5SZHUxOFZiVzdORnhlK0FlTmpZa0NjSVNCYWErOGdMTEo0NXRlVUNnWUIzeDhxR0FKNzU4a0hQZUJlUi9UQTg2RitETk9Pbm1jOXFVQnJJdTh2T0liYkJkdVNMdmJHOXRRZmk4SFBJbkxZakl0WXJ2cmplaE90QUQybVRYNHdiRmMwWFNabVFrNXlwc2ZFUzBCSTMvdGlsU0pBZDQxWnlRaUs4UTVDWjN1N3F4NEV3WUFpcm1pVTVVdC9IZVQ2WkhLY25USlluc2FQZlVVZWd4RnptTFFLQmdEdnJPM0RodFJtTHVDNlZRWEw5VG5FODZxMmt4cEdPVUE1ZkY4QitIM3BrU0hqS3htWHR5d2s5OER5SzZpU1BMM2pCUjdkckljeGlReUxZN1dPU0tuNkhxQmZWL25LQllkV1ZXNnQyd2ZOSHlEZ2Z6TldCUEVSRDZtWWxMeHc2dlhKU0VVWjJoNHd1Y1FtZDBxc0Q1RlFZT2gvVWNtcHQwTDFpdWxqTGpHb3BBb0dBRGN2amZ3bVN5T1ZucjIxMWp6UmNZNEpxVHdlSTZYbkR1Sk1ETGRtOTZGSmlPWmFla2EzcnBSMjNtbnQ5NlkwcHJidkdDc1FZR2IwbHVONzI4aGhSYzkycDlHbFNGOWhFSnEzYnZpWmpYait5YXRzUDBHdlRPMUFNeTJUSUU0dFNRVVRWZWJMOWZNRUVxNGJ4eDlpQ2lvbzQrRkJLclRsa25iT3FlU3lRdE9BPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0doSVVUNER0QTV1QjI0bWVFQW5LZGtpblB6aFZ5TktmZVorbDkyRFAyaHg0empQQWM4V1hwOUp2RS81WnF3RE0zTmtJZXlpZUpHYmVVcjJaWGRaaHFHcDlzZW4vOW9lNUs3UzFDOUJDSkxmc1BpZ01QdWtQQjhLclBMVXhxRkdPdmRhZjFyMm9vTm10UlkxREFGeWl6SG9IQWhvRmpzakQyTHluUVRkSWpObkFoVUF3aldyeTM3Z1NnTDJhNXprdEZqeWMxcTdKUU1DZ1lBSjN0MHljdGFVZXB1a3VLUUFxYnlXUStoZEdVZDRmKzRUTkJrY0o5OVlhQ2JqN29ZdWdIeVY5RnNNL3JuVkg2SU5YdWVUY2hJYm5hUWh0VGdoVXRRVk1ibnllN09FU3ZDUlNvVG1KUGlkR0hLeWFzUEdpaWNGN09kMlNFTy9hTW5yV0V4b3Y3Nldybmxtd3ZNQU9HeXFnYmVYbzk4SnA3d1VZRGprZiszcmhRS0JnRWU3dE9xT01UL1dPWlVXTEV3amgyamJ6Zys5OHp5b05zVkFzZU5KSEYxUDZXR3lWWHBsMWFhd0I2ZWlQczBPcEJEalhqRnZXZ1MvUzJxeWwvVmpqWWdXRUhQaVVWQ2F3bGlHNDVHbjdXQ1BIKys1TkJ5UmRRc09ZNXI3MmZnSy9jTUlLSHZ6NFRGUjVZc29SZW1KNnI5dG9JR1FjT3huZ1Vnb1JtUnVzSlAvQWhVQTJBTDhGRzREeDZrUnhYQ05JMDkrYXJMY0RVYz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURKdlhxSHFjOE9KNk9vM1ZnWS95em0rQ3BUYVQzOEh1akF6V2ZUT2VnVG9BY0dCU3VCQkFBS29VUURRZ0FFL0NNR29XOGhjYkhyYkQzVUZZYjRpZEdZNFN4aUoxVGgrajZrNkI5T2J5K3A4Q2c4c01nbWVVOGhGTFQvZ0pCTDMzZWlxUitGcWF3OGNFbmp4ZUZnSlE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVEbzZvY3pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVE16V2hjTk16SXdNekEzTWpBME5UTXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0doSVVUNER0QTV1QjI0bWVFQW5LZGtpblB6aFZ5TktmZVorbDkyRFAyaHg0empQQWM4V1hwOUp2RS81WnF3RE0zTmtJZXlpZUpHYmVVcjJaWGRaaHFHcDlzZW4vOW9lNUs3UzFDOUJDSkxmc1BpZ01QdWtQQjhLclBMVXhxRkdPdmRhZjFyMm9vTm10UlkxREFGeWl6SG9IQWhvRmpzakQyTHluUVRkSWpObkFoVUF3aldyeTM3Z1NnTDJhNXprdEZqeWMxcTdKUU1DZ1lBSjN0MHljdGFVZXB1a3VLUUFxYnlXUStoZEdVZDRmKzRUTkJrY0o5OVlhQ2JqN29ZdWdIeVY5RnNNL3JuVkg2SU5YdWVUY2hJYm5hUWh0VGdoVXRRVk1ibnllN09FU3ZDUlNvVG1KUGlkR0hLeWFzUEdpaWNGN09kMlNFTy9hTW5yV0V4b3Y3Nldybmxtd3ZNQU9HeXFnYmVYbzk4SnA3d1VZRGprZiszcmhRT0JoQUFDZ1lCSHU3VHFqakUvMWptVkZpeE1JNGRvMjg0UHZmTThxRGJGUUxIalNSeGRUK2xoc2xWNlpkV21zQWVub2o3TkRxUVE0MTR4YjFvRXYwdHFzcGYxWTQySUZoQno0bEZRbXNKWWh1T1JwKzFnangvdnVUUWNrWFVMRG1PYSs5bjRDdjNEQ0NoNzgrRXhVZVdMS0VYcGllcS9iYUNCa0hEc1o0RklLRVprYnJDVC96QUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUURBSERJMU5WK3VEQkdxcG1ra1NUWWYySER4a0FJVVI5Wk5oa3VYa1ArdzdTL1A5QmhhWnRYSUtlaz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUWFGVFp4TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVE16V2hjTk16SXdNekEzTWpBME5UTXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUOEl3YWhieUZ4c2V0c1BkUVZodmlKMFpqaExHSW5WT0g2UHFUb0gwNXZMNm53S0R5d3lDWjVUeUVVdFArQWtFdmZkNktwSDRXcHJEeHdTZVBGNFdBbE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnVXpCVXZwRHVMK0pud0VvM0Z3empWZFVvQnRxY3oyMk5OUkoweERhNjBFTUNYd2VzREFodGlZL3ZPcms1L3lYRElIRWdwYjRKSWgzaUNlVUFEelJjcXZNd3BxejFsekNaS3VVeldLWWlRT3VUSVZRNUxodHhXem1kSWVVdTNxUjZjeTNwRnJTd3pOeTM2dlowenhqQm5UejdQcyt6Q3dWN2Z4cUdiL1kxWXFQbQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVEci90VFRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFExTXpOYUZ3MHpNakF6TURjeU1EUTFNek5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXYzQ293amFTcDJzY0JQQ1IrZXQyY1RSQUsvWGdES1N3d1JlU3RvSXZVUlpFa1F6RWZaZm9DNXBXMFVOYi9ZOUwwRXFBR2xmdE9IeUFPNGV3ZkVzbHBGUnMybkVqRUhFUVkzcC9FaTlaUU1TZzVVaTZkNWhWN2xyVU9UTjFRVnpZNm91NHFqcUhXTncrTnRSMVBHNlc3enFFVHhTT1g3aHloYjZVOVR5VzJJWVZ2KzkrSW9DRmVPOXNHREk2VFdXem9GZHdaV2F0S0lWNjN0VjdsL2M1UzlMYXpDcUtDR1R2RmhYV0lzTUFaU0VrQ2ZFM2JqUnhZS0xBdTN4cnpsVjB5M2M3RlJqVC9KeTlIUzAybHBsL0IzUDhldTMxOUNNL3MwT0JWSEpycURUR1lNSUZidVdFOVgvODQzZ1JVbTlHSkxIWC9QL3RCYytENTBBV1NoQXVpUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUR6bUZzQTZ4QzdhNkYxTktnN1M5ZEpOVUtQRGQ1NGZ6TVFzTWdQR3JWcVBIK2h2dWpQQWNKSE5neS9sRWJOTm1LNDFoZlBTVUltbU13YUVSYTJQZG5YNVJtQWkvazkrRkxVMVhtQlVuUk9sNjNHbllRQmhvaStaanBpQjBuSWl0b2VGQzZsY1daZDR1VTBYSFd3RUJvQTBZTlllYU02d3RjMklxZnRoY3JDT3hpVENsbHZlb3R0NDNYN0xXZ2xLZnJLWVRzK25wd254bWJuSEJFTk9qQjk3MFY4UjBhdjZrTUg5N2Q3KzlodCtWTDFSbVpudjBBTjFiMzNkVzNNeS9SVWhzMFhENS9JcTdGb3dGSkRsQXRLKzZTN3cxTStWTWNVOTltWXhKcUhLdGgwSmRGdE1qS3BXMHl6R3dydHBqY0hqM0JQV3JlMFpKMHdaM1ovbUVL
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
    logging file debug ../binTmp/zzz99r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQXBqZEtya1pndzVYYnJxOEtXTDJuUHZFSlZHcmlhL0w0dVRLU1pwdWVDMHU2M3JGcW1QYkx4cFkzRTAvdnhXd2d6eVc1b1lnQnZURGFMeXZXZnhqb245YU5sZGpKY2tXb1MwSjh2aHIzNmFCMnpoSHVhcVh0K0NIRktWK2d0SW4vUXd5RXpVempQQjFyREVyN2o4SHNDSTRIclFqaVNtV1JRaHdqSXN3RCtXM1VhUUhwdENINEhNeGttaXd3UmV6cTJyK3JBVGNvMkJTT290MmxId0pla1dRV2xXTmZmUW1jaWJBVXhkLzZ6NWJ2VXRhUmxRT0RLTmMwT2FrODh3ME9mMko2d2dGTGZjZys4SWN0UVNqcTR6OXgvRU1yRmtqbTVSWXozOWFFY3JZNUlscDVjeVZSNk1nejFiQWpDUzR5TWkzRy9iVm9tTDdCTmxGSDlZMDJWd0lEQVFBQkFvSUJBUUNRODgwaitHb3dod0xpN3ZHRi9EYmJGQmMvMEVxUE80QWUrZlJrbVRlVndFQkNMdFM0ZXhtd29KVjlPUXZ2em1FNlpUcmluSnB2cENmU1ZWZWsxVk1nK1ZuV0lRMWtvMHlsL1dDTjVUVG9RREQ3ZXZYQmVkenl0SGlkb1RDajRXaUR6Mm9OSkExVEFwQzFVcnJaWHBONXptcnhRcnNkaUQvS09JR0h1Z1dKUWc2SnpQelpYeGlJOGI0c0k5MFJlTjZXUXF4UlRyRlEwcmIvMlliNE9vTHNuRi8rSXU3TDIyNWpTWUhrUVhxSVlsT0NWdUV2QVZ4L1dWdW03eFVhTTNYR3lxYVJ3bFlZTmtTODRnSnVuSlpzN3Jab2lxcEtobGpPMHpBenRIdDJ1b1pTOHU4WEVRcTEzV0pxTU4wWjJONTd5RDhNOGNvYTFNcGdHTzdNYUpKSkFvR0JBT0RQNlVYYm1MRjh5MzhHbjh4YiszQ2s0TUlLZks3NEVWclhsQ01QZVJNK0lEVzdBOEJXUWxmdUQ1Q0Z4YTBSL0FDOVQ0QzlkT214dGNUcUIxSi9YVWRBYlBXZDdpZDNRZ3haZEFhNUlrbHp2U281bHpiRzZubzFCTTZRUGpEYmpnbXBOdGdsOHZpalIyVDRVa3h0RGF4K0x1ZVRlVkV2ajJYTU1qNlowQm5iQW9HQkFMMUdYaEc3aWNGdFBVczZXN291akF1bmRBaVp1Z1ZZb2dTTzc3dHVjdEVncFBISlh1eFkxMmp5NzZlR2M1UmtTbDF2M0RlMVpwRUtrSFRWSmxveGY5ZUtSNHFxbW9laTFWbVJSNlFTWEpCaGcrZWMrRXRQREVkb0ZTbWlpLzF6TGhmaERSVGpMcWlxYzFqSUJac0t6dTZjdEhjRWJYY3JSUGZrUHRFbHRGUTFBb0dCQU5sZ0QvWXRUS3FwdVhhODUvekpJQW9lVXZrcy9MeU9Qdkd3cTV0dkZhcEdrd3lCSlRKdjlieGlBd2pDWUk1bGFsOG9yZHdVMVJ3MmFrVFo2WFNhbEk0VnZJV09UTDQ2Y1ZIUm1QLzdPU3orelhVcnRJd1JzSjJ6OEU3dmFFTUR1SWFjNk52OWJiOSsyY1RHMjRUc21hRWxiYU1ibE4yc2VDSjlYRVB0cEN1ckFvR0FKbWNObFFsNDlMN21UY29rYkUwZmF3bnB1QWtBdmk3eWlIdzcxY3FlRHlKUmRTRkhXaXJZWWRuUW1Ddm1iWGcvd2w5OHplekhSNnhlRE9abVpxeGVaT3dRZ2VrRmUzbWxVZ3Z3L2pBZmljZlBUSUlEdXJ2cUlON1VWR00vaGdnRmxTQzdWNzZVYS9KUmZ2VHVkanVtS3JHdXgrc2xEcVcvMDVBQzBzcVVvUFVDZ1lFQXBzbURvQUVsSHpxeVFqS1FPbzcxVGs3N0p4QkhhSG90V3ZuWGZqN3BvY216OG9mQ1JlUkdtRVBpektkTTVJSnlJajVEWSt6UVB2Mmk5V3hVNWlpamd5TElOUi8yc0JORnBwR1hjYUhodjBqZGh1b2k5S0tjVURnN0I3Z0VTcElDaXI4S1RSTHZQczVaZkE5ZlBaOHVZdEsyMjFaR1djQUNGQlBrYXFjd1phZz0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0dBbjFLS3RIcHQ5ZUt2N3NRWk0rMjZCcm05L21FNGIvYjNqY3ZLUEUzeVR2RCsrMEYyVmZhQ3JkSEpNTEhnSjA4RloxR3pTQXVxNTdTMmM0b1JOZkhyQTRwR3liZnVnR0VaQlh3djQ5anQvK2k3MFFvS2Z3R2hlZjMvK1lFaHl2aGVtVExmditJUXZ1RDZ3bEpaRSs0MnY0VW1OOTdLc3htLzVuMXFqYnBRMUFoVUE3N2ZTUkVaR2gzNlE4RkhrLy9iOHYrQ3JpTXNDZ1lCWEJBM3N3N3NEeTlONVZpd2VoM2JpS0tJcGJ2YnFQdjZVSEdVZkhCcGV4anU0MGpIWmpxa3R5NFpWVVdqQlpZMFIrT3pqSXJlUVEzV2dkOVZQeURrZGZjT2dWTGg0RnhhT3pCamhMK2tEaThuR3llTmdRTVNLYnJUc3ZVRlMyNHdHNm91QmtRTEY4QlNhd25QMDBYMHZkZ0Z3bjBkdVEvMGFJUkNkNjgrbTd3S0JnRXh6b1NDUW5nOHgzcVZLWWZXUFpjVmplMEU3dURkSWNZYnhQOVA5TE5zRHVvR3IrYU1Jd0N1TkxWYVlYaUJvOTZHVXA3a1FGUHowNXY3dW1zQUpVbCtoLzdkb1p4UFF4aE5wYUtPR1F2QjN1dTcxdTVwRm5pTkVucW1YMUZmOENod01xOWRyZVllcTJteUtWSVI4T2p3RE9tM3NRTGt2dnlYSTVoSldYKzEyQWhVQTF2T0dQcE05Qk56bkYyV0NtV25adTNoVW1xST0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMmVkMXBlZkVUVFpkeFJUVUw1am9FYUhFSk1BWHo1K2VsNEtvcXc1TWxlZ0J3WUZLNEVFQUFxaFJBTkNBQVF6M3ZoNE5zY1VJSit5dUVnMmZGdlEvT2hpNXhmV29vOGhLOGF0cDJPaEY3RlNsbElRbUVFZ3ZZODZsTW5ycEpKUzBVcHYzR2JTRjlGdjBtQjVhcThZ
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVOaWxYNnpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBOVFV6V2hjTk16SXdNekEzTWpBME5UVXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0dBbjFLS3RIcHQ5ZUt2N3NRWk0rMjZCcm05L21FNGIvYjNqY3ZLUEUzeVR2RCsrMEYyVmZhQ3JkSEpNTEhnSjA4RloxR3pTQXVxNTdTMmM0b1JOZkhyQTRwR3liZnVnR0VaQlh3djQ5anQvK2k3MFFvS2Z3R2hlZjMvK1lFaHl2aGVtVExmditJUXZ1RDZ3bEpaRSs0MnY0VW1OOTdLc3htLzVuMXFqYnBRMUFoVUE3N2ZTUkVaR2gzNlE4RkhrLy9iOHYrQ3JpTXNDZ1lCWEJBM3N3N3NEeTlONVZpd2VoM2JpS0tJcGJ2YnFQdjZVSEdVZkhCcGV4anU0MGpIWmpxa3R5NFpWVVdqQlpZMFIrT3pqSXJlUVEzV2dkOVZQeURrZGZjT2dWTGg0RnhhT3pCamhMK2tEaThuR3llTmdRTVNLYnJUc3ZVRlMyNHdHNm91QmtRTEY4QlNhd25QMDBYMHZkZ0Z3bjBkdVEvMGFJUkNkNjgrbTd3T0JoQUFDZ1lCTWM2RWdrSjRQTWQ2bFNtSDFqMlhGWTN0Qk83ZzNTSEdHOFQvVC9TemJBN3FCcS9takNNQXJqUzFXbUY0Z2FQZWhsS2U1RUJUODlPYis3cHJBQ1ZKZm9mKzNhR2NUME1ZVGFXaWpoa0x3ZDdydTlidWFSWjRqUko2cGw5UlgvQW9jREt2WGEzbUhxdHBzaWxTRWZEbzhBenB0N0VDNUw3OGx5T1lTVmwvdGRqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQjBwSWdlV1VTeGRlM3I5QmMyNVpzZlR1czJBQWhRY0xBMUQvcDZXTzlyN1RHYTBvRGdpWnljN2pRPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUjF3Vm5FTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBOVFV6V2hjTk16SXdNekEzTWpBME5UVXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRejN2aDROc2NVSUoreXVFZzJmRnZRL09oaTV4ZldvbzhoSzhhdHAyT2hGN0ZTbGxJUW1FRWd2WTg2bE1ucnBKSlMwVXB2M0diU0Y5RnYwbUI1YXE4WU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnR3VpTzdxZlN0RVFENWZUU1dLUEw2NC9yUmdUeVUxNlRQUVdPT3MrN1pBUUNYd2ZtdFNEbVlSUmF4bmJxVE5zby8wcUxPd0xlNldtSVhWdXRHbS9YUDNUT1U2S1ZxMmw3azZ4NnBGMFNaVGNWQjZuZUhLWVlodktzWlFqNjZJa3F6Um9rSTBZZEhCSm83YjdNdU4rdE1nT1B4VmhzeW9uUlBvcHhkVnFNMFlSeA==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVDcDhwd0RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBek1UQXlNRFExTlROYUZ3MHpNakF6TURjeU1EUTFOVE5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXBqZEtya1pndzVYYnJxOEtXTDJuUHZFSlZHcmlhL0w0dVRLU1pwdWVDMHU2M3JGcW1QYkx4cFkzRTAvdnhXd2d6eVc1b1lnQnZURGFMeXZXZnhqb245YU5sZGpKY2tXb1MwSjh2aHIzNmFCMnpoSHVhcVh0K0NIRktWK2d0SW4vUXd5RXpVempQQjFyREVyN2o4SHNDSTRIclFqaVNtV1JRaHdqSXN3RCtXM1VhUUhwdENINEhNeGttaXd3UmV6cTJyK3JBVGNvMkJTT290MmxId0pla1dRV2xXTmZmUW1jaWJBVXhkLzZ6NWJ2VXRhUmxRT0RLTmMwT2FrODh3ME9mMko2d2dGTGZjZys4SWN0UVNqcTR6OXgvRU1yRmtqbTVSWXozOWFFY3JZNUlscDVjeVZSNk1nejFiQWpDUzR5TWkzRy9iVm9tTDdCTmxGSDlZMDJWd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQTc3R2RyWkZoYVpSN0VpL1RHWGFMcFZFMEF6SjBxMmw0cmpZSE9FOEpYUlB4UE9BYzFBazBlVmQ5MExvYzRjSDJVVE1ZMzE3YlEvNmdBQU5RQ0pMTHJEckNtNDU0bjRFbGs4WEt3ek5qcVUyUFdsWitMZGlEbjkzeWN5d044dmFJSGRqR0RvcXFtTHNzb3d1ZFluWU01MXhOUjlVZVE1R2NYaExTQ3RIeFRGeGoxdWU3aC9QMEJVc005MTN4K3ErdjZ4QU90YmU0VHFnbHFweU9XTXZlVVRwcnlKVGFzTVZJRFBNN0JQalh3c3RYT1VxVi9rSncrSjFacGtuYlJSVDE0M0dFcldabGJqeWoybUxXU1Q2eDdack1nWnJxSEF1emtXZmZEU3N4T1plamVkRTNPRGVhMng4OURwMlF2WC82QnFoUVF6enVuY3Z2b0dyVjVCN3dw
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:04 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:04 |
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
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:05 |
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
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:05 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:05 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:05 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:05 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:05 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:05 |
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:05 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

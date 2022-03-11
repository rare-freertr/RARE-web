# Example: tls test
    
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
    logging file debug ../binTmp/zzz74r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWpvUmx4M3JDTEZVYVEyZkdsZjlCMnVndWtEZGVjeW5NSmpmd29jZ1BtL3hyME1XMHpJQ2x3ZndIQ2xNbWtxZFJVbXlDWFlpUzN0TWRZcHZ3eGFnVzVWOWJXSTBJajhnclR5Y0wxTkRoVE45ME9pZHZHWlMrRmthY2J5U2hjcHZPa2tMMWxDZkN2R3l3bGJ0andGUnE2dFpNU2ZIRjZSeHptT2pBcnprTm91MzEwbE5RVkJFUWtSaUVOZUsrVjZQNVJiUUlCZG9GUHQwQXRZcHY0cTJqcXpmdE52VmpUa2RGZW5WcG1KSmJiWUdoOGkwcVpoQjc0eFNEQlNlUVNkbU42SDVZczlGUlNMYWVUaW16a3ozazEzT2syVXlvTDM4SWFQbGxQdlFMWjBrR3lNbVRmK1ZIWC9tWnI5SHNWaU5sVmNMbHNEVXhXY1hzb1JQdStBamNwUUlEQVFBQkFvSUJBQWJTN0JTckdoVUpWaUtZRzNnZktzWVNpL2czem52eEttZENFbkdNcE1LeFNYQkxweWFMbW1RNWJ4VGRlbUZYUlp1T3VvZEQvTlJTZzN1dlA4NFhDRkdmU1Q1cU1sakFHdUxGV2Rtc3pyemhqaTBpcWowdFZCUzQrTkNSam5Gd2FHbTBieEhTL1k0TUhrQnRJbytZK3kyWGFUdTVLZUxKaS9kc1haMkdPOUxyUTZHdHFXZmxoT3hHL01tNDdBaUVLbXpNK3lkamhld2xoN2V6Y253ZjJoN1VyczMvdTVsQzNSZHZwRXRqdk9Bb2dXQkt1WVRXLy9YOWcwZmtkRXFsdjV1ZmdiMVZhR2FENUgvaTdXbDRLN3haNFJSdHdpTTRDZEcyeXJ3UGpnSGNWZ3lYUDVQKzZ1S2RNR01WdDE4UFFQRFJiSjF5ZjNhQ0dOZVBKLytvVUVFQ2dZRUF5aks0eDloZ2c1MFF4UkRLWk1WM0VJN2lKNUtKU0ZSa0RpSFo3NHQ5RUxPRXhKRzlLSTlZaTBpazNqYmdIc213OTIrdmZUeTFJbkdxeWhvUmZUaVJYbUIzdWF5bDdrcWF5YzhEZnNOUWFIemtodWZQMExnV1VRQmJ5aVd6aUhnZ0lHZjFpU1lnUjIzY1NZTmRnS0RuVkNub3JpZkVhSUVBdVR3NU5WOHgzSmtDZ1lFQXRIQllNNE1lbmhvTjNDRXo4YTdnSlg2VDRSS3JMM3RuZ0JtMmhleEtxUEJLdyt0VnkyT0dSbjBpb3ZTenJ3WkFlRERtN2t4azZSdDRUWnRTYmR2REJuZEszK1hLZlpnYjZSS3htbTNtM0duRHM0bDhUbFROOUhOL1ltbUE5R0VFcjNyOXk4SW0vT0pJSkpaV2htY3hUR1NhVGRDaFZSVld5eWwydmtNbm0rMENnWUFuaHpyd2RyQ0hpbEVZOVd0YnYrN0M0ZXY4YUgxR0VwbHMyZGxOSnl2UDlBaGtsVWt4Z0xTQ3BqVDA3QzFzVjJtdE5ieE04MjFGeW9yazc2dXptemR3QjlQZ0RJeHp4VW4xWWU4QS9SWGZGMnRscERQUVRleXU4UzhBbWRZN082Q3NOU2FmSlVEeU5kdjIweU9ZWGR4YmE4WDlKZkVUclFTRE1lN05MRXNISVFLQmdRQ2RRYkJOTE1CWmNFR1dFVVh4SThUc1NKWGZPZU1CM2Q1RmNhTjJzb29iRkZsRXlPeWI5eUJHZkxiY0tNSVZEekRPejJma1ZhWTQxeDBSSGdaSUFwakZJT0Nibyt6SGF2TWdQWStXRktSNGdxRHg3eWZzS05MYWNuS1p0WE9UQ0o4SnhQbytRL2F3dlJHOCtWMXRnN0FlY1N0ZUdDOFROU2JRcDFGNjNwSTl2UUtCZ0Vua1R5RHRpbDhBQjFGb2hkMWxJbVlaTGhKM2VOYTMzSTU2dmF3c0ZmYjAyQkp6SC9sTkorWkNXRjk5N1g1RnBUN2Jqa1VSTmI2eElKQ2pvMnRIUFJDa294VTZZWXBLanBVR0FsRmU1TkdpUU8ySEduYTRtTkRyWmh6OC95NGVrSWh5NndMMXhqQjN5U0lQODdGT0d1dmhWbDk3ZVhNUTE1VDE2R1I3am9Nag==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FER3lSb3YrUEdhRzYrcXZaS3d4SXRqODZkMlBxY3ZiOGRwcUc4ajd4dHpXVEs3R2lpMVNDZjl4OFZtMXNWU2N2QS9zanl6N1ZQMU1yRUgyMC9INTdkcThnUDRmOXViWDF3dTBvay91dm1CSCsxTERpWU94dUM4NTErelhmMjRPK2JwaDJUNXVvajljcXpqWEhEMGxpV3JES2JFY3k0NGg3Y1h4eE1rYmYrdFJ3SVZBTmhWODBBRWVMZlZGUVVnVHUveTd2amY5ZE1OQW9HQWMwM2NxSDRJaGxsb0JXdUt1ekF5N3VucVp2bDdUM01LK0M3NlExSmxZUlFzNG9vcEFhbzErcnFCa3JMdnNsaENNNTBrZ09HY055a2Jza0xBQmJqRXU2VDZna3Y0QXQwWmtaNm9aZWZNQ1krTFV0c2d0a2QzeE42Z05tNHhxOXVVVThnNE1sS05yRmhpekVobXUxTkx5Vk5Vd1FIYktYenBKdTNpWXIybmloVUNnWUFHZXdPZmVqMHFBSjg3b0MvaFNTTGNreVZnS3B3OGZDSEVUNUNKQWozU1BweURPbkhiWU5wanRianNCczFnYlhLQW9lZENzR3RGSGs1UCsrc0tSeFdlamtEcEFwUUQ2QStNdXM4N3ZrQXNZSWNqVXB4QzZORGNsM1pmbGs2Z1IzbnFPYjFHclhMWkZSUXhVWWhMR0JjN3RGYk93dS9YeE83c0tVR1VBM0tjM0FJVWQ2QWlkYm1KTDhPUlJxY01zUHduallOcjdHQT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURMSXlpVHo0cFFhSE5oZzNZSFMwWllZTmtJT1A5WC9GakdRTHRiUnljRW9BY0dCU3VCQkFBS29VUURRZ0FFdVlvam1aa2t2VzJnWEJMV21lRWJXN3RuWnJML2FNQTRPRitQVmR6SlByQ2I2Wi9KZ3V2c3dKTnd1bFJBSHVndFM1V1VVaWRqN2lHWlR6a29TK3pKNmc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZUQ0NBaENnQXdJQkFnSUVUbVN0NWpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVEU1V2hjTk16SXdNekEzTWpBME5URTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FER3lSb3YrUEdhRzYrcXZaS3d4SXRqODZkMlBxY3ZiOGRwcUc4ajd4dHpXVEs3R2lpMVNDZjl4OFZtMXNWU2N2QS9zanl6N1ZQMU1yRUgyMC9INTdkcThnUDRmOXViWDF3dTBvay91dm1CSCsxTERpWU94dUM4NTErelhmMjRPK2JwaDJUNXVvajljcXpqWEhEMGxpV3JES2JFY3k0NGg3Y1h4eE1rYmYrdFJ3SVZBTmhWODBBRWVMZlZGUVVnVHUveTd2amY5ZE1OQW9HQWMwM2NxSDRJaGxsb0JXdUt1ekF5N3VucVp2bDdUM01LK0M3NlExSmxZUlFzNG9vcEFhbzErcnFCa3JMdnNsaENNNTBrZ09HY055a2Jza0xBQmJqRXU2VDZna3Y0QXQwWmtaNm9aZWZNQ1krTFV0c2d0a2QzeE42Z05tNHhxOXVVVThnNE1sS05yRmhpekVobXUxTkx5Vk5Vd1FIYktYenBKdTNpWXIybmloVURnWVFBQW9HQUJuc0RuM285S2dDZk82QXY0VWtpM0pNbFlDcWNQSHdoeEUrUWlRSTkwajZjZ3pweDIyRGFZN1c0N0FiTllHMXlnS0huUXJCclJSNU9UL3ZyQ2tjVm5vNUE2UUtVQStnUGpMclBPNzVBTEdDSEkxS2NRdWpRM0pkMlg1Wk9vRWQ1NmptOVJxMXkyUlVVTVZHSVN4Z1hPN1JXenNMdjE4VHU3Q2xCbEFOeW5Od3dDd1lIS29aSXpqZ0VBd1VBQXpJQUFEQXVBaFVBcG5qTkxoS1BrMFBaM25jcUtkSis5RDFMUVVjQ0ZRQ0pjS1U3UzlieHlKR0thRVIvOU5xcG9Iemt5QT09
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUk9mcENuTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVEU1V2hjTk16SXdNekEzTWpBME5URTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTNWlpT1ptU1M5YmFCY0V0YVo0UnRidTJkbXN2OW93RGc0WDQ5VjNNaytzSnZwbjhtQzYrekFrM0M2VkVBZTZDMUxsWlJTSjJQdUlabFBPU2hMN01ucU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnS3NzazY4c0ptTjFCdUtyc042NXcwc1Q5MGpLVkFwemQvVEdiaU5ybEdnTUNYeHovaE1kTll4UDN3Y1pZczhYTkkzd0N4bUVsRHJSZkMraEt4dVV5ek5DLzM1UEFwWE5saFc0WGxEekpFN3RNOEgxdlRZL29YcW81b014RG1uZzl3YjZ3b2J0WjMrb29LaDUwOUZWNndCVW43dUJjbUdxOFoxRzJPOVMvcHgzZw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVSemhCUnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFExTVRsYUZ3MHpNakF6TURjeU1EUTFNVGxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWpvUmx4M3JDTEZVYVEyZkdsZjlCMnVndWtEZGVjeW5NSmpmd29jZ1BtL3hyME1XMHpJQ2x3ZndIQ2xNbWtxZFJVbXlDWFlpUzN0TWRZcHZ3eGFnVzVWOWJXSTBJajhnclR5Y0wxTkRoVE45ME9pZHZHWlMrRmthY2J5U2hjcHZPa2tMMWxDZkN2R3l3bGJ0andGUnE2dFpNU2ZIRjZSeHptT2pBcnprTm91MzEwbE5RVkJFUWtSaUVOZUsrVjZQNVJiUUlCZG9GUHQwQXRZcHY0cTJqcXpmdE52VmpUa2RGZW5WcG1KSmJiWUdoOGkwcVpoQjc0eFNEQlNlUVNkbU42SDVZczlGUlNMYWVUaW16a3ozazEzT2syVXlvTDM4SWFQbGxQdlFMWjBrR3lNbVRmK1ZIWC9tWnI5SHNWaU5sVmNMbHNEVXhXY1hzb1JQdStBamNwUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUgvcTN0Wk13SjBsWUpGSER3bmNFVE5YT0Z4N0JvdzhaelE5Ny8vd2ZBRzcxdzVPZ2ZNdmk3VWJUVmxML3FmL01ZeEpITU1CMDFlN2c0dEJRUW5LZ0FnTFJWcm9GdnQyNS80NDBvc3BSb3hZNS9yOEttQWduWjRFMVdhb3JBSUo1ZDQzTU5xS2p0alNpUGJNMHlFdWVBYStjcHNlM041RmRWLzlQV09ubXd6b0NWdEVpZWtTYlo1bWovQ0hCSnpVZlpkSm1abnFHbTRvUndMM1JmUzY5M2UzVktweWRGc3c5N2xRSm50a0NxK0tTLzBZSDlxNzFjMWlUK2xiODUwK1FEeW5qOVRad0M2b01Bc294eVV0a1pHNGVVY25HTUFaRmd2N2VhM0pBQUhpcUt2ejZBTnBQb0dPQlgwMlkvZDBhcW1kbUN3ZUFlMnFaOUp0ZHlaT2dq
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
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
    server telnet tel
     security protocol tls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
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
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
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

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
    logging file debug ../binTmp/zzz1r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQXVZTFJTYUdhc0YzT3NFaTdYRm53U3NaLzlHNjdlbnNZY1FKQ0cxM3h2R0NlblRuQ2pDSnlRbjdzTEJWQTdrUE4rV2J6QUI0Qmk3LzZjdkx3d1ArUUt0bHBWeHdFWkczRklPdldRTjRVVFl2M1JsSUQvOEE3K2xWT0JFR1BlcURtYTd1YkRPOU1HTnVPOGVOUk5IUkVhYy9Ia003azFvM1NxU3pGQTlhQXVXT1laUkc3WXl4VHVNdk54ZnU4ajBvTTY3QU8xV0dkYXlsSkR4RVhYdzlOQ0JGbHVCZmZ1UWt6YWhmaDF4Zm5LcmllM0FPYUNNRzJxYWZDVlQvcHEzK2lsbTVWT3p0OVR4WFlsV1FJYjd5UVJXOVhXSFl0My9QWGE3V2NRN1ZQK0tzUlVPc0tvTDVOZGlwdFplRUVsUVk3cC9XZmVTSURLTVlMWHdaaiswRkx5UUlEQVFBQkFvSUJBR1JSU2J2M21COG5tMDNaQnZpNTZpZUZrRXd1VlZPMm5WRC9WNkJVL1JSUmEzUzZkMm93ZG5sZkNYZ05SaitTaXlBRGZBVGtOUkhOanpINkRoZFFIRFlQdTlkUFgxQ3Z5NW94N25yRm5WVVNDM1lMZy80WmhsV3BLN2RCZk1Wam5UZEZER1BDUS9SdFJxK25yWklnRFo3cXJaQ3hVUzUxSXlZNC81RkR2ZmlCNTFLdis4Y3c2K1dJVmRoQkgzTndGcHNkUE8xWU10bXFRZjdKVWlpdVA3UmU4cTJBc1lMcG9nMnhPZDhnNFNTZ0JaakloM01jVk1PdEtDM2NhVnoyTG4wVUQ4Y2IxY3J5SUhDRUxOcTl6M3Y2anVocHNQV3NzQ3dEVDdaN29SWjlFS3Rnb2xKZGhySG9kQjRCMG9KcEE0SFRsMWVIUzBUMkJGbFhlNHpiNE1FQ2dZRUE0dzlaVkNTUjJyL1M3ZTh1THFwS2FPL0xMVVVWbzM4cU4xWVFnRzdMaGV6cnF2TGtKSG83Nldic2VjeHFCamRmTUc4YjVwc1VyMDBYWDU2aFFRNy9tRkZuUjJXa2xFZ28raHkrb29vUElabHJjSm9yRHJhdy9US1JBU204cFlHdndFbnprRkZjYzRzRU00V1MwRUxWakljTis5UFBmSlJveTF6cVdpVHRYR2NDZ1lFQTBTZkl0ZVpUMVdMc3FDQ2EvZmhObE9EU1ZMZFRCbVA4R0hudWpZLzh3UFlzUkRjaW9pT3RQU0Z0T3RsZHlHaW1ja3FYdUl1VktjMlZSUXZobyt1c09RM2hLdjZJOHErNVd3cnVkZmhTM054QTJMeTZsYUY2RGl0ZFJNK3dtNHBMMGk0Rm1EajJMMVZBL3dCa2dibmswdUR3dEJmQWlKSkdUSDY2NjJqUytFOENnWUFMMi81ZmJiV01obDVlL1JJZGI5bUpGNVUySFJpZlBJSVk5ODdPMW5xYzJSNEtCTHV6eUFxZkN6Z291R3VGUFpra0wzbDJsdjBDbHZVMGtsVjd6MnU4S2V4S0IxNE1QS1NmUTZjVldENm9FNXBQL0UxcGJGTmNOaXJxczZKZHhxTkdXTloyNERrQzgrelpRQTNHQU9la2VsMVpuTnVHZHozdCtVRm9TZXQzMndLQmdHQlRpVTIxR1hFU1VWb1JRakNyZGRlV1AyaEMwaHNFVzJ0T1pMNlB6T0YxdnVkZjJUU0JaOXpha3pyaU54NEFqSC9ndU1XR2k1a29GSklyS2ExYjhnS0kwT1lET2tGREN3UFNJZ2IwNmZ6TDk1V2FQZmlCMlB2RG52MzlCU0p0YkFRTnJBZnlXL2RxdFRkOEQ4M3JObWFrc0ZiUkJad2dlZjNxODkxTmRyUmpBb0dBUEFYNkR0WVhub0oxY1h2Q1hmUTNwWWJ1US9waVdQcVpORjZWNXZTRzRuMTdaQytpWnlCS1l4aVVZZDdUZ2VsekpxMjhETDJRSVJpd1hjdFdxcmRYTlN5bUVDeWwzSit4NmRhN245VzV0Z3dIYmErVXZ0ekJ3N3NjcnpKYnF5TGVKMUwrMVgxZXZhVVY1bFpETE05ZU5OYmJvZTF5RTBhcXNQS0FPQ0tIdzJnPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0dKV1lpQWY0dDZjVzc3WVhrK29iZ3FFSlUzaSsyaU9KbDNhVkpoVU1XUTZRaVdFUlBreGJlZThjODNVa2p1T2RZWE5LT3dFTjNqZXovS0RBVEFGY3hZOGxCTWtQSURtTE45UXVJbE11OVpKY0lDSExIcnpEVnZScUhTT1U0ZDlmNUNqUG52MEU5Wmt0ekR5c3lCdHFqTlR0Uys5cDFSWWJtQjM0ZWZ1QTFZcEFoVUExVHFkeS9SSEgxb0MxSWhwNUYyVXduWkdLaWtDZ1lCS1Yxc0dBZjlobDBBMzZkNisvbDV3VjkrTFF5cGpHUFlrMUJmU2lOUlUrcjJoTHV6WFZpei9hVUh6cWN1NGdRckdYRTZhWDBRQVkzK1pTLzJVV2FuNk5keVpuSnFCMVk1U3Z6dVBmQkNVY0RESGJOejM5dVZwYUprZTE5QWxkZEQ1S3NTWXVEY2ZiRklTYzNuU3VRcUtjT0krT2FkRm96cm5oSG4wQ3drUXZ3S0JnRkhkamJUdTgrOUFRZlZ1NC9WSkl5VStTYnZPUTlPTGp2QnBzbjNNbUhLaGxUU0JqM2hZSmIyU29KQjVZTGFaZ2FJdGRENFFaWkw2eU9GZWY3MDd2a21kcWxGamFwTG1lZ1A3NVdRVzNjT005NHBZbTVJaEtHd3RsSW5Wd0E5SzNBS2tya0RDaHZ6eFRUUjJ2a0JpbXdVNjBtZ3RrNS9QbHhsaERVQVpuZldaQWhRZ0V4NVZxY2FNWlc0Ym93VnJzYUlidnIwZFh3PT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIM25xUE40L1A0SFJZcmFpUXNsdlA2TkYrNjh2Q3pocWZPVTRvWCs2UFhXZ0J3WUZLNEVFQUFxaFJBTkNBQVFjTHVrVldvTHdsUXRLL01ZRkYzWGlubGd1SDh3UFgvYTN0YnVBbHVWa3JkMWl3TloyU3NPTWtqZjQ5b25yME8zYUNQZTgrWEZ0MW1sb1F4ckFibG04
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVmZnRsN1RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01qRXhNREF6V2hjTk16RXhNakk0TWpFeE1EQXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0dKV1lpQWY0dDZjVzc3WVhrK29iZ3FFSlUzaSsyaU9KbDNhVkpoVU1XUTZRaVdFUlBreGJlZThjODNVa2p1T2RZWE5LT3dFTjNqZXovS0RBVEFGY3hZOGxCTWtQSURtTE45UXVJbE11OVpKY0lDSExIcnpEVnZScUhTT1U0ZDlmNUNqUG52MEU5Wmt0ekR5c3lCdHFqTlR0Uys5cDFSWWJtQjM0ZWZ1QTFZcEFoVUExVHFkeS9SSEgxb0MxSWhwNUYyVXduWkdLaWtDZ1lCS1Yxc0dBZjlobDBBMzZkNisvbDV3VjkrTFF5cGpHUFlrMUJmU2lOUlUrcjJoTHV6WFZpei9hVUh6cWN1NGdRckdYRTZhWDBRQVkzK1pTLzJVV2FuNk5keVpuSnFCMVk1U3Z6dVBmQkNVY0RESGJOejM5dVZwYUprZTE5QWxkZEQ1S3NTWXVEY2ZiRklTYzNuU3VRcUtjT0krT2FkRm96cm5oSG4wQ3drUXZ3T0JoQUFDZ1lCUjNZMjA3dlB2UUVIMWJ1UDFTU01sUGttN3prUFRpNDd3YWJKOXpKaHlvWlUwZ1k5NFdDVzlrcUNRZVdDMm1ZR2lMWFErRUdXUytzamhYbis5Tzc1Sm5hcFJZMnFTNW5vRCsrVmtGdDNEalBlS1dKdVNJU2hzTFpTSjFjQVBTdHdDcEs1QXdvYjg4VTAwZHI1QVlwc0ZPdEpvTFpPZno1Y1pZUTFBR1ozMW1UQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRGFDaktjMWtvUlAzMG4wM0dlYW9WdTEyWVBTQWhSR29kVEV2VDdDMmh3OWhPRXg0SEZDcFJ3VTJnPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUXNQeUJuTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01qRXhNREF6V2hjTk16RXhNakk0TWpFeE1EQXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRY0x1a1ZXb0x3bFF0Sy9NWUZGM1hpbmxndUg4d1BYL2EzdGJ1QWx1VmtyZDFpd05aMlNzT01ramY0OW9ucjBPM2FDUGU4K1hGdDFtbG9ReHJBYmxtOE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnTE1TcE9pSUJuTEswZEpaYWkxVUkwYnhWdm1SNkQyWUZONEszMktrRmM4UUNYd0R0L2t3WUlWeHZrNkllbm16Nllkc3MzOEV4ZmNCVjVCT1QrcWRFKzk4TE52d042M2NVaGYyaE1La3FNcHR1aWhHVnh1L0dYdDJhSWh4ZThLaWFGVEk2RE0wLzZhbzhCUzE0TjFFeUNpT2w3dWNBVkJQWW84Y3QvTFpaUUFQQw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVJVE5mZlRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXlNVEV3TUROYUZ3MHpNVEV5TWpneU1URXdNRE5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXVZTFJTYUdhc0YzT3NFaTdYRm53U3NaLzlHNjdlbnNZY1FKQ0cxM3h2R0NlblRuQ2pDSnlRbjdzTEJWQTdrUE4rV2J6QUI0Qmk3LzZjdkx3d1ArUUt0bHBWeHdFWkczRklPdldRTjRVVFl2M1JsSUQvOEE3K2xWT0JFR1BlcURtYTd1YkRPOU1HTnVPOGVOUk5IUkVhYy9Ia003azFvM1NxU3pGQTlhQXVXT1laUkc3WXl4VHVNdk54ZnU4ajBvTTY3QU8xV0dkYXlsSkR4RVhYdzlOQ0JGbHVCZmZ1UWt6YWhmaDF4Zm5LcmllM0FPYUNNRzJxYWZDVlQvcHEzK2lsbTVWT3p0OVR4WFlsV1FJYjd5UVJXOVhXSFl0My9QWGE3V2NRN1ZQK0tzUlVPc0tvTDVOZGlwdFplRUVsUVk3cC9XZmVTSURLTVlMWHdaaiswRkx5UUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQktvZmUyTjRNaTQyb0tyWEhTeXc1RzFxVXVaKzlaZ1lFbG9oN0I2dFAzSk9FQzB3WVN2cG1ORklrT2l0VkZHbzc3LzZhbDBadnpvbDVFeWhjS044TlE5c0VQUmdiSUUzREZZM1ZScjYvLzNGVEJQS05tbGhlaExpaXc1dDhTejVwbUFWWlRWTjVtaXp6QnZTaFk0aGVTaTBpSEljajNlbWhRa0F3bmkydVo0aU9vbllHUnJoU3A5YnRsRE5LSWlHVVFhL0N6N2kzdk1VN2liakRGdXFWWlZZVkNTUTdJS3Vvd2RxOFNvMnI1NkRudmcvWGlPNjJhbkhkNEU4YUZzNG5aQkg3VGxuN3NEcURVWTdQZmhQRHpGOTYvT2MzMW9yZ3IyMDNqOWdudEprSGpPdmxGSHBvYW1DaDhJakNNNVZoc004L2lJOFVOd0RFdDI3R2EzOU45
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
    logging file debug ../binTmp/zzz1r2-log.run
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

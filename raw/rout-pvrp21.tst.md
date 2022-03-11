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
    logging file debug ../binTmp/zzz57r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQWtXMjdITXdIRU5XSDNYbTVYZ0ZsTUpIQW9WamJGSHZOeHJJOUNHOFJ6K2RaK3VndDUzRE5HNWFKaDBMb1JHbTVQNHRZMDJPS0UwemZ1NkxZVVIvd3NFR05Lem1DL09oMzhJaWtqQ2QzUmFDMlJaYStENHU0Y2ZURW0vaDRDVjZ6VDV0L090MnhwbmVkVGt1YmtNVWdxazlQRWwyOEdQcWVoenk4d0dxT080UTFkSlQvanFsU0xlaW8reEt6cU40UEQrWmtCZ0tSVlRPa3NUbWxReGFMdFRWNG5BVFZkMUpFc0lOODZtSllLRTBhL0hTWFIvVHJnZWFQTHZUa2FOVU9FMUJ1LzExc3VmTVk3bnRGd294WFA4NXJtNE1Bd3czbHpMTGR4ekhyUU5TNmFGMzhqSFdxejBVMU9FUk4xZDJIblNSQlFsbmkyMjZGNFRpQUxORUdWd0lEQVFBQkFvSUJBRERtbWZWcjhiQktiTjRmTVNLWUM0T1NieGlSL1ZEYzlHdXN3WE1WamdLL3czVG9INDlrVWNQR0VjYW15OTA5UTZwSFcvM3d5WndGekhHV3AzQlg4aUlDV01yQkV2ZWgzN3JFNTdldENhRWpFa2RDRWZTK1FhNG41UGloU3hPemdVM3lkb3kvd1IyOXVPcDc1L3A5SHFmRjlVdXlzeTRmRDdGZnpnUlJrRFFZbGExTlo1clhWVGxsRU53NWozbUhCRHNLZkc0Lytqb2YvK0JvWWpQRUk3SktSSTZlQllsMXB0WHZmSUJyTVRiUGlmcFBOV2twOEN3YTlwUUo0bmZ5UzdXckIrSXdJajcrOTc3d2U1RG8rSWlzY0NxUTdQVHExRVBiam5selArR0tBYVI3eThseHFtcWx6SHpCYmthaC8xUUlIY1RNZFFEYmxQMWxHNkpaUGtrQ2dZRUF6Y0VuMGlKQmgyL0I4QlltM1ZGSzB3M0IrZ1ZNL21wdWZJQWN2eEppbVhKMFgvK2VzYzA4M05jempGUnFxWEY3NnU0Y1MwbmMweTA4TDZkWlB0STFsS3dGSWJ0RzdYb0E5ZndqdHQ5Z0J4Vnl4UkxiWi94L3RQSWluaDRQa0lmNDAvQlFiWTB4YS9ESTBFSTJzd0JsT3VoeXNhcU8rWGhsL2VtTHBNVXc3V3NDZ1lFQXRQRkdCS2c3bWMzamdSdGFVUmlZT0lqRjN2RFkrZmYvdzR6dzNVUkw2WXNMMURaZmovbGR3M0RUcUd4V0c3bjA0SWRzeDlMWE14Vng5eXo5eXAveFA4TGZZditlUEJGejdEV1E0WjRzcmdLajhhTDBRQWxYMG15WnhVYi9tc2VkR1B3ZW0rT1hEVXZrQTlDVy95VDQ2UE9weXFScTRLNmo5RlJhWm9YSXVjVUNnWUVBcnZQbEZrckdpWkUveVJRczY5ZHAxbGhHYm4vL1hmM0dBTnMybGtuZHlUaUhOL0cxVU42Qk9BOU01N0FJR2hoREZCcHZ1SjBQeGdrYXVqS0VNbVN2NXNEMmhCNG9TMW1JWTZHSUJNR2ZkNmFITm9lNFJJMXhVYnpxTHFURSsxS0RCRU85UDhubEVqRmxyNS85dnV0QktIdnF1cU9hZXdvalAycE1zVWh6T0EwQ2dZRUFpZ2hBL002RjRSZ0NoUHdqMHhlckQvMnV6UnI0dXdCb2VYb3NTTytQNVpKd0xLeHFERUFVT2tMNUJGUFpBSC9FZ2dCdGlLYWNDbGxDdm1meEY4RVozaVZBR3BxYjBJRVQ2TThZUGpWWEtrdlRXME9QaHNaWjI2bURTTTZYc1RDejlGcG8wMDAwYnkxRXZYQkRzRkk1SENTOWsxd0lPR3lob0lNMUQxN2h1RzBDZ1lFQW5sdXp0Uk14SXhhZjJGZkhodjQ2RDRWVWdIZ21ZdXgwaWdZUkVtTitTY01tS2lnTUV1Y3dpcHFMUUpKR01LL1N0d2dmcTgxMTRGNC9LekprZGVBbkZ4SDNUdXBHd0NEZnpBelRlR2dTQ3RaV1BPcURLMitEbXZ5MnpGc29pWHRqcXR1VStFZXUzcG5hblNNenFMMGlsSTVFT2p5WXJuTkpLVXJXeGtYb2dtQT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0NLcFExUmk1c2hTc0ZIT2hPZGVxWnVvYTRNNVhuclhIRzZWYUY4TFFKVlN4TEMxRkwzUkw2bDc1THd3V29SOEZIRkV1NEM1QThoMENiNkdKNi90ZzlLWmFNTDEvMVdlU2RRZHJmWmZCeHhMSlU3b2tNaGJ5aExFYXF5NW1lTHZKRmozLzJxZGcvTy8wNmxkMVBST3dZU3RYZkQvRElHWjdKTUxHZllabjMvakFoVUE0Y3NjQTE2U0ZOZVQxZmNMcnFJNFpjdVExZmtDZ1lBYVB4cFNrSjFuY0JVNUtxV1BRZ0VKVHF0UzJnbE5vdi9FTEFZR1RHbTZCVzBDTUpWZHQwdFg1MnRxSW5HNXZEUitrczF5SnhwcVdncmkxaCtjcWpTK2pncVVjWjFiVHJHOUU4Mzc3czQzUUdCa1U3WWdSWS9HRDJFY281Q1ZNQy93VithTVBsL2M0dno2d0t2TUp6K2NiRDVZZkxqNUpFaUlSVVVXL1pxbklnS0JnQkg2cjNRVDdKb002QVVGSkpUN2hCb3FLbk02eERRME53NUtKczU2T3NZTHBZNmgyTzY5RFZMZ081STRZc1lUNWxUeE1LOTZ1NkhXUVRQTnlxdHpWWGE1c1YvK050R09kSFFSaVJ0cDVUZ2ovODNrNWRkOHJyRUtWN3J0eTRXZDMxSDdqY2xMdFFjeU9vTDhsTjNCRGxCZkkzYmNHN0RPQ253OG9memthMkZGQWhSZm44REVkWVRreUhPYzIxZG1mbXhhSFRKSXFBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURJRXRzbFdJeFhDbWJVOG9aWHJZYnYyK1hiaWFvTGhjMEVHMXJab01MWG9BY0dCU3VCQkFBS29VUURRZ0FFNHB6Wm1wSFA4cmVYV3ZJbHkrZy9GN2NOTUl1RGU3Y3oycngxU2l5UFBFMjd5YXR1T3JWUVR2WFlIMzVrZG03RUFnSEkxVkp2ZS93VWFhRnJKbklYRkE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBZytnQXdJQkFnSUVUNkR1d1RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVE01V2hjTk16SXdNekEzTWpBME5UTTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NLcFExUmk1c2hTc0ZIT2hPZGVxWnVvYTRNNVhuclhIRzZWYUY4TFFKVlN4TEMxRkwzUkw2bDc1THd3V29SOEZIRkV1NEM1QThoMENiNkdKNi90ZzlLWmFNTDEvMVdlU2RRZHJmWmZCeHhMSlU3b2tNaGJ5aExFYXF5NW1lTHZKRmozLzJxZGcvTy8wNmxkMVBST3dZU3RYZkQvRElHWjdKTUxHZllabjMvakFoVUE0Y3NjQTE2U0ZOZVQxZmNMcnFJNFpjdVExZmtDZ1lBYVB4cFNrSjFuY0JVNUtxV1BRZ0VKVHF0UzJnbE5vdi9FTEFZR1RHbTZCVzBDTUpWZHQwdFg1MnRxSW5HNXZEUitrczF5SnhwcVdncmkxaCtjcWpTK2pncVVjWjFiVHJHOUU4Mzc3czQzUUdCa1U3WWdSWS9HRDJFY281Q1ZNQy93VithTVBsL2M0dno2d0t2TUp6K2NiRDVZZkxqNUpFaUlSVVVXL1pxbklnT0JoQUFDZ1lBUitxOTBFK3lhRE9nRkJTU1UrNFFhS2lwek9zUTBORGNPU2liT2VqckdDNldPb2RqdXZRMVM0RHVTT0dMR0UrWlU4VEN2ZXJ1aDFrRXp6Y3FyYzFWMnViRmYvamJSam5SMEVZa2JhZVU0SS8vTjVPWFhmSzZ4Q2xlNjdjdUZuZDlSKzQzSlM3VUhNanFDL0pUZHdRNVFYeU4yM0J1d3pncDhQS0g4NUd0aFJUQUxCZ2NxaGtqT09BUURCUUFETWdBQU1DNENGUUN4Yi96eW1xNHo0LzMyM2NvTndFY2lwRmtzS3dJVkFLQ01JZHlFWE1LOE56WUxETERLWElHMVJTbmE=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUTg5eGx0TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOVE01V2hjTk16SXdNekEzTWpBME5UTTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUaW5ObWFrYy95dDVkYThpWEw2RDhYdHcwd2k0Tjd0elBhdkhWS0xJODhUYnZKcTI0NnRWQk85ZGdmZm1SMmJzUUNBY2pWVW05Ny9CUnBvV3NtY2hjVU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU83T3JCQ1pKKzF3ZFBlaTdkMjlCMWZQb01pQTMrM1haZ0xEam5vak16SGVBbDlFZFUyTVNOcjQ5Qm5GQURHR3drdnZzblFLekM0WHo5MGIyM3hwMmxnS29pSHhzZFcrdzRmbFBqdXV5R1FYQnBsaHZWbWdzOUVEZHhGNnNSbzJYaEdIdjVEdlpLOGFYb1ZWcVRIbUdMZXpXMWhXeFM1ZXZLZU9YVlVteTg5c1FBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVPTTNZTHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFExTXpsYUZ3MHpNakF6TURjeU1EUTFNemxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWtXMjdITXdIRU5XSDNYbTVYZ0ZsTUpIQW9WamJGSHZOeHJJOUNHOFJ6K2RaK3VndDUzRE5HNWFKaDBMb1JHbTVQNHRZMDJPS0UwemZ1NkxZVVIvd3NFR05Lem1DL09oMzhJaWtqQ2QzUmFDMlJaYStENHU0Y2ZURW0vaDRDVjZ6VDV0L090MnhwbmVkVGt1YmtNVWdxazlQRWwyOEdQcWVoenk4d0dxT080UTFkSlQvanFsU0xlaW8reEt6cU40UEQrWmtCZ0tSVlRPa3NUbWxReGFMdFRWNG5BVFZkMUpFc0lOODZtSllLRTBhL0hTWFIvVHJnZWFQTHZUa2FOVU9FMUJ1LzExc3VmTVk3bnRGd294WFA4NXJtNE1Bd3czbHpMTGR4ekhyUU5TNmFGMzhqSFdxejBVMU9FUk4xZDJIblNSQlFsbmkyMjZGNFRpQUxORUdWd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUZOeU1hNmtxWktJM1NseC9Mc0c4UytSYjBWRnBwc095R3J1bVFwUUdzZmtRN2VZRFNlNERaMlRUYWV6Y0NmOTdlaXNzeHNZMkZtSVlCekFma1BFczZLREFoT28zZUp0ZmVaaGRJNWY4bTVVeEpDRnQrRDN2VGdnZENtemtUeDhhZFNEZEZQa1BQVzBYd2pSSXpHektzSmVkMGRvblhFQVRDb2lMY0VoalZlUGxKOFkzZTRwdU9DZ1N2Mk1tb0s3ZXJhUG4vV2dUN1pyZ1Y0T3dWUHZXdENXbURkSkVoSk93a2NPN1BKb1J2ajBsR3FEVGlzVG5IM0NQMmU2c3VRbXdQbTF0RmtEZFU0VG55TEdtZENZaGZmeUtVQXVNbkg3WUl1cjFBL3JmcDRnTTlFUFJKWnl4YjZRdXEwNkthUFdnb1liS2xscGtQWUZtK3Bxb05LRTNX
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
    logging file debug ../binTmp/zzz57r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQW1nZTl2bFE1bnNiakg0UUc0OTVuci84RGVwbnFodFRSZmlKVVhCTlNKVWN0WW5vWU9nb0MvTzgxMS8rS1ZtZWJHVTR0bUpUWjhNR3VoK211QVExa2g0dXBpRWlEWlhhdW5xSGZ1Q3QzS1JKaUF3d0Y2YmlTVU1sMEFhaTlWOTluRlV6Vk51QzZBVjQ4bG9hcVN3MTgyVzl5ZEdybi9GNnVtYUsxQjZyNG55MEd6cEVJdGJtajhva0tGQW5Fa1ZOeWdNN24yQXpDcTdLY3dzQ0ZoeDNLeTRkQUFuS3djTVJkOGFjMzJIciswWkU3V2hKLzFTcHBKN1RMMlZsQU01TGV6Mm9sSlo5RmVWVS9oamJYQmJyanNqamZjcCtneWdYZnBkUWFZbXJJc3dZS21heU9hazJkdXArUDEyd2NaVWpqSDI4MVQvK2dQWk1kM0Zka0pwaDFBd0lEQVFBQkFvSUJBRWlVMFVKNHFkWTUzaGlodkNWd1RlZlBBVEtxaUtzVWFjdElIZnh0Vms0ZXBqSTdXbU12Q0kxcm96R3ZSdDdFWDMraktUVTNIeU9tQUxvbTBVbkpwODkvYmxtNzRiN1VHQ0RFSW9uRVlaaEhBMHh3US9FSWVsbjdNK0Q4Ukl5OXh2TndpeUFhOFV0bnZxRW52K014N2R6LytTMEdtMTUrdDBQS09nZnM5czc2UmprazFHYTE4RlM1NFU3KzF5UmZrb2xZWGNFdDM1RGFiZm5QY01YbXRzYTMrdk5jM05LbUlSSll4MVZybUd3NlFrQ3FCLy9xR0tqTTNvOHpzeFptQ0oreEh4M0xITUVGWk5TcVZjMmVtZ0QvL1EyU0JwRjJMdXplMmlyZHJ2b0VPT2NGTCtwaEh4azdvUjlmejVCS3ZNdDMxWWFzNmJ3VUs0SDFxaEtycEFFQ2dZRUEvQUVzV3duU0I2WWFNZzhMWnJHSmpPWEgzMXVkcS9CcDN1UkFHMDQxWGVBaFhkR2ZEM3NBenQzQml0ZndiTUpNZjJNR1N6VkRlK3BCOUJ4WWFISkcxbis4VlFQMFIzMTBmM1NLdis1OTY1V1VZL205cmt0UjlMeHFweGRyb203OEs3RWNQUG12Nk4xcjB3RG9UejlVWU94SjNYdVFiZWdQT2tvWElxRTdhZ01DZ1lFQW5IanAwRDQyczVIL2FodkZzcDMvRHhpR1drSTE4MWh3VTNZc1hyU0c1cGxvU2xCVUtvRmk1MzJvU1JnUFBTaXBpREp1b1lpNU5vZUhUb3RsWkxvOTFRaXdVNHdyeXF1SW9nS29pZEhJelRWSGdXbEZ5VWgvd1pJc2Z4bUdoUzgwZ1VJMCtiQ0pkN05JcENCbW1QajVJQXlMVUZDeExiZC8wRnJablJYV1dRRUNnWUJ4Vm9tL2JCeEZDbVJ2clNxQWhrcUp6dkprdDB5amZ0M3V2Qk5FOUppMTNzN0M1anMyZUNpMTRUQmhwSnJpSDBUT2FoZnpqVUlMb2lFRmpCWUs2NUtHZUM2WXdjMkV0WnpHa2dDeEw2NzhYR3EveUJ1U0h4ZitEUnVlaUw4RThBdUVEd1RYTzZqcy8yQzJKb3RVMFBPL0g2WmM4V3pVc1hEZjAyQ3lWM2RrUndLQmdRQ0tXSm9haGpkbFUrdnBqSDZpNi9FdERya1Rxc0Q2MUxJVUNVTTN4UlFWWllRQldMN2lDaDVCb1NlZTRRZndRamlLOUZRK3ZKMU42a3luRkxia2RZcmdCZHVwTXlFeEE3TTkwMjNpMVRwZXZnSG9HUVViNzk4TmJrbXJZdzArU3J0NG9lb203b0RNOWhaL0R5ckhqREx3dEVhbEQ0Tm9jWHN2NUhQTjRSWHhBUUtCZ1FDT3Baejc5T1hacW1qeGFsaDlQT0FyZmtmeEtBQUE4L3dTWXhHWldXUmg0U1FKKzlVTEEwZG56R3BMWVdvSW9UVGY3bXdHUDg5UGVUdmZOVDJUdHpycHlNRGdtZkdSd3NRd2tYeTZ5UEFTdE1DYzM2YWdKYWQweDhBSThneG1kUFpmcmxyRjk2VDB3NUxIZk8yaDR0U1dFU3JYQkIyVmozdkFTMEJjSitzWFBnPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ROWExFUHJaT2w4SlpvU3hmbm1lTUNIU2I4YVZsblN5NXpMSU9UL3FIWmZTK3JEck04U0J0aDJQMHdJcXluVlBVNHdOMnBkWWN3WXhlb3BITWJxRnpYc1VwdjlOYVhObFRISTZsRDVoeERZYVZodGx0bkp2MSt3Q1ZNbEI3SmxzZUVQc2JFVXg4RVZXQTBUb3dDcE56MTlIUjlXT2pVVUtvbDdTNnY4anRSdkFoVUEwRVZFOVhkUG9NUUlUSk5SOEMrYnc2ODdCRU1DZ1lBSTVSb0UzMWM4WUZhcGZacGxNN2ZteHBpSWxpT25TQ2paRUtGM3VKV2lxZTUrT0lKVnpZNzdSQTF6TFpNOHppQ0ZlRHVybVJkQVEzcGRCMjU1WldBL05Kc1UwVE1mbWVYQzVZT2IweUYrMHpNcXBQdG03ZnZ4Rzk0ZHFsaTg2eUZGU2NKRmRlUVlyUXdoc2l2ckFBUXptbmVLUkpVTzd0TGRkV0N1SVB5ZjVnS0JnQzBpSHBxbW1IRlViYVBSZEtOTXdOcWlMeWZJM3Q4aDBraU5RekkvZXZubEVvWmR1aDFyYlkxc2I2eXRUaXF4eUhqVXJ2SldyVUhpQ3hsb0dURmdoSTV5bFllRkhmK0tmaWh2WWVtNDNDc1JzVFZybEZ5cWpoSk8rNGNBSDJ1N1h3aUZtTmtZOXhjRExFVWVvUHFoWlFPRHIza01XbmV4SU43bytidnY2RWNPQWhSbDh0R0pRQkxRQjJFMlh6d2M4bkE4Z2ZIT0xnPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMGVLY05jUzhacFZ0WERmeFlESlN3eDBueWJJcGpiTGhLbWMraElwS2RLZ0J3WUZLNEVFQUFxaFJBTkNBQVRUeVUxNkpES2NHSjBLSVRDR0s0b0VBbDVhT1VPcGhwZFYxTHEvalJHOHREL3NSN0dPS2lTUGRSV0RrU1hVdWdWYlhJRG9ZOEM5OWNNUjEvbXZXTytM
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVORUhaMVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBOVE00V2hjTk16SXdNekEzTWpBME5UTTRXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ROWExFUHJaT2w4SlpvU3hmbm1lTUNIU2I4YVZsblN5NXpMSU9UL3FIWmZTK3JEck04U0J0aDJQMHdJcXluVlBVNHdOMnBkWWN3WXhlb3BITWJxRnpYc1VwdjlOYVhObFRISTZsRDVoeERZYVZodGx0bkp2MSt3Q1ZNbEI3SmxzZUVQc2JFVXg4RVZXQTBUb3dDcE56MTlIUjlXT2pVVUtvbDdTNnY4anRSdkFoVUEwRVZFOVhkUG9NUUlUSk5SOEMrYnc2ODdCRU1DZ1lBSTVSb0UzMWM4WUZhcGZacGxNN2ZteHBpSWxpT25TQ2paRUtGM3VKV2lxZTUrT0lKVnpZNzdSQTF6TFpNOHppQ0ZlRHVybVJkQVEzcGRCMjU1WldBL05Kc1UwVE1mbWVYQzVZT2IweUYrMHpNcXBQdG03ZnZ4Rzk0ZHFsaTg2eUZGU2NKRmRlUVlyUXdoc2l2ckFBUXptbmVLUkpVTzd0TGRkV0N1SVB5ZjVnT0JoQUFDZ1lBdEloNmFwcGh4VkcyajBYU2pUTURhb2k4bnlON2ZJZEpJalVNeVAzcjU1UktHWGJvZGEyMk5iRytzclU0cXNjaDQxSzd5VnExQjRnc1phQmt4WUlTT2NwV0hoUjMvaW40b2IySHB1TndyRWJFMWE1UmNxbzRTVHZ1SEFCOXJ1MThJaFpqWkdQY1hBeXhGSHFENm9XVURnNjk1REZwM3NTRGU2UG03NytoSERqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNKOE4xa2NScXZkTkIvOWxNdDNXVUxjUXl5M2dJVUZFdExoNFdlL2JKcm93ZTh3NE0vTGhJY1RLZz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUS9ncmhwTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTBOVE00V2hjTk16SXdNekEzTWpBME5UTTRXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUVHlVMTZKREtjR0owS0lUQ0dLNG9FQWw1YU9VT3BocGRWMUxxL2pSRzh0RC9zUjdHT0tpU1BkUldEa1NYVXVnVmJYSURvWThDOTljTVIxL212V08rTE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBHVmd4NklULzc1dmRuZ0lSdmJKUVczbmdvOGYrRTdUNlM3dUVjS3VTdDZBbDhWL1luaFdFNEY5UWd2c0R4V3l0U2pLNGNHQTFCeFpHcmJLdjRta1EzSkYwRjNsOEtleGhlcTl1RWY3NjI0anVmT0tLeVEyRUQ0M3BGVzNyYk8yMnZTREZyRHhiYjNXKzVOUmhiemo5RS9RbTZSamYyaE5SYXV6d0c1c0lBZ29nPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVjenpZd3pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBek1UQXlNRFExTXpoYUZ3MHpNakF6TURjeU1EUTFNemhhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQW1nZTl2bFE1bnNiakg0UUc0OTVuci84RGVwbnFodFRSZmlKVVhCTlNKVWN0WW5vWU9nb0MvTzgxMS8rS1ZtZWJHVTR0bUpUWjhNR3VoK211QVExa2g0dXBpRWlEWlhhdW5xSGZ1Q3QzS1JKaUF3d0Y2YmlTVU1sMEFhaTlWOTluRlV6Vk51QzZBVjQ4bG9hcVN3MTgyVzl5ZEdybi9GNnVtYUsxQjZyNG55MEd6cEVJdGJtajhva0tGQW5Fa1ZOeWdNN24yQXpDcTdLY3dzQ0ZoeDNLeTRkQUFuS3djTVJkOGFjMzJIciswWkU3V2hKLzFTcHBKN1RMMlZsQU01TGV6Mm9sSlo5RmVWVS9oamJYQmJyanNqamZjcCtneWdYZnBkUWFZbXJJc3dZS21heU9hazJkdXArUDEyd2NaVWpqSDI4MVQvK2dQWk1kM0Zka0pwaDFBd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFrNHc3SEJJcTRVcXVuRVVsRzlLZ3haL0dVQ2ljaFB4V2lTa1FNcFQ5czJiR3hGZjF0UCs3cHNWQzB6K3dPZFVnQjVaQldQTGJ1cnhUQnFudS9INXdyQ3JoUWZLaW9zSUJXTUo4R0pWczV1MEJ3Z2ZTZ0pHeGpRZktwdU92WG5YYWphZEs3Rlk2ZFdqNXpQWE9LLzZ1U2hYTk40VGhaNWhqWjZsaDNHeWFzemdrK3c3Y0VyU2lyV3UrYW44SWNkaUNGU281bmpWc2FyR2dhV2pnL2RKZW9BS1JtV2ZEcElETkh5Y1MreGx4YWtyM1kzb0RXaUxEMW9LT2RhSCtraERmdHVnR3RHVG9kdGh0SHFHS3hQYVExMzVMbW9iQ3JxR2tjajBHYXFNdXJsT21uQnRNSmpQR0J6Uk84SGtHdHBSZ1hmZVptWXR3bUY5ck5Zays5RUkrMmc9PQ==
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:05 |
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
     | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:00 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:00 |
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
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:11 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

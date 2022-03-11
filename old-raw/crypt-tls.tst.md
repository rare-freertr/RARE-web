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
    logging file debug ../binTmp/zzz56r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCSjExV28zZ0tuUkRkOGpGdU5oUEV2VitCZTBYMGM5d0RzdzRlZ2xmZWZOb1NxSTVOMUMrOEl5SVZodm83TTBWYWtiY0ZmWVJXTHRxZzJqQnlxQTNuM295eVUyY3ptNXdmelpWK0w0c0lVMDZVY3lwc2dHWHIxbnR3SFZ5bTVaQU9YWFYvVzd2Q1ZrYjZwbzRLb2gweTh2QTNxVmhnTWpRc0VMRnZybUxCYnR4blBTcGMwdUlVVzBsbzh0a2xWUUFoMU96Q0VoanlVSHhrWXI1b0x4Ly9CMSs3dHA4eC8wQ2s2SExjYW45cU9adndtd2NRNEVaSDB1d3RwQTQvWnRjNFlBVjJYbExaN0g4c2IzN1BhcFJPMGlYL3o5U0RnMS9yL1kxcElZSmNnak9ZYTBCb2FhTU8zOFZ0NDEzUmtRYWo3TS9UY1pteG1xTUY5Ti9mR0o0UkJBZ01CQUFFQ2dnRUFEYzdOZnRGZEQ2Z3E5QWhQQ215a3FTUzJtU1IxVDloRWZRR25OL2t6SDd1VEhUbWYxbEJQOTRWL282SjlrNEZGd1dPZ3VGUXdNanNLdzRCNXo3VHN0c2oxaWpRY0k4VnA4REt4cGpmVjhRME9vQTZtNlY2NlpubTVUVW9ZVEVtT2ZseUFrbkdGM1lJdWRBeFdYMnRGaHpsbkpMM0txM1lvYkRSYlQvZnlhb1BrTnpTMVJSYi9HVnlvL0NpaFIzaGtZcEdhZ0lsQ3g2YjZkNWNrSGJnaTQxQWM3VnBzUlFNSHVOSEx5TThxZmQ5c2IyWnozQlk4Uy9HNXVnMk4wVkdodUp3RDAwcjRVaXF6bmlQMWVpZTl3VE5wb2xEOGNIaWlBUEQ4T1g4VVVydEJTbWdNdkVkSzUxV0QyeEtqZEorbU5mUXBHQ29GSzNzd3NDSzFmeW1VVVFLQmdRQ1JwMVJzRE9XNHNLN1AwcC9aRXF0eGFhVER2T2NiRnQ2clNqRTBqWS9jMElyZFJEdEFqa1NqVUpaQ2xyMXhiL1lYZjlkaWhsRmI3VTN0SGZub1lXc25KK3RJTytMN0tKdEU0dndKb1FZN3loTVhKRUIzRDlzMnZDT1RRVytyQnlDUmN0ZzI2bFdhZGxzTGl2YjA4ZTFCQWF4LzJpVHdrdU5VYk1rNlVQRnAvUUtCZ1FDQnlHVGZaTkNrazRRRmo3ZXlIMU53VzkydFkwdHJsZjFrYWxaTGZSWUM2T0h4WmhjTjJJaTZ2cVkzSVI3R1dQN3ZWSWVzY2tRT29MWmlhdzRyUTVRRDAvN1laWG1NRnFYby9hS0V6MG5vcTUrbUN6K2YvU0FQVThzMkFLcjgrMTlBNFlMM1lZcGFPcFNZWnp2MkxUbXJ6NTMrNmdBeWZxNVc5TlJQNnBaa2xRS0JnRXJFRXhEWDJmL2hLZ3JoK2sycVNMa1IycExqWDlwRzlnd0ZMSmJtWjhlWWdQK3RxNkNxcHM4U2FkOUtrM29zVjYyZVlRaGhIRmhNeXVpQnI2dTZmZzkrYlVjSi9xeWdIbnZRN0VGaEY5c1BFcGVaYzBIcXNNTTY5aVA3dmYrVHpBTDlhY0Zlcm94NFhxbmhMbjF6eGk3TlZpZlc2WWxZVFRza0VITlA0MnhkQW9HQU9ycExxeXNibnQyQjZHSllaYW4zUCtqU0x4dTNqVCthSWs1Y0xseTBFUzBBMFJPNWF2S0pMTGdJenZtVnkzdUtJUkxITWltaTBsdTNMR0gxVDI2TkZBNWlTOW5mWHAwQkJxVi9YVW5QMEJHWmRMR3lZTnRTSHAxMFgwTitIR3hEZGtDVjJ3dXdaNVFLbWN4ZFBkREpRQTM3R05jYXI3N1RkVlhrblNVeVdPRUNnWUFkYnJkaDlRamNSMlF2QTczdEtQTllkUGFpRTNzNGpBMmFnbkhWcFJjMGNhN3cvWEllSUNkNTF4NHhULzFHNTdPRnFMSEY2VGZPMUliUG1xejFUMUF3RC93MERuZUxnWTVmK1dJNlNnTWZ1b0VzRmZVRWdPREQ2SXZyZFNTRldYNmVmUnhMYysvS3Q3c0lTOHR5U1o3SFVuRzVxRFIvWDBXbld1Y0NwMTFXZ2c9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0RJZWoxYkVTQk9zVG1FNC85Skd1OWV3Zm1XQW5OaFlOTnRia1U3eVdNZHRhRG01Y2QzUXZjRmpYMEs5Rk5FVWdWSGE4dWtoZHhaRTE3ejA3eDVNSDJnblNHRzlnVHRpcWFHdWI0MFg5TURqcFJMeU11QkxVTDAvbWQ5Z2FkaUdLZWRaeXB0QVhyNzdVTXNhYjFzbjJmeDc1QTdSZjJ1cUo5MmJhNDl0eG12ZkFoVUFzOEpEYjE1Y0pqelYyTGpQczl3ZTJKRTc1R2tDZ1lBeFRjcS9HRnBCelZvNmZQNFlUTW5FMVBNTWJ6RmJYUHloMGQ0YndWSWYwTUQybTVjb250bXc0bGlIaVd5bWMxNm90VlVCeW9DV1JhT25wL1RPNmY5R2tUdi9CM09RTkRwRFlFZUk1cFNwWXhiQkNHUm5Uc0JXWWg2aHhoV1l5RGJqNWVkeUw5bDUrVEcxZkdVTVFJcjV0LzJueW1kMHdJR0RiSkZyWEtUbzJRS0JnQ0RSbFFUSVhjRGRpREo3dXd2QUxweXRzTUhUNysyWXdPcmFiUG9lYTRwWUNiVzh4YlBXdjcyZ21ybndua2FPcGlyM21DQkZqTERUNTdlaGMrdE9IL0pocFFHZ2Q0WnBlOHdiL3NFdzBHbmFIWXZ3LzRpb1ZoeWFCbmRvSlJVY09uc01NN2RFM09HQ1lqaTV0SllmRUdzTVNvVVFhVHlRY0Ryd25TRVQ0N3dhQWhVQW1HOEpkdmltUEI1TTNZbHNUdGxsR3FrSUUvZz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNYUGY4V0VLVi9GR1pQaWYyZjhOWHI5K3RyTWhRaFJIQ3ZuQmxCdFNLZW9BY0dCU3VCQkFBS29VUURRZ0FFZlhSTHdSRkxvZFJrZkZ0ZG9MV3JaVVd1aXhRWWRzaEtjUWVDRWJUNjkrSzhNclBBZzZ5eWxXRUhGWlN4YXIxekpUQU1LRmw2ZVpPczhjM3h1VGFpWHc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVIdm40b0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNRFEzV2hjTk16SXdNakF6TVRVek1EUTNXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0RJZWoxYkVTQk9zVG1FNC85Skd1OWV3Zm1XQW5OaFlOTnRia1U3eVdNZHRhRG01Y2QzUXZjRmpYMEs5Rk5FVWdWSGE4dWtoZHhaRTE3ejA3eDVNSDJnblNHRzlnVHRpcWFHdWI0MFg5TURqcFJMeU11QkxVTDAvbWQ5Z2FkaUdLZWRaeXB0QVhyNzdVTXNhYjFzbjJmeDc1QTdSZjJ1cUo5MmJhNDl0eG12ZkFoVUFzOEpEYjE1Y0pqelYyTGpQczl3ZTJKRTc1R2tDZ1lBeFRjcS9HRnBCelZvNmZQNFlUTW5FMVBNTWJ6RmJYUHloMGQ0YndWSWYwTUQybTVjb250bXc0bGlIaVd5bWMxNm90VlVCeW9DV1JhT25wL1RPNmY5R2tUdi9CM09RTkRwRFlFZUk1cFNwWXhiQkNHUm5Uc0JXWWg2aHhoV1l5RGJqNWVkeUw5bDUrVEcxZkdVTVFJcjV0LzJueW1kMHdJR0RiSkZyWEtUbzJRT0JoQUFDZ1lBZzBaVUV5RjNBM1lneWU3c0x3QzZjcmJEQjArL3RtTURxMm16NkhtdUtXQW0xdk1XejFyKzlvSnE1OEo1R2pxWXE5NWdnUll5dzArZTNvWFByVGgveVlhVUJvSGVHYVh2TUcvN0JNTkJwMmgyTDhQK0lxRlljbWdaM2FDVVZIRHA3RERPM1JOemhnbUk0dWJTV0h4QnJERXFGRUdrOGtIQTY4SjBoRStPOEdqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGR1duMm5PVkdqcFN2MVhpdys2dXN2NHg4SEtrQWhSNGVOaDl6WE8xQVZsSEN1OFhrS3VxRERoa213PT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUUVDZC9LTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXpNRFEzV2hjTk16SXdNakF6TVRVek1EUTNXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSOWRFdkJFVXVoMUdSOFcxMmd0YXRsUmE2TEZCaDJ5RXB4QjRJUnRQcjM0cnd5czhDRHJMS1ZZUWNWbExGcXZYTWxNQXdvV1hwNWs2enh6Zkc1TnFKZk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU0zTXRZR05uMGpVd1pkeEc1a0szbGw2Vi82ZGROL3loVWlLQ2JTRHMxeDlBbDgrMHRBUmtwWkIrRkgvY3g4eTVmMDdDRWZTV2NOSXQwWTh0UmlJZmxrTGFCSDNxNFZ0NVJuWWVWRTF2UU1ITjVJVUxua3lKdlNkSy9qYmxCN0w2MnJ2N3BEakJ4N1FvNFR5Ty90SXB2M05NdjFRc2VRNGlYK2RraVJuaEYwRzF3PT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVhd3NPN3pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVE13TkRkYUZ3MHpNakF5TURNeE5UTXdORGRhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCSjExV28zZ0tuUkRkOGpGdU5oUEV2VitCZTBYMGM5d0RzdzRlZ2xmZWZOb1NxSTVOMUMrOEl5SVZodm83TTBWYWtiY0ZmWVJXTHRxZzJqQnlxQTNuM295eVUyY3ptNXdmelpWK0w0c0lVMDZVY3lwc2dHWHIxbnR3SFZ5bTVaQU9YWFYvVzd2Q1ZrYjZwbzRLb2gweTh2QTNxVmhnTWpRc0VMRnZybUxCYnR4blBTcGMwdUlVVzBsbzh0a2xWUUFoMU96Q0VoanlVSHhrWXI1b0x4Ly9CMSs3dHA4eC8wQ2s2SExjYW45cU9adndtd2NRNEVaSDB1d3RwQTQvWnRjNFlBVjJYbExaN0g4c2IzN1BhcFJPMGlYL3o5U0RnMS9yL1kxcElZSmNnak9ZYTBCb2FhTU8zOFZ0NDEzUmtRYWo3TS9UY1pteG1xTUY5Ti9mR0o0UkJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFDdmk0dTdzYjErL1FUdkpJSjJHcjVRbWRvQlB2a0R4VlEwS1ZzVVZrR3VPdmZCQ2ZrUEZUZEo1Skl1Z2hCd2lTYjJGQVZiYmw1eDZXRDBDY2lBQW5DbmFVRFRiSXAzK3lSaDVKREhxZzdyUHB5bkdSak9BK0I3WnBQSEY5RThlOUxqbTBKcVdZdE8wTTJSQmVDQyt5cG5JMURkTGQ3N0xTVHZXVGpRMkI4OXhyTWozd2o1aHhlWGU2ZU55QllNeDExWlg1TG1CK2xOdXBSL2pYbThST3dtNWF5RkJGaG4rK1o0b2s4Q1V0VVRuSEhwSUxLK0J2UExGZldIdENiSXcxQlRCR1dYRGgwWFY5R2RJRGRTSTNqN0JZc1Nqa0crT3k3ZDROR2Rzd20zV3VrQXhKQjdiemdMRXBtYlcvTW4rcUQrb1dBbjBIcjcvaXVma0N3SC9VWmc9
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
    logging file debug ../binTmp/zzz56r2-log.run
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

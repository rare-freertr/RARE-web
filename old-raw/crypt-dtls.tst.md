# Example: dtls test
    
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
    logging file debug ../binTmp/zzz58r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQTJBTHhwQ2U2MjVaaURGc3pZZ3FxVjVWNFV5enZaN2N2L0VtZ2xSSG1xZ1RWVzhoK3o4RXZYdlU4VEdldVR5TGxPSkZhd0JjYVdMUlBnUUtvSU5Yb3hlQ3J3cE9ZeWZHamJTeXhIQUthVkw0NnExQlltcHliTXdKenRxL3JPK0FUMmpTVjRxY3ppMXNhallmK3BpdjNpeDd1ZStDMlBYWTVWbnA0ZEVqUVZSOEI4NDY1NWtIM2Q0bnVMNzc1UHNnbjdsbnA2dyt4TVVzTGZUTTE1SGR0bEFjby91eThteWU0KzdaTjdTY3R0NkNzK2NhOHlydkVtVW50bzU4MUdQSHJjUUpYQlRNemp0SWJlQXBMVzRnaHNqM0ZIcjBDcDdjb2NheGZrOUo0UVZTZmJUQW9QVFVSTWlSUzlaUUQ5VEdLRTBEdEtTZlp4Rk8xTWZHWjZDNTdRUUlEQVFBQkFvSUJBUURQV2xRWEhjUXpFYkpnNWhMMjVBSU1QUURaNXVLUkRyblRWZUg5OXNjVElieWxkRnEybDEwZnJBMEwwdUx5T0M4TkZBcW5KZ1kyYkM5OVNjMldaNEFnb3NCOThTelRmVTlCZDRzenRoUHJrUWZFZDBYMmRLcE9WdVk0MGJuZktnUWtqQ0h0Qms5bVVEZTI4SHF6akxUOUtONElyL2FBSFVLQkR1TWR6TitmTkhhMXpBb3lEbi92UmZRVWNMRkZlVEV6VTNpeHFjby9pbmJSbU8zYm5CM29UbjUwSTlFUzB3K1hZaGRSQWlqUTk2NTVLa0pobzZJQytTNmdWcVZ1K25vdDBYRHBKSUo1blRKc0g0TVltRW5YeURFVERMZzNvcnhJRVZFVVdUV1JRTTdoZk1wNHFIdlQxaS9kaUsxRi9DZW9TZ1Z3aUtyVFQydHBGY05ibHdWNUFvR0JBUFp6SVpYcEtVUENtZnY2MWVkMWtOQWJ6UGZza1RnUmE4aCtROXJCS3kydVZic0tKWmtOeFNmZ2t0c2FHcG1ZL3hiZnlTWnBmZXZDVk9YOWxGMWlVKzVCYTJDMFU0MUJBN0E1cVN0V2R5TnJ5SXY3RnhzdU9rdk1hOU1pWWJ1Mmx2WlRUQTI0bXNZN1B1R055TU9MQmJNSnoyaXBYRjkvUkJBZWU2Slh5T3pYQW9HQkFPQmgyc3JIN0pNUVVXekZ4a2xHUFZpN1hHWDlOdHlqVlFyT2ZyaElOdllCVERDejBIdzJNZzhiTGpKZzMrdzVRanAvZmdwOFZjQmxuMFJPd0NXN1NnQ0JWL1ZONmQxNW5pZ2t3bUo0bXNjMWg0b3JtOFEzZHFUeklkUXRuc0s3eW0zeTBhTWlpM3FFWEkyQ1d5Mytqb1dvT0l4a01rVllMNVBxOHo0dFlYMm5Bb0dCQUtmUGszSHhkdUNsMUpZb29aaGVqRUc0ZkdQZzJLMDE1NDk0c3BsMDZRTE03NkZSY25KNlZ1SWxYN29EVjFONVExRC9Cb2U2VXp6Q2NXNjlzVlc1QzI5emFqdEo3bzZEVTVDZVlwdVkzN3psdW9QZWNFaFl2T2M2QmIyWmJyVVR5azFtUUtZaktuaUtoUEd1eXFLanVqakVHRStxNnJRNEEwOTZnakx6MVdPM0FvR0FkN0RiTkJaSFJQK01YN2gwR0R3bWwwR0NmVWtBVGR1MmpvZ3VJb0VyQ0RrUytsdkExN0ZWTEtlMEVkMkpOUW9xSU9oSFJMS2tUM2dsNkJzVjlrcWNvLzVhL0JodXF0eW9HQVBieVFsS2p2OG42UFZ3SnMvck12d2F6SUwxVUMwNlEwSW12NTI2eDBUNTFlWjJXdWVTQVF3RjlpV3doenNPVGhvalhNUjZYN3NDZ1lFQTFtV2tFMklEd0dpeW5MSytUdHNRL2hWeGZVNXVyN1JoZENmdWZUbHdoNno5dGFPaDlETFhQbkJsbXpSWHYxQmxFd1NjTlFTa2pGQmNadEs5WU1QVnlqZmlCMW91amlESzNnSGdEQTRYSklya0hISFBoZ3R0VEdlRDN5QmwxeTZ2SFFvNTkraUNkTktBMWdhU042b1NKbGRjb3V0RDlXNE90ak05ZFB3azUyMD0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0cxYXB6RTNKRFBhMDZydXZHT2M0cmgxVC9qZ0tLYWpkbUVveDFCNVBTMGI2eWs3SHFGNG9CTWRxS081R09pTXNPQzFsdTNLY1RtM2xDVFRsTHN4NWc5R1V4emc1S1pkQ3FJMFRmUldaSk9aTzhMc0MwdWozb3FZcWR4TmxJVmpQRXR0Nm45dFd0eUM2YzhkRWprQkw5R3BIN2NJNnk2bnFHdUZIZDZYYWMrcEFoVUF6eEtrVFFPRU4wdjlpRTh3Z0I0NzZuVnBNeWtDZ1lCc05rVjFzelZ1a1ZWbnhmZTVZWjdtUkxxcXJpNnBPSlhQWnFNajRSWVNMRlltb2F2Tyt3WjdEejljTUxDb1dYSllRZTlzbHV0aEVvU3Y0NVBVU3NTZTBVNmxMQkx3L1lyMTlQKzk4emJLS2RvVnVpdXZFTXJhRVFyN2NldDVpb3p5Mk12c3hlR2RIQUZUUkhPRENQWCtweFc4MUFpQnhsTVZrRUxESkt6YTRBS0JnR0grdXBMTzgza0JNVUsxQmJnbXdCNkVHeW4vVCtDaVlDd2d2WmNQdGFlYkdhTEZLSmEvVm1jL05iaGdnakNmNW03YmFGSmZOR2NHdzl0SmtyemdVQVArcDJvWUkrWjB5MVp2bTRCSW5FcWdQMklxZDNsa0hRcElHSTNtak5JOUJScWZUUEVZK3J6ZEM0VlNWVndzMDJudEIrSml4aythWFk5QXRCbUowczhIQWhSQXJpNEJzM2cxZUcxWDZGa0xTVkNZenAvUzlRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURZUXk4bmxWNFFmTzNQdFFnbGphRG45eElHVjJFRGM1VTBFRXZZTDRBdm9BY0dCU3VCQkFBS29VUURRZ0FFUVQrYWM2aSt5VHNUajVDMTdOWkM4dkFXbXM4RHl1aHVXWm9sUVRYSVZ4UHh5RE5xRWlSY0R4aHZNd3NoM1JEczB3MmNHTGZKRHJSK3htblFJYk0rZVE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVMSW5hc3pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOakkxV2hjTk16SXdNakF6TVRVeU5qSTFXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0cxYXB6RTNKRFBhMDZydXZHT2M0cmgxVC9qZ0tLYWpkbUVveDFCNVBTMGI2eWs3SHFGNG9CTWRxS081R09pTXNPQzFsdTNLY1RtM2xDVFRsTHN4NWc5R1V4emc1S1pkQ3FJMFRmUldaSk9aTzhMc0MwdWozb3FZcWR4TmxJVmpQRXR0Nm45dFd0eUM2YzhkRWprQkw5R3BIN2NJNnk2bnFHdUZIZDZYYWMrcEFoVUF6eEtrVFFPRU4wdjlpRTh3Z0I0NzZuVnBNeWtDZ1lCc05rVjFzelZ1a1ZWbnhmZTVZWjdtUkxxcXJpNnBPSlhQWnFNajRSWVNMRlltb2F2Tyt3WjdEejljTUxDb1dYSllRZTlzbHV0aEVvU3Y0NVBVU3NTZTBVNmxMQkx3L1lyMTlQKzk4emJLS2RvVnVpdXZFTXJhRVFyN2NldDVpb3p5Mk12c3hlR2RIQUZUUkhPRENQWCtweFc4MUFpQnhsTVZrRUxESkt6YTRBT0JoQUFDZ1lCaC9ycVN6dk41QVRGQ3RRVzRKc0FlaEJzcC8wL2dvbUFzSUwyWEQ3V25teG1peFNpV3YxWm5Qelc0WUlJd24rWnUyMmhTWHpSbkJzUGJTWks4NEZBRC9xZHFHQ1BtZE10V2I1dUFTSnhLb0Q5aUtuZDVaQjBLU0JpTjVvelNQUVVhbjB6eEdQcTgzUXVGVWxWY0xOTnA3UWZpWXNaUG1sMlBRTFFaaWRMUEJ6QUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNJWjBOb2prWHFiUTIyeE01LzNBTWpUaWpCblFJVUdZNzNkVktpblQ3QWtsc25IUEhnT1F6YjZaND0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUUVnYXNDTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlOakkxV2hjTk16SXdNakF6TVRVeU5qSTFXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSQlA1cHpxTDdKT3hPUGtMWHMxa0x5OEJhYXp3UEs2RzVabWlWQk5jaFhFL0hJTTJvU0pGd1BHRzh6Q3lIZEVPelREWndZdDhrT3RIN0dhZEFoc3o1NU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtKT3Jnd2tVYTdHRGMyempkNGFteks3UStPRWRSdW55OFBNaEg5dUNEZmRBbDhyMVFoUzVBMzhvQWdBdmMzelNqWXRYWnM3Rm1GUnYvVnlyQjBuZ0JnNHF5ZWVDaXhsR29oUEQ5RTl0eTQyRGpZK3JPTWdjWmpHa250ZFFHM3FIbmVkelZkRVlHd3VEQVdNcE93dDhySGREbnhHeXBYVXFkelB4cEVWeHJoTktBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVVZWVFc3pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEkyTWpWYUZ3MHpNakF5TURNeE5USTJNalZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTJBTHhwQ2U2MjVaaURGc3pZZ3FxVjVWNFV5enZaN2N2L0VtZ2xSSG1xZ1RWVzhoK3o4RXZYdlU4VEdldVR5TGxPSkZhd0JjYVdMUlBnUUtvSU5Yb3hlQ3J3cE9ZeWZHamJTeXhIQUthVkw0NnExQlltcHliTXdKenRxL3JPK0FUMmpTVjRxY3ppMXNhallmK3BpdjNpeDd1ZStDMlBYWTVWbnA0ZEVqUVZSOEI4NDY1NWtIM2Q0bnVMNzc1UHNnbjdsbnA2dyt4TVVzTGZUTTE1SGR0bEFjby91eThteWU0KzdaTjdTY3R0NkNzK2NhOHlydkVtVW50bzU4MUdQSHJjUUpYQlRNemp0SWJlQXBMVzRnaHNqM0ZIcjBDcDdjb2NheGZrOUo0UVZTZmJUQW9QVFVSTWlSUzlaUUQ5VEdLRTBEdEtTZlp4Rk8xTWZHWjZDNTdRUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUExK0p1Vll3d1puZEhSMzdUN3lKVVBpUmlxSkQ4L2dmdDYrVkJRd1VwNTRsVDVDNXJjWDFLV3RYT1hVWWtEOVA5Ym9mOFlMUjR3cDNGN0hsWlRQY3R0VXFTVlF0dWlDdjAxbUZYbTUvR0hwYUFMMHZjQ2JlU3BGd2QrRGtZWm9DdlpOMjJGTTlIT0ptQ2JHWmtxRk0xYlZkZDg2TlNnbXhTZUNEMUxVQksrNUxMNDlSNnB4UWk2UWRUUGZBYnY5SDA5VFI1ZnZ5bnVLWSs5aGcvUjJJK3M1eHZBUFlXTlRRTU5mcUFpRXIxczVMUFo0RG5NeGQ4MTRhQTRrOG93QmhtdkVMZ1kzVndvcEQwaTZFUWZ4ck1UWThkMDVqczRzVFBEc0tEMWlidVNoemF6WmNLZ0h0Q08vUjNURUVVUHB4WGM2TzlZeWZva3NWemVRZVMvUkJITkE9PQ==
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
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    server udptn udptn
     security protocol dtls
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
    !
    end
    ```
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz58r2-log.run
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

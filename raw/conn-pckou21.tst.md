# Example: ppp with packet over txtls
    
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
    logging file debug ../binTmp/zzz3r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQXFkWHFuazFXV0xNV2NyekdENlFNTkV4b21xZUd5Z0k2MVlJRmNMK0FIWXVobzlGdmFGa1J3RWFkR1o4Q3RnY2lNa3RDMGZBakpmR0VBMGNoYy8rQmxkWXZzNGppVS9ucDV3aHdmMCtIVW0yRmJqdEhmQ2NFUjFiOU1YbXBUS1hYZlQxOXlHMnczb2s2cFYxMStHZE45cjJFYnkrMFBjMzM3RkVJU0ZJT2htRG4zclBySnQvUDlBcERDRjdzN3UwbkpSQTlnY1hLRE1vT2RScFBncmR4ejFmOHBnTnNDQmtDTTNReFF0cU52MUZJSHJmM0szWHpVUVFJdWh0Z2JaY0F3ZDZYaGRvTHZHRHNvOENtaldJZkVjWjhYMzJOdXFpTzVmbFZpc3pmb0VKOVdxa2tRN2VucW1OQXNhQzZ5Z3VqbmlNSWU2WkNJMk0xQ095dWVnK2FWUUlEQVFBQkFvSUJBUUNVREtCcnd1c2tnMmxzTjlkSVJ5OUVYOTlJQWdYa0R6R09jYnVnWDYrbEVkV2tZcXdGZ0srU3QzdTNtLy9YQWp6ekx0eGUra0VKa0pJTjhYSGVGcnUyREhLa3hRelhPNktFL2J4am5zWk9PcDc0U3NDMEg2Y0JNWG1pS1haR0ZNUFdyMFg0OUhZY1ovQXh1MWxkWTJCNVdSZ2JmTEJZdURZSlVWSXhDU2NVUi9YN1NZZkFySWVhY2k1TjVMNUY4WitVVUxWNWI0UCtBaGpDYTd4MHQxSVVFMDZnT1pIdmoyeTdMaDJuWUxaTGlVRWFYNzBEcDY5ZWJ6MElZckIyYkFUUFNOTUtNcjRLRUswMkFYejZ6SjJxbWx2dkFYYmdHRXVHenNJWHBTcFVha01lcU5hdkVOTXJXbVl5VW0wWVEySnRObHlqdjdoOVdkTG5MYnp1R0JiQkFvR0JBTlRxWEFxayt4dXFGazBUZDQyMENLbU03cHA5SlJGd1FHYmtNVW5DY3JzRjdFOUMzTFhYMHM4SG10aHQyZDA5OFRkVWRvakRoUk1QYVNxMlpGZ1lIZnUvTjdqY3pSa3F4OVlBL2JGY0FPbmtCMkI0MERsQ3VUKzFaR3RYaUkwS05xcVV0YmRsYmlZTkRMZFNTanVhelN0Nll0elYvRno1NlVhRWx1Z0FqS0hOQW9HQkFNd3o1U1pJNU1pZWkrR3FrN3phYUc1NXdnRUp0cndDblZ2TWdXUUhpUTRHbVJ5UUx6bVJFUjNXeHhzRjllYVNkWGtWTEoyQkR1NFZpVGJteHlJczQvd1VEc1lnY1l1TDkzWXgySkhiU3RxNE4vRUMvKzd5NFNSZmp5OGdGU0QwMDJqV2pIajU5c3Q0UTV4Z3E2RXU3K29FYnhDZC8rQXNvU2hGeTVTY1dmS3BBb0dCQUs5WmpCQWdLOFp1NEFyK1cxblN5Y2VKa0FDZnpHVitReXY2QnpXdDlQdGVOMjVYckpuK2MxbVo4OGNIUVlSYVBVektQUTBKcVpFM0FlL3hZdGJDbGY3OVRwRHJGK2NBT3JCZkJKQ0xLeDExZFRYWWlmUitwVDU0ejRrdi8vL1lSNGxaREFkTWU5ak9xb2hZTjFhN2VQbXp3N1FJYjl6SzNYbjhQS1E1djVpSkFvR0JBTE9ablJ5OEZnVGhkWFJJbStJSlVycC8rb01CTVNoUlFHZWlDZGVaelJCNSt5YWxKZlFDeEVRelNERmJYN2lvN2d0TjlVeWVXeXhKNHNKWDNhTVFTb0RHZjJ3QTB2MENZT2NpMWpFSzU5NVJFbHEyNGJVZkI2Zi9LQ2N4bDRQQjhVTVBHTU82VGpjTkVxSXlZQ0hHNzVvcXhpaWVYcE9qalNhbnBIT1R4SVRwQW9HQVhucTIrL0dLdGVzWDZlYWVDbmhzendGM08rMlBkV3AzbjJEZjRCRWtpRC9oQkNvam1JZTNSakVvbVdCUmJFejIvbEUrYVdkL3QySlhzTWhRYXFsWk54eXFBRnhMazVVZ3pEeWVNSDI0aDVFS3lSWVBJUmNEb0dPT1ZaVTBFdncydThTTThBOXBsY0hLQTBVTGo2dWN2MVBlU3VkY1FTTUpuVmF6Wm0rRWpFST0=
    !
    crypto dsakey dsa import $v10$TUlJQnZBSUJBQUtCZ1FEVi9LbHNNb0o3d055eURmZVg2TFdBL213VkV1SnNyUmtYeUIvVDB0RDFzYzErd2JCbUphenJSZk5STHZkUHljSHhQUDNnSFBMRlUwNHpEYk5IcW1yNXdwSzE1d1pqcFRmMkNDV0NsM0kzMU1zNklyQjU0U0t4dEFxSlVWQTI3YmdNdDFYTlB4WEFqR3F5MCs4R0FDQ0ZBN04vaHVHd0grUUdKNHJ2MG12clp3SVZBTmVCZERkMXBkL2Y3Y1l3d0x3Y3JzV1o4MzYvQW9HQkFMWCtaWFBYaS8vM002UUtOZ1d4dVRBM0Q5YmwxKzVjTnQ5blJMWjRrSURUZDAzRGVBaHYzeU1ycmZhMUh0VzQxdXR4K2FqRU40T3MvUXdEck83Yi8zT1liV1QyNmYrOWZuVlBnUW1kcXU3UkRERmI2Z3NudGhIRm5MeHdyVjlqK1E4QzhPYVhCL0JzcFpkNEhXbmh3MzVOMWp1Y3dMOEJ3ZXNsbUVyaVVGeFZBb0dCQUluWSt6OE5icGExek8wZ05BanVSQ0UyYkV4RmMyOStacDhuZ29KR09JdWFEbytFREduZ3ovNTRJdzE0Q2VYTkt3OUNqT1czL3pmeGFCVGx2Q0pyTURSUTBubEdtdjQyWHJxK2U4eHNNSDlsS1p0RHoxTHlhbGkveDhrWXkvb3FsVDI5WUF0SjBSdC9uSTNvdjhrNU12c0Y4N2RqZWdNczQ2bzhlR2gwdGprM0FoUWdYMUhZaWR1MENMQ2RoZjZSU3hWRmVWaTQ2QT09
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURvbUUwLzFEeVJCWC9CSHluUTVYbmdTZHRpU0xYbW5CQko5N0ZuYXhnZW9BY0dCU3VCQkFBS29VUURRZ0FFWjFMNmtTSkNCRHp6ZWxhcjBlM2NaOXN6K1hhOE1venFxMHVRQ3JGaWFOV3ZkaHBveXYzc3NIZThmdzhJZ2lnem9zK2FzQ0tBblB4bVhsZW0vNW94QlE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZqQ0NBaEtnQXdJQkFnSUVHYkN5aERBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPREl6V2hjTk16SXdNakF6TVRVeU9ESXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYmd3Z2dFc0JnY3Foa2pPT0FRQk1JSUJId0tCZ1FEVi9LbHNNb0o3d055eURmZVg2TFdBL213VkV1SnNyUmtYeUIvVDB0RDFzYzErd2JCbUphenJSZk5STHZkUHljSHhQUDNnSFBMRlUwNHpEYk5IcW1yNXdwSzE1d1pqcFRmMkNDV0NsM0kzMU1zNklyQjU0U0t4dEFxSlVWQTI3YmdNdDFYTlB4WEFqR3F5MCs4R0FDQ0ZBN04vaHVHd0grUUdKNHJ2MG12clp3SVZBTmVCZERkMXBkL2Y3Y1l3d0x3Y3JzV1o4MzYvQW9HQkFMWCtaWFBYaS8vM002UUtOZ1d4dVRBM0Q5YmwxKzVjTnQ5blJMWjRrSURUZDAzRGVBaHYzeU1ycmZhMUh0VzQxdXR4K2FqRU40T3MvUXdEck83Yi8zT1liV1QyNmYrOWZuVlBnUW1kcXU3UkRERmI2Z3NudGhIRm5MeHdyVjlqK1E4QzhPYVhCL0JzcFpkNEhXbmh3MzVOMWp1Y3dMOEJ3ZXNsbUVyaVVGeFZBNEdGQUFLQmdRQ0oyUHMvRFc2V3RjenRJRFFJN2tRaE5teE1SWE52Zm1hZko0S0NSamlMbWc2UGhBeHA0TS8rZUNNTmVBbmx6U3NQUW96bHQvODM4V2dVNWJ3aWF6QTBVTko1UnByK05sNjZ2bnZNYkRCL1pTbWJRODlTOG1wWXY4ZkpHTXY2S3BVOXZXQUxTZEViZjV5TjZML0pPVEw3QmZPM1kzb0RMT09xUEhob2RMWTVOekFMQmdjcWhrak9PQVFEQlFBRE1RQUFNQzBDRkNUay9HOXY5a21lcFFEOXhLV2ZJbGJIZTdRNkFoVUFneEs3VVMycThidEFOOU9ZWml3Q2ZNSFgzVWc9
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlN6Q0JzS0FEQWdFQ0FnUTk1MjlpTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPREl6V2hjTk16SXdNakF6TVRVeU9ESXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSblV2cVJJa0lFUFBONlZxdlI3ZHhuMnpQNWRyd3lqT3FyUzVBS3NXSm8xYTkyR21qSy9leXdkN3gvRHdpQ0tET2l6NXF3SW9DYy9HWmVWNmIvbWpFRk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1ljQUFEQ0JnZ0lnQVB3YXRtU3NtM2I3b1h6Rk9yM3JFc3FPVjJKa3lldUtweFhSTndvZHpjd0NYZ2pYV1RjZkJPaEgwRTkrWm01Y0Yyb2JjbjR1VUhJMWZINjYvUWdHN0dPVXJCcHFsR3JpQm14cDJhNWk2MFZrN0JOR1FDMFF4eDUxM256Nlc1L0FSQzlreTRtNDQ5cEgyWGQ0dnVWZ3VJZWZYYzNzbmJjTkNkdEtJMCtzZ1dRPQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVSQ0FURnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEk0TWpOYUZ3MHpNakF5TURNeE5USTRNak5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXFkWHFuazFXV0xNV2NyekdENlFNTkV4b21xZUd5Z0k2MVlJRmNMK0FIWXVobzlGdmFGa1J3RWFkR1o4Q3RnY2lNa3RDMGZBakpmR0VBMGNoYy8rQmxkWXZzNGppVS9ucDV3aHdmMCtIVW0yRmJqdEhmQ2NFUjFiOU1YbXBUS1hYZlQxOXlHMnczb2s2cFYxMStHZE45cjJFYnkrMFBjMzM3RkVJU0ZJT2htRG4zclBySnQvUDlBcERDRjdzN3UwbkpSQTlnY1hLRE1vT2RScFBncmR4ejFmOHBnTnNDQmtDTTNReFF0cU52MUZJSHJmM0szWHpVUVFJdWh0Z2JaY0F3ZDZYaGRvTHZHRHNvOENtaldJZkVjWjhYMzJOdXFpTzVmbFZpc3pmb0VKOVdxa2tRN2VucW1OQXNhQzZ5Z3VqbmlNSWU2WkNJMk0xQ095dWVnK2FWUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFqSStqTU5hdDIvbzhaL204R0JXZHdoSElWZE9wRzdyeVM0cEp3Y1NWM1g5NjIydXZVTmIyellkekFWcmJYOFZZNXJ5N29RdE1VWUcyR05EVUZvRXdOVnNmZkNQdWNzRzFaRXlTazNydWhQam93ODE4Q2lIWkFOeGdZNnpNZGZpbGJhNGF2U1BxdS9KYlpXeVJiWThVTjNGQ1p0dmpoZTVHc1lSTnJvbi9ybnlidDZSYU1qSFUwVVVaaStaRURxWnJvelNIYmw5VFA2ZzVWM3YwOGlvUzZoTEZXTEc5TzEzTy9FT0RXdzV0aDQ3enJqbjZDN1BNMUpBKzRlYUtWOWt5K1grTUtLSDFlRExrcXZVdHEwKzNIMGt1YnUxUEdWVmoyS2hjbU45ajAxZWNPcHlJVFRKeW5ja2lveGxDTURibE5JSHNDRzVFbnlVY2RaNDBPSlhQQUE9PQ==
    !
    ipv4 pool p4 2.2.2.1 0.0.0.1 254
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
     ipv4 address 4.4.4.4 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
     no description
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 2.2.2.0
     vrf forwarding v1
     ipv4 address 2.2.2.0 255.255.255.255
     ipv4 pool p4
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
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
    server pckotxt pou
     security protocol tls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     clone dialer1
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
    logging file debug ../binTmp/zzz3r2-log.run
    !
    prefix-list p1
     sequence 10 permit 0.0.0.0/0 ge 0 le 0
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     no description
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 0.0.0.0
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     security tls
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target 1.1.1.1
     vcid 2554
     protocol pckotxt
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

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
    logging file debug ../binTmp/zzz91r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQWxod3gvczl5ZTEwMEMrUkRBOVlaRTJYckVRK0lxTmYrYVlSTEtzODNyc3NjYi9seTdvTldHRjJDTE1VRDQwclNoYWthMnVpNWZDUUtKQW8ycG5VNWM5aUJOdTIyY2hFZFdyRW1LMUt2Z2M4OHBxbXhVakUrWTZDVDFVcnF5ZGR2UlkxMklxMXRiN2JMZG1DeEl4NEpqejZaZE5FcXBsNmsxODRJZ3RRK0wzNFEwcFdnM05waTlTQW9HcHlOdVNYT05xR1FPZXI1Z01jOFdva0p4M2QyUVRwNkg3SGFUVWVBdnJBUmZmaml1OCtvMS9md1JjNmJpYng5SGwvM2tkVzNpcjVpUU13S3BBSFd4WEVLQzBUeDdqakdQTlU3QkpUUTEwaG5sZlgvRXNZY2tqNGN6V0phdmtzcmFidSt1NjZyWGJTd0ZMMSt4RGpKOWZEOWN0VERlUUlEQVFBQkFvSUJBR0JtRlBsRmNZaWx6ekcvMGdXWnJacldmY0lFRHNnWGhjdHZhUEpDQnNsYXFKV0VSWG5Fb0RxZmVtU1QxUzVYTTZFZ2V4MlFET1liSXVRSUp4WjQrMzlZejRwZDJDZWl0QTQwNjRVdzRZTGtlbGV4YkMyVGNEUjh2OU5lL0M3SkNpMUpiazlRdnBIYWV3azNpU283TlBwbndoYlI2S2pVNk5tcDk2OUU2L2FFNmx5VTd5Z0hKZFpiMGRLSTA0NVp2MXFJVlR0UUViamdTVmh3RFh0Y1BGL3VFNzdDZEVJNmlJQUNBUnpISEQ1UnRRWXJ2SFZUN2VWdER4NVplM0xjNWN0ekxkZEJVcWlvQldLejB2R3BMckFMYkV3WjArQ0JQVmZTUHhzMWlhaUc1WEQyWWQwUExMOUFER1FnQVUrd0NPVktFN3lqeW1ONnZ1T2NkMDNpUzRFQ2dZRUEzUzd5TXlWQ2FtWUthUkJrN05aL0FnWWVwdVRhOUx3cWhndXlicFVDMXJkTGhibndUZzMvbU1jTk9HN1ZQbzV6RXRnTXc2SnRkK0NsZEFTakVoUTJ5eTBPZkl1aWZtam05NUFCelFUdG53RExMcnFyS01qRUJTVzZvRUMrZjJrbU1KK1ZUcjRyNm52Nm5YR3c3a0tSVnFnb3B2K0hwUU5zdmprKysyTnpsOUVDZ1lFQXJiMHpzUzRRTnAzejk5KzU0enBGSmhPMzAyVDBaYXU5ZlhrMUlZUjV2eE9HcWVxa2FYRzdSdlRqeVJBbzVZYkZTbGFuQnRpc1ZOM3NqcUxrUWloWW4wdjhuYWY2NytJRHR3MkdhbFprMlgrVXYvRlJWYlRTcWZvbGdyQUNKNTJ6Q0pSbzlONjcyYVo4RzhLZlFpdnhLVXVmeGdMbC9kREFRV1ZkWCs1cUF5a0NnWUVBMFcyd095bGVkNnhpMHhTSTI1QkY5ajZoSzFtcTBPeVNQeFk0UDJpc3BXNHMvbFFPNjNscHVObFE5VXhNY2MwanZJWUJvQVBlTHhIdzE2ZkVXRXYzamUzOXQ0UG51bFhOekQ3NDFZMkRDWGtRNmhBcUhKWHN0UXNDYU5hbENiTWdUQTN1cS81NVNxOVZuMXFWTXlTb3hTcTRRMWZVc2pSSjlOdnpmTWl3SE9FQ2dZQWNCQTU1Mjd1eGt2YnNXWjlZRE9WcHBuUldHa2x1dTZycXVNamdoc1E3RTZMN2MyTGZ2Zjg5Q2ZCUlU5SEVjVjhQQmJvWldJY3hpRGZGS0c4Mlc5c3VsTW8vZ2Y3cy83MHBuM3kxV1FrYUtZQ0xFeGJTZ3o0Vk9za2hzZEFuSXo3amUwc1JjWGxKTjVkN3duNTc1U29XUnFPVkFwS2p3eTI5WGVNWXZSRkxRUUtCZ1FEU1hXcWVVaEJsRmlaa1hja3N5VkdtWC9NQTJhL1pWUjFsWnlYYWZuQkhHN09SWVBQempyUkUxaHVrWW9rUmFaVjBZek9iVC9xVVYzSXc0eGdlWTRRRmc3VEduUmVhYXdPaGFyaEJNZFFoVG9CcEpGdi9kNGlRN3d4cEhyMFRzdFBJWWhnS2FUbzF4dGp4Zmg4SDh0c1BETFhLYUtuU01ZV2QzYWZjZXVQMEtBPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0NzQk5hSXg4S1BvYTFiN25WKy9zYXRBVEh5OW1lL2FHWjZtMGRQd01vL244cEJaK2pxTjFvTi9tVkxLL0pSK0JwK2c3Z1FJdW9mWUpyVFl1UlF1cEdFazN1Z1JrUlg0WTlxd3ZBTFlVK0tkVGluZjBSbVBuQTJvWEFNN2F3MW45RFU1R1d6WXZIU09hNFlkdS9MeU9KbDFUdGR4a0tmRFBuK3JwRWc3dGlnSkFoVUEybEEwRG5pQWxIaTYrYnVWemY3OFY4Q0l6YWtDZ1lBZzlPY3RremkvbjJaQXBXNG1PbFNZRWtuUG1pZmt0WEhHZHBnRk5kUGlRRk56OE00VFFtMFJWUFp4eC9UZEU4Z2c1RkpUNjFDK1NjWktDUFZrWk1Ud1l3ZTdnWlZVcWVNMTFzdm9YSUxpV05ZV0VIZnBDRE9CWjNQZ3JXUno2d0ZxZTJ6c0o3YzJOQ0JEbi9ZMkQzZmdYTTNWdTQ3MEVqbGNiT2p0N1FOTXRRS0JnQjk1N2FoUFprR2JkeUljYmxDZUZQeldFSnRXTTF1S1h3TjJmRWFPTTdvOUdIV2EzdkZSaWZvTDI1OUVUb0Y4YzJUTHUwY2Zwak91dG16Ym1Uc3dWK0ZKcWQwcVVFZ1p2VXJzcU1WNXV0SzNTMFF5NGJ0NnoxSStVaytPWU1VOXgrMlhjajRyMHh0YUUrcFpyN0thbWV2UGNPamJCNThubzRsK2dJaEErM05CQWhVQXlzWU5BWHRqQnNtaENuaVV6OUo1OVZ5NUl3bz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUR5ZDM2dHp6L2lzZXZodVhOUXQxU0F1dzVXcWc3dCt3MVNCT3FEMVZLNm9BY0dCU3VCQkFBS29VUURRZ0FFbkVkQnV4dTJ1ekFWZkxxTFJGRk94aWRYak1FMHRGc3dQWUE0OVZpNjNNUzdERVZIeUliZjZWdmhsWGxHNS9hOUVhNmU4WWxHdkE1VnV6MjJseVhHSFE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBZytnQXdJQkFnSUVLdk9NV1RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOekExV2hjTk16SXdNekEzTWpBME56QTFXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NzQk5hSXg4S1BvYTFiN25WKy9zYXRBVEh5OW1lL2FHWjZtMGRQd01vL244cEJaK2pxTjFvTi9tVkxLL0pSK0JwK2c3Z1FJdW9mWUpyVFl1UlF1cEdFazN1Z1JrUlg0WTlxd3ZBTFlVK0tkVGluZjBSbVBuQTJvWEFNN2F3MW45RFU1R1d6WXZIU09hNFlkdS9MeU9KbDFUdGR4a0tmRFBuK3JwRWc3dGlnSkFoVUEybEEwRG5pQWxIaTYrYnVWemY3OFY4Q0l6YWtDZ1lBZzlPY3RremkvbjJaQXBXNG1PbFNZRWtuUG1pZmt0WEhHZHBnRk5kUGlRRk56OE00VFFtMFJWUFp4eC9UZEU4Z2c1RkpUNjFDK1NjWktDUFZrWk1Ud1l3ZTdnWlZVcWVNMTFzdm9YSUxpV05ZV0VIZnBDRE9CWjNQZ3JXUno2d0ZxZTJ6c0o3YzJOQ0JEbi9ZMkQzZmdYTTNWdTQ3MEVqbGNiT2p0N1FOTXRRT0JoQUFDZ1lBZmVlMm9UMlpCbTNjaUhHNVFuaFQ4MWhDYlZqTmJpbDhEZG54R2pqTzZQUmgxbXQ3eFVZbjZDOXVmUkU2QmZITmt5N3RISDZZenJyWnMyNWs3TUZmaFNhbmRLbEJJR2IxSzdLakZlYnJTdDB0RU11RzdlczlTUGxKUGptREZQY2Z0bDNJK0s5TWJXaFBxV2EreW1wbnJ6M0RvMndlZko2T0pmb0NJUVB0elFUQUxCZ2NxaGtqT09BUURCUUFETWdBQU1DNENGUURSOXdOd0FFWXdhRjdTTXVPTEFqeTFmeWw1QlFJVkFOQlNBSjF4amJxTVFuUk9oM3duQUpyYTdnRmc=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUVk5bnVITUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOekExV2hjTk16SXdNekEzTWpBME56QTFXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTY1IwRzdHN2E3TUJWOHVvdEVVVTdHSjFlTXdUUzBXekE5Z0RqMVdMcmN4THNNUlVmSWh0L3BXK0dWZVVibjlyMFJycDd4aVVhOERsVzdQYmFYSmNZZE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnT05ZUXlYZnM3d1M2ZTdUZVd3Umd0bi9aam1xWFg2QncydFhYb3p6anBIQUNYd0YrTjFnWTA2c0hnVFE4UkV4OUdZczV5a1lRTnp0U3gvT094VGZQa1poM2xOZGJlYVM0eXhLRkx4TnVHbHZOMDFZNkNzcVYyRVVyTGdQeExxTXN5c0tqWENyajB0KzZ3SHoyUzkrQ0NWaTNpYlZRdXRqYVBKNGhOT05KaC9pNQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVJNHB4NmpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFEzTURWYUZ3MHpNakF6TURjeU1EUTNNRFZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWxod3gvczl5ZTEwMEMrUkRBOVlaRTJYckVRK0lxTmYrYVlSTEtzODNyc3NjYi9seTdvTldHRjJDTE1VRDQwclNoYWthMnVpNWZDUUtKQW8ycG5VNWM5aUJOdTIyY2hFZFdyRW1LMUt2Z2M4OHBxbXhVakUrWTZDVDFVcnF5ZGR2UlkxMklxMXRiN2JMZG1DeEl4NEpqejZaZE5FcXBsNmsxODRJZ3RRK0wzNFEwcFdnM05waTlTQW9HcHlOdVNYT05xR1FPZXI1Z01jOFdva0p4M2QyUVRwNkg3SGFUVWVBdnJBUmZmaml1OCtvMS9md1JjNmJpYng5SGwvM2tkVzNpcjVpUU13S3BBSFd4WEVLQzBUeDdqakdQTlU3QkpUUTEwaG5sZlgvRXNZY2tqNGN6V0phdmtzcmFidSt1NjZyWGJTd0ZMMSt4RGpKOWZEOWN0VERlUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQW5nUGZLMzd2NFBFT2hKelZ1eHcrMmVFZHRabnZ2QUM3a2xHU1BPeEh4eHlxQXdKeWJzVlh1OUZEQ3llZlcrODBESWhmZUVrbUMxaHAzYnI0K05nWUVkaUZVT004ZWRkWXM4Ky9CUHQrU3AvcjhYTmh1bXAwNVlvRzFFcXEybjZ5RW1PK3pyT2RSY3dHa2Vlb0pPNTNRZCtJSWl3TDZPd3c4blAzRnZSRUFtc0JLNlpWWG11c05VblVyc1FFcVB3TWd4U29sNUR2L3hFK0Rlb25Vc20zd2RON0pPSnpGQmpUODdDb3dYSEVOV0FsYlRiLzNYQlpKTk51Q3VtRVk5dFhUSS9Eb2JuR1FwMm9RbjlOMGJpVFZmcVZlT2R1a1pDMXprMnUzdkRHN2F1WUtYaDU5QnFqMWdTS1dheFM4Zms2RHkzNUNlRXpFaXVrL1puMlRJd3ZU
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
    logging file debug ../binTmp/zzz91r2-log.run
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

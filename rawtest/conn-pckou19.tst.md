# Example: ppp with packet over tls
    
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
    crypto rsakey rsa import $v10$TUlJRW9BSUJBQUtDQVFFQXVMd3diNU05d0ljTWNLNUpHcjlGUDJTdEZ4U3pnQmx2N01jWmJSWFUzSmg1MkJjVE1rQ2puakdJdkUydWVzM0Fockh2Mnp1SWhudEtoUlI1a0NxMU9wd0ExdHdBWUhxQkVYbnZwM2VvM1ZDT1djZEduenIxcmZkWWhmMmdPbmhabGhkdllVcFFRdFg3WkxZVDhQS0kyLzhycEU3NG5oMDJkYktHbkU1MmR0ZUwyZzV5NHFOZjFxOUl6VVhLQmt6SXg5eGVnNzhEOEpYQVZmcmV2RFBBS2tKL2hVM0d6a2tDTG5xYVFZd3dObnZhVG1Ma2FpSXlxeFpkSnN5Z1VEaDJiZ1E5akF3bzQ5VmMveVE5ZXg4S1ZhWjBtNzkyVzlkK20wWTV0VDQ0cDlSRDNTT2c4ZUhXSm9OTXhpOXVFbkEzZGJOTTM2REZoblRqd3FPVnNSK2xkUUlEQVFBQkFvSUJBQ2VaTDBpN1p5RTkwWXpWenhYTXFpdE1pVTNKUWpEVFF3cWVJdlVmR09Hd1RXM2toRmpoUWpGR3JPaXdQaFpVeEZBYkZDOEtNOW1mMC9seXlodjlDNXZrbE1sNW54c1BKMXQzcDhkZC92UnhzQkhPaFhUY1RvMWIxNzNnLzllSXRLdFhtcWhnSlpRdUNoVXNjbG5UbzBLRkQvWElkOEpzd0orNkJPQzhjT2hJTHBVNHFUbHBsN0JUSTU4VkcxdDZHSElDSy9DS2tuaE5hc01KODlRSFlSMGZhNkhCTW9rR01oVithbkpvYWJ6aFdScU5qVWR1VDliNFdjOW5aRHN5S2FtVjhLMC9ta0hqTUZWbStPdDNKMHdRaVVJK2k5bkR1Q2RJNzVjVGVjTXI2VmtveVZlbnRIcng1L2dQdnRSbkM2bFNOVElnSjVmOVRFRFdSajBuQUFFQ2dZRUEzRGdIUllkeTB0MXpWWWM1aWtsbG1UY1gyU1V0V3YrUzVqd1FmOXVhajd5UmlqT2VnNVVqbmdlWENFb2M0Qmt0UURkUzNIbSs5dFQ4NEpnS0NRbzVkWDlha1V3clkrWjFoZ1BVbEQ0SkJmandnLzhlbTlIeDU2dkdRQ3dQWXhRczVHdkNEcDlxeXJlVld4Um1sYjk3WE5wcC9Ib2NzTEVUdWlCeGx3bkY4QUVDZ1lFQTFzQTRNSWFWSDNRVWhDVHc4VXRoM2JSd0FLZWloQ2Fwa3oyeFk1UkxQdXpPaWYvUGpJTldkdVFjSXR6WmcrcjBaYTZQQTNtQnQxM1NudEppQTdEaTdKbUg5SUJQYmhML1NmNzM3YmFyaXdKNDU0VytWazRoNlBWUHZYak1qeS9WTm9mTEV6QlZBRTRvTkpNSGFFanZtcjdsbjZBR1BLRmtBRU91RTByNDlYVUNmMEZnWU1oRGJkTXI2eEY1RTV2NkxpOU9LOFpMUXl2QXM5dWwrVC83OGVhNkZIcnkyQnc0S2xxLzVoYVA2Z0tkZHRHWm12L1pKTmdpWXZCS01yQjhXSktKUEZubVF2dGxiMzVacE1KZHFGQWRsMG1ZYzMzTzFnSHcvT29RS29FL2ZCUlQ2VWh1QzBZak9qUFAycVNhTkFWYzBob2lKbUpPTDQwU0ZLYkNRQUVDZ1lCbEhrK1c4ZGdIM25YR24wcGdvL2txRnN0aVU0emZvd0RZRndXTytRWFJWRm9RZXNhMHlDY1BobXVGTXU2dEFoWWdSdWlLWDAxb0ZTS1dyRU9BcjJxNnM3Ump1WU10Tm43RXplemFIdGg1ZFNtUEF0ZlQ5YWhiOUI2ZS9lRjhUcTZicGFkR21zeDdmMUhKSjY0bU9hbXcrTkJRc0Y0ZmNITVErTTFmd2o2bC9RS0JnQTdOTTRjT2tENGE2VWVUUlovTUMwTnYvdnNFT3BINHpObVN5eXRobURuZ2dCemNnZ0liODBNYUhwYVZiUDRMeW5YbERIWEdINFZ4cWEweUVNN3k5dTZxTFV1cVlxck4vTVRteExqTjdOakdIa2kyaUp3cWJmUDV3emZYamcxSTFGam8wQlVrb3BPemNSNlBxalBSQ1k5b1FHZVh6d1lRSDREM1k5WWJQam5j
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0IwbU11a2VGb2RjVlk0ODdxQ1VSMU9QdW5WRTk5MGduZy9nSFdEY1Y4VWVIUW9nb29PRW9JMktZL00yaW04SE1UeGhJUmN0RnFEbzZrTjU0NVFmNEREN1VrREN4dkpnTDJXWC9lOTVpNXkwbThjWWdaMzFWNWF2b0g2SEZLenM2Z0RGdklaTWJKZFh1cmRpTWQ2V3l5UFQ4TkhVN09RdklmOFJHTnM2TGI5TkFoVUFqYlBKZHRjcThuWGxma0RlMlkvZ0hTWTBvamtDZ1lBV0xvWGIyWDMxTXo4MllNcXAvc1h5R0tuSFRKdFF3NGNrYVVuMmR0VnlSMHFHejFvakpoRDg2SHAxaWJ3RXErTHBSSTduZis3WTRxUzdtajBONFJiaWNqcDlqc2pDMEEwOVBiZWNncDVyYXM5T216NmtjcGVWNjlGcGV4d1h6OVlIZVpBTjZCOStJRTNrd21nZXhjZlRXV2dEbU5uS2J6MTBCOFZkTVgyVTJBS0JnQVdLYXJiN0x3M2MybnFPODlCOXB4eDh4TzVSK2JXSWRHWkFmY1FLMEFaQ1dEOFhzZW43cGZ1V296TE1jb3ZOeTc0eE8vSVJ4N2Fsc29SUUc4bnNac296ZkQvaDEzck1HODlYLzB1NzRMZllGeWQ3WWJ0RFdCMDJNSm0vbWpOSWdyYjdtZUhjT3ZYTlcwNlRmS2RwTm1DR3lNVzdoelFGQWJ6ZWhnZ1hHNTQ4QWhSVlVjOFF3MFZJNWpjelBKRVpBbThCY3JacGh3PT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIM1JKVE1EWitmSFJxZXFLZHA4eTFMT2luS3hab3RiRDJYN2djdnRrdEpDZ0J3WUZLNEVFQUFxaFJBTkNBQVJ3UmdkMHNUazY1QzZnYTh5TmN4ckJ2QjZvOVJMUkk4eFNFVmJTcEVlZ2NQMDdYZmF0c29NRVBsWFpLdmMyaWxoY0xGM0ZKOVlTVWpaQVZiczlCTGtS
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVjaU1WN3pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pOelV5V2hjTk16RXhNakk0TVRrek56VXlXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0IwbU11a2VGb2RjVlk0ODdxQ1VSMU9QdW5WRTk5MGduZy9nSFdEY1Y4VWVIUW9nb29PRW9JMktZL00yaW04SE1UeGhJUmN0RnFEbzZrTjU0NVFmNEREN1VrREN4dkpnTDJXWC9lOTVpNXkwbThjWWdaMzFWNWF2b0g2SEZLenM2Z0RGdklaTWJKZFh1cmRpTWQ2V3l5UFQ4TkhVN09RdklmOFJHTnM2TGI5TkFoVUFqYlBKZHRjcThuWGxma0RlMlkvZ0hTWTBvamtDZ1lBV0xvWGIyWDMxTXo4MllNcXAvc1h5R0tuSFRKdFF3NGNrYVVuMmR0VnlSMHFHejFvakpoRDg2SHAxaWJ3RXErTHBSSTduZis3WTRxUzdtajBONFJiaWNqcDlqc2pDMEEwOVBiZWNncDVyYXM5T216NmtjcGVWNjlGcGV4d1h6OVlIZVpBTjZCOStJRTNrd21nZXhjZlRXV2dEbU5uS2J6MTBCOFZkTVgyVTJBT0JoQUFDZ1lBRmltcTIreThOM05wNmp2UFFmYWNjZk1UdVVmbTFpSFJtUUgzRUN0QUdRbGcvRjdIcCs2WDdscU15ekhLTHpjdStNVHZ5RWNlMnBiS0VVQnZKN0diS00zdy80ZGQ2ekJ2UFYvOUx1K0MzMkJjbmUyRzdRMWdkTmpDWnY1b3pTSUsyKzVuaDNEcjF6VnRPazN5bmFUWmdoc2pGdTRjMEJRRzgzb1lJRnh1ZVBEQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNHOXJPa0JTdFZ1REtLazA5ZEc3QSs0UnEzQVFJVU5pUGJMMUxXNXdYRDlGa1lpYkJpWDJyVXUzOD0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUlBvYWF0TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pOelV5V2hjTk16RXhNakk0TVRrek56VXlXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSd1JnZDBzVGs2NUM2Z2E4eU5jeHJCdkI2bzlSTFJJOHhTRVZiU3BFZWdjUDA3WGZhdHNvTUVQbFhaS3ZjMmlsaGNMRjNGSjlZU1VqWkFWYnM5QkxrUk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtkYUN5cHpuSi94VVJlTDlsNjF1Rk8va3dvaGpBQWRGRU1lY0dxTUFXd3lBbDhRS0xjM2lsUVZSeDFVWStoOEF5RkowZDl2MXZVUWlKcHRTQ0lDd045dE1RaVA3REpJbnFMTk4yakVPSGV3Y1VkSnJiSUhmT2x3Q0w2NnB6M0R4T3k4Q2grRlVxYjh0elduM0FqaXkwOE5tR2lka3gxWmxPUTFiNHc4d0J0bkNnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVSQ1JERnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXhPVE0zTlRKYUZ3MHpNVEV5TWpneE9UTTNOVEphTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXVMd3diNU05d0ljTWNLNUpHcjlGUDJTdEZ4U3pnQmx2N01jWmJSWFUzSmg1MkJjVE1rQ2puakdJdkUydWVzM0Fockh2Mnp1SWhudEtoUlI1a0NxMU9wd0ExdHdBWUhxQkVYbnZwM2VvM1ZDT1djZEduenIxcmZkWWhmMmdPbmhabGhkdllVcFFRdFg3WkxZVDhQS0kyLzhycEU3NG5oMDJkYktHbkU1MmR0ZUwyZzV5NHFOZjFxOUl6VVhLQmt6SXg5eGVnNzhEOEpYQVZmcmV2RFBBS2tKL2hVM0d6a2tDTG5xYVFZd3dObnZhVG1Ma2FpSXlxeFpkSnN5Z1VEaDJiZ1E5akF3bzQ5VmMveVE5ZXg4S1ZhWjBtNzkyVzlkK20wWTV0VDQ0cDlSRDNTT2c4ZUhXSm9OTXhpOXVFbkEzZGJOTTM2REZoblRqd3FPVnNSK2xkUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQWtvcjJKNnc4em90WEFUMHo5cy9ESUlpSUVqdlBIaVJRVlR2Y2djNmJrUzNod3U3SVVJS3dZZTlaYWI2SURNblZVSzJJcEFLU1ExaDB4VEpHN2JKdVZ3dU0ydVJmNC84enZGR25EQnNlS0NDbTV0dS91Rm51NHlmdjZ3WWpLQ0RkYnhBcERpTGh2Y1hHdW1rU2tyc1lIeHlPOHJnYUkvNWtVenMwam5QaExGZlBOTkFhNlFzR1kxTE1uZGJUQmJ3eDB6N2ZRalN0ZWwxc2tPYVNzTDdJSUtoa254bkIvZEhFN1JjK1VLemJYWUpmbUpZY1ZXNFdMajUwNVB5ZUptZjl6RHNIaHZOdjl5Nm1TM0lrdEFqMDBDN0ZqT0dQYTRJbGNuZVM5N05vN0FDbGxab0hPTTgvazg2Ti9VUTZyV2hlOUhDVVh1Z1lXbnJXdnl6SWd3U3p6
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
    server pckotcp pou
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
    logging file debug ../binTmp/zzz1r2-log.run
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
     protocol pckotcp
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

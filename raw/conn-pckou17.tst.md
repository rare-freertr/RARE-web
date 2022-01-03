# Example: ppp with packet over dtls
    
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
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXozSkZNekp0QnprYmpFVUQrS1dMQnROL2FOYUI2bjVHQnErVUtpaHhtSHJ2L0RmZEtYWmVPZHQ1SDNHeUdLcGFPa081R245Nk9UMFRzc2trUUpMa1huYWQyKzhlK2hkbjF3VmJ1dVNiRG8wZE5BRC82K3ZaemVLWkErZStVcGhSMHYxTnBnUk1HRVBWeTgraDdVU3ZPVXNQczI0N1dtZEp3d1o4Zi9TSGpaVzlNU3I3ZlZMdmM0MFV0eU1DT0ZkcFhqbTJ3Vi9jSFNyWVZuamN6ZE1wY3EvNjFsVE4vUmxuYXNiOTFiWGF6ZkIvU292dkRmVStORExrZENSSG5mQmZKbVphQnhyMEx3RVU5bzYrRnZZd0JPSGJHT3UvdFUydEd3eTdPZTZZYVgydTVidlhMMlVvN0p0dk1xeEQ4UUJiWjNNQUIyaGlDaWJLdGtvelFzT1JOUUlEQVFBQkFvSUJBSG9GT0FrT1R5MWhmUCs4Rk1McjlPUDJBY3FUNm1VWkUyMlpWMmlZMDRDaVI0a3UvdXNGa2hVc01JbTdZY3U2WUVwSFRaajFoTm9vUCs3NCsxYjBVRm4wSVpTZGliWUhrRy9jMmdFTHVOME5TakV0cVZ1SEpsMUJQVW9ieFVwbUNETTRCYlZ5YjZRU09xNmdtaG1yUGZwUVdaTHNjd01SSUVVVUNxVmxHMXErdXFUbHVtT1BJeXhvRk9ZemN6ZDZjSmZXbitub3R1ZDY2amZJWGtNVGs1emJRVjg0Z3VEeURQY0ZJRkxpeGhSVVhEVVFnZTNiTkxKWVZnQ1Q5V29xUUVkMlkwY2k2aXZGYUE2dE5xRTExdWpYaUxqeGQ4ZVkrL2dZK1Nuek0zbzQydEJGQ24zZU84VDZpcFd0M3JhOWJyZUZqU2t4MlF4TmdOU3FBejZGOG4wQ2dZRUE5UllEc050WjBQdi96TXRVSVRoYTFHTXU0eXprS0VOSUM2OGtITHdCK2VmSjZRenBUMUUwVXF5NElIUHBiQWV2d090NnVqbEQ3eGRnWVR2SlNnQ3h4RWFkRjdJa0Q4WWNoeFo3cmNJZk5Rb05JcDg4UHh5dDlsbnVMdjVlZG1QNmowYnJ5K2wrNVcwWkZ1Q25jcHBhajJXN3gzbDNzeGNJaW04dkNBTlFUVk1DZ1lFQTJLOHAwZDlwUmJSWFNkVHlwTjM1YURuTUhqMTJuZW81UjNxais0ZDlBRWgyeXdaZFBITzRUd1hBcW5rS2d4YVhjWks4UEhJTjhITVdYZklDTnhjajlYQWcyUDlES1RFTllqS1NrdHIrLzJYclM4RUhCLzJLWVNwNlFjRm9iSk42cC9od2I4VTJ4aEE1dmpKckhJeWFuZ01ieDQzNjNuSERXWDM4MEdJdVRsY0NnWUJSRExPeHhBaUMxU04xN1hQbi9JUUZJcnU1d3ZtODJ1c3plZnIrU2FwNW80NmhOSFRmbHlJdmlSRG5JbzM1L056QmR0NUNRWGZXMUtzNTNKU25sVzAwVkluVThVTjl0KzF0T3lFeGlEWGJ5M1Ftay9SUGhzTjg2YWFjQWVEcFZBempYdmZSbW1rdHBCT2MvalJCOFF1cnlsLzhDbzVzT2x6SHN4Y2hsajd6SXdLQmdRQ3pXeklyaFZqWEdMS1Q2NDg1Um4rV2RSanZBd00zTFZSaVJUS05GaFl5OE1oYnZ4WFgzeFYxVzVhaHhQVWRrc3FpZU1vVTRuZUZTMDM5VHova0orUmMyWVptOTh1NHdlQ0pJc0ZPaTdVODVEa0NpSEZ3Zkw1Wk5WYmpMTnRwM0IxUUFnWFhqbytMSEkwZlVRNTJJREF2a1BVaWxmUk13aS9uMkxBMk1MNlJtd0tCZ0dTWHFoU0hMdnNjeXdmSXlROU9NS0tqeEUxL0h5ZFEwRE94WkdjLzFxRmlXVE5RelJ0SktjVzdoNjIrTEV6V043UmM4TmxzQ253cTFoRGlUaElwZFNkQzhoRzhmSzluT2p5MmhmbEdTeXpnakFGTkNIRzJHM2dHY2drd2IyNndkRjN2RmVFOHcrb1B6T2hkMkQ4Mlo3eStZcTBDblMwWkZ5amNvclJTSmdVLw==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0FVNWF5WEdieW1kcVpsQTRZWldlT1llRlU2aHZycVppY0NBWkFYWHNrcElrZmJkUE52bjJLUFpqL1BCYkxBcE8wdzN4a1hTcFZ1OXdHcTNZbUlLSEFtVUsrN2JUVVNkdVBaOFVTYUxFa0x2M0Uwc0ttcFU3a1BXdGRwbkpSbGV4WitzTVR2RnErZnJYdSszbGVGcGxFODBoT3hXd2VlVnNMakt2M2VDNEhRTkFoVUFuaERUU3FiVEVaa2ZEMDNReGo0cFU2bkZHc0VDZ1lBQjFaWmFYNXV2bEYrYWREakZRTDdzSnNVSDMzOVBYNnVYUnNnbk80aDF2SXdHT2wwZnpJNGIvTjFUWnVyUkxMSll2Mi9ZOHdGY2R5UkpTaHRCemc2Y01PT1FZaHM1ZWM2OHZ0SjlkKzVZdkIzR1VlQkhMODBoRGRKMnhmTkd2T2cvMG9DNExPUURPR1dKczlmTWhuR3E0cWd2M3ZZWTNMb3FMdVFzKzNjVFJnS0JnQU1hV05waVRpZW4rSDJLRVBORkJENXQwaWIyd1drVHd1ZTVGb0V4K0xramxQYjVkaVF3UzZSNnpwWEhhOXBINWJqM2ZQRjhtb0tPS3VURGpQR3drRSt3SVFFSzJHVnJ6THhqaEQ0R0IxVjNraVRmK2ZZcGYySlNYdEJBSWdoa3p6MWdpVHN3WUVUNGR2cnp1aGc4eXcyL0EvbytzSHBEVmtLYmV5Mm5QempUQWhScy9peGgreENoK1RPQnl6QXFlN08xUXZiWGJRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURFNzNTSTVaNVQwdWhXUEU0UitVRmUzZEM0ZHJvMERuSHFIckxKS0dQbW9BY0dCU3VCQkFBS29VUURRZ0FFWHRCamU5aTN0YkovL2VKdFZyaFdXUHFmUHR0bFA2V2l6T0xDbVpZTVVFSFNhZzVraitXd28xTzlTZnc4NEo2amFSTGUyRFJuOUdGck5WOTFLQk02MGc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVjaWF1QnpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pOek13V2hjTk16RXhNakk0TVRrek56TXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0FVNWF5WEdieW1kcVpsQTRZWldlT1llRlU2aHZycVppY0NBWkFYWHNrcElrZmJkUE52bjJLUFpqL1BCYkxBcE8wdzN4a1hTcFZ1OXdHcTNZbUlLSEFtVUsrN2JUVVNkdVBaOFVTYUxFa0x2M0Uwc0ttcFU3a1BXdGRwbkpSbGV4WitzTVR2RnErZnJYdSszbGVGcGxFODBoT3hXd2VlVnNMakt2M2VDNEhRTkFoVUFuaERUU3FiVEVaa2ZEMDNReGo0cFU2bkZHc0VDZ1lBQjFaWmFYNXV2bEYrYWREakZRTDdzSnNVSDMzOVBYNnVYUnNnbk80aDF2SXdHT2wwZnpJNGIvTjFUWnVyUkxMSll2Mi9ZOHdGY2R5UkpTaHRCemc2Y01PT1FZaHM1ZWM2OHZ0SjlkKzVZdkIzR1VlQkhMODBoRGRKMnhmTkd2T2cvMG9DNExPUURPR1dKczlmTWhuR3E0cWd2M3ZZWTNMb3FMdVFzKzNjVFJnT0JoQUFDZ1lBREdsamFZazRucC9oOWloRHpSUVErYmRJbTlzRnBFOExudVJhQk1maTVJNVQyK1hZa01FdWtlczZWeDJ2YVIrVzQ5M3p4ZkpxQ2ppcmt3NHp4c0pCUHNDRUJDdGhsYTh5OFk0UStCZ2RWZDVJazMvbjJLWDlpVWw3UVFDSUlaTTg5WUlrN01HQkUrSGI2ODdvWVBNc052d1A2UHJCNlExWkNtM3N0cHo4NDB6QUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRGxSZXkySHB5MU9xTEQ2YnlDOExuZCtBbDQ2QWhSWGFXTnltd3pSVjY1RG9rdXZNdS9VSTlpYWh3PT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUUtkaE51TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01Ua3pOek13V2hjTk16RXhNakk0TVRrek56TXdXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSZTBHTjcyTGUxc24vOTRtMVd1RlpZK3A4KzIyVS9wYUxNNHNLWmxneFFRZEpxRG1TUDViQ2pVNzFKL0R6Z25xTnBFdDdZTkdmMFlXczFYM1VvRXpyU01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnQk51b2h2bXgvVWpVcTV5M0FCMGxDeGtYUURIVHVOZk54OXhFUU04SHI4NENYd0pEQ0hFVk1nS2lFTGlvaUhpdzJsUmVyWk9oZlorR0xadzhjVFVKbjZSYklGMjI3Q1cwQWFqOE1oamxJRTRKazR1Q1R2N1RkS1pXM0ZYdUhKSXpWZSszWUZSN2s3L2tQeGU2SEVZdm5JTEJ0SGNWSTNqd2hHQmVLSjhwUktLZw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVkMG9iaFRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXhPVE0zTXpCYUZ3MHpNVEV5TWpneE9UTTNNekJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXozSkZNekp0QnprYmpFVUQrS1dMQnROL2FOYUI2bjVHQnErVUtpaHhtSHJ2L0RmZEtYWmVPZHQ1SDNHeUdLcGFPa081R245Nk9UMFRzc2trUUpMa1huYWQyKzhlK2hkbjF3VmJ1dVNiRG8wZE5BRC82K3ZaemVLWkErZStVcGhSMHYxTnBnUk1HRVBWeTgraDdVU3ZPVXNQczI0N1dtZEp3d1o4Zi9TSGpaVzlNU3I3ZlZMdmM0MFV0eU1DT0ZkcFhqbTJ3Vi9jSFNyWVZuamN6ZE1wY3EvNjFsVE4vUmxuYXNiOTFiWGF6ZkIvU292dkRmVStORExrZENSSG5mQmZKbVphQnhyMEx3RVU5bzYrRnZZd0JPSGJHT3UvdFUydEd3eTdPZTZZYVgydTVidlhMMlVvN0p0dk1xeEQ4UUJiWjNNQUIyaGlDaWJLdGtvelFzT1JOUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFpbUgrWDcxQ0R6SEQ4WUdScVhJWFdXOGZESS9kd2lqOTVPazdZQlVheFE0YU1XcGY5ekNlYTUyM1IrSnA2T1lMYVBUemNEamxyeFgrcmo3OHlSaWpEcjRQYlloNEk4OTFCR2VyVjEwSlllRVlwL3I1WkRycXRNNE1yUWlPQUlLRzB0by9VMHVuc3NpeHEzaUVpQzNvT0hpSVYrU3FKbkJGaURQcStXZVg5aWhwSkpyNHF6eGVCMXlKQlY4QTdDWGt6M2hMeEVUUWh6bG5yZVJPbUl6RlBYQUwyMWQ3WlkzSDlqU2JzeUpDazJyUysybDUzRDdxSWhERGZweUFyek1kOXI3bUlGRmNSYUE4bnRKd0hCdTlrNFlsQ1dPSDV0V0RzcFZsYVE3enJ5MnpkVXo1aTZXN2RTWXMvMU4zczk1WW90cDhJQVp0RmtFQkVTcVJPWTRtYUE9PQ==
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
    server dns dns
     zone test.corp defttl 43200
     zone test.corp axfr enable
     zone test.corp rr www.test.corp ip4a 1.1.1.1
     vrf v1
     exit
    !
    server pckodtls pou
     security protocol dtls
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
     security dtls
     vrf v1
     exit
    !
    proxy-profile p2
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target www.test.corp
     vcid 2554
     protocol pckodtls
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
    client proxy p2
    client name-server 1.1.1.1
    !
    end
    ```

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
    logging file debug ../binTmp/zzz3r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCcDBETDVhQVRkSHVmNS9USmNJUmhZOE93ejlOOXVnQ3VWQjBva0xaYzFkMi8yWm5YeXlCZEdhQUlGaFFZL1oydmZPRiszYVlvZElOYXhCa0RiQnNQb1ZvNmhoNkU0ZGNkS053QTExakhpOGY0b1lqb2dZVmtIUjRMNW9KUGhKb1pod25NRlRqNVlBSnA5aEJsYjNKT2pRV3FGeG9BL3B6OGJtdVdTQndrSFpHUHJoOTBYNHlqRkgrQVJoVzlTQTFtYndsWE5kcXVVTnptZ3BGa0FqQmhLcTY1RlhCV3NpQUVlR01iUkNhcTRVbEN1SEVudjFyR1ExTUJLc1VpZG1kL1RyUVQ3TXB4UzFTZ3FwMjBBTnZlbjZ2ak55ei9VcG9NeEdhTVE4ZXFDaXFxbldmeGdqTEt2ZVVVOXZQZGtkaTVNTCtSbHZOMG0xWGpKWWFyS3ExOFhBZ01CQUFFQ2dnRUFXTTZndWFxUHluWVNCRUo1YmRGbytkemFvWkMzcGFwMDZaTkFxclNJNEJycUlVZEZYd3FJWGxNVXYwVXlSU3lyNEtFVDFJQURwd2JVcWFheDhDSHhjcUtTK3djMlRJaXRScUI2MExTQkVoUkFWK3g1Rkl3ZmlIaUFlTHBJNHdMT2JtWWcyeWNjTkFmdG9jS285ZXhmRFBudVNYQ2NXdEFucXllSjNkR0J4bTFvdTRoNzEvQzJuanZydXphaVhlc1J5MjZ6bVRLWlBCQ2FlNjEzVzJ4VE5ScFAweUE2bk41REYwY2h0cHVHVnlNNi80NVdudE0vZzZwVmZpV2Y4Um5IdndaWFlPNHJhdjhJRUF3UDVxb0VUUCs5RkZhT3BhL3MvQnpwV2JGUm14MEZFak9ObGlaaXhGWVpjQ2ZnQW01NENrUjVONWlZeWxDUS9ZaXFSdm8wZ1FLQmdRQzdtVFV3RThvb1VhdzFhYmlnWEZWK1k1SlQvQkFiOGpKTzZ0ak5la3QxWkE0eDdJYzlmSDhwazhTZGVITkxuZHFSVkpuMkpIc284WG9SUUtEdFhWODVvd21JWWdYMG11TkNrbWpTdU5aZUFXZURkMTdZNEMvbEhEbXEwYlZzci9SS2lWYTdrcFFQRVNGOTNnaThNSUlsRDI3cGY2Zm1SMldHZVY1UnY0NTA1d0tCZ1FDUVpRSXl2UnZ1YW9xSm5WaFF5blo0L0VhNVlWOTVzSnN5MlZwOVVNNFg1cVUxRi8wZmluUFFmdnNUUzY0ZlJjTmdzRkFwMkdGeFpNdXpmSXI1ekRnNW5PZUZJTlA3U0xkeHc5ejU2MTB5dVBzeExsZlYxZXQyZ0lJd29CR1FlWU1rdHUydFhyZWJOYXpQN1ZXeHViMnAxMTA3eHpBcFoyaUZpeE9aNS9aT1VRS0JnUUNVS2pnZzViQm4wY0d5V2ZLUTdQdzFHNDFwdVk0N2xEbDVyUEJZc1h0Qmx5bkM4bTRKK1BjeUxsdytodkNBeTRiaCs3Q3lBRFFwclRiY3cyK1dxWVZaTDFTTEcraGFQYTY2V0lwank4cTdhbDZJTGRLQ2RlWStET0hhOFZCYUxFcEVTRjV4UFI2bEc4R1krTEZyZU9DQlJzUXh0VG8xblRRcFZsaFJObnJjQndLQmdFU2tjQVlVMWxsaHRwZ3kvNC93bjU5bU5temNPRm9PTmNsWGdHZ0FhT2o5MFYzTEdKN00zNytuRGM2ZmRKZ1RQdzBRNUJyd2JXcE5nM1RBNlFSVkxBbGZhTVJsMWNBb1VtUzN1cTNvVUxiVEx6NnpERGh3YUc0K0t5WFlnbUVQRXVQNlBrVGp1UjhFeGpGV1h4Mk04ZmZ5bExUZFBTMEJwck9OYVBVS1M1SHhBb0dBRjl5eGJLTGNLeHh5OE9tTWp1aUxGTnlCTHF2c3pCc3p4NGI5L084MWY3akp3ZEVBY1VTK1VFZEN1azdjZTJMYjVnZW4rVTNqZ2xSMzQ1NGljNC9BdVJrRDloVExwaTNqVGtSYngzYlh5TTRCa1BrSW9CekZVWUFYbjlYc0dWcEpoZ0d1MDAzbmlYN1JMNVhzU250RjJ1NlZFdllRRVZmNlU1emF1WkhRdVA4PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0dpcWwraXhtaGRpZGZCZ21vNHFaZVdJeEZsVU1KaVVzWmIwcW1pSXFkNjRzeXEvVURKYjlNR0lieU5OaFZ2ZWlubkJ1R1g1NWdTZThtZUZwUDkyMGhjMitIaWdpalN6WjZ5VDVEZzA3cHR2UFV0emlyRVZraVYzL3RNdE02S0kvNi85NUVQUi8wZncydytFY1hqdzVlNHNRbmFGaWthYm9xMEhXOGgrY09rakFoVUE3aE5GQXRQRzA1bnpqVVBmeDRhNUJtKzB6cHNDZ1lBclJ1REI3SGowTkpNd21EKzJDRVBKbG5tY2d3dEgwRkhxYnN6aEtvczRuS2IzYU1Za1VBVEZobTZ3Wlk4WDF3VVBBMG1JNWd0cWQ5SFZDOTNsUGUwM29hOHpEVjdqNU5oZkc3R2U2blJ1VmNTVS9kYWllNjZXdkZtMDMwT0FOeEhHQU00UWszYzNyN09YdHB2OTVPUkpsUkYyVDFESkxNVGtGSVhESmxvc1RBS0JnR2ZucGJ1a2hNeG9VTjhqWWhDZjVMSExzeHJjRDB1bm9scjlFeEJ2cjA4ZVd1bDl6K1lvcUIzTjdMUEtFUCtNZHcyUEdpTkVIRFpEN1NEbWRYaklmd3ZNMUs5bW5uekRVL3VaeUZXTkZyeC9CM0hYVnlrcVBFTnQrOHg0Q3lGT1RGRTRORDBIcVVwWkJtVllVS2J4c3M1dmZnaTVNVFV6MFhaeXRSbjdoa0ErQWhRTi9iK2k2eitJRGJFTVZneExEaW0vOCtWS0VnPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeGF6WEVteE9TMDRnd0srL1k0SUJ1TTdnLzR3c21CdUlSWnIwSkx3U2grZ0J3WUZLNEVFQUFxaFJBTkNBQVJOeFdROXpBa0k2aVBuSlVVckxEbno3UkllTFl5aHQwUHZhQm5DaWs0NXhNQmVyNXp4Y0FIaE5ueFNvNDJEZnFGOGhuZTVic0hEQVliQ2Rta0wwOFky
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVlREdTM1RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPRFV4V2hjTk16SXdNakF6TVRVeU9EVXhXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0dpcWwraXhtaGRpZGZCZ21vNHFaZVdJeEZsVU1KaVVzWmIwcW1pSXFkNjRzeXEvVURKYjlNR0lieU5OaFZ2ZWlubkJ1R1g1NWdTZThtZUZwUDkyMGhjMitIaWdpalN6WjZ5VDVEZzA3cHR2UFV0emlyRVZraVYzL3RNdE02S0kvNi85NUVQUi8wZncydytFY1hqdzVlNHNRbmFGaWthYm9xMEhXOGgrY09rakFoVUE3aE5GQXRQRzA1bnpqVVBmeDRhNUJtKzB6cHNDZ1lBclJ1REI3SGowTkpNd21EKzJDRVBKbG5tY2d3dEgwRkhxYnN6aEtvczRuS2IzYU1Za1VBVEZobTZ3Wlk4WDF3VVBBMG1JNWd0cWQ5SFZDOTNsUGUwM29hOHpEVjdqNU5oZkc3R2U2blJ1VmNTVS9kYWllNjZXdkZtMDMwT0FOeEhHQU00UWszYzNyN09YdHB2OTVPUkpsUkYyVDFESkxNVGtGSVhESmxvc1RBT0JoQUFDZ1lCbjU2VzdwSVRNYUZEZkkySVFuK1N4eTdNYTNBOUxwNkphL1JNUWI2OVBIbHJwZmMvbUtLZ2R6ZXl6eWhEL2pIY05qeG9qUkJ3MlErMGc1blY0eUg4THpOU3ZacDU4dzFQN21jaFZqUmE4ZndkeDExY3BLanhEYmZ2TWVBc2hUa3hST0RROUI2bEtXUVpsV0ZDbThiTE9iMzRJdVRFMU05RjJjclVaKzRaQVBqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUMydGoxRSt1QlJrenlVaUdwQ2lOS1ZMckduNUFJVUJaVlNQVmNlV2JrVDV4czFscHM2eTdYUm1aMD0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUXZCcFNZTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TWpBMU1UVXlPRFV4V2hjTk16SXdNakF6TVRVeU9EVXhXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSTnhXUTl6QWtJNmlQbkpVVXJMRG56N1JJZUxZeWh0MFB2YUJuQ2lrNDV4TUJlcjV6eGNBSGhObnhTbzQyRGZxRjhobmU1YnNIREFZYkNkbWtMMDhZMk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnRjMzSXBSc09xVzFBUjYyT0VPeDBpS2F6U1JVdXAvSjVROXNKUnNxMDBJUUNYd0VIY3pYdEJhVFlXYXBPVDVTaURiS2l6TmFxdGRYaCtSclVaeDdnclpXSkR6MEhXcXNNVnlvZks0T3g3TTM0czlVdGZhV1pCQWJybzZOaEpWVzNkcE43ZWY5UFZhUE5MMVFZeU4xWHdmUjNlcmpoOElkUG52S2RBNnNRd3U3dg==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVYZGRFa2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBeU1EVXhOVEk0TlRGYUZ3MHpNakF5TURNeE5USTROVEZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCcDBETDVhQVRkSHVmNS9USmNJUmhZOE93ejlOOXVnQ3VWQjBva0xaYzFkMi8yWm5YeXlCZEdhQUlGaFFZL1oydmZPRiszYVlvZElOYXhCa0RiQnNQb1ZvNmhoNkU0ZGNkS053QTExakhpOGY0b1lqb2dZVmtIUjRMNW9KUGhKb1pod25NRlRqNVlBSnA5aEJsYjNKT2pRV3FGeG9BL3B6OGJtdVdTQndrSFpHUHJoOTBYNHlqRkgrQVJoVzlTQTFtYndsWE5kcXVVTnptZ3BGa0FqQmhLcTY1RlhCV3NpQUVlR01iUkNhcTRVbEN1SEVudjFyR1ExTUJLc1VpZG1kL1RyUVQ3TXB4UzFTZ3FwMjBBTnZlbjZ2ak55ei9VcG9NeEdhTVE4ZXFDaXFxbldmeGdqTEt2ZVVVOXZQZGtkaTVNTCtSbHZOMG0xWGpKWWFyS3ExOFhBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFEZWQ0ZklQa1dUTFNIeHBOUllnbWVrNm04USt5OGI3VHF0UjA3R0dZblFxd2dERlZkUG9jc003cnFqMDh0WGhHVWZQOVEvaWExZWkwaGVMaks2VmFoNlFyQnNMMzMxb0ozc2VDWTRlaVlyMHFiUVVZa1d4QmVjVXVMRlNFUGliV0VtSHVoZ3JoTXVvTWExa2NkaWVXTXRhSFdVVHI0MzE3aUhIYXc0YkZHWVFVRDBCU1dxSjN3SHZVQ2ZOQW1HYWtZbXBvL3J1MSthOGFLcUtZWmZXdDU1WXNpSTkyWGZKTm5ZMVBJSWxIa0JaVy9Jems3dTVSK0JYLzNhbXV2L1VSc09JbitSdVlTNldUZnBSb2lhR3RzNFJLNzFkRHIrOEtWb2dlY3FsODFqL2hZcU9DYnE1YWZJZXhWdkxrbFBFZTZubmgrZ3ZPQmR6eGFGdG0yV1NYZjg9
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

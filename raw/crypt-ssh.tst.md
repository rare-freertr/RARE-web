# Example: ssh test
    
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
    logging file debug ../binTmp/zzz86r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCS3VpL2UzaUFpOXBrVWk1OWN5b3pkdSt3dEp6dGNObHFYT2RxZDJBTTMzSnFDOWRjYU1QdzJ2Q0dSWW52MXVNd2FvNU81NUNXUUFrOXM3SzVtK3NacCsxeHhKT3Z0a0x2RGEyQWUzSmE3b1N5UXJ0OHE4MHV2NW5QT3RLUm9yeUtHdmNDeS9wb3lXbGgzMFMzRUVsM0tlRmVEbGJCb2loSGhFbWlDUStOMjV5bUlOWmhYcWJONmErMlBwUTJLd2ZxN2lYVVZhZm03dytaZXJUcXBrVXo0Nk9OcVB4OHhSWU1NOWRjeVRqcC9GcVFvOCt4M0huSlBiMEVmazJjUWg2U0MvS2ljL25xTUJSVjc4RlhOLyt2NnNqZHpFTzJQK0lYQTF6M2RTRXZSaDgrelA0NGY1cGR1eEhJS1R5N21mQTExUTFKajBVQmpramh4UFZjUFI2OTNBZ01CQUFFQ2dnRUFDTGF4UWxHd2VhTTdzbk9kZjVwMjFweEZLL2E1SzBXRFJzTU9SUDJkVW5RODZDeDJpcTFQbTZwUVY3MmVLc2NEdGMrQk9GbnNMMkMxbGtQN0NqTVAwK2ZsbmFQcWh1Y3JuZHYxZDJQTmg4K0JmTldIWEdER1lKcUV3b081OENNTDZaNVN6QXg0T29yaWFnWlFTZDdDWlF1bldNYXByV2I4TXJ5TXh6UFhZRlB2NE43UnZEenJRcnBSL2F2Smgyb3o2Ny94dVRORFZ3ZDAvZTEvZm9NRXZ1L25GNUtBVGlSZGlPZkNSZS8wQUlBaXZBa3JscHR4RXJ0RlJWQnNuc0pQeHhlbWVGY0hzQk9Ham9hUHVOYXhTMko3b1JmajF1ZVM1VEVDejdKOFpFNm5wS09tdXVvRllYT1ZRMHl6dGRQTGxqZmJuT2QvOExSd1kwR3NPcXRDVVFLQmdRQ1ZHN3dSbmJrL2thdzBwM2NFMnFCTnRpVUxnZi9uUzJwQkhTanp0RStKK2lrQU5qUnRZcEw1amVYUTdFQS9aeTRXd1B1S0lRRGVtbnhLWUtlMnZEb2FzSkF3KzZFV29WWVdoRTkwRzQ5OTI2cEE3QWtmN00zTUZOTHdWR3NENG5qcHNnOWFJV3paUkxXOUVmbmRhLzJiZkNia01tUUNJZ2ZTSkorNmFzK0tld0tCZ1FDQVRCZGFpZ04vUG1MNUJrVDVYMFlULzdPd1dzU1Joa3lEWUI1VFNRM3VFNUJ6cXo3Qm1QRkNHY2ozaTFLNUZjS0Y1WWNyZU91S1FSa0V5N28vRUJGSi9pQXJ5ZXBhZi90YVNMbkw4VllwbEZvejZYZUdaRVo0SDBHOWR2L1pYRHJxL0hSK3orTDhzUFdnSzhuK3lQY2c1NlNrdER5a0owTy9OMDdvQVFMTU5RS0JnUUNMNmhKM2xVQ1czZUp4SmhNUWd2V1k5aW1jdXNlZUNhNFNtNElwN0RBV2tKNllqRVIxditHYU9nUkVIdXZLa3M4MG1yRnQwN28xSjFFcG1iakdSNmxlRWYrN2R1S1prWnB1Vm9rWHNpVGJQSnh0Znc2dzNrdmVERXhESjNPam1ZZE1Bc0ZWR2JoQng2K2hVcFRicU5HNGJLOHh3ZmNGNlZqZFgzQmlSSWVxc1FLQmdFeFQrTGptenpuT2xmZHRvVzl6SFRBY3VueTdJNk1vY1REZjZHcklWYjlFYUhaSWRTZWNwRHdkTnhEL0ZKSUV2aHdHK0NvRzRLcjZHN1pjdGt0NmRhNjl2OG9OY0oyeThvaytKenVNTXlTOW5BU3lhMmZMRkptMmp0ZjNpak40eVp5djRXYm9xelNHMnpzVmtqRkF3cllTMmtNYTc5RUJneTZwNnduZ1FCZlpBb0dBSWkxUEIvSTgxNWg1RU1pcjhOeHlkT29oQjhwempNbHFGMXVSQ0JFdC96ZHNaQzYwMk9XMGVEVG5JMzJXcU5EZUExMmtDTGJKSDkwQlJ4ZHY5SDZvN0tBZlFJTHd3WG1iZVJMSUdsVGVlWXpZZHYrSHBNbzgvaVpVSmxMdHA4eWlSUHZUQ1ptV0J2SUc4MEdicTJzTDJLTFJybVlQY3BONDlUUlJxeGRpU3lRPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0dabFR0YzUrUnJ3eFc0djNCNWlVZmRiN3kwMURVTGUzWm92aUlQbk9KdEZMdEs5d2hCaHkwaEJISGhJR3psVGVibzlxYkZBZVlaZGUvUnh6QWhYdEtienpYL0MxZ1JyS0d1L2tHR1MxUnZ1SDRONC9EZHJCcmN2UDNOelNwVnVTenRRcmU1d0QwMEhkSGltUWlnL0NnOXh3S3g3UUM1UzNUSC9GYTVHZ1dmaEFoVUF6a21TblpFai95UENuMUljTTlnQ0tjanV0TTBDZ1lCQnJrVFBFbVlXaHdqc0cxVnBuaTVtTjZ5bmRSb1ZJL0RuNlZoWVFtMmNkKzBpQ3d5SXU3dUVEcWNXdGlmYy9kZ3F2d2V2dGJhK09LU2UxQ0tiTXpZOGQxYWt1QWVobjN1WUZjRWE2K3p1V2s0WXF6aGhLbjR1SzF2Z0NkbTZaTG5UNFVRYXRZTmUzV3R0dXcvVGEyTzZiUXV4RnlYZ3NsVG5Qdm9zYkcrN1pnS0JnRGVDM2g2SFQvZ3l4TzgxKytXNU9jdmlWTlozSFprb0pJajJRMmFmR2FjUFB5QytwakhMeDJLOVpTb3VDK2JSY0d2YUtxUmhRbmJZdWFtdVhIZWk1Y1l5dmQwcFRValhzVWZEaTI2YXZFaWUrSTVtMGw0N3pEVndYM2ZRVWpzUUFTK1RyaHEvRGdLamdobTVkMk12aVBIOHI5eFAwVlRGZExya3dLalUwMU5oQWhSRHFIRlorN3dLMm9pbS9nYmpSYmZoenVNczhRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNxUERNVFQxTGdLb244R1VrM2xDZHE1am16T0Y5d3MyL3BtNTBiSjc3aG9BY0dCU3VCQkFBS29VUURRZ0FFbmo4Y1Q4eEpGWjFjdGszcUphdVMxQktvRmtLY2FCbUUrR2V4bDUwUFZIMk95NjE0RHRiWmRIQkxNUzJQcTFuRkpIaGx0VWE1Q0U2OFB6a2ZLL1JJc3c9PQ==
    !
    aaa userlist usr
     username c
     username c password $v10$Yw==
     username c privilege 14
     exit
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
    server telnet ssh
     security protocol ssh
     security authentication usr
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
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
    logging file debug ../binTmp/zzz86r2-log.run
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

# Example: sdwan over ipv4
    
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
    logging file debug ../binTmp/zzz25r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQWhuRHFlOGVOd0YvTUdWNi9XNDhkMUNFRlpGTmtqVVo2S09ZRnBjeHlwd0hCVWNjd0JzOVREWUN6azZOSjhHVm9lU0F2T3N1d2l6Znh2RCtKMkZlUHA3VmVYZHhaUnoxajAxRC8vUCtzeEJEaW5Fc2NTM0NyemE1bTZySGRJVEFsSGJlZ0RodGRydzlRNWRQK21iaU5ZeW41RGhEMmpXRjBYZWRRS3RGM2J5bjgzcGd5Y2tQUzJoQ0NKRDM0d21GTUJGLytCWFV2WmFlWUl1dmVPQ1lNMXJEOUx0b05Za0ROVnNtQkR6T1A0QXVmMGJjMnZnbUtPZTF6RE5WT1pnNDF5MW0ySXlQNTgwVUNKSlYvd0trd1YzTkdOS3A4ZGUwZTRRbHZ5ZEljZitDanpYMVQ0ajBMYTVTL0ZWUm9adGxJaDZjbU1aNDdhUTZTTDFkdlQxMER4UUlEQVFBQkFvSUJBQm91aFV2RHloUkwwN2loSGcwYnF3aHp3ZFFPOVljWjBaS0RjVmdmbjdoc2ZCU01BUXRpZHQ4clVFMlJRRVlEeWJ2RkM4MmNlMjR4WCs5MFJFa1FqRlp4Mk1YWXNyNVA4MC9rOTJWeStWZFpubmdubklRSWxqekJHU1BkclozWC9YSnpIMFdBQ05lZDJQaFpONzBDRnU3WDdydlJpK0p1dHpYT1pXdGhUYXdsTGVCNWcvZGNmZGFod3NiYkRNLzdLSzRQeXh6S3Vrd2l6ZkxFMTJ5Q1VSN2c2SFJickh6eTN0T3AvSFdKL1RTaWtJVTN2Yk9nUmFXT3JuU2dKb2tzSFQ2dVIxQ2VtY0JSWTZhM0lVOXhDbTVQY1FiWmZhNWtYUVVoSm1MWkgrSWdsVXUxTW1CSnZ2a0Q2Ui84R2dtTmFTM0xBQ0w1ckZuNTlqTlVuMWV2Qm1VQ2dZRUF2OEIwTnYxQmZiSDdCRTloMFlHSVBIejBKanhGTnhyYjErV3lVRS9ZOGVKamczQXRQNzh2S3hUTEd2dWNGdk14ZFprL3lUOExFbmRTaEE4MEVGbTNzVllsRlc4ZW9meVdKdUlZL2UxN2NHckNEZ3NmSGZrR1B6SEk3L0hueFZiMHdtaVNwZ0tXS2sxdHpQWno1VGFhRWhvVHB2cUgrODhjeXZmTXZnbC9YWE1DZ1lFQXMzeWdObWp4OFBibzZoeTJETUdQZnFweis2Tkg3L2lKUEtyWWpORTRPM3dEclBLUCs2aFdRYlZBS3BnVjhXdklvWkhtV1pkWVRWSW5VYkNkZDk1dXFLcW1TK0ZMSGkyZWVFQmRWaVd3c05WODNIM1JVaGdyZHJzNUlMVmRoTTZINGdlOHpnNlZ5T1I4M3hGUU1lRmV0WUxrNmVkd3czZ3pYVDZxZUlyMVMrY0NnWUEvcHVndEZOYTNuZXhBbXdWU29aZ1MxRHZMc1hnY2VicitxUTRQSU9KWU1SbHRtVUE4Qi8vbFlpcWwwMTRXTkRaMzNoNVJkSzc5TzBUVjk2SUZ4M0oxMkszSXRyRkpmbXB0aitKUjhKSm9WOWdCQjJvVjdnTkgyUVBsdXJ5QVFvUlBRSjFscERncTVMY05NY1o1RVM0RjBrZ3h4cnA3T1Y1S2RnV3VFOE1HeHdLQmdHbE9YbVZ0N3oxMGNEVWpRVUI4dENjWjlOQ1gvUlh6V1BtS04yRnZRekhMVWhDL2cvQ2YxSFBhMXRubXYwRVUvdktrdW1Tb0lqdkRUcVJrSGc5OUpxbTQ3YmFwYVR3OGdiU0Y5djBiUWU2T1l5S3Vnd2hLZS8yK1hRY3V3YjZ3dWhMSWZXTGNOYzlYRjFoOVBQTDNDbTB1YmdZNkx2UFFhenB6RU91R2crTFRBb0dBSU9hZ3ByOC9Zd0FDcXRWZXhIREpvUnplRXlmVjI5TUp0SUM5SXA5aDZoZ2kxUFNIMUw3d2dRcTFOYmpLYUk1RjdLbnVWWndyenhvckxuL0ZXcFpwTWVxSTZNUUhRYmlFbTQya1ZqZVF6SkNEYTFrdnp3NzB4NDZCY1hkYTFObEJ4cElTeEErVGRXRVlwSVZkMitUUm9iVVlUb0EwTFV2Tkx2MU5mRk1jaGZJPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnZBSUJBQUtCZ1FETUJYNTNnUFpxSXk1VnJIQSs4NTArSlh5ZzFjUVFFdTllTGFIanhOdUd1bGl6RVovbXh6OFljaWoxaU44dWNJWE5MWEJMU29mdThFYzJOdVc0MzdnamNMYzYzYjYzYzZsZGM4M2EyN1FjL2xDaXVjZmJRWWNzQ1FoRkd1aThQWWUxR1lQOW5GTmlxSWNYMWdseVBOMS9NRXd5UEhtenYrS0FhWXg3aVZNRkpRSVZBT053ZmF4bHFkMGg3TlpjdTlqQjlveGxySS9iQW9HQVVacVJ4L3doZUVrWU9maytlVU9CQktHRVE0d0p0RnIzS0ZkaXpwVjNKeFZ2UnE3eWZrZHJHK1dOM1lReVpiR0VyWitJZGxEbGZUbC9Mck1lcjU5cExOSHhNcWYzN1R1MXYwK2hFMXFKQU5tWEJJYTBhMUxxNERaRFdPcmVoMjFGYlZGNnNiT3ovTDBwUEMxOThSVGZ4UWIrVW1ZZXRzRkJ3SjB4bnp6bklUSUNnWUVBZ2xYdXJZVHdIZWpNbXhzTDluQlJwSlBmL0o5Tk8wMUNtWG1tREp6c1VITHFhVmV1T20wYk9YQVd3elgrUW9yMVd2WUxOdzhEdW1rRGUvUU4zMFJxUnp0TDZqMzlFZUE5cW9mR0F2TENMbC9zR00zeGlDRUdob05DRDFEelNtMDkrUzZuTEpUK0tQSlhuaDZxVGhaQmpLTzZPdk45UzJrRlB6bXdCbjk2QzQ0Q0ZRQ2dRYVBJRVZTbUFBdGZBd2RYcW9JUUt2VnY5dz09
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMG0zWmZaNWlQNUpTcXNXVE1SMkpGcTQ0bzZpdTAyNWlMa2NhRGRlK3RXZ0J3WUZLNEVFQUFxaFJBTkNBQVFHSVFjQStHcXVJY1Raek1FY0RRemhtdDNRUmZ2OVpYVHhrS2ZuSHlTUGk0UlphMHJmRnl2bS9najFvVm5YSlNVU0tvMk0rWjNBNDFVVWh3QXNEb1Bq
    !
    aaa userlist usr
     username u
     username u password $v10$cA==
     username u privilege 14
     exit
    !
    ipv4 pool p4 2.2.2.2 0.0.0.1 3
    !
    ipv6 pool p6 2222::2 ::1 3
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
     ipv4 address 1.1.1.99 255.255.255.255
     ipv6 address 1234::99 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
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
    server sdwan v9
     security authentication usr
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     pool4 p4
     pool6 p6
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
    logging file debug ../binTmp/zzz25r2-log.run
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
     vrf forwarding v1
     ipv4 address dynamic dynamic
     ipv6 address dynamic dynamic
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1.1.1.99
     username u
     password $v10$cA==
     prefer ipv4
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1
    !
    ipv6 route v1 :: :: 1234:1::1
    !
    !
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz25r3-log.run
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
     vrf forwarding v1
     ipv4 address dynamic dynamic
     ipv6 address dynamic dynamic
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1.1.1.99
     username u
     password $v10$cA==
     prefer ipv4
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.5
    !
    ipv6 route v1 :: :: 1234:2::1
    !
    !
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz25r4-log.run
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
     vrf forwarding v1
     ipv4 address dynamic dynamic
     ipv6 address dynamic dynamic
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1.1.1.99
     username u
     password $v10$cA==
     calling 1701
     prefer ipv4
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.9
    !
    ipv6 route v1 :: :: 1234:3::1
    !
    !
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

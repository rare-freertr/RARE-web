# Example: sdwan with fixed addresses
    
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
    logging file debug ../binTmp/zzz55r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWpUUnJUTzNSVVNoZlY4RXlFZ0JtbUlhaFVSbVRFQlF6RmZBWHVhQ1pRMDU4NHhLL1dERnppOWVCcW5WZjJOT1F1TnpUZFdqSEExU0tCRTNzbmVVWUdheElzR0x6RzlFTHNmdTVSdzhnNkw0TWpRTnRvUzhYd2w4aVFRS0hGM2szM0xYQUlrajFYTFNxcTFKc3p1aCtGTkdOcUFOZEpvdk43bWpIRW03aTBlakxPYTdLNHhMb05Ocm1WVzBKOUtQcXBEZDUzUWxFOVBXMlE1dXFpeG9nc3hMTSttenZnU0tXckVKL2x4eXJRdWJOTzljRDgzUDNLVmxDVGhoTjBuai9tbUczczB5cHh0cG93VTVoMnNoRlFabHdvYVlSeGNRSHhJYVFucGtrWm52K2hiYlFzeE9DaWVEVlNuQXd3QXdObk8zYmV4REFLa1I2YnJQZW9BbnV3d0lEQVFBQkFvSUJBRnI0Z0lDSlhxYzRxV1F4OVg0ZmYvbVlFdW5hM2lJbndWbksycDRlMTE3RGZEWVc1K3Q3d0lOQmppb3hnRlNDeU9Rd2NKTmRzNGx6dDQ5YVhLekU0YWY0bE1QK203MDZDcHphSGQybjQzM09vdXRlWUF6TitES2pjOEFLVHRwU29DaXpkMXNmUWVRK0NRNWpCZkt2V2pzelhsMzEvTmRPanBlZ0xWQzAyN0I3b2swdzQ0bEJGaUw1K1QwOXFqUDF3OFNueDg1NUZDcmVnNElKR1d1QXFQam5JUW11NnU4UWsvTXlZM1JPbG9OUU1UQlJodml0eDdQMnhiOFpuY2ZJZFhkVmw2MXkxcUZCeVhJSTZvOGRlRCs0T1FPUXE5cW9JQ2QxWlYzMjNwaGxmTmFMRlRid0dHWmNqOFZ6NU5veHpZRnZsYXdZZE5aMkc3MHlWRVE1YlBFQ2dZRUF6cVU3c0ZzOFpPOEtkQ1BNdkp5SU5PVkRsbmNUbDNIQ1BpVkN4QmtuNXNaUlA3aHcvN3FyY3pFdCtubUN6MjcxY3ZvaWViVDJYMTNJWDRGUkRqaGI5aDdOaEltNFBLdVAvWjBINHp4NURVUTBWbGJ5L0EyaytScEk4dE1XZXV2ajhGb3lLNmtJMmwwakh5QWdreWJFQTMvSCs2RWZIM21LazBrRjFEMG82TjhDZ1lFQXJ1Mys1MzFrc3NKZEZpV3pVZFZOR2pMREtXUGtrRWF2c0lieUc3QTZEMkJDVzhvUkRwbkNKVzg3Q3FLTjY5OG55T3M5WS9qVkJaYkc1Z25XcDk1R1BDTEllNUFPZzV6U2VPVGplcWNqSktjMXU0eTNyQkR2WHhiMDEwbzk0OUxHeUc1VndPR2F0ZEJ0NGdDR2lMMm9GUTUwejNoMWlHVklRTmFPQjdvcW9wMENnWUFCNGVWeVROSjNCT3B1ZG1rR0N0TCswRnZXUWcxdW9yMm5QVVduYmFjOFpmQVZpWU9XQU1oUkMxQ2s2SGgxbFVndEhQUTFjWjJRN3RURmNmTWdFd2xiYTVwcHE2dCsrZjBjelZKbUVvWHp4ZnhJRVJDemxSZzhvSzJyY0pyUzBkVkl1am1jeGpScmNNL0NGOVBVSTFWRHh1VTJlSmhFL0NGMENBVkNrckFOdHdLQmdRQ1Eybmx6UGEydUxTNmlFVlA5VnJFREdiZnNSVkRXZkFJdUhvRExsdEZ0UEJ1WElLdWhPSWZCTWV0bE1oaHRrcHZDVDdIRllCOGVBcTN2ZllRbisvS1RCNGFXYzBMaGozSG1ORHQrckhwNGRwSVRIVUpYRktyelJmSTNlTDNwTXZmeXJ4TUpwb2ZUT0taVk9IUXZOVVhETWZaZWV2UndudFlIQXVRWDEveElMUUtCZ0hHTDlTMVVMNWdOVmtKYndMZyt3cGJFWmIvYURqZVdtUHBZTkdkdlRNVG5zOXpKZWtIOEk1M3dkMmY1MWRMaFpEd1JrMU9ZRHh1Vis2Z1JLK1JBd2xRK09FVklIOS8zRHpJUW5zYmR5WDV3elU5RHc2dmNZbTBoUkhwbGRqcDBZWlZ3THdiR1ZXUElLcHdTZWVzZ0Uwc3ZhdmVpaXFXWmdjNnN6OXBtWWgrVQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0N0a2Z3WHp4dGI5emFtSjNhcVg4REQ0d1VxWFdNWWJNNi90WEhrb1dQdEVmV2pIZWVKcWNJd0Rkd1p1ekpZL1JjQjlFbVpUZFZpd1lCT1lmUXdHZit4ZDhMZGZBUmwwRUlzZ2NKOUY5aXovMDFabm8xVEJuendnYXZ5NzV5ZVF2cVVORXZ0K3RMVTZwOFlMTzR3TThCQmJuU3BGWUE0SVRSWFJMTG1BeFlMRkFoVUFvNTBUMnU5QWo5SXM1bFN3WWZydGtiQTIxaWNDZ1lBQ0dtZW9tV0FFNTl6Z1FOYXVtUmNxYUpaMGRDa2dxVVBQeXZzQ2NmWHhuemdzV0N1UlZacUxrSHpFbVRuTXgzNlBjV3FNKzFwRHJ2Q3pqakRzemlJSm00K3B3cDA2ckJienNWUzQzZXM0aGJObEZuNWxMaVVqbldYWHhIZjVNT1ZOVG9mUldUNk95STRZVk1OSDZ3dEVhWjc1SktPTUJqWmROdkoreUZaL1RBS0JnQW13c3FXbkRJaGhLM0Z3UVNobzJYRkxYTDIvZ1FVRTc1V1Z5R0hFUnkyS0FRaXJZT1RubitPUzJLR28zMHI2SzZtUjkyb1RDMXhzdVZRZnBENGhqWW1jV01WSjdIclBQZW9FY3dJaWVrUG1raWsyRFBKUnArdnZ5eE1uYXVxNnl5bUNhVUhsdzdCQzRPQzVTRXZTN3lrdXFoNkduZmFBRnVmaGV2RlJCQjByQWhVQWlHZzJYclovdTBaMURiNDVtTXh5cXFtSDZPST0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNNRGN6YmhUQ3p6eDhwTU5pNHNGQkNrVXVpNjZKdUswVXhKTUc1WmFRT29BY0dCU3VCQkFBS29VUURRZ0FFTDVrU3NCZWIvSTZENTZNTTgzVjh0eExTSGY3d1JadHB6NGo4SzdKMVR6S29kcE5Ib3Mrby9iVXJ3MVo5RlNUYitVVUR6R3NLK0E2bjVQZkIzNkg3SHc9PQ==
    !
    aaa userlist usr
     username u
     username u password $v10$cA==
     username u privilege 14
     exit
    !
    ipv4 pool p4 2.2.2.222 0.0.0.1 3
    !
    ipv6 pool p6 2222::222 ::1 3
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     vrf forwarding v1
     ipv4 address 1.1.1.99 255.255.255.255
     ipv6 address 1234::99 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
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
    logging file debug ../binTmp/zzz55r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
     target 1234::99
     username u
     password $v10$cA==
     prefer ipv6
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
    logging file debug ../binTmp/zzz55r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
     target 1234::99
     username u
     password $v10$cA==
     prefer ipv6
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
    logging file debug ../binTmp/zzz55r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
     target 1234::99
     username u
     password $v10$cA==
     calling 1701
     prefer ipv6
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

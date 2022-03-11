# Example: sdwan over ipv6
    
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
    logging file debug ../binTmp/zzz98r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCZWJJNXo0OTQyVnI2TXliV0hTaXdYUitZZGxrK2ZHZFoxZ0JSUFJXVHBNckRLdXorN0x0YXF6cHdSd0c4Q0V3NFB3MTY4NDUwZDR2MmV1L0RyYkVadkxwTUJFeWZLc0hNbHJPUHFQRUdnbU9PbFMvbzdlazdPT3E2WkhLWm02OFNCS0RRZElIVEltUjdUTjZvZjd5VmxPYU9qM2wxT3QreCtOUFM5S0tEUVNCRVJkNGVxOHpjQVBVajRUbU1FbkdoLzFPMkRrZTk3VE9BMG90T1lzWWpqQUJJc2VvU3B6eVNoNjdoRXVBaUhGSUJRZ0tOUUxSZTZxc25kbmloRlRYQjZzcVh0ZjFTdVRBamo1QVBlSGNzWENheGN2Z0FXMWhyNlVCU1I5S2NNbGNvWVhTYUxrMXZKTXRhS3h1Qm1lbXFxT0JjM2k2WkJCb3FqMEtzMHRsZ3pBZ01CQUFFQ2dnRUFFRTZERTNTSXphMlJYdEwrN0l4Y3JQQ1h4d2hNVzlla2Q4cFV0NVB1WjI5L3BLTk4wRSs0ZHVzVGZPVlV4bkR2L3J6b3dZbzFlaEhYWnZCaUhPWW9DODlwUjhnOUdQMzhCTWVrM0xEblRJcmExWk1YZGVvYmJmWW9iUHpMcC82VGd4S2tYVnRiajhFUjE3eEhQeGlYeHJGN2x6TXh2Z1I1YlJwTUlkYkFYdmU4Nkp3dllSY2Fac3JJa0VNOFREWnlVUUxQQk5CRE5VcGZSTUlmblRCTzdQZk03RnozVHU2U21kTU1RbkFuTUZJT0l2Nm5CNGZVMzVReXdtR0lHa0NPMWlHYVc5eThjSFI4YTFQQnZQSURjR29hU0QvakVRK0tsaGNOSkJGMFpLQXlTMVNpM2JGRDlEVGN5TVczVXMybDNoMmpPR3gvYU1BRnpVQjBYeWQ5VVFLQmdRQ3pqN2ZwZXM1Vkw1RnNsOXltcERDcDU4aFVwbDNTVWh2aVhnelZlSTZHWjhNTWFHaE94a3BRenJoOXV0U2F4eDh3Rys2ZmV4alZxTFMrRk5QeFBpY0pQU3BMNHlLV1JrRmN5SCtBTkpCVHlucVhjdlpWWkZsK2NFU25TNDcwa2QyRjJzZUYvVUJWc1NyLzZsc2g5VXVwNVl5RGhpQlFqUGRPb0dEeUtSZkUxUUtCZ1FDR25yaWJPQUVuNUFHWnp2Ym5JNE9lTjA0OGYwNXhGajhNUGxSanZySlI3MlJ0VDYxV2dlWU53L2FFanlCcTQ1OWxpS1k4Vkg2RElxRXNLVklOZ1MreWx6cWZUN3RyWGt0dTBHNEpEV1hVUUxlTnZDMHlFbmVrc0xzbHVwbHdTM3B6ZXJtS203WXhXbUExM0RhNUl6ZFZQbDdxQVZDOUlqbmhqZkxJN3NMTTV3S0JnRmRqTDNkaXUvNDdTMFFWV0Y2RmMrV01sek9UVC8vbTFBbEVDbXp0NGpkSlVtUzhmMTh2SThYV0JYV3pNbnN0UTJGdmhwOTVFaW9Say8wYU45ZWxqdXZ4SjUrTktDMElmaEVBeHdTSEVHS25IU2lOMjVMTlpyeWhPTmhPYm9GYVovd1g4SmltR3VSWmQvcmFmSVczVXA2Wng5dk9yL1ZqMVl3ZmcyNzNUc2tOQW9HQVQrK0JpTkdKaGlsU2RnVTZBT2ZLcUxFSWFNM2pReTFGaEx5aUdaUkxpSEdRL1lPWlZzdk5VaEV4bVdidmhlamhaa1h0QjlmWVEzL1Zta1p5N1lmdlRhbVU2ckpLaEtlNlBQUFEwdGs4eFBza3d5bWc0S0dzbjRNOXJWcU83K294ck02THkrMUlFeWdxQnZGYklUWHpEay81eGhPLzRINnBSZkNtNEg4OTlyTUNnWUVBZzFzYVRKYmZCMDdWYnZIckFsNFQ4bzg0YUdyQWVQRTdOQWZyaU85TEpYVmM2SkRFR1VhZzhkcUFPYUNzdjhLM0hsc3VqcUNGMzgxb285VFZDWEcrN05oeENsYnAzSWxiWmZTZXNQUmt5WlBxeFJtS3pMR3BxTWRwTUczd0k3MzRwTXhIekdMNTI1SFpONHBwaUMvWEh6ZkQ5SUpLR1BkbkFyU0xkMkNEMnhNPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0hyRDcyNXluYzBMY2lIdUFxU2JmdnVCbVdLb0FLSkpyMUZTbDZndnZ1V2xTaHNhOUJFMjFDK3BQVnUrY25UNFQ5YlZpbXhqQU1Wd1A1aThOeE5XbloxNkxVdklzVWlVNUNyRHJyL3hnSC9PaXRiOCtaY2NWL1V4TnNURjdGRmFoOTdiY3BWanZneDNMd29GS1owcWtTckt5TkZkMnErSkhndy9wZjZ6VTN6TkFoVUFsK0dHbmMrL2ViN25aWWtTU1E1c2R1SG4yL2NDZ1lBSHZEUmpxRG5DcVZBUERmOXNBMUc2SzJQdUd5L0NPOE9YMzgza2Q3WkdhOUlCeHBHYi9GY1BWSmovWFgzRk0vQzZCbXlCRXVsS1AxYTNoUUFGdmpHcVF0dTVWVEphTGRhSFVOQndGM1ZCSWlLQnJBaFNCc0FlWXN6anJnVENKZ3hPRG1qLzZTMzJtSUJEa3FSVXUwSFJsaEs2WmN0dmtqSGlHMkVzM3J2NVRRS0JnRjgyU0djUWF3cGFmZnJwM3ZHeHBXNlFybVFjUmJUQmk0UXVyKzAzQmMwbnZFSSswbnBwc01aZWU4RFJYdEtIU21jRXpVNlAvWmtBWm5NSTZRcmRjUTBVQmQ1eHdPandvYW9PSGdMSWNGbUxEVGJoaDl5YVVVWXZVdEgxdlpCRldXVk55eGZXVjNQU0VxQ0tsNHpRYzg4VDlmbGozMnN5ckwwM09veWVUVWZZQWhROGkzVVY2T1E3TC9sbExLdEJYd3Z4dHBEbGZBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNBaXVIUkdTazAvZFpxMnRrcmc0Ujk2TmxRa0lzcWJFWlQ2UC9TbForUW9BY0dCU3VCQkFBS29VUURRZ0FFTWk4M1BvUmNXZDNhNGxnYW9xaTRSeUVmVXorTzk0TDBhK2NiSkIyVlErZlozMG5UenhySHliMGtEb0creTh5Ty9JOVdmUTA5akkranpJZldkMGhrSkE9PQ==
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
    logging file debug ../binTmp/zzz98r2-log.run
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
    logging file debug ../binTmp/zzz98r3-log.run
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
    logging file debug ../binTmp/zzz98r4-log.run
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

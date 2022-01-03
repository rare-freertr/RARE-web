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
    logging file debug ../binTmp/zzz1r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCLzEwSVRSWFJsZ25mVHFaOC9BY3JSaklKUDBLdzNRV3F5UGhTdE54bU5hZW1WUU9qWE9WQ0RqNFJCS0k4Q2F2azgrVmFEWjU2RjRvYVVQMVU3K1NGVk1SMVBpaGp5VDJkQ29LVVpRcFhyaEhWV09XUlJVWHRBY2dlQTU0REU5Y0k1eXIwZXBZeXpkci92SkZJT2JyNnRrVjVibkhMdjNRakJKQ1Rhd2R4b1pCeDc0WW41VFpBVEVsZjhYU1lNeTlDWlpBaSsxRnQxc0hYVUlIRFNSbVBockUxUGI0R1VIc25FVVdpa3NNclRtQVphZlBEeUlLbnBzUExDd0JLSTZjMUoycFpqZVFjU284aGFDR2ltb0ZVbzNsclc3Q01TZmc2Uk5kZUZWQk5hREJYTDh6dDNoRFU0MnU3ZGJHUytPbVFSSitkZWt1bmNHS01vT2NEbVF5ZUZBZ01CQUFFQ2dnRUFLK1pXZVZtcmE4Uk9zNitXME1Nank2dXRnQTBQWm5ZZlZvLzg5N0pwSXVlUTM4RUhkQWpwZmhRRmZYNlpCV0tJcmdpTlRkaUNWa1dBbzEzUVBpVUI3a2hNWVdqeHdodkVRTnY3ZGQ0b3IxU3dHbWpnNncvSS9FdHNDamIxUUMySWdlSDk2WTA5OE03QmdEUi92UmNJZ1gvZTRDU3NUM1Flc254Zjc0TU0xZ2V6cSsyeHBhYmgxS0RlMUFGclh5NG5lZ1M2cWtsUWJnS0pWaCtEajQrYmkzeFh6RllFRjYzOVQ3Ry9VaGtIV2JXbnVIeHBXMUFEemZyVEhrQ2p6cGJGWkZFUHI5Rmpzb0lpVlVFcHh0R2tSSHFyb2xPcHJmWWVWNk5DMm9ZT3BMVTVKTDdIcHRTT3hHS3dCSndtcXNRR29ncFlvTmJXbXl5M0RuQ3dXS215b1FLQmdRRGdCRU1uSFBLRTZIQm9zUGhBdXNSMWZZWFhGdisvR3l6R3NmcHhuRVlKdUxad1liYnNnd0lrWkEwVzJNSTRBQjJONVg1cG9yeGlFTkw1MTgzTWhTc1lUSms5MnhKL2dyZWtRU3hMSUorOGUxemlBT2tkd1ZSaDYraGdRZERFTGlQV3BHeVlvZ3g5RGU3OVBtMUNta2t4V3ZRNUQ3ZmVyQWthUVJNTEUrR3pPUUtCZ1FDU0Y4MEJ2Q1Z6QnpPNTQ1MXFSSHgzem9DbHd6anJ3ckIyNjdnMDQ5QXpGYisycldKOVVadlBYWjJqUjM5T240RTc0ZGV2RWR2WU5lTC93OGk5NVZJcUlXOU5RdVdZdW9aUHd5UkVwNDMzanEzMWxxQWl1ZkZJcVBoT0h6UkN3SjRNTVpJMktMNVVoV2dXdGw3dXZKRkJNL3B1MnRLaDRDSndGSk5TMUpOYXJRS0JnQ0g5ZzVMenVYaWhMQzAyYlBTbFloblJxZlV3OEMwM0dsd3J0U3gzNGNpbjFrYkhETkptTG5VSEdWVldIbUlRNG1zZFgwajRBRTJBOEFJbzFIa3IyNVljU1VReGNXVVhtSFc3emRTNFpvUmEwNFVYVGtmTmhkZzF5MVNQcC9XY2FxT3UzeXRwcXl0dWFjelRKQkR2Q0J3TkNQRi9pUTZvVzlrMzlvTy95SWRCQW9HQVFLY056OFcrNFAvLzhUVDg5Z2xtOS9KSVZwTmx2bGhEbGUxTmNRS2NvZTd2RDkzOVp5NVZnTmlTS2E4N2RNVDhBVTg2RHowZENMc1lRVTRZcVlreDZua3ZjNGEyYXZlbzl1V0tTR1BLWFJNa2d6bnNsbEdwcVJrMkFnU25NUjlqRWt4aHcxd1dsdnNQREhZYTN4Wk9SZ2ZGdllkVGpkWE9COEhqVE5YTWZHVUNnWUVBMTAxR2dKKzBtYmNsc3NkM1Zackk2Ti9nSkVQZjRnV2piMkVFUFUrRllyU1JUQXBVRW9lMUw3bWxBRlY1Q0xaa1ZsbmJFckFtSzBaR3VKSFFaM1p1ZlJGeW9vbmFGdi9WWnViajd4Q3JxNUJVTjVuVUZsNGdXNzlBMGRtTkxGUTZPKzc0Z0VkWFBvK0hUZi9ScjZQNHB5ZTMxSG9yamN5b3UvTUd0VzhVU1N3PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0hDdXorMjF6RWNJazVzNUtpVXA4aWNsalRIWi9TYVNPUmtBS25DbjZoTXZDdU9wOVFqY01zeVRiQ2oxRmgyaUo0emdXN3oxZk1yMXdpZGRRbGZCZDYvU2RSK1RVY3pNQTZJMVpzVHNSLzdyNEg3eXRRdmM4VWFTdlo2NW5CVytJMjlFZ1lEUDZzZUpvbWthTDRlZ01KbGxiZXlKMldBcHUxNnFVM01TcDFhcEFoVUFwdW93Q21wS0Q4U2dTQ2hZZXE0S1FiQjNCaU1DZ1lCT050MWVpQUV1ZGdydWxreStSOHRBbk9xa2pkTHdza2Z1NTd0a083ekRneHJCT1oxLzNWUkRVMzVEMUFpTi9DZXYvVlZWcURySFhEeFN5YTd3RmpkQlFrMmJyVHVLMUtpekM5OW1DNXVCMlI5UEFKcTlWQVl5NjF4NlBYcURmT004RlR0NElTZWdvS0VubVNac0RkRHg5YjRYcmtnb3dqaFpHdktrYTVkSzl3S0JnRGlZMGNLT0l0d0lSR3F2QVBveFh0R05VVFc5TDZZbVlBY3ZPZENOSDZ0RjlHZis4ZmNuS2czc2c0OGtVaHY1bGs4ekphTHA4QktBTGhwaExqT1BaKzVrRUl3MTdyUzY3elIvY2pGWnRnZC91NVFYaFRUNGZ6OVRxdXdYTkJ2QUR3WGtuRUl6b0JVcytuRmIzSVVDbk1FTjRCZXllNFZNc2I5dENQWjNBUys3QWhVQWwwT3FIV0gzOHJaVjRsZGZyRitxVXdqOS9hQT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUM3b2cvYkpJZkVIbTFmWSttcFlydHhEZng1QVdTWGpPdjh4Ukw3Rjc2VG9BY0dCU3VCQkFBS29VUURRZ0FFc0xFZitxQUlEcW5ncXpPNGtFazNUR05nNVFEOUFrR25ZOXp6OFkrTEJ4ODNMYjNmTTU5QWo5Mmt3cEtteklLWTBKaDI4TG9uajdFd2RIOU1VRzY5VUE9PQ==
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
    logging file debug ../binTmp/zzz1r2-log.run
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

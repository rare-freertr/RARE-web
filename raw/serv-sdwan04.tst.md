# Example: sdwan hub and spoke
    
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
    logging file debug ../binTmp/zzz41r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQXh0RlBGeUVFTzZKY0liakxtenJrK1doQ3hKRzZjSE5yN1M2UTlkNy9iY2ZYVzRIUGluTkVibWF2TEh6VzRPS2ZDZDk4N1lQb1dYNk82RlRYN3dYT3JrS1FWbUV2NDdHTnJzakdJbXY1Q1hOS1I1dmpyd2tkTTgwMTlhaXl2OWIrVnRNTjFqSGQrdGFURmk5a2tvVTF5TDNMSkJCMkUzZUMxOU5kWnZmYjdMeVY1ejFLVHV5MFVjWm5wYnVIbEJ5NVRUNC9HTDR4NzJHU0hxWmc1L04vTEwyOVcwZVZWb2I4aU92cFl4L2ZWalZnZk01S3hLMDZFbUFiUlZHTWVEa2lyZU9VVE1VWlJCMVZ1d1hVK2EwQ05xRWxUcnY3ZklJeGdBbCtUSlUyQmM3ZUtmL0dMOUcyRWlGUytMYXU4eVVQZEViUmlkNlRpSlZsUXEvckhjTUhZd0lEQVFBQkFvSUJBR3JHck1CU05oREU4TkFYakJueE5sb1FPWk9TWkZ2U1VVdFBjQURzWTZnVTVMODdaemdIRWVCcyszVmNFcGN5ZnBGeDJvbEJCMzlRN2ZVdTQ4MTJBL3NvdXBYNW1odWlGdUtnNTNCREpydUJsSW9DMmZQK1pCV1hCM3pJdmo4emV1TXNkRWp0L1RhakdObVlXRjRzZHFjNTd5aU9RcXZQeXBDWTdwZkhVL0MrbjFEcWk3TWdMWWxQVWQ0bTFLWjNNSXZBeGI4Q0JnNC9MNnFycWlNV1drQmJSZUJmMFdxM0VhTldFMlNxRU1qY3AycW1sVWlXcithLzRhbUFUNUxGNjBzYUhPRVY1TGpWcUtSMndtY2hrSVdSeEFjY3hsYm9xa3A4Z3hEL1I4YjRIeG1kam82QjF1MFRnSVJ0Y0d6b09WeWs5TGpVUHpTcEZHN1Q5aE1LeUFrQ2dZRUEvOUI2N1BpazhKTkpkU0pnVmVxeTNuLzU1NURETUk0czFHaTczeHlSWm9LNU50QkZLS1pDZkdGZDNNQkVLYjBuNENwK1QyZS9HS2d1bWl3L25SUWRtUnYvVWM5NE5QYXpidmZmSmdqNHYwalQwRFFTVVBiZHRUa3kyY05kc3EzMnpxaDBDR05hQkozRUN3bGFqbDAxUTN4UGdKOXErdnU4MGFkRCtReStrMDBDZ1lFQXh2WTl1UzRTL0FIVlFrNDZBN0VyQlNtRzdRQURvMjJNRU1RWXZyMVpibXRFUmxZaWErbm53MHExaERuM1NXRFZkeUlSZldGUEdHRE9HTEdLbTA5L285VnphQmRaL0RnWm1hWStjR2VoZ1lsekdpdEtnMHlYSVZDc1p3SE9jYVV3Z3VDMmZGRDRjemx5ZUtGdElFeXN3YUI2M2M4MHNEOVcwY1FNTnVpZlRXOENnWUVBK1JMQ1BXeXpHOUlzbWJJSTNsNlFIZmU1R1BCb1BDU1NIWmFFSmU0bzNBaTMwVmpqblhxVURZcTMyeklRckJzU2NqNnRrUjdRZjI5eFFJZUl3S1pQVXo1aFVBU1RZKzQ0TXZtQStnV09QS0RxS3pRb0NWRHorWGxodTRsdTk0Uk9aRlM3OVZiVzFOdlBmM2R5Qmw5V2R3allWOEhnWmRNcHUzQUN6TURONVprQ2dZQUoycnhuNVo1UEdSQWsvcGJsQSt0cmtBajh5QmxtQ05EOUs1bEdLVDY2dDFsa1duUE9BSUhZTEdVZExYblFDcG5JRXNubStlRGZCanh2QUt3cTBSOHpVQ2t0S0tydVVTRURlVFp5ZnMrRENQbklmQWh1eEdaZjRnMEg5UkR5bEFuNUVZUTRXQkpXTXF3MnlWZ01WMy9lLzBIV3BxS25jQnV1dkJVV3l5TEl4UUtCZ1FDYlhKcy80ZkhhWWltVm90SzJPdG5EMUh1dTRUZUhoU0M0bkw2eVlGa3Iwanhoc0ZoMG1TYjBxRXN3NjlCdkNZZFdBZnplWW96M0luNitYVXJVRUU3OW1wQTJ3ZTZPbnNpWVBTZDNUUHBCaXFYeW0wbno5Z1dsclJvUHBMVjhHMzhxbEZkRmpvQW0xVHlDMi85WmsrVmxvQjRhM1JSMDJWVTBHY0trblJibW5RPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0gyUHhwcDc0Nkg4OXRmd1ZSeDk1TmpQTW1iL0IxK1BicncvWGlpd043WEcyREFzTENHaU53Rm5FaTlkRnlZU0xlU2VJOUhGMkhVRWRJY21FS1A1ejA3QVpIUEVDT1IrK3NQTDJzZC9vbW9RdWhjTDZJRnp1a1A5OUZFK2x0K1htTGVWeEU1UkFSMktUeXZJSWRVQ3g1Z2poUmFXWVVuRjVKZXdWTk1aWEUwbEFoVUFnQWxDb1BURmNYTmFDemRydDcwS0hka284Z0VDZ1lBZnBGODlXbHU3SDJyUzFxT2VyVVZWTHJhWkJvYU1VM0tTdlhyUGdEMGJhUEdzbE1pWW1Fcmkxd1NKYTFuQlFpMUtqVGRrN2RWSWJ6TEE4QWhZTG9yWTNwYzhRakcrM1lmSytsNmU0dEoyL2JNUzJaSGRYVGNpR0kvWDhSSU12S21uMkM1RURYQUp4R296bE9SUUhsOEthc2ZveXZIRi9OQUJYMjZmYlVEK0R3S0JnSDEyYjNRZ2p1dkp6UFNJT1FxUWtRekRNWE5Ga3RHcFBDWmJNSk1ralN2TzlTRTlHaGFuVVUxdG8rMmI3SFIyOUxxeGdwU0Y3c09TZFc5elZpT2NRS21EV2tXMUo0SjNhZW1ndURkbDFmcFFpY1FncGhyaXZlTTkzMUNUaXJ2QjY0Y1lNRGtYcDVybWZ4eWdpODBoTCtxOVgwYVpJcGxQM2tETThQVGRLYXc0QWhVQThFUUtSemxkcjYrdnVPcmhzRFRjWTVqODNkbz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUQ1OFJXWUEvQnU1QURmRkFPaUNoTWlFdGRzWTNkYlpEZnJCS0lTVmJ1MW9BY0dCU3VCQkFBS29VUURRZ0FFWDEvVHIxZzZUcFdLZm1hbVUyV3NMYUNJNXNVK0FSeHF1bUdibWlDbjhyQnEyMjg0a2pXbVIybzRFV1ZIWGhvYnJQSWtWU2RiSWFjRzZwTDFQSWVocVE9PQ==
    !
    aaa userlist usr
     username h
     username h password $v10$cA==
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
     hubs h
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
    logging file debug ../binTmp/zzz41r2-log.run
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
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    logging file debug ../binTmp/zzz41r3-log.run
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
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
    logging file debug ../binTmp/zzz41r4-log.run
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
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
     username h
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

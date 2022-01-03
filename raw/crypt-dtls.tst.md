# Example: dtls test
    
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
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQTBlOUg5OG1XMXZ2QWwrSWNHQTJMZ2hmWjJCeTAwdldKNFA0eTl5N2liZC9qSExvcENDSU4vRmZoTkxTaUFGR2xUdXk5QlFkNWNNUk90L2crdFZtb1dYQTF0SnVKcjZSNmwxVUIyZy9BVXJCOEJPVjlnYWx0WDhRUFdBUVlqa3NJQTQxTUxYcmdzQXdEMEUvV094VDhwNWRUQ2RwZ1FpRzdtb2VxL0grK2RPaW9KQ1ZsMkpHYnY4OThTdmpEUFFpdmdlZEd3ZVpDeTFsQVhpTzVZOHcyb0lxZDFIWkl1aERHM01VelRYbzFTMy9EUE44bTJ2SmJORTZ1MFJvcHo2VExXRGZYeGtmZ05uZExGTkZyVURZR0ZXdGI5TVNXbGF3ZGhTMU5IdDRmREUvTnA1TjIwb1AweUovQmZLV2xEK09QTDIwTWlFMnYrdDY4c0tHT2NJVUtrd0lEQVFBQkFvSUJBQU1sU0xqSHhvRFdLTjZkdnJvRmllK2JGK0tMRzVLRnAxazl0ZG5LVkE0OWFwUEZubFBHM3RySEhsTEIyaU9URlowSEl4WHVOTDJoMDJRaVRoNDloNjQvWmk2Y25nV0p1MlNGRzQvKzZHelV4Q2Iyb1ZqT0J4dUdQb3lkRXhrZXVySUM3ZjlJZGhGdFBLbGthTnRkeHlOanV4VE10dUNHek43VjVaUCsvZ1dXWitzNzM4RkNZc29PMk84RmR6R1QvdkVaOWtMQjV0RGNNNzlScjBscnhDd2laUmZOWG0xb0pzQ3BQaC9xOXNyMUcwVFp4VzBQZlJsMXdLRmY0S1lUbXpvRjZ3YXNrK2JGUFFnS0JDdmdHV2JpQ0lJZ3VocllwbjduQzR4RnBSejg5VWtrSXpWOE1aQTBuU0V0WjQvTEc0QUF0K25XcGc2WlZmdGpEVzh6dnRFQ2dZRUE3dUc2SHRXdW04RGhXb2N5emVlYWFmV0dBQ1NYaTJIUkFuN1c2dVU3d3dmWGtMQU10R0pwV1Q1c3VpNGNFK3NZUE03R0tkZ3JEQ2NxT3R3K3JpV0ltQjhCa0lQWVdyeC9SYmFzTUJmS2xWTU5VMStpSjYvZ09GejE0UENoays0QkxOS2ZabzRHU0NVd3dRQkRQc2FJUkg0NkVqZ2NKL3MzVmMwYTFaZXo1ZWNDZ1lFQTRQcUZuRGtTOUdqZHRkOU5kbDEyZW5HTndvUTlHY0ZoZ0RhRTlVOWRkanF6eGk2NFA2MENvUVlhT1RZR1dqcGVta0Q4d3V1WllwM2RoV1BIcWhSbis0Z3FBMU01SmJZbS8weXFwcWRuZFRJWFNLdkEzNkRHMmxNVytySmJkeVFHRlppZmdnY2ZqVUJUQlR1WDZOZUZMOC9uWmhoQ1BpaDY3c2dsQWt1OFNIVUNnWUJUMTVJVnBIWUdZS28zdGVBVStNYnZqYWNjZ2J0V3hsd3ZmZ2s4cEh4WE5YZHBad0R1aHVQbTJNd2NoSGFDWHk5QW1HcGc0V2dxZWN5T29DSzN5S0NxazZkZTY0ZVNRVHFDWTEwSC9ERzBPMVFnQVI3T3d5SDFabHMrT2ZiY0R0c0d1bDRNQnFrWnhVUFpXWmhBZmpueG9FUU5oUGdNNkZWQm5oMWUva0c3M1FLQmdITDd0MFBUNjdzY3lZdkZtQnFSeEJicWFIQnRFNmxSSzVyU3dudDUxNk93ZHVjb1E2VFBzTk5KZ2llUlZBZlRZenhsVUlueXpjOFlMZnFadDVkV25KcHl5ajR1ejd0VmNITDA1UmNONGhPRXlWK3I0SVNxOEZidk5vUmttZGkzZ2FDU0E1djZOZ2NFUkNvZGZoTlQ2MDgzYStYREtrQUlnbVA5eU9SMmZzRnRBb0dBTjIxanN4aEJDb1k3OUVteVU0SmtZNG9ZckpkOCtvNlk1cG5qTHliMlczVTJmeWo3NW5SNWRkN1pTVDB4bGhrWXQxTzBYT0s0bXpYT2VlMTNxWnZNc3B0aVhtem9GRTI2QmZLSGhaQ2NwVHkvZDVQRllJdjFhZ2s3M1FjQlFoQStIaitDblkvSjllZjliTjdQZlFMSFdwTm5URXgvU0ZlR1J3d3BjNmdGNk1nPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FERkF6enZFeVFXYWxudG9kSTErcm5mU0hzMjczdzgwY1Y3YjdwNXExRWNXV0Q5VU1BZXdHMUdnWVFRdWJUYzZRKzVJN0J6N2dsOWc1KzYrcU9lWXZXT1pMY1dGR2t0b3dVckMwekxodEdaam9ld2w1bkVnQTB6MXBjWXhIaWZxRHFqR2J0Q21rMGR0Tlc5NDNCanhCSitDakV4bUplYi9ldUlNb2VuWlQrN1pRSVZBUFpFejNhUnQwWXprVjQ4RUs5amJ6N0cvQXQ1QW9HQUx6eFRpbGQ3dEF4cHBBcjUwdFFxaGZTYVZmUjZSeWNwUkhNbDNKa3VrOFAydmNPMHFoekJ5d0RJU3RnU2xFLytIeTVJdjZVK3RWdm5KZDlOTkdXeElJU3B0b3g1WXRUQ3hNOXVIRFdDa2xkdG14ak9raUJUSmgzWVJ0M3cycmsrVXVEWkVCZlA5THo0K000ZC9YNWYwNGNpRmZNcEIyVks1eEhQSVNJaFcwOENnWUExZGJHUHpPUTd5eEd4dUM5SHd6bXg1aTB0ZXZHZ1NudDJ1VktsQ0VpRmVxWjY5amwveWdqYWRnaExPMDRpWDdRK0FuRFVvY0VVYTdWYmhZV3NzN3ZsNU5sdU5EN2JIMTJNY3Y5alJMWGVEeldBZTJoUnBlYjB5cC9BeFNvVUU1akFrcytFSzdDNnhBU0FIdzN6QTZnN0Q5MDQ3a05VMmpZVlZrWnY2MjU3N1FJVVhVYlFRVVJZU0llcDlJd1BMVnoram0rcTJlYz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURNdVEzaFJSR2lCSmpYeEJqUlV0dm5hWTV5MllmalMxS1ZPVENzYVkvZG9BY0dCU3VCQkFBS29VUURRZ0FFbmpOcWJaeUEwREE4L3BQd1p5cU1hTVdINnJIME15VENqd1dTdkh4NDNyOTZkOERJL0dSckFqZzc4bm0wUkMxYUxoSHBoVXJ4WTJGdlpDZ1VjL3BxY2c9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZUQ0NBaENnQXdJQkFnSUVNSllSMHpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01qQXlOVE0xV2hjTk16RXhNakk0TWpBeU5UTTFXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FERkF6enZFeVFXYWxudG9kSTErcm5mU0hzMjczdzgwY1Y3YjdwNXExRWNXV0Q5VU1BZXdHMUdnWVFRdWJUYzZRKzVJN0J6N2dsOWc1KzYrcU9lWXZXT1pMY1dGR2t0b3dVckMwekxodEdaam9ld2w1bkVnQTB6MXBjWXhIaWZxRHFqR2J0Q21rMGR0Tlc5NDNCanhCSitDakV4bUplYi9ldUlNb2VuWlQrN1pRSVZBUFpFejNhUnQwWXprVjQ4RUs5amJ6N0cvQXQ1QW9HQUx6eFRpbGQ3dEF4cHBBcjUwdFFxaGZTYVZmUjZSeWNwUkhNbDNKa3VrOFAydmNPMHFoekJ5d0RJU3RnU2xFLytIeTVJdjZVK3RWdm5KZDlOTkdXeElJU3B0b3g1WXRUQ3hNOXVIRFdDa2xkdG14ak9raUJUSmgzWVJ0M3cycmsrVXVEWkVCZlA5THo0K000ZC9YNWYwNGNpRmZNcEIyVks1eEhQSVNJaFcwOERnWVFBQW9HQU5YV3hqOHprTzhzUnNiZ3ZSOE01c2VZdExYcnhvRXA3ZHJsU3BRaEloWHFtZXZZNWY4b0kybllJU3p0T0lsKzBQZ0p3MUtIQkZHdTFXNFdGckxPNzVlVFpialErMng5ZGpITC9ZMFMxM2c4MWdIdG9VYVhtOU1xZndNVXFGQk9Zd0pMUGhDdXd1c1FFZ0I4Tjh3T29Pdy9kT081RFZObzJGVlpHYit0dWUrMHdDd1lIS29aSXpqZ0VBd1VBQXpJQUFEQXVBaFVBc2hzWnFZMHpRcmkzNno3NityOXpBdW1Uc093Q0ZRQ0dURTZGVnMrREVrSVdYck44RXo2OEwva3BGZz09
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUjMzR2NCTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNd01qQXlOVE0xV2hjTk16RXhNakk0TWpBeU5UTTFXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTZU0ycHRuSURRTUR6K2svQm5Lb3hveFlmcXNmUXpKTUtQQlpLOGZIamV2M3Azd01qOFpHc0NPRHZ5ZWJSRUxWb3VFZW1GU3ZGallXOWtLQlJ6K21weU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnSDlLYkMydUxxQ0FhQ2pzWjB4TUxoRmtaWTJmQU1aU1l2ZGtVTERFd2oyOENYeEo0d3FIaFNic2l2b3FBaEhEZHBSUXZKdVpxeTUxTzd2OW9IOXlTNGFVeEc1R25ReE8yQnNtMlErdUJ5T0YyeFgzQ0RhNnNhRmNqbXZQaVJleGFtQUZ3UnBFSHY5WVJWVTNOY1cwdmR4T1ZwVVg5ZjhBdDdvTE40YTBLOGoyNg==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVkYzcxRXpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16QXlNREkxTXpWYUZ3MHpNVEV5TWpneU1ESTFNelZhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTBlOUg5OG1XMXZ2QWwrSWNHQTJMZ2hmWjJCeTAwdldKNFA0eTl5N2liZC9qSExvcENDSU4vRmZoTkxTaUFGR2xUdXk5QlFkNWNNUk90L2crdFZtb1dYQTF0SnVKcjZSNmwxVUIyZy9BVXJCOEJPVjlnYWx0WDhRUFdBUVlqa3NJQTQxTUxYcmdzQXdEMEUvV094VDhwNWRUQ2RwZ1FpRzdtb2VxL0grK2RPaW9KQ1ZsMkpHYnY4OThTdmpEUFFpdmdlZEd3ZVpDeTFsQVhpTzVZOHcyb0lxZDFIWkl1aERHM01VelRYbzFTMy9EUE44bTJ2SmJORTZ1MFJvcHo2VExXRGZYeGtmZ05uZExGTkZyVURZR0ZXdGI5TVNXbGF3ZGhTMU5IdDRmREUvTnA1TjIwb1AweUovQmZLV2xEK09QTDIwTWlFMnYrdDY4c0tHT2NJVUtrd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFpZFlvOE5PMHUzOE1nMkFjcURCait6dWUrNVQ1eTlhVEJDelBTc3hhOGFVZHpzNlVyZUdkR1BFcFovSzB3Rk5wRG1ITXFrZ1psSVZrYUFLQ3BtRE1FWVpUeXMxT09ObkFtd2lDL21KYndMRUJnU2wzbE5ZbThVSzhieUljWGx3OFhWZDkrZ3NZUzVHM1c4Um94NkgrOU56V3hKVVNUWEp2MG9KbUh6Wnl6eVRnVVE4YVJxcWhtbzJpZThWdEZna0xwRDhNUEE0eGp3YVNvYSt4aER6eHJPNVVwcnJ6ZFNoS0VER1dQN0RaZVFuOUV1U01Ba1MyR2MvSTMyaStBMC96R3JqV25qa0Q0ZmJNQzVXdTRXZ0dpV2FDU0prZDE4UEdPMnpqU0dWM1hBSGFVRndOUVB1NnlzUTRhbzNJTjQxY2tFQTFwYWR2b2g0QnpxNEh0cVk2QkE9PQ==
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
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    server udptn udptn
     security protocol dtls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     port 666
     no exec authorization
     no login authentication
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

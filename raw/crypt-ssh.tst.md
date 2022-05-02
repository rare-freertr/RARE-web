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
    logging file debug ../binTmp/zzz23r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQWtzRkhXKytmeW5KbWFlRHYrVjEzWWJRcGFtSXl3RTFNTzJ2dVE0MG54ZFJSNHBubVVmRlJXeWRYNThzZThIRnp6clZocVpVL3E0QSt2Ukp3STR4N1VxaSs5MndGdFFZSkdzZGdyQXJPWUVaZ1hYNkhHbldUSnBJQkNkR0NTN2laa3d1L1pTMWp2UUM2cnZzdXp6bmFIYkJEWGwrK25CemdQNW1TY0MwR2hrMTJnQU1lUlVRYi9aZkJwa09FWU1DNFRZUk44cFpjMXpUQzU3aEk4N3h0bkVrWUVrWDAyOWp1Ym1NVTNoU0hBZEVieFIwVTIxbGtBbEhubmt6NXBmOGxBczBjOXNBUzJoL2RuaHdMdllvYWlxTUpUTmpTTUVKYVFLcGpISy8xdkR4QW85SDlJVFRBdEVRTTFyOEN0Z0g2ZnZNWjZ5RFFnbFFVcm5Eblk0VGgyUUlEQVFBQkFvSUJBQlFXcHZqN3ZTak9MaHl5TU1jMnR4L0Z0S0dlWFlvYlNxTWJyQnJOR0xPbzA2aXNIbTM3RllMZnlOV3U1VVpPa1dhclIzb2FOd1AzNHg2b2huY25STDVVNFFjblgwU2ZWZUczaHhFbHpZZzZPZml5V0RZVUFCZVlodEhjUHZTMGlUa3FzNEZiRERzVC9YbjBZanoxazFqYkJ1M0ZOMmRSUUpVVUpZcDdiMWcwenVKUEZWTlBLUEludktQbGNMZE16L2t4VzRxUm9mVllxdStLMVBvOHhsWGlKMGJ2S284UnlzTWRYM2hQT0ZVS25ualpCQ0ZmSXB0VGJ3WXFoSyt1bkZCRmpUS3BZb0haellMVmNHeTNvampoRTVFTkdoZ2N1QmVjbFV5NTlGVTRUcnYxRUsxRmxxcWtqVkFRTm9lTmZqcnVLUm10Q29vRTMyaGZ3d3kwNGIwQ2dZRUEya05UUWVwWkJPOG4rR3ZKanJrTkUwZDd3RUU2WkFlcGRrODN0Ri9walVBYnU3cmVPMFRxK3RsNk43VHVITk95eHRpRXVzNVhCODZENFZuOHZCMzRjSTJlTDRtTXVXVnJCclh0amNCWnlJV3ltdWNISGNzazNSaFBKYS9tNThJWDB6d3VuOG1RWlNHWkp5a0Z1dC9rejQvbHZPTlBzald1MUtaVmZXRDRsZ2NDZ1lFQXJDRGt1SGxFWnRYTkRIL0ovSmpLYUtzLzYvTmI1bGtvUlJXclpnK21kUm44d2phL05CYnZDbW5ZSjBkaEFwMDJTYU9WeUx1QWIwQmpYNzFvQ3o2WDlJM0pHSi9rcENoT1BhWDZoUjVmK2xkQ0Z2VmxMVFpEaGFic3NVWWNma3FZdmpaY2pEZlEvWW4xTGI1MXFUV1JTZHJzUXFPWHo2YkFidUdpbTRIWjBSOENnWUJlWEE3cGgxUVc4d0hYdjFtekwwTjgyMEdmKzFNd0hiUGdweHpSQ1VvaU85NEJpaWM3Zm04TUpldFZuQTM1UG5paXlNYVJNRldsMVYxa2xvL1NFQzd4RWZpYVdxQVJJc3hqYVZHYkg5WncvNFFZdmRwd3dmdGM3bjZCTDR2bkZCMVN3RWp6NGFOZ1pXY2Q2L2xETWpwc2xheGZ2ZklkZkdIcUkwTUFZbVQyRHdLQmdBNER2NXVsaEFRN2RDNklXUkhQL3VyMnhvV1hrdXYyWm1qNWtyTUVvekQxcExiTGJsWDNhQThZL3hoem4xcHZJblJzZFUyYXRxSllRNzhQMU9EVmY5blJrWVlIdnIzKzZoL3EyN0xxL2pXTDFUMjVUVHVaSjNaQ1dSTTEraXZ1TnZHRnk1TS9HQzBNaG9IcTkvbUcrd1ZnWmN3bk5iMGFmcUNJam96S3pjbFJBb0dBTVBaa1pTRUZzQ3ZwdTluVnNURDE2bDJtYThpbElIcko5djZyWXpELzk4NUJTQ2VBaGU4NE1uTHRxL3NybVc3THdkN3BsVmdiV1d2bWVjcHVlK29JZWhMWjlmUmtQdDc2V256REw5T2RxTzlUVEV6SGdqRlVOZXBJM1RNUmd1ODQzMk9PWjA0TXBnUjQwdU9GN3FYaGhJYlA5QXlxSVgxWVQzZ1FGOTRUSmhnPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0hreElRWnMycmczSUNWZExzZjhCdzFmRkdsSlJNUUNtazIvV1Jsa3kzc0lBNEpUVGg0enBubGsxZTlsd0oxbDlzU3lta2hjSFkzTXVha3J5Y05MOGE0WE1OTjEydW9BeGlhZHBPTHVCczNUREt4QnZYbk01SWNFV3FZVkVCU0RBdVF6RzNOWndOVVJBcHF5bTkyMHJqK0FCak5kNmVCOWJzdytkUitwaENPREFoVUFoNUl4Vktpcy9RRzFDS0NiRVdiZnRGMFBJS1VDZ1lCMG9IbzBSbGdTUFprdWFWWjBsOXlUVStuL3BKUVBvZ2RiN3ZOQnJUeEc4VGdLZFkzN1N3V3VRa1piK3dKcVJFem1xQ0tIMkgvMXFUc0srdENubllwRGRQTktXZW1WY3VWYWxodk1TSWczd2ZtaVBvQjJkcm0yU1VUWGlwejRPcERpOGpOaHk3OHNVd2EzRzMxU2orNXdZbGlEY2NNYVREY2I4RTFpK3VYVzdnS0JnQ0JDK0tvNllyRTFTMmhWb25zTmJEdUNYalVEL290Rm81ZUJBckNHd3NWVWVLcWJZeEJvS0xIdFZKcjNyZHpsd0RCRzlvblBDd2dKY2ZFd1Z3cmVJbzJWdGZVZnVrYmdoWGxlczJOdDBtenp3VXdHMzZTZ2p3ODhEYTJUQUVMb3hrbGxHRWVQT2hZRmlCbUVwN05pQjNnU01YekxiRE50N3VBVkJjdnhybGVzQWhVQXZMN09nbjhqR09aQnY5NXZwalhsbDhrRGxWOD0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMW1CZm1IOVJxODkycmx5MWp3OXN2dzFsREZPYnVYYVNrcEdvUHIvaGFlZ0J3WUZLNEVFQUFxaFJBTkNBQVFOWFpxcFg1K3VQK04raEpEOWlhU2NsNkZrVDNKMHF4aHVSQWRHbDJza3pMZ3dIY0ZGR1RXSUdJdXVXZjJXTHNUUE4va0MzUGJZekQzUGMwZTdSNlc4
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
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
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
    logging file debug ../binTmp/zzz23r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
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

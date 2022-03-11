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
    logging file debug ../binTmp/zzz29r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCN2oxWjYvZTBUS2h3MVAvc0QrYURZWnJDZ0t3N0VOeGhXSmxXd011TmdMMitMb1pabmx1ODJzL1ozQWw5ZG1lbmpDZXZ1ZUI1UTlZbi9QUmlZSFVwS1NTQXdtOVZLZmxHV2tVNDRDa1lGZFpOc2RXOTZUZmtzVTR4OWlGd1FZTE1abDMxM2JVZnlncjM4aDdJRVpxL3pOTUt5aXpQZU8waVRRQVFGa3ZSdjZ1UWlteUxhY0hJUFJpdmlGMUZPWnVkZlNCM3hwQ2tQZG54dnRFV0R6b3ZtNmJ5YkRVdy9xRUVSUUR5SkZTV2NFcVpJbm5SRnAzditBQldjMDd6MXdhNFhEeUtNcDVEZ0FFdk5rZnd0YWdEeHp6cDFUT3FGU3VLVXBLOU4xdTZNWTJVYXpKNVVnUTFqdFpUOGt0RDFOcE1IUWZYTmxCUHBldjBSZm1IL3dYZ2xBZ01CQUFFQ2dnRUFhbng0K3B5VzBmcHJ2eFM1MzQ0bXFmbXVaUXRXdVpJRi9sRWhiaTRkT1lzSUpoMkh3eFVZYWx1a29LSkIwQ2hTb3VHdEhLTVc5WXozZGlxUVpLQnhveDNzaVJmME5UUXlXb0kyR0NQNmZyLzY0dkUrdHZnMk01WjVzTUp4SFloSk1sZ1Z3SFJGR21MRkc3dFNsMnBzWHp6c1F2V25LUEtNdEtMcUZHZTNGQy94ckEvYXRGT0ZXb3JZTW8veEs4Wk9NcEZ5bWNrQVNXSHJ0WUFha0Z5dVdJYnFjNzNQL2xTQllCa29VbGRQR2g3ZlcyTDd3TlJoRVZTdUMybi9XaE5ib3dvaWMralZCR0hoTThsZkV5d3ZMWXBKbDUvQWZhTG5UQWpyTGtRc1JxdDBQYUNMblNmNlEzUkN0cjdVNFZQS04walRoUE1OS1BwcVNnM040eHJpSVFLQmdRRFo5ck94aWg5SmFORDhPdnpFdkx4MDREYlc5Y0ZiRndSQjN4TjNwaUIyNlNlWTlVZTNCT2JIOXYxcXJMc1VaVTUyZWM3RUlBYWhGWTNPS2NTa3dhR2tqcklqWklqVHNqbWh6ZTFObklUd3Zzbjg3SHVuaEcwZGt3YXRuUERWZVRsK1NxQjkrdUw0QzQzVHRGeXVvbld6cXJDdVFJNDhtejdFR1lidm5BM0lHUUtCZ1FDUkh6ODRWSkp2OFF4VklDY0pqdlpZRTdaZEdmbDNlL0pWdWU4REdrQk9aUFpPOHJOZ2lMZU1XRWJhRHNxSHRIOTUrTkVpSUdXeFlNYTdQc28rRURBemtMUS81T2t4UUNXTzdYRlZkOTE2bEFsV1R6bllGSHNzcDk5dXBzTTJvS0R4aTdicERPZ216QXRhaHBwMVJHb0JOYjhZU1hqd1ZGTUdPYVdHMkZRaDdRS0JnUUNma29uRDlRY3F5MTRWQzJwNjdtSmFmcnduYkF4L0Q3N0NLdnNwb2FvcTVFOWxJRTI4cEE0Qlg4WHdEejEzbFNONGdYenJBVGRaUDFwdUVRNHlRTUNDcFNXdDI3Q0FxLzZkZ3hHMHZGNW5rb1oyY1B1bWpNRUY0ZG9GeU54WXJVTjJQbFI1WnZBOEFObDRvSmNxRXk1d3R3cGF5RkJaOXA1aEd2ODY5Tmp5SVFLQmdBSmxXNnZZYVpxRGhrcVpmMHQvR3I0VmhUdEFSSWdlZWIvRWxCZWZCVlRHQWZNSHVzSnJQMnlId0pPMURzN3l3ZkFIbFp4VW9Ka3ZHZGpaam9rN3h5L3l3YWNVWm0wenUrc0NMSTdXcmNkcVRrVW9oYkgxbEpzR0lvQTNMSjNvUlAvMzZJc3NkV0MrbWFsaTg0WGdIVWZyMVQzWGFMRy9FcWZWcDgvMEhsOTVBb0dBS3o2TjVkMlRCUkFrMFE0cHhveFpVT3ArYjZ5QTZVd25yNURaS3VZcVduYXo2T040Y3JsdldxYitudWQzZUZMSFUwTjUxcXBtS1dBNFo3YWR5QnQ2SGNzTTZ3UnRhYzNpcXNJcEluZkd2czdjbmowVkRQZ256Ujh3eDkwWkU5YktjMG4waVd5UEVZdlIvVVUwRnJKVFQrY1ZNVkF6TnNZNGs5R1UyZTZqWjZjPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0R4T3crbU9yV0pNaFRzcHNoUk5sd0swTjh3SWI5S2RSZDQ1RWhQdEo3U3Z3RjBCQ2NEK3JZM1ExVVpuV25EWWJybHpmZCtCWkVkMzFoSURneksxMk9kMk1VREs0enVGcjBtUGlISXpGZ1l6MEJMVjhmUW9ISlFveU1aY3NGRUJUdHNQZzYydFZ2bVdpZ053QkFvTjI0NXM1NjZQZFpNRE5JNWk3NUNGa0UzckFoVUFxeFNRWGVrU1lENE13NVltSWw3L3FTMjBGN0VDZ1lBY2hPQzl6clIyMURGSlVSRlhwRXI1TTFkWUtNTlV1OHBBR1dRUVBuUVpBeDBUUFhOMjRob0w4dTU4eTV0MjdEUlNQb001T01md1RjSytCS0ZKemY5dEVDaTlIUjduQXZla0tKdTVzRnl0NXVBMzRITjI5Vy9LTVVxYWhydWgvWVFVTlZUalJhQzkvdVNqazl2YjNMeU5YWklPdG1lNzFTK1NIdU5JV2YydGpnS0JnQVkrNEROOUFhQS9rdWpBZDhmT1oyajZlMTFyNWswTG5ZNTJPRS9QYVZ0ejNBNUxVaVM2ejVDd0Jjc1lqbmdldEtTSXpvdmVaVDVGOFl5Rm5TbVhZT2tvZkNNT3QvSWI1MU1zeXBUYVcyVGc1cTEvaHJmV3V1UEFkREZIeUNkcmpFaDI2NWZEYTJVMkNZM0Z2RlYxUkRvZEozdVhuRklLRGZoWUJ2Q25EekNTQWhVQW16QkhxeldUbVZLcmJvNktWTTFtSVcxcllWWT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMjd0U05RUUFYbUVjemExUDVLTzcwbWlVSWxUK3dNakgvUkJxR21wQ1hLZ0J3WUZLNEVFQUFxaFJBTkNBQVE1SE5wL1BlbjB2VEVzQm5US3FsZU0yNm9BcnpYaEd6R0JKZWkvamE4alY1cnNLaGJsakU4d0R5VGhPUWZtYTZyT2RJdTlreWpWdjErd2hGTUpOSEF4
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVFaDErRnpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOekl3V2hjTk16SXdNekEzTWpBME56SXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0R4T3crbU9yV0pNaFRzcHNoUk5sd0swTjh3SWI5S2RSZDQ1RWhQdEo3U3Z3RjBCQ2NEK3JZM1ExVVpuV25EWWJybHpmZCtCWkVkMzFoSURneksxMk9kMk1VREs0enVGcjBtUGlISXpGZ1l6MEJMVjhmUW9ISlFveU1aY3NGRUJUdHNQZzYydFZ2bVdpZ053QkFvTjI0NXM1NjZQZFpNRE5JNWk3NUNGa0UzckFoVUFxeFNRWGVrU1lENE13NVltSWw3L3FTMjBGN0VDZ1lBY2hPQzl6clIyMURGSlVSRlhwRXI1TTFkWUtNTlV1OHBBR1dRUVBuUVpBeDBUUFhOMjRob0w4dTU4eTV0MjdEUlNQb001T01md1RjSytCS0ZKemY5dEVDaTlIUjduQXZla0tKdTVzRnl0NXVBMzRITjI5Vy9LTVVxYWhydWgvWVFVTlZUalJhQzkvdVNqazl2YjNMeU5YWklPdG1lNzFTK1NIdU5JV2YydGpnT0JoQUFDZ1lBR1B1QXpmUUdnUDVMb3dIZkh6bWRvK250ZGErWk5DNTJPZGpoUHoybGJjOXdPUzFJa3VzK1FzQVhMR0k1NEhyU2tpTTZMM21VK1JmR01oWjBwbDJEcEtId2pEcmZ5RytkVExNcVUybHRrNE9hdGY0YTMxcnJqd0hReFI4Z25hNHhJZHV1WHcydGxOZ21OeGJ4VmRVUTZIU2Q3bDV4U0NnMzRXQWJ3cHc4d2tqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRjQzUUhENEtIN1VOTlNOWndlK1IyUVVnOVNyQWhRU0w2RzhJMkRNYTYvaGlpUWVJemw4VEhhMitBPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUndRakxvTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTBOekl4V2hjTk16SXdNekEzTWpBME56SXhXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRNUhOcC9QZW4wdlRFc0JuVEtxbGVNMjZvQXJ6WGhHekdCSmVpL2phOGpWNXJzS2hibGpFOHdEeVRoT1FmbWE2ck9kSXU5a3lqVnYxK3doRk1KTkhBeE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU9vRU9qcDBPSW1mWFV4TW1ZUFRJR1IwekZOLzAxSE9ORTNaVGM1TzhoUWVBbDhWT1llMWJyNklEb3pab25DMU9mSWhYYUFWNWhzcXVISTQzeDl3S2RmTDRsL3E5NElSb2dTWTAxVUIzY3NmR05pMzB2dy8yNWc2SkNMc0xDRTJJbjE0ZjArQTIyS3BwTlhnVWkzNHgxNEFINVlCVVRYOFVHQ0pKdTF0Unp5bHpBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVOeTdYQ1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFEzTWpCYUZ3MHpNakF6TURjeU1EUTNNakJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCN2oxWjYvZTBUS2h3MVAvc0QrYURZWnJDZ0t3N0VOeGhXSmxXd011TmdMMitMb1pabmx1ODJzL1ozQWw5ZG1lbmpDZXZ1ZUI1UTlZbi9QUmlZSFVwS1NTQXdtOVZLZmxHV2tVNDRDa1lGZFpOc2RXOTZUZmtzVTR4OWlGd1FZTE1abDMxM2JVZnlncjM4aDdJRVpxL3pOTUt5aXpQZU8waVRRQVFGa3ZSdjZ1UWlteUxhY0hJUFJpdmlGMUZPWnVkZlNCM3hwQ2tQZG54dnRFV0R6b3ZtNmJ5YkRVdy9xRUVSUUR5SkZTV2NFcVpJbm5SRnAzditBQldjMDd6MXdhNFhEeUtNcDVEZ0FFdk5rZnd0YWdEeHp6cDFUT3FGU3VLVXBLOU4xdTZNWTJVYXpKNVVnUTFqdFpUOGt0RDFOcE1IUWZYTmxCUHBldjBSZm1IL3dYZ2xBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCYUtGQWE0S0JQazF4Y3MvMVJaYVp5d1FSSkRDeDFJNTlVeEk0R0dtWUZpYkJWUkk2ajFTcGhPbWJ2U3hNdkJkUlpQK083RjZVWE1xc1FaemUvelI3Y0h1bnRYeTNPNzNaWFFCempZQjg1V2M5QzBDN2srMmdVWU5STm5lN2tiTFhwakNIOXF2OEl3bXZUTlpBc2RERFgxdnk2aUNGUXdMN3Z1aTlOVWZTaC9DK1VWYlltelV1b2kwYUhkdGtkYW9ZSHV3TXBycmpqNm9rZ0xBMlluSUFxUDlSTlFIMXFBSDZMUFVuMnF6eFkvTmxjSk1meVE4LzFPelcrQ25ENHR3dFVUY2h0Z3lRMWhtZTRNSDVWVUYyZ0VGbVZDRm5NdjV3NjdpbFZJVEFjSDR1djE1VkNQZGV5alFRaEdRMTRtU2N5Z01uU2ExVG1mdGlaM3V5dFpJWWc9
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
    logging file debug ../binTmp/zzz29r2-log.run
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

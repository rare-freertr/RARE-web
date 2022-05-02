# Example: pvrp tls encryption
    
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
    logging file debug ../binTmp/zzz13r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCb204YXpFU1BjYU5aRUtGTERob1VaTmY5aGp4ZHhtME5MandoR2RnOHF0ek4yd0JPaXpoeXFYSmwrV3Z0VUMxSmtwNkVhN1ArRkNnZTgxeXVnaDg0KzRMRUpuSDBrK0FiZjNLLzF6aVhFcU1iODdBbnBYWFBMTnZUS3pwMmlyT1VSbVNCSVJaR0FjQit5dU5EeDlmRlN3RUUzOXYrcWNWQXh1czc3dGhDd2RGdElQaUZONkV6d240cUM0V3NsY3hvZ1BJZEdXWSs5ZUtYdVd6d1c0cU10RmxMRjB4dXFuUmU0SkhOdGxqZy9QTmVvdkg5Vm1OT00yZkVVWStud3ZBZFJrTUFiQVNydzJMRFR2cW1oeXZpYmlFU25NM0MzMG1OYSsrcXFoVHRCUnFGU21zV0xxKzlSTnFkdm1ISVhtcW5INzhSTWZuRFpqN0NCWFZjblZvR2ZBZ01CQUFFQ2dnRUFCYlRScnZ6MVh0V2RNcFNjaHl2MFlMNndVcXNTbFZEcDU5cENrazFvWUdVaitvdFp4dHpGZFltZG1lWHVwZFFFUjVkWlUzV3dMcHF3ZDEycGRKVlQ2OXduN0NWTU1sTVJWTzdkN21PemJibmpPUExMUzU2Y2JXNXZCZzBsVGpWdVBYcUQ1MDFjTll4b1BrQ1VyVTVFUHNaY0NHaUI0OU5RazVYa0twanc2aDhzNmkxdHV1VXo2S2cyaVVYeWNBTm5zZU5Nb2duQ0pPaGRvYkFYbUZ0d01uZFVtdnhXaWtmZEJJSmUzaEJoWkNjUjJzc3pKcGpCV0lxZnUvSjI1dnkwanI0TkxsNSszRklCVFhaWk83cWJkRW5Md0N6V2d5MkpjTWdxemhGNWFDN3NvMVZ5RU41bjNYSmVOMVpjayt3UHFiUlJCMGF5SktIQXZiKy9SNURLNFFLQmdRQ3BnTjg1MFdjS0poS3ExclN6YVkrSEdSY2lXUGE3QmJtRFBWQUhwV0NrTVhER3pDbVdSdVVxZERGM0g3ajNwQ0R3SXN6WXMvbzdGZStlUVRlK1orU2UyVWdrMVkvcFA3RkRJTy9Iejk1RENZOHRKS3VDWFMyaVRyWEZVem5KWk5CNjUwbU1EVTVBVmYwbkFyeTBOUUlzTFJCSmRDNkJ5RElUdGN2TjJza0JjUUtCZ1FDZC9WYS9YTW1ISFp0M3pqbkZhZnJ3aHdvQXBzQ05vbkZDTWdlL1ZOeXZKWC95ZnUzdzVxbE1IcTljT25ETi9vcEFuU0lqaCtzNGZPNitWdjFHLy9STWdySGdWOTV4WlhrN2Q2OUF4R2J1Z2FEZUZQL2x3b3MzbTg0bzU1RE1uUkI2bkxpWk5pYWl2ek01YVNvN0NVcEFuSVY4dkdlYk1PRjlDV2MydGxBc0R3S0JnRG03QTh4Y2JyeTlKT1I4eGdUSk1qSXdNSG5wVlBkenhyQlZSSm1tRU5rN1lZN0Q0SEluYVV2aFVTdWlhVXdtNFhVSVZUNkZaZmVUekEzWlpwUDZMSnFScEltdkZ4bTVNTFdOVlQxM3BkcXRPYytGU3NqVzFZRVBUOGVLUmdjNngrcmtOVjkyOUt6aTNKclp5czJSdEZDNWRHK2dHMnJtZFcvVEhqdlpoVlp4QW9HQVZ2UW1HSENUSW1CelByOHNJTEV4d2N3dy95Ykg5NndlTmRhZldQajE5UmZva2FpMmdNNFRBNmduejlVQ1hQM3BUYUt1Tld3TFZDMitvTmZ6MG0zeElXTVZUMnBOTFpBeDV6NzZIK1Y0MlhCUy82Z0RKNHVwWDlQSzVjeDliNEJLbjVFK01HVVRZcU5sS0FYdmprcVFxWHI4SlNqMHhQOWtPNU0vVVdlS1BKVUNnWUJyck9zMFV4eWNLVU5JanRCclFkajl5VXVUTisxaE1TWkFFZ0d5c1p2SnVHcVpSRU1UaVp3WUs3QXExMGlBZUxyZ20vYXJxblpsOTA3eC9ob0Mybjg0c3FmU0luSFlmNzdTa2FOaVZRYk1LYlRQR3NWb3J2bGdVbmpuaThSV1F5cjJ1ZXdzOUxGQXg0bFhCMkdKVlMrUEF0WE96RHRBZFprK2dyNkRyVDA1cWc9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0U5NldqZ09DQWdDWHhNeUNqSS9uVzVCM0QvSGVvUGgwUUp5Qm11UWk5S3BRTEx3YmdCZnUvbCtRdUxJUjFydG1SUGk4VW41UHVBVjI4a0E5aHdmN0pOWU9Cem5MZVVEZktocG5meVFmd3Y1eVIzbU55NzJzTFFIYzJSMnRXLzJQSlArajhHOTY5ZVlLQ1RkT2pMbU81Y0JEbTdjNlBCQllqUkdJVFo2UE9rL0FoVUFtSTNlWmZYVFlsUStpdHJyZlhpMkNUNENlS2tDZ1lBUzlGNVNuQkZWODV5dmVYbWZ6cG1VSXZ4bm5YL0VCTVVna1pHNTEzYWJFYmlYQzJPaWxqVVRQY3lmcVBmQTh2U3pITDRGMGZkQmkyT1dMUzQ2TGNzamhhajh5cEFXYm5lbHRLUVpWdS9nUzZLNEN2WnFlK2FsUzFhV1NNTFZTbnN3Q1FCWnd4WTlJdXFpVFJBZ3M3ayt1QklVUEU0MjE5VTBwYzcyZUY3NHhnS0JnQWJJcmtyYWZoWmNaSWRjakRrem5QSm9RZ3VtQ3JXaGhjdFFydWtPMDBva3BrYzBjYWwydFE1a0tzdHlHYnJlbUtmZjBDTVdML1I1SUlMam9BLzlIc3NoZjJFQ3FoRjhCTWlTYkNPZGloMTN4MXB1alVRWGtTcWhVRVNtNmRhN2tEK2NmR2orazZKZWYzdFhLOEJFTW5CTE5hU1FhTGVVbWpSYkVZd0hOcEFqQWhVQTNOUVp0WlY4UTh3STVUSmhETkhLdDBlQVNKOD0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMlJGS2NqVDBCcFI3c1AzNDhka3JXUW5yTmZHSU5HVjRtZjQzdFBKSGgrZ0J3WUZLNEVFQUFxaFJBTkNBQVI3L0wyTEV0TU9tZ2JPSmpkdW83WkRmSlNQaXNpM3BGcHdyaUF3UXNnbHRaUUNWVDNteE51Y2lWZ0VvNzZyTDdJWFRKdkZMcFk2WnJTQ0pValJrVlYx
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVESU5URURBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNVFF3V2hjTk16SXdOREk1TWpFeE1UUXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0U5NldqZ09DQWdDWHhNeUNqSS9uVzVCM0QvSGVvUGgwUUp5Qm11UWk5S3BRTEx3YmdCZnUvbCtRdUxJUjFydG1SUGk4VW41UHVBVjI4a0E5aHdmN0pOWU9Cem5MZVVEZktocG5meVFmd3Y1eVIzbU55NzJzTFFIYzJSMnRXLzJQSlArajhHOTY5ZVlLQ1RkT2pMbU81Y0JEbTdjNlBCQllqUkdJVFo2UE9rL0FoVUFtSTNlWmZYVFlsUStpdHJyZlhpMkNUNENlS2tDZ1lBUzlGNVNuQkZWODV5dmVYbWZ6cG1VSXZ4bm5YL0VCTVVna1pHNTEzYWJFYmlYQzJPaWxqVVRQY3lmcVBmQTh2U3pITDRGMGZkQmkyT1dMUzQ2TGNzamhhajh5cEFXYm5lbHRLUVpWdS9nUzZLNEN2WnFlK2FsUzFhV1NNTFZTbnN3Q1FCWnd4WTlJdXFpVFJBZ3M3ayt1QklVUEU0MjE5VTBwYzcyZUY3NHhnT0JoQUFDZ1lBR3lLNUsybjRXWEdTSFhJdzVNNXp5YUVJTHBncTFvWVhMVUs3cER0TktKS1pITkhHcGRyVU9aQ3JMY2htNjNwaW4zOUFqRmkvMGVTQ0M0NkFQL1I3TElYOWhBcW9SZkFUSWttd2puWW9kZDhkYWJvMUVGNUVxb1ZCRXB1bld1NUEvbkh4by9wT2lYbjk3Vnl2QVJESndTeldra0dpM2xKbzBXeEdNQnphUUl6QUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQ0RyMnN0WGFwTHliNEl4RmJ1MXdqY2h1aTlkQWhRc2duOEdUT1ErYnlMckR3NFN1a205K2pMa1VnPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUWs1QmczTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNVFF4V2hjTk16SXdOREk1TWpFeE1UUXhXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSNy9MMkxFdE1PbWdiT0pqZHVvN1pEZkpTUGlzaTNwRnB3cmlBd1FzZ2x0WlFDVlQzbXhOdWNpVmdFbzc2ckw3SVhUSnZGTHBZNlpyU0NKVWpSa1ZWMU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnTy8zdXdOeWpxRjZpVm1vd3QyQWU4R3F0K2Mybm41bE51djltMDBtL3Vud0NYd3hJQzdnWThNcWN1RXpPV1l1WGMzOWJGcG5RVlNCbTRwT1NscGVCbXJTcDVrTHJDMTdIbUgwMTVmd3A0YXJNd29VSE9BcjNmc3FxVzIzenV1eXVxK3dRS3ZkSmRzWm5sTGM0NDJrbVpXQ1JodzRwUmhyckVHeW50ME9idVNRZw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVFZ1RZWHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEV4TkRCYUZ3MHpNakEwTWpreU1URXhOREJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCb204YXpFU1BjYU5aRUtGTERob1VaTmY5aGp4ZHhtME5MandoR2RnOHF0ek4yd0JPaXpoeXFYSmwrV3Z0VUMxSmtwNkVhN1ArRkNnZTgxeXVnaDg0KzRMRUpuSDBrK0FiZjNLLzF6aVhFcU1iODdBbnBYWFBMTnZUS3pwMmlyT1VSbVNCSVJaR0FjQit5dU5EeDlmRlN3RUUzOXYrcWNWQXh1czc3dGhDd2RGdElQaUZONkV6d240cUM0V3NsY3hvZ1BJZEdXWSs5ZUtYdVd6d1c0cU10RmxMRjB4dXFuUmU0SkhOdGxqZy9QTmVvdkg5Vm1OT00yZkVVWStud3ZBZFJrTUFiQVNydzJMRFR2cW1oeXZpYmlFU25NM0MzMG1OYSsrcXFoVHRCUnFGU21zV0xxKzlSTnFkdm1ISVhtcW5INzhSTWZuRFpqN0NCWFZjblZvR2ZBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFFUndkMEMzZ2xINnRPVUlVd2t3Tlo5blBWVE9jQWpVb0lzc1RwQlh6d1poZzNRY1MraUN6S0IwNlZjbmQ1dWtHby95QjhyMjhPcDRMN1VOVDdnM2l5UHJydzV1alpMNnhLbFU5VG0zcVQveFlmSnhWUGpLNFBqb3BNa0JjVkpRSmVLTlAyNzRIN2xJRlE4SU9GRDlWdHB2c3FCMFpvSXBhRjRrNkMzU21ZNHVyQUswY3pDVlVlRnAwUzFLb2lRY1dOaFZ3RHpJOEdlMVNCYnNId0M3em5YZkY0eERsMklmS2wyTVVPVkNBWWZJTFV3TTRyQzhuaTYvT0VseDFyOXRNRWlUY3lWTlQzYTNZVGplUUVJckhBRmttT0ZXeVlWRTFyYitnN1E4QWJ4OXJseDhURk91djkyWFR0cExGRWhEeklYbEQxbDVzZ1Fqc3F2TXVvTEs0TzA9
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.1
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router pvrp6 1 enable
     router pvrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz13r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWxKTUVlcGtJMklHOEZXZklwQzJPa241dkNVckc1M281cnpXRFNCZy9GT2tnZVYvUXd2U2FueWlUQlNmYVFlUXdsUkNuMEtCQW5NdDFqZFo2YTExUDllVUtWZWo0Smw2TVp6MGo0ZDVCNExuak1jQWJmb3h6WE93RXF5NWZ6SFBOeG04UE1iK1N0aW5VV1QvckY0L3dOSFY5NVVjOCs1OTYySWZjWGdQV2lIUldNSXo3RU5Pcm9ycTFaekU5VEs5T0Z1TlNIQjN5d01qTVYySHVaYWhYRlZEaFhlNUo2YWVTaVdsTUQ2R3VIQjZvaWZodnlGUTY1QURoSkp1dEhaSGhrN2Jvc1dKcWhxek95VUJnclo2TFNIZmU4K2R6eUwyQjhMWlorYnJqSG9UY0xkMXVnT3NRanhhOHJKOXNIN3RxRWZTUXBzMHpZK2JnMk9oZVFzdnNaUUlEQVFBQkFvSUJBQmI1WE5ud1RCUGVpOHpyalhVRnJtUXN0TkxGQTFqTDU1dVdOTVN6S3gzNnBwRGVKaFBmYXdGdGJyNS9XUnFUUklmb1dXckRQUHFCNDUyWktyanJadS9wQ040YjlqTklyNEZQVFBzaU9TR2MzT3JXZituam9mc2VhK0prZTEvTUVHZTh5S2F5cnVjSU5OUFFOSFFpUjh4MDFwRGJvU3h2anJsbzJNU1k1MVdXR2hFZnJLT1BqbGZuV3UxT2JNcWYyZi9odDkxWUtoSVRsNGkvbThCM2dtZzlvcWRlRU1pV2wreFdjdUdwcFo2WDhocS8zVG1GMHYzQ25KdVZ1Y2RRWUFXRGR3cThrZk9GK1ExTzNEVDczRmxuUWNjYlVtNkVoNndhTmk5ZWlreXNjbUNHL2xrdURMK05WREl6R0J3ZWZnSm02cTVSYnRZOGM3N0tRNVNWRzRrQ2dZRUE4SHM5eDJCaHlSbDhxZ2ZoMEV6bDF2Z2ovQm9Wa0hrUUJrY2ZzRWtHeG9wdmx2UzZEeHNzeGpFLzVaUThMR3lFZU9DNkVJMkJYNmY1Rjlma3Y5UUhsZ3poWTFhOUxyc04vM0d0aXNSU29VQnFRay9acHg2UUs1c1dkNXFmdjgxM1RKOUN2MHB0eEw4M1FxKzh4UmhrbmxwSDljQUVOTWJJMnIrOVl0YjFQLzhDZ1lFQW5pbDM0UUNlczROSnk1aDMxM21oMXVzZXV0TXllLzJERTl3OTRvL3hlRXc2L3pVWXZjdlJWTWlRNUNGQUNXSjI5RHAvZnkwQkgxbVlyVTRSL0VRdVR6ZTZZRVBlajA2NnZBOTZ2NVdIRit6SDNEMTI1aUhrYllJd1VuNGIyb2hvUmdXQU1ER1VJbVNwUlk2UG9xY3R0Nk1qZFZUc0lTRVo3cExncDBkeDA1c0NnWUVBa29NRFNJMDRCa1U0NW42VzNVbDhYbFFmMkdBcjh6Rk95Z1JiRWhQcnhOcGkwaDJYbmN4NG91Y3VmcmlwVUlkc3poaGNRK2x5Z016ZHZlRVN4S3h4VXNIV0w2ZVE2diticjUyYWxZaTJydmVIeFk3UWxEalNyVDUzbWJiaXpRQnBSbzFoSlJvN2RqcnBkLytKaXFzcDRqQXUxMUo5UFlvK3BNZGNvdk5EeUJFQ2dZQisyQ01jZ0xMR3BYUjVwRDM0d2NQWjZaY3JubFhPdXZKMDZ4MTJwcHF5TC9EZzNHU0xVdnIvVkJ0ZjJvclErL2NLeUIrWWp5OW5SU1A5V2E5eThmdHg3Tys4WkxJSm5NcUdLS1A1SXFMRnZWQk1nYjdwc2lUUTdxaHlnRkUyWWsrK1dJc0dHNzBDR0ZqcFAveFNKbUd6OVZKcXQwRHBFUE1MTXlDWkIrTnlJUUtCZ0dYcVUvNlhwRWNwWWxPZThIYi9pZ2hTZTg1UGw1dElJb1orNjNFN0V4MncyL2tiUnNRZHpHS1FTK1RSc2U2UVpmbTNpNmlmcU1zZisyejFNbG1TdmtqVnVJUWJlRTZVblYwK09Ta0JLTWZEbngvTHpOd1pnamQrK1dGZ3Y5WEZOTkNOWHczTUdNaDdmL0VySUdRdkFhM0pRWkFkWmFrZ3RwZ09HQ2ZOZWQ2aQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDQ3Nwczk0MW8vR0tKQTRpR1ZpbVBRU1NxMy9RWnNEeDRpZFhaK2hBTjdDQ1d3QXRQaGJvRXliNUFXTHNaWi9nTXZBUmw3WmpuK2JCb3QxbUgvenpEVWxOcEdXR0J0L3BWN0lUZ0IvUmlpY212NlFTSktXV2JxN1dBRXhDcXhTaTZSYXp6OFhyUjlKL1hLaVZwNDNGVzgxOVlNbWtwZGJ2U280OEExUWI0Q293SVZBS2k2VUNORjlIb1lHR0tYOGlLc21JVW9VT1FGQW9HQU1QZTlpT3lnU2pTMFhSREI4eGM4MHpVMFZ3emZwT1BkL3JmUktzcnBKZkV4L3Y5K25hZFpTVjREQy9majFrK25OSjk1c2cwclF4R3RUSlUyeGRHNmFtMGZZRXlsalV2eFpyR2lWa0FSMFN0K1dLbmdvSk5WVG5EWDFwZ3llME1uK1o2QzN5RmNQOUhNaWpzZDhuSWxnc3VXeHNSdm5NZ3dVQzhuNTVpQ2N4a0NnWUFwMnlLeXQxcEl6cjZCeFpFcCtzdlMxbTFBSjhvU3VJUzJSUTNxNDVOdDdSUktkS09xM05GQ2pQVmJ0RVIzdklzMGFyVi9QN1pqTkhWbmJaejNxSEJTVFdtUU5pekoxS24zRlBOUUVwY3RFTFRNQVlpREQvdGI1c0UwYkd3Y2luUUxncERzR0QvcVQ2elV6QUJUczNKYVJBZVV0eDNncGkyZy9YTlNiVWliSWdJVUxzVHd6WkR5cVBma1NMTmxBVWQ5alRqVDBRdz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIM3d5L1VhMDREbGkxdXNoYlhyZE5wRlNHUUI3dm5CalZRQUdBU05ZaU9xZ0J3WUZLNEVFQUFxaFJBTkNBQVR0bFJSSzIvTHVjWnY5Z2pua0pvRUZ5THhFUXBLMmdzK1dvYWdqcFluOHA5Z3dQTElEQWZId2lOWXJPN3plK1Q3WHNHRUV5b0pRdWNEMmt4OEZwenN5
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBaENnQXdJQkFnSUVZWWt3TVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhNVFF6V2hjTk16SXdOREk1TWpFeE1UUXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDQ3Nwczk0MW8vR0tKQTRpR1ZpbVBRU1NxMy9RWnNEeDRpZFhaK2hBTjdDQ1d3QXRQaGJvRXliNUFXTHNaWi9nTXZBUmw3WmpuK2JCb3QxbUgvenpEVWxOcEdXR0J0L3BWN0lUZ0IvUmlpY212NlFTSktXV2JxN1dBRXhDcXhTaTZSYXp6OFhyUjlKL1hLaVZwNDNGVzgxOVlNbWtwZGJ2U280OEExUWI0Q293SVZBS2k2VUNORjlIb1lHR0tYOGlLc21JVW9VT1FGQW9HQU1QZTlpT3lnU2pTMFhSREI4eGM4MHpVMFZ3emZwT1BkL3JmUktzcnBKZkV4L3Y5K25hZFpTVjREQy9majFrK25OSjk1c2cwclF4R3RUSlUyeGRHNmFtMGZZRXlsalV2eFpyR2lWa0FSMFN0K1dLbmdvSk5WVG5EWDFwZ3llME1uK1o2QzN5RmNQOUhNaWpzZDhuSWxnc3VXeHNSdm5NZ3dVQzhuNTVpQ2N4a0RnWVFBQW9HQUtkc2lzcmRhU002K2djV1JLZnJMMHRadFFDZktFcmlFdGtVTjZ1T1RiZTBVU25TanF0elJRb3oxVzdSRWQ3eUxOR3ExZnorMll6UjFaMjJjOTZod1VrMXBrRFlzeWRTcDl4VHpVQktYTFJDMHpBR0lndy83VytiQk5HeHNISXAwQzRLUTdCZy82aytzMU13QVU3TnlXa1FIbExjZDRLWXRvUDF6VW0xSW15SXdDd1lIS29aSXpqZ0VBd1VBQXpBQUFEQXNBaFF3NUdQMGhna3ZxWVJaVjF3eGtVL3l0R0NMY3dJVVpuaEdQZFA4RWNLcVUyc0RBVkJGNzl0UEVxRT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUnF3U0ZoTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhNVFF6V2hjTk16SXdOREk1TWpFeE1UUXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUdGxSUksyL0x1Y1p2OWdqbmtKb0VGeUx4RVFwSzJncytXb2FnanBZbjhwOWd3UExJREFmSHdpTllyTzd6ZStUN1hzR0VFeW9KUXVjRDJreDhGcHpzeU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnV2J4d0pQeHdjcEtJSC81NitzbDlqVHJiczJBS1M2OGFmY2dsamM1cmFhUUNYeEoyMHlBZzFoL09UYTlqWmUxYkRHQ09hSUFtUE5DUy9scEhOVVNDeFBsQWVXRzlxZndmenRxN0szdHljSG1MeE9hZG9CNEQzVkxQdWpIdzFGWEJMRzNON1IyaVc4eW1GNEtMMHhqUW15bk9HSExXdGtnUnFvUDViaDloZEVORQ==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVCN010UERBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBMU1ESXlNVEV4TkROYUZ3MHpNakEwTWpreU1URXhORE5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWxKTUVlcGtJMklHOEZXZklwQzJPa241dkNVckc1M281cnpXRFNCZy9GT2tnZVYvUXd2U2FueWlUQlNmYVFlUXdsUkNuMEtCQW5NdDFqZFo2YTExUDllVUtWZWo0Smw2TVp6MGo0ZDVCNExuak1jQWJmb3h6WE93RXF5NWZ6SFBOeG04UE1iK1N0aW5VV1QvckY0L3dOSFY5NVVjOCs1OTYySWZjWGdQV2lIUldNSXo3RU5Pcm9ycTFaekU5VEs5T0Z1TlNIQjN5d01qTVYySHVaYWhYRlZEaFhlNUo2YWVTaVdsTUQ2R3VIQjZvaWZodnlGUTY1QURoSkp1dEhaSGhrN2Jvc1dKcWhxek95VUJnclo2TFNIZmU4K2R6eUwyQjhMWlorYnJqSG9UY0xkMXVnT3NRanhhOHJKOXNIN3RxRWZTUXBzMHpZK2JnMk9oZVFzdnNaUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQnVHOThXRXVBeElEK1hodnE3eVpFa0k0L01vNjNSRXk5MGNnSTN1eWtlVURUN1NKMFNpSWkzZVRGd3VIckZpbTJna0FoYlA3cDdITGNQenNoL1FxRW9YK2RBYlRuTHEvN0pDUXFOVVBOaU94TVFSQXZtd1htcmJFbWFabi95bGQvYUh1bG5PcnBRNlp6bDNYNXNEU20wV0FOY215bU85TkR2RS9oVXRSVUd1Y3RtM2FoUTZvbHRLRjd1NXlzYUxkMXlKMFFsN09lVDdxbUpXdU9saFpCQVhaRGY5REhBS1preHN4OXZEVHVvWCtRQ3RjUGI4UHJiZ2Vsb252MDVVNnZjd0Jtb2xOR2FjSkU5RzVSNytpN2l1NDFYYzN6WlZVTHJTbE1kenZmODZKekJ2Y1BYUTVjcDREVWcvSTRodnBYUXVGTEJBOEJTa2V5NDZwTEVrZFdx
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router pvrp4 1
     vrf v1
     router-id 4.4.4.2
     redistribute connected
     exit
    !
    router pvrp6 1
     vrf v1
     router-id 6.6.6.2
     redistribute connected
     exit
    !
    interface loopback1
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router pvrp6 1 enable
     router pvrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 pvrp 1 sum
    r2#show ipv4 pvrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
     |-----------|---------|------|-----------|---------|---------|----------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:06 |
     |___________|_________|______|___________|_________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 sum
    r2#show ipv6 pvrp 1 sum
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer      | learned | adverted | uptime   |
     |-----------|---------|------|-----------|-----------|---------|----------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:06 |
     |___________|_________|______|___________|___________|_________|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 pvrp 1 rou
    r2#show ipv4 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:03 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:08 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 pvrp 1 rou
    r2#show ipv6 pvrp 1 rou
     |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix      | metric | iface     | hop       | time     |
     |------|-------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:00 |
     | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:00 |
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:08 |
     |______|_____________|________|___________|___________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 route v1
    r2#show ipv4 route v1
     |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix     | metric | iface     | hop     | time     |
     |------|------------|--------|-----------|---------|----------|
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:09 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:09 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:09 |
     |______|____________|________|___________|_________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 route v1
    r2#show ipv6 route v1
     |~~~~~~|~~~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
     | typ  | prefix        | metric | iface     | hop       | time     |
     |------|---------------|--------|-----------|-----------|----------|
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:09 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:09 |
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:00 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:09 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

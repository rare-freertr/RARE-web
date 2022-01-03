# Example: pvrp ssh encryption
    
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
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCaWpJNVNrZHFXODlKeXZYeEVKSkEzSU1uSlp3ZWVkVVpzd3JZM3NOZmFCbHg4c01NaUY3dDNNS0xndnZaWkFXMWVWNTRwcFdrbUQyNVhhMWUrNk9QejM2emZ5Snp1UGxUV3dDS3pSNk5oSjZvSmxTZFo4WjlqYmhLa0tUbTEzcmlUWERSUkg5U2lnc3JYODBSRm9mT1lrNFpxYVQ0M2hqclpkZEhUbDFDOGorRnA4dEU3cndRenA2R0Qrano3c3lBRm1ObmJwa2lUZXRwbXdvbUs4a0xCZDQ0UnJIQVhDeTNuSW1wcFlZeU5Tc01YUDI1TWgrMlJoSjBTVGVVRnpkNjU5OFY2RlZQVThJMndwUXZ4ODZDNStSVlBnRXg5QmdSdkpHWEs3clovNzlVNEIyaGRpdHFhcWFkbUdMSW1ncmNORHdDVU9IcDg3Tmhqa1cyYUQ5QUxBZ01CQUFFQ2dnRUFFQzg3Tkc1RnN1TEtIaFBtYzU1NW5NUWl2NVBQR1lQekUrdUtWMjBRbGZyVGQ1cmtBUlphc0VGcGpuVnVLY0hsUDBndWJuSis2VVJCZjlQZUxqazdMcEwrWmlZaE43TSs1YUhhVVEwajFOSFp5QWNaMWxpckwzNGxTNWFGcHN1MERtZG5KQ2VSR1R0WHFzMkYyZFcyRnNtcm1wQThLb3c5My9iTWhlNWswUUt1eUlVQVozVDQ5MlRmdU5MYXdQUkFrNzZqWmJuMnFmcVNyOWFHNGtjSkdhM0tSZmxndDNoc0R5VEltVW9NVCthUDRrSzBXaCtyQWlJWkJPWTlrNzUwWTFtcVdmYTAxNWRCeERjRW5oRWpvTFZjTTArUCtwWERkVmJ0VFR4QWpvYU5rZHNIUWwvSXc2bFVIckN2ZTNJQVIzRlV3cTA4aHRJQzF5aC84TVZWc1FLQmdRREV2aFhrbG01eWZSVk40UC9CTktLQ3VxN0RsaUh4bGdxRXVEVzc4MHFLaTJUSmNObXhUQ0hNbUxUNmpHM0tPTm5SZ2Z6MkpabG1wSGVxL1dNcHM2N0tkdk93aE5ZWXAraEExWGV3TFVKQ3FPZ2Z0QXNPblhNc2REOXBTU090b1VIbnhDZ0p1ejJnazVHeTdOTW9ndzE1bmc1NHhGOVlmcFQvZk9neDQ4YWN5UUtCZ1FDQU96aXdnWEpSVjN0eFRkQlNpZU9sMU9NZFU3dGVsQzhIVE1PV1JjL3ViS20xeEtEVDJKdk4weUQ1UkxZcU9Zc0tpYlczd2Z5bS9qNm5McVYxT2VoR1liN0JVSFk2SldVZ0ZNby80OXR6WWI3elFxWlQwdFMwTGs4VHEzL0lneXpYMG5uTjNpVG9VS0thb3ZqQlJOcFBUenY5R0xQSkF3UWJrUjhXSmhmME13S0JnRU1qQ3AyQ3FCWHhrVCtPTkRoZUdjYTZwY0NnanR5OThzRHZpNGFqc3lBc0NTeWtrZVRxc2UzN2ZtYXhYUlhRNktPUjFCeTdIK25pM2VNL3JJTWlpZGNWV0hzNEdVYzRwUXpheTRrWEtMRk9xa2VIVE82ajFCV3JaYWdzQ1R6SzlvNThaWjFNZys4ejdGZytjS0EyZUhhejlRUkpIckE0SWVnOVc0OEt4MC9oQW9HQUgzWG9KNjNxclRoSWFma01abU84UFlCb3BGWlp2dytlSmkxWVF6TW5tN2gvUHNCYU1QK1E0a090Y0ZyQ1VzUEJjRGx2SXdGdUNrNlFjcFlJTkNXYjdrQ20rMmpSU056SjNjQWNDdWJOZlpaNnNkWWxWcVdBV0NDUWVDUDRldXBzQXh0NWxOK3VzR3l3S0Q1Wng1a3I4bzlmQ1c2WkZYVXUrZEIyRHdvVGtHOENnWUJNeFVQbzlITkxwZzNtbE9aYnNJOURONVJUSExjYXRZVTVxVkloakROazJVR1Z3UUtmVHNNWU5BOG1qZEV5TE0vZFJYSy92M0dDVWw1UUsvTHlMT1VEdWtIZXNnK3l0MDI4YXNycnk5Q0crVTAxTlRTV0V1R29xZU1sZi9vend6Vm9MeE1PN3VZcklJNzhmbHRrODRPdEozazg3OUpjRTZNZk1XM3lRNkZ0SWc9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ZoRUh0cEdKR29jZkJsamk1bGRtK1BBSmVhU0VieUVGRlJmaC9OZmhYdWlxazB3R1VranF6NUhHaGxpV1hKbXNtUUszV0JkZGp3K0tka1dTNGxvNlJMUmtjclc0dmZXcnhtVkhsRW8zdjVXcWlXV0VsR0Rudkd1aXU5Y1o2cmRrdTFSWnJjYnVONDc5aFpIdmFNc0N3S1JQSmp2T1YvbGt2NkdWRjBRb00wekFoVUE5VDJPekNpUEFIUjdoSXNFU0ZmMWpZVU9ZbkVDZ1lCV01UcnNFUDdIc1NXK3dsbkE2alMwRFdBaDFWYVRRTkRNSHlkS0hIYzhoNjZpcjVsZkp0c0dLNDNSNUJqQm0xUzczVnQzeE0zRlc0UTNwcHVCeGhYL2pheC9XNUphZlRBOVF2bitHVThrL0VWNW54QTZuTmpLSm01d1ozRlJQcWN6Y21rR2RmMzI3TkF6VFJOWkE2T0UrNk9NUVYycW9lRTd5VGwveEJSMTZnS0JnQ20zZlJtQmJhZE8zOElqMVRDS3hjM0lHZU4vdzI5TytpWERMaFU3VGV3YUxHc2UrbDc5d3FXWCs3SU13bE4yZmhBNkc0Q0pDek5ybVJOZXZsVEtWcTJWajlvczdyN0FOeVZPblpXS0JrdmRHaXFCSVdMTUNZcHcwRERLNzBBdXduN1FVV251b0F3SEZMMytPNm9RZjkvT3c4ZVNTWHNoLzlvUm5zNFlGZXhrQWhSdHZqWGhVZDE5Qyt6U3JzcDg2ejRhMUtETmxnPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeUhVUU9HUktrQWtMeTZUeUlHN1JuRWUwREZvMkd0dUFMQ3plbjlQQlA2Z0J3WUZLNEVFQUFxaFJBTkNBQVNyTXhHK2tZdUw2V25ORzArZFlJa1MyOW05cEFxQ25FZXg1UUtwT2psdVl5ZVhlNk5TTHdidWUrQVB1eHpqTnlyTHdLUlpqNWhPYjU0b20zQlhNMlVz
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVmL2oxd0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1EUTFNREV6V2hjTk16RXhNakk1TURRMU1ERXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ZoRUh0cEdKR29jZkJsamk1bGRtK1BBSmVhU0VieUVGRlJmaC9OZmhYdWlxazB3R1VranF6NUhHaGxpV1hKbXNtUUszV0JkZGp3K0tka1dTNGxvNlJMUmtjclc0dmZXcnhtVkhsRW8zdjVXcWlXV0VsR0Rudkd1aXU5Y1o2cmRrdTFSWnJjYnVONDc5aFpIdmFNc0N3S1JQSmp2T1YvbGt2NkdWRjBRb00wekFoVUE5VDJPekNpUEFIUjdoSXNFU0ZmMWpZVU9ZbkVDZ1lCV01UcnNFUDdIc1NXK3dsbkE2alMwRFdBaDFWYVRRTkRNSHlkS0hIYzhoNjZpcjVsZkp0c0dLNDNSNUJqQm0xUzczVnQzeE0zRlc0UTNwcHVCeGhYL2pheC9XNUphZlRBOVF2bitHVThrL0VWNW54QTZuTmpLSm01d1ozRlJQcWN6Y21rR2RmMzI3TkF6VFJOWkE2T0UrNk9NUVYycW9lRTd5VGwveEJSMTZnT0JoQUFDZ1lBcHQzMFpnVzJuVHQvQ0k5VXdpc1hOeUJuamY4TnZUdm9sd3k0Vk8wM3NHaXhySHZwZS9jS2xsL3V5RE1KVGRuNFFPaHVBaVFzemE1a1RYcjVVeWxhdGxZL2FMTzYrd0RjbFRwMlZpZ1pMM1JvcWdTRml6QW1LY05Bd3l1OUFMc0orMEZGcDdxQU1CeFM5L2p1cUVIL2Z6c1BIa2tsN0lmL2FFWjdPR0JYc1pEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQm1xQWJVWEd4N1ZrL21TMEF2TDFjMjNzemZCQWhRU01lQlNjSXJXUG1kNmhrL1ZrL1ZkU1FKa0tRPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUnZOczQvTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1EUTFNREV6V2hjTk16RXhNakk1TURRMU1ERXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTck14RytrWXVMNlduTkcwK2RZSWtTMjltOXBBcUNuRWV4NVFLcE9qbHVZeWVYZTZOU0x3YnVlK0FQdXh6ak55ckx3S1JaajVoT2I1NG9tM0JYTTJVc01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtjMVQxNnZqcWdwRlYwVGdOQWhGYUNxQWZIUk9sVU01OHdlQmtxYloxVU1BbDhJeEsvZ2dCR0VMMitvRTR2RHM2ZjAzM3ZFdlcxbHg0R3MxL0R1VEhvU0VwSGVicEpiWmozaDZ5REdrelc1eWxYdFhaK2xzUDZReWp5WllJUEZSUXl2Mittcm1nVzN4UXpScTNiVFh5bzB3WGZGc1VOdGovREVVVG1xWk4wck93PT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVQN2J2ZWpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16RXdORFV3TVROYUZ3MHpNVEV5TWprd05EVXdNVE5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCaWpJNVNrZHFXODlKeXZYeEVKSkEzSU1uSlp3ZWVkVVpzd3JZM3NOZmFCbHg4c01NaUY3dDNNS0xndnZaWkFXMWVWNTRwcFdrbUQyNVhhMWUrNk9QejM2emZ5Snp1UGxUV3dDS3pSNk5oSjZvSmxTZFo4WjlqYmhLa0tUbTEzcmlUWERSUkg5U2lnc3JYODBSRm9mT1lrNFpxYVQ0M2hqclpkZEhUbDFDOGorRnA4dEU3cndRenA2R0Qrano3c3lBRm1ObmJwa2lUZXRwbXdvbUs4a0xCZDQ0UnJIQVhDeTNuSW1wcFlZeU5Tc01YUDI1TWgrMlJoSjBTVGVVRnpkNjU5OFY2RlZQVThJMndwUXZ4ODZDNStSVlBnRXg5QmdSdkpHWEs3clovNzlVNEIyaGRpdHFhcWFkbUdMSW1ncmNORHdDVU9IcDg3Tmhqa1cyYUQ5QUxBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCY1p3MDk2U0UrQjNUeFhyNDZ2UVZJSmVKQ1JSbU43cURKU1lMSW93VzVJYjBzYkVEU1c1QlNKU2p2WG9CRWtVajJubGhEWXJZWVIyNDZ5MWlUYWIwNnpBaVZIL3VUS25sS3JCTkx4K1piRnpZVlA3eVM4ZFc1Y0R0TmhUTGJTRVRqR2hKN25qVGt6RTJSdlU4eWRCVFVOeHM3Z0pPVXZkaXNzUU1wU21YbTR0dHAzdGlxelEyOGdzUlprcXN4SVRqaER4UGJHQzBsQnNXS1N2ZjhSc0h5b0YxNEtrai9OdEFZdndMemJicGU1VzV3LzRWdmpjY0RDbEFndWlHZVZSd1RaenB2dU9iSS95cGpTQTlmWXlkUE1MaURBSGRvSmZhRmp3NDJiUVU1ajhGNzZBTHFpbGlOeFdMQkNVVnhvTXFSak4xYy9pWmk5YStLNjVLbDA1K289
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
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.255
     ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router pvrp6 1 enable
     router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
    logging file debug ../binTmp/zzz1r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQTNySEtUNTVORlY5OCtuTnVqK1Zpdm1YNFZXa2F3MzlGUEc0dDlXZE0rL3pIN2x1eGMyaC9UZ0NIOFc3VWdGYmpKdEc0c1ZHdVg3WmZ4VVhXaDNVSnBsb1NudUpzQytGeWw5ckxRa2crUEVTQlRuVHMvTEY0RDZlRFA4VUk2MGswM1VQSFp1VVdCSnpyOHZrczRmVERVdHdJR1FMUGdtWWhnUlNZN0NtNmovQVJGTElTMEJ4am5uaW9QcGFoM2hnYVROSmxWTUdqREZkRE9FRVhiZ0FWVzZRVDExTmcycGpxZHFXM05iaFhEaWo4OTRCK0crenZWV1BKRkt0dFBzVHJZUXcxMzYvZ3YvM0V2K21RNjJqR1dMR3dyUUxSL0dUNStRaTIrWXAzUVgvOWJmSXZ0QzVlTUw0TkE0bCt3SUtGakFudy9IdDhDS2gycFlSQ0syZzZUd0lEQVFBQkFvSUJBUURYM0hLRXRxZDFmamZBOVQ5SWtFc2t6K2JsczVuVHdudzBWWUNMRGZUYmxXMmZLSlpiamdGSWRNOVJRZU1OL0NyM0ovYmxPbzNTRFEvTVF5UHQ3WTdMQnloaGhvekEvMmw2dFFTdFhTV21lYWoxaWZWbUJBaWk4L2NQUzBpWCtVQWE4bVpJNE9wMDBqOE1LR2hQSmxobTZ3MldZTmtRUnp0V3ljWnB0UkU0RHVia1QwVyt2YnJ1UXRRbU1pZ01LTml3bzNRMzJHUVhYOHQ0ZW15cXdNSENZM2FHcUpCS20zU2J5eDNzdUp2dW4raU44NTZFZ1VlWCttT0s5QzZhVWtpNzkvVlNqVkJBOHRMZjBUSE1CblF4aStqSzFiVWNWZVVwVk96R1JmM3EwSFNtOWhHc01GMjhOMmFtUjBSRmNiUDI4bVpodWxoT21pdXdmNWw1aVkvQkFvR0JBUGdsR2dCT21UdnI5R3ErLzhaT2RiT1h4Y0x1bU0wekc2V1drWitNeUlxNmk1UE8zN2ZjVDA2cEgyYXVBVEtlbUQzbWhxNXdxZFRlZVRVUno1cTV3YVFXVjc0azZWTzVhOTV2aFJHWWtXQnorWjVpQkpDRk5VRU85OGY5anZnU0RYUE9HakU3RjQ0Zi9KaUhkeURHaXhReFZaVC9rSFdEcXV4ZmY2SU1nRS8vQW9HQkFPVytjZ09pdnByTVBudGdaN1VkZFFtdk1IcjliLzZmblZZTFZ5RWkrR0k2djdIYmg5NjQrYWJNblhKd0d6MjJ6a0RQMGhFbE92SlNlb0NFZGFyalZ3R2hnVXFnSUsvdVh0RnJ0T0xqVzlXQkNVM0JIVEJsSE03cGp0dVViYXR1QjRmOW1XWmdwTmRJMnNoNzYwQk9TNVNPY2orVnlJZWoxMG1qNEVTdjN4V3hBb0dCQU1jQWloK2c2UWJETGRyRm5qNGRBZ3VyTmZBa2hPcGJpRnA5cS85MldnWFhvTVJDN2V0M2hTcWlPd3FQbFdwUkFlcnlpeVF1T2lUNjNkMlBrUnlXeUJLZDBIUXZDZWdaRmNiblRLSlY1cENoc1pneEoxUDNZRVB5aXdnWjhxUkRaZ0p2VVZZVis4Z0JJd1AzNzdPYlJrSkZaa3I5d1k1Y3I2Q3MzYURKd2NWbEFvR0FKRExMbUJNT1lTbUpOcnRMMjllV1Z6NUpMemU3YTYwT2h6NG1Ma3hxUWwvclVFUzh0YlVEY09xUWJEV0p0VUdXWWRQY3oyTEVWT1gxODBYcm5FOVJxQ29nU3ZmTDdxeHFPQ2oyU1VGMWVNQnFETncra3g5N1dJYW9RYVN6V3UxdE5sb1l6MjZ1eWxUcVUraGllckZiYXo2K2RaSk9GRUVXYkwzcldpY3p5U0VDZ1lCT01WYnltQ3V1YStWeUFJQ1h6Tm5zeTN5eGQyOGF4VHpKZWw0VkFCUGl5dThhYzlMaGRnVGhMU0pHRTlrKytzNTZGSTRqQzgzc0NMRUxib1gvSjNyRGVQYWx0ci9NbHdwWXU2RWlXVHBFYXZPM2c2YnhNTmlycWI2NVRBaU81NFNLV3YxMkNMd3RDNmsxa04wT2VPRHJyRWx6b1pjRWVyWE1PVitYUTdvc1dnPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ZMU1pNVzZHNlMvM1dzTkgwKzBFU2VqNk5qb3cxd2tieVpBbkhwem9zT1piaGhtcGFXbWRNaXpWajBlM3M3V2lmR003RHR0Vys5YTlUL2t3aXNxSUFwOXhwd2NDUUNWRklaMUpvTGF3eUtKVTJSd1QxMk5UNkIzd05SbFFSMXRBWXYrWW9RaExWd1VNZ0E4ajZKQ1lDYUtDNEViU3lnRU5UTFcxMmo2NWZ5M0FoVUE2Yy9aa3E1OHJrOGxYTWJkdjRQbnJ4aG5TTTBDZ1lBeGFMSVBwUzJSVkZyRnZLSFFjS1NpYzlMMWVXTzRscUs4NEpFVFIwQzg1QTNZUlRHSTM5d2NlUy9yWVVUQW5FbGhIN3d5c0VBQXdEY2dyZ2J3OFYxdlhYTVpGSCtWU0Z4VVdEeEVRaVI1cmFidzd2UFJoRWFpekpKaFM4UFNHS1FjUmlyYzBSbkRWVy9OUkRaTldBbG0vL2VlWXBXS1RVamF4TlZGanQ0MU9nS0JnQ1pQM2xJOVJySzE1T3dDK3I5cGQyeHE4VEFFL1F2VFpTeUNQelBhdTFhSGtlU3RFaEwvUUpueCtDOEpBMGNJbFR2VWRPck02UjZNRFcyNE92ekhPQnF3TlJhTW5tNjdzZzlHdkMwNjRvZ2YyRmx4VWdZVTlmcGlkdEI1OFpNZUkyMDkzOTRLbE80YmhSZ1AvNGJzekM0VUZPZk1lcjk0NWZXbzF4M21FN0Z4QWhRN2x5OHp5VkdOM3NKalJ2bXd0UjBFMXR4S3FRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMHE5QjBiMEFrYXlhWWlDQnkrWHhLanRzWGwrSVowVEVxTmxzV2pqb0ZLZ0J3WUZLNEVFQUFxaFJBTkNBQVIydzNMdC9meVpxNkRQYzlTTFMyL1Fjc3pQVGJnNzBVblB3bmpDU2htQ1NSMkcrKzhVNlNhK1M1WmpQdFh4TCthREVGMmhtVEpVWWZMT0szLzREK3h5
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBZytnQXdJQkFnSUVlKzFwMXpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1EUTFNREV6V2hjTk16RXhNakk1TURRMU1ERXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ZMU1pNVzZHNlMvM1dzTkgwKzBFU2VqNk5qb3cxd2tieVpBbkhwem9zT1piaGhtcGFXbWRNaXpWajBlM3M3V2lmR003RHR0Vys5YTlUL2t3aXNxSUFwOXhwd2NDUUNWRklaMUpvTGF3eUtKVTJSd1QxMk5UNkIzd05SbFFSMXRBWXYrWW9RaExWd1VNZ0E4ajZKQ1lDYUtDNEViU3lnRU5UTFcxMmo2NWZ5M0FoVUE2Yy9aa3E1OHJrOGxYTWJkdjRQbnJ4aG5TTTBDZ1lBeGFMSVBwUzJSVkZyRnZLSFFjS1NpYzlMMWVXTzRscUs4NEpFVFIwQzg1QTNZUlRHSTM5d2NlUy9yWVVUQW5FbGhIN3d5c0VBQXdEY2dyZ2J3OFYxdlhYTVpGSCtWU0Z4VVdEeEVRaVI1cmFidzd2UFJoRWFpekpKaFM4UFNHS1FjUmlyYzBSbkRWVy9OUkRaTldBbG0vL2VlWXBXS1RVamF4TlZGanQ0MU9nT0JoQUFDZ1lBbVQ5NVNQVWF5dGVUc0F2cS9hWGRzYXZFd0JQMEwwMlVzZ2o4ejJydFdoNUhrclJJUy8wQ1o4Zmd2Q1FOSENKVTcxSFRxek9rZWpBMXR1RHI4eHpnYXNEVVdqSjV1dTdJUFJyd3RPdUtJSDloWmNWSUdGUFg2WW5iUWVmR1RIaU50UGQvZUNwVHVHNFVZRC8rRzdNd3VGQlRuekhxL2VPWDFxTmNkNWhPeGNUQUxCZ2NxaGtqT09BUURCUUFETWdBQU1DNENGUUNURHZjTmhzMENJeElHclFhQ3l0dXk1eGFDdHdJVkFJZURaZEpjSW9PSkI3SkpBUTZ1Q2xPSFFFbTQ=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUTBRWmZ1TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1EUTFNREV6V2hjTk16RXhNakk1TURRMU1ERXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSMnczTHQvZnlacTZEUGM5U0xTMi9RY3N6UFRiZzcwVW5Qd25qQ1NobUNTUjJHKys4VTZTYStTNVpqUHRYeEwrYURFRjJobVRKVVlmTE9LMy80RCt4eU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnTmNvbWxwd3VpZ1FxSUlVUGc5bmxNcFVHdVV5ejdBV3FpUHJaSTJOOVhMZ0NYd25oZ3FQK091L0hrbWp2WFN1MWU3ZzdDdTZOcndmVHE1L2hPQU9NZkFpRUxha0kyWkI4bDdhUXhJMW5zeUN4dkROVTJESndhSFkvQjlPVUZtZW9Jck1xaWptVGpPeHpLWmtNTG1LWVF1TkZxSkxKQnN3TGcyQ0c1c2xjQTF1dw==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2x6Q0NBWDZnQXdJQkFnSUVNajl0ZnpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRFeU16RXdORFV3TVROYUZ3MHpNVEV5TWprd05EVXdNVE5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTNySEtUNTVORlY5OCtuTnVqK1Zpdm1YNFZXa2F3MzlGUEc0dDlXZE0rL3pIN2x1eGMyaC9UZ0NIOFc3VWdGYmpKdEc0c1ZHdVg3WmZ4VVhXaDNVSnBsb1NudUpzQytGeWw5ckxRa2crUEVTQlRuVHMvTEY0RDZlRFA4VUk2MGswM1VQSFp1VVdCSnpyOHZrczRmVERVdHdJR1FMUGdtWWhnUlNZN0NtNmovQVJGTElTMEJ4am5uaW9QcGFoM2hnYVROSmxWTUdqREZkRE9FRVhiZ0FWVzZRVDExTmcycGpxZHFXM05iaFhEaWo4OTRCK0crenZWV1BKRkt0dFBzVHJZUXcxMzYvZ3YvM0V2K21RNjJqR1dMR3dyUUxSL0dUNStRaTIrWXAzUVgvOWJmSXZ0QzVlTUw0TkE0bCt3SUtGakFudy9IdDhDS2gycFlSQ0syZzZUd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFnQUFzV3Z5RlhGcnJFc0FDK3YzSDg2K0l2Nm8wbmp1bnBzVjljRVZBb0t3TGVLSzI1eGs1cjhZNnBEZHh1a2pTSi9wY04za3k3Sm9aNThKdmJZNHZpUUc1dG9VVTB6WmhqNTNmSkE4SlVkR1BrcDVGcjh4VDZUckRwYXVyZkxsM2JLWEtnYzhJblFZK1dTbGo4WXN4RTV5UVNqSUlkL3hZWlV2bkF2NlVaM2J3elJNTmhSaTRqd3pmNS9Ec3hYb081ZE1nZklkdDFVMDhtWmFudVRIUWx6b29lZnlpOEZVSmlWM1BxSkJ0ZUk2bms5Ulp4MmY0eWJKOGJYbEZRemIyZGNUUkdId3lCQXkxM0phbEJHWTlIaGFtQU12TVloaUZEUHBhTnJvSDBwRHBPR1h5ZEgvNEpaUTgxR3NPajEvalViZTJyZ3Nsa3BlQXBEU09EbGtNcktZNHc9PQ==
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
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     router pvrp4 1 enable
     router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router pvrp6 1 enable
     router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:07 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:07 |
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
     | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:01 |
     | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:12 |
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
     | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:12 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:12 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:12 |
     | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:13 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:12 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:12 |
     | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:13 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

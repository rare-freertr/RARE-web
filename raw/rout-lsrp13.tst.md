# Example: lsrp ssh encryption
    
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
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWdaTEoydmRUTkczc2gyQTNHTXdGUXdNMFBqTkFGc1J1SlFBdjBYbHJ0Y2tYM1ZpeS9NMFp5NjQreEltYi9nWis5MTA3bjFMcUZqS0xCU3hwdTNrRVY1WTF1Mm91WFlmSkpUTXFrb3R2UTRZV3Zqc0xmTkJsbEEwS2xuUktRakd4eWQrQW5HNFZCb2Q4dXpiSmZkS2luRTUrckxGQmo5RmJyNGhHcHRyZ1pOQ3JuZHN5aVB6WFJWK1ZCcDV6ZXZaL0ZCUWQ2UjlSMkpCVkVaaUxrNld1Y0M3QlBVWmRWNDBnRHVUODNnMWlMV0JQQnVZdCt6alZDc1ZKMDNmdCtESjhkWS9PL0FoOGJLbUN6cVRQNy90WG5QcG1zQm1zYWxBSTZzZC9Ha241L1ErWjNkVklzL0w3UFYzS1Q4NXI1VVFpZG04WnA4UytVYk43STc1K2ZLZkRDUUlEQVFBQkFvSUJBQ2tPZUFOMzV0ZHdGVWg0QmoxSE9FdVprazQ3TXcyRHhGclpDazNYcVhkNmRxTmVYYWlZM0ptYlpxd2o1bGZCZXkycVR5QVd4N0dzNWp3SGJLRklvVVdYaFFNVGpBbDY0eE4wZVFMaVI2a2ZyY2t0TUdDbUwrbVBrRkZJRzllSm80b1IxZEM3V05JdTBDa0tIU0pQUWROQlZBWW9URnZqdktlTUNNY0tCNXdweE8wY2pIb1RwV1hac3JGMHJRR3hqMnJ3QjdyMk5sQVBKTzVmZWJLMzVvUkJiMnpFUXhnUDh3TzNPSGNHTVpaVUR0NWROOEw0TGN6VnpES2tsczU0V3lqMHRZcnRSdTYxT2F0N1ZtZjV2TlF6dXY4d1RQSk45U1RleTZvbDFaY0d1MkdoM3A0MkU5eldHSGs0cDQ1djBMMFErWXM2QXdnblMwYjZtalRtdDFrQ2dZRUEzY1A4K1dFN2dzUE95U1MxMDU0SWwxZVBENjg5TDF1WjlXbFhrWXkrVS8zWm4yYUhneWplMm42b3JxenJIS1I0R0hNSWNzTHpKRHgxMWYwRzJLWGhpSm5SS0VaNXpwZnppLzNLQnhRUFl1QXVXS0ZOL2xzaHdDa0hvMHJETVVrY0h5MFVWS0dFc3EzR0RPcXlLZmpXZ3FaVWFOb1Jvd0lvZllpbW9MampnR2NDZ1lFQWxaTnU2R3pEMDZsbFRBMmJPWHp3RDZ3bnViNVZtekx6NVZpcEJkV3IyQXB2SDRzYkVQYVowYUx5UXg1V2p3MDJ3RjkvRTV1dlNBNVluSmFNbE1kRXVsaGJMeHZrbXhlL1p4Q0EwVUFlNG40MnpKdzZzK3QrTE9rTkpjcHR6NTdkMDVnb0ZjWjdrbXNIWTZnY1VtZWRvNWxZOXFBOWNsR1BpTWlvams0NHV3OENnWUVBdytqb0NzYkM4L3BYSzRxcXRvL2R0eFU2NVBoQ2JSdlhIdDQ0NWZRWUQ4c3AvWTl1RjRoN2x6cGRlako0WVkxS0t3ODBYMjJwcmxGYkovZW5uS3l1V1NiSmgzTDdHRzlVVUUrYnNqVWVncExaWHFMaGE5ckdMaVFSQTBpQXQ0R0d2bVBzbWZjMmEwTG91M0I2aEdtMzF5TnBYbGVIVFNJUzh4Tk5ZSjcxRy9FQ2dZQkppQk1yMjl4aFA1TjIwZkdQVDJaTXJodFJhc3AyNDVPWEdnRHR4MThWYy91eERCZWdQVHJkSGpmdTJ3aytoZ1oyaC92V3plQmJrZ0hwNlBEdmF3N1VkUDlPcDIyNCtQRzFYeDJVd09ydCtaSkRBRUt6bEgrUTRIa0FMUVhTM1l5N3FyOTZCUHRXdlpzQ1dQQ2phaURLL21ZSHlEcXM2bitmaE5Xb0w3Z2Y3UUtCZ0FYZTlzT2s1MnN2TWdrSklLcDE0RVdKTENlQ0thVmxyc3hFMFJmOXJmL1IvNTJPb1NHSldBVmNMTUZKeDR5dzEzZGJvelMwanhXejQ3akErQ0dXZnRCR0x2OTdLcTA4c1hydUtmOEJHTGZXT3A2VERPbkZESHJsYlRKemF2OFBsMlNJVThMcGZrbWFNLzRiTmEwdXVjckRHajllKzNYaW51Mmc4TVVjR2JYcw==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0J2aXB3Y0tsSmhGSGM0L1h4K2ZKVlNFQUo5Y0JOSDVxYVZNS1JPTWJpYVdybUc5VU93Snc3cTg4SStWUHp3VUMySHFlUjMwcTgyUVdxUDJldFlhZEJ0KzNleVNyekxjNEEwUmM2WDJFOUZ0aTB3VHN6TUIvUEdiNlh5Ulo3MVNva0drUDhEU3kwYkNTeGtiRnN2R3NSTElQL2dxNkNUZktHTjFNQzlQWXR4SEFoVUFobFNJVVVzdDhkRDdRbXF1TU00cUdvdWt5MWtDZ1lBQlJDVG1BRFUxQ25nN09UcXovTmc0NGw0UThxb2VkQWdOWFVWZUloNVgwZUJLbTNTeHNSbm1mVllvUGgwdmIzdVRLVXhudzdPeXM5emFWdGsxTmg2MWZhRC9scklUSEJOZGQ1Q0tIMmtWZDlSNWdFSTNSM1B3OEdHak92cCtWOHJ4QWY3S20zL09XZXVQSXRNaHJIRHhMN2xsbEsvVzlDakZESWJxc3hLZ0tnS0JnQkZiQUwyaHROb2hnOFVicXJuTWQwazkrMmI3YjA4OTJnYkdqcENEbnI5M1N0NlhuSGtDa2pEemk5bUxLdEtFRXFnS3pTb01QSS80bUJ2blZ2VVlNQVNEK2VKQTRyMm90TE5LcGZqVHZpSS9sb3IzUkd4eUdVMXhSTEdKeUNEV0VWZTJBV2lZZUFVTXp6ZHkxZGtsQkRCYmx4WVY5aHpVQ3hCMmROWlNWSUI0QWhVQWlqK0Q0NnRKSFYwdFU5RWhuQWRTajhLbnNrTT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUR0T2M2alpGQmhiclRHdlN2ZUdPV0t0ampjUGN5dzEzU0gxZlA5ekZwVW9BY0dCU3VCQkFBS29VUURRZ0FFMDVCdUdwSXJ3dFVSbnVUSFR4eFArMzdHYUl6Q1c4UjE2MEV4cWZNT3FzT1dxRVBsQVVPZC9RaXkwMjl2WFNmQjlPeUd2b2hCMGQ3amtTL1RiaHJjK2c9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVZU2hYRVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1ETXpORFUwV2hjTk16RXhNakk1TURNek5EVTBXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0J2aXB3Y0tsSmhGSGM0L1h4K2ZKVlNFQUo5Y0JOSDVxYVZNS1JPTWJpYVdybUc5VU93Snc3cTg4SStWUHp3VUMySHFlUjMwcTgyUVdxUDJldFlhZEJ0KzNleVNyekxjNEEwUmM2WDJFOUZ0aTB3VHN6TUIvUEdiNlh5Ulo3MVNva0drUDhEU3kwYkNTeGtiRnN2R3NSTElQL2dxNkNUZktHTjFNQzlQWXR4SEFoVUFobFNJVVVzdDhkRDdRbXF1TU00cUdvdWt5MWtDZ1lBQlJDVG1BRFUxQ25nN09UcXovTmc0NGw0UThxb2VkQWdOWFVWZUloNVgwZUJLbTNTeHNSbm1mVllvUGgwdmIzdVRLVXhudzdPeXM5emFWdGsxTmg2MWZhRC9scklUSEJOZGQ1Q0tIMmtWZDlSNWdFSTNSM1B3OEdHak92cCtWOHJ4QWY3S20zL09XZXVQSXRNaHJIRHhMN2xsbEsvVzlDakZESWJxc3hLZ0tnT0JoQUFDZ1lBUld3QzlvYlRhSVlQRkc2cTV6SGRKUGZ0bSsyOVBQZG9HeG82UWc1Ni9kMHJlbDV4NUFwSXc4NHZaaXlyU2hCS29DczBxRER5UCtKZ2I1MWIxR0RBRWcvbmlRT0s5cUxTelNxWDQwNzRpUDVhSzkwUnNjaGxOY1VTeGljZ2cxaEZYdGdGb21IZ0ZETTgzY3RYWkpRUXdXNWNXRmZZYzFBc1FkblRXVWxTQWVEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQnhUR1FSTHBoN2dUdXk0M0xhcXFhc2FFQ0ViQWhRYmxsWGF1ZlROMEJvRzEvNXdqeU5DeUU5NW93PT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUWs4b1VRTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1ETXpORFUwV2hjTk16RXhNakk1TURNek5EVTBXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUVGtHNGFraXZDMVJHZTVNZFBIRS83ZnNab2pNSmJ4SFhyUVRHcDh3NnF3NWFvUStVQlE1MzlDTExUYjI5ZEo4SDA3SWEraUVIUjN1T1JMOU51R3R6Nk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUp6NHlRSmRiNUtsaytRbzNEbmUzTUdWN2dHQWVOMlpsdUFLR056YkxER0RBbDlVTXM1d3AzdEFLZHJyd2JKQXkwNGtpTHZ2dXpkMUp2RVc2VTBiRmJyUjFpRTQyblpLZFN1TzVtS0JYNFo5UmZCNThyeFBGWnJBUmExRkUwNWZZZW94QVFHai9hNXZxZVdFdlhqVFhsV1dLYUgyRmpwWlBjK21tL1V0SnRDa3dBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVNT0lrOHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16RXdNek0wTlRSYUZ3MHpNVEV5TWprd016TTBOVFJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWdaTEoydmRUTkczc2gyQTNHTXdGUXdNMFBqTkFGc1J1SlFBdjBYbHJ0Y2tYM1ZpeS9NMFp5NjQreEltYi9nWis5MTA3bjFMcUZqS0xCU3hwdTNrRVY1WTF1Mm91WFlmSkpUTXFrb3R2UTRZV3Zqc0xmTkJsbEEwS2xuUktRakd4eWQrQW5HNFZCb2Q4dXpiSmZkS2luRTUrckxGQmo5RmJyNGhHcHRyZ1pOQ3JuZHN5aVB6WFJWK1ZCcDV6ZXZaL0ZCUWQ2UjlSMkpCVkVaaUxrNld1Y0M3QlBVWmRWNDBnRHVUODNnMWlMV0JQQnVZdCt6alZDc1ZKMDNmdCtESjhkWS9PL0FoOGJLbUN6cVRQNy90WG5QcG1zQm1zYWxBSTZzZC9Ha241L1ErWjNkVklzL0w3UFYzS1Q4NXI1VVFpZG04WnA4UytVYk43STc1K2ZLZkRDUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUorM2Ezc0xGKytTOFlROXdrRFJKUXNGemdOUXhhT2dBVWNtMXhoVFNGK0s1emd1KzlxR2xKdUw3VHdqRzJBZ05laDlMcmxmSGhLRjlkNjkxNTZQV0I3em9xYlF0YlZWUjVQVUJNR3JZRkFzL2p4Z2ZQQmlhZTZTNnFaWGVjR1ByWk9wbmUxL0twUE9Zdk13ZTBadWs3M29ZdCtXWmtkTlNtN2JueHRiZDcvaUtlbitpcm5iblJGaVBqTDl6SlJXVzAwdjBNcFYrRXc3L3pabFpnTEp4M2ZybXNySE8rRWtkLzJuWWN6RC90ekVlUUsrSEdUcHprL0ZBL1NVVUpsZU5ITklaS0RQWlpFZVZTVHRMdHRjZkt4NEI3bjRSZkFKdmhvd3pjN2lzWXQ1R1FzQkUwTmhDMzNvcmdQVVZNcEZKeFR6aUVOZkwveW9GNHVZeUhTaUZy
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.1
     redistribute connected
     exit
    !
    router lsrp6 1
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
     router lsrp4 1 enable
     router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFCNCt6VGZGQTNtNTdpdGt2WFJZcjhCT0RmMW1qZUxpcXpSeUVOSWw2dFY0cUNURlpYUmlVRDN4UlRZZE0xSzczVUw2Q2RGNWs3aWJoSEhTU2hkTVVhY0pOcUFaRVQrWmpDYXBxZHFNTjU2dUdDWkJpS2Q4dlVvaldkbG55bjJtV0JQVUd5K20yWTZNTXFxTGVVdElldTJUcWgrODZoTysvYTRPMGN1dGNOQ2JWbUtNbkgvWEVqOWJIRUYvd0JpNTJuUS81aVFXTVFPbmJwMHNVaC9waGp0QWI3MHR6K2ZCRGlscDZCV2tMdTkrV1gydHQ2dWo5SmQrWW5pWktEVUFhenpCMll1aHdka2FuSHNiVFpSREJPKzlRVXA0RlBKazVLK09GSEVIS2lMUXd4Q3dkWWZVTi8wNlkrRTNLb1RZTjRZYmFKOTNOYU12eXVFT3R2c1FIZUJBZ01CQUFFQ2dnRUFhRy83T1dRM2lCQ2JkWU83SHhGT2NBQVhGcmNWb2ltSmZPT1RhZFE4ZlR6UmY0ZVB1TDN5enJGY2lHdDBXVzhUckw2eFFIOUxzOTV2RElsVUJmY216RjVvSFpQeGwyZWlKNjhjTU9pVTluMjZMZitFM0xOQy9jbnI2MmNXTTZJOTZObzF0ZW15dXlNcG9QVlR0TDFtblErVUYxdkIvTVU0Tzl3NFc5TmZCelRsMVpNYVBicVFYRUJJODQ5bThKajFmVndjVGEvbGhET05zWEdHMTBjQThESnFCOGgvSHVZR1ZKQzlyL1lmQTRtM2oyaVU0aHM0RXJnc2tCODdYem1oY01yRkU1WmxFOHlkYmo0RVNwNUVPL0RhTDlaT2JGdE5IVEY3NGtZazZlcEdBMGQwek5vVDdaK1hTcXVQbWhuSWxhV0o2THM1SmczejZldWR2RFQ5TFFLQmdRRFordXBpbDRSSW9uRWdJdFVod1BpZTB0ckFWdmsvMWdzS0hadjYxMTZtdzZtSlNaVWE1a2dhTHlGSzBZQVRKVkNOUktrS1RCTVd1Y1RSdUhESnBvcWJiQmgxbjB4MXZkRWdUWVlUSEZZVW9pbE9SNkx1eTVUbjNjZ0doZHgrV1hHTGJ1RTUrYy9BZk8rNDNsRHZPZWN3ZVJIV3NrOGttOC8zMDBDRGZLdjlHd0tCZ1FDT0ZTdkhyQTc2dFlYN2o0M2NNR2JkK0JHV2YvaUNYRnhUaS9PeDlFRUUvdXE0OXNyL1h1bmhBdUpsM0Z5UnpSUDNMeWFPcUFrWGxIbmRONjE2eHBTM3NnNHF4WVdRRDhkVDRSc0xwN1MyVE9DdXVOeDl2SGhSci9nUjJYNDZlYVJ2Vk9WSXJFeVd6RVBCRXdoV1VlSUhwMkJTczRaN21xVzNjeXREREJGemt3S0JnUUN6bHpvQ3pzakxPeUt2RW1PODhvc2o5NThJOXQ5V1M5ZytsbFNMbjJPNVM5MWpZZjk1OFI2WWpCb0cxWUtLdzZTUkwyK0NMMWxPMFBFcXhLWVFUYWxIRWhFNDMyMFVXTFp5d2N4ajlHV3JqRXN4MW0yVUJxRUJROFZvTW1PT3FjeVZ6MTI2OFduTU1tTWpVZThtbWZNekNaeTc0WjY1RDdLUmdUaFczS0dxM3dLQmdDNUl2VU5GVEhmbFRDa2ZvWUc2RHJoK1NCUnp5WnVGeE5tK2ZIdGE2eGRhaDFJTHF5TTNZdzdXcHJPeDdrSGN3WVZEU2RjczdCRlBYOGR0ak1pekNkMHhWcVllUkIwaTFyYi9YSlVXWTZzRExpb2N0RThOWjFDTTkwMnhRUXFCZDh5QXBsUmZORy9uU0tjTHNTcVZjQUU0U0F1SXllVllBbVhaVVoxOHYrNmJBb0dCQUs1VnJ4dzNDdGNzWE5FNlNOVllCY29XZzBMMi9GUVdPeWJqSWl2ZGY3cUFBU2pubGhybzdaTVZZOUppRXVFSG1seEFYVDlDYVpiaTN5WWFLSUh4Nng0UzVJUVdjaXpXdk9JNmJMeEY2bnZXZExlaXpiRjg3ZGw0Ky8vc25WU3E1emd5MGY1Vk8xUzg3NXpZR1NsQi9VSWloNlQ5RkR4Q3VtcXhTNGlWWHQ1Yg==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0hNeHVJT3lubFdJVy80QjhGS2tSU09OSGt5ZDV4NzFKQmZnVG44ajNFMnFEbXJKWG11VnlDUG9GeVVmRzdER2FFaVFKSmtHTnFDakcxb1FySHNvODloM2hWNXZVY0NseXQrbytUYndQTnNsQWM3d0N2MExqcHBjMVpTWks0UG9vRGlkVHdWWjJXOEFNVGwvZWRoeTBiWjU1RXRUcGpidVFqN2E3OUM0Tm9VTkFoVUEvOVJ3VDdnQnJtSW82dFM4MmFQTnUrWnBZaThDZ1lCRm9wRGwxb3VOdlVUYzBJMHd4M1VTSXhISGJMRmVaUlBGckxNY2NIbHhONDhyem9Dc2tIQysxYzZXN2huQnN0bHpGS1NXclErMHNoUGliYWpLZ2QwcXlzR0Y1UUd3aFR5WCsyMnV5aEV3M2ZaMG5RQmxLbDBFTE5EUG8rRVJhdThjK3pWVFg2OC9aZDh4dE1yS2dSMFhMeUdSdVFtZllPZkY2aTJkcS93OGxnS0JnRnZsN2F6cU5HeUJ0WmlINGVrd1c0bE9McmcxY0tNem0rQml2eFUza1RjUmNDNUliZGFsTUJBWTZsWHRnQlNpRzBmd2EyU0hZWlRFZndBRysxcUhOaEJqQzQ1Vm50Z01Ld2NlaDZGV2Z0cVQrRjV6b1AvNnFPRndxY3F5aDZTdk4wUUwvSzhLekM1NXlwL0tERU5Pa2gvNGE0SndGM2M2dHliSTU3VnAyN1o2QWhSMkMwODFMSVd2dlNhS3ROYzdZQWFsQUNBdnFRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIM0NlZnVTM09uS09SbTVLWWNrb0EwWEVwR1d6d0dubnAvSmlIeHBJeDBhZ0J3WUZLNEVFQUFxaFJBTkNBQVEzYXVsaHhKR1VYQzYwZnNvalIzWWJ6Q3JhVS8vVFpsS1pqVnY2V1ZKb1dxNk1CU3JwVHpQNWtEZHdsSGJNNDVPZUJuZ0RzSVplQ0xZVmNDUFZ2TWlQ
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVTRWZvb0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1ETXpORFV6V2hjTk16RXhNakk1TURNek5EVXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0hNeHVJT3lubFdJVy80QjhGS2tSU09OSGt5ZDV4NzFKQmZnVG44ajNFMnFEbXJKWG11VnlDUG9GeVVmRzdER2FFaVFKSmtHTnFDakcxb1FySHNvODloM2hWNXZVY0NseXQrbytUYndQTnNsQWM3d0N2MExqcHBjMVpTWks0UG9vRGlkVHdWWjJXOEFNVGwvZWRoeTBiWjU1RXRUcGpidVFqN2E3OUM0Tm9VTkFoVUEvOVJ3VDdnQnJtSW82dFM4MmFQTnUrWnBZaThDZ1lCRm9wRGwxb3VOdlVUYzBJMHd4M1VTSXhISGJMRmVaUlBGckxNY2NIbHhONDhyem9Dc2tIQysxYzZXN2huQnN0bHpGS1NXclErMHNoUGliYWpLZ2QwcXlzR0Y1UUd3aFR5WCsyMnV5aEV3M2ZaMG5RQmxLbDBFTE5EUG8rRVJhdThjK3pWVFg2OC9aZDh4dE1yS2dSMFhMeUdSdVFtZllPZkY2aTJkcS93OGxnT0JoQUFDZ1lCYjVlMnM2alJzZ2JXWWgrSHBNRnVKVGk2NE5YQ2pNNXZnWXI4Vk41RTNFWEF1U0czV3BUQVFHT3BWN1lBVW9odEg4R3RraDJHVXhIOEFCdnRhaHpZUVl3dU9WWjdZRENzSEhvZWhWbjdhay9oZWM2RC8rcWpoY0tuS3NvZWtyemRFQy95dkNzd3VlY3FmeWd4RFRwSWYrR3VDY0JkM09yY215T2UxYWR1MmVqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNTSEczcW5qc0wweDliVkZSZnFuVEkzVHIvL2dJVWFrQ25tVUYwejI4eFhUVkppaWtKM2VWZkRSbz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUlJ2TTN0TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1ETXpORFV6V2hjTk16RXhNakk1TURNek5EVXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRM2F1bGh4SkdVWEM2MGZzb2pSM1liekNyYVUvL1RabEtaalZ2NldWSm9XcTZNQlNycFR6UDVrRGR3bEhiTTQ1T2VCbmdEc0laZUNMWVZjQ1BWdk1pUE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnV0xMQldrb2FlQ2ZzaFJMWVVjR2hvT0NCQjVHbWtsRUthazNrOU9mNE1kOENYd1Q2bjVpVGhCV3loa0ZVVG1Ma25KMWwyeXNIOERvYU9YNmNHblY5cGl1Uk9SOGNDYURwQ2Fha1U2MjU4R2FEYitjbFgzQ2pFSHRQV2pEZ1ZYamJVT2g4WkJDOW9zSm1oZGllT1pjYlM3NzRwZlVENi9CdFdqaHlWTHUvV3oxag==
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVLSzliZ2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRFeU16RXdNek0wTlROYUZ3MHpNVEV5TWprd016TTBOVE5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCNCt6VGZGQTNtNTdpdGt2WFJZcjhCT0RmMW1qZUxpcXpSeUVOSWw2dFY0cUNURlpYUmlVRDN4UlRZZE0xSzczVUw2Q2RGNWs3aWJoSEhTU2hkTVVhY0pOcUFaRVQrWmpDYXBxZHFNTjU2dUdDWkJpS2Q4dlVvaldkbG55bjJtV0JQVUd5K20yWTZNTXFxTGVVdElldTJUcWgrODZoTysvYTRPMGN1dGNOQ2JWbUtNbkgvWEVqOWJIRUYvd0JpNTJuUS81aVFXTVFPbmJwMHNVaC9waGp0QWI3MHR6K2ZCRGlscDZCV2tMdTkrV1gydHQ2dWo5SmQrWW5pWktEVUFhenpCMll1aHdka2FuSHNiVFpSREJPKzlRVXA0RlBKazVLK09GSEVIS2lMUXd4Q3dkWWZVTi8wNlkrRTNLb1RZTjRZYmFKOTNOYU12eXVFT3R2c1FIZUJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCaGVRRTJqRkQ0ZS9LSVRwY1FUb2h2OE10alFIc0xCR0dPNnJGZXhNaGpyVlZxSmlNMFVhYWVVbGpiUWhEZmNDajIyQ0VHa0FpckxJR3VETFRWdkNsa2VOeHRwMHY0bWFQNTBUOHduYmJ5Zi8zVkR0NjFodHFPcS9LZmxXWlNXOGFEUWtGSm5nekpIbWNUQVViOEUxUGUxTExTSHEzTjJ3RlNNR28yY0JzRU5NcjN5TnZRY1M5RWNZa3pRSk9YL21OYWl3M2JXUzUvTXdVRVBTb3ZrYmVmWk41SjZGYWtXRGpyVmRCejlnRTVVdTI0bEUvR3lFZ0VObEJyWmNDVlhhcDhNaWY4OUVKL3g3bk5sYVRQUzJCWWJPUStVZW5jby9WU201U0xyS1VkZXJ0VWFZYkgrL2hKM1gzREZtVFFzMkZEREQ0TW1aaCtrN20xOHdESFEwbG89
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    router lsrp4 1
     vrf v1
     router-id 4.4.4.2
     redistribute connected
     exit
    !
    router lsrp6 1
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
     router lsrp4 1 enable
     router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:07 |
     |___________|_________|______|___________|_________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 nei
    r2#show ipv6 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer      | ready | uptime   |
     |-----------|---------|------|-----------|-----------|-------|----------|
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:07 |
     |___________|_________|______|___________|___________|_______|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 dat
    r2#show ipv4 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 4.4.4.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:58 |
     | 4.4.4.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:58 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 dat
    r2#show ipv6 lsrp 1 dat
     |~~~~~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~|~~~~~~~~~~|~~~~~~~~~~|
     | id      | name | nei | net | seq | topo     | left     |
     |---------|------|-----|-----|-----|----------|----------|
     | 6.6.6.1 | r1   | 1   | 2   | 7   | bf1864f4 | 00:59:56 |
     | 6.6.6.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:56 |
     |_________|______|_____|_____|_____|__________|__________|
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 tre
    r2#show ipv4 lsrp 1 tre
    `--r2
       `--r1
    r2#
    r2#
    ```
    
    ```
    r2#
    r2#
    r2#show ipv6 lsrp 1 tre
    r2#show ipv6 lsrp 1 tre
    `--r2
       `--r1
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
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:12 |
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
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:03 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:13 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

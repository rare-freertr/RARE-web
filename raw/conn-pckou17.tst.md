# Example: ppp with packet over dtls
    
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
    logging file debug ../binTmp/zzz70r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCY0pEcDJvaDlPS0wyN3R6bC91anFZTkNTd3FPdHdQRmVNSmQzUFA4bERhNWxWZit4WnN3RnRPWXpRdTVLenFtZmY2ZVIyUlA4VFpLcjd6VFQrSFU1UkVKZWh1TG9xTEhpL1NxTWtSTUNDVjFZK1NiTlZ4OTZLUjJyeWUwcEJVMDFUV2Z6QUVCYi9GODJzek4vVUlaeUhSQ0pZbnplanRBNGh2emY0N2ZFRC9XYzhOZGJHUXFuN2pmelFLdUZsenVlMjI0eU5uSG9zZkNsazZaRndPWWloNFUvTkZIaWpWby9UL3NsM1E0NmdiNUR6S0VHRjB4cEh4YVpOSzl2VGN4d1FneDVTdmVtMnlQcHdvTEZ0dWx0TUh2aXpxVlN2TlJaVG9MLytYNVdHYUZKYnE5ZTNMb1hIckpHaXhtQ0hqM0pnM3hkNU5KRXJqOExySEJwb1N5YlJBZ01CQUFFQ2dnRUFDOWVnSi9Vb1B0eGZua3VyT1M1UEw1YXNESVI1VmdCN1pBak4zRUFmZHVuU1dEbkx2NitSQkYrOEtHdWpMREkvalhpN0l6UTA4R0lrMDU0SkxJdkpzQU9JNllFYmRDWXBFclRlQ09CSk9iZE4zMDJMbmYvRksxS0lmVWU1UUhJYll4WVN0UUNjWkFiRUtXeGZiQjB4eC9USzBVY05XSjNnbnhlN2N1UHA4UkF0dDcySFoxQXQ5NW5pYmpodW9VS1VsWjJTbER5UmU4RWhDQ2VWNzJZeEVhb0tld29Fb0tIbmowTDNEQ2xpZ240bUQ4Zm5RRlRqM1NyZFcxN2ZGODJyZi93Z3dNdklDb2NKT1YxN1VXV0NkUnpzMVNobWZaSkJVVDd3MWkwcHRxZU9KU1AwcXdrTWJhd3M3ZC9rTEgxY3N2TEZvWWVoNmthaVBYS0Vnc0MxRVFLQmdRQ3R4ZzBza25zcmFyVzZVSXRhZ2lGK2R2akhCdEJScVVUNmYrMnhYOGtaaUs1aUR5Mm5iZ1FSdmVuY1JRZCtOdGVnT2N4d2dSZ2FlRXdFaXQ3TkhvbEpGREo3QTRtQzQvbkNTYURZOE5GT3VIWGFaM3AvVHdjQ1E4NzZSbVpXT3phemFnQml5dTEvVFlac28rc1JrTTNYYWk2ODE5TWdRNGFUdHZsME1DUG1KUUtCZ1FDSHZib1BlZmdsSUQ1SnVwYjE3SnRGY05CUk1DU0U1YnNnSlM5NjAyQTRaVDBpNVl5ZStyVmE0dHFJUWQrMXVUdkZvUVBUN2RjYldFQnlYb09SZjE1QUcxdUd6WmZDMzloL0t5Ukw1TXg3OHJmY1Q5cDVLZzdPc0pja1RFcVZDYkJWMCtsMjFvQlIzRFZ4dkh2ZmdGUTNIUUFHMjdKZEx5T0UrRndYNFg4UVBRS0JnR29XZ1RCMjlPOGFwSHRzZE1iNnJ3d1FBZTB2d2JvNUJyMlBvRU1yWVJCUG0zYU9JYWNYeVRBenF6UW9pRnlMaXJSczFOelNVeTdGeGxMM25QSEk5TE5DdTFiU1gvOGl3dlhVRVhpZi9JaDhvS2FIaWdkeTdhcDZUMEFIL3E0aVZGRFFKQkFzSnpZUzFFQTdDbVdjNjYzWlMxTkt4Ny9vdVo0d2xMWlVOWFpwQW9HQVB5cjVoTzQ3bmZ0TlFUNUZ0aGZ2Z2ZjbjJrQlBIbEZTTFhsZ2lRWUl4dlhGNTVGdlNTUmVkUGNRdjB2NGNUYk1MQUhzS0JtTWVyc3M4b3d0S2U1ZHkvTnZPbUkrZDM5MzNtWVROQVk3YW9yZktQVTROQjV3V1pzd0dzSXVDd0ZCUUErbm01Zmlpeld3NFViWFZvRC9yODRkRHhQNkF3ZEd2a0JkaXZkekMva0NnWUFFVzZCUjZVbS9uVnlNZlNWb0puUTEyVmcrK1ZTd1JrSWhRK2ZVME1IMVBjeVRISVdMM001cFBnOFhaMCsvTW5nQ2s0K3Vhd1M2VGIxeHdFbVhMMHNiUE56dzBnbHBtUnZqMW92a2pyanhkSlJ2NVptVmJKRUh0Vnl6dnVITVlaL3FRMWlGTHB3eEFVUU1lZTBkNUFBeVErYXZNUGNuazZvb3F6MDdRYTE1YkE9PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0MwVU5WcWJZLzZ0OTdoM1FHQkVXc2daWTBhay9GNFB1UzhKSm1GaVZ3ajJZaFFraEhaM1AxRmExNmptV1IzbnpGNUdhODhwYVcwaUxhdzY0TnZpVWRkL3ZDTkljV1hlQVBkcFpxaXpLTWIvM2ZZNVpjSEFJZXVsd3FJZGpiaGlMTkV0RHJ5aTErQUN1M1BjTDY0cXh3d0RuajNBY1UzT05ZRnlYNEl1ZmROOUFoVUFtdWVVQzF1dm1uVlg1QnM0c2I2Qm44UzhkcmtDZ1lBWmNQYlpJdm9SaGZuMzNsbE1icUpYeXJNVlAweGEvK3YwY0YxQUdTT01JWDhDT2FoMTh5d3kxcGJlMmlJUitldUlIamdoR0JHVzJnNFlEN0hCRStIYTdqc2FrUWM2Mk9JQVVZWmRHNXhqUU5TN09hd01CUXlBKzd3V0NlSGtzdUFnYmQzSzZoRTBkM0ZzUEtQamN5eE5vVStqMVd3WE1qbXNNa0RoNmVBNGVBS0JnQU9SMjdtMTkwVnR0SlVpd3dtYkhPZk1rejVScFpaa2p1VnpneTFJSE5ITG9Mb3NXSll5bUM1TlBhMmdsaFY2R2dHaGxXOGtLQ2FXb0VFVThhSlc2YWxqWng3TFVSL2o2THJpenVOR0ZwdUpnNks2U05VS1VuN1NMeWo1VVhGL3JpZkVPWkpyOUErUWNZSitneGtJSWo4YVoyc2xkb1pyWHdxbGtvUmlrTC8wQWhSVkR3blNSMDNpSEs4Wkswd29EOVpFaXJvME53PT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUMwdzdVTE5mMStQQlZvVE1wM2NmNmpISXcwZCttNkZCQkJXbFVjQjZVOW9BY0dCU3VCQkFBS29VUURRZ0FFVFFFTFE2UFEza3ZLV3k0WUw5M2N1V0wwZ1hnUTFQSFJZNnMyOGY4RmFxalhjS0ZmZi9yczlqZXhpd3cwME1NYjl5cXNRZjlibFV2QWZYOGRsS3FwdXc9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVISUhoMFRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXdPVE01V2hjTk16SXdOREk1TWpFd09UTTVXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0MwVU5WcWJZLzZ0OTdoM1FHQkVXc2daWTBhay9GNFB1UzhKSm1GaVZ3ajJZaFFraEhaM1AxRmExNmptV1IzbnpGNUdhODhwYVcwaUxhdzY0TnZpVWRkL3ZDTkljV1hlQVBkcFpxaXpLTWIvM2ZZNVpjSEFJZXVsd3FJZGpiaGlMTkV0RHJ5aTErQUN1M1BjTDY0cXh3d0RuajNBY1UzT05ZRnlYNEl1ZmROOUFoVUFtdWVVQzF1dm1uVlg1QnM0c2I2Qm44UzhkcmtDZ1lBWmNQYlpJdm9SaGZuMzNsbE1icUpYeXJNVlAweGEvK3YwY0YxQUdTT01JWDhDT2FoMTh5d3kxcGJlMmlJUitldUlIamdoR0JHVzJnNFlEN0hCRStIYTdqc2FrUWM2Mk9JQVVZWmRHNXhqUU5TN09hd01CUXlBKzd3V0NlSGtzdUFnYmQzSzZoRTBkM0ZzUEtQamN5eE5vVStqMVd3WE1qbXNNa0RoNmVBNGVBT0JoQUFDZ1lBRGtkdTV0ZmRGYmJTVklzTUpteHpuekpNK1VhV1daSTdsYzRNdFNCelJ5NkM2TEZpV01wZ3VUVDJ0b0pZVmVob0JvWlZ2SkNnbWxxQkJGUEdpVnVtcFkyY2V5MUVmNCtpNjRzN2pSaGFiaVlPaXVralZDbEorMGk4bytWRnhmNjRueERtU2EvUVBrSEdDZm9NWkNDSS9HbWRySlhhR2ExOEtwWktFWXBDLzlEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRnpCMXJrK0pkSzU2WS81Q2tSSkQvQ1cyQko1QWhSdmo5TXJId1VQZWx2dENENHlmOG9sMzFqRVdBPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUlFwZUdNTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXdPVE01V2hjTk16SXdOREk1TWpFd09UTTVXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSTkFRdERvOURlUzhwYkxoZ3YzZHk1WXZTQmVCRFU4ZEZqcXpieC93VnFxTmR3b1Y5Lyt1ejJON0dMRERUUXd4djNLcXhCLzF1VlM4QjlmeDJVcXFtN01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBhckpTaWt1T3M2YVA1RHdJcStCbTRXckpURndqU3VXbEI1TmFBdk5vQUxBbDlYRFRKK1RrQ0RKL1lOdkVyNjkwVnBBanVveVc1SFVuYXlYVEVnQjBubXBKYzIwYURyaTZlejFNcjA2MTZqWGhSZkZVTzhYa2hwRllFdDZ1cGRGdUVkaGY2c1M5LytJa0lPUUdZOFZEb3JOTVMzTmd0eERDM2lmdzJQZGxKMkhBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVKV0ZMNHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEE1TXpsYUZ3MHpNakEwTWpreU1UQTVNemxhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCY0pEcDJvaDlPS0wyN3R6bC91anFZTkNTd3FPdHdQRmVNSmQzUFA4bERhNWxWZit4WnN3RnRPWXpRdTVLenFtZmY2ZVIyUlA4VFpLcjd6VFQrSFU1UkVKZWh1TG9xTEhpL1NxTWtSTUNDVjFZK1NiTlZ4OTZLUjJyeWUwcEJVMDFUV2Z6QUVCYi9GODJzek4vVUlaeUhSQ0pZbnplanRBNGh2emY0N2ZFRC9XYzhOZGJHUXFuN2pmelFLdUZsenVlMjI0eU5uSG9zZkNsazZaRndPWWloNFUvTkZIaWpWby9UL3NsM1E0NmdiNUR6S0VHRjB4cEh4YVpOSzl2VGN4d1FneDVTdmVtMnlQcHdvTEZ0dWx0TUh2aXpxVlN2TlJaVG9MLytYNVdHYUZKYnE5ZTNMb1hIckpHaXhtQ0hqM0pnM3hkNU5KRXJqOExySEJwb1N5YlJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFDK1VPYzI0TFY5R01zeDF2KzVMcXFqUjUvSTRMamtWU2VUeVdsTlRkZXpVTEdUN1l6WWt3VzdCYmdZWjgxSmUzMTFiNllJV29IUzh1U0FHdEZKb0dLY2FjamtxMWlKL1BNQ0JndzJCWCtBM1hEcU5vV1ZSTDBjRjJhWldZWmdZY2NUVE9TZ3RBVzJ4SklwQzBTQVFIWmlBMFZOVkFKVm9WYjlmeHVOaXgzdFZ1SVMzUG93WGJyYkFQK2tkNlR4d0E3NWJGWHBya1BKSjFTN2Q2MVlueDJ1UkgxTVRURTFyamw0UHZGNGt5K2xNSGF6U3VrQ1NiTFhXN1RGMFlXY01STlJvRjNlU0hNc1lFRHRRWUMxOFJMUUcyNlVTWnpVSC9nWDZ4M3NxZEsxTmNHTXR2ZzQyWEFWNTY3bklwc0JMUmhhdmNFMngzYjlCL3VYek9iYk5OSEk9
    !
    ipv4 pool p4 2.2.2.1 0.0.0.1 254
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
     ipv4 address 4.4.4.4 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
     encapsulation ppp
     ppp ip4cp open
     ppp ip4cp local 2.2.2.0
     vrf forwarding v1
     ipv4 address 2.2.2.0 255.255.255.255
     ipv4 pool p4
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation hdlc
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
    server dns dns
     zone test.corp defttl 43200
     zone test.corp axfr enable
     zone test.corp rr www.test.corp ip4a 1.1.1.1
     vrf v1
     exit
    !
    server pckodtls pou
     security protocol dtls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     clone dialer1
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
    logging file debug ../binTmp/zzz70r2-log.run
    !
    prefix-list p1
     sequence 10 permit 0.0.0.0/0 ge 0 le 0
     exit
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
     ppp ip4cp open
     ppp ip4cp local 0.0.0.0
     vrf forwarding v1
     ipv4 address 3.3.3.3 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
     exit
    !
    interface serial1
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     security dtls
     vrf v1
     exit
    !
    proxy-profile p2
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target www.test.corp
     vcid 2554
     protocol pckodtls
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
    client proxy p2
    client name-server 1.1.1.1
    !
    end
    ```

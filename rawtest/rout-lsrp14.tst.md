# Example: lsrp tls encryption
    
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
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCOHAzbm45UjJLZHgvbHk4a3FlY0ZFeWd5OWU2V3BDcnlNSHdEMm9kTG1BQkt0UzJ6SVl1ZHJ2Mlgzc2RZcWgvbVVLSEgvZDc3YjZRZHZCNnFCaWc1MXZFc28wNG5QckRUeVI4QnhLWWNTaktiRWMxcTZZR0ZLeFVEdXFQOUZUYjd1dEZUVXBIa0c0eWo4L1d0bkZxb1dwQjVWQ1ZwSXNrV3p2bUZBZ0lqNzNsWjUrOUF0SWJKa21BWW1UeFNGLzI2Qk1rbnVia3RlV09jZDcya1Q5Y1hnbmQrbEVOTU5WS25TMC9obUlsc2pGbThmUGZaK3d3c09mUGdMd3FaQWQveThrWmg5U3RrdWZ6ZkxqeW01T0dESC9pWXE2cy9lNjNpZnp5L2NmcDNGSFJjcDlFd3QrUG52TXFPYis0NnpOM252b1ZBNTlMcVJWSTZZQnRLemYrZExBZ01CQUFFQ2dnRUFZMFoyUGhmbXVQbjZlMmI3QlVzR2N5Ui9WUUQraEV3NnNWV1h6TlJBUkZEV2p4RTh4N0tOSURERW9xb05LTDQyTkpxcGY0MzhnT05ydWk5ZXllQUxlQlRIdnZJS0ZVek90ZzRTNDR6eE9BS3dabENBZDJKKzJhK1M4UC9DblkwM2ZLQTkxMFJONXdCUENuMUJaazZVazRlTmFLZ1VNVVZaWWJkRGVMMWxXMEV3TGhXTU0rcmlXdnhRQzluUW4wYVdxd29IU3d3U000ZnhhUVlKOWtPNmp4WUZ0VlVYdTJvaFFuSjRyVm9yQ21iZ3JBbjBxNVlQdkpXNnFIRERJUkVWcmc3c25aVVBDd3h1aUExR3NVMUJ0Wkl5ckUzVW45N1d1dWQ1YXRRUm1YaXRJQXZBd09ta1RQWUZlbU1PZ1lKSDlDTmVLOFZaUzh4Q05MNTdkTERWd1FLQmdRREJRWEpBOWVyKzdtMkdUbGpKbnRPVDh2amxpN0pZeThTWWttVlAyVlZ1Vkt6bXJkMW83eTFQaHpiRGUyS1ZOMjZwVWtxNTRQalZveXlicDQ4SjdOMGRWZncyd2tiYjRZOFYrUHRsZUlLMkNySzdjRHRBY29IODhYanFMWlpzVGx4N3pEbTVRbVU4ZUZKMzBIejRXU00zakNjMWJTQVBGMUcwREhSc2xsbFRPd0tCZ1FDbElDNTU3bnIwWHo5amdNUC9KZlRTaUgzekVmbW5RYnB1bEE2TldtR2luLys5NTh2QWNIeHErb1VSMXNES21NM2pKL1hMS1VtNTluY1FOYVgyZDZueVA4T2U1b05EOEVvUmRUWDJ4Mm9xNnJhYTBDK1VpU1daR2VOU2ZqY0N5dEdrcHZqeTd0SjNYTUJST2VYK3lweEtoTVlna29ac2IwMGhzdVVmTkdOYk1RS0JnUUN2M2RjVHRyZDc5NDVFUXRnWjR5ZTM0ODBOVit1ZFV4STlwanY4UmxPd2ErNU1ucngyMmZIcUJhcVlpcGhVSW5YYU1NRkFGck5iOTNxSXpCc25kUjVqcS9ReUFPcHEvd0V2aGIyQndnRnhtSnErYUl3RFFqRjQ5bWFLOWFHR1BtbDdYNGJJU052SUE5ZElvYnFZWnNYZHJ2V2ZjUWRUdEd6dDVNZXVhY1F3TVFLQmdDK2dCb2VZWnRJUW5xRytROGxWVXpWZHRLWGtxMUs0UEdNa1JNWTBLVERVWU5pUEFFOHlvay9nalh6RnFibEZOU3l0RzlGS3lUN2ZmUnVwdllKR3BUZC9lSlpkK2NJZ2pkeFhLQWRUSUtYY0tHcWlYUGJFVDVuR3c2L0pRMmlFd3M1d2NpRHZETGpzZ1hOcjlZLzFNL3F5TE1xOE9CVVNUUGJKT0JnMTdlb2hBb0dBYlZGMGJlR2h6d3NWY2w2NXg4RjdNN2dha0MxemJ1ZEN6YUdRSzBxeTdvaS96Nmt6NXpDWVNWK1lmNG9zNXIwNFVrMHZLVTgxQlJUcXVRcjZKeW9KUVl2d1Y5NnZNYmJRV0lBbkhsOUtpdGo3RmNpcytTYXovWnkwZkNmVlVESHIzd0NyUW95b1ppcDUzMTVYSlhjMXpOc0dPSVVoN0ZUQ2hBNW9JQXhqb2ZFPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0RKbGhwMEs1ZDlzR1ZhdnJPVU1ja0RtOTRrakwwTVR6RGNwZ1RBNUtaZTBUeVU3Mkc3TWhxN1pDcEZNQVB6ZjV0Y0w3aldYcnhVWERud3RrcUhNNDJUd3B0Q3Jzdnh5MFQ1L2x3VHZtcExMdmdoOUYxODYySmlTb1ZheWJjdHVrVitEYlZGY1dmTW5MUkV2ZkJGZ0VyUWZkdkZwOUhlVUFzQmgwME5oWVRacEFoVUF4OXVnNzZtd1B6LytoNXN5UGluM1ZPUkRscThDZ1lBaXVzTFJMYVQvc1lZNXFEVUFtdGMvZXI5SWVLSm1wYjZQQ0twTnVnRGZLYndjRnNXS1RFSnJZVkhIUVF3dVhEdFMrVDNobWRmUjI5VnpBTXFpSFNWekNPZXYxcVBHRmM2UnJZMEZwNHJWbElpNCtIc1pGK2R4UlNweDJGTDFhLzd5ekpNTmNuMjdDcENJTWcxMXAzZXpwSDZHMGs4ZkVHNjI3RmtvSWpqRjF3S0JnQUpTWG9FcXBuN2xlNzBXYmFlOGwxMVVEWjdPMDcwZjBqeWpCOW9hK2R6d1ZXc3JGZ3NYSk9LRWRlN2NGQ21NRTdNaCtHSVlZZy9rWUg3YWZldmFTSEtqOHo5c1ZCb210Q24xWmJ3Y1VIOGtJVTFadFFHUzdha0F4bGlmZDRkazBjdy9yOVVzYWZDNHZNQU15V2JMWjNYanhPTHdmRHZzWm5iYTVNYUloRURrQWhSL2hXUnJhRC81N3F3UjYraHFVaStFMC8zM1lRPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeTZnbFNMMm5PTkZJNFQza0dxRkxINnVCamRVUGlSVDc5bGxUOVNNenBpZ0J3WUZLNEVFQUFxaFJBTkNBQVE3WW5qYlBtSFhicUNKbkVFcVp1UFdDNW5nRk1Kci9lenVQMEYxOEc3THU0WmxUTXYxcWQ2dzdnbEhFci9YZkZETVpiTk9WMXJvQms5aFdGNGRXcU8y
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVUOFkrVkRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1ETXpOVEV6V2hjTk16RXhNakk1TURNek5URXpXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0RKbGhwMEs1ZDlzR1ZhdnJPVU1ja0RtOTRrakwwTVR6RGNwZ1RBNUtaZTBUeVU3Mkc3TWhxN1pDcEZNQVB6ZjV0Y0w3aldYcnhVWERud3RrcUhNNDJUd3B0Q3Jzdnh5MFQ1L2x3VHZtcExMdmdoOUYxODYySmlTb1ZheWJjdHVrVitEYlZGY1dmTW5MUkV2ZkJGZ0VyUWZkdkZwOUhlVUFzQmgwME5oWVRacEFoVUF4OXVnNzZtd1B6LytoNXN5UGluM1ZPUkRscThDZ1lBaXVzTFJMYVQvc1lZNXFEVUFtdGMvZXI5SWVLSm1wYjZQQ0twTnVnRGZLYndjRnNXS1RFSnJZVkhIUVF3dVhEdFMrVDNobWRmUjI5VnpBTXFpSFNWekNPZXYxcVBHRmM2UnJZMEZwNHJWbElpNCtIc1pGK2R4UlNweDJGTDFhLzd5ekpNTmNuMjdDcENJTWcxMXAzZXpwSDZHMGs4ZkVHNjI3RmtvSWpqRjF3T0JoQUFDZ1lBQ1VsNkJLcVorNVh1OUZtMm52SmRkVkEyZXp0TzlIOUk4b3dmYUd2bmM4RlZyS3hZTEZ5VGloSFh1M0JRcGpCT3pJZmhpR0dJUDVHQisybjNyMmtoeW8vTS9iRlFhSnJRcDlXVzhIRkIvSkNGTldiVUJrdTJwQU1aWW4zZUhaTkhNUDYvVkxHbnd1THpBRE1sbXkyZDE0OFRpOEh3NzdHWjIydVRHaUlSQTVEQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRFdhdUJDbEN0NiswUC92M1lubkN6U2Nid3JUQWhSb21FRmtPYlByb0pramVHTnhBcVJSL1hwS2lRPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUVRmQnpxTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV4TWpNeE1ETXpOVEV6V2hjTk16RXhNakk1TURNek5URXpXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRN1luamJQbUhYYnFDSm5FRXFadVBXQzVuZ0ZNSnIvZXp1UDBGMThHN0x1NFpsVE12MXFkNnc3Z2xIRXIvWGZGRE1aYk5PVjFyb0JrOWhXRjRkV3FPMk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUxpbjRmVjFVMk54R0VRZzNkNjRVVXkzMTVtK21EaVptb0QvblZsTXg2OGJBbDhRZUJSK1pLa0xvVkhxWlcyeFh0djNKNTNTSm9mbE9UTjJUbFVRVVo2NUt5Z25JZlRqdnowTG91cnNrOVR6SUNRczg5MXZITy9acHNTTlMrNnlxWXFEUFR1OXIrWnZ0aHE1dmEza3V4SW5VVkoxTG9UOUprM0Q3aDZCajYzRGRBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVQSzJkalRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRFeU16RXdNek0xTVROYUZ3MHpNVEV5TWprd016TTFNVE5hTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCOHAzbm45UjJLZHgvbHk4a3FlY0ZFeWd5OWU2V3BDcnlNSHdEMm9kTG1BQkt0UzJ6SVl1ZHJ2Mlgzc2RZcWgvbVVLSEgvZDc3YjZRZHZCNnFCaWc1MXZFc28wNG5QckRUeVI4QnhLWWNTaktiRWMxcTZZR0ZLeFVEdXFQOUZUYjd1dEZUVXBIa0c0eWo4L1d0bkZxb1dwQjVWQ1ZwSXNrV3p2bUZBZ0lqNzNsWjUrOUF0SWJKa21BWW1UeFNGLzI2Qk1rbnVia3RlV09jZDcya1Q5Y1hnbmQrbEVOTU5WS25TMC9obUlsc2pGbThmUGZaK3d3c09mUGdMd3FaQWQveThrWmg5U3RrdWZ6ZkxqeW01T0dESC9pWXE2cy9lNjNpZnp5L2NmcDNGSFJjcDlFd3QrUG52TXFPYis0NnpOM252b1ZBNTlMcVJWSTZZQnRLemYrZExBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFIZUZXOVV5YlY1a2YzMDhCeSsrc21rQlAwSWdtY2hQZ0xOVVMxS2M0UURzbTBSOCtXc21icmlIM2d2YjkzcEgwUUJTRmFTeUV5Nyt5ckx5Nk03Z3prczUwWE9LcjdEUW1XUTNMQW1waTFLaTVDbm1RZzNJeVVTamJBd3I1eHNQbTlMbGNJL0NZaWtJTExJQWZCUlRiRWFXelpOUVprNkRYc2laOFc1WW1ZTXVtVS9YakdrcDRJUkhsS3hUTDhUVitZcWQzeTMwM3MvMXN1N2pmNDhzSmJ3RFdVTU5MdlFyOVFuL0NPNnl0SVVqdWZPSGRwWWZLL0kzZ1M3MkVsQVd1aUhHTkdkRnVRZXNSa09ETXJzTlRuWW53M0l3NWQ2YUVVVEJuMmV2R0llOWl1Nmg1UVBvY3dpOVREckUyQ1JMU0Fvdk1CektoRlNoVVNiN29TenUxUms9
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
     router lsrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQXRsazZWdGFLOUZHVDZYQW5uR3lZWHNwTER5UHdTY3FyZWlyRzR3b2k0R2VBUWpDd3pmdk9hdGRzemRoYWx2OTY1Z0c0OUFpbG5EWU80cEpaL1J4WnByK3NObmlmK1k0U2VLejJPaFVBTHdoWTMyREJvWTRYeUQxUlRUQnZ3ZDJmUVYxUGxDamtnZlg2OElDSklodjZuTWN0dzZ2NDRjVXBKWjQycUNvd041dDA0RjNBMDBaWXBTL3JxWDJMZDdNbUs0YnpNY3U4a2ZMWUdWbTYvenUyNCtBYVpXTEh3MUtaUjFnM3k2MXREYUFpRlYyUGdTNVh0RXZvMTJvKzdWaUtOZ3NyWWZONEEwN2FtdEFLeFIwZytHNE1oZVhNUUtmcnA4NHFTR3RmaUhVbGsxalBqeFNQMVc1K2lJU2E3ZlhqcTNOUms3czkxZ3lpV2JNN1JGZXRDd0lEQVFBQkFvSUJBSE9DcEdVYjlOdjl6VS9EM3lQRTJ1UzVDc0VsaC9LR3N3ZHBqNkdFNjBEeDc1cCtVNUc0WURMb0VpRjNXek5wMVVWY2MvZ0tmall0UEZLa1dPTHdrWTRDdnltbVVkaDQraFI5cEdCNHF5d2dBb1JHTzRLR2kyUXFDNVYxQ0dacmFKVzBjVk91YjhvdnN1Mmt6cm5QdFhxWTVkR2MzOFRNNjFyTUZWMkRsQlcwajUwdlNtRmx3M0NOY1BtSVdDMThGTTM1dnNMY1BteE1iNnMzTjBCZWRZd1NzUG5XTi9maCs4ZWNFWFpMT0I0cW1jUW96c3NwZnd4d2JMYlhqL0R3dHJkOHkrL0t6THpVN3IyV0NZREh6UzZEcjZPeExxV2FzVmFVL3lsN0tSNjhGays1Y0d3OGd1T1JIbTN3cUJFaFF5MnhZTi9mUDJ5YStyeXcrNzBJYTNFQ2dZRUEyci9ERzIvcFQ1bEppZ255Y3Q2YjB2bDM2KzZIVlI1dFJsaHNSMHN0QVNyZ2V6RVNWY0loVS9FTVhNSllhOW1ES3A4cmZES3pMUWtQOGpjMmdKRllkUFpjaE1TNXRybXRqanRiMmQrT0F5LzZ3aFpiUVhab1dyWTZQeTdwelREUTNubDFRS2U1Y1l5ZEVMRW8xV2NwanNkK2FkMVFZOElzNEpPTEt6aXFvdWtDZ1lFQTFXYWJMZFhETHZzQ3dZNEZ3c1N2c0ozcG9XaG9YWFZSS3Nhd0RsTElsM3FuZnpXbXNsVVg2cUFCT1FFelVpOWtNaGYvNWpyamR2SytXNngzS2FWeDMrSVNpZG1vak9zVGFUcUgwd3o2c0xKV21uK2VRcVpzNGoyS1NiYnlJdXZtZVdoODZyU2pKMmtKcDUxRGpMd2l5aGlya0dnUFFvTnlmZGNnMXRDUno5TUNnWUEzMFdUazFHcXhjQWp1MjFqdGJOWlFRRzRVV3ZwWGd2c1pUeWphREZuQWlZTmNqQW9FcmhPNUNySS8zU3VZNFpqeHdFbmxXRDZXU0ZDMFd0aGllRFFkTEZ3eFdNMld6Y3gybGJqN1lHc3BidzNLaHMva1pXVjllREJtdlA3VjZCWDBId1FIYW9VTWIzZ0lzVndkRUVUdmRRSlIyekpQTWxZblBCN3YrWGE1T1FLQmdFUWNGSWtqZ2NGYjRmeE96TzNtQXNFWEZYc3JyS3V2aHZGbEtzblhpQ2c0d0g3c2E4RGRRZDNqcGFCQkR0VTdSUHBzQ0lPOTVkMlFDa3VPRnhaV3RLcWxLQStSUmFkOFc5eXBEckxBb0w2R25QZUFwYzFWK3NpV3BhMXpVNExyMGNxTUc5cDVQdDJVTzcyZ2h1L0RHRU55YmtlUHZ0Y1d4eEw4OTRFNFhtRjdBb0dBRVVteUZXRDJYa2h1L2ErcDdvcjZRYm1HUytaUUovbitPOHZDbGo2OHkwNDlUNTQ2UGhIL05iVEZRd0VBZkQydGtZUTNmYTlLWjM0MjE0akZBY3NiZWxtS1N3ZncxMWxJRWwrYUlyL0Zpd2JCNnNDWURhV20ydDBTRWFRK3kxNEw1R1RTSmxFZS9xbDBTejFNVEV0Z3lIZm8zcEFQeUxyeGI4Skd6eXhmMVhVPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0ZNdEhhMGQ5NzF4QmV6MlpHQ1ZwSmtGOENPdkJJS1kxUENWZDU3bk80L1JyS0FvRzNuTjEwejNBczBhczM2aGpHL0JXY1VlK1d3bjh6UHozK0xFL0JPR2RDTDJ4T2FQcjRWaDk1VGtkWUNDWUplR2V0eUdqdHE3L0kvUUxqMFptdEdHQjJ5b0VQT0pucjR5aFhKOG9zY2xrbDQxcFk2eERhN1o2Y3pqZ3lUekFoVUE1TXo2cS9UUzE2MlJHOEExcTVEQnBkRmxwdDhDZ1lCRUo3YkVCWm85TmtpazB1WTNvMWM4dUpYNFVNcWtuck5CSlFZZ2V1eXZ5UzJra2V6VEFEVkVCVC9DdmpVMGh3cHhUUlBONDZQRE0zdkhrMmZXY2g5RHA3K2lmMmNPREtrdXVORmJoL3ZnS056c21VcW0yb096WkVzNTVxdFQ3UmFGb2g4QVM2bGFBU0V6cWREcHlQY2Z6TWNnSk9WUzdTN0FzRlpOMzcrRnZnS0JnRW5RSkxCOEVOQ3RHOHMwTjJvOFY0YWt1ZXpHdldxczQzN3RzUGJBZjlNZ1VhNDVyN1RTd2JmM1RtcTRKSHYzeERXUSt1cUQwTU5RL095TjFJMEtpdnJ5MzNpMjRuQmVEM0FidlZia05sTmxVU2Fyc2hyd0VSckIyelBxVWF0MjhqSmwyanZKalFEVk1sck55WkVoTGY3NEV2NVorWFRLSW4wdnZGVy9wcjlGQWhVQWsvMFJMMXZBbmtzMUhkZG5jNndsYWtvdG9OZz0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIdzN6eFlBWkFkajNxdWVUTER6U0hFR0ZvdkNOK0NNRDBqQTFqWE1hbHU2Z0J3WUZLNEVFQUFxaFJBTkNBQVNjcEVWWU9BRHpuMHl2dkRXUGxtMWpLMUdNTGF1S2hVb0FYYVJ1L1pxMEJmUENTL3ZKLzM0NVJGRENSMGVORWcxeVg4UldlRTZKa2k3cHgwdW13SnRi
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVFaTJraURBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1ETXpOVEUwV2hjTk16RXhNakk1TURNek5URTBXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ZNdEhhMGQ5NzF4QmV6MlpHQ1ZwSmtGOENPdkJJS1kxUENWZDU3bk80L1JyS0FvRzNuTjEwejNBczBhczM2aGpHL0JXY1VlK1d3bjh6UHozK0xFL0JPR2RDTDJ4T2FQcjRWaDk1VGtkWUNDWUplR2V0eUdqdHE3L0kvUUxqMFptdEdHQjJ5b0VQT0pucjR5aFhKOG9zY2xrbDQxcFk2eERhN1o2Y3pqZ3lUekFoVUE1TXo2cS9UUzE2MlJHOEExcTVEQnBkRmxwdDhDZ1lCRUo3YkVCWm85TmtpazB1WTNvMWM4dUpYNFVNcWtuck5CSlFZZ2V1eXZ5UzJra2V6VEFEVkVCVC9DdmpVMGh3cHhUUlBONDZQRE0zdkhrMmZXY2g5RHA3K2lmMmNPREtrdXVORmJoL3ZnS056c21VcW0yb096WkVzNTVxdFQ3UmFGb2g4QVM2bGFBU0V6cWREcHlQY2Z6TWNnSk9WUzdTN0FzRlpOMzcrRnZnT0JoQUFDZ1lCSjBDU3dmQkRRclJ2TE5EZHFQRmVHcExuc3hyMXFyT04rN2JEMndIL1RJRkd1T2ErMDBzRzM5MDVxdUNSNzk4UTFrUHJxZzlERFVQenNqZFNOQ29yNjh0OTR0dUp3WGc5d0c3MVc1RFpUWlZFbXE3SWE4QkVhd2RzejZsR3Jkdkl5WmRvN3lZMEExVEphemNtUklTMysrQkwrV2ZsMHlpSjlMN3hWdjZhL1JUQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQlE1WkRmOGtWa3owdlZwTWczbFVnZTl2RHZyQWhSYTFQUTdVQk41c2pnTmdmSnYyMnNjMStZdmxnPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUm1VMkEvTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV4TWpNeE1ETXpOVEUwV2hjTk16RXhNakk1TURNek5URTBXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTY3BFVllPQUR6bjB5dnZEV1BsbTFqSzFHTUxhdUtoVW9BWGFSdS9acTBCZlBDUy92Si8zNDVSRkRDUjBlTkVnMXlYOFJXZUU2SmtpN3B4MHVtd0p0Yk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUxJaTBMcGFBS0gxVlM1TWFqZk9zZ1k5U0NFcWlxRk9WWGtUQ25yOFcrOXRBbDhGZ1ZHa1FBendWMk91TjdjUVp3YVdpV2lxU0hsRU9FeUhyVkVMZURpSTNkTFJhUFVsV2FhcU45RW9CZU1yenVYY01ZdGtsU0FMODJySjIrYTBoazZjL05ZQ0F6emFrWDVLNSticVdtbElHNTRlcEF2UGNyOGdmcU1TQnQ2L0dnPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVEcVhvZXpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRFeU16RXdNek0xTVRSYUZ3MHpNVEV5TWprd016TTFNVFJhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXRsazZWdGFLOUZHVDZYQW5uR3lZWHNwTER5UHdTY3FyZWlyRzR3b2k0R2VBUWpDd3pmdk9hdGRzemRoYWx2OTY1Z0c0OUFpbG5EWU80cEpaL1J4WnByK3NObmlmK1k0U2VLejJPaFVBTHdoWTMyREJvWTRYeUQxUlRUQnZ3ZDJmUVYxUGxDamtnZlg2OElDSklodjZuTWN0dzZ2NDRjVXBKWjQycUNvd041dDA0RjNBMDBaWXBTL3JxWDJMZDdNbUs0YnpNY3U4a2ZMWUdWbTYvenUyNCtBYVpXTEh3MUtaUjFnM3k2MXREYUFpRlYyUGdTNVh0RXZvMTJvKzdWaUtOZ3NyWWZONEEwN2FtdEFLeFIwZytHNE1oZVhNUUtmcnA4NHFTR3RmaUhVbGsxalBqeFNQMVc1K2lJU2E3ZlhqcTNOUms3czkxZ3lpV2JNN1JGZXRDd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQVZ0Vk94RGJCdEVYTjFQZi9JTU5oem5BUGRDeTREc29wNWR4dkEvOStIaElGNlVzZDBJRmVjQ0tPdWNDNW1EbDM5WWdOV3kvZE1NeVJ4RDBoS3pwaGU5Rm5qZEo0WVlUbTBZZE9lWDMxcGgyWmZYMWJPUTBhWVZTY1BsdlJ2aHVMcEIxRURtYlRhaUJNMXlOYzJWaHJyVUMyazhvQndCbHdkMnJOWmlxSm15SVo1Q2QrQXJTbXhLVHFiMzVJMG9xbGREajR5MWVHaGZBbzVUU1NCMTFheWRVV0E0S2ZnRVNCazJneklvd21mTlJIVVUxV2huYVZtNVlDYW0rNjFwMTJEYnpvcVZiZG5aUlJBTXlIRCsvZW1oR2JPT1k3VzVKcmh5VGhDamYrcWhkbjJDc25qQkl3L1QzSnB3a3NOemFBTTcvK283MTdOSjllQjlQSW0vNmhz
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
     router lsrp4 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
     router lsrp6 1 enable
     router lsrp6 1 encryption tls rsa dsa ecdsa rsa dsa ecdsa
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:06 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:06 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:59 |
     | 4.4.4.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:59 |
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
     | 6.6.6.1 | r1   | 1   | 2   | 6   | 58f0e2a5 | 00:59:58 |
     | 6.6.6.2 | r2   | 1   | 2   | 7   | f141cf47 | 00:59:58 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:10 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:10 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:10 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:10 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:10 |
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:10 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

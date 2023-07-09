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
    logging file debug ../binTmp/zzz44r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQXRkVWY3VytrcTlEMFFQenFBcG5VRTJrbkg2ZzZsanFxMmZ6Skd5RnZyVUVRZWRubnFObGd3ejlDSjhRcitsS1BveDdVcytka091UGQzOEx3dXVYK2E4VlJDSFd6bUtDck1NZTIyVjdmWkc5dUF5S25OR1VGK1VHRlFORlk4VWVRRW1zZWg2aWpQT2U3eERkWnZyRUlobWpGMFB0SXhtVkIzK282Q0JsZG1QamlvTm05K2pPTWxzM1VCaUR2TXhLMHF3L0c2TjlVMGpBTHkvN2w3aXZXS1pkMVdqZDJzbjNrcFQ0UjNuR2dBWkVWQ1o0K0VaVGFvTzhRR0JmWWdhSUNMcW0vaFV6QmFxZEFZRzdvWGEra1BhOHo5VWVmd0xiaWNvRVFCbGlCWjZzSmsxeHo5OTdrUGZyMEJLSVByNE5aYXVnZDIvOEJYUy94aGFEMi9ickVvUUlEQVFBQkFvSUJBRzJwaEtEcE5USWVTa0VyaDJKY0xlZ3JBZHA0MWlTbWEwWWV5NWJlT29FTi9ZYlBvWVJXM2FIRGMvMlJ0VWc2Sk1DbkpuYjl0WmhDdHh4dGNFdjN5OUpwWlM2cDljKzJEcWpUdWZZczNxT3ZCSFZGbi92Y2RaYlhLaXRtVnJMbGl3Rmdzei96dDhkU3B3NTJwMXgzWG9IWmpIdzJJTFR1ZXFVMW1Sd3JXQ1NaNWt4MHZSY3plUHVmdjdPRGhPV21XWVIzS0Mra0FaYVNUWmRpYktKMzFEQ2h4bVpRdHlWYy9PYkRucUo2ektEbjI1aVNYbXF0TEI2VHFSNTZ1czdlK0Q2aDdNcDExU2xoWmsvdC93WDl5cm0zb2p4RzRER24ra2FyM0hTbHRLenpJSUJMOEkrdmovemxoTkRqT2FYNU5YOXFobnZ6TmQzOTg3ZkxHVjBuL3VVQ2dZRUEvWFB1SFFiNzR3MXhJZGJoT09GVWRERk5JaDRkYmZWaU9aeUhrUjMxWVNXeUoxOFNJTFhyTTVqSWwraTViaHdjMTlXajFRQVRRVlEwQ01XRHVYOFh1a1plME0wQkk0SHJ5d3FLTkp4akdFa1h3aVd6ak1sWGluZXZ5SitwWWV1eXR3bXBta09JZ2k0eU5tdUVJbm95aEE2OHI1dFdrTm4vbTRVb0hMZ3lXQU1DZ1lFQXQ2anZBem1Eb3FBRkk1Wk8zem4xVmtDUWw2YlVLS05vQW1iT0JsQlhyZXpFVXU5dlVaVHhDRmlheGp6ZzZIZ3R6S1Q3S1cwS1o4K3VwemVjRmZ2VE5jNlhXZEhVYmwzLzV1RlI0K2szcVJYVjB2UEIrcm5yR2xxc3g5cThnamgyWVRGQTV5cDRFL3hvamNoc2k5ODJiSXZzZlJuZXBWNkdNSGFiRG1JWnFZc0NnWUVBbjlNdU1WSEpIem5Id0k0UFFsNGRjcFB3VHZac21uMWxybXk5dEU0UEFXN1M5QzdvY0lZblJrY3ZIMVFiTW9zNXlRVW9wZFhCVHEzNWpocDNZVTc2dUhWTnJ4L0hld3VmbEU4V0xlejhORUZMWVJ1REtPR0NlWWZWNm81OE1vcCtEUnhqdmlxZDkzR0lLbmNNUU8yTDAyaXpwWTB3UG5HcDFQbFgvUnhPYXQ4Q2dZRUFoL3hZaEsyNEx0aUhGWk44Y01KTVNvSGh6YmZqelBjNDB0Wmw0N3puUHN0WmpnTGxES1hZVmhLcy91MGlwbDRkb3pIaEdnbzNzeWZPTE5mN0JUZ0JhZ3krZWUzb2VaTzJIN0JqM3ZuV2thYXVQTlRwb3dpMzhEcUZSakZLZEt6ejBnRVRDbGFpdEVHbTlKd2E2dkhxTFRMcGRyT0o3QzN4ODc1T0RyZEtRd01DZ1lBZjBiSi9XdGFEV25NU3dzVlI4c291WUgxWHJ0WlZEdlRSeUdiNlBwZWRDU1pORzhrcll6NHh1TzZWVWk0b2huV2JkRG5Ya2pKTk45Z1Z2Ri9aV0NYU2xHSUlna0hwTWZ1SDZZeXlsRDBycVRmTWd1cnZrdVJkZTBEL05KNWZVZ0xuTGVOdUdWNGZyd0UrQ1o4R3ZjVjdmR01Lc29sdGNjNmh2VzdMS3hXbGN3PT0=
    !
    crypto dsakey dsa import $v10$TUlJQnRBSUJBQUovTGxlYktRcFpDMGZDamZpTHRrUlE4bHVveE0xNVZPOThWazZQemsvY2dXUTRpZGtHZ3pJOTRZSjk4ZHBydjdCSVFUWVpUVTZxZ2NKc2t4bWUwNDFIUUlOVVlCNXJScExTSWcxWjYyeDd4YmwxTHozckhGTmExNy9zbEtQdnc5dStqOXpkOURMbEtJWnFWRS9CcG9PRmNmUnR2b3M2WHU5T3I2WEp0NGRPaHdJVkFObyt1MFpwSnU3ZG9teVIxNDNWN3laTFUyV1JBbjhPd2JqdEEwVjUyMlJ3a0JOdVRsSktoak9Xc1JvQ2xxY0NrZXhEQ2Y4MmsyTTN5ZUppbjg0b01kY2s0cGZoVXQwaXlndGJUUHhUTFBOaWx3VDUzaW9xRi8zTHV4elVmQm1sVlZDOE9iRktDeWtzdGIzaWd2cG9DK0FmZzhGUENzYS9iaFFYaURRMjhOMXBldnI5YXJHN3hIbEVSeHlsMTJMN01NWlNuZzZWQW44RUVqNm5OWGRkMGdWSzRueExhYWxWRWUvZmxTTGFGZUxJd2lNN0dlMnBubWpqRTExVnpjSmI0R3ZzOTJFNFpPbUV0Q1FFVjN5dWp3YWNwSW9Xd3pPNDFVa0JTQ1Y3RnA2Z2tTWnlQSHFZR0loamZuWlFheCtjbVlkTHZOT1BWZzBHR0h5cjkweElINVBBZGVPRUJyZ0lhRENMK0hrZUJhME9Ed01OeFhhNUFoVUEyVTQrTXBQU1pFWnBGSVJEbkRiQmR4L0tmaW89
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIelVhTDdib2g4S3NCKzdCNTVoazU2S2xWYzNOT1BBSktCMVl2LzRkTElTZ0J3WUZLNEVFQUFxaFJBTkNBQVFrLytwUFAwR2pXNUE3NVE4VFR5RGhmRml6cXZjQzY3YVMxRkFGalFrTDl3SzhjdFI5QVpZRGJzNkRGMXpFQmNhMHFMNUVWT1ByU05CSEFDSHcxWlpx
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1RUQ0NBZ21nQXdJQkFnSUVNc2F2NVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNakV3V2hjTk16SXdOREk1TWpFeE1qRXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYTh3Z2dFbUJnY3Foa2pPT0FRQk1JSUJHUUovTGxlYktRcFpDMGZDamZpTHRrUlE4bHVveE0xNVZPOThWazZQemsvY2dXUTRpZGtHZ3pJOTRZSjk4ZHBydjdCSVFUWVpUVTZxZ2NKc2t4bWUwNDFIUUlOVVlCNXJScExTSWcxWjYyeDd4YmwxTHozckhGTmExNy9zbEtQdnc5dStqOXpkOURMbEtJWnFWRS9CcG9PRmNmUnR2b3M2WHU5T3I2WEp0NGRPaHdJVkFObyt1MFpwSnU3ZG9teVIxNDNWN3laTFUyV1JBbjhPd2JqdEEwVjUyMlJ3a0JOdVRsSktoak9Xc1JvQ2xxY0NrZXhEQ2Y4MmsyTTN5ZUppbjg0b01kY2s0cGZoVXQwaXlndGJUUHhUTFBOaWx3VDUzaW9xRi8zTHV4elVmQm1sVlZDOE9iRktDeWtzdGIzaWd2cG9DK0FmZzhGUENzYS9iaFFYaURRMjhOMXBldnI5YXJHN3hIbEVSeHlsMTJMN01NWlNuZzZWQTRHQ0FBSi9CQkkrcHpWM1hkSUZTdUo4UzJtcFZSSHYzNVVpMmhYaXlNSWpPeG50cVo1bzR4TmRWYzNDVytCcjdQZGhPR1RwaExRa0JGZDhybzhHbktTS0ZzTXp1TlZKQVVnbGV4YWVvSkVtY2p4Nm1CaUlZMzUyVUdzZm5KbUhTN3pUajFZTkJoaDhxL2RNU0IrVHdIWGpoQWE0Q0dnd2kvaDVIZ1d0RGc4RERjVjJ1VEFMQmdjcWhrak9PQVFEQlFBRE1RQUFNQzBDRkJrcGFnMHY4NUw5cjI0ek11bWxkYWlaWE82MEFoVUExUVkvNWlHRC9WUlNUOG01OXAvN1d6TnlwWjg9
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUVpyTW5ZTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhNakV3V2hjTk16SXdOREk1TWpFeE1qRXdXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRay8rcFBQMEdqVzVBNzVROFRUeURoZkZpenF2Y0M2N2FTMUZBRmpRa0w5d0s4Y3RSOUFaWURiczZERjF6RUJjYTBxTDVFVk9QclNOQkhBQ0h3MVpacU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU01VWRwUlpSS09iNE9kNkxSb2JNREMxcjJySGZtZ1VWTUhPMnNxUkk2Z3pBbDhoY1ZVSHJOV0MwU0xoK3B1THdtTGE1S3AyQU5heUplR0NzZjZac0lINVBnZEdvZjJmQldNbUdXc0QyWEM2c0JsSXJsWjF0K05nY1lIREQ0U1hyOTluSXl3T1U5SmlNekpUNWs5QWJQQXN2Z0YzamFwdTBydE1RY0xZdHdTS3JRPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVlcjQzN2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEV5TVRCYUZ3MHpNakEwTWpreU1URXlNVEJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXRkVWY3VytrcTlEMFFQenFBcG5VRTJrbkg2ZzZsanFxMmZ6Skd5RnZyVUVRZWRubnFObGd3ejlDSjhRcitsS1BveDdVcytka091UGQzOEx3dXVYK2E4VlJDSFd6bUtDck1NZTIyVjdmWkc5dUF5S25OR1VGK1VHRlFORlk4VWVRRW1zZWg2aWpQT2U3eERkWnZyRUlobWpGMFB0SXhtVkIzK282Q0JsZG1QamlvTm05K2pPTWxzM1VCaUR2TXhLMHF3L0c2TjlVMGpBTHkvN2w3aXZXS1pkMVdqZDJzbjNrcFQ0UjNuR2dBWkVWQ1o0K0VaVGFvTzhRR0JmWWdhSUNMcW0vaFV6QmFxZEFZRzdvWGEra1BhOHo5VWVmd0xiaWNvRVFCbGlCWjZzSmsxeHo5OTdrUGZyMEJLSVByNE5aYXVnZDIvOEJYUy94aGFEMi9ickVvUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQXEzU3ltUDlLL1pQNERLSGNldmhINXZqUWJOZXNHamg5c243MlNnRGp4QTJVRlJ3dzl4S1lsUEVFR3dweUxHMjkxR2xXVm9LaTRZR0hNejM0Z1libWJQd3VLQW00Qzl1MzBSV255RVB1UVBianAwV09KWkpLVnBqdk1yODBxK3psRk9CVzNUcUlTNmd0TFJubDQ3V0xsbkxiTGw1TGo3M1lrQ1QyTGZwcDg3Vy9JNVorU1lvVTVQTDlVc3lsRXF5VmFWZWN0cHdqb1RmY3NKUE5wSXJWWi8xUlk1YyszYlA3SUVzY290YkszN2NjNGFxMEYweTR3cmNDWnFqZm53NWZvWktZLzYxdDZrdmx5amxNMG53QXc5MXdYY245VzJLdVI5WEdVMXJXb0hkRCt0cERqa1BnZ0ZienQ4NjhKMkpwYjlNN043N3BoTjNuOWM1TWwrWTI4
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
    logging file debug ../binTmp/zzz44r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWwxZEp0ZEJYRU5xTks5Y0RKaDliTHBQZHRhV2VKcmo2YXZrbFNZdC9SVHRuMmxqdlY2TGorYnFuU0dLQVhHMXM3V3RCbS83eVErY0h6dWpPcXExdGdmVmlsbmNxbm4rcUg4KzZ3aGVRQmlYTGhYOGpkSmVSMnZ5Y1JmcVpTL2xEb1BhQnJjTGRMWkE0ekUvN3EzSWxNanNIOWU5WS9TeEpseEgwYmJjYXBSUTRYOE5uQlNhZVZ2MWljdy9rUE0vZGtUM3BCeDdyelJHYUxyVktRWGczeVQvbml1K3NOWXhjS3BOdkNMNmpkcG9KWFZPSm8wRUYzUE53UHlKbW5iVCtoVWVDaENWM1BBQmEzVFJmeGV3akFBN3pYbDFyVzhJVlFYbkxVN1cya0d2eDhlRFdNY0ZCRXROWGdSNGFHMjlqNHFJRzNuN3NWKzVuVHdWdEFzTVVGd0lEQVFBQkFvSUJBRFZmb201TnFMY1g3TnUrTzYwUk4rNG9WZk8vRWhTai9pVUY4eUdKNGZ1L3BMTzcwOFU3ZkYxUmQ3ZXVqWWlMU3ZROGRHb1lzc1pCejE0b2V1SjB3WDhvMUhrdVU4aU1TNnBtYjM0T0kwd1h2anc1aDM2U0NlMktVMjdXbjRQTXlBNFhnY3FQUThQUzdrVVlIRER0MDdKd1lURmFGUzlNbERPRU1Ja1ZIMytDSkRxSzlpQ1BUT3llRm9oVDF4aVh1SmxzelNISzN4WVZBK3FHVHhVRTZjRzZvQ01MTUtybXYxcU53Q01KSDlhbHRyYW1kaW5TMTNZVVNXTUo4bW1TTkxPaktNdEpZMUFFMG9EbFRmZDgwZnVNdnpRQmRHMVNpOUMxSDQwaS9yZHBva09uRjVDK0lGaGh3Mmptay9KUWdsTHpSRVJ0cmZPc3JsaEVudzZHQWVFQ2dZRUF4MVcvc2EwY0VSSTBSQnltaGdGaG1xcHVmd3lYeTNLNlRDQ3c3bnhGNExVcG16NnRTTTdHVUo4TlVrREsyWk90cHYyWWRsUXJsSTdRbkZMcUVNT0trMEhRQlJBcWlVazhYMnJmYlZzblM3NGVzUFFkakloNE9BZmFmT0M1N3pLTmEyR04vRHZTUjNGbnBOVlRFRzlJNEtGUDJkenh5d3ZQNUJwRFZDc2ljTkVDZ1lFQXdsemNhaERGL0dVeHBDZEVsMDFVNGxFdUNwTUZ2Tml4ODNnVzdSNEQ2WGFNZFY4VnZucUJxTEF2TVBiRWlpc3FoeDdCeEhTaG84SGlHd0ZJYjFVWGNWaVVSWmQ4NW1EK0duWnJ4ckQxd2lkV1FBbFR1WlJFSzJoclRUcFloUmduSk1KazlWSDlYS1QvUG02V1VWQTI1ZTBqQUNtaTBBMERHV0xwanFyWXNHY0NnWUFKN3dvSWpybnhWOWptOUE2UWF3MDBLZjRyc3JMMTNwZk9KMnJwMTZPYjJTdGpvekg3aU9KMUxoZjUyMlRBaHcyR1h1ajBMS21uVTU2dHk2d0NmZHd3RG4yUll3YmJwSnl2bktIWnowc2NDVE42V2hBRzZ0NGkzTEZVdTlaSVIxcW8yVW04SWpjT2ZHWlAzcG12SGZ5aHhTZzNrVDB6Z3prdkF1Z01EOEk5b1FLQmdIajIrbWM0MFQvb2F5RFRINmxiQTcxbThOUzc5Qkk0ZTJnZ0VZUzU3WTFicnNkTnltYW1NQlFnc3Y0eVZ0ZjNUWnlTMDkzRkNPUzJRbGEwVWJTWXJPSnFVcjJOTHJyakdzSzFlUlpNQkdnMXUwUlhpYmd5UXNzUlRkYmV2VUQ0YTBSQmlEdjJMMDE5a3kzei9iSFZ6cFVESllsd1lGaEVBTzNIMWJ4cE1EdDVBb0dCQUxQMnNyVkE2M2YxYk9FSVpGcWtVYmxRRXdkOXJZV1VYNmY0cGN3SlhrOXJKTGdCWkpIQXkvUFZOcjlkYTJ2Um9LbWpQMVRKWWtFdmZIc05FZExkdUZxaFRrN1hsSW9kVDJTTUVJUFVSbkllMUFJUGVVd0ZjMDVGNG1QS0FlbDFpUEdKeGcvMnZjS01Ub2xudjBzVDVwbHphcmwvTXArWk1XNnhpcVlrZVp1ZA==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0dNQlpSOFJUNVNZbkFiMWx4aFJldzV0SldNbE1kbG5ZdnVZOGIyMDJzZTdIeXRVRm0xMUpRSllBdi91T3E2ZXRjV0tMeUYxVjB5NkRDY1piekxuRTdFbnlzOC92UUsrWWI4UFNRTWFwSG1tTU9QeFB6Vmxwa3dvOTVkdk5Tb25saHBKdjlUWEdNMkE5a1RVMnc4dTV4cC9EUnhUZElDODNXcUlvcnVnVWlCYkFoVUE2bDdyTjJvRmRUTllhSFdUOFFINmN0WjdZU01DZ1lBZVExUXZBU0g2SXNiaHl3SFlHc0lXVThMM3g4MVZHY0N6WjA0OE9Zb094aTZSR3FWQlFMYXBFZzVOV3hkTkFFWnVOL3Eyc3BrNHpYTUpVcm9CQnVqa2NLNDBReUJTTUJmWjZXWVpwOWM5T0xneS9zeTBlM0J2SVBzRVBSUVhVWDQxNC9oamo2eERyS1FpL2tFeHAyQmtuTHl2Q2d0T21Oc2E2VFArRnIvRXh3S0JnQkkwOVQyYjZybTYvd05XQitPMHIxNW5vN0Z2Zy9NdUpuUlhtdTlUblZWUytRSXJjMXgwVmw5MlptQ1g4U1ZheFU3UXZwSDVBQ0dJNkNtbTBEa2NKR2VVVDJxN0VBem13Mk1YU1FKcU9yTW9XVjFiTkxmazFYV1VDbmRGOVM0cForZytoUFc3TUZvclFnOE00Ykd4L3RGaU1ZQWMySyswcG5LWTBwSyswQUtKQWhScHc3VEphcnczKzNnbm94L1dGLzgrMEFBMDNBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNuMzlWMjlOOCtVVTdNV0NhWHpGUWJGbUpxV05UaUVaMHY4bGtGckZITG9BY0dCU3VCQkFBS29VUURRZ0FFYWN5YmxLUkhYeVhQK1cwb2tMRUszY21nUTRLdGhyMDJ4cTc5bVozSDN3aFNmTDYyZEJodE94dC96dGF4aHM4UDRIRTNpS3FKNEFOV2JacjZ5c2gzblE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVIMHpGOWpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhNakE1V2hjTk16SXdOREk1TWpFeE1qQTVXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0dNQlpSOFJUNVNZbkFiMWx4aFJldzV0SldNbE1kbG5ZdnVZOGIyMDJzZTdIeXRVRm0xMUpRSllBdi91T3E2ZXRjV0tMeUYxVjB5NkRDY1piekxuRTdFbnlzOC92UUsrWWI4UFNRTWFwSG1tTU9QeFB6Vmxwa3dvOTVkdk5Tb25saHBKdjlUWEdNMkE5a1RVMnc4dTV4cC9EUnhUZElDODNXcUlvcnVnVWlCYkFoVUE2bDdyTjJvRmRUTllhSFdUOFFINmN0WjdZU01DZ1lBZVExUXZBU0g2SXNiaHl3SFlHc0lXVThMM3g4MVZHY0N6WjA0OE9Zb094aTZSR3FWQlFMYXBFZzVOV3hkTkFFWnVOL3Eyc3BrNHpYTUpVcm9CQnVqa2NLNDBReUJTTUJmWjZXWVpwOWM5T0xneS9zeTBlM0J2SVBzRVBSUVhVWDQxNC9oamo2eERyS1FpL2tFeHAyQmtuTHl2Q2d0T21Oc2E2VFArRnIvRXh3T0JoQUFDZ1lBU05QVTltK3E1dXY4RFZnZmp0SzllWjZPeGI0UHpMaVowVjVydlU1MVZVdmtDSzNOY2RGWmZkbVpnbC9FbFdzVk8wTDZSK1FBaGlPZ3BwdEE1SENSbmxFOXF1eEFNNXNOakYwa0NhanF6S0ZsZFd6UzM1TlYxbEFwM1JmVXVLV2ZvUG9UMXV6QmFLMElQRE9HeHNmN1JZakdBSE5pdnRLWnltTktTdnRBQ2lUQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGRDlPNFBDbG1FTVFoM0d6ZWlBem56QVpKdGRtQWhVQWwxQjU4NHJLVU9kWUpodmZMOVFYUmhmcGFzUT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRqQ0JzS0FEQWdFQ0FnUk1oM0s5TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhNakE1V2hjTk16SXdOREk1TWpFeE1qQTVXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFScHpKdVVwRWRmSmMvNWJTaVFzUXJkeWFCRGdxMkd2VGJHcnYyWm5jZmZDRko4dnJaMEdHMDdHMy9PMXJHR3p3L2djVGVJcW9uZ0ExWnRtdnJLeUhlZE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lvQUFEQ0JoUUloQU8wMndBcGx6U2FUMExMUW0zSVhxdUdLQjFzd1hhMzZQa0tROU1iVnVZd2RBbUFBaW5nd0JRc214eXEvWUplWmxhMStIMjlIUHhhWk1peGZsRFNVOCtRWFowTVZtUWVIOUNmYU5EZWNDUlFMa0MrMC8rZlQ5UW1qSk9DNGZ1VDJVWDUvNEVGZUNvS1hkZGZ4VWl0VVpGUCt3WDViY2tUSGRqQ2F6OVNNYlVUWTlUdz0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVPT2Y0bGpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBMU1ESXlNVEV5TURsYUZ3MHpNakEwTWpreU1URXlNRGxhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWwxZEp0ZEJYRU5xTks5Y0RKaDliTHBQZHRhV2VKcmo2YXZrbFNZdC9SVHRuMmxqdlY2TGorYnFuU0dLQVhHMXM3V3RCbS83eVErY0h6dWpPcXExdGdmVmlsbmNxbm4rcUg4KzZ3aGVRQmlYTGhYOGpkSmVSMnZ5Y1JmcVpTL2xEb1BhQnJjTGRMWkE0ekUvN3EzSWxNanNIOWU5WS9TeEpseEgwYmJjYXBSUTRYOE5uQlNhZVZ2MWljdy9rUE0vZGtUM3BCeDdyelJHYUxyVktRWGczeVQvbml1K3NOWXhjS3BOdkNMNmpkcG9KWFZPSm8wRUYzUE53UHlKbW5iVCtoVWVDaENWM1BBQmEzVFJmeGV3akFBN3pYbDFyVzhJVlFYbkxVN1cya0d2eDhlRFdNY0ZCRXROWGdSNGFHMjlqNHFJRzNuN3NWKzVuVHdWdEFzTVVGd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQkwzNUtCeURPL1diQU8wNUxJYjBzc1pYK3dFT3BWaVN2NjRUc2I1bWduZWYyOG9URDZ2SXp2K01HeDZlMzlSb1BWUmtMd3VNL3FmUi9ZVzJzTnhjZjdpYnc2UzZHdFdBcG5Tcys1cldsdkdvazMxNG9JLy81YlBTK2tENkVkSnBKZGxWaUZ3TXBPTVljNVJITzF1NFFkbWZvYjdFYlhIemR3TTM3QWdLV2xXcEcrakpmTHBkNHdWa1dXUWVWRkZkNjNsRmNvOFNJb202UXpPNmJEeUFkNUtaa0lVbXRkTVpTOElySmdNLzlhU1FpLzRLVWRLT3BBaWxKL0NXN2lLVVRhUmpmQjVoR21yUnFLalhlM3Z0TDdZNmQwS1FkNjRvWTM4T0hlc0FFZHc3RVkvVFQzZUpDWmpnZjBIeUMrL3MrSXZlQ01ldkN6cmRJSVZzZjNjRVlw
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
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:05 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:05 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 6   | 58f0e2a5 | 00:59:57 |
     | 4.4.4.2 | r2   | 1   | 2   | 6   | 48ba14af | 00:59:57 |
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
     | 6.6.6.2 | r2   | 1   | 2   | 6   | f141cf47 | 00:59:58 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:11 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:11 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:11 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:11 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:11 |
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:02 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:11 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

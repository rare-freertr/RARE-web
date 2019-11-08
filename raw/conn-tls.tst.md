# Example: ppp over tls

## **Topology diagram**

![topology](/img/conn-tls.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
crypto rsakey rsa import MIICWwIBAAKBgH3oGPAPxpD7SS4c2fQqO4uPsTslERKLU/LQpTUj1V6bs1E7v8ucVemLgwmFD+HD3tT5fIHV8qOX8lMIiFwUsTjObYYovLrD+I40cX8MC0SbiyXN1Tty9yx72+xBlpBoCVgjsc1CoYhJrE+bl4Mi5U8s+gLU6Z8il30591UrnOaTAgMBAAECgYBDJ2cdq5xiOdUXZkYNx/TIhFSoUiXf+TZGXWiwhjNI6czjt/WdWP4tub6jdjg5V2pjt8njykRHY0TZasSoMFUxSYMmcMTEbqcit7m68wMCSyX/5y2GZlY1mAb6a86O9fvYhqIQjPkHsjvuIPpqMF4A2mPWKvUFCZIK++f9NeddaQJBAPTUgl+hZKLW/93RFAjnpHmy/ItEPa2fv3XDHFizI+IhGzsxjEk2NwIMaZJFVcxcKx5FFe/TCPp05gqNPGyZnvUCQQCDpp9g0rSwooYQSVlR8Ue4JYVkEbVcyKw7ouWzBc92WmGj8IKaCdOpZhUmhEFetSH5gcPl9zgb2klzqgn/OupnAkAdpZ4j9mc5UM+rDKZgbax9EC+Erb7KR43ntLi6BPdTaq7hfB6Avw/qL5aZH8xD8uVFxRfi8qsjqQQyQugOPowBAkBwtsGRthS5fgxl+Uad34PV51nzOS4byDudu3QJ+BmNbQhXwd0vYOZ1DE9jcKw/F7mE01MTmrvRLOziOFzixmBVAkEA5jY+pivJSXjr3UNzHw5XibJu6RGb+zB8C5qfiXgkSb1RJrr8WmA1J6esCdk3HIFWPbkmk51U6gJJbMLC7VBUhw==
!
crypto dsakey dsa import MIH2AgEAAkARuCVR2ibdMg9RzBpmTAF/H6m9GjhO+7PN6WA0kXwKJq9BYqx/fOW81zli2iJ92Sob46qTwkI2xlWon2U9ViPjAhUA2rBTFJAuhMUuPw8Z7ID4vE68nIcCQAkY1+pjOUBr9kDhFIMLJoypT8NGaOMM1FgBo+KVDldXzJiNupSYd+C/U5YjUdCVXeTv6vx5KvsBslCiBQf3dfgCQA6y17JdXeMHIkEMyc3kFWActGgFQFD1rdis3DMTHAsODJPjVUVQmjTcg+yYzVvAe//Vb3uxRTh4ZUTzYq0SlwkCFE1kOS+kYKHGzwmn+rJceR/15I95
!
crypto ecdsakey ecdsa import MEQCAQEEEACtT1ZwRkfDhndc4zXN/1GgBwYFK4EEAByhJAMiAASucERsdb81h9FyhNEdSrMbnK55VVz3W22q6dz+ggcGQA==
!
crypto certificate dsa import dsa dsa MIIBiTCCAUigAwIBAgIEGYt11zAJBgcqhkjOOAQDMA4xDDAKBgNVBAMTA3J0cjAeFw0xMTExMjYyMzU1NTJaFw0xMjExMjUyMzU1NTJaMA4xDDAKBgNVBAMTA3J0cjCB7zCBpwYHKoZIzjgEATCBmwJAEbglUdom3TIPUcwaZkwBfx+pvRo4TvuzzelgNJF8CiavQWKsf3zlvNc5YtoifdkqG+Oqk8JCNsZVqJ9lPVYj4wIVANqwUxSQLoTFLj8PGeyA+LxOvJyHAkAJGNfqYzlAa/ZA4RSDCyaMqU/DRmjjDNRYAaPilQ5XV8yYjbqUmHfgv1OWI1HQlV3k7+r8eSr7AbJQogUH93X4A0MAAkAOsteyXV3jByJBDMnN5BVgHLRoBUBQ9a3YrNwzExwLDgyT41VFUJo03IPsmM1bwHv/1W97sUU4eGVE82KtEpcJMAkGByqGSM44BAMDMAAwLQIUAkcIL2/c3U1UY1eF+r8sdT7Glv8CFQClUXhdcULO8gjpyKvt5e/nlkJBzA==
!
crypto certificate ecdsa import ecdsa ecdsa MIHlMIGOoAMCAQICBHdcELYwCQYHKoZIzj0EATAOMQwwCgYDVQQDEwNydHIwHhcNMTQxMDIzMDc1NjQ4WhcNMjQxMDIwMDc1NjQ4WjAOMQwwCgYDVQQDEwNydHIwNjAQBgcqhkjOPQIBBgUrgQQAHAMiAASucERsdb81h9FyhNEdSrMbnK55VVz3W22q6dz+ggcGQDAJBgcqhkjOPQQBA0cAMEQCEQCj1kFVhYyMmgeEsIMMCTalAi8Wvrl1ZghtS9ybZuiheuKZCFHKHPDOWPd4C6dKxyvvBsLep0GvqeRn/Un7+8QB0w==
!
crypto certificate rsa import rsa rsa MIIBjDCB+aADAgECAgQBejsQMAsGCSqGSIb3DQEBBTAOMQwwCgYDVQQDEwNydHIwHhcNMTExMTI2MjM1NTUyWhcNMTIxMTI1MjM1NTUyWjAOMQwwCgYDVQQDEwNydHIwgZ4wDQYJKoZIhvcNAQEBBQADgYwAMIGIAoGAfegY8A/GkPtJLhzZ9Co7i4+xOyUREotT8tClNSPVXpuzUTu/y5xV6YuDCYUP4cPe1Pl8gdXyo5fyUwiIXBSxOM5thii8usP4jjRxfwwLRJuLJc3VO3L3LHvb7EGWkGgJWCOxzUKhiEmsT5uXgyLlTyz6AtTpnyKXfTn3VSuc5pMCAwEAATALBgkqhkiG9w0BAQUDgYA84W/4XYB0ryB1wd1/XYWXzPlOTts8Ziwm4xWalk+2F/aiJbRKkAYxQ5yrK0Nmrla7UjlKS5GcafBgIFR2muxrIbpfKFD2XmQ0uOOItQzvDnv2vgfe6IyK5hWXwddf+PFreCOGcvwY9hc1HTC1P+K4Hhn1Oo9xzyjpgNYd89iddA==
!
aaa userlist usr
 no log-error
 username c
 username c password $v10$Yw==
 username c privilege 14
 exit
!
ipv4 pool p4 2.2.2.1 0.0.0.1 254
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface dialer1
 no description
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
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
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
server telnet tel
 security protocol tls
 security rsakey rsa
 security dsakey dsa
 security ecdsakey ecdsa
 security rsacert rsa
 security dsacert dsa
 security ecdsacert ecdsa
 exec interface dialer1
 no exec authorization
 login authentication usr
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
logging file debug ../binTmp/zzz-log-r2.run
!
chat-script login
 sequence 10 recv 5000 .*ser
 sequence 20 send c
 sequence 30 binsend 13
 sequence 40 recv 5000 .*ass
 sequence 50 send c
 sequence 60 binsend 13
 sequence 70 send ppp
 sequence 80 binsend 13
 exit
!
prefix-list p1
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface dialer1
 no description
 encapsulation ppp
 ppp ip4cp open
 ppp ip4cp local 0.0.0.0
 vrf forwarding v1
 ipv4 address 4.4.4.4 255.255.255.128
 ipv4 gateway-prefix p1
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 exit
!
vpdn tel
 interface dialer1
 proxy p1
 script login
 target 3.3.3.1
 vcid 23
 protocol tls
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
end
```

## **Verification**

```
r2#
r2#
r2#show inter dia1 full
r2#show inter dia1 full
dialer1 is up (since 00:00:01, 2 changes)
 description:
 type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
 ip4 address=2.2.2.209/25, netmask=255.255.255.128, ifcid=10011
 received 10 packets (940 bytes) dropped 0 packets (0 bytes)
 transmitted 10 packets (940 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~|~~~~~~~~~|~~~~~~|
 | time  | send | receive | drop | send | receive | drop |
 |-------|------|---------|------|------|---------|------|
 | 1sec  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1min  | 0    | 0       | 0    | 0    | 0       | 0    |
 | 1hour | 0    | 0       | 0    | 0    | 0       | 0    |
 |_______|______|_________|______|______|_________|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 940 | 940 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 10   | 940  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 | size       | tx | rx | drop | tx  | rx  | drop |
 |------------|----|----|------|-----|-----|------|
 | 0-255      | 10 | 10 | 0    | 940 | 940 | 0    |
 | 256-511    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 512-767    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 768-1023   | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0   | 0   | 0    |
 |____________|____|____|______|_____|_____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 | class | cos | exp | prec | cos | exp | prec |
 |-------|-----|-----|------|-----|-----|------|
 | 0     | 10  | 10  | 10   | 940 | 940 | 940  |
 | 1     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 2     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 3     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 4     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 5     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 6     | 0   | 0   | 0    | 0   | 0   | 0    |
 | 7     | 0   | 0   | 0    | 0   | 0   | 0    |
 |_______|_____|_____|______|_____|_____|______|
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- seconds
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- minutes
           1|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
           0|
         bps|0---------10--------20--------30--------40--------50-------- hours
r2#
r2#
```

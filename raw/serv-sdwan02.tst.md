# Example: sdwan over ipv6

## **Topology diagram**

![topology](/img/serv-sdwan02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz79r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCeElkSHU0M3RKSWRtUU5Dems1clJOaU13WldzV0Z1ZnEydW1vcEc4cVA4bENaQlpSUnZ2TjlxeVJESndlM1ljRnFhMVpSejRtT1hucnUyeFlObXhzdlpDK2Zkc21TMUZRcFFYVDl5Tnd3TGJvOEw5WTEzUlkzcUFHcmtueFYybTRlSXJVQUdWc0pucTlqNjdqN1F5WE1iM0c3Ylo2V2NLSGtZS0NoYmMrOFBMTVZmNTNFY051eWF4cXlxbWwxQm0vL1BEL1pwOGltdjNWT04rSHI0amdqK0JuZXlYeHlzYnczSnlGMlNMOEdoOU8zWkFvMWozQWdVdGQxdEN0TjdZZ0hQMDdQNFRlcjRXQmFEWFJrclpaTTZIc3N0RkFiVDVUMndDcXlWMWx3a0NVMVBpYnByUEZGWFhFSXpvRlNtTVB1WXp4a1EwNS96ZmJwek43TW9rRFZBZ01CQUFFQ2dnRUFJRWtsajBaT05jVzZRQ1FUdDlON0d6RnlCYjVZNWx2NEI5UFZYaHYzUi9OQU94dFRnNnk1OG1BMy9nNFNicXd3TlgyaWFjQ1BvaGltZnFuNWRqS1FwSXF6Nkk5TzRWOUZFVzBEeFRWZ1dVT0RoWStsVTBQZ0Jrd2xCZUROS1Bjb08rTnR3alI2UFptU3RqSmNYU0NCbGdFcjlQQkl0T2c1MjJJVUZWMndUaWlqeW1naTJpSDBqMHgwWHMrdDBjUnR2aG13S3NQYWlRbGNNeUxYQXIreDd0RWFSNkNKQ3RLS0c2VVFPN0E4WndrRVM2R2JhVzZPZ0JMSmF4RFBTOGIvbno3aFY5UmMzT2dRbyt6UkVHWkNheUNHMUJkUjJROEZvNmtkVjF2VUhHRTVMS0x4dldlbUtheDM5UmwrY2FDUFlxcXRrTEc1dWVNbnBYL1lnV0tmTlFLQmdRRGV2ZEpKeStQQ0ZOWHFlNldQNVlMS3ZaT0FuVHYzcXh3NVhsS0FTcFRVYm40U2VLZUoyWFRoNHNueXgyekk1T3hzcmtzR3ppMVRTTkk5ei9ScDB2bWNnb3oxZ0lmNE5VdW5PYUMydStrb1RGR3pSd0tvU0tlZElLTFJIQmxPL3lRbTVyTlE5dDMydU44S2kwUG54Ly9HYTQ0VDA1WmdPQ0Z3V0V5dTd6dVR3d0tCZ1FDQ0JqeVF6dzJKRWhCOXZQT3RTZVUrd1pQM0s5VFo2S2VBWGxkUXQ4RUtibHJ0NDQ0VnBkS0hOelQ3d1RVN0pBS2swNDJRSUQrK2NYVUFBWFFBMzVnU0NETmZ6VWRxeCtyMldnUWdXQjJDNldjaWdFQzRPcXVaZHVTZzJocDF6bHM3Ykk3Rnl0SlRESGJ1bERBeSttejArd1hpSDVrUWN4dEFXd0RrVGs4SGh3S0JnRm53cmh3TVQwQk1KNENTUXUwUzBMaEt5bWV4bGNoUStJbVZzNXlJQVFheVF3ZjBYanBFYTNUV25aTUJ3Y1J3NDZLUzBrckNMLzBrTjNpc0l0WWtVWlJJQnVFTzhGaGlOTlVtYU9YQWhNbzMzdm1VSDllUjF0U1VuQW54M2FwUFRlckRWdjdIWUNOQ3pSVTEzTXFYc0lrUFh3UlVlTEVMbVQwQytwdmNqK0wvQW9HQWVOMURQM2k0cEVuZWVvTkNJRHNvbGdWcmZiK0l4R2E0RFdPazFxdDVEakUyNVJzNTRIV2NGWVVFQTJHK0VaT1B3WmZGWjh3U2RQMFNQVWNjaGhOU1VMQyswTGNKUkFGQ01HM01tQ1JRaW5oY0huNEpxemNlZkRGQXBTVVlvNW1HeE41TWVSL29FcnJyY3lyZEF3WTJjaU5GZk1UU2k2LzBEUWFLOWE2MVY5RUNnWUVBdmlITnl6WDJjR3QzRk1BRkJZYnB0WjZrQWJqRWFqL0FGWGVtQXJ4L3VReHpEblhiWlJ6djdrNXhwTy9uaHdweWt4RU0wMDBtcmV4TUQrSEZxaXI1Q0RGdmQ4dWFJL1dvLzhhdmJneUxSUVhJMkdKakR5eU0reGZuV0JNazFKcmE3Yk00TjZpUUZZTlBGS1VOdGswMU1ENloxOGtaQU9rNkttS1hNREdzUm1zPQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0FSby9yS0M4My9pRHREMlg2RXBlSlFuUE9QenptalNMTUUrWFBXWkpXS1RZZVlOdlNzdFIyL2tvSXhRRG1tdHh6UnhsQ1lQTTdGckdqRXdjRjdXdjFvVlpjZzFSM3E0cHR5NVhvVy83dllEdnc1RjlIWEp4QjJhRStkMG91SnU4NlEvV3Fhb1NOLzRqaHFvK29ZQWljb0djaG9mRTNCajZVdDNsRTB0OUVFZkFoVUEwSVA3SlRQQmp4TFdlQVVWMEpxbWJEd0ZLRk1DZ1lBQW5rNVN3RGtHaGJ3N0lQelM2N2VmMVc3UnhFY3ROa1ZVZWRGQWNTRWt5L0F6cnlWc3ZrSFc2WEI1Ti9JZWp5RTU2NnhLR2hac2tlK05FK2IvckN2MnhjMlk1YVA4M0hxNnJ5bExPaGtUUkI2WU1nd3M4YUFNU0pSMFJMejVxMVI5MmkyUDgwazNvb1U4akZBRzA3eHV1SU1lZnUvYUV1MjJUMlRDNVZrNHN3S0JnQUpVZ1QwMEtCalZSTlNLa2pwSk01RzhBT3VBN1ByRWk1a2pHSGlmVEVqUEhvZEpoekJUYXJKUDZjNzZlWERkejRUd3pJTXdwZFBTeHdtOWE0QjdZekFTd0szQVhQM2Rua2VzclVCTlVTdWtxcUh2RXVWWDZNVUg1anNiL05JYkl5OUxsSVRXQk1DbFZUNmd3ODduaGJYNXpPTHFXWUhLSkpVUDR5aTUrVzJ0QWhVQWdXaHFucWpISEp3Wkp0T0YyeW8xenlNMTU3az0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeXlvQ29STk1GeS96dkRWZU1mUUpYVzVVSVkySEovbFdHRER2dHg1aDcrZ0J3WUZLNEVFQUFxaFJBTkNBQVNFSm5mWW9UVE1VRmpjR0t5bnMrRG5qWmlZOXl4SndyRk1HYnhxcUMvdm8wTG1sdldHWTZKVFBTVVdSRXF4SjY3eWJtUnpxT29Yd0JJTU9Dek1XL0sx
!
aaa userlist usr
 username u
 username u password $v10$cA==
 username u privilege 14
 exit
!
ipv4 pool p4 2.2.2.2 0.0.0.1 3
!
ipv6 pool p6 2222::2 ::1 3
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
 ipv4 address 1.1.1.99 255.255.255.255
 ipv6 address 1234::99 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet3
 vrf forwarding v1
 ipv4 address 1.1.1.9 255.255.255.252
 ipv6 address 1234:3::1 ffff:ffff::
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
server sdwan v9
 security authentication usr
 security rsakey rsa
 security dsakey dsa
 security ecdsakey ecdsa
 pool4 p4
 pool6 p6
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
logging file debug ../binTmp/zzz79r2-log.run
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
 vrf forwarding v1
 ipv4 address dynamic dynamic
 ipv6 address dynamic dynamic
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source ethernet1
 exit
!
vpdn sdw
 interface dialer1
 proxy p1
 target 1234::99
 username u
 password $v10$cA==
 prefer ipv6
 protocol sdwan
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1
!
ipv6 route v1 :: :: 1234:1::1
!
!
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

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz79r3-log.run
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
 vrf forwarding v1
 ipv4 address dynamic dynamic
 ipv6 address dynamic dynamic
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.6 255.255.255.252
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source ethernet1
 exit
!
vpdn sdw
 interface dialer1
 proxy p1
 target 1234::99
 username u
 password $v10$cA==
 prefer ipv6
 protocol sdwan
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.5
!
ipv6 route v1 :: :: 1234:2::1
!
!
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz79r4-log.run
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
 vrf forwarding v1
 ipv4 address dynamic dynamic
 ipv6 address dynamic dynamic
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.10 255.255.255.252
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source ethernet1
 exit
!
vpdn sdw
 interface dialer1
 proxy p1
 target 1234::99
 username u
 password $v10$cA==
 calling 1701
 prefer ipv6
 protocol sdwan
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
ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.9
!
ipv6 route v1 :: :: 1234:3::1
!
!
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

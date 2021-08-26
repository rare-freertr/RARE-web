# Example: ssh test

## **Topology diagram**

![topology](/img/crypt-ssh.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz88r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCOGphc0E1UldkYU1HK3E1M3U1d2ZkbkZUZXVNSXQyYWVhSWEwUE9IYUFkVmYxaHJmT2lrWHhDNHFkdzlqNWtQYVZrQndYaVZGcE85VFNzZlJtNXBCNTVaUFU0VWFYdnRzNlZvM1JWTmVpSmFXaVJqZ2FRS2J5b0tKdUpQL1BGTEZQL2ZDcjFnU2lYQW5UMzhlbG13eGZTbXRaemlIYnBkd1VmNFJRd2ZnN3NlTStFSEs2anV3ejZqV2dSUSsyOFlKd292UnlqWFpacHROZXJBNFBzOHlTN3c5K1JOR3VWS0hGOFYyZTIrdWlGYmhpT2E2Y2IzS0RlMzhqaS9vNENTR0ZwTnpuRk1uRUFRVE14bCs2NTdjaG05RlF3dXExbnlMK0craGFGRm05WnVzeDY3dzJqQTFpdHMzVFl3a2w4RjJ5ZUFGSkN2RkwwWXVTL3NWN1FjK0JBZ01CQUFFQ2dnRUFBeGNZdVFyMkFGUExDc29EUHh3b1M4MUhKY2Q3dWR0K2x3cGkycy9SME5vWWRwVURGbkxEelhrMTFUZzR0K2hxMWNjZmkwM3k0U09FNGoxY0RQbUhlQjdFRGpJUXFFOHA3VWFjZWljYXVvRW9uT0FWSUVHZVlzS3RoUUlSL3JkS3R1dGIvMGR1RWdFcWxVRW1HT3ZCNE5OZDJucU15SUJTOTRjNlp5NkkxQ0pLaXpHRm42VW5XT2RZWkNBOEpRNUYwaklhYXNUYisxSnl5Q1ZvamdQR0hETkNQRjRXRFlWUEVWZXRhWU00MFRBSVBXdU80aFVicjVHUlRMQ29rUGlrck1oZ3FnaWlaVUZVaVAvdzhiUnBLK2t6V3g2c2dMeHhnaUhmVldSUjc1ZHowWWREaTBKdittaEZHMU05K0pZL0J2WTUzNEM3N3RMUVNQMnBCeWk1aVFLQmdRRHFDbWt5U3F3MStUNVQzTExtbjh4Y1NjTHZQSHIxKzMxR0xZSGEvTzV0aXZsQjhTV1BYZlNQdTJxYVlZRVN6ajdWb2RpYk15KzRFR2ZxUFBubTBqSllNYlYrSDhTUVltdnFJZXJFb2hYeW1SMWlBc0pIeE1ReWw1QTBOVVNnM3lYcHFEaWtuUEtKY0p2OGZVN0xlR3NiN0IrWHB2UDE3MGRrM25reU5YZldBd0tCZ1FDSVBXZUVSSi9NNUVqT0FuTHh5RnZNOTFieklDVDJHd1pFck9KTHVadDQyd2YvWEpSVVV2NnR6a1EwR0dubzBuSTJtTHhZSEx2VUtkT0dENE1VRmZ1dTk5TE5qWHc5ZmZjUTJxVWp6OTQ1bm5va1QrTVl6TTgvK2JHUzRjdThCK293N2txeWNLcjBPZHZxNTlDbTRDNjVqaGxOOTFQWDJXNUVWY0FqL1dlZkt3S0JnQXhFVFcwNFlyeFZld0hVUUlBOEFlOFlZcUk5YmtoMFRRV2ZudjNHWWd6Vnl1aTg1ZllVdTV2SSsvWnBnK1ZqY0FHc2dQanBmdWZMM0ZaM3FiV0NjT2NVZStuSGFuc1MzWXNoQ2ZnU2Nzb0xZbkhmcVNVdjJBUzYwdkVabGFaRTYrektSMlhCWUNqNkFRTUQ0bHhoekdOalJlaWg5SW1BYUNLT1VwWGlIWXpYQW9HQWFXdmFaaWNUNEYvbFZrUGUzZWpENEY2a0VZMldERG50SjhiL2RNa3kzTm5mM21HdEJYTVRUenFFM0Nyb0NSaU8rR0JIblliZWNOWE1yN2ZoSGZIRXh5ZE5IM0dUNmFGSFJPdHJUY0xUbXBKZXdTcHYrQWpEZGlXb21wZk9Kcm1aSmpPOTZVWDFndllpamlyQzhkNFhTYzRERnFtRFgwc0lZQ2hhZlg3Z1ovRUNnWUFsOXZ6STZlWVpIQzA1cWdpTVZqdStSV1JUQXRYWjhvamNhZitmYm1RK2NybkJSWlpuZHdBdUd0d3ZSUGZJeWtBUWFFWnJOcFVscGRsOWUxOEZUWkY3eC80a2VmckYveWNabzFIL3VoNjVtOHN4OHNrMGhmdzlFcnl5bXNKREZuaWx4WVZWWkhaNllHVnNET3doeS80eHJ5NWgrTDN4ZlN4NmYxSnNZbmhtVlE9PQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0dGSXAvRlZQSTQ5TnZEMUx5MmhScTVRL3BFNHprMXo0NkVCNWRGY1F5TWNZN2FwbU1FeFBmaDJpV25OeGlJYWxqcUFEcU40RzcrL1ZWTDFCdVd0TGZwOVlqWk4raWVPL2JDSUVEQUtoWU5rdDhpZDFWb0ttcWFxd0g2STh1N1ZCcGJrcjFHbkJBSWNJNmg1Zk5maHR6SzNDb3JBRzlzcHdGMDNlKy9CNzQzWkFoVUE0UGVURHhQSHcrK0QrTXI4b3JvTWxSWmJLbmtDZ1lCWDIySEEzb0NwMDVMdVM2OHhzeXZhQzBML2pvSGMzeXJWVVFndGpwRldyV0FHMXR2MWUwbWlHNFozbVBhSTA4L0pBT05lOVZZOTlsRXZsUDRKd3QwbnIwd3J5SGRtQzJyVW1vcWFKWDAwQzFOSUkzTFlWV05CeDEyRzg5cDFnNGRhMkMvUDN2NnI5WTJCVElHU3IvcDl0VFNQRURoNHFHS0ozOFcxNjdibGVnS0JnRGNtU24rc3J1dzIvVmRoZldXWGl1dGIvTEFXU2FtWTd4UFFNT1djV09MWXpEZDA2a3NiQXpXajJQN3g4YllzQnBvblR5ZXU5TmFmVGZQVWQwNFNGQ0VEbzJlSDltU3pOMG1lTnR1U2Z2ODBsT3hjMzBKTDYwQWtUbEhoNXR1WkRmWWhqUnQ3NlExd25OVG1nZFJUelNwWVRRMEN2bm1ESE45UU1mSk5Ob2phQWhVQTczeklMU2R1Yk1COG5xSnpuVk03NWVOTXRKcz0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVId2x6SzAwTUNNRmRRSWYxdHJITEduelVEOG00cjlBR2Ntd0JJaUJTUi9hZ0J3WUZLNEVFQUFxaFJBTkNBQVJNWDJKL2tpU3JOdEUrQXRyVVJydDVKN3dJRXpGVGdOM0c3UHlBOU4yTExSaFdiZGdJZ05DOEl6V1FxNTllL296RTdHR3FPcVRZcjAwZ2xveDEwcXJJ
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
logging file debug ../binTmp/zzz88r2-log.run
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

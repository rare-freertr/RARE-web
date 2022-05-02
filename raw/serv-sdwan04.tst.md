# Example: sdwan hub and spoke

## **Topology diagram**

![topology](/img/serv-sdwan04.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz29r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW9RSUJBQUtDQVFCYmNqUGtZY0lPQkhOS09Gbm9JL3NyU1AzVjRlYWJIcEh4cVE2OXlWVWFCV29seVVzbXR3ak14b2hIZVdzQ3h3VGlPTW5mT2dwVUZIVzMvd0IxdGZLWjBOM2FiZTNZTWhKY1N0Tnk2cVhKRlBrQ2ZwWkJTS0tQeGdITDhiemlIWks5UUFUVm9ibUJqeEJBdjBYV1hXc1VIR1pLQ3B0ZWpPeFRDU3h3ak1EeHI3VHJuTEJQRFhJaVRPdjVLaXRLNXM0bjhPTXJpTDVBMTNmN2FlZlgzbjFEeDJBckl0NmcrOFZXb2JYT0dLdHFtbEdabTB2ZWFkOHFMS1I3WXIvTnppQlhCbWp3dnUwVERWYmNyRXpkRjN2MWI1ZmFVV245K3pZRHN3bjFZZEVvNFE0Wk1iVDh2RWI0MExVNHpEdm53Yk1ZU2hibWdydVVVekpMYm4yRjVaMERBZ01CQUFFQ2dnRUFTTG1TTzFiamxYSkVuZ29pdGxPbk5NMWYwZkZPREo5TFFmMUpFL1pDRCtldWUwNlN6YjlTNkVnYnFYd09kcThBVzBqK2d1RU54Y0Jmdm15MldPYlNnVEZ5dm53ZVk0bXV3R2Roc2txYWZraUhvRXc4QXI5WlNTNFh6N0g0blhzWGNCcXh2WlJZaTRqVFRDclJ4NkdUdnZLM0JydFl4T0VlTVF0aXBEL01VbWlMMTRwTnM4aDB5czN3L0ZVMkxSYlFxSTRGUXZZRjBCRWtzeXRjSHRQVDQ5UVFYYjZQNEovbHRxWWJHQWJYU3RETG1vc0UzZDlLOUN1KzhaWm5tVzYxSUNXYUhkajFuM1lPTE40NVg3N1daY09WVkxWNm1iRnVmeVRUNzNsSjR2eXo5MWcrbEdxVkx4d0NTM3Awb1pNb3QraThScEJVb01IUmsxT3N4SDBUZ1FLQmdRQ3p6QWNxWGRQc20wUEovckdUQ2xjb1kzb3psT3ovUnh4R3BuUnRVNU9sU252MmN4ZklrWnNMT0pNQlJYZ3NwbGZrYXd2OFdRRlFJZXkvQTV3TnNpWGQ3RGlEckF5SEQvT25iMmZZYVNEaHAyMFhoV091aW54TjM5ZkppYU9GTWhZdUkxenYvak1QK2tXbkpGbEdGaGN2aUdJVkpIenc0c0FGZWZ5cVFWazU2d0tCZ1FDQ05CcklVYk5LYWRPc29yS0FiY09RM2J4eGY4TXhmTWdZMUovbVhpMXdQVkFIYjVjdVJPVzBzN1dUOTl2TEJ5MDNMUFNkQVIvbWNiaU5nSGtmcVF1UDh5UU9XbFV0SE1mTzdSdTNPUzJ6dEk2bHh3WkJTbFhON1oxUExKeVRhekFqOVV5MGJidHNzMmhGNFRuSmVjUTlmR2pLdGVYQVpLOHVJUDB6VFNVTFNRS0JnQ2lIWkZJYmhtcitjT0IycGlha0hST0FvUXBCbHM3UWc4STFRV2RuZ0krdzQ1S2hUUW9zTUV2dU84ejhrT05YdDlaSWZ4SXFLZzZiSnhmRHc0aWUwTVJldkRxS0xPVEJKc1ptYVgweDdYU1FYaG9BT29FY3ZIcDlhOUlGVWJQem4yWlZHRjBNNnd1OStiZDhqUmNzWVp1WVhhdXdadTJSMzRFY2gyVUZpQXh6QW9HQU43aXl5WTNsYS9BMFRZcG5WLzBobDhxOVRkbCtvSndsU2pNY3Awc2dxUXNrUjdwaStjTTBod3Z0cG9DSmlLN3VrOUZpY2hxOEd6UUo1a3pZQ1V1Z0RoL2hDMTl2V2xvWnpKMitvY0FQcGZ1Y25LZTdMby93ZnF1MUNlQXV0Z3hHVXUwMHdYYkFvamw1WTRhSzQ0V0FEVXhEMEpUZDJXTjljUUZmT3VoRjlUa0NnWUJFUEZlWEpBOWNkYUNzZDBsTDdlbTF2TU9jdTVBOExIbllRN0NFUTduKzhRYlZjYWN3V3EySVBjNmdxWUVldGp4a2pVRFlLV3AxVzM3ZXdWRys5TlhKbjBKK2lxQlFyTjdxY3NuVkZiTWpDYVM4TTEyOWZJYkVYYTg2a1FCYUg2ejk4MWlzWWg2cVVrVCtjMnRkMFVNTE9IRzZ5ZzVYZ043YndURjNjRWswWXc9PQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0VIVkgrdWFKZ2oxaTNvOWVZUXh4T3JIbERmT012YVZLRDMvRUdUcjA2MFZDZ1NsNUZYTEUvWGt6MnlKY3J5dVloRUkrVG1sV3EyeFAvRFdNYks0LzBPNGlvUDB0WTdlR08rWFg3ZEZrTEx6clZPc2RPVHFnZW8wQ0xaN0xVbFYzMk5WeU1VSFJ4d21IeFBMNE9OK0h5U0hXRFZ1UjNhUGJHbHBmaFBZZE9abEFoVUFwT1RxZXE2bzBXVUtzVmJCbHZUL1Q4RGkxWVVDZ1lBS2dhUDBpTm5xTnBTalhMY1NCVTc3YjZGaXBERnAxdXkxVHdGMTh3T3MralZ4OElWNGdvR2FLR0ppMG1kRmJMYW1DMVlaSERvOHhRSHZXaGFKM3pJeUFUY3JNWG1MS3lNd2lPRExCYkdQYWJZcTRCVzJnSjZwSEQ1d0NJaWxWazlKdGxLZFd1TmFYdVRoYjVRZzg1VXpKejZraFNNV2MrVEZMQjg3b2dEd25nS0JnQzlXYUQ3M1JzazlPbGFDWlpvaXk2cDRXai9oVXFqK2d3NnlSZEpFY1QzM044QzMrMU9tUWJBWXFRTVExZ2Q0NjhTSFo4S2lxU0xUdXFGZUJiR2haR0RPRXM0YzNYSVFjL0pzaldyeDZtY0czZW1ESCsrMVZEaDdKdFNSc2dlNDkrYkRjN0h3Zlp0dU9RL0phakozL2VjMWkwMGlRc0VHazduVVo3cHczOTh6QWhVQW1KTmJkSEFEMUt3WWFHelROSUVDMlNTcm1IMD0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMzNJQ1l6eUh5S3U2bS9tNUNVVzRxa0MySVlPcXpKRHduUVQxOFNYaVVtZ0J3WUZLNEVFQUFxaFJBTkNBQVFvN2lMRzZtMFQ5cmlEYUk4N3l4ZFRrZzRLenZyTTVsc3dUdlo4eXdVSGZqMStpcmk4UStMZjAzOHFxbnYvTGZIYjl2Q1g2M3RTaWJ0bVVNSmtzalcv
!
aaa userlist usr
 username h
 username h password $v10$cA==
 username u
 username u password $v10$cA==
 username u privilege 14
 exit
!
ipv4 pool p4 2.2.2.222 0.0.0.1 3
!
ipv6 pool p6 2222::222 ::1 3
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
 hubs h
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
interface dialer1
 encapsulation ppp
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
logging file debug ../binTmp/zzz29r3-log.run
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
 ipv4 address 2.2.2.3 255.255.255.255
 ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
logging file debug ../binTmp/zzz29r4-log.run
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
 ipv4 address 2.2.2.4 255.255.255.255
 ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
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
 username h
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

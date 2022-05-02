# Example: sdwan over ipv4

## **Topology diagram**

![topology](/img/serv-sdwan01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz25r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXBvSWEwWjVGeCs0bEZKM3NKK2xDR21rYWxhUG5WeFFTVlc1a3hTN2diRkIvMjJYZFhYaldZNnFpbG4rSFZuQTk1YmEvT2N4aGxvYytjUHVGTWV1Y0RqWVpTazMzK2IzdjlFNFJFM25ySllYWlJaM0hWU1pWczByNDlycWM5UW9nVjhyQkI4MjRlNjRQK2FVQ25hWGhFcXBZcWEvTG1nRm9vTzVhcGRWcTRuZjdua0NTcU40OFl1a3JsT0MxMEpyQXhGRGRsSXc5NHV6M0JOQ3JCTHZ1UHoyOTEvWEVBY2FNRy9EQnBJRy9VL1RuS0dRR2I5cUU5eEV1T1k3Q0RFeUx4Tkdtc0N3VktDcW50N3J0aENTelU2SkNvbDNrTjFmWHE5N0FnQndWOVlXRHhIb1krYURjdEtmY2p6TlFScStsOU8zT0VLSEhGaHhXUmtkT2tEd3ZYUUlEQVFBQkFvSUJBRlBiaG9JM2dkRlZJSnVuaFQzOGZld3JMdFphTzdKaFMzSjNMSTBhTkxDWVFpeE91eFBPUGJyb1B3WW9xQkppYU9uK0JZU29hQ1dWYTE4ZmJVOWM1N1ZJamFnY2FGMEF5WTV5bXFzQ1plajU1aGpuZzNKZzRoeHdENzdDOFRWL3FoWk02TFp6Wnd2eTk5eTB2QUtGZmpzV1M1ejZDa0kvbjJBZGFzM0dGQlNGcEt2SDlQR2t6b1RCNDNEWDRQOWE4SkpxeWJUSTF5L1RCYm11WWp4czZMbGplbHgyUFlySHN0MSt4eXBxdkh1UmhsSzRQaHNRZmROSm1nL0RZb1NzUk9lTjRObjNRMStVcVR3dnd3WGZaeSs5dmNIcDg1Q1J4NHNHUUdRRE9qWDNPL0JHcW9QdVc1cnIvTkFnT1FDR0F3ZEZnZ1V6c01xZUtKWG1vZjVBRllFQ2dZRUExOFJXTEpjalhLSjlyd2dDWkFCbVUrbzhKeXk5MGl3OVpXYkoyRVo0dWdISGFzeThuV1BmaWpueWc0Y1JnZ1FDWG4xLzlJRmNKMVVTcUZoMEI1Tll3SnZjdzJvYThod3pnT0tsZmtXeG50VnF6QnNQdEQ2L2RLODZBajhWSUtQNWZVUmw2cW80QnNMRnJ6NndmLzJVOEV3QXhwc2JISG1kam1CWmRpV2xXSEVDZ1lFQXhZNWxqNTFINVRjaDhPY1ArYzFoektGSG00YWovcWdpTlZ3cEV6akJKOEFYQ0xtSDJFbUJjMng5Y0VuQ0IyK0Qwcnl0M1JJcTF5aDVua3ozUjlJRW5MdWlsM3RONjFuV1NrMXZxUSt0TWxCNnBwcWE0bWZHK0NXdzFQSk9HSm1QUExnK2lmZktBakVOaVRsanU5R3F3cllYZWZNNWhnL1dhb3Rqd1dPam02MENnWUVBc0VoUXY0MmI3b3N6ZEZWdTNwVVZCV3BTU3c5YTV1UU9KVktkaG4zTkZPdHZLZXFzRDBzUno3VVlWaTE4T0dWZUtpVU83WXppNVorejVxYWQ1YktVeUlpUERYa2JHc08vc0lWOEFIYWdiOHlkdkxRL1dGd0x3Q0dKbTF3K3ZyUTVtZ2JQM2JIRXBJRnRVWWcrVzlPcVk4azB1UTd3VDR0dEZtM1JxWjJJUVlFQ2dZQTVJcWZJMDBvWnhzb3dMQU40MGFkNVVTT3VuVkFNdEgvQVF2azJML0hkRnpjU05PWk83V05kQ0lGMjJqNGRmR2o1cDh2NDVlb3g4K2pJbWFYaXhhREQyNWg0aXhiTC9GMTNlOUhSYVZGRC9mYWEvSmZTNXdTcWUrd2Fpa0YvNTlsL1RDSDZNUW5oZkdKWHo1dENsSzc0UlVXZzVYRTdqcFVLbDJtd1lxck11UUtCZ0U0V2lENUkxSlVDZ0NvUHBuV2VLamVUSWpSc3ZNaEdnbWwraHhldTRybGVFVzdxY1FHbkhUaWh3amx4UU9VK1ZReVgzR01TSU9hM2JHSk42djBBWE9TNGRlb2ZvR1ZScWtWK1UreG9qdmNsajFOYmRVMHd6b0RUTWkrbVhCRGpGRkVWbGh0bXM1b2FtaVpldzArc2ZVbnlGQVFmMWJ5SlVSbzYzTFk5Vzh5Rg==
!
crypto dsakey dsa import $v10$TUlJQnV3SUJBQUtCZ1FEWjdpRE1HV0VsVHNFZDlmT0hqZG1ZdFo2OEFxRU5SaWhYY3dVV1JnOE40aDN6VTJZelhIY2FMakFLRHJMUEpCc2pBdDE0aVJSckhGbWFrZzhGYStPbEd3RjhkeFhIK2lBdmQ5c0hSRHJlMUNLSzhHdjRpVlFOMU5MSDMyYUFpMk1QU2FIWGpId01XemYxSFhvSzRlNXpxRklsVmhhaFFBTGFuU21LZDZkNWt3SVZBT21pNHdTdFJsMFBsRW5NQUsrWU4wNGFpT2hIQW9HQU9PSHUyd2VOc0hETnc3MVpHQk5ERkFsR0piVFcvZTBGemJFYlNyaGNvZWZqaGx4MSszSjNsTnpXaWtkalJ5N0RpY29IYlBYWCtCQXl6b1RJYlJ4RFZUZVFJV2ZNYWxnOWdJendBYkNSVjNqUkc3OUlGSGdHSGc1bWNoRVpKYjFJeWZRQ1l4NEJISE1sSmgyUnZZSGorQ0hDWnp6QWNsNWF0OUZCaTJQRklkVUNnWUVBbk1OUVdwMGNFelBmR2RZZEJkT2FDR0dlRVNkbElXSW01V0x3RUl2ZkNrTXZBaDQ4OEVQd0ZHWE5Gc2xMQTI1aGU4YWRMVTNBUWhBSFRWTCtZUVlEVVA2SmVhUEhVRGFYOEZYVE8xcXBmSndmTzRPY0FPRm9hQmNqM3ZBVk5zUUd0N1diM3RKZUhxV0xvdVVuVXh5R0hJSjdudUQ1cWJsenFGYkdlN2h3d3NjQ0ZDdG0yb1A4T21NNmh3QWF1OXJjOTFEb3Q3cU8=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMWgybi9MenlTdUlIVnJINDhva0d3a2drazk0a1llc0pabWs1UTFucjRhZ0J3WUZLNEVFQUFxaFJBTkNBQVFLeS95UEFrQlNJajJKZTYrUXo5aFdFUHpNa2E5c09QN2Z2VVc2TzIwV0d4b1VmL3dmbmlZL0xZeDNsQXBEVExObnMyam50NW9MTXg4allSdUpiMUdT
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
logging file debug ../binTmp/zzz25r2-log.run
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
 target 1.1.1.99
 username u
 password $v10$cA==
 prefer ipv4
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
logging file debug ../binTmp/zzz25r3-log.run
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
 target 1.1.1.99
 username u
 password $v10$cA==
 prefer ipv4
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
logging file debug ../binTmp/zzz25r4-log.run
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
 target 1.1.1.99
 username u
 password $v10$cA==
 calling 1701
 prefer ipv4
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

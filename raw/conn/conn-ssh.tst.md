# Example: ppp over ssh

## **Topology diagram**

![topology](/img/conn-ssh.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz92r1-log.run
!
crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQWwrNHI3N1J3ZzBKNXgvdmhWODBuaVFIVEphbnNHU3NZZ2NBUTN4dDZNclVoRTkvM0E1UzMwMGdSRnhKbWZIdFIxZDVKOXJydGt6d3hEb2twUXQ1UEg0WEg0cVBwUFZQNWVUM2tHa29hYUcvWjl5YWR2bzZOeTFjMWFEbjBqdWNjNEZPUGF5RHRsTGUyU2pOZlpuVGFueDAySXQxckF6VXNYWlI2dXJ1MG9WMUpOb0s0dVFpK0VqR3hPaklyNm9YREdWSjd5UnhXcVhQamJ1VHNITmFmcy9RanNqN2tYeXhBS1ZLQkhId3Q2WjRsb3VCV09YY2RjK0ZJOFd1K2plamowUkdRTGhLMC9ENW1HeGVPQlBGZjllNzNLMjg3RERQb1FwMUpaaTA3dVFRNWxsNmZtU0JtNjhXTys3OVU2YnR3ZUt5YS9QbmxqcG9FN2tnNkw0SldWd0lEQVFBQkFvSUJBR0R2VHcwVFhTNENQZDBBc2hmcEJ5NTlBWkRvUjRFUFpBVjAyODdkb3l1ek1UV1RFZkV3ODlCVURNTmh0QTM4U0l4aDFXTWNoUFFKMVdybXpIS2prR3dXV1NBYllIY0dtd2RtRzZGQ1luTDcybCs4UGEwVkd4Yi92MDJPbktDSWlINEFFbU5Sa1FQdjZ0aVF5bTkrWXZaZUZ1cEx4emsydGVYSEZEOE1BQVZya3hqaXdnTWJ6Wm5nQlI4RmpQNUJNYmNyY3BkcEw3UWdtdmg4NTcwaWs1RFRGdmRTTmhBTW9POTM2UE5vQnZHcENLZkIweGdzYmlCUktLZjUyQmtyYmYvUVhOcVBNSHpydVhVdVoyTTU1SGtlUVFjWldFKytxeFBFUTB6Rm1DNlVxalRMMThkd2pkOFhtMWZkVWtzWDB5Sk45SGxTREpDN3FyNS9KUVF3TXZFQ2dZRUErSnBHM2taV2lrTUhDemw1c3p5TXMyL3BXT2s2LzJsVzdMZS9pZ3VHTDdHSW9xOEhlWXF4Y0VZVjBLOEpoblhGQ3VtZ2ZhMDNOVkN1NzVUdWJZUHdadUVoNms0WC9zcHJ5bFg3aUt6bENzaCtReUw2bjJqdDFNOUVOSnNuUWV4Vy9MOG1EaXlmcDhKSEdRYkVubkltZ0lOdGFuczFNU2dKRThpOUNPZDlWaVVDZ1lFQW5ITi9Ic1kzNWQrcG01QmZEM3lOV0Q4Q1pIT3YrY0VNUjV3R1YyUFhjWDZta3R6aUl3QkFGSmVTWmtjZHI1d0N4V3dVa1dHenc2c09WL3VoZjh1V041Wi9wRDJnWm8zdEVTUmk1dWZuUWZKM0hsdVZId3FRWlhOZ1lvRDhoRndJVWprblgzdHFPSDg4RGhuQ0pDbzA3LzV5dkNNL2taaXVyT0dseERqS3U4c0NnWUVBaWhXWFc0c1NNb1g4ZVoyWkhaZDZSNGpYd2d6Nk9qZ1drakdWOEdWcVNUK0JOMnVrNlR2Q1J5eUduWDA3K3pXYkZ1Nmh1R3pvQjNNalYrd1BhMEVuM04wYjYzc3BGTnIyZUZLOS9qS2FuaHl6RlROdXBmQ3dlYzRPZ25IVG9taFdBTmxqbCtmdFhrOHBFcHVSeHJoODdsRVNDMTBZTkkrYVN5VHE2dkU1eXdrQ2dZRUFrQ3gzRnZyL2hCenJCZXF6VDJndU1RWlB4QlpBTXQ1TjNLZlJ5REsvMVYwclQrZXhsU09qNmRZTUdhaXJtS3NpZXFBeERCQ0hRbWVlSGtKSy82T3pXS0tlR2RLWXdDbEdNQ2ZoNUh3TXh0OFVHcXUyN2hZa0h2bUY5d0I2czliRDdGR3pFUENBWUhRUCtjYU8vQmpSRStEZUJyWk0zSFZoY3Z1MmNPOE5GS1VDZ1lBd2E2S2NhVGZUNDc5N3ZYNjRoNzI3d05vNk5yNjkrVWZnUmZ4VmRIYlpoNlV4RVNocThyZHozWUV3c29qdmZHS2VVZ0V1QkJNYkhzU3VqUTZLRGVEUmtVMHI4RHoxdFVaMHhYQjFJT1JnWVREZmdnWkF0MHo1QSswZWZnS0dOMUprTTVQL25xdXJ1MVR2L1JKcmxyK2tYT2pFWStuUEx4WVpwMHovRHRlditnPT0=
!
crypto dsakey dsa import $v10$TUlJQnV3SUJBQUtCZ1FDVnJ2eDM3bk4rbngrNFQwNHI2aGtUN0treXcydG91bUoyS24wSng2UTIyMWZjT1FCWVFVK2dHbzdzTnNIZjhYc3V1bjE1cUh0M05DdXdKaXRRM3grbGhNYkhRaE9RZ0VqcnFxWk1RVEtJYmJ3RzFEa0tVVXRHMWpnU3MwK296RCtDUEd1TE96RVJuN0xqanVGeWhtL2R0NE9QOU1MOHlwb3BNQ3NRa2ExOVV3SVZBUDM3NWRwRDU2QmlvM1RxckNRYU1KMEVhV0xwQW9HQU5oVFBuQWY3M1Y4ai9uclJWdERFRVluR3hCVlU5ZmdxZUhNNS9RSUZtby9iY3hoZXN5V3hCU0phSTBTOUU0VHFyOVR5ZVJpSXg4R1UwSjF4YUV5WGc5ZkxLQUhFdUVvSEMrbkxYMSsvYWF5QWNITVlsdng5UW5rZUovRnZhbVI5Ylh1dWY4dnhSNENkeCtTRTRpM0o3cllVbktqQWVFWFNJS05nNGVrTUlCTUNnWUVBaWhIaStnT0FqdGdpN1NMY2NKOVBIS3dZNEZjdXMvR0I3YVlBTHg0OGJqdi9jOWMxbTdQWHA1SHd1elh3YUYxc0ZMSHl3MjN6R3BNSlIzWWlYQ0NnVWxOV25KYzZqbE95b0srN0podGZwMjIra29wOXdCbXZObGN2Nm9qQkxLaFR4NytENnZaUFdRMHc1RUtrQ25VVkIxNytTdVZwOEdXS1dJTisvWVdjWU04Q0ZBM1dja05ERnNyaVI4K1V2UFZuSllvL2wxT1Q=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIM1dxdGR6a0lReDNNMTB4UVlVM2tOektSTThXYW9EOXFjODZkeVg4ZjJhZ0J3WUZLNEVFQUFxaFJBTkNBQVFsUHBMT0prdXdzZzdzMmNJSHhRb1JxODllRlBnVEZzRzFlSzZnRVJsUWo3SlJmU3FDekRGYU9ZeDByd1EvU3IrTjBFTGg5dWtaMGNHU1hKVnFPNDVo
!
aaa userlist usr
 username u
 username u password $v10$cA==
 username u privilege 14
 exit
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
!
!
!
!
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
 security protocol ssh
 security authentication usr
 security rsakey rsa
 security dsakey dsa
 security ecdsakey ecdsa
 exec interface dialer1
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
logging file debug ../binTmp/zzz92r2-log.run
!
chat-script login
 sequence 10 send ppp
 sequence 20 binsend 13
 exit
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
 username u
 password $v10$cA==
 vcid 23
 protocol ssh
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

## **Verification**

```
r2#
r2#
r2#show inter dia1 full
r2#show inter dia1 full
dialer1 is up (since 00:00:01, 2 changes)
 description:
 type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
 ip4 address=2.2.2.91/25, netmask=255.255.255.128, ifcid=346230569
 received 10 packets (660 bytes) dropped 0 packets (0 bytes)
 transmitted 10 packets (660 bytes) promisc=false macsec=false
 |~~~~~~~|~~~~|~~~~|~~~~~~|~~~~|~~~~|~~~~~~|
 |       | packet         | byte           |
 | time  | tx | rx | drop | tx | rx | drop |
 |-------|----|----|------|----|----|------|
 | 1sec  | 0  | 0  | 0    | 0  | 0  | 0    |
 | 1min  | 0  | 0  | 0    | 0  | 0  | 0    |
 | 1hour | 0  | 0  | 0    | 0  | 0  | 0    |
 |_______|____|____|______|____|____|______|
 |~~~~~~~~|~~~~~~~|~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |                          | packet         | byte             |
 | type   | value | handler | tx | rx | drop | tx  | rx  | drop |
 |--------|-------|---------|----|----|------|-----|-----|------|
 | ethtyp | 0000  | null    | 0  | 0  | 0    | 0   | 0   | 0    |
 | ethtyp | 0800  | ip4     | 10 | 10 | 0    | 660 | 660 | 0    |
 |________|_______|_________|____|____|______|_____|_____|______|
 |~~~~~|~~~~|~~~~|
 | who | tx | rx |
 |-----|----|----|
 |_____|____|____|
 |~~~~~~~|~~~~~~|~~~~~~|
 | proto | pack | byte |
 |-------|------|------|
 | 1     | 10   | 660  |
 |_______|______|______|
 |~~~~~~~~~~~~|~~~~|~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |            | packet         | byte             |
 | size       | tx | rx | drop | tx  | rx  | drop |
 |------------|----|----|------|-----|-----|------|
 | 0-255      | 10 | 10 | 0    | 660 | 660 | 0    |
 | 256-511    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 512-767    | 0  | 0  | 0    | 0   | 0   | 0    |
 | 768-1023   | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1024-1279  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1280-1535  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1536-1791  | 0  | 0  | 0    | 0   | 0   | 0    |
 | 1792-65535 | 0  | 0  | 0    | 0   | 0   | 0    |
 |____________|____|____|______|_____|_____|______|
 |~~~~~~~|~~~~~|~~~~~|~~~~~~|~~~~~|~~~~~|~~~~~~|
 |       | packet           | byte             |
 | class | cos | exp | prec | cos | exp | prec |
 |-------|-----|-----|------|-----|-----|------|
 | 0     | 10  | 10  | 10   | 660 | 660 | 660  |
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

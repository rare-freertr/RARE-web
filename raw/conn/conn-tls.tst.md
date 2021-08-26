# Example: ppp over tls

## **Topology diagram**

![topology](/img/conn-tls.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz5r1-log.run
!
crypto rsakey rsa import $v10$TUlJRXBRSUJBQUtDQVFFQW5aU2ZkWjZKdnl1dmNDN0huUHpGS0JLQjVRM25xVjdDaTRLMWkzVkM2RnNLWGF2VmlpcUZSTEpFczJtWXhnYWIzN2VxY2FyclhDdmlRQjNyVXgyNEFONGJNZERZeE1nREN1V1BTUEJaa3U1cjF3eU5Ob21mRDladExYZVZKV0lkVTdwS3F3VWlVczU0T3ZuTm5haUcyWnlDVWxhTDhsT2VuVWpNaDJRSXM1WEk4aWZoNTRyUytOc1lVaml2alI3QVU1Sk4xR01ZUUZPRWprVVZFam95ak0wcmg3Uy9vQlZ6VFlaY0wydFJaeXBuODFkeXRuZlZFRmFXVi9TbUxMd3dqMTE2Tk1DL2UzdXduYy84MmlvbUpyWVdHQmFXSnRNTVo5enhOTWhFaTBEZGFYd3Mwa21NOHhIYUcrK1NROG5XZUlYYVU3dzNaVkRDLzhvK2M4bXdyUUlEQVFBQkFvSUJBUUNXM1d1dEdCT1l5eUl6clJXKzN1R0M4L1VZYnErVUgvenh4RG83UWhERWxDVGdlVnIvNUtXaWwybmV1d0pnMUlMM05NZ2greGxLTFZsM09TM0xiWEIwcERBMUNWWC9UOTVaMkYzTjN3NWk5WkNaV3BMMzI5cEZOMjFmVWxXZ2JNYlhHa3ZTWUIvMFYyZ1VUb1RrcEN3MnV2aXFDK0lBSnI1OHB1M3AwWVBqS2NpblpVS2R2TTQ2dk1maUl5WWVBdGVjSEtsRUVld3ZzVHh1dVdRbkYvcTdFMWZZeFhRRmRqcHNueGpYZWZPdFgyMm1rdi8yeG16elJXcktCN1N4MUttSkx2TkpGdTUwRkRVSEhwWlo5Y1FXeWhFS2lSQlNDeERyUzRWWGVNWU1sYzlQcCtWVWp3ZmNtVWxJNENOODJscG1XcXhwT0ZycnZaeHdBYy9GeS9PaEFvR0JBT05SZ2tXNEQxNWI0YWRhZ3FDcjdwNHB3MUVLTFFJVkE3aDdpMjh5ZGVSRVFrK09KdWFTNGxtaEpXRW1iSU1ZRkFHbmlmQlNVV3laVHVvMmJZK1M0TEhsaG0rYnZJYjJUSnlTNDZHbkFLZDZubDJXd25TMEJSS3YzODVGMjVpVnRzOVdWWkpPUWQwdFc1Mm44d2RBMFhnVnp1bmhVQW8zT2NYMmZlYUhWdXRyQW9HQkFMRjJqSkVLOWJYK2Zmdmo2eW5OcWtCa2kwMDJtUHlLTFB4SWp2RTlPNGpMb29NRE1hOFl0bW5zeGNDZFJTSXFVbEM2bFF3UDJKUG5FMHpqVmxRVzdqZDdyeXRGVVNnT24xdDZzOVZGK3Brb1pUNG1TUllrWTF2NU9CMkpENXQwSzBBNGw3K0RFTTdVMGR2VUFsNHMvTWM1WjFGTzdEMitweGlIaHNWZWVySkhBb0dCQU5zZ0xHc1dwY0g0NGtwWHhvb3Brc2ptUzBCb2hjQjNEM0licmVxUUF2TDdGY3pvby9rcWFJV3NBSU5vN2J0bFQ0dlV1L1JzOWM2dzdsQjZEUjBVb2dMNjFaL3F5VTUwU0orNlBUSUw4V2FBbmY1cm9LR3RFeUxUWlBQTGhZYk44ejVrNC9JMysrZkFuSXNhWmZ4ODhDOUpIbjkzMFpjM2F6cTRoTjdmWWR0bkFvR0JBSWtkRzRhRmZVdGNrbUtvdXUzVnBoR1NuYjdPekcxekpVYlhtUG56WWFoVURnQkQyNE42Q0piWEJnUElmNzNpRFMrcXViWlVGL1pPdDY3VWg4TDQ1SjJoeHJvY0dKUm1sK0hLY0YvOGJaOGdndmorQThKRDR6RVE0YmFRUzZyRW14WkhvNWVvNExldDMyZUY2ejV3YSs1Ui8rM21tTWtzSVZibWY4N0hMTzNKQW9HQU01ckZCQU9ZSmwyYTh4MUZRVDY0MDRRYjJTK3Nnc2tBVmZkWFQvSGZUUDBsalBrYmU3dldFZDhIT1hXUUJqQUR2ckxPSGdWeTg4MGM4dHJwTmI3MkxCMnZXS2trMmExMHBlL2tRejQ4NDllSFdKdWlhZThCQ3d3YUJqc01wazlYVkhON0xiTmNCS21Zb0NiMW1oWWdYSGlBUExvckp2TE9XYjBSMEZGcnJIST0=
!
crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0dwMTExcmZwby9QWVdncCtFL0tIa05nc1I2Q3VFZ0ZONUcybGZZb1p2NExxVnprOHVnWEVndFU1dXcvR3dVRERFenlUdFRrZTdEaFp2SVI1aXdLZlhEaEV6dWpEaVBBS1lzNEV3M2pNRlRsTW9PMFh0L3pOd3hMeFBoZzkxVndwMU9rc1kvTE5yTHMza2xYOGVuRm1GcFJoeEdLSmdEOUVYT2pyNkZ0OWk5SEFoVUFsQThmbGhxRnk5WnlVeGZualkwOXB2aWc5SXNDZ1lBdHIwNksvQnQxV3Y1ZFRVeWRIYkNhZS93eGNDcGh4d0RYNERnVjhzS2Z1UGUrRUpIaTc3Y0wxdElscDR4T2h1LzZIb0dMaDk0a2lIN1NabGpleFFFQ1UrM0xHdGt2NmxLTWIvUjBiZWdnZnpGL28rKzJUallDcTBaVldHZldhRDhyTi8xSjQ0eWx5SmdQdU01YUF2YUVqdFhDU1gxRXpscVYwdExQRGhHVkVnS0JnREdLelp1bnZSUXRYMVZEOHZYSEtZSzJTeTBRdS9DTjNvc2ovRWZSdlRFejc4cUNCU3JZeXNEY2pKYXZNN3V1UHlHUjRBNjNDakFOcEtEMGx4b0hlOCtJaW03L1pHZzhVNnZ6dkh1UGZqdVFVUTN0dWR5anJKcjVWeG0wQ3dRUjlWdDhZektuWTFVMXVoU0VWc2pidVdSMVgxMmI1eDkvcE1lYmJGb2hVTXlHQWhRKzhTNVd1bi92R0NNN3NFV2Y2eUhkdjVCQ2t3PT0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURFaVZRQTZTVGJ1bVBtZHh0Qm84d1lmOVFoS0V1SFZ3Qzk0Y0pmNnRubm9BY0dCU3VCQkFBS29VUURRZ0FFdzJBYlcyOUdoR2xQdnh6d3dGVWlxc091ZzY4NUxvREdMYW12TFdqL0tJL08xY0FRUGlYZkxuVjNZTk1vcjRFci84WWxmYmF0SHpiNkJDRjE4ek0zdGc9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVRQkZnZURBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPVE0wV2hjTk16RXdPREUxTURnMU9UTTBXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0dwMTExcmZwby9QWVdncCtFL0tIa05nc1I2Q3VFZ0ZONUcybGZZb1p2NExxVnprOHVnWEVndFU1dXcvR3dVRERFenlUdFRrZTdEaFp2SVI1aXdLZlhEaEV6dWpEaVBBS1lzNEV3M2pNRlRsTW9PMFh0L3pOd3hMeFBoZzkxVndwMU9rc1kvTE5yTHMza2xYOGVuRm1GcFJoeEdLSmdEOUVYT2pyNkZ0OWk5SEFoVUFsQThmbGhxRnk5WnlVeGZualkwOXB2aWc5SXNDZ1lBdHIwNksvQnQxV3Y1ZFRVeWRIYkNhZS93eGNDcGh4d0RYNERnVjhzS2Z1UGUrRUpIaTc3Y0wxdElscDR4T2h1LzZIb0dMaDk0a2lIN1NabGpleFFFQ1UrM0xHdGt2NmxLTWIvUjBiZWdnZnpGL28rKzJUallDcTBaVldHZldhRDhyTi8xSjQ0eWx5SmdQdU01YUF2YUVqdFhDU1gxRXpscVYwdExQRGhHVkVnT0JoQUFDZ1lBeGlzMmJwNzBVTFY5VlEvTDF4eW1DdGtzdEVMdndqZDZMSS94SDBiMHhNKy9LZ2dVcTJNckEzSXlXcnpPN3JqOGhrZUFPdHdvd0RhU2c5SmNhQjN2UGlJcHUvMlJvUEZPcjg3eDdqMzQ3a0ZFTjdibmNvNnlhK1ZjWnRBc0VFZlZiZkdNeXAyTlZOYm9VaEZiSTI3bGtkVjlkbStjZmY2VEhtMnhhSVZETWhqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGR1ZkbnMzWFZ4RHE3c2s5Tk9ieTA2QXhCSUJmQWhVQWcrZkFhK0JSZWp1RlAzT2tCL0xLTGZwOFdpYz0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUjlPN0k4TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPVE0wV2hjTk16RXdPREUxTURnMU9UTTBXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFURFlCdGJiMGFFYVUrL0hQREFWU0txdzY2RHJ6a3VnTVl0cWE4dGFQOG9qODdWd0JBK0pkOHVkWGRnMHlpdmdTdi94aVY5dHEwZk52b0VJWFh6TXplMk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQVBWSEZvaVlGby9JMmFJQlRNTTJwZzBmQ3dHYnNtU090OG1PM3hSMVVBU3dBbDgyWVBJdWppV1JZOEVjWDc2Rys2N0w4c0hham9jU0NCRmoza0R5RGFuaGpadVpsbDRvK29aSEsrZzljTVREYUJKUEZFdWg5Uk1pdjhLdFlDMGNWUXc0NWN2S3hWbm5SUThSVWNtbmtNMG1rSE9LWjJHWUhsYW1DbXMzSzBDQnpRPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVYWFFQMHpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRBNE1UY3dPRFU1TXpSYUZ3MHpNVEE0TVRVd09EVTVNelJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQW5aU2ZkWjZKdnl1dmNDN0huUHpGS0JLQjVRM25xVjdDaTRLMWkzVkM2RnNLWGF2VmlpcUZSTEpFczJtWXhnYWIzN2VxY2FyclhDdmlRQjNyVXgyNEFONGJNZERZeE1nREN1V1BTUEJaa3U1cjF3eU5Ob21mRDladExYZVZKV0lkVTdwS3F3VWlVczU0T3ZuTm5haUcyWnlDVWxhTDhsT2VuVWpNaDJRSXM1WEk4aWZoNTRyUytOc1lVaml2alI3QVU1Sk4xR01ZUUZPRWprVVZFam95ak0wcmg3Uy9vQlZ6VFlaY0wydFJaeXBuODFkeXRuZlZFRmFXVi9TbUxMd3dqMTE2Tk1DL2UzdXduYy84MmlvbUpyWVdHQmFXSnRNTVo5enhOTWhFaTBEZGFYd3Mwa21NOHhIYUcrK1NROG5XZUlYYVU3dzNaVkRDLzhvK2M4bXdyUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQnNwWUlpeWNPbW91SlY3T1g3dTVXUDhLMmh6UDRVZFdxWWE2VFdDQmRhYWM1Rk5JRzdOK2ZZbGQ4TE5jZUlXaEtRbjl6UjNPdGVQWldwTXE4ZGZrSFo1cFJaMGdCMmtTUHA1RmlpaTFPaWJMR01yTlBDVVBUUUJCeGJrYXU2SDR6bExsMFZnSHBsM2RvRnFVbGNIZ3h4d09jdk5pMGlzNEdTWk9GM0VkbGxYelNCazJoZThMVVFHYnJnRzRubXBrYndBelRYOGdvZkRadFdhRXFmUnFkbW0wakJOTVdTcy9LaEdnaTA1Ri9ITlUzWFZrczM2Q0FPRTlyNFdVdllhQlp0Vkg0UjlwR0I3WSt5VGZNL0s0NTl2b1VNbVhIZlNidGxXVllxU3ZGM3dNTEU5SDJEMUxuZGttT3FzNktlVHIzdmQ1aWtPdjF6ZThzb1dTMm1ZQnJl
!
aaa userlist usr
 username c
 username c password $v10$Yw==
 username c privilege 14
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
logging file debug ../binTmp/zzz5r2-log.run
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
!
!
!
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
 ip4 address=2.2.2.51/25, netmask=255.255.255.128, ifcid=1008310525
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

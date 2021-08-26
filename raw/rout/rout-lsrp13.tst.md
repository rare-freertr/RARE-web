# Example: lsrp ssh encryption

## **Topology diagram**

![topology](/img/rout-lsrp13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz51r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQXBmR1EwMWJqQ2ZHZUlTcnYxMFJzaFZIVFIyUmlsdEFMRUpUL3VtVWZyUEd6Qm5DWmhpdGF4OTlXMDREOTlYV2dIWDRJdVR1a3cxT0F1UmFpeEpNVmFhOGVYV0NhaDdEbi9udEh5dDRkK1REbkg0cWNkbU1wR2xOcFIrOGhLNkU5OTlFVFdlTXJOSnh4ZVJ1NXBlMkd2dFo2WjBOVnlWc2w1Y0x3NjY3TjAxSVl4TVdkK2RiL01QVFlxMC9DRUErNTlKdkZXTnFZRXQvbzBCa1I0T2x4OWpISlpkSzlsTEc0aW55VVVDSnFQK3YvdUFlYW5uVjJLbnpnVmgxd0NXazdaNUdVdjJyTG5FM2lHNVdPK0lza1Bka0cxc1RnYnlydzJZTFdLa2VwOC8rcE8zb25Bd09mMmE5QTFUVHZSOWVrV283MnloZ05wUmkyUXhDbWIweFFHUUlEQVFBQkFvSUJBRWRkdVhRNmhNL3MrcDIzRW9qWTQzYit0c2VZVTVJYWpQZW5yTWRqNEJpSHBmK2FBMXloWHB4ZzM3MThWenZ1UjFzSHJnYkRzTnRVR1NNQXFpV3lQOTVBc3VWanUzR3Awa3d1aHJTbmkrcDBicUd4QWhNa0dEUTdOU2I3bjU5YzdBS2RCeDU4UlVPT0dIc0dRblFxeisxWTNqRjAwdnNTMlJ5VUZ2cTFKYzNBYXAxWlgzdlRKcE5YMEFHcFV0TmdGTnJNcW1hV1ZPQnlyZ2xDZ2VyYjhPUC9RalAxc3hYbDAzdTZpRUVzckpBc3pEdWhLaWpYZHFaODdCNkZHUnlsSG1kRHdubHVBb0NYeXA1RDRUS2dEY0xIelh4STBKakhtdXJnTm5YTjl2ZmFITW5Sby9WaU5IZk1oRk16d1h2YTdPaWlhL3FkdFVjbHhHNTEvSFNBU2xFQ2dZRUEwRmFtTEVWdjE1OUVqMlpHdmtVenAxZVdKb2xMWnp3RmFDeE1nU0RhcjNyUTBWdmF4UStSOWlmU3NDMDRhWUEveWRVN3RYdDZQTURkcndmUjBaQ0dUZXN3U3ZUMTFyZEdSRm53V3hHbFUyYktLMlB1UUthRmUrSG9xY0Rka3hLUWZuTE5KdkxtZ2QvQVZYR0NmQnFpKzNKRHhIMXFmVHBYWXZDQ28zb3hjTDBDZ1lFQXkrZ1BaWE04b2xaaUdSQU5UbnUvdVJwZW5MelM2SU83T2RKS0N4ZkRUVHRvTGNvTFlXS1hoYktuOXpzdklESGxNVXVTa3p5UDQwZklkYVFpcUtOa1hlcytaMFdrb2hKZ3N1anNrbEJEK1dEWlNNQXh1ZWFRT1ZWOWpPWVFReGo1b1JrQUpZbmVKL242bEt0Q2xGQjRmaHp2VmdwSkJKc29RWkE5MnpBMW1JMENnWUFVRk5ZTm5GL01hOWlpN2R2UnlUL1NXSG5ybXY0K3BDVnRSaC9Wcm9JRnVoUFlxajdyRWJZakFQR284NkxsWUd4Rm14MFhRQ0NuTEh2eHZCSTRYZkxrSGRCWTJVVzgvWXR6V1N2Mnl6dWhUMTRiVXBXTGU4R1FFRlZwejJKTUk5VHpxME1sQnZLN0FBTTgrU1QzcTJXY1VRWkJNVW1MYW8wenh6VUFadTNQRFFLQmdINTh6OEF4QWZYNS9CUnIvclVtMHNHeWQrcG12N1o0c1JXbk8wTXlWSForV1p1OTc5MVRXWWNZVWxWdEkwaW5hdk52VzlkMkJCUUxIWERNaHF0eDMvcmF5UFVySUh0aFJ4YjBvbndJeW9IUjhEZk84WW5PV3IwV0tUSFVMVlpTRWRnN04vb1JVZndlZDdEdG8vbDVDYVhCc1Q0QVYxZENJSEM3VjRPMm5paXBBb0dBQzJZTURIOGlKcHptNm5lRkFIZitBazEySVRZNjZaZm9IZG9RYjV3V1lPOHVCR3gyZ1RlSVFSbVVqUlRxMjFyaUlIWnRvZVlKNmV5ZTZSRm9JNGRoeVBiTElOdEhKL2tNd3dieWxaTjRMOStkYnZETksrVENoVFlIZHNOdEFoMjAxcmQvdzNBN3VVQVA0dUhJZWt5czVIc0VpM0I0SlRFQkE2NkRlK0NkV0RVPQ==
!
crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ZFUlAvaDl2eEUzWkpYQ1IyWUhRWEJ6NVBkUnZtbTJ2Z1NNeldJMTMwRVZYZXBVR2lmWnlOaC92d0ZhQ3FGVGpnWDlTNmY5bUNnbEtkbTBPNkEvbGdZV3ErVjA5TkdDamhrRmdUYnpUTHZBM2tFcndQNnhMNFZCSGZXVlJrQU13bmxCWHdmTXVtaGdzSUZ6NndtWHkwWlhsMEg4VHlPeTRQSm1HWTEyblNYakFoVUFxeW1MVjRhVUdsRDhuZWtUc2tVUytYKzl5T3NDZ1lCT1p3dENhd2xTSTZXUFkzTURVa0dXU1RxaGZwbzBydkY0VUx3cHdZVWxRNnE5MkZabE5VR1FSN1F2elBwWHZnNEJCYkdvOVlyS1IrUTdYcVowbjFETVZVRy93anR1RlBUa0QxNjQ5dVRkRnVyOGZYcEF4TUZHTDZxU0lBcmovSHhzSnJDNEZQb1BTV3J1NHZqTVdLLzRXdXdiUFVnS0pJbEFhMG9vcFZDaWN3S0JnQXZISkZGZWxiMnVzZlcvbFhPWlNNZ1RrRVJvUnJCM2JDTkkyckREQkYxcTR1L3NzQkkwdHFGVnRWMDFwVXh2cTYyS25iZTNNaFZlNWZPb1Bsa083MWY3NXVhWTNOaXQ2VnNobWFQQ3RzWjNyOG5nUmwyRnlhSDQ4aFRFUjBSR3dyYU5FbmRXUkFNK3hoRzBRd3R2Q0M0c2JHQ0R2Mk1zbnhmeWJPekZwdXRtQWhSRlE2aHYvZ1MvekR3cU95S0tYS1J6SlRha21nPT0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNQbHZrZlVxOXFrcmc2azhCY0w1azAvTy9OQ3lSL1BvNDJBWGk1Zi84bW9BY0dCU3VCQkFBS29VUURRZ0FFUjVrSFVwNldtWlpvR1FYSEg1U0VIZTJ1SmU2MnBYSFQzMFZlTkFnd2RXNlVkblJ5c09iR3dPSjNBVEE4bU5IcE1QQ3Z5SHZQSWdzcHBlZHVkU1h3c0E9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVWQ1ZiQ2pBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPREUwV2hjTk16RXdPREUxTURnMU9ERTBXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0ZFUlAvaDl2eEUzWkpYQ1IyWUhRWEJ6NVBkUnZtbTJ2Z1NNeldJMTMwRVZYZXBVR2lmWnlOaC92d0ZhQ3FGVGpnWDlTNmY5bUNnbEtkbTBPNkEvbGdZV3ErVjA5TkdDamhrRmdUYnpUTHZBM2tFcndQNnhMNFZCSGZXVlJrQU13bmxCWHdmTXVtaGdzSUZ6NndtWHkwWlhsMEg4VHlPeTRQSm1HWTEyblNYakFoVUFxeW1MVjRhVUdsRDhuZWtUc2tVUytYKzl5T3NDZ1lCT1p3dENhd2xTSTZXUFkzTURVa0dXU1RxaGZwbzBydkY0VUx3cHdZVWxRNnE5MkZabE5VR1FSN1F2elBwWHZnNEJCYkdvOVlyS1IrUTdYcVowbjFETVZVRy93anR1RlBUa0QxNjQ5dVRkRnVyOGZYcEF4TUZHTDZxU0lBcmovSHhzSnJDNEZQb1BTV3J1NHZqTVdLLzRXdXdiUFVnS0pJbEFhMG9vcFZDaWN3T0JoQUFDZ1lBTHh5UlJYcFc5cnJIMXY1VnptVWpJRTVCRWFFYXdkMndqU05xd3d3UmRhdUx2N0xBU05MYWhWYlZkTmFWTWI2dXRpcDIzdHpJVlh1WHpxRDVaRHU5WCsrYm1tTnpZcmVsYklabWp3cmJHZDYvSjRFWmRoY21oK1BJVXhFZEVSc0syalJKM1ZrUURQc1lSdEVNTGJ3Z3VMR3hnZzc5akxKOFg4bXpzeGFiclpqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGQWs3L2RZKzczb2JPTkxKVDdJN01yQkpraHg5QWhVQW5nUDJIaWpZTy9VNWM4ZXlMc3VuUTBrRHFLQT0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUXFnTmlYTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFPREUwV2hjTk16RXdPREUxTURnMU9ERTBXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSSG1RZFNucGFabG1nWkJjY2ZsSVFkN2E0bDdyYWxjZFBmUlY0MENEQjFicFIyZEhLdzVzYkE0bmNCTUR5WTBla3c4Sy9JZTg4aUN5bWw1MjUxSmZDd01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtSMVpXemxGNEc0Wno2R25pUUJ0Z2ErZC82QmwwbTNSTTB1YktSaTEzeE5BbDh4UzZJbGpiUzlubThka0lhd2t0TGtVWGlLTVZDS3p6TTl5b1ZuUGtyUjZKYk52dWRGNzJxRHVqN0xsUENrdmQzam1wcmdMZmFieCtBbjJOa0RNak43TUlSWXFoeTZ5NEZsNERTSWVmS3VmdTNwR1FtNW9yek8xQlpCSVV4bzRBPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVJdVpnalRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRBNE1UY3dPRFU0TVRSYUZ3MHpNVEE0TVRVd09EVTRNVFJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXBmR1EwMWJqQ2ZHZUlTcnYxMFJzaFZIVFIyUmlsdEFMRUpUL3VtVWZyUEd6Qm5DWmhpdGF4OTlXMDREOTlYV2dIWDRJdVR1a3cxT0F1UmFpeEpNVmFhOGVYV0NhaDdEbi9udEh5dDRkK1REbkg0cWNkbU1wR2xOcFIrOGhLNkU5OTlFVFdlTXJOSnh4ZVJ1NXBlMkd2dFo2WjBOVnlWc2w1Y0x3NjY3TjAxSVl4TVdkK2RiL01QVFlxMC9DRUErNTlKdkZXTnFZRXQvbzBCa1I0T2x4OWpISlpkSzlsTEc0aW55VVVDSnFQK3YvdUFlYW5uVjJLbnpnVmgxd0NXazdaNUdVdjJyTG5FM2lHNVdPK0lza1Bka0cxc1RnYnlydzJZTFdLa2VwOC8rcE8zb25Bd09mMmE5QTFUVHZSOWVrV283MnloZ05wUmkyUXhDbWIweFFHUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQmJwY0ZuZVJuTXBHZXBkclRsS0F1SWIwMFdqd0pRZ1RtdklRZEhQcVdUblphcEFUcUVJNWw4L09ZNTV1eTdxRm1mb2NsN1RTRVZJREN0MG5tZVcxeEZtdldKVXY3QnFoY2k1R1pDcGhGc3FScXREeDVEV0E3cWhjMWtlV3JwT015OVc5WWxGV2xOMzJxbWdjd0JpcGx1VTJENy9lU00wa0FxUHNsZ3dNKzhVcmZyMXZneUozS0lpZERXd1kwRnhGcHhEemlwWXZ6YXBRNnpmSWZva3FJVHI0eWFNOGVnYlhpcVJjL0t1ZWViU2k0eWxnMGNFVHRyRHRuNWIvQjQxd2d5VXppM0VYenJ5MC8zOUc1eUU4RE8vKzh5KzRGNWxuL0Vsa0JBZG5tOXVHSEFEVDFwdXJGUmw2ejlHZ0Radm5PZFNYZDhocWxmQjNkSExtd1duMUl4
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
 router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router lsrp6 1 enable
 router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
logging file debug ../binTmp/zzz51r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWc4bnRTdTIyeGVGSTk2ZlpOSUM5bGMxQVIyTkVtMFpPVG1MRlg5RkFJcHREMjg4Y3hieXRXSkcwN3NGM1N1ZHNFY0liRi9RRlhCdGgxVldaRHlCODlBSjRnTGlsNjl1NVpreFZDanNJMHFzdHk2QzZlaGZtU3NFQ3M2WS9OcXRDWUNzRWhBNXhxcTg3dXljUW4wU2JzWGw5UG45QmtqRXBsS2V4UU9WS3NWNUFjNEcwcEwxNXZHbzdZREZNVGJ1dUcrVExiYlNCYVlxeTllR3R2NUNZNFUwSlQ3VWNCN2U5SGprTTJLdWpUMkFkSnBwZ3M0QmI4MmNjb3JTc2ppTVZHQzF6YlJZUWN6bkNtTndIRVlya1ZhUnB4bXdkMzcyWnNucjlJMDVWOUk5NUxkWFVYQkhYMUZET2JoL2hDYjQ1NmxGelp6Vk8zSkFXQ1FZZG03RFBkd0lEQVFBQkFvSUJBRStRUXpCdlgxOEw2YytLaURtSVYrenVvNVgxdWwrOERGNktodnFZREE1WWlwbFQ2dHorVWZFYzFvMG1RK3oyMW1uS05DMDc1MWg2TjVCaVF5dTh3M05WWW9iajgxZjNxWEMzT01nYVovTTM0VWdFVzFDR3lVUHNUc05DNVBzT1hkNU5Xa2FYcWN3UVN4RnNQajdKWHUzQW1QcDRQWkFUR2pWaklFSTdxK0owVThWczJ6QmhjdENVN2FDT3Qxa2dzZTBaNExwQkc3WnFCKzZFSDRRVlRoZjV4VER2THhBYWdpM0NqVGlkQXNFeWM4Z0xGeFUzWURVLzdFZnhMT2FmeTRkSUZJbXhtVEtaQkREZWVFVHY3YisrSkFwQVpPOXM1b3JjTXpDaCtzN2p0bU55V3Y2bllxNURCTHBoU3VzOHR3QmZZQ2NhR09Wb2F1U05oZ2NxLzZFQ2dZRUF5bHpyL2pqMGdvbkw5MHBYcVY0aGFEZUphUGRkMnhqbDN1dGtFOUhJYkl4cG1YOXo0SGNqSm9FVFpDUzl3Yy9jd3BHR3duUjZwMW5sM3M2SnBEVGRxay9Pak1DVERLTythZnZ2eThwenFsSmxwcHJyMWd2UGlHQU8yZ3p3MWVIM0JxOEVYWWNtNk1JWDJLWEJERGRkK0lnL3hpSjByWlFzRlFOQjd6MVFJQjhDZ1lFQXByaEl0cFROVGt5a25rdlYxU1ZPRmdiYmU1ZDNpMXo5bkRNWTVodVBUSWd2WUY3OEszVmxPWUdEdmdpMmx6RmxvdWN0aDg0M3d6NStnRTMwS092SEpNZjFpcDRIMUZTenJ2MnNoTUhVUkw0TnRPdUZXOFVxZitMbHI1b1FxZTNoVlErNFZNREsvUUtobWt4Rmx0SWxPNURZbm9OdkpQRVBiNzlObXIxMUJha0NnWUJoYWJIQXd6SVExTHgyNGphb3RVTm5vN1JsN3c0ak5pMFJ6a1p5cy8zREl5U0NXN1F3VGFtQ0U0aCtJS0duOXFQU2xiTkZVRVRxNG4raGJkTWNWTWFRQWJMd1ZwTnk5aS9uWFB2bUlpTGp6cDVZUVNOZCtubUFzSnoxb2wwYzJKWE5oZHFZRzBORHNJdENJeWgyOVFBcmI0c2ptZHFJNUZjRUZubGE3U3p4Q1FLQmdINXY2QVUvMkd2M1NDa2N6akIxdUVDUU5zZ0dXUTBDR3Z2bzdJc21mNGpGQjFrSThDbHRRTFZaK2JXWEdoS1R6Y2E3bUJZVVdNbmpqVUIwM2lSaW00YlRkdTRIWjF5cVdCTHdJM1FUSTQ1MnJDSjNNNDRqZTFXOWwvK1MwZXh0a2FSVzVhNncvOERkeS8wZXR1L29zMy8zRzdFcmNKRU5tRzFoSWRPbXR5YnhBb0dCQU1qRHFTRGRJMnRuRUdySkVTcVdPNm1xMG1ndWYzL1BaaExTMXlUQlYwdDJsaEx1dTNxZ09YcDFKYTRHWkxoVlpJMWVWeWVwSVp1VEkwNDF6dFpHK25ZNUI0TVFwSkpVaGRQK3Y2WWFtWGoyd0N4YXhUNUJJcllTTDVTUzN5cW1jSUxuVHFuTVVjK1RjTkFUS1JvK1J5QnFKOU55OXQ1VmhoVE1UWFhDeXp5Sw==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDaXRqVEJsa3dGY0EyMGpDM2tobjV4ODUyS1pNbXhBVnFidU42eUdoQW9mVURoSTc4YW9zSEYvWWFudlBpNHozWjJ1OHhsZlI3WXlGUUowU0JCNE9DVk5TZEdadkFXb2oxYjBJWDVOVWU4Q3ZsMmV5ak5MVjVPQ3BPQ2pMNzlLcmhEeXkwRWcvckk5VW5jSVNBY29NQTc4ZDMvU0R0T1hHTU5OMUsxV3NPTjdRSVZBS2ttbHVWME85cE9vTjM3ajgzMTR0Vy9qN3NwQW9HQWYxZkQyUzBTUlJMR3p4UjFGbVBiQWlqSFRJYmp4Q0diNG12V1k4clNrelB4MWVjVnNIeUs5aVBsR3ZmRS90VWlBK1V0RzdkMHJFM1hNTUtFZERudTNNc2RKblZtQlVSTXN5QUw5bkhraVdLOWdhcjVia2VSMHBrUHR4RkNiN2pGSk8yS0dQMFdHWWRuNFBzVTdTeVJzTEI4Mm1ZYTB0WWg2U2c0L2NHZXhwNENnWUJuZ2tWalJsekIzQUIxQWtmSCs5UmZVUm1OTTRPRksrQTJMdFhVSDBxYlc1ZFhDL2NXUk45TnJnNGNRMFMzNVRLVFVOTlE3OWJsRFJrYUxPcm80VFBucUFieEZ1RTJSV3VGVU95ZUN1WlMyN042YUo0S2E1cWJwdXNHc3VkbFpQYnJrR2N2bGkwN1NtejBSblhtd2k1MzBYOU05NmJYakVPOWd2YXVUb21KeVFJVVJHUFBSVUFnRzZWcDJlVGJURGxkajY5N1psQT0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURaSEViSzVWTTJMaWRvU2VzeUFrMFB0YmVkRHBKQ2ZacHpadTE5OG16SG9BY0dCU3VCQkFBS29VUURRZ0FFaitaY2JobjU2dDFoVnhnZVVDMTFsUkN6b2FrSHJyanMyNUV4V3cvNlpHaFQyNzUyalVrcUZWaDlvVHNSU1NXTEhMR01yN3B3TVNIZUQ1K1lYaXBSUlE9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1ZEQ0NBaENnQXdJQkFnSUVILy96WVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFPREV6V2hjTk16RXdPREUxTURnMU9ERXpXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDaXRqVEJsa3dGY0EyMGpDM2tobjV4ODUyS1pNbXhBVnFidU42eUdoQW9mVURoSTc4YW9zSEYvWWFudlBpNHozWjJ1OHhsZlI3WXlGUUowU0JCNE9DVk5TZEdadkFXb2oxYjBJWDVOVWU4Q3ZsMmV5ak5MVjVPQ3BPQ2pMNzlLcmhEeXkwRWcvckk5VW5jSVNBY29NQTc4ZDMvU0R0T1hHTU5OMUsxV3NPTjdRSVZBS2ttbHVWME85cE9vTjM3ajgzMTR0Vy9qN3NwQW9HQWYxZkQyUzBTUlJMR3p4UjFGbVBiQWlqSFRJYmp4Q0diNG12V1k4clNrelB4MWVjVnNIeUs5aVBsR3ZmRS90VWlBK1V0RzdkMHJFM1hNTUtFZERudTNNc2RKblZtQlVSTXN5QUw5bkhraVdLOWdhcjVia2VSMHBrUHR4RkNiN2pGSk8yS0dQMFdHWWRuNFBzVTdTeVJzTEI4Mm1ZYTB0WWg2U2c0L2NHZXhwNERnWVFBQW9HQVo0SkZZMFpjd2R3QWRRSkh4L3ZVWDFFWmpUT0RoU3ZnTmk3VjFCOUttMXVYVnd2M0ZrVGZUYTRPSEVORXQrVXlrMURUVU8vVzVRMFpHaXpxNk9FejU2Z0c4UmJoTmtWcmhWRHNuZ3JtVXR1emVtaWVDbXVhbTZickJyTG5aV1QyNjVCbkw1WXRPMHBzOUVaMTVzSXVkOUYvVFBlbTE0eER2WUwycms2Smlja3dDd1lIS29aSXpqZ0VBd1VBQXpFQUFEQXRBaFVBZzVIRjhBakEzNjRzMlZ2ajFEdldLRm5BcVpFQ0ZBT2xlOXFVVHA1QnM3WnVmeVdHZTdzRlc4R3g=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUWR3SmwvTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFPREV6V2hjTk16RXdPREUxTURnMU9ERXpXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTUDVseHVHZm5xM1dGWEdCNVFMWFdWRUxPaHFRZXV1T3pia1RGYkQvcGthRlBidm5hTlNTb1ZXSDJoT3hGSkpZc2NzWXl2dW5BeElkNFBuNWhlS2xGRk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnT3pwb2dmdE9qZDYwblZraEIweFRSUVlyNENPMGVvSDErbEdXSmoraGk2b0NYdzRxN1VwVXo4QUR3WENqY3ZvQ1JUNXZuQzJCTmExbGFiZGpQSWhRczN3eWE3ZTkwNDE3RHNjOThHZ3k2VGlTQ2F6djYrMnlHbXhDYThMUUl6NGVoVTh0TkJXaEx6M2FINHpoS0dPTlhMK3hQVkR5SzJKaHBYMnJ2MGZnYXdpKw==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVUVGs3QmpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRBNE1UY3dPRFU0TVROYUZ3MHpNVEE0TVRVd09EVTRNVE5hTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWc4bnRTdTIyeGVGSTk2ZlpOSUM5bGMxQVIyTkVtMFpPVG1MRlg5RkFJcHREMjg4Y3hieXRXSkcwN3NGM1N1ZHNFY0liRi9RRlhCdGgxVldaRHlCODlBSjRnTGlsNjl1NVpreFZDanNJMHFzdHk2QzZlaGZtU3NFQ3M2WS9OcXRDWUNzRWhBNXhxcTg3dXljUW4wU2JzWGw5UG45QmtqRXBsS2V4UU9WS3NWNUFjNEcwcEwxNXZHbzdZREZNVGJ1dUcrVExiYlNCYVlxeTllR3R2NUNZNFUwSlQ3VWNCN2U5SGprTTJLdWpUMkFkSnBwZ3M0QmI4MmNjb3JTc2ppTVZHQzF6YlJZUWN6bkNtTndIRVlya1ZhUnB4bXdkMzcyWnNucjlJMDVWOUk5NUxkWFVYQkhYMUZET2JoL2hDYjQ1NmxGelp6Vk8zSkFXQ1FZZG03RFBkd0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQW95cWlZTk9QaXBNRmhNejlOaFRrdkpjZ3QrTDJ1Rmpnd2VKM2kzY3lURkplQjBYRGN1WFBmNGJxWFljZkhnMTU5R1Bsdmx0OWI0b09kdGxPWFNLZkp1QnFZTFFUQ053TndJR053bmNQT0pZOE5lbnh1ZUU2L3R1bldTOGxNTTRuNGFDbktrNGc3OW5WaUp5T1ZlbWRwSURPRDNwM1Y4UTZIbkNoTzY3NU9FRnVubW14RngrSHpKSlJ4QWd4UUZGaFpYckdRN2kzMTBGK2pZMUVTYnY3Qys0c0FmUFBuQy8vY2ZEOTMxYXBWdjJGQW5QZ3JDSXVSSzlFc2xjY1ZVeS8vQ2RWQklucVRkYVo0TTVRZk9iTDU4TWNwdkx4REp6TWhSeCt5SUZwWHk4RnMxc2dXU2taNjJDbFpueDYzRkRLVk56eWY3cVVsL0VTVmRUY1h2cXlN
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
 router lsrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router lsrp6 1 enable
 router lsrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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

## **Verification**

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
 | 4.4.4.1 | r1   | 1   | 2   | 6   | 55c2a7bf | 00:59:58 |
 | 4.4.4.2 | r2   | 1   | 2   | 7   | efc4fb78 | 00:59:58 |
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
 | 6.6.6.1 | r1   | 1   | 2   | 6   | 722ed93c | 00:59:58 |
 | 6.6.6.2 | r2   | 1   | 2   | 7   | bda3d49e | 00:59:58 |
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
 | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:01 |
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

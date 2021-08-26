# Example: pvrp ssh encryption

## **Topology diagram**

![topology](/img/rout-pvrp21.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz81r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFCK01RWXk5cWVZUE45eDJLOGlEN3RMR1RwanhlTlhjQ0pwSk9IWFMvY3pUcDkyZGtoWXZwTTZHM3VLVmkyamNYMFFVOWNtS3RlbFRsS2ppK3VOZzB1ZFhVdkY3ZHRRNTV2dTRYS1hzUHUrQ0lCOEE0TFQwOXNUbGZicjg0VFJVTW5VQWlWb0dYdTAxS1IwTGZnbi8vTG80MXdNcDBVT0p3VnVHRG90NEcyLzlKT3Vha1lpbXZCUkZnd2N1RXRBNVVDcjJQSnMzbU1sSEdlZGc4Z3RYOVlyaHFjNGhCM1hGSlBOendPZkZzY0t2VE5adEpVck9Cb0N1dE5nTVBNVm96eTduVng3MG5iU0JnNmJGazZkSE9EYlNBcm80bVlvQVNjbUUvc0NGc3p1dXF5QTE0Zm1GRk0wU3ROOWkyV216aHp0K1N4L1FDeU1Sa0FCSnh2ZkxHRGJBZ01CQUFFQ2dnRUFHZHlFTDdlYSt6a21kZGQ1ZE5xU2dMNkgxK0M3U2JVaWFEZjF6TUMxeFo4TVVTUEdpZUZzbk5EN0RZdkJ5S2crZ0RVZWQ2VDZFdGV0V2ZVWDdpV0ZQcGZiS3BJbml6b2NHK1c2TFZwSkRWWUN0dWVsVFRJeXlKM0lQK3psUUZ4MU1Hek1LN3hsUE5jRGFRZnV2b3ZXeFdHckFMRGJGeDVxSDNqNW0yTk9Pck5pY3p5MlRoQVg1RCtDcG0xUFVTeVFhY0QxMCsrbXN0eUMzSXB3ZWozcUt2czFab1l4K0ltOHVtbnZEVUNRMTFNRFdKTlpjVS9RQTltZ1d0K3FNOGUyYVhMSDNrRzU4d2xEYWpRTGlhcndZRUY2MW9pVlhJaTdpNjV0blZ4QlMwYS9KZEVEY3RVVll0Y1RGNHVQdUY4SVRqQzdYWlZFb3BYM0xpQ3FiRS9WQVFLQmdRRGhBUDhnZWk3bkVrdFRMRU11dkdvcDFVUVI5RkQ2cHFubndKUi9ibmE1djViY05VUkxidmErai9QNnB6a0Zjdm82MktHSFZLdW9VZS9Nb1B0Ym1zWHNjdklFZFRtbGVNOFlXQm8zaGJLdnFqVDBkek43NXo2K3lnOTVPajhZTkttYUxudGNabFArVFBYRTd0QWRvb1VUQ1M5SWZHSXJ0cWQ5NmRsZ01DQWZnUUtCZ1FDUGswMS9kS1Y4SjJESmFKMW84TDc5ZTFuNEc1WDBSZVFmcWc2Szk3UDdYM2JLV2NXbmk0UnBMM2l4a3FUU01rNVQxSkNRK3Q5eUlxcW9iVFlSR0lPNTVQWDFqeUphZ3ZQdjR2Z0VKcUtOaVJrZ3hrakZ3QVlXN1BRSWZBRDZjSWZzaldmeHRmeXNNNTlIZjRjcVNLamNnYlpKTjBDS2tVdlpsemlIQ2hndVd3S0JnUURQeVVYU1RrT0dMUVRXMkdkcWY2Rmk1SW9xTW4rZUdjK0tML1J6QWlZdVAxb29IaURsc0tHNU5lTlFOS0dhQUtaSk5jbGwyckZ6amNkd0o3STQxR08zaWljcUtyK0RxbDlGMGdiVUEyb1NnNUxIdUZVWk5XSmlldU56Um5FQi81QW96SWdydW13U3lpdWxKQTJaY0g2SUo5RThsWEZyZ1JDSVhTN2JmMVlMQVFLQmdHZHFIV2NSdU9UTlpFeU9XdHNzbFJUMWxWODlWMnhrTHlXVGt2Z0w1UXJKdjBHUEdleE5kT2xpdFJlS1hjZTlUbWZaY3V2S2w4bVpLTDA2TkxocHBPL3YrQzJRbEprSE8vZHN6MklHQmczV1UxQWxJbU8xcFcwNzdhWnkweTJRZ29jamIxeE56aHFtOERKS3JDd0x1LzFnUE5GTngrSkhONUFaK1RCalYvbURBb0dCQUtudWcrcUw3eUJFT2tsc1pqUVA0MXlnMkVOVUFwcDdickxyTDl1cHNJaVJqSmxCMjJUcXpQT0ZyNVF0dStWVmZqTk1TQUh3OGNiTG1tWDZBUFlja1czVFdXcTNuYWlrdVltYWFyL0g5UzNza1h4NjVldjlRNFg1aDI3RldIN0VDNDlLTDlZZzJSemVXbXRXNFh5dmptT2NieGtVWmpvb0IvdHo4VDNPZGM1YQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0J4cWh6Zm5jYVoweGcrdGJ5NUpLL2VFbnZHMm05N1JjaDR5YVdpQWYwVEt3QVBybTVmc0ZZaUlKL3R0cktOcncwVlh2VlFOVW8xRWJaeHVxVDRuWHFaampRN0p6ekE1MUJOaU1FOFA4ZlA4a1EvU1dlWWRmY04rK2hWYzBSeVhjL1A1MGVLUzN0N2hqWlhFNkE1TVRtMC9rdFA5WXJCQTdwRU5neGJ3UUFnTkFoVUEzRWJ5V0ZEOHJnNENxQ1NlYnZDdGRzWnlwU2tDZ1lBVnpWUDI3ZThDbUllbEZSREZ5NUVWL0lqMVMyeHhCeXNCUmN6ZG1mYjFpcnREaytyYklMR3l1Tis0YnRwWFp3K1RjYnI4by9RakpyRUY2VFBsZXZoSkpxR2h3bG1vZXNFYzQ0d1RjbGJtRXdkU25UZklVbGFoVmNFVXoxZGRFbHNkR09KTm1NYjZlSnUzbXB5cG00MEtvOWV0MFZYWUtTSzV3Z0E2NGt3YmpnS0JnQU1TWURvelhyMTJXYk9mbXRSRlNXN2pJeEl5eWZ3OWFQSjN0THNBSllzaDB5SXNNcld0YThVUW5ZdithRDlOV0NZSlRGQWdrMGRzaWZtU2FGMUp6aGE4bjJ2MmtLMGQwZHpFOFJEbThlMTJBaTFOeXMrMUxOZmVQYWthRlV0dnpCc1FWOXlvRVp2VCtjSEgwckx4RWJLWVVtNEpUaklYQlZHM1N1elRSMXVKQWhVQTZ0RkNBRC85amFycWlXQzE3ZFpjVk5NcW5DYz0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNOK3ZueHdMdzZrYTZvUVFWek02RFNJb3RhaHFUSE81V2xWdHYwdmROdG9BY0dCU3VCQkFBS29VUURRZ0FFdFJVQS9scFhDbEU4VHNGcGROWVFHcHEraWxpOVFHTThWdE9tLy92M24rTFFKUmRqYXZNVnFMSmxWV09mWmovN0p4UThSTGpwaE94cHk0TjYxaE96YlE9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVPbGJOMERBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFOVEkwV2hjTk16RXdPREUxTURnMU5USTBXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0J4cWh6Zm5jYVoweGcrdGJ5NUpLL2VFbnZHMm05N1JjaDR5YVdpQWYwVEt3QVBybTVmc0ZZaUlKL3R0cktOcncwVlh2VlFOVW8xRWJaeHVxVDRuWHFaampRN0p6ekE1MUJOaU1FOFA4ZlA4a1EvU1dlWWRmY04rK2hWYzBSeVhjL1A1MGVLUzN0N2hqWlhFNkE1TVRtMC9rdFA5WXJCQTdwRU5neGJ3UUFnTkFoVUEzRWJ5V0ZEOHJnNENxQ1NlYnZDdGRzWnlwU2tDZ1lBVnpWUDI3ZThDbUllbEZSREZ5NUVWL0lqMVMyeHhCeXNCUmN6ZG1mYjFpcnREaytyYklMR3l1Tis0YnRwWFp3K1RjYnI4by9RakpyRUY2VFBsZXZoSkpxR2h3bG1vZXNFYzQ0d1RjbGJtRXdkU25UZklVbGFoVmNFVXoxZGRFbHNkR09KTm1NYjZlSnUzbXB5cG00MEtvOWV0MFZYWUtTSzV3Z0E2NGt3YmpnT0JoQUFDZ1lBREVtQTZNMTY5ZGxtem41clVSVWx1NHlNU01zbjhQV2p5ZDdTN0FDV0xJZE1pTERLMXJXdkZFSjJML21nL1RWZ21DVXhRSUpOSGJJbjVrbWhkU2M0V3ZKOXI5cEN0SGRIY3hQRVE1dkh0ZGdJdFRjclB0U3pYM2oycEdoVkxiOHdiRUZmY3FCR2IwL25CeDlLeThSR3ltRkp1Q1U0eUZ3VlJ0MHJzMDBkYmlUQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGRlVJM2pHM01xTnd6a3NEV0dua2ZYM3dJQ3JxQWhVQWljOFk1d28zblRXWE0zTktYK3BaRFFreHUzcz0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUUJla1VaTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05NakV3T0RFM01EZzFOVEkwV2hjTk16RXdPREUxTURnMU5USTBXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFTMUZRRCtXbGNLVVR4T3dXbDAxaEFhbXI2S1dMMUFZenhXMDZiLysvZWY0dEFsRjJOcTh4V29zbVZWWTU5bVAvc25GRHhFdU9tRTdHbkxnM3JXRTdOdE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUp3eDJFT0dycXA0R3VaMnZoYjloVlBiRXJCeEJ1OVlIMENJSEVnaU80cjFBbDg2S2dXWmFSdEhId3F2UHZQRit2TnBEajU0WTNuVFEyOFBJUEl1ckhZRU52ZUJZTDN4OWEvN0h1Tng2ck44dTcrRDJzMnNzYTVuVnVTVFhUTlpqSjNlZ0x6R2JtT2VoeTAxclI1VFF0ZXpkTVk5UGJ4WDdGbVpWVkUvMHdRVmxnPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVSSWxidXpBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TVRBNE1UY3dPRFUxTWpSYUZ3MHpNVEE0TVRVd09EVTFNalJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCK01RWXk5cWVZUE45eDJLOGlEN3RMR1RwanhlTlhjQ0pwSk9IWFMvY3pUcDkyZGtoWXZwTTZHM3VLVmkyamNYMFFVOWNtS3RlbFRsS2ppK3VOZzB1ZFhVdkY3ZHRRNTV2dTRYS1hzUHUrQ0lCOEE0TFQwOXNUbGZicjg0VFJVTW5VQWlWb0dYdTAxS1IwTGZnbi8vTG80MXdNcDBVT0p3VnVHRG90NEcyLzlKT3Vha1lpbXZCUkZnd2N1RXRBNVVDcjJQSnMzbU1sSEdlZGc4Z3RYOVlyaHFjNGhCM1hGSlBOendPZkZzY0t2VE5adEpVck9Cb0N1dE5nTVBNVm96eTduVng3MG5iU0JnNmJGazZkSE9EYlNBcm80bVlvQVNjbUUvc0NGc3p1dXF5QTE0Zm1GRk0wU3ROOWkyV216aHp0K1N4L1FDeU1Sa0FCSnh2ZkxHRGJBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFDTEs2VFZHQ2FkWmozYmJkTC9JS0tkUXdHSVkzSTdDMkRnRnVacXBBeGRxb3NiaVQ3VzlQajZURWFLNzlKeEowRThRSmE5dnNBSFo2Qklrc0c5L2kwZmt4YlFOQ1JMNVhsSVZ0MXZDYnZpbGhGOEhsTW9OTFdoL3l3bUovN1htZ2d2ZG4xUWNtOG03cEJtWmo5R2FUcHB3Nzg0SU9uTTRjNGxEZ1VzUGF1YW41b2RKcDYvS1JPajZudmNxM1BWQ0JvTEdjMHR6TEVIdjVXcnJqcHJDcW91SEoxYlZLdmRVbXk1M0tScFVnZnk0K1g0cm5FQk9VYjhXdDlnMVJISHM1czJZUnAzYTJvRVVreVpNTDFtcXh2ZWdwSzFBQ2pCMVFSYnArYXhCVUpUKzJGZThwZEJJMWltRE5hRWpnNXdtR3g3Y2NsSVZsYXZybXQ0K0pIUkxVT0k9
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.1
 redistribute connected
 exit
!
router pvrp6 1
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
 router pvrp4 1 enable
 router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
logging file debug ../binTmp/zzz81r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCVEpIYlR0cE9YR29UR1ZYam5kQVI1aU1GaDQ0Z0lXcFdYV0ZMVCtreC9mTm9JQ0s3dVd1YzQveG9zRVFuV3hKRENpdWlzRzltTEo4dWh5ektFbnVaNDVtWStyU1ZEU2pPVU52WmpObDZMT3dYM05ucEJMeEpENElXRHZWTnFad0t3b1ZtQmtsR28wd1crWVJ2YWFVQXgrWXdrR2tieHZBU2ZGamNhbW1ydjJOdVozVy85dHpkTm4xcno3d2R5eG9pd2VWbG5sc0NqUWlDdTRHRHdpd3R1dFgzRmpKUVU3aVJLMmN5Sk5VckxHK3FlaTEzdkNWUGlZVmZMYzFUalZsQkRVUkpkdDZ6WlJiREJzZzZFbXlIczR6OXFtUlVaT3BOcGI0TkFMMCtxbmVvbzlPd3RDZkF6Ui8zbVFvRTlGUnowbG9KbEV4L1FNZTRMZXBuL00rUG5BZ01CQUFFQ2dnRUFEZWx1RUtMZU0weDJweEVxTitCTDEySXdxWVorL3BiWnJRZFVaSy9mR1AzMUpaNytWbGZUbE0vcXV6RG1xbzhkZ2Mvb2V0UDJKTGkxOUE2aUYxclhTYWVUdUMwVXJSdS9ZYStJcnJVc1FMUFJuYm41M3VwWGJoQWxoeE9vMzRiNUJrRVpUdnNDdXZNRVpRU3V1bThlRkw2aTJtK2pLMVBBbWpZSFptWXNPcEdud3pneHVjd3JlS1g0M0dSZzFURSt1OHRpV0FNd21XQ3NESXNHL25FVURqdEtrbmErbEJzSzJlQ1BIMGRCcGRuRVI5YlkyZjBEam83dVg0M3MwU3h0K1Q4WkZBMjFFT05WbEFEZkt3Y1MxWG1lYlkyWExveVljdHQ3dTFxcU51WjA2bDNRemY3K0R6QjhLV3VXSDZCUExZLzdCZG50aXQzcTdvamJXcHkyNFFLQmdRQ2Q1ZFZ3L2FFNVZTK0F2ZlJhR0ZLS1dIRXRvU1RQT2xmc0YzTVJ2TXRpR2src3ZVaE9TWFdFRDQ5UGkxN3B2Q1J4MmVXQmtVcWtIbzBRVkhjdW5TTjY1Szg3U1Ntc0sweVN6dm5HdGVKeWtwSDZMNUt2YVRCUHBaZHl6MmRkVGQ3bUs5K0RpcVBaL3drYWU1bzg0bDd4MXVsd2E2WFVlbUptZVlOY2Y0WkYyUUtCZ1FDR3pJdGI2Y1ZJVkFJd2lCL1FTWXl4czZKdVJvYW9zMXI1Z0NaOTU0Q3FVNGFlNUtpSnRXVlNHU0M1YVhMUW53U3VrR0F1L05IdThqbzZWV2gyQ3BmajJkNC94MCs5TXUrc3ZhdDF6SjFmNjdMbXFBdVFDRElSV2xPalpvQUNBM1dybGUzSjJNd09UeXhHTnVKY0YxUUIvRGdaUXdqVkFUaXQvRHlUdjBTZnZ3S0JnUUNkcU1YTWdwT2ZDWjNhOE5DeHZTTjltLzIyVC9iUExEUnFPcWZkQ0NRVUdxMS9qNmhJOHpSeDNvOThIMjl2OXpwMHE5dHIya1VyUm80WHhoOFMzamgxRnk2WkJkNmtXTCttdngvTCtBVFozZHdBY2N3SGRnS1ZKSVRxVUltbk1uL2tWOTVnRytpclhPb2NGVnJXZkRuTlJJZm1ocllZU1BORDJ3VDlNU0JEVVFLQmdHZTF1NHFOd3lFd3NUYVJwSmhsM2Y5aVM1ZzRYcVl3eDgrcUR2TlRSNlREK3BFSkw3b3plNjY4Y25iMGNFZWQ4TVkxZ2lya2pNZ2dTVGhVT2JpSDBmQ1YwTzZVOC82R3ordkJTY2VxRTNLWEx0OVRid0h6ckVHNWt4dm1ZcG9wKzBCMmE2cWVSL0RDYlRmZ1JpdkFMdndRQjBFNFYvVTVxVmdDOXNCZHFmaVZBb0dBRmhyWWRPNnNqZUpmQTJGbTRiS0FITEt0NFRpQ0hTS2RhKytJWk1TQmJBZi94VkxmVlVqTll4RzhBdGlIVGc1OVQ5U0tyZC9uUmhSVnVlWStJcDR6dEZqVDhKeWwzdU1HbEhoMHpwTVBqL010VCs1Tm53RTNEWlR2TDc5NVZrYzRsYzM5VkZrTDMwTWNtUEo3a2Vxemk3azV4QUxKOTJ1emhYVFRsWkVJa3p3PQ==
!
crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0NhUmQvYjV0SGJMZXA3ZVRaSVQ0eEVEV1NKY2lsWnBnaHNmalBtNkljRW9zVis2NkdiSXJBREo3S0hnUzRxRWxTQzM0MDhwVFdpeFloN0JVYk0xWXE4R3A4TEZRZEtGa1d1NXg0d20va21ScUx6OHQvTS9ZTlM1V0JnRWlXWGk0NzJQMjBLNHJIb0diYmNLeUZ1UTRqZTNIdDJmZ3poaGI2bWcxUGcyRHl1TkFoVUF3Q1R2MCtsM0VlNmhEZlpsaDhSTVhjbVg5YmtDZ1lBVE9IZHpZbFJFd1g3aDc2U2NXelFpMUtoRXhibXBZN2s0TUpId3JZdjVCdWg5M3J6WUdKZm96c2VFY09zZk9La05XTGFURng2dXNQNGtVQStGZndyWFFOZndCVERoK2M0TEFBR0lFU3BtL2hxaUFjdUpFZFlYMms5b0kvaEQ4S2ZXZzA1ZkludE5BbXB1VE1ITE9Ja1Y4ZGFEYnFMUkpYb1M3R0g0Z1BtalFBS0JnQXBHRUdxQjdGcktBZCtWVXNrN3NSZllMZ0lOc0FZclZ4UFQ0YnBZcmFkMVB6d29ucEpYWStlNXBjL2ZZemdzZUlDVjFCazBJbnNrcU03bWp0T1hoOHRCZ2wxdy9oZDV1SzBFcUYvREdEbFFTbmhxcWRIT3JHMng3d0N2eWpCTGdBMFUveVJrcFFSMlUzT2xOVHIyN1NZMmZoVENvdWhkaFdiQmU0ZU9CRnZhQWhVQS9rZFRkZU1qV1Z0VE4vV3lwQlpYTFJIWVJJcz0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMnNXd3lFQ0RkUDQ0Zm9CRWJCQzE2ZzN6U3Y5bTFqeDhCazBkMkNzTkdHZ0J3WUZLNEVFQUFxaFJBTkNBQVJjWHZlMDFlamdQZFA1Yyt4d2lEd210bloxb0lRT05saUMrRm94a2Q3Y3kzMThDMDl6QngrMEdHUUxlUnNxd3c3SnFtYWZQcURZY0RNR1gxejNKU1F4
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVFL1k3VWpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFOVE13V2hjTk16RXdPREUxTURnMU5UTXdXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NhUmQvYjV0SGJMZXA3ZVRaSVQ0eEVEV1NKY2lsWnBnaHNmalBtNkljRW9zVis2NkdiSXJBREo3S0hnUzRxRWxTQzM0MDhwVFdpeFloN0JVYk0xWXE4R3A4TEZRZEtGa1d1NXg0d20va21ScUx6OHQvTS9ZTlM1V0JnRWlXWGk0NzJQMjBLNHJIb0diYmNLeUZ1UTRqZTNIdDJmZ3poaGI2bWcxUGcyRHl1TkFoVUF3Q1R2MCtsM0VlNmhEZlpsaDhSTVhjbVg5YmtDZ1lBVE9IZHpZbFJFd1g3aDc2U2NXelFpMUtoRXhibXBZN2s0TUpId3JZdjVCdWg5M3J6WUdKZm96c2VFY09zZk9La05XTGFURng2dXNQNGtVQStGZndyWFFOZndCVERoK2M0TEFBR0lFU3BtL2hxaUFjdUpFZFlYMms5b0kvaEQ4S2ZXZzA1ZkludE5BbXB1VE1ITE9Ja1Y4ZGFEYnFMUkpYb1M3R0g0Z1BtalFBT0JoQUFDZ1lBS1JoQnFnZXhheWdIZmxWTEpPN0VYMkM0Q0RiQUdLMWNUMCtHNldLMm5kVDg4S0o2U1YyUG51YVhQMzJNNExIaUFsZFFaTkNKN0pLak81bzdUbDRmTFFZSmRjUDRYZWJpdEJLaGZ3eGc1VUVwNGFxblJ6cXh0c2U4QXI4b3dTNEFORlA4a1pLVUVkbE56cFRVNjl1MG1ObjRVd3FMb1hZVm13WHVIamdSYjJqQUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGRkwrYVhDdEg0QXdISTNUTXl0ejFvY2thZ0pqQWhVQWdKNzhsQ2JmT25MbTQ4ODlZLzRmNXVrSTFYZz0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUmpRMzJnTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05NakV3T0RFM01EZzFOVE13V2hjTk16RXdPREUxTURnMU5UTXdXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSY1h2ZTAxZWpnUGRQNWMreHdpRHdtdG5aMW9JUU9ObGlDK0ZveGtkN2N5MzE4QzA5ekJ4KzBHR1FMZVJzcXd3N0pxbWFmUHFEWWNETUdYMXozSlNReE1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnSklzWXR1UXB5T1oyYUVlbGM5MGdVOWo3eldpT1M1ekJJR0FjeDZpR05uY0NYd0laS0E0Um5kZWZEMHpmU3ByUUZrc1lpYlNNODVBZ1drMysxVkJiVXYxbS93UUdjYXZjVndwSVJaUDM5OW9DTzZkVWRqODBTZm4wd1Nuc2t2Wmd4SnMyZVBXR2NlU2piNlUwUVliKzJxRXdYN2xSK3dPWFhRM1luOENFY2s0NA==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVLYzZBRlRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TVRBNE1UY3dPRFUxTXpCYUZ3MHpNVEE0TVRVd09EVTFNekJhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCVEpIYlR0cE9YR29UR1ZYam5kQVI1aU1GaDQ0Z0lXcFdYV0ZMVCtreC9mTm9JQ0s3dVd1YzQveG9zRVFuV3hKRENpdWlzRzltTEo4dWh5ektFbnVaNDVtWStyU1ZEU2pPVU52WmpObDZMT3dYM05ucEJMeEpENElXRHZWTnFad0t3b1ZtQmtsR28wd1crWVJ2YWFVQXgrWXdrR2tieHZBU2ZGamNhbW1ydjJOdVozVy85dHpkTm4xcno3d2R5eG9pd2VWbG5sc0NqUWlDdTRHRHdpd3R1dFgzRmpKUVU3aVJLMmN5Sk5VckxHK3FlaTEzdkNWUGlZVmZMYzFUalZsQkRVUkpkdDZ6WlJiREJzZzZFbXlIczR6OXFtUlVaT3BOcGI0TkFMMCtxbmVvbzlPd3RDZkF6Ui8zbVFvRTlGUnowbG9KbEV4L1FNZTRMZXBuL00rUG5BZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFEdHZwRm1nR05scTV4RTNUSTlTOEw5S3B1N0ZUbitFQldDMWZlK3pxUG1ROXhGb251cjRIb3Z4RlRzTmxoZjZ6a3g2MW1jWi9MZXZvMWt1VUpnSWtiK2N5YTNKeFNjWVZMOHVsUUZBb2ZNZW9BdzM3bmk1WVNlSjdrK0NsQ2hFRVcva3g2QnViTExHWHNOMHRlVTJ1aEJXNlZFRkhKUmp0QUcrRHNZR01IRThWOUpxaHRSeTNGWjN4VTd4TndKMGN3UXNUUlkvSEdOT2xwTE9mLzRmaDNPTW1Jd092MTROd29YMUs4dWxHdEM0Nlc5c0dWck9ZcG1yc1ByM0E0VHhUbDdZUVUxY08vL2ZVZzFQUi84c1BQM0orNFBiN0ErQ0RnSWFzbVAyRVZwNFltQ1VKOWpkUWpicEJjMW9LNlZJdVFHajZ5T1FYbCtEd1dpODhxN2UxbTg9
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
router pvrp4 1
 vrf v1
 router-id 4.4.4.2
 redistribute connected
 exit
!
router pvrp6 1
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
 router pvrp4 1 enable
 router pvrp4 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
 router pvrp6 1 enable
 router pvrp6 1 encryption ssh rsa dsa ecdsa rsa dsa ecdsa
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
r2#show ipv4 pvrp 1 sum
r2#show ipv4 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer    | learned | adverted | uptime   |
 |-----------|---------|------|-----------|---------|---------|----------|----------|
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | 1       | 1        | 00:00:07 |
 |___________|_________|______|___________|_________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 sum
r2#show ipv6 pvrp 1 sum
 |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|~~~~~~~~~~|
 | iface     | router  | name | peerif    | peer      | learned | adverted | uptime   |
 |-----------|---------|------|-----------|-----------|---------|----------|----------|
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | 1       | 1        | 00:00:07 |
 |___________|_________|______|___________|___________|_________|__________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv4 pvrp 1 rou
r2#show ipv4 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix     | metric | iface     | hop     | time     |
 |------|------------|--------|-----------|---------|----------|
 | C    | 1.1.1.0/30 | 1/0    | ethernet1 | null    | 00:00:03 |
 | null | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C    | 2.2.2.2/32 | 2/0    | loopback1 | null    | 00:00:11 |
 |______|____________|________|___________|_________|__________|
r2#
r2#
```

```
r2#
r2#
r2#show ipv6 pvrp 1 rou
r2#show ipv6 pvrp 1 rou
 |~~~~~~|~~~~~~~~~~~~~|~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~~|~~~~~~~~~~|
 | typ  | prefix      | metric | iface     | hop       | time     |
 |------|-------------|--------|-----------|-----------|----------|
 | C    | 1234:1::/32 | 1/0    | ethernet1 | null      | 00:00:01 |
 | null | 4321::1/128 | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128 | 2/0    | loopback1 | null      | 00:00:11 |
 |______|_____________|________|___________|___________|__________|
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
 | P EX | 2.2.2.1/32 | 80/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
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
 | P EX | 4321::1/128   | 80/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:12 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

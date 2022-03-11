# Example: lsrp ssh encryption
    
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
    logging file debug ../binTmp/zzz26r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCbmtDdnpXd005WUdMQ0Jwano2QXJaTGwzTDFWOHBtcFpxTXViZ1lER05VSTN5c0lQeVFiYWNWSi9mMVV5YVVhdDQrTno4bnNKWVIzQUNjS2QzYXRZTHArZzJaOUorZ0laQ0FaWEdnRktBbUNvOERtVU85UVI5MkM3Vk5kNVdIcWMxTElNYWFERldJY0NjOC8wSEE1VjVYajYzK0Z3NFZJV2s4Q0s5bUw1c2ZKTHVMZ2JFZVZRKy9maFp0L0lTQ05pM1J6VUJXeUNCUkY3eERHbXJzLy9EZDBJZElnaVE4ZjJxR1FoOTF5STFYVmc3a21tTjNvaG9sdnFQclpuWUVwNXpGUjBnOUFKM09aNk5qa2RWVXVqbkkxZ3AyeFN1VFJoNlhuVG1RMEEwWFhWaWtheS8vK2ZhZXkzdWZtL0o3OThKc2xDRHE2UXJlOSt3VVZ0YThjUS9BZ01CQUFFQ2dnRUFYNGNaUTJ6Y1hDMGdhNkR5VFducE45UVJLUWcwczRlbzMyVDhtbE9nNFoxQWtuQklCWnFmK3l3RUhNLy96UWt3aG5Ib1JnMmJieHJXTXluL0Q2UTR0Sis1RHhaTmorcTE3UVRSUnp6dTNUZC9IYzZaWVdhWk1ndkxoMWdkTW9zcjZWeVp3aTRCOUZWRitvRUZFUWM1UmE2dFk3MXdNM1dqb1RUd2xycmlTK2FmKy96SVRINjR6ZjkwRTh6NlRNRlp0QUJteTBWN0FMancvdXNZVHZUVEJhdEpDS3ZxWE1RajZzYlBVeGM0R0JIMCtGalIxV3poWFVwdkxoM2VLekZGSDZDUUhvTlVHMmQ4OXhJVk1IUXdIbDBXZWRMOGNvUis2QXRqM0VPaU44SG9Pc1RySzdOcDVzUHJTZUpjU3RlSW43VlVTT0wyWnRsNlR6aC80UHhUQVFLQmdRQ3VTdUlxcVRFY0ErVnY2R1lmQXVRUzJmTDJBUjk0TEVrcDdvWlFHa29sWGFlbnRuenArMEF4VDF5ZmNrMjBVYUpyM3A1YmR5MmdHQW5NTXJYNVJZWE5wR2plK0JGSHZFYzBveTExS2pacy9nSWF5MGNLeTVWazlBK3FKUWk1RmpBcDB5eHZOVEVMZFIwYm8yQnNyTzNqdFBUbjFwaDNjVlBVL05zYnR2bHUzd0tCZ1FDWUhQTU1EajVCQk9nY3c2T1VsSi82S3FuMmZIYUMybnB0MTB1Q3pUekpibDlSMFRpMnJYdTUwK08zaksrM0NSSjF2djB4WVZBangwdU9wSFp1akFPUzlZSEhGUUJsUXRuSVpBbmZKbUVpdHpqbWFLOUlzSFNWS3VVWHVqTjRmREFzd3hhdmpuQmlqNTlwNVFTL0xyNWhWMXR1ODNvUXlYaEc5NXpmbTFBMm9RS0JnRXlqTHJtVmRidWMxdmtURmp4U21CalY3dWhPN0JoNldKMXdmV3loY3JMbGNIL2xWUjNKVlp1WkN1QXRjWTkxU2RibXAza09lV2hveVg0WldqekdYaVJqUTUydk5HSDNudE85WUpLaFFoZEF4WW9ra2hOa0cwZXRyV21pS1NqQlllSXlNZHFnWi9WaXhLN1BjdW0yVEZBUTFKTlFuKy85UytCZVlyWFlDZXUvQW9HQVB0SWw1bUt6ZnpMQmthK1NqVGhjWVhyaE9yVG9WTjVhRmFjR3ZueDRrRkFPK2NGSWhObGM4Yi82bWNGMmlFY3M0b2dBRlRhMVhERmdtUVovQ3VTMFRTc3JiOGJTcFA5WTVoTzZwL2czd1ppZDNUcDZ1YkIyVld5anRJcm4ydWlmRkwxMVR3ZXFqbW4yVWt1TkRGQUh2RGZSd1I2NDJObjczSU5Ddkc1dVVFRUNnWUVBazNDZCtBYmw5bGVLTUhMKzROZ1phQ3VNTWU5eW03TmxReTJpbks0U0s3QjdlUndDQ2lOdEJYanlTUUhnMUZ0S2RkREc5aDlSbzlDMVRIRjdHUGNHbHZMUWtCamFmRDdXVkFQQnIyWTI0bnNDZEdCNkNzMDFMa2duc0Fqcys5aW9wVTZ0ZWFFWThvQTk0SGpLZnJMNHZPMWk3MWR4K2o1WmczME5BdFlXaTlVPQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ1FDS1RCRmtzU1hKMmtzYWl1SUo3bWc4bUx6eXhhdi9FUzVzNnNUazU1d3ZkaFlIc1B3UEdxalNSN2RscUJDMmdtV1l4dUR3ZkFUSDFJTjE5ajFOZEJRL21ralRRdTFmUmlxRCtxWXRid08vMFVVakRPVXJkV2tCbGxZN3NWMTVKclhscjdPMkgwQmpDZDB5MjhudjF1WVhDM0d3NjYvdnhHYXpyazRxa1piazFRSVZBS1BKczQxWWpuVGE4VTRqN0NEQ0JNZHh3ZjlwQW9HQU1Ea2NVSWMzclMwVWtGS1Ryd2Y5bnFiOVZmQmo0dVlqT2w2OUZKRTZETlpUcDF1OEMzMEg4SkllZml5L0dQcnc2L01QZmVaSTlSUmtvTklveDkrMFRVeUtFWVM5S0kyZG1kT1BMY0hEK1JNVmdLTjN2cGFsVUdiMm93RDhIek0yMnpibjlaV1Z0MEJyamZEQVNzQXdFcWloTldvYk8zR1d4QndDVXA2eXBOVUNnWUFZME1Fa1hLeGcwQXMyemRHRCsrRnF2dXI2YVVTZk4wY3VTdDJzanpaUlk3bVYzT3JqSmIrME43bnBSRzRpNm5jK2xPdmwrVkpSQVFTR2laYXhwUVJRYkJ6SmpZbEQvQk5IWHluRzZKbGdsWDN4LzFucFhpYldNcDhad1Z2Wi9xa2ZTSVQ4aHY3YlQ2SWYraWRnckRKajNTTjFzbkdSRGRTUHBDNUZKMlZVa0FJVWZCdEhpaFE4Q3Bzb0hDRlVQM2I3NTdaYW9QOD0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNDYTNjWnErRk9VZ2FkZmhya2gyLzJaQ3VCSERhWTlZbkhZN0hmZXRJMm9BY0dCU3VCQkFBS29VUURRZ0FFUTA3NjArMnNBVjN5cU5DUzNQSHkwcGlmMjFyYVJWcitZQmRzTFAwZEF4eU05MSttZ3JpdktRMFNHcTdsYzFDRGdFdFUva2pqQlNvQnVUTjAzVkJDdlE9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBaENnQXdJQkFnSUVRTnhuN0RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNREE0V2hjTk16SXdNekEzTWpBMU1EQTRXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYll3Z2dFckJnY3Foa2pPT0FRQk1JSUJIZ0tCZ1FDS1RCRmtzU1hKMmtzYWl1SUo3bWc4bUx6eXhhdi9FUzVzNnNUazU1d3ZkaFlIc1B3UEdxalNSN2RscUJDMmdtV1l4dUR3ZkFUSDFJTjE5ajFOZEJRL21ralRRdTFmUmlxRCtxWXRid08vMFVVakRPVXJkV2tCbGxZN3NWMTVKclhscjdPMkgwQmpDZDB5MjhudjF1WVhDM0d3NjYvdnhHYXpyazRxa1piazFRSVZBS1BKczQxWWpuVGE4VTRqN0NEQ0JNZHh3ZjlwQW9HQU1Ea2NVSWMzclMwVWtGS1Ryd2Y5bnFiOVZmQmo0dVlqT2w2OUZKRTZETlpUcDF1OEMzMEg4SkllZml5L0dQcnc2L01QZmVaSTlSUmtvTklveDkrMFRVeUtFWVM5S0kyZG1kT1BMY0hEK1JNVmdLTjN2cGFsVUdiMm93RDhIek0yMnpibjlaV1Z0MEJyamZEQVNzQXdFcWloTldvYk8zR1d4QndDVXA2eXBOVURnWVFBQW9HQUdOREJKRnlzWU5BTE5zM1JnL3ZoYXI3cSttbEVuemRITGtyZHJJODJVV081bGR6cTR5Vy90RGU1NlVSdUl1cDNQcFRyNWZsU1VRRUVob21Xc2FVRVVHd2N5WTJKUS93VFIxOHB4dWlaWUpWOThmOVo2VjRtMWpLZkdjRmIyZjZwSDBpRS9JYisyMCtpSC9vbllLd3lZOTBqZGJKeGtRM1VqNlF1UlNkbFZKQXdDd1lIS29aSXpqZ0VBd1VBQXpBQUFEQXNBaFI3cVhOeFJGQXhQU3VTRkNTclE0a1hPd0gyVmdJVUF6Vjd1aEFVZEsrQSs5YnJST2V4VHBTaFZWVT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUk5jRndKTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNREE0V2hjTk16SXdNekEzTWpBMU1EQTRXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFSRFR2clQ3YXdCWGZLbzBKTGM4ZkxTbUovYld0cEZXdjVnRjJ3cy9SMERISXozWDZhQ3VLOHBEUklhcnVWelVJT0FTMVQrU09NRktnRzVNM1RkVUVLOU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU1PVHF6NnpTendZeHhFeEt6QStNeDBHVFhaQUY2MXF4Skx3RklYRGNPdGlBbDloL2ZjVmloYW9GclBFb2xyTFpCOUdTN3FGNDNRMUJKY0pDSFJVUjRIcWtWKyszZ2hzS2grZTdRRFF6OUVmR1kvZEtsRmlKZmdkVzk1MkpaQnVYT0k2NFJTS3NpVXZ5dm5LTDV0QTcwY2FLeU5rM1h1U1pYNU1CbzR4d2RpK0ZRPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVBSXgvSFRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFV3TURoYUZ3MHpNakF6TURjeU1EVXdNRGhhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCbmtDdnpXd005WUdMQ0Jwano2QXJaTGwzTDFWOHBtcFpxTXViZ1lER05VSTN5c0lQeVFiYWNWSi9mMVV5YVVhdDQrTno4bnNKWVIzQUNjS2QzYXRZTHArZzJaOUorZ0laQ0FaWEdnRktBbUNvOERtVU85UVI5MkM3Vk5kNVdIcWMxTElNYWFERldJY0NjOC8wSEE1VjVYajYzK0Z3NFZJV2s4Q0s5bUw1c2ZKTHVMZ2JFZVZRKy9maFp0L0lTQ05pM1J6VUJXeUNCUkY3eERHbXJzLy9EZDBJZElnaVE4ZjJxR1FoOTF5STFYVmc3a21tTjNvaG9sdnFQclpuWUVwNXpGUjBnOUFKM09aNk5qa2RWVXVqbkkxZ3AyeFN1VFJoNlhuVG1RMEEwWFhWaWtheS8vK2ZhZXkzdWZtL0o3OThKc2xDRHE2UXJlOSt3VVZ0YThjUS9BZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFFWmpkcVUvNDZPQjFQRnZ0blhubmNwRnd6c0tERitPS1VjMHd0UDl4YmVUTVBkczB2R1M2blJRMzczRVdySGZRQzVxT1Q5YjRhKzN1SFNYTVI2V1hjZUZkQWR5ZElCT0JRdHZlREtVcWFsMnNETFFJZmtwTHJsdkszaHVheGpaeWRyVFRLek9DU3FwZEp2V2tMYUwyTjN6dm1PMk1GdTlBblM4UndDcVpuYlNSOHc2RFZnbVhzN3M4RWNaRWY3VmV3NXliY25jRWtSWk5QTVo5Zm5kbXhkR25JQS9USEJrRU5BdHRKcVBBNnpIOEEyc3o1RHBLQ3Bzb3BrSWVoQXhPeHZsZDFQOXE4ZERiYXd5a3Jzd010RWs0RUZLSXlYc0hvZEFwY3RtQlJWaUNuVWFHb1B0OUNmSzhwN2FiV2VzL3hSdXI4Ym04RE53R1hoVmhMN0pvaFE9
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
    logging file debug ../binTmp/zzz26r2-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFFQWpwOExJcGRuRXhsMmZoWGJ6K3RSK3QzUWlqSzVUYWpKVFhQbDhvYmhYMW9uMjlaSDl2bGtVaUlNRlMzdEE2TE00d2xMRyt0TThJRk9Jb0RjTkN4WjJIaFpsNzlMTWdyaWhrY2tDRVkzTHhVR1A3d2hzZWp2UEh2RVJmUjRDRXA1V3gzMVRaWXRieEJZR1dtTnRTN0gwK04rTTlOT3ZnQW82Q2xmMkJnalByM1ZYNlpERERNUkw0eUsvUU1RWUl3YXo4NnYxcnJWTTRxZFh3eS9uQTBzWlI5RnB0N0JZaGVxNGd0Rzl6QU9hb1RWek90aTZDSFl4QUhzTWtkY1NIUlh6R2JhdGtpWHdTZkRpVXNZdmlnQjlLR0R1N3JjQUZQSVV6RlB2dXZhOHFBWS9DS3U2SjA3cUlmb3VnOVdJSE9ackV5ZDZxUk1YYkcvMVVrUTRCR0hhUUlEQVFBQkFvSUJBRHdYWE55MVNCT3ZEZEx3S002QkN1aVZYeEZyYjlIOXhOdGljc2R0OXpWeXlncUJUWThNNHkwTDlXVlRGV01MekNINHYzSERBWWJ3SkZpN1RJeWJCendDOFZUVG43NDFBZDZyeU0zSHIrYWhpQ0dBaGYzczlDZmF5Z2JqaTFPSzlYamp0WUI4UHlabGo0a2RoVHlLdWwxWG84djRRMXdndXh1ZW15aDBleDBxd24xQ1JZaGpLSGU4U3VGS3BLT0ZROUdXY2pZMWNpb1JLSW04SzZQSnZpSWEzUWgra0RpeUpZSTIzLzhtTzMyTE1zZTFMSStKYzVyM0NieTEzS2NNaUQvaW5CenQzVE5ROHh0YU5sRktZTXNRQ3pnVHBqNUg0c2x0Mm9oSFNOMWI3RUVPaDd2YmQydkJYSVRybDg3bURuQ29mUXArLzN1YTVnN1doMytleFJFQ2dZRUEyZDlvendDbHBlU3Vqb1NodlF4V1dzYVR4ZlVLemNjWXVZYkUwMDlFWDdKRmhMUGkzR3lBVVE4Z3lSMmdxQmpBeVZ2ckNOakpSS3ZTU1RLVm1RZk5ncjhSODVXVytIVzdlRGZ1WEtjcno0VFAyZTJ1ME5TUTBLNHJXei9VRmxhYVlVUGxYNkVFVVF4NWpRQlFGVnQ1dTJKTkJtbnVlaVRYbjZ2aHRlQWpLdFVDZ1lFQXA1Um9IRy80TFF4SDV0RXA1UllGWVZXT1I3Nk53Q3ZYY3JyOHdCWkNFd0NEaGR5ZDVmeHJwNTlyMjJ2NWtMQ2V5UlJJVnEzQUNEODJCSlp2YW9WSzNIY0tkTzZPZHlaSU1zUHk1QTFwT1NCWmV4UHptakg3TWdDcm5teGQvRFgvTzBaNkkzMDZhaU9zbWpXZ0JZT1NCNi9MYXR6eWIyV2VQMVZRbzI3QkRFVUNnWUFUK3RMbnVNMTRDeUtlMnpiaDJWSEovVS9yNVc3YU5Cbm1XWitQS1VQQjZ0MUpNQjNyek45dmo0MllJK2xwd090ZEM5cmY4dEZ5UkxlQ0V1dDVIeWdQaDJva0JtSFQ0eWdQL0VFVnFoYndidU9JdnEwN1pXTHFZQzZGcmJMTFlhSENyYkZKTmNEcGxkVkh3dkdWSTlCa0NMMjdpdGRkeUNjbDgyTTloSkoxQ1FLQmdIcWx6bERKeml4Q0tibVA2Z2FsU0VqRmtqMkdCRDdhbDNONzBSSlErQWpxUGxoUmNDcnJ4R3JJN2VxSXF2MnZsbmI2WmpzeUxUS2IrTkFBdmdpTEI1QTFlNnk3RC8rNlArc1BxSXdxR0pIYjBFR1pCNWdaN292Wkc4SDE5QTlzQWFJRFljN3BqMEF4WGRqN1dHUFF1S2J4allKbnRQTzh2c1lCamVRZllpQzFBb0dBYUliL0F6Nzh2dWREOWFCZExuaURsMlZlL3h2NjdZcCtUZExQQmo2VDJoU2RqZTk1TWc4d3A3Vk5hc1g1djNxeVRKRFF0bVdGMlF3Y3BBQ3pjaEFPOHdvYjlnNC9EZ1kyQ0hNZVNoYkNBT0xnQ1pkUnMzL2RXeW5lci96MXRJeCtrM08ySFhTSXJ6UXRoZDk0b0hEaE41SWdiamFyTXV6QlFnZko2NmJZN2Q4PQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0NXMUlFeElhZkhMd2NCMy9yZi9hWUxIc3dGeWN3aHNMK1RoYzJicEcvcDlsMDBZN3pFb0tIWWpYdDBnWDBGS0x6VHlUMmNRYlpNMGVmak43SWxCZ1djYmhnaUZaNmpzZDQ0eVhTMlphbE5UYUpaOHNrM2RUdUcvL1l0VCthK2w3SjJ0Q3JzWHpEbjFvdi9VTEdMU3VGWVM4K2tDSTE0OWQ3RkpJZmpxeVRhREFoVUF5VG1MRTd6OE5hS2U0Q1REZDZXbEJZZW1wU3NDZ1lBWnE4NllpZDA4UnRteTJLU1V3Rk00NFZoZDR2Rzl2VHVXYjBFTmZ0Zng3THBkbWNwb1dyeWFxUVpBM3Jqc2VQRXJscGQybnFxVzVBSFF4ZklTZFJzR3AzcU5ENmJXaWNFNDN0NjRmZlZDNllyVDlWck9RaStrUlh3T0dNMFFyQmFnYWxCZmhqQW5TSnVHLzZYMVNHNTZmVHlRb3lWUkpUVm1taXBoYWxiZmlnS0JnQTN3MXEvN05iN2dManVWbUFBaTA5Z2NzdGtNV1d3QzJYa0luRFpMdnBQR1pMRHNzRzJVK0lyUk9OTzVHcFhXUlcyZXBEeVJ2a3E1Snhwa0F4NWw4NldzN0l3YU1WeHhwN2FuNTlta3ZxWlRpZElrb2dJZS9pS2hJdTM2VGJ0QnE4R25kY1RkNE5JOW82V0xuMUUxd3lLREk2MGRQcGdaSDZvSHBxZ05lSTJLQWhSWHhjWTIxcjdZOGt2MDRVMllZS0dyYUpYdWRnPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMCt0QTZmKzcxa1pPMTFiNXhvaXlUdDRvWi85T3BSaFI4aDlZMzMvQWp5Z0J3WUZLNEVFQUFxaFJBTkNBQVRWM1VsSUcyc3BLVmNPZmhnZmVYUjg5L2pTSmlRT2VlbnpwSkduY1pvaUVudG9zcitubDY5WnZNVXBFTzlpMkdpWlhaRndDMjVyNGd2bFo3MCs2MjJP
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVZNHlPaVRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTFNREF5V2hjTk16SXdNekEzTWpBMU1EQXlXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0NXMUlFeElhZkhMd2NCMy9yZi9hWUxIc3dGeWN3aHNMK1RoYzJicEcvcDlsMDBZN3pFb0tIWWpYdDBnWDBGS0x6VHlUMmNRYlpNMGVmak43SWxCZ1djYmhnaUZaNmpzZDQ0eVhTMlphbE5UYUpaOHNrM2RUdUcvL1l0VCthK2w3SjJ0Q3JzWHpEbjFvdi9VTEdMU3VGWVM4K2tDSTE0OWQ3RkpJZmpxeVRhREFoVUF5VG1MRTd6OE5hS2U0Q1REZDZXbEJZZW1wU3NDZ1lBWnE4NllpZDA4UnRteTJLU1V3Rk00NFZoZDR2Rzl2VHVXYjBFTmZ0Zng3THBkbWNwb1dyeWFxUVpBM3Jqc2VQRXJscGQybnFxVzVBSFF4ZklTZFJzR3AzcU5ENmJXaWNFNDN0NjRmZlZDNllyVDlWck9RaStrUlh3T0dNMFFyQmFnYWxCZmhqQW5TSnVHLzZYMVNHNTZmVHlRb3lWUkpUVm1taXBoYWxiZmlnT0JoQUFDZ1lBTjhOYXYrelcrNEM0N2xaZ0FJdFBZSExMWkRGbHNBdGw1Q0p3MlM3NlR4bVN3N0xCdGxQaUswVGpUdVJxVjFrVnRucVE4a2I1S3VTY2FaQU1lWmZPbHJPeU1HakZjY2FlMnArZlpwTDZtVTRuU0pLSUNIdjRpb1NMdCtrMjdRYXZCcDNYRTNlRFNQYU9saTU5Uk5jTWlneU90SFQ2WUdSK3FCNmFvRFhpTmlqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGRE1mTjJBb0kwUER2T056cG1meE1jbmNaeXJSQWhSTmhnY1JDRkVyeko5aGt4Z1RDVE10R1pLSzlnPT0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUlF5ZXJ6TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TXpFd01qQTFNREF5V2hjTk16SXdNekEzTWpBMU1EQXlXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUVjNVbElHMnNwS1ZjT2ZoZ2ZlWFI4OS9qU0ppUU9lZW56cEpHbmNab2lFbnRvc3Irbmw2OVp2TVVwRU85aTJHaVpYWkZ3QzI1cjRndmxaNzArNjIyT01Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU91cmFlckdobVNiSFBOcGFOa0xDSWs0MW5EQ0lVcG1tbWFXVnlWMjdjbGtBbDlETVFIMjdnWFJCaTkvOWFYUjVaU25PcjEwLytNd29pdTA1ai9YbkR2dFdYN1A3ZU5lRFhnYVIxajZPSUhsUjlwMVJiUjJwTG1SclRzS3JHcXRQbXUwM0p1alRzdkFzU1B4K1BBWU1ReWFLeHlwZEJjYWFid0hNbzJQaVRnUXFBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVSaHVsS1RBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBek1UQXlNRFV3TURKYUZ3MHpNakF6TURjeU1EVXdNREphTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWpwOExJcGRuRXhsMmZoWGJ6K3RSK3QzUWlqSzVUYWpKVFhQbDhvYmhYMW9uMjlaSDl2bGtVaUlNRlMzdEE2TE00d2xMRyt0TThJRk9Jb0RjTkN4WjJIaFpsNzlMTWdyaWhrY2tDRVkzTHhVR1A3d2hzZWp2UEh2RVJmUjRDRXA1V3gzMVRaWXRieEJZR1dtTnRTN0gwK04rTTlOT3ZnQW82Q2xmMkJnalByM1ZYNlpERERNUkw0eUsvUU1RWUl3YXo4NnYxcnJWTTRxZFh3eS9uQTBzWlI5RnB0N0JZaGVxNGd0Rzl6QU9hb1RWek90aTZDSFl4QUhzTWtkY1NIUlh6R2JhdGtpWHdTZkRpVXNZdmlnQjlLR0R1N3JjQUZQSVV6RlB2dXZhOHFBWS9DS3U2SjA3cUlmb3VnOVdJSE9ackV5ZDZxUk1YYkcvMVVrUTRCR0hhUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQVprVDRVTzdURlpwdGVaWlpNU3ZLVzhpamIyd0hUeFExY0psblIrcm9wdGtvN3c2L3RyOU5WdzIxMmJxZ3hhRExPMHAzOUQ2eWlZK2JSYkxxUHAyRkw3VlNRSEtqVXdxQU1rODV6Wmdka2ZGK0FVNzFGZDU3QkJNU0NvQXVqSktmVlNsaWpuVUNWVXZLRVJSSlNPdXowMzFBWURMM1Y1THNxQ1Jod0o5U2h4dFBZK25lbVpJazIyQ1dqMTNXNTdnNll4d2lWWUpQMlRTRDVJN2h4WEc1ZFJvVEE5ZVBZRnN0bkdtUDA3ek9oYmtxUzBsWSs0Y1pmTXQ2dXVOd1RZRmlvZWp1NWFmS0xqU3dKYUpRT1hBa1Z4ekN2NFZ0S09QdXNKTVAzL1VFSDkvRk5qdHpDMGNzNnVTMkZFRUhSSExNdTMxQWFTbFRBdW1tY2VEM0gwWERZ
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show ipv4 lsrp 1 nei
    r2#show ipv4 lsrp 1 nei
     |~~~~~~~~~~~|~~~~~~~~~|~~~~~~|~~~~~~~~~~~|~~~~~~~~~|~~~~~~~|~~~~~~~~~~|
     | iface     | router  | name | peerif    | peer    | ready | uptime   |
     |-----------|---------|------|-----------|---------|-------|----------|
     | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:09 |
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
     | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:09 |
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
     | 4.4.4.1 | r1   | 1   | 2   | 6   | 58f0e2a5 | 00:59:58 |
     | 4.4.4.2 | r2   | 1   | 2   | 7   | 542fdff7 | 00:59:58 |
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
     | 6.6.6.1 | r1   | 1   | 2   | 6   | 58f0e2a5 | 00:59:55 |
     | 6.6.6.2 | r2   | 1   | 2   | 6   | 542fdff7 | 00:59:55 |
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
     | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:20 |
     | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:20 |
     | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:02 |
     | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:20 |
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
     | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:20 |
     | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:20 |
     | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:04 |
     | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:20 |
     |______|_______________|________|___________|___________|__________|
    r2#
    r2#
    ```

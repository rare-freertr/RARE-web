# Example: lsrp ssh encryption

## **Topology diagram**

![topology](/img/rout-lsrp13.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz13r1-log.run
!
crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWtmbk1FZ3F1L0VJUmdiWmpKTzN5b0hSMXEwaHhuZlJqT3NaY1ZpY3hMYzRPOHlwcUhqYXJEQ1oxYkM5Z0QvcXphenN0Q0V3a1FzRjExNmRRS1BJM2FDd2FxZlZZekU5bTZEWlgvamJsTEJJemMzczJRVUpOd0ZiSFlIRXNjeW5xMlFJMXBCQk5CTmRMTURBbWRJeVNOUndlM3pOaEU1MjY5Zm9JOXpZclRHMURjQUF2TnVHN05TTEpRcjdLc0plTFloMW5SUkFiWUN2dkRvS0pCeDZuS2xOMTBRZ2Fwb2NxaUhoZzhQclNYd2NaRDltZk9IcGhKdk9LT3dGb2lMOGdncDg3Wk0zQ0FIRFRGVG5YOHRaTld6MXJWektoYkRONldieDd5SnJFV1Jka2M4T0RoSDVzRzh1MlBkVTZNWHE2S1ZTQkIyZ3VIYTRzOWFJM3JjT2JuUUlEQVFBQkFvSUJBQWJOL1N4T0lUQVRLRnZDazhhUjdRQjd6VXhwdVJvaTNVbE5HOXJNUXVlZXRtV3hjWGJ0RjNZZWlOUzlOSjRxRXBrS0RpUlg0RXpZVmRUeXNMTG43NXRFaXcybktUZUU4QWdkR0diNlNoNk96cVV3ZGl2K21qOUFERlU3a1ZYZysxaVlXTVhJR0w4RUJqWTkyRjBRZkhSTFZra1RUUkFzQng0V1JMcTVaTFZRUkNYWDVLTmtsU1p3M2JKZHdjVmROQVJGNk1Oekg3N29iaktBWFdwVmRHUWtNd3JDK2szaHN4bjRlMDZ1NHRpUU1Lc0tPRnprLzBLODFNc1MyMW4xYVJObXM3U0Z4VDdYaXVQUzlTZGpMTms2cUxLMStKdDQyNUxCeTFkbG5MSGoyV2xVbnQ1eWdoMkNLcWZ4OGZtWjdzV2ZKMmFQSDl5R1BTSFhKTkJsdUNVQ2dZRUE3OTVja1ZUbzZHWmJuYVJJT1FVR0V5S1FRTEgvNitFUU5ZZ1ZGN1NMNlBqUzBMSE5aZmtZS1U1Z1dXUlVOUTZqcDhxWmx4dHZpQXppWC81NkVCNy9vM2xEakhxZ0JYMlViWC9lMkhocFpUQzZiSlJKd1ZzY2d6a1V1MnF4dnpqWk03YTZUVDVsblVNNFJOdE92aGEyWlBPWENNbXVuMGJmRTJQOUFnQk1OTmNDZ1lFQW04cno4QkJMRVJFazJBM0tteUVOeXVxQTZjcWhUajlTOENxZlpJYmZtNTU1Rm9DdkFyUk4vWHZUWUZ4SW9qaHJZa0JtTlpzTEFLMGZpSm1TbjFJakhzZlk4M0VpeDBVSlZhR2FSRDhuUUhSTFhDb0IvTnNWMzBjV1d2VFZKd1dNeEVvN09OMm5kNXlqTHRjMFNWeU9LeTVmUjZteCt5SmlzZjAzdDBRc01Lc0NnWUVBM3RMaGl1QWx2RDNadllkdTBBa3FxM3ZnSlRrMVZCbXV4UXUxREdCYjEvL05WckRVN1hXSVRGYlNpamY1UVpCbjF1Y041cUZGNmt5TnZqN1hoVUpHbDhWK1NuRmZWYnBpdDVXaG5kVzlrcExCbXp2bGlBanJZN3NTMTBjMTl6MElDRkltbnJyb0NqNzNkbitEbG5IaTNjU3ErUzdoV0hTdHBZV3M4cjcwQytFQ2dZQUlib3lUVXA1dGR3c1NjblNqdnI4N1cwUE00MzJsZVlIb283WHF2KzM4UXpCMGlsUnVoZ211alhRY1JBSmVYVVZhbFBlek1RZ0FhbDVKaTE1SEp5L2xhNVdQWDNFdGJjd2FpVnVMRkF2d3pocUNDM2YrRW5GMW15aFhsZWF2YlBwNGFUZ1pWTTNLaUh6QWZUOUVOVEV3bnhyakN3a3ArV3QwREt0bVROZERid0tCZ0ZtZHRpNStsWmp5aGh1UjM5dFR2OU5UTWdkUXRVeC9xK1l6bDdScnl0WGhCZnNtei9GNlhNQkFKT1R6SEVGRHNOdWRld09QdThTVWtzaXBrMmFYayt5M0ZpQ1VZRHZ3bjBMZllCMmgwTUtPS3plVzQ1OGhKdFhOa0RtV3RveFowZjlDelorRTBnMlgycVcyVWZuSFBrNlN3Q1Ivc2VlNWd3UDB6WTdQS0hZdA==
!
crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0FRc2tjMWFsNFVMa1QrWTdXNjNzUysxL2V4aU9aL1JtVnlBN3h3UVRjeDVpQUxSYnhJdVJxa3BVdHNOL0Q5VEdCMGtXbUI1MGpQZlFvK3o0ZUlsai91MFVrUXZRazVUaUNxYVFSLzBBc1R5OXo4VXlWQVBxSVFHM3JZTjFuczVKOTFsM3R5YVRpcWpFTGUyRk96MldnTSt2bHh1SjBlUEZ5ZHhtQnFHZFVSaEFoVUF3QUJFejFWd0hUY0JuWjY0UlROYTA3cHFORWNDZ1lBQThVeDlVdURMRzVvVUgvb2FXRHVkYzM0aXg5aDYwNDh0L21TZ3FJbkVQYTBCSmVwWWllSU9TeXBxYUxyZVA4YWRkaTE1NjgwT3JKTW5lYm51a3pZUldhTmxtUGtUMFhhZW92Ui9PVVhoL1R0MThKTlhUSThPT2s0RXRieGZ2MXpUVTNUMWJQUGxnK1VpazdSUG4rMEtGUHhLam1pSkdneEpVbVpIWHF5R3FRS0JnQUR1dUdmRnRSZEVYd1ozR3R3amxVVU5NalFmLzVYSEdJRnZRUUY1WGhjbFpmbi9kWjRlVmlNL2puT3VtZ2hWSVc4NEFKZXB5ZWFRYUNlWVpMaHpJRlRkbU44dndUVzFOUmJ2WmRmUGNGeGFYSFlrem16czRiUU5hQk1nZ0dxbktQN2g1Tzg2c1U2WkhMZ2ZUTWtMNS9qWXFtUmZMMUJ3OUxPS3d0anhTd0lpQWhSazBROVdsaFhFUjc1czcxd3cvRkd1T1NnUUVnPT0=
!
crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIeDZaME9zeWg4M2psbjZndU5VUGVRNFlyVlp2QXpSVGRic04xdlJSWjdtZ0J3WUZLNEVFQUFxaFJBTkNBQVR0Njh6RWJ5NzZvOG9XTm1oSjl5QVhHVHM4a3F4cUNGb2x4OEFYZWFNYTZibVkvSVZEWFkra29PL1NWT0gwZHJRalB4Z21maE45YjRVd2VwL1BRbTFO
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVKMnlqaFRBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhOREkzV2hjTk16SXdOREk1TWpFeE5ESTNXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0FRc2tjMWFsNFVMa1QrWTdXNjNzUysxL2V4aU9aL1JtVnlBN3h3UVRjeDVpQUxSYnhJdVJxa3BVdHNOL0Q5VEdCMGtXbUI1MGpQZlFvK3o0ZUlsai91MFVrUXZRazVUaUNxYVFSLzBBc1R5OXo4VXlWQVBxSVFHM3JZTjFuczVKOTFsM3R5YVRpcWpFTGUyRk96MldnTSt2bHh1SjBlUEZ5ZHhtQnFHZFVSaEFoVUF3QUJFejFWd0hUY0JuWjY0UlROYTA3cHFORWNDZ1lBQThVeDlVdURMRzVvVUgvb2FXRHVkYzM0aXg5aDYwNDh0L21TZ3FJbkVQYTBCSmVwWWllSU9TeXBxYUxyZVA4YWRkaTE1NjgwT3JKTW5lYm51a3pZUldhTmxtUGtUMFhhZW92Ui9PVVhoL1R0MThKTlhUSThPT2s0RXRieGZ2MXpUVTNUMWJQUGxnK1VpazdSUG4rMEtGUHhLam1pSkdneEpVbVpIWHF5R3FRT0JoQUFDZ1lBQTdyaG54YlVYUkY4R2R4cmNJNVZGRFRJMEgvK1Z4eGlCYjBFQmVWNFhKV1g1LzNXZUhsWWpQNDV6cnBvSVZTRnZPQUNYcWNubWtHZ25tR1M0Y3lCVTNaamZMOEUxdFRVVzcyWFh6M0JjV2x4MkpNNXM3T0cwRFdnVElJQnFweWorNGVUdk9yRk9tUnk0SDB6SkMrZjQyS3BrWHk5UWNQU3ppc0xZOFVzQ0lqQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGSE1HQkUyWjBNMFc0QjZsL3ZaUDhSdk5lYjJpQWhScitEdnplQ0lOU1M5YkptcW9sdjhRVG5iVTNBPT0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlREQ0JzS0FEQWdFQ0FnUmp2REpKTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TlRBeU1qRXhOREkzV2hjTk16SXdOREk1TWpFeE5ESTNXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUdDY4ekVieTc2bzhvV05taEo5eUFYR1RzOGtxeHFDRm9seDhBWGVhTWE2Ym1ZL0lWRFhZK2tvTy9TVk9IMGRyUWpQeGdtZmhOOWI0VXdlcC9QUW0xTk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lnQUFEQ0Jnd0lnRW1DMmVsVlI1UHZrY0FTalFhS29NNW8wd09BMVNheVUwU3lpYUZMS0NtOENYd0hRQW1iRUJaY1AvSG5qeXlOc05NRTFoRU90NkowTkNPOE44K0w4YjZVTG1Dc3lNZm5aWEdTbmY3RFR6ZWVIQjh3VDRtM0x0VG5xM29xaFFLbEh4VVVBOE9hVmwyNnhNSWhVdlZHZlBIbk5Bc2JCcXVmOUdpY3NrSDNKYi9Gbw==
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVUTjFXV3pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBMU1ESXlNVEUwTWpkYUZ3MHpNakEwTWpreU1URTBNamRhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWtmbk1FZ3F1L0VJUmdiWmpKTzN5b0hSMXEwaHhuZlJqT3NaY1ZpY3hMYzRPOHlwcUhqYXJEQ1oxYkM5Z0QvcXphenN0Q0V3a1FzRjExNmRRS1BJM2FDd2FxZlZZekU5bTZEWlgvamJsTEJJemMzczJRVUpOd0ZiSFlIRXNjeW5xMlFJMXBCQk5CTmRMTURBbWRJeVNOUndlM3pOaEU1MjY5Zm9JOXpZclRHMURjQUF2TnVHN05TTEpRcjdLc0plTFloMW5SUkFiWUN2dkRvS0pCeDZuS2xOMTBRZ2Fwb2NxaUhoZzhQclNYd2NaRDltZk9IcGhKdk9LT3dGb2lMOGdncDg3Wk0zQ0FIRFRGVG5YOHRaTld6MXJWektoYkRONldieDd5SnJFV1Jka2M4T0RoSDVzRzh1MlBkVTZNWHE2S1ZTQkIyZ3VIYTRzOWFJM3JjT2JuUUlEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQm55V2pBL0hkYXhrOFQ1MW9iNHVsU3l2UmtidG1UamUvaGxqSXpVMElpYTNnMk5NYjhRSzkrUFNPcjZLbVZ2LzNiQWt1bnYvTk42dzhvRTlvTHZrOUN6QjkyaUdrYkxQVktBWGM3dEdqK2tmQUZXRTV5VTh5WFk5VkZEMmVCQW81cFZieXB3WVVUUGRoY2NZTGNldjlpZVR3alQ0SlhVL0JVb2F2bXUwaVVScXlMUjNJY05pNUZ4Y3NObXY5SWRZeW9kUGlBNzh2bVJRMUp6alJKNzN4MTNWbnhIcTliZmVwbnZ0ajBlbVI2emNJVXJibWl4amhzaUx0YWZMOFBmU0xTVWdXaTVIU2xCQ0ZVTHJxdHFNSG10TTllR3hMT3ExUk9MSkFjbURmQnEyR3o5OFIzTjQrbHNuNUllNzl3N2s5eHZNbWdUVmxXTDZPbmdQVE00dHdT
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
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
logging file debug ../binTmp/zzz13r2-log.run
!
crypto rsakey rsa import $v10$TUlJRW9nSUJBQUtDQVFCVU5FYnBkSkVqU1JadXc2Mmx6ZlJuZ1o2R2pIVEk2M1dPNG82K3cvelpZaytBRlNtR05qelk5anZqUStBSHpjNE1mcER4cWd2c0w4R0hZOHY5VzBrSU1NM2dCbmFwaXBKRWZ4QW1VMHlrUHFCMy9zemFVTERMTHhXdk9vODB3Mlh4R3JJdEUzeUZFSTZrSXNQa09Mejl2NG1hUS8renEzcDRjQVdLbmF0eHNjL1k2V0JtMTRYVnBNUFBEU3IzejkvM2Z6WmxWUUVFemhudDVBU3BlVXFHSi9PVzJWdWVuS3cva1ExTlVBdldWNGZYMmErZHpsdytvQkpXWTI3NXRiNzJlYXcwMjFsNlVCM0NaK2NjVXFKNjh3MVZEd05GaTJHREtvdjFkUjFaMkQrS1FZbm92dytJcVIrTVpRcXBWWG5NNW5BMmNUZTJKOVkyUXBrOVk5bVRBZ01CQUFFQ2dnRUFQUW5rT1lrUlNNWExhQ0dhdCsxUzlORW1MQnlXNzZxWGZpdEhGSXdYdHpFbnRnNGhHclFvYVpJZEdZSnpYTlRZUDRCajYzcTd4OHRhZTUxaEd0aFlXWUtmU24wRSthT0VvZmlGcVhLS3hTak14QTlGU2lCaDkvZTZ2Vm95d3ltOXRRZ0lEdHJvVWNFTjFYZUtEdDcrU09iV2hhZ3pMSGZxZ0hHYjRyNm1yL1JEZlBtNmRtbUdvak9oRTJaRXE5ZVdXZkZjNTU3Rlk3Wm5UMDkxOHZtUk01MFhad20wSVF1TXpHWUswZFIxVDF2Y3Y2czJJeVlmYWxtMjl5YlVmS1M0T3FMOEc0YzVUVnlzS2paM2ZzcEExUCtleHZYOEhsWmh0VFpESmlEKy9RNlQrWjRMdE9vanV1bjdQUU5qRThaNXV0Qi84SHZHSjhZdzZPT1FsWW53R1FLQmdRQ1RpT1lYMkE1TkhBUEpUZDVEa1J5WXZXY1NteUpYY2I3bHFKNUwyckFubU9mYlhnWFlySUk3ckR1b3ppMDhHZWJaL01oaThRYjBkTCtYS0owUnNXRVo0WGZGNGpiWDRwdEJVVmt6M2dUaTVkTDdzRnp3bjdDaHV1L0RXejhUUS81UDRReEE0ckN6Ri9hWk5RQktwbFFtU1pPbmtuay9Bb1l0SE9mOTBHdlVYUUtCZ1FDU0hCMEFVUDBiNHVqN0J2U1EwTFhkSHZnZS85Z05QRWY5Ym5tMTRuNmtjclhRekxxT1BlTFJrbkNkY0lKMXMvaytiUDVFaXAwQkZxejJ0RWhsS2VPTnBuRDd1ckk3YXdZUXp6Yy9CTm5ZWldKdjVpUnoyTjNONWJTelZpZ2I2U3UwTGY3eHJjTnU5SmVjNWY4SEJ6emFMSzEwZXU0VWJ5djlXY0hDbEVtR3J3S0JnUUNMNUYwNDhyYnN5c21VVVcrVlpiMVYzeElqQkZLVjA5Y004TXZZWlM1dS9YK3I5QVZiSklnQWlSbXd3SDhINUErUFZ5K3pFWlJrcTJjWHIzenZ6OStncUxmblBNNS8rZkQ1Q0dlcTFMU1JhUmFiYk9sVGlEZjF3c21oMVoyRGFROTFNcEZwM1FscmFDZDlzbEhxZHJpSDdYQkNqcExFK21HNzJSTHBDbjJVU1FLQmdGbnZYQnFadjNLdTFXSFBBak14aFFBNjA5ZWcrOGdKMXZZMFRrNmF3QUZSYW9DL3hBVlNLbzk5YUR4QXlNelNueFRCMmpFdWNUMytTekQvLzUvbGpOL2dGNk9iWTZJWFdvQjJURGRLTVIxMktvVmVVQW5PNzVpUlVBMGpkMFRXM2NQbW5Bci9QbERKMVprS0tWU1dLK3JQbldVWlZmcldBMm5MR2UwL2daS1pBb0dBTytSY2pjb2RhL1F0dXV3VGw2Z0tZZ3VvZkcvaVQybExYNWh1V0wwTEliR1plWmlUOGJSTkZLR2RvRC9SZFpYUzNvREJ5QlEzM3RQL3RTNjM4MFN6cFhtQUI1NWdPQVdUcW5zK0FjWEZUVE9zL09BV00zVVU3d1hlRy85eE5OMmJibjBieUd5MnhtOU94T2Z4NjVwN1VXQkZUNzZGRlhKdkJZUmo5WEZiQjRBPQ==
!
crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0hwOW9rU3FrRllpTW54aWtkNGdlZEphNzErN2MreGlISEhERVRRS0hoRGpyc3g5ZWZMK0hGYmZSVWhtb0c5a1RmZDNrNnpmNlpuWFh6V3ZLMGpIUlVCbmV2bFpVQlNrZ1JsSFBmVmdXeStFUERlWXdRUFBWaDUzeG5KRktURjVOSnZQcmNzS1BUdjBvdEFKenM2djk4MjdLZnFTUFNXMFp5TnkrNGw1WjJibEFoVUFqQ0dNeWNIYjJObGZ5ZTNEYnZCU3oyOXVxbVVDZ1lCczYwMHAzQ2xBaHMxWW55emdJR2RVNmk0blNuQ09XWWpTcFlQZEVCMVpJQ1Z4SGRKTTlSbUtBdWtCeStwTUh5bFR0VmR2VFhKeW5wcjhsb3NmdVByQnluQ3pYMGFiYWF0ZCt4ZVkwRlJ4SDdEc09SNFpDOFZxMEJic2tndnI3cHIvWS90YXFqL0JtUzVmSVpETzNSMjNIMERsVnBiSUxidXN3TEdUL3Fsb3V3S0JnR2I2WGZzdVdDRzlRNXNLcCtSRWVJVVo5WU90Tkh6d3ltbmRUMzdwRitaSndTQWFES01SaFkwQ0hNYWY2cXhaVHpRWEgvMjB1eHplWGFOVGpaRWtHVkVnR091czlLYzU0UlQ0eGFwWGJleHZ2by8wU0NVUFJOKzZkd0pTOUJySDVRQlNIbUh3NjRzYWRNa250MHA0MXAvYzhDMWFoN1JMUEpsY2tHb0R6TUE5QWhSUzlVOGZrTEJnOGVKM3ZySDhuc0xnYzU5M2lRPT0=
!
crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQURKQ0NJZmNuWHp0TW5qbFUyS2Q5ZDNIczVZUFFUL3hRcGRNV0RQTVNwUW9BY0dCU3VCQkFBS29VUURRZ0FFOW1Mdi8vVkwzK1pSTEJnYzFkNXFVdytCeEFmcTA0YllMNDdRMWhSYWlBUGFiOXpBa0Uza3d5SmJ4cGFrNGNkUGdrWVZxZ3poVHRTaXc1TlNFUWk0VkE9PQ==
!
crypto certificate dsa import dsa dsa $v10$TUlJQ1VqQ0NBZytnQXdJQkFnSUVaNGNWTmpBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhORE14V2hjTk16SXdOREk1TWpFeE5ETXhXakFOTVFzd0NRWURWUVFERXdKeU1qQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0hwOW9rU3FrRllpTW54aWtkNGdlZEphNzErN2MreGlISEhERVRRS0hoRGpyc3g5ZWZMK0hGYmZSVWhtb0c5a1RmZDNrNnpmNlpuWFh6V3ZLMGpIUlVCbmV2bFpVQlNrZ1JsSFBmVmdXeStFUERlWXdRUFBWaDUzeG5KRktURjVOSnZQcmNzS1BUdjBvdEFKenM2djk4MjdLZnFTUFNXMFp5TnkrNGw1WjJibEFoVUFqQ0dNeWNIYjJObGZ5ZTNEYnZCU3oyOXVxbVVDZ1lCczYwMHAzQ2xBaHMxWW55emdJR2RVNmk0blNuQ09XWWpTcFlQZEVCMVpJQ1Z4SGRKTTlSbUtBdWtCeStwTUh5bFR0VmR2VFhKeW5wcjhsb3NmdVByQnluQ3pYMGFiYWF0ZCt4ZVkwRlJ4SDdEc09SNFpDOFZxMEJic2tndnI3cHIvWS90YXFqL0JtUzVmSVpETzNSMjNIMERsVnBiSUxidXN3TEdUL3Fsb3V3T0JoQUFDZ1lCbStsMzdMbGdodlVPYkNxZmtSSGlGR2ZXRHJUUjg4TXBwM1U5KzZSZm1TY0VnR2d5akVZV05BaHpHbitxc1dVODBGeC85dExzYzNsMmpVNDJSSkJsUklCanJyUFNuT2VFVStNV3FWMjNzYjc2UDlFZ2xEMFRmdW5jQ1V2UWF4K1VBVWg1aDhPdUxHblRKSjdkS2VOYWYzUEF0V29lMFN6eVpYSkJxQTh6QVBUQUxCZ2NxaGtqT09BUURCUUFETUFBQU1Dd0NGQVh3bFhUT0tteWFhNm5MY1FEMm1QVU92Q05BQWhSRURaVFh3ZWZlUkNMOEFqOEsycHE4WXp1cHV3PT0=
!
crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUWE3SC85TUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pJd0hoY05Nakl3TlRBeU1qRXhORE14V2hjTk16SXdOREk1TWpFeE5ETXhXakFOTVFzd0NRWURWUVFERXdKeU1qQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFUMll1Ly85VXZmNWxFc0dCelYzbXBURDRIRUIrclRodGd2anREV0ZGcUlBOXB2M01DUVRlVERJbHZHbHFUaHgwK0NSaFdxRE9GTzFLTERrMUlSQ0xoVU1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQUtrck1vSFhQRmg3L3MvMDE3ZFA3QlR6T2NMVm5GZm9CVUpBWE9SNmVSQ0hBbDliSjB3cU5sTlo1VWJCWUd1bWNlMXN4NXNoYmFONEdvMkJZNVZqTFA0UjJqem0rdXhNWUlQSnBQeVVTdTAvVXlseFpkSVFhMVNNNHpLOEZlVEo0RXBiak1pZ0lFTnVQYkQ1alc0N05sUlRwQ0pZRUg0Mk9rOUZ5VE9ETUJKNWRBPT0=
!
crypto certificate rsa import rsa rsa $v10$TUlJQ2xUQ0NBWDJnQXdJQkFnSUVCc1RGQ2pBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1qQWVGdzB5TWpBMU1ESXlNVEUwTXpGYUZ3MHpNakEwTWpreU1URTBNekZhTUEweEN6QUpCZ05WQkFNVEFuSXlNSUlCSVRBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE0QU1JSUJDUUtDQVFCVU5FYnBkSkVqU1JadXc2Mmx6ZlJuZ1o2R2pIVEk2M1dPNG82K3cvelpZaytBRlNtR05qelk5anZqUStBSHpjNE1mcER4cWd2c0w4R0hZOHY5VzBrSU1NM2dCbmFwaXBKRWZ4QW1VMHlrUHFCMy9zemFVTERMTHhXdk9vODB3Mlh4R3JJdEUzeUZFSTZrSXNQa09Mejl2NG1hUS8renEzcDRjQVdLbmF0eHNjL1k2V0JtMTRYVnBNUFBEU3IzejkvM2Z6WmxWUUVFemhudDVBU3BlVXFHSi9PVzJWdWVuS3cva1ExTlVBdldWNGZYMmErZHpsdytvQkpXWTI3NXRiNzJlYXcwMjFsNlVCM0NaK2NjVXFKNjh3MVZEd05GaTJHREtvdjFkUjFaMkQrS1FZbm92dytJcVIrTVpRcXBWWG5NNW5BMmNUZTJKOVkyUXBrOVk5bVRBZ01CQUFFd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFESVNTdGhrSHFhb0Q0SkhHUGhFN1NzMmlBSTNqTEhsZGhtZENIWEVwOTdXNG1UdVh1L09FTjZJYi8xbUZNSms3dUFOS3VFaHQwYkVudnM3WVZ4UWxSMm9SUWpPQitsMksxeDlPVmxoY0xkZVJSTmRhN2JpcTQzVlFVZmJIQjBNc3JWbmFnOFhUd3VPcVZVVmtkTkFlbGtKL25WMXVkRno5WExyb3pGS3NyTEV6YzBCak1Wa3NwYmJnTkRLUm5SOUtzamd1NzlPSUUvclBlZG1JYlA4aUE2M24xVE5uVmlVQnAyeXZRME51bkJqOXJ6T2hNNUorajdSTlNWU3UrVk4yUmUyaFBlQmIxUE96R3htcnUwQnVKL0xZZS9uVGlyU1p2eGtiUnlpaWNqRllNQ3Z3cmNTQ1ZET21QM2FXa1Fnck0yb2gxMGJoZTJYSmtqdkdQaUtuNGc9
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
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.255
 ipv6 address 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
 | ethernet1 | 4.4.4.1 | r1   | ethernet1 | 1.1.1.1 | true  | 00:00:08 |
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
 | ethernet1 | 6.6.6.1 | r1   | ethernet1 | 1234:1::1 | true  | 00:00:08 |
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
 | 4.4.4.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:57 |
 | 4.4.4.2 | r2   | 1   | 2   | 5   | 542fdff7 | 00:59:57 |
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
 | 6.6.6.1 | r1   | 1   | 2   | 7   | 58f0e2a5 | 00:59:58 |
 | 6.6.6.2 | r2   | 1   | 2   | 6   | f141cf47 | 00:59:58 |
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
 | C    | 1.1.1.0/30 | 0/0    | ethernet1 | null    | 00:00:10 |
 | LOC  | 1.1.1.2/32 | 0/1    | ethernet1 | null    | 00:00:10 |
 | L EX | 2.2.2.1/32 | 70/10  | ethernet1 | 1.1.1.1 | 00:00:03 |
 | C    | 2.2.2.2/32 | 0/0    | loopback1 | null    | 00:00:10 |
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
 | C    | 1234:1::/32   | 0/0    | ethernet1 | null      | 00:00:10 |
 | LOC  | 1234:1::2/128 | 0/1    | ethernet1 | null      | 00:00:10 |
 | L EX | 4321::1/128   | 70/10  | ethernet1 | 1234:1::1 | 00:00:01 |
 | C    | 4321::2/128   | 0/0    | loopback1 | null      | 00:00:10 |
 |______|_______________|________|___________|___________|__________|
r2#
r2#
```

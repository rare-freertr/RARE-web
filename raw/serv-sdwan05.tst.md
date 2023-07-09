# Example: sdwan with mixed addresses
    
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
    logging file debug ../binTmp/zzz39r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQTd5Qnc4TXc1ajJnWUJWa2dkYzhGTEJkMnpVaVcxRzRPM1Qyd2lqMFRiQXdoeHRxc21YRTlGTThmRUpTT0EzREppY0xCV1dwQ3BMUE1LODZXcTQramdwZ2Vka2pEeXpwN3RycDk2WUMreWZnc3F3cS9pbWpJRkFBY0J2WXo0RENlZlRzU1B0WFBMZGlhckNtdWJOSlZXbFdYK0RHb0JxNXpwa1VoMHhHNXZHamQxalB5dDlIekpIanZjdm5IUDcydjcvbE9pRWZXdS9ONVhWU2xCdDVLZlZUQ1Y4VmdnbEhiRFFSaGJxcW4wbEVXK1Yyd0w4RWxMRTRlenZldG1IZnF1b09XNU9SdnBCMVVBdFpicVJjYTZoKzQyQndHbGJoTVFWdHdyVUg0dlMrU2hHUTRQUGNIZnR3d21IZGNMSVhFQmt4cW1oWUg2UDUzYmRwaGtUOE5qd0lEQVFBQkFvSUJBUUNCcFlrV1JPT0FTT09kSXJGaXJoY1R6TFR3bjhhRzdoVEpCc1ZNYmNpMTcrM3dMbWNkMmpOUHNPd2F4VEFwMVdDdmZCUHdNcGhuUzhRS2pEdE1VTmhKMmNmS1FiRkY0ak5vNHJ1WmVkLzNDTUxQQ1VqSDlmOWtPSnI1ZTBxczVpOUhubHRLRGdvQnhVbzJ4WEo0TmFGcEZMY01MWC8zLzJWY1pHYnVWTkhxdjdQMmppbVVvdVh4SmxNWDFJeHJFVTRHcTNtcHlGdjdBNWNSNklUUlg0MU9KbjFUYmJBcHFDTE1BRlBvR0g2THZsdG1FTmdhNjZBRDhRZUNsaWV5bDF4OUx6a05ZZ0ZnZFdBYWxkcGhyQ0J5NHJZajU3aUtnNzlvdlI4NitzTURuWHd6WmpOT3dQWHQ5NlBKcjlxSFBCQTRkeEJaclhldThjMkNnWVMwZ3N4QkFvR0JBUC9Gd0NsckE0R083aDhJQWVIdW9scXkwdFZZUDA2dzdPc1ByaUpJazdxVVNOMGRyciszdnQxS1Y4YzVDUVlFeGxtdGdNMURqNTc3RDBxK09xT3JPaVBsV094cUtHTWtqNnhpK3piYkg5U1dkQndsWXl0ZzVsWExVQllHTjVmWGNuOFIrR1Q2MGVINFNyQkNYTE5qUmRrT1ozalVDSm1mUFllc0l2Q3ZrQ2NKQW9HQkFPOVc1ay82OU8xcllNUHNkSUg2N041am5PcmVzUGRnTUdvOVprRFphRWkrWlV2SHZjZ2lVMy9ncm1QTHhxVkNiUG02R0JnUkZYWkpqNnQ5cWFDSHFTbkxJOE1XS2FnaDVuaWU2M0xLM1R4Y3orTlFtOFpMMzVTUEpGY3FKeTdvY2FoZ3JoNVRRditNd005REpNMVYxdUJOTE5lWnZwSnNuVEtXQVVmNUFGM1hBb0dBSENSN0YxT1NDREJjM1FjNWhjMkhDYW5CYnY0TndTL1FjYkRBL1Q2MUdvTjBYUGdHSVV3cmNSZmIvcXkwNUhla0Izd0N2eE1lKzJRdWM0L296ZGRxUjBiVitQVlpTa2RjazZBMGVmMjBTK1RlRTdhOWFhbDR6cG5YVHdVU0d0LzIxaXA1QlV0ZnlwaFNSNENWeUpzMHRVUlRlRVVFU1RydlB6MWVmdE1pYmxrQ2dZQnJucnF2U2h3cVNmZFlBaElkaEZSUVo2QmVxRVlRNWlxL0N0N1kyQ21oVkNPK1lKR0ExWmFRVU5wNXUxNldYdmtiamNkWnd3elFoS0Zhcm9YQXpsK05rRytEUUlyNHRFMnEvV0xIMmxxQzB3VVRwT0oyMXhVdyt2Q1BWVUFMUXJBZzAyQlgrSDZPNUo2cVUvblBid0xSRjBMTHE3RmFyQVkvZ2Q0UG0vTERQd0tCZ0hxNjRKN2daZTRRM2dpVjg0QjVDWXlUbmJHbGZvOFA1UGd2YlR2cUx0VTZYeWtaOU9oZEtCb0RUWlo4UnZWMGx4Ympmd0hYM3ZuZDVZb0I4LzBqUGhiY1BlUjVKSHA2U3NGdkdVQ0c2WnVlbU1uMDFzd2NvV1JZSm5UUjVsQktvcDR3ajdiMThyRzVoWlBZdHFxdHR4SkVYU29la2E1RmUvOElweC85Z21wZg==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ZBWnM3L2wwMFhOK0YzQ3pReDlCdGFYWlFhck80SlBjWlRVaWxnNVRLMjdGS1BoTTI1TXFtbk13dXdwTm9ob0tsV0JNOXBKSktDcXlrNVZVdFpGeFdHMW1NMW0zbjFsOFh2VkRJZmdUeE5IYjlkL01JMHhzbjhZM1ZQSHQ0bFh0bXRKaDBHOXd5VDQ2SlNiUXBTeXd5NTNKaUllNGpXOHMzcHcycTdsTGR6WkFoVUF6aS9JbjJGWmI1eFZJejk5aVM3aFkvdStPTEVDZ1lBb3ErMVJHN1U5VkppM1NZUVhGcDF0a1hUMXI5dElhQWRpY3pUQkRXZEtVdEk5U1d5UGV2WlNIa3lDY254WGhpdkExR3VSejExeHV3bkZjQXFWZlNZUzM1MFRhWi9TYmEvWHU4ejcxYzhBZG1WWkZFa1pPRzZxWVRFclg2cXB1R3RkUE96VURIZWl5bzZXM1A2QmsxYi9jYWRPMkhjZlF1b050RWRmdmxjVFhRS0JnQSsvUTIvMEV3NDE2Z2tIejBqaTQ0UjJsK09XYkVlMFF0UE5sSnA2d1dubEVndnVQRmRwc240ei9sOXFqblBPcUNuZUVtMys4QXZRcVVVS29tWkNIRjcxK2l0ZEZoWFBaekdIdSs2NUJ5dHg1VWhXSUFzNGtKLzhtSGlqdkVianpTUGpIT0NJaUpMcUZENm8zOEI3S0xEcXZvb3c5czFLT1MxTFZoaTlkUWZTQWhSdnVnQnZ4WExwVHlXSzVGUjZOaDRJR1ZBL3R3PT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNOeWY3RG92V1B1Qi9ITkJBS2cyYnhEQzJ1b04va1h6Zlc3WmEwa2xSeG9BY0dCU3VCQkFBS29VUURRZ0FFQVE3VXA3STZIUkI2NUtUVzVTc250Z0l5T09sT2RzTVhHb3M1VzNGM2c2L1hOUVpxM1lsVFhVcmkvUVhiSXdpR2piUW03eXBObFdUKzdXZzdLYzdEY1E9PQ==
    !
    aaa userlist usr
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
    logging file debug ../binTmp/zzz39r2-log.run
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
    logging file debug ../binTmp/zzz39r3-log.run
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
    logging file debug ../binTmp/zzz39r4-log.run
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

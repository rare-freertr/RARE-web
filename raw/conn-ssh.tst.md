# Example: ppp over ssh
    
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
    logging file debug ../binTmp/zzz62r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQXRyYmp1Q1owRzlKTmZkSnlsUW5BTERyYjF1dUQ0NDIvV29VdWxyS2daaXNhMm1WUEdBeCs1UHEzQ1U2M1hGbFIvM0hNUmszUlFzVVQ5R25IeXFNd05zRzBSdUlXM0JBa05NdXQ2dVRPZ0J1UFJkRVhxZk56VnE4M1JPaUFscHN4eENUVjlXU0RkKytoaWJabVZuc3N6bWJsQkpLL1BHY1laOXltVGl4bExndVJOOWVscmk5Sk5ZQWYrUVRhWlVadnZ1Ung0YmVwU1ZnMEk5SVFqaUVlcUZWRVdtSlBzOC9oSDRad0ZOTWZhcXRnaEhPdUpYd2tSM0lHRGFIYmo3MTliZ0QvbU1DbDJjZkZqQzBRWlg3cHJCVWJ2dndhSzhCSWFlcXhRTkIvVDVBWEw3dTZ2V216WmZxcmF5aDUrUDJhWlBLN0xzazV4c3U5Q3JuUm1OZkppUUlEQVFBQkFvSUJBRSsvSzB6b202eTQ4VkdGVkxWditBeFY5RFd0dlhiSUcwaXE4RmFkeUJ4UG0vek9VdU13TVFKSDJ6T1l3N2J1MVRja3QvL0hYeHBCWWlBL094QmFnV1NrenNaUlQ2RGsrcWlBYlh3a09XejRtbVBpaXUyR2NFVFpYTW9hb0dVYmYzRVlrcm4wRU4xOEhZazVyeGozMGVxVVJramtzOHJ0UkYyd2xIVnlNd2NSRDE2Z1EvY0t5SUNqZGlHOFBOb2lkSWpNNkNCSXpMS2Z2SVVLRHFZOHlMMzZRL3N6a2NOblRZd1JNUlVmbDFiZUlmOUd1Nk53RmpNZXJ1WXYrdTVxN25jSDI4WFlvSmVsVWNCL1MrNEpkUVk4SFFVbGxSWGZaQkxEaFJGNnI3K2ZEUzRUbnloa2UrR1lONUUweDJ0eWpKdS9JSGFYUlFvZGlhRklHRlluczhFQ2dZRUE4bkFBbjRiUWpXOWsxczRSakM1MStHTWVMc2dMamd5dkdTd1h3cTRTajdTZkJOMkk3VWtoSHJjZm10WUxvT25xVkNMUFVpUS9Gc0lSb3NLOTRrSklnNFQ5eHVHS3dydzJpVHNQRW9POGtoWUgxTk9qaXJtWE1ySk92SXdqMjJMZzFsaEJOUlpJcWlJM1lmMEI4Rm9WaFlXQmI3YmU2YTZIK280SDVtVkU0RDBDZ1lFQXdPK1VqcnZnVktROXFmNXVTZE5NZkk1WWg0QjZzZGxyM0UvcDlLazNzMmdhbklSRGZBN2lUVDRpVnI3NFd4eUEwUjhEWVZIS0ErOFZhQUtmT3JqV2ZEek1OWHA5MGx2cGsxUVVRQ0pkUU8yU0dVT2FlNEs3TXgvM3JNYTRLQnc4bE5FSER3T2pLZTVHQTl3V05TSHpKSnFhWS9DUG1kMVE3NlB6aGpFYWR6MENnWUVBcmdCZklpQURmUStQUTNDaFBZaDNHVEFpa0piNVhCbVVicStyMmdsUHZ4NTI1Mm9OQmFsd0FQaVQwWENBNWh3ZEdBZm4zdCt1L0NtTHVOS21zRWE4ZnRDcng5dEcyVjkya09YM2VtVmNxVWp3ay9yV0xSSHBCL1RiK0ExcEN1T2IxWnVBS1piMXprNUNpNnlvZ0paWFRmNjFHTFlhcFlPaml0djNwWS9YY0UwQ2dZQWRTZ0dXYllVUHRHTThGRWp2NGlqaFc4YXF3MkZjOEhIRVgwbFgvL3hadXZzWE9hajVBMVZ0Zm5vK0N2MnU3elBMQzFjN0JleVNEbENFbXFsTGc5WGp4R01IMTFHVWhxbDkyU3k5MDdtdWFxSmNQWHdOTmZwdk4zSWxBNEhmYlBIeGNZNE54SEtYb2ZsMUNvdEFnNmZpcmFtMGRFZUloeVdMUzZ0amVyN1d6UUtCZ0JTeHA5MVRicGFaUEg3c05wRmVabDFLMFFrdEVHOFNScm93TkN3dDZ1WFN6YnV1YWN2YUE3R3RoV1E3dHhsc0FtMlkrVjg1Z1Y0OHk5VlQ0ckVFd09ocXljRWhwaUVNYWJHUnY3eHZuNHJBUk1sY20wK0dIRFNoR1dqZzEraFJRYmlSUkt1Z1lVcTJMUnBtVnVjckhxMHcwOWNtN3dDOVNOWENaNmZaRWNZUg==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0ZFT3dMaWZFNi9mM2pwdmFwUVZ0LzNHVllpREpWa0V5eHFxa3EyN0JreVMyM21DWXdWVTZndHFjTEdkM3p2OSs2VnZpR1YxQWFhN1FvRXJzS3dWWlZWUEwwYndua29BdUt6YWNQL0JYVnljdEVWWG1Ud3JMbDN0UGVvanNRUjRQc2w2TnNlLzcxT24vaENObXlpTitYbGNJZjRiSHpuRmsxZVdhbDJkOENMTkFoVUE1SmpobDh6SkVOTTlVRzJCRjNoU2s4QmxwNGNDZ1lBTGR3cHBySlpQUllkSHNteS9LYWw3ZFFNYWxBbHBIT1BHQW5BbXl0aDlubk8rQTRJMk9kT1k3OEVjaXU5TllHYjlTc21ROVFJRk9tNWc0a2doZC8yalhqTFJTWGtzcHpKSWFhYVdSUUZoUW5HUm9ka2Z0V3BuUlhTQ0J1UnVkQWt4MG5FdWNjSzRnN0xWSnJReTR6VXlvanlzcVJLUG5WSnkvbWkyUElWSFVBS0JnRWVEbjA2Q1gxNklEbGh1akpiUzJhRjFyUHJjYjVYcE5JZno1R1gvMVExSkhLVit6YkhSVURqTzYxVDdTb0hFdStLbjdCREVPbWh2ZlVCOW9yejdvQmlCUmliTVpyeUJzS2FIek85MEJIRWxUSFZtRWpXSFcvSUVCeTFZeWhUUDIxNnJnM1UxZHkyQWJEcTZTeXhyU0tpamRJZHcybml2NHdpV3Q1cUNhRVNXQWhRTHVsSUxUamZHKzhhTkdKM29ScGdOWU94VklBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUQwRkZHaGhpTk9RdzZVbWtaT3ZLdFpvd1phbHRlc1A2UXJYMlZiQWRlcW9BY0dCU3VCQkFBS29VUURRZ0FFS1RzZFA2ZHlvYjVSZW5sNjZCS0UrcTU2Q0JZTk9vak5IeGM5L2JESTVUQnloZUo5aFM2ZEZkUWdMZi9ITy9ubE5CejI5dDJlWUVscVBGbnNucWpBZmc9PQ==
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
    logging file debug ../binTmp/zzz62r2-log.run
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
    
=== "Verification"
    
    ```
    r2#
    r2#
    r2#show inter dia1 full
    r2#show inter dia1 full
    dialer1 is up (since 00:00:01, 3 changes)
     description:
     type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
     ip4 address=2.2.2.202/25, netmask=255.255.255.128, ifcid=634917650
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) promisc=false macsec=false sgt=false
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

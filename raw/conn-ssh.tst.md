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
    logging file debug ../binTmp/zzz2r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWpRT0xWZlBYbnUrbStaUGRoVzRIckdVdlNRSWNFQ3MrVE50U2dmbWNEN3BJV2poRGFsVEtic24vVkNDNlZLWDR2YmZ4cHU0WktlL2g2Z256QzhXc1ZMTFdZL2QrdjRJMU1sKzkxNkR4Z3g5QzlIcG9TYkYxNUREbHVWKzFGdjlMQWRoR2FjQ0pHMFJEb09OeTB4VjlTMlp5dWVpUDI3RzNRYVorWEE3VjROSXJQVmdFeHZyVlp2L2Zld01xWTZHZi9mS3l6bXYwbGNKWjJuZGVQU3lVMXROK3JrSHlpRkdGekd0OHd2TEo3amQ0bHovZEVZTGlURUVrcEJwMXRDa1dWem1pcGhuQjVCRm92NTZ0NmthQUxsZmFjeHBONGpWdGpaaXFHTkNNTWNPTjhkWFcrK1V1YzV4OEpJV0hnSVpJN00vMkdkSWFENEhmUWtiTVhpUGltUUlEQVFBQkFvSUJBQ3NUQVJYeFZWVU1XWkgxTS82VkhLenhmNThxa00zemw2VThmWmlNV2JxSUtaKzlmZ0pXQWp3VFlmWWR4UzBrUWJZYUlTdmZvVG9wTjNZWk1lL1BveE9BU1hMaDRBcTV5R3dweU1DOFBlblN1ODRZTWhFSXJ6MVVIbWdncngxbVFGQkE4MGxNY2RVdFpnY1lVelBkWlplSnBOUGJFVTZIbTdYbkdNUWdGLzhEWHlSQXprQlZDcmYyMVRIaUswZHo2eHhPeldwczJkdU1wRENlYmM2KzBWVVlXK2VYK2ZpbGVSQ3U1ejBUTkN6VzNCVTRQWDhUaGFUdis3V25ucWtQdVplbVgrV1BmaG9LUzFtZ1FnVXRCWVk1TFhMTlRFd0g2OXl3cTdzRG5EMXJzTUtoRWVleWNZaERTUVNxSkhURjMyaFdiTHA3bktFUXhFMStjWkRLU1RFQ2dZRUExZHZJTVY4b042WGl2KzMvSHBCSklzSmo0UFRMK2puemhDOEExT3kyYVdGMlJuM3VrQ1hXemtGZ1Z5T0xKc3RNTlNOeE5GZThaMzJDQi9PeVNSN29Edm40aHJiNk01bFJCL3pLa1JsenhPUUYzRlJHLytDem14cXNiOWEzbTJJVk9Ya3FobUphbTVnSFEzOC9FTnM2b3FqNkUraVd4Tld2eWpGRHNPRXNFWVVDZ1lFQXFNMFI2UUNpUUg0U29wcTRRQ0g1d3lxZ3ZUSGUxdVNPQ3J4c3NuTmFCYy9uOUhPK3FzdFl5Mk5Nbnl2bU9KTWVnV0lITEJkYlNHRVZLb0V0VzluYkhUQTNSL05nYTQycVRSZ25kSnlQQmhWVXpDSUoxTEkwOUtZS3NoV2FxRXA3elllbFhKWEFhNTJXK0RpVzJLcG9ESW9lb2YrY1RVQVlLdlMzUXdtNXp3VUNnWUFibVpQS20yZExWME5lVmM3WkdQSDNaSE1UYzBSbjlOYXl0b1k2OUpuT0c5L3gxUXJXMjZ0UFR5eXAwbEtCSFRlbW0vNWVMUHlKdHE3emE4WVVuY0tCUEUyUXhVaWhKQ1pMQzVyeEF3SG41UzNFYzdQK0RmZmdDcDg2aDlHR1lqQXZESzRxVGNNMzFYVUtoditTbzFoNzZhYnNydFhXYldXVWlLc2R4dEd6S1FLQmdINjBWNUpIT0lNaVh3aVJER2FQV2pRR0JsdWRXSUNEVko5NGFqclUzU2pwczFuSm04QUdIU09sNkxpOXNmU2JjZFY2YUpuTyttVHRBbjlDTVhMMXAwUlVrZG8vTkF2bmJZS3E4OHJUVFlRcWROazVYNW01SG9qWkxjUVk5VnNIZGNDRDVqc0Y2VWFlSnRreFdRRlBnQVNSbEliVElGYllHb3Y3M3FmQ1lDZWxBb0dCQU1SS09SUVpkMVZXeDVwbUFqTWx2ME5zbEVOWGwxYmlnL0RmRythYnM0TWJNWkowazZNVjlyb3hUVzNUQlo0ZXN5dUpwbXR3TVlVeTdKY1dQTHpJK0lYTlo0NW8xeTF2amt6cEFIbHM4dFBPZFlVNjNteDd6YjdrTE4zaEJRTCtXZU5HOFI1Wlo1QkM1NGduME5GYVk3akRxRmkxT0hNQzNJZTY3S1BDUHZWYQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0FvTTFEQXdvMXQ0OGQ0UkN2MWNnQVBZczhmdXZPcG1aMzB6ZkFQaElyNlVJUGxEQlIvVVlGRHo5M0tEMXBCSm9na1lXUE51Zmo2NW1aRW9rQVppaU1MaGV0bmVwS20vb3Z2RkZ2ckxZZ2dvbGZCS3R5S2dTTHJtdGZidkZ2NlNoUVRIa2M5RzJDOFRsbk9UVUFVK21hK1pMN1dUUlMwaTZocW81bTk1bjJKL0FoVUE0b0UwczJiaTFLOFdJMWFkZ1hrYm4yM1ZGYXNDZ1lBRi95R09qREJFVG1kZ0h4T1BTa0JJMk5PTFpid3VDVFM5a1hRZ2l6SkZsY1RwS3kvNmp6TFhFenc3YkVsQ3p6QzZyMWVtQUpnMWx6NmdodEdLNG1aajNoWHNDWW9INk1tYjhjTCs4NWV1eTQ3QW5kQjBLd3ZFMDZsbUxOaTN2Vk9xaDloT1RlcVY1VlRQOWNEZlhTSWVLZkc0aEdhZzd4aHVpdnpBcDZLQXl3S0JnQUhuYzJYMWprYkJxL2pCYzg2c0pEZUlpMndUN0x3bnRyN290VVpKYnVMTkkrUFI0QzhHcXV3cFdiS3kyTU4yeW95cldNNG0vSTRIWUFVQ0o1bzBZQ2c2NXRtR0locWh0dG5qaCt5cll5WVhCRStXRWJ1Tnc2VVBwUTZVVUZYQVdFYVhIZmkyVGFkL2FUTWNoQlpES1R2R0ZhTjI2OVNlSVRuSmlYMlk3dmtUQWhVQTZZUjhKanlDRHV6MDFNMGo3T1pmYjJ1RFdvVT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMXQ0M3p6UUVzaE10aTllMVdLcWxvSmRxV250MXloMmxIT2VRdkxMS2dXZ0J3WUZLNEVFQUFxaFJBTkNBQVMwQWJqOXkzM2ZIaVRycUUyS1BwNk5qdkpkMi8zWUlFcHRkblZPRG1vVVBBN09RMmdmV0FNamxmajg0YTlNdDA1bXp5cDFaek9mUDJ2aTNLWXhyWmJH
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
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface dialer1
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
    logging file debug ../binTmp/zzz2r2-log.run
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
    dialer1 is up
     description:
     state changed 3 times, last at 2022-05-02 21:15:13, 00:00:00 ago
     last packet input 00:00:00 ago, output 00:00:00 ago, drop never ago
     type is dialer, hwaddr=none, mtu=1500, bw=128kbps, vrf=v1
     ipv4 address=2.2.2.152/25, mask=255.255.255.128, ifcid=927532203
     received 10 packets (660 bytes) dropped 0 packets (0 bytes)
     transmitted 10 packets (660 bytes) macsec=false sgt=false
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
              10|
               9|
               8|
               7|
               6|
               5|
               4|
               3|
               2|
               1|
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- seconds
              10|
               9|
               8|
               7|
               6|
               5|
               4|
               3|
               2|
               1|
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- minutes
              10|
               9|
               8|
               7|
               6|
               5|
               4|
               3|
               2|
               1|
               0|############################################################
             bps|0---------10--------20--------30--------40--------50-------- hours
    r2#
    r2#
    ```

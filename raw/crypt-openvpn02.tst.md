# Example: openvpn over ipv6
    
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
    logging file debug ../binTmp/zzz29r1-log.run
    !
    crypto ipsec ips
     cipher des
     hash md5
     key $v10$MjJmOWM2NzZmNjU1MzM2YzNmMzE4OGI4ZDljYzc1OTkwMzczMzIxMmVkNzcyMzFiYzM4MTI2YjYwMDBiMDQzZjFmNTZkMDdiODg1ZjRkMDA2NzZhZmQ4ZmVhMjVjODhmYTkxNzI5NGQ4ZjFlODliODQ5MjJkNWQyNTU2ZGU5NzdiZWFjMmYyNTRiYTJiNjc0NzcxMzFmNGQ0NzA4Y2I1MDlmNGM5Zjc4NDc4MDQ2NTQ2MmU1MDJkMjkxODM2NjViYmQ1ZWZmNmJkYzI3MzcwZjA1YWExZDg1NmI0OTdhMWY3ZWY1ZjIwYmFkN2FmZjE1NTYxOWE0YjA5ODQ5ZmFiODE0ZWU3NmU3MTIxYzJhZGY4NTMyNmRiNGMxY2NlMTMyMjAwY2EzZTRkMDM5MzBmNzY1YmE5NmE4YzQ2ZjFhYjM3NGJlYjczZTc5MDkzZDYwODc5YThkOTU4NWYyZmViOTg3ZDg5ZTY1YTMzZWYzODU3ZjNiMDlkZjgwYTI0MDNmNmM1MGRjNTA0MzllMjU4ZDYxYzdkYWMzNzc1MTRhOGQyODFjMTBmZWVlYTc5YWU3YjA2MzA2NGFlYzM5ODliNGQ4NjdiYjI0MTgyZjdkMDA3YWQ0MTI4NGVlNjU3NzA1M2RhZTJjYzI4OWRkMzllNjZjZDhmZTcwODliNzAxNWY=
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel protection ips
     tunnel source serial1
     tunnel destination 1234::2
     tunnel mode openvpn
     vrf forwarding v1
     ipv4 address 2.2.2.1 255.255.255.0
     ipv6 address 4321::1 ffff::
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
    logging file debug ../binTmp/zzz29r2-log.run
    !
    crypto ipsec ips
     cipher des
     hash md5
     key $v10$MjJmOWM2NzZmNjU1MzM2YzNmMzE4OGI4ZDljYzc1OTkwMzczMzIxMmVkNzcyMzFiYzM4MTI2YjYwMDBiMDQzZjFmNTZkMDdiODg1ZjRkMDA2NzZhZmQ4ZmVhMjVjODhmYTkxNzI5NGQ4ZjFlODliODQ5MjJkNWQyNTU2ZGU5NzdiZWFjMmYyNTRiYTJiNjc0NzcxMzFmNGQ0NzA4Y2I1MDlmNGM5Zjc4NDc4MDQ2NTQ2MmU1MDJkMjkxODM2NjViYmQ1ZWZmNmJkYzI3MzcwZjA1YWExZDg1NmI0OTdhMWY3ZWY1ZjIwYmFkN2FmZjE1NTYxOWE0YjA5ODQ5ZmFiODE0ZWU3NmU3MTIxYzJhZGY4NTMyNmRiNGMxY2NlMTMyMjAwY2EzZTRkMDM5MzBmNzY1YmE5NmE4YzQ2ZjFhYjM3NGJlYjczZTc5MDkzZDYwODc5YThkOTU4NWYyZmViOTg3ZDg5ZTY1YTMzZWYzODU3ZjNiMDlkZjgwYTI0MDNmNmM1MGRjNTA0MzllMjU4ZDYxYzdkYWMzNzc1MTRhOGQyODFjMTBmZWVlYTc5YWU3YjA2MzA2NGFlYzM5ODliNGQ4NjdiYjI0MTgyZjdkMDA3YWQ0MTI4NGVlNjU3NzA1M2RhZTJjYzI4OWRkMzllNjZjZDhmZTcwODliNzAxNWY=
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface serial1
     no description
     encapsulation hdlc
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel protection ips
     tunnel source serial1
     tunnel destination 1234::1
     tunnel mode openvpn
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.0
     ipv6 address 4321::2 ffff::
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

# Example: wireguard over asymmetric ports
    
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
    logging file debug ../binTmp/zzz5r1-log.run
    !
    crypto ipsec ips
     key $v10$RUZ3MnJKRWRxRkdEZ0M4MHVtM2Z3TW1BYWZ3cVhubytQc2JNSFBaMHVtTT1NNnZEVjhRZGlXRFFwcFZLaktmOHhqb0t0eUdBZVJLL1VlNDhrd0tJNVNzPQ==
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
     tunnel key 1234 4321
     tunnel vrf v1
     tunnel protection ips
     tunnel source serial1
     tunnel destination 1.1.1.2
     tunnel mode wireguard
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
    logging file debug ../binTmp/zzz5r2-log.run
    !
    crypto ipsec ips
     key $v10$NkpoeXZLUHV0UTlETkx1cE9QbURuUUxSV3RVV2xVakk2UFRKL0laOWwxdz1iUU1tcENhR1Z5cTlmK3Y0OFhHbWZINURNTHl0a3F6aUlEK3JCSCtxUWljPQ==
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
     tunnel key 4321 1234
     tunnel vrf v1
     tunnel protection ips
     tunnel source serial1
     tunnel destination 1.1.1.1
     tunnel mode wireguard
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

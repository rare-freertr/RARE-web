# Example: wireguard over loopback
    
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
    logging file debug ../binTmp/zzz46r1-log.run
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.101 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel protection ips
     tunnel source loopback0
     tunnel destination 1.1.1.102
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
    ipv4 route v1 1.1.1.102 255.255.255.255 1.1.1.2
    !
    !
    !
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
    logging file debug ../binTmp/zzz46r2-log.run
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
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.102 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     no shutdown
     no log-link-change
     exit
    !
    interface tunnel1
     no description
     tunnel vrf v1
     tunnel protection ips
     tunnel source loopback0
     tunnel destination 1.1.1.101
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
    ipv4 route v1 1.1.1.101 255.255.255.255 1.1.1.1
    !
    !
    !
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

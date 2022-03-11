# Example: ppp with packet over tls
    
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
    logging file debug ../binTmp/zzz27r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWgyZmh5anpHTk1OQzlXbGZCeDhBcWVWSkxBUlNOZk1qRFYrYS93ZmczZWRmQzNiMHVuMnREMnBkdVJTbGVxTy82aTk1VjY5OEIzNjV2ZFJ5OUdCaXliZnBsY1liaHMvM2lsaEhRNVFNd0tKM2w1dGJFazlqcEhvWlNKNkZJdTdkY0xhR0lGZE55NWtsY3RqOW9WNkhrcGJqNnZJdEFPcGpzaWVaeTgyL1VIamx0U0VZS2pWU0h5Q1lYd0cxWU1NV2x1RXROQ2ltd0YzSVBYSHc5TnlpTGZ4MjZmV2FhVVlibGR6TmM4Vm5IVHhYeTdJY1pWb0FCdjh1b09MMEZmSUFtNkNtR1BRNnVReEd2RG9WZDdKNmw1ZkxQaERwT0EvNVY2bzd1aW1xUVlTOHU5K3U5QzBlLzQva2VKYzJScjFNV0VOV0pkN29YRkJWN1h2QldMSXA2d0lEQVFBQkFvSUJBQ0x0NzFjR09uTWQ4OFh1K3E2Umx0QTg3NVZGUUJmZXNxb2VnWk5NYXZ1VFZmZFZKbWg5UndsMC9OeGpzUlJqN1h2eDV6RnhlV05OazRpZXAxRFhGR1RJNXA3V1RmK0c0bXB6djE1MWNKeTR6SFQxaEpiQ21BZXozNVhXSHE0V1JGVnhJRVJ6Z1FRR2E1eW0wVGF4ZGZPZ3JRYk1sa05vTTNPZnQ1TFZib2JKYUU5OEx6K1Q0bFFGZUlqREdMeW9NWmNwSFNROUxvamNScUtpM3cxS21tSjROd09mYmVKS2Y0T1RWY2dEdlI0SkxqTXprWVYydEtaem1oVDM0ay9BQzN2VjJEM1VOejEyWmxiYWdpMTlCV0RrNU5QaVZWdzRRWTdCSWNGVjJQRythOWZXSFpscENLZlNBUFEzMXhtS0N2NXJuaGtlNzArZFRwYTlTeVpOREtFQ2dZRUEwNktrNlNzS2t0R01vQTVZaWlYVHdiMnZoc3VvN2doczFIMDRPZi9xRnY2b3ArSy9JQjZ3Y2RTTmhkUWNvQ3pOS3hMUWg5UlBBS0xId0d1SU1XVzlDM3MrQUJaUVRaUmt0eC80NFNQcmVzTWQxbzNQRkNGSU5WVUFMZUcwL0R1SjQyWW14SFlMeXFRTUl1L3NCOWlCaHhVWTd2VEdZVXRBVXdqL1RtTWNQTWtDZ1lFQW84cG1KN3RmTEJhc2xWYisrV0o1SC9yN1FOODk3anRPUktpcnphc09sN1RuNlNMcXZmdVlaRWVyL2dLckp3bUpQeUUzaEwzN2pPMHhOc2N0aG9Sd2duZ0taWUlLK0dvRFRDMC9PR0t3azBKWXZMMTVZdjhpSzRvMXdHWkJ0S2wzN3NYV29seGFTM2lVRVdSdmg3Q3hKY1lqczhXSnFvMXZJanlsMmJrSzd4TUNnWUJLMFlnZGlvTGRic21aV0JrREZlWnI2dVJmOGlZUnFOYll0RUFwZVFqSUFsV2JyTFRHNVRLWnUzd2c0T0VSMjJUWkluaW9YRzFsbXlhbEp4N3AzNzdhalVKWkE0cDJNc3o4VkloSEI4emJCSm5LM1MxbFAzTG9yOWsxWDBMOW5RcmRZcUszOThlcFp4K0hSbXlhUlhkZFN4OGFjMXlpenRpNXdrZUg3Yy93eVFLQmdRQ1lYeW81dkM0RnJmSlAyK2JIeWJ3MDdCL2hjYzBEVzFpc3R0MWRMODBiaE1oYU1vbCt4Qmc0OGhRbThnU1hCR0FSd3EwTGFGSWtBR1RRT09zNVFPd0o4L0o0REVwNFh1ZENiclZwbHlYOVdMT0VvaC9TNE5iQStvcVd1b3BWcjNKTFJ2RXRpZ3pXT1E1R1A5RWh3bGFLZFpHeEpBdTJCbTFreEZibC9TY1cwUUtCZ0MzL2Z6YXBHMXZjOVZtYUhJaWJuenU5WS9xWUVzc2N6WEtKRDdCbUtSU1JWY1V5TTRoLytlTjJnWnpPeFlRQjJSWTdFdlN1N0FvY1RlZU5aL0hYL3dGT0o3QmoycHBJLytpY0c5TlI4Wmc4RTZkanRyU2dLVTM3c1lMMXFTSEdIWHA5VXVEZTV4eldZR1ZJUVVZTEdzR3dwZzhOL1V1UjI5aXpNcVh5cDA2aQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVnSUJBQUtCZ0N2NWFBc2o3ZlJSWlpWaGNyWUNMT05BTkFDVHV0Ym90NVkvYnJ4MHVzdjRJbDhjalQvMGdBRVViL2g3NjN1S2dZaVBJT0VFdW9VQVRJL2g3REhZeFN3ZkVoWjlCVHFlMFRteU9DOXhON2s2VkFod3BCbzdLVGVweFZ5eDNhMVRFR1ZwZVA2OHNHdkVkRGIxUzlXNFZlZEl0bTgxTVRGVDNIRHduZjZzTnZVWEFoVUFtYlJ6TmlkTkNNcVRoU3dmOWJ3bW1Tem5ORzBDZ1lBUVVka2Vyb0FxUkRMclErQXQ5TUtnY3l3RkVpenF4YmVFWHU1N0hDVWw5cU0zNGhmTjZ3eVZHN3l1cjdRU1lDKzJualJRaDF3RE11ZS9WWFNEOGt0Mi9iWDlZck5wclRtNlRVaVJOejVrc01IR3FBdldEVXBhc01pNW5VeE1tWktlNnVnaE1MUm9RUFlZWWRSUTcrcFRnck93djh5SzE0ZzZjck9oL0djdGJRS0JnQnB1SGhUN0RSUDcyY2Y3OHhUZncvS2J0MmRYNjIzWGRzN0RRZ01kTWY4Q3paUThPNDhpaDIzUUdGVFpKQjRFNkhLNUozY1dTKzRiM1Rrc2RMdXZpd1p0T2w2R2E0YktJcmszT1I1R2NlRGdtWWN1d3FEdDBYd0NnSHZzRFltYW12RUxyY0xtZHlyZlI5eXVKSmlzdEQ1cURBM3kvTmVmR0oveTl2TTRDNkJQQWhVQTdtSDVPZjZHUnpLZElzV2EyRE1HbWpXcm5TUT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUNFYUYrVVlZd1FmbVV5NVNtQ1BENEdFc3AwckpsbWdCV2dhbHE2USs1VW9BY0dCU3VCQkFBS29VUURRZ0FFRDFPdzlZQjIrb3hieVQ4ZWRBQkRuWU9PWUlpM0ZENDJ6MzVsU0QzMVJEK1JLcUtiNWUycEVrMjJsVHMwQ3BuMnV4M0dtZ2tocHFJN2xMT2s2bEVQa1E9PQ==
    !
    crypto certificate dsa import dsa dsa $v10$TUlJQ1V6Q0NBZytnQXdJQkFnSUVkOWU5c1RBTEJnY3Foa2pPT0FRREJRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNREV3V2hjTk16SXdNekEzTWpBMU1ERXdXakFOTVFzd0NRWURWUVFERXdKeU1UQ0NBYlV3Z2dFcUJnY3Foa2pPT0FRQk1JSUJIUUtCZ0N2NWFBc2o3ZlJSWlpWaGNyWUNMT05BTkFDVHV0Ym90NVkvYnJ4MHVzdjRJbDhjalQvMGdBRVViL2g3NjN1S2dZaVBJT0VFdW9VQVRJL2g3REhZeFN3ZkVoWjlCVHFlMFRteU9DOXhON2s2VkFod3BCbzdLVGVweFZ5eDNhMVRFR1ZwZVA2OHNHdkVkRGIxUzlXNFZlZEl0bTgxTVRGVDNIRHduZjZzTnZVWEFoVUFtYlJ6TmlkTkNNcVRoU3dmOWJ3bW1Tem5ORzBDZ1lBUVVka2Vyb0FxUkRMclErQXQ5TUtnY3l3RkVpenF4YmVFWHU1N0hDVWw5cU0zNGhmTjZ3eVZHN3l1cjdRU1lDKzJualJRaDF3RE11ZS9WWFNEOGt0Mi9iWDlZck5wclRtNlRVaVJOejVrc01IR3FBdldEVXBhc01pNW5VeE1tWktlNnVnaE1MUm9RUFlZWWRSUTcrcFRnck93djh5SzE0ZzZjck9oL0djdGJRT0JoQUFDZ1lBYWJoNFUrdzBUKzluSCsvTVUzOFB5bTdkblYrdHQxM2JPdzBJREhUSC9BczJVUER1UElvZHQwQmhVMlNRZUJPaHl1U2QzRmt2dUc5MDVMSFM3cjRzR2JUcGVobXVHeWlLNU56a2VSbkhnNEptSExzS2c3ZEY4QW9CNzdBMkptcHJ4QzYzQzVuY3EzMGZjcmlTWXJMUSthZ3dOOHZ6WG54aWY4dmJ6T0F1Z1R6QUxCZ2NxaGtqT09BUURCUUFETVFBQU1DMENGUUNNSGR4Q2pReFI1VkxSM1NlTHoydGVCVnZPUndJVVFLeHZwNm9BbGlLRDE2MDlUNlpLb2JYR0I5dz0=
    !
    crypto certificate ecdsa import ecdsa ecdsa $v10$TUlJQlRUQ0JzS0FEQWdFQ0FnUUxoeWVVTUF3R0NDcUdTTTQ5QkFNQ0JRQXdEVEVMTUFrR0ExVUVBeE1DY2pFd0hoY05Nakl3TXpFd01qQTFNREV3V2hjTk16SXdNekEzTWpBMU1ERXdXakFOTVFzd0NRWURWUVFERXdKeU1UQlhNQkFHQnlxR1NNNDlBZ0VHQlN1QkJBQUtBME1BQUFRUFU3RDFnSGI2akZ2SlB4NTBBRU9kZzQ1Z2lMY1VQamJQZm1WSVBmVkVQNUVxb3B2bDdha1NUYmFWT3pRS21mYTdIY2FhQ1NHbW9qdVVzNlRxVVErUk1Bd0dDQ3FHU000OUJBTUNCUUFEZ1lrQUFEQ0JoQUloQU4zeks1M0pDcElmelRzQWN6SmY4bEw1RGIyUjM2WjNwRU5PRUpwMzNTSE1BbDhPUERSUlo0MTFMNHZQSmxYZEF3UnBiNCs4dUJIVmxWbVROYXFPbHRRWTErMk1GbnY1ZkdDSDVYalp2YXIza3RWcVRxbEdBSWI5RitxVGMrbUhiT29sUEh6VGtpaGFCRGtqQkt0U2dnb3dXNWI0SkJuVzJFWVB0RFFHd2JmSUVBPT0=
    !
    crypto certificate rsa import rsa rsa $v10$TUlJQ2xqQ0NBWDZnQXdJQkFnSUVlaWpvRkRBTkJna3Foa2lHOXcwQkFRc0ZBREFOTVFzd0NRWURWUVFERXdKeU1UQWVGdzB5TWpBek1UQXlNRFV3TVRCYUZ3MHpNakF6TURjeU1EVXdNVEJhTUEweEN6QUpCZ05WQkFNVEFuSXhNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQWgyZmh5anpHTk1OQzlXbGZCeDhBcWVWSkxBUlNOZk1qRFYrYS93ZmczZWRmQzNiMHVuMnREMnBkdVJTbGVxTy82aTk1VjY5OEIzNjV2ZFJ5OUdCaXliZnBsY1liaHMvM2lsaEhRNVFNd0tKM2w1dGJFazlqcEhvWlNKNkZJdTdkY0xhR0lGZE55NWtsY3RqOW9WNkhrcGJqNnZJdEFPcGpzaWVaeTgyL1VIamx0U0VZS2pWU0h5Q1lYd0cxWU1NV2x1RXROQ2ltd0YzSVBYSHc5TnlpTGZ4MjZmV2FhVVlibGR6TmM4Vm5IVHhYeTdJY1pWb0FCdjh1b09MMEZmSUFtNkNtR1BRNnVReEd2RG9WZDdKNmw1ZkxQaERwT0EvNVY2bzd1aW1xUVlTOHU5K3U5QzBlLzQva2VKYzJScjFNV0VOV0pkN29YRkJWN1h2QldMSXA2d0lEQVFBQk1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQktwMGsyS2xuT3ptODRGNHFlZk1LaG40T0o2WEt4TTN4dWNhNmlXVDRMNDV2R0hPeTJPT0oxRmhpVHBmT3VuWUJLaGxkTjJ0M2VIbnFEZzlwSFhZVkJJUFdBOXNwaVR1ODY3YjBFeDlzOFdteFZtWkxCQ3pVTUFIbFJ1MnZwRzJBcVZGQThrYTNqdFNNc3VoTVZQbjlmUGZ3S0hsZW9nYm5FMncwU2tuSWUyQ043eHBSeGNveDI4OGdKNHowc1lBaUsralp2RUlZVEswLzNHaG1uRnJoelZqVXhwNU8zOXRvZitteTdURmxNeExPZ1VjMU9iNWhGTnQyL1Z6YVU3dTUxQ0hERFZxcVBQNDBnZ3M0bDU5aUtYOThwOHpxZ1pYRW5TdnliMUpSd2NGV21IcERuVWdHdXJiQk51a2o2dkg1RTB6eENMMFBsbHJmL2JWKzMvVlYy
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
     ipv4 address 4.4.4.4 255.255.255.255
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
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
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
    server pckotcp pou
     security protocol tls
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     security rsacert rsa
     security dsacert dsa
     security ecdsacert ecdsa
     clone dialer1
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
    logging file debug ../binTmp/zzz27r2-log.run
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
     ipv4 address 3.3.3.3 255.255.255.128
     ipv4 gateway-prefix p1
     no shutdown
     no log-link-change
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
    proxy-profile p1
     security tls
     vrf v1
     exit
    !
    vpdn pou
     interface dialer1
     proxy p1
     target 1.1.1.1
     vcid 2554
     protocol pckotcp
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

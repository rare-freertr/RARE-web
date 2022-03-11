# Example: dummy test
    
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
    logging file debug ../binTmp/zzz31r1-log.run
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
     ipv4 address 1.1.1.1 255.255.255.0
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
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
    r1#
    r1#
    r1#show version
    r1#show version
    freeRouter v22.3.10-cur, done by cs@nop.
    place on the web: http://www.freertr.net/
    license: http://creativecommons.org/licenses/by-sa/4.0/
    quote1: make the world better
    quote2: if a machine can learn the value of human life, maybe we can too
    quote3: be liberal in what you accept, and conservative in what you send
    quote4: the beer-ware license for selected group of people:
    cs@nop wrote these files. as long as you retain this notice you
    can do whatever you want with this stuff. if we meet some day, and
    you think this stuff is worth it, you can buy me a beer in return
    r1#
    r1#
    ```
    
    ```
    r1#
    r1#
    r1#show platform
    r1#show platform
    freeRouter v22.3.10-cur, done by cs@nop.
    name: r1
    hwid: tester-slot31
    hwsn: null
    uptime: since 2022-03-10 20:47:15, for 00:00:00
    reload: code#11=user requested
    rwpath: ../binTmp/
    hwcfg: ../binTmp/zzz31r1-hw.txt
    swcfg: ../binTmp/zzz31r1-sw.txt
    cpu: 40*amd64
    mem: free=162g, max=162g, used=162g
    host: Linux v5.16.0-4-amd64
    java: Oracle Corporation v17.0.2 @ null
    jspec: Oracle Corporation (Java Platform API Specification) v17
    vm: Oracle Corporation (Substrate VM) vGraalVM 22.0.0.2 Java 17 CE
    vmspec: Oracle Corporation (Java Virtual Machine Specification) v17
    class: v61.0 @
    r1#
    r1#
    ```

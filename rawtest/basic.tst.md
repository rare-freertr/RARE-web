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
    logging file debug ../binTmp/zzz1r1-log.run
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
    freeRouter v21.12.30-cur, done by cs@nop.
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
    freeRouter v21.12.30-cur, done by cs@nop.
    name: r1
    hwid: tester-slot1
    uptime: since 2021-12-30 18:24:05, for 00:00:01
    reload: code#1=finished
    hwcfg: ../binTmp/zzz1r1-hw.txt
    swcfg: ../binTmp/zzz1r1-sw.txt
    cpu: 1*amd64
    mem: free=16m, max=259m, used=32m
    host: Linux v5.10.0-10-amd64
    java: Debian v11.0.13 @ /usr/lib/jvm/java-11-openjdk-amd64
    jspec: Oracle Corporation (Java Platform API Specification) v11
    vm: Debian (OpenJDK 64-Bit Server VM) v11.0.13+8-post-Debian-1deb11u1
    vmspec: Oracle Corporation (Java Virtual Machine Specification) v11
    class: v55.0 @ rtr.jar
    r1#
    r1#
    ```

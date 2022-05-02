# Example: dummy test

## **Topology diagram**

![topology](/img/basic.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz19r1-log.run
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
 ipv4 address 1.1.1.1 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
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
r1#
r1#
r1#show version
r1#show version
freeRouter v22.5.2-cur, done by cs@nop.
place on the web: http://www.freertr.org/
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
freeRouter v22.5.2-cur, done by cs@nop.
name: r1
hwid: tester-slot19
hwsn: null
uptime: since 2022-05-02 21:15:44, for 00:00:01
reload: code#9=dual active, reloading because lost on priority
rwpath: ../binTmp/
hwcfg: ../binTmp/zzz19r1-hw.txt
swcfg: ../binTmp/zzz19r1-sw.txt
cpu: 40*amd64
mem: free=162g, max=162g, used=162g
host: Linux v5.17.0-1-amd64
java: Oracle Corporation v17.0.3 @ null
jspec: Oracle Corporation (Java Platform API Specification) v17
vm: Oracle Corporation (Substrate VM) vGraalVM 22.1.0 Java 17 CE
vmspec: Oracle Corporation (Java Virtual Machine Specification) v17
class: v61.0 @
r1#
r1#
```

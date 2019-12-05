# Example: dummy test

## **Topology diagram**

![topology](/img/basic.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
end
```

## **Verification**

```
r1#
r1#
r1#show version
r1#show version
freeRouter v20.1.15-testing, done by cs@nop.
place on the net: http://freerouter.nop.hu/
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
freeRouter v20.1.15-testing, done by cs@nop.
name: r1
hwid: null
uptime: since 2020-01-15 06:17:58, for 00:00:00
reload: code#1=finished
hwcfg: ../binTmp/zzz-r1-hw.txt
swcfg: ../binTmp/zzz-r1-sw.txt
cpu: 8*amd64
mem: free=224m, max=268m, used=264m
host: Linux v5.4.0-2-amd64
java: Debian v14-ea @ /usr/lib/jvm/java-14-openjdk-amd64
jspec: Oracle Corporation (Java Platform API Specification) v14
vm: Debian (OpenJDK 64-Bit Server VM) v14-ea+27-Debian-1
vmspec: Oracle Corporation (Java Virtual Machine Specification) v14
class: v58.0 @ rtr.jar
r1#
r1#
```

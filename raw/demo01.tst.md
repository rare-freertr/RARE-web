# Example: empty demo network

## **Topology diagram**

![topology](/img/demo01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz4r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
int eth1
 desc r2 e1
 lldp ena
 exit
int eth2
 desc r3 e2
 lldp ena
 exit
```

**r2:**
```
hostname r2
logging file debug ../binTmp/zzz4r2-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
int eth1
 desc r1 e1
 lldp ena
 exit
int eth2
 desc r4 e2
 lldp ena
 exit
```

**r3:**
```
hostname r3
logging file debug ../binTmp/zzz4r3-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
int eth1
 desc r4 e1
 lldp ena
 exit
int eth2
 desc r1 e2
 lldp ena
 exit
```

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz4r4-log.run
!
vrf definition tester
 exit
!
interface ethernet1
 description r3 e1
 lldp enable
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 description r2 e2
 lldp enable
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

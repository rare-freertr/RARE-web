# Example: empty demo network

## **Topology diagram**

![topology](/img/demo01.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz-log-r1.run
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
logging file debug ../binTmp/zzz-log-r2.run
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
logging file debug ../binTmp/zzz-log-r3.run
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
logging file debug ../binTmp/zzz-log-r4.run
int eth1
 desc r3 e1
 lldp ena
 exit
int eth2
 desc r2 e2
 lldp ena
 exit
```

**r5:**
```
hostname r5
logging file debug ../binTmp/zzz-log-r5.run
int eth1
 desc r5 e2
 lldp ena
 exit
int eth2
 desc r5 e1
 lldp ena
 exit
int eth3
 desc r5 e4
 lldp ena
 exit
int eth4
 desc r5 e3
 lldp ena
 exit
int eth5
 desc r5 e6
 lldp ena
 exit
int eth6
 desc r5 e5
 lldp ena
 exit
int eth7
 desc r5 e8
 lldp ena
 exit
int eth8
 desc r5 e7
 lldp ena
 exit
```

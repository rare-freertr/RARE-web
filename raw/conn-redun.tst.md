# Example: process redundancy

## **Topology diagram**

![topology](/img/conn-redun.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz-log-r1.run
vrf def v1
 rd 1:1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
```

**r2:**
```
hostname r2
logging file debug ../binTmp/zzz-log-r2.run
vrf def v1
 rd 1:1
 exit
bridge 1
 exit
int eth1
 bridge-gr 1
 exit
int eth2
 bridge-gr 1
 exit
int eth3
 bridge-gr 1
 exit
int bvi1
 vrf for v1
 ipv4 addr 1.1.1.2 255.255.255.0
 ipv6 addr 1234::2 ffff::
 exit
```

**r3:**
```
hostname r3
logging file debug ../binTmp/zzz-log-r3.run
vrf def v1
 rd 1:1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.3 255.255.255.0
 ipv6 addr 1234::3 ffff::
 exit
```

**r4:**
```
hostname r4
logging file debug ../binTmp/zzz-log-r4.run
vrf def v1
 rd 1:1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.4 255.255.255.0
 ipv6 addr 1234::4 ffff::
 exit
```

## **Verification**

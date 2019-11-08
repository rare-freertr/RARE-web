# Example: interop9: config wiper

## **Topology diagram**

![topology](/img/intop9-zzz.tst.png)

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

## **Verification**

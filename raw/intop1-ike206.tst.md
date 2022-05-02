# Example: interop1: ike2 with aes256cbc

## **Topology diagram**

![topology](/img/intop1-ike206.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz41r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234::1 ffff::
 exit
crypto ipsec ips
 group 01
 cipher aes256cbc
 hash md5
 seconds 3600
 bytes 67108864
 key tester
 role init
 isakmp 2
 protected ipv4
 exit
int tun1
 tunnel vrf v1
 tunnel prot ips
 tunnel mode ipsec
 tunnel source ethernet1
 tunnel destination 1.1.1.2
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.0
 ipv6 addr 4321::1 ffff::
 exit
```

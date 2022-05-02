# Example: p4lang: openvpn over asymmetric ports

## **Topology diagram**

![topology](/img/p4lang-crypt056.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz21r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
vrf def v2
 rd 1:1
 exit
vrf def v9
 rd 1:1
 exit
int lo9
 vrf for v9
 ipv4 addr 10.10.10.227 255.255.255.255
 exit
int eth1
 vrf for v9
 ipv4 addr 10.11.12.254 255.255.255.0
 exit
int eth2
 exit
server dhcp4 eth1
 pool 10.11.12.1 10.11.12.99
 gateway 10.11.12.254
 netmask 255.255.255.0
 dns-server 10.10.10.227
 domain-name p4l
 static 0000.0000.2222 10.11.12.111
 interface eth1
 vrf v9
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.101 255.255.255.255
 ipv6 addr 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int lo1
 vrf for v2
 ipv4 addr 8.8.8.1 255.255.255.255
 exit
int sdn1
 vrf for v2
 ipv4 addr 9.9.9.1 255.255.255.0
 exit
crypto ipsec ips
 cipher des
 hash md5
 key 22f9c676f655336c3f3188b8d9cc759903733212ed77231bc38126b6000b043f1f56d07b885f4d00676afd8fea25c88fa917294d8f1e89b84922d5d2556de977beac2f254ba2b67477131f4d4708cb509f4c9f784780465462e502d29183665bbd5eff6bdc27370f05aa1d856b497a1f7ef5f20bad7aff155619a4b09849fab814ee76e7121c2adf85326db4c1cce132200ca3e4d03930f765ba96a8c46f1ab374beb73e79093d60879a8d9585f2feb987d89e65a33ef3857f3b09df80a2403f6c50dc50439e258d61c7dac377514a8d281c10feeea79ae7b063064aec3989b4d867bb24182f7d007ad41284ee6577053dae2cc289dd39e66cd8fe7089b7015f
 replay 0
 exit
int tun1
 tun vrf v2
 tun source lo1
 tun destination 8.8.8.2
 tun prot ips
 tunnel key 1234 4321
 tun mode openvpn
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 ipv6 addr 1234:1::1 ffff:ffff::
 ipv6 ena
 exit
int sdn2
 vrf for v1
 ipv4 addr 1.1.2.1 255.255.255.0
 ipv6 addr 1234:2::1 ffff:ffff::
 ipv6 ena
 exit
int sdn3
 vrf for v1
 ipv4 addr 1.1.3.1 255.255.255.0
 ipv6 addr 1234:3::1 ffff:ffff::
 ipv6 ena
 exit
int sdn4
 vrf for v1
 ipv4 addr 1.1.4.1 255.255.255.0
 ipv6 addr 1234:4::1 ffff:ffff::
 ipv6 ena
 exit
server p4lang p4
 interconnect eth2
 export-vrf v1 1
 export-vrf v2 2
 export-port sdn1 1 10
 export-port sdn2 2 10
 export-port sdn3 3 10
 export-port sdn4 4 10
 export-port tun1 dynamic
 vrf v9
 exit
ipv4 route v2 8.8.8.2 255.255.255.255 9.9.9.2
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.2.2
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.3.2
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.4.2
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
```

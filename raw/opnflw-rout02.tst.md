# Example: openflow: bridging and routing

## **Topology diagram**

![topology](/img/opnflw-rout02.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
bridge 1
 exit
!
vrf definition v1
 rd 1:1
 exit
!
vrf definition v9
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.101 255.255.255.255
 ipv6 address 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface loopback9
 no description
 vrf forwarding v9
 ipv4 address 10.10.10.227 255.255.255.255
 no shutdown
 no log-link-change
 exit
!
interface bvi1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v9
 ipv4 address 10.11.12.254 255.255.255.0
 no shutdown
 no log-link-change
 exit
!
interface sdn1
 no description
 mtu 1500
 macaddr 0048.4749.0634
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 no description
 mtu 1500
 macaddr 006e.1e25.3622
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 0067.6549.5708
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 0046.6a66.1044
 vrf forwarding v1
 ipv4 address 1.1.4.1 255.255.255.0
 ipv6 address 1234:4::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.1.3
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.1.4
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.4.2
!
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::4
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
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
server openflow of
 export-vrf v1
 export-port bvi1 -1
 export-port sdn1 1
 export-port sdn2 2
 export-port sdn3 3
 export-port sdn4 4
 vrf v9
 exit
!
server dhcp4 eth1
 pool 10.11.12.1 10.11.12.99
 gateway 10.11.12.254
 netmask 255.255.255.0
 dns-server 10.10.10.227
 domain-name ovs
 static 0000.0000.2222 10.11.12.111
 interface ethernet1
 vrf v9
 exit
!
!
end
```

**r2:**
```
hostname r2
```

**r3:**
```
hostname r3
buggy
!
logging file debug ../binTmp/zzz-log-r3.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.103 255.255.255.255
 ipv6 address 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234:1::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.1.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.1.3
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.1.4
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.1.1
!
ipv6 route v1 1234:4:: ffff:ffff:: 1234:1::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::4
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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

**r4:**
```
hostname r4
buggy
!
logging file debug ../binTmp/zzz-log-r4.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.104 255.255.255.255
 ipv6 address 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.3 255.255.255.0
 ipv6 address 1234:1::3 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.1.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.1.4
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.1.1
!
ipv6 route v1 1234:4:: ffff:ffff:: 1234:1::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::4
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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

**r5:**
```
hostname r5
buggy
!
logging file debug ../binTmp/zzz-log-r5.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.105 255.255.255.255
 ipv6 address 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.4 255.255.255.0
 ipv6 address 1234:1::4 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.1.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.1.3
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.1.1
!
ipv6 route v1 1234:4:: ffff:ffff:: 1234:1::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::3
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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

**r6:**
```
hostname r6
buggy
!
logging file debug ../binTmp/zzz-log-r6.run
!
vrf definition v1
 rd 1:1
 exit
!
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.106 255.255.255.255
 ipv6 address 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.4.2 255.255.255.0
 ipv6 address 1234:4::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.1.0 255.255.255.0 1.1.4.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.4.1
!
ipv6 route v1 1234:1:: ffff:ffff:: 1234:4::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
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
tcl:%noproc:telnet 10.11.12.111 2323 /vrf v9 /int lo9%
tcl>exec "telnet 10.11.12.111 2323 /vrf v9 /int lo9"
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 33698 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=1086950417,type=all,bucket=actions=output:ens4,bucket=actions=output:ens5,bucket=actions=output:ens6
 cookie=0x7c9c3d8d, duration=49.550s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x29e2d4e4, duration=49.550s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x75259649, duration=49.550s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x4db6c4d1, duration=49.550s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x236667f4, duration=49.550s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x16849e2, duration=49.549s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0xcd49dea, duration=49.549s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x3ad63e59, duration=49.550s, table=0, n_packets=36, n_bytes=3816, priority=2,ip,in_port=ens4,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,2)
 cookie=0x386b5774, duration=49.550s, table=0, n_packets=1, n_bytes=60, priority=2,arp,in_port=ens4,dl_dst=00:4c:49:4c:77:56 actions=CONTROLLER:65535
 cookie=0x5fb0fd03, duration=49.550s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens4,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,3)
 cookie=0x28364c52, duration=49.550s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens4,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,1)
 cookie=0xfe831cd, duration=49.550s, table=0, n_packets=39, n_bytes=4134, priority=2,ip,in_port=ens5,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,2)
 cookie=0x45b35442, duration=49.550s, table=0, n_packets=1, n_bytes=60, priority=2,arp,in_port=ens5,dl_dst=00:4c:49:4c:77:56 actions=CONTROLLER:65535
 cookie=0x2a63637a, duration=49.550s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens5,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,3)
 cookie=0x4b72bb40, duration=49.550s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens5,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,1)
 cookie=0x7aa97b3a, duration=49.549s, table=0, n_packets=39, n_bytes=4134, priority=2,ip,in_port=ens6,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,2)
 cookie=0x15c1785, duration=49.549s, table=0, n_packets=1, n_bytes=60, priority=2,arp,in_port=ens6,dl_dst=00:4c:49:4c:77:56 actions=CONTROLLER:65535
 cookie=0x1908d9b, duration=49.549s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens6,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,3)
 cookie=0x1e885602, duration=49.549s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens6,dl_dst=00:4c:49:4c:77:56 actions=resubmit(,1)
 cookie=0x7f3b015, duration=49.550s, table=0, n_packets=90, n_bytes=10460, priority=1,in_port=ens4 actions=group:1086950417
 cookie=0x581b2f77, duration=49.550s, table=0, n_packets=89, n_bytes=10334, priority=1,in_port=ens5 actions=group:1086950417
 cookie=0x20f7670d, duration=49.550s, table=0, n_packets=88, n_bytes=10208, priority=1,in_port=ens6 actions=group:1086950417
 cookie=0x5cc557a7, duration=49.550s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x257870de, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x2b0769c7, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x4e3fc089, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=589549,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x50d22089, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=710284,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x4ed84993, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=302876 actions=CONTROLLER:65535
 cookie=0x3c585984, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=407176 actions=CONTROLLER:65535
 cookie=0x64890b76, duration=49.549s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x3ebb2fb, duration=49.548s, table=2, n_packets=24, n_bytes=2544, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x1cc2ec8b, duration=49.548s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x7ce4fb14, duration=49.548s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x78d68dc3, duration=48.868s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:33:33,group:1086950417
 cookie=0x3db3fff, duration=49.548s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:33:33,dec_ttl,group:1086950417
 cookie=0x35b137b, duration=43.067s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.3 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:44:44,group:1086950417
 cookie=0x139b6ce2, duration=49.548s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:44:44,dec_ttl,group:1086950417
 cookie=0x48a79a8d, duration=37.265s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.4 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:55:55,group:1086950417
 cookie=0x63075e3a, duration=49.548s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:55:55,dec_ttl,group:1086950417
 cookie=0x417fba26, duration=31.461s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:46:6a:66:10:44,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x50bdf30c, duration=49.548s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:46:6a:66:10:44,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x78b0bae2, duration=49.548s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x1870ea8, duration=49.548s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x271be97f, duration=49.548s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x1cd6052c, duration=49.548s, table=3, n_packets=24, n_bytes=3024, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x67879aaf, duration=49.548s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x53982070, duration=49.548s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x6b03699, duration=49.547s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::246:6aff:fe66:1044 actions=CONTROLLER:65535
 cookie=0x4ba37907, duration=49.547s, table=3, n_packets=3, n_bytes=258, priority=228,ipv6,ipv6_dst=fe80::24c:49ff:fe4c:7756 actions=CONTROLLER:65535
 cookie=0x6c2ddb6d, duration=46.467s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:33:33,group:1086950417
 cookie=0x321f27a6, duration=49.548s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:33:33,dec_ttl,group:1086950417
 cookie=0x6bdd548f, duration=45.467s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:33:33,group:1086950417
 cookie=0x7e605307, duration=40.665s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::3 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:44:44,group:1086950417
 cookie=0x2c6ab3ff, duration=49.548s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:44:44,dec_ttl,group:1086950417
 cookie=0x221c5978, duration=39.664s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:44:44,group:1086950417
 cookie=0x12ae9e59, duration=34.863s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::4 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:55:55,group:1086950417
 cookie=0x1dc68c3d, duration=49.547s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:55:55,dec_ttl,group:1086950417
 cookie=0x1b00798f, duration=33.859s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:4c:49:4c:77:56,mod_dl_dst:00:00:00:00:55:55,group:1086950417
 cookie=0x2e5473ca, duration=29.061s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:46:6a:66:10:44,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x70dbe958, duration=49.547s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:46:6a:66:10:44,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x2fbd431, duration=28.060s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:46:6a:66:10:44,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x343ccaa0, duration=49.548s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x26401b5f, duration=49.548s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0xd4cd09b, duration=49.548s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

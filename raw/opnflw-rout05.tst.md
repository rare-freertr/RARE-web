# Example: openflow: multicast routing

## **Topology diagram**

![topology](/img/opnflw-rout05.tst.png)

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
 macaddr 0060.5d16.0478
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 no description
 mtu 1500
 macaddr 0012.3031.0940
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 multicast static-group 232.2.2.2 2.2.2.103
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 multicast static-group ff06::1 4321::103
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 005f.7c5b.697d
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv4 multicast static-group 232.2.2.2 2.2.2.103
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 multicast static-group ff06::1 4321::103
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 0025.7d0a.3b1f
 vrf forwarding v1
 ipv4 address 1.1.4.1 255.255.255.0
 ipv4 multicast static-group 232.2.2.2 2.2.2.103
 ipv6 address 1234:4::1 ffff:ffff::
 ipv6 multicast static-group ff06::1 4321::103
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.1.2
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.2.2
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.3.2
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.4.2
!
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::2
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::2
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::2
!
ipv4 mroute v1 2.2.2.103 255.255.255.255 1.1.1.2
!
ipv6 mroute v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::2
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
 ipv4 multicast static-group 232.2.2.2 2.2.2.103
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 multicast static-group ff06::1 4321::103
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.2.0 255.255.255.0 1.1.1.1
ipv4 route v1 1.1.3.0 255.255.255.0 1.1.1.1
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.1.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.1.1
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.1.1
!
ipv6 route v1 1234:2:: ffff:ffff:: 1234:1::1
ipv6 route v1 1234:3:: ffff:ffff:: 1234:1::1
ipv6 route v1 1234:4:: ffff:ffff:: 1234:1::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:1::1
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
 ipv4 address 1.1.2.2 255.255.255.0
 ipv6 address 1234:2::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.1.0 255.255.255.0 1.1.2.1
ipv4 route v1 1.1.3.0 255.255.255.0 1.1.2.1
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.2.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.2.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.2.1
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.2.1
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.2.1
!
ipv6 route v1 1234:1:: ffff:ffff:: 1234:2::1
ipv6 route v1 1234:3:: ffff:ffff:: 1234:2::1
ipv6 route v1 1234:4:: ffff:ffff:: 1234:2::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
!
ipv4 mroute v1 2.2.2.103 255.255.255.255 1.1.2.1
!
ipv6 mroute v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:2::1
!
!
!
!
!
ipv4 multicast v1 join-group 232.2.2.2 2.2.2.103
!
ipv6 multicast v1 join-group ff06::1 4321::103
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
 ipv4 address 1.1.3.2 255.255.255.0
 ipv6 address 1234:3::2 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
ipv4 route v1 1.1.1.0 255.255.255.0 1.1.3.1
ipv4 route v1 1.1.2.0 255.255.255.0 1.1.3.1
ipv4 route v1 1.1.4.0 255.255.255.0 1.1.3.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.3.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.3.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.3.1
ipv4 route v1 2.2.2.106 255.255.255.255 1.1.3.1
!
ipv6 route v1 1234:1:: ffff:ffff:: 1234:3::1
ipv6 route v1 1234:2:: ffff:ffff:: 1234:3::1
ipv6 route v1 1234:4:: ffff:ffff:: 1234:3::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
ipv6 route v1 4321::106 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
!
ipv4 mroute v1 2.2.2.103 255.255.255.255 1.1.3.1
!
ipv6 mroute v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:3::1
!
!
!
!
!
ipv4 multicast v1 join-group 232.2.2.2 2.2.2.103
!
ipv6 multicast v1 join-group ff06::1 4321::103
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
ipv4 route v1 1.1.2.0 255.255.255.0 1.1.4.1
ipv4 route v1 1.1.3.0 255.255.255.0 1.1.4.1
ipv4 route v1 2.2.2.101 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.103 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.104 255.255.255.255 1.1.4.1
ipv4 route v1 2.2.2.105 255.255.255.255 1.1.4.1
!
ipv6 route v1 1234:1:: ffff:ffff:: 1234:4::1
ipv6 route v1 1234:2:: ffff:ffff:: 1234:4::1
ipv6 route v1 1234:3:: ffff:ffff:: 1234:4::1
ipv6 route v1 4321::101 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::104 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
ipv6 route v1 4321::105 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
!
ipv4 mroute v1 2.2.2.103 255.255.255.255 1.1.4.1
!
ipv6 mroute v1 4321::103 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 1234:4::1
!
!
!
!
!
ipv4 multicast v1 join-group 232.2.2.2 2.2.2.103
!
ipv6 multicast v1 join-group ff06::1 4321::103
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 44730 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=1962377749,type=all,bucket=actions=mod_dl_src:00:12:30:31:09:40,output:ens5,bucket=actions=mod_dl_src:00:5f:7c:5b:69:7d,output:ens6,bucket=actions=mod_dl_src:00:25:7d:0a:3b:1f,output:ens7
 group_id=1765478571,type=all,bucket=actions=mod_dl_src:00:12:30:31:09:40,output:ens5,bucket=actions=mod_dl_src:00:5f:7c:5b:69:7d,output:ens6,bucket=actions=mod_dl_src:00:25:7d:0a:3b:1f,output:ens7
 cookie=0x131f0bba, duration=40.226s, table=0, n_packets=76, n_bytes=8056, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x6d0cf778, duration=40.226s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x1bd8a47d, duration=40.226s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x7b0f3878, duration=40.226s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x2db084b0, duration=40.226s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x1735736a, duration=40.226s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x6d9909b2, duration=40.226s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x4a94f056, duration=40.226s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0xa9442d1, duration=40.226s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x5daee7d1, duration=40.226s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x79b2e964, duration=40.226s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x245d8e4, duration=40.226s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x44e1902e, duration=40.225s, table=0, n_packets=5, n_bytes=530, priority=3,ip,in_port=ens4,nw_src=2.2.2.103,nw_dst=232.2.2.2 actions=group:1962377749
 cookie=0x10e5d64f, duration=40.225s, table=0, n_packets=5, n_bytes=630, priority=3,ipv6,in_port=ens4,ipv6_src=4321::103,ipv6_dst=ff06::1 actions=group:1765478571
 cookie=0x2aea4c4a, duration=40.226s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x7a66ce61, duration=40.226s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x7278b4eb, duration=40.226s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x265e3926, duration=40.225s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x39effaf2, duration=40.226s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x4e971243, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x49187989, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x5b453da, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=109531,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x6c01ba19, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=332399,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x2c1ce4dc, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=345880 actions=CONTROLLER:65535
 cookie=0x1c7735, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=738996 actions=CONTROLLER:65535
 cookie=0x2006d322, duration=40.224s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x510faa85, duration=40.224s, table=2, n_packets=6, n_bytes=636, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x60a6b640, duration=40.224s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x341eabf7, duration=40.224s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x469556c2, duration=40.224s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x343f95b, duration=40.224s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x152d112d, duration=39.850s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:60:5d:16:04:78,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x5cd28865, duration=40.224s, table=2, n_packets=45, n_bytes=4770, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:60:5d:16:04:78,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x2faccd5a, duration=34.048s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:12:30:31:09:40,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x9832819, duration=40.224s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:12:30:31:09:40,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x6c20630f, duration=28.245s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:5f:7c:5b:69:7d,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x15cb4457, duration=40.224s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:5f:7c:5b:69:7d,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x369630ae, duration=22.443s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:25:7d:0a:3b:1f,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x5ada2f01, duration=40.224s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:25:7d:0a:3b:1f,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x3862aff8, duration=40.224s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x706500c1, duration=40.224s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x5dc4a1d5, duration=40.224s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x3a3424b0, duration=40.224s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x4432b17b, duration=40.224s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x4d648414, duration=40.222s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x1f23d70b, duration=40.222s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x32c53a60, duration=40.222s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x1ed4bc0e, duration=40.222s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x729a94e8, duration=40.222s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x2cf2a9be, duration=40.222s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::212:30ff:fe31:940 actions=CONTROLLER:65535
 cookie=0x1cdc35bb, duration=40.222s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::225:7dff:fe0a:3b1f actions=CONTROLLER:65535
 cookie=0x1b3a7f37, duration=40.222s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::25f:7cff:fe5b:697d actions=CONTROLLER:65535
 cookie=0x33740ec5, duration=40.222s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::260:5dff:fe16:478 actions=CONTROLLER:65535
 cookie=0x35c7ea87, duration=37.449s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:60:5d:16:04:78,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x244ec982, duration=40.222s, table=3, n_packets=45, n_bytes=5670, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:60:5d:16:04:78,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x476e225, duration=36.448s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:60:5d:16:04:78,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x3463e94a, duration=31.647s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:12:30:31:09:40,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x6c58f4c0, duration=40.222s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:12:30:31:09:40,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x2fea1af4, duration=30.646s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:12:30:31:09:40,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x370d639e, duration=25.845s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:5f:7c:5b:69:7d,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x6bf92138, duration=40.222s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:5f:7c:5b:69:7d,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x2a2d8b4c, duration=24.843s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:5f:7c:5b:69:7d,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x28902918, duration=20.043s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:25:7d:0a:3b:1f,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x663c2e34, duration=40.222s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:25:7d:0a:3b:1f,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x500b9a9c, duration=19.042s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:25:7d:0a:3b:1f,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x1fd5d894, duration=40.222s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x3749388c, duration=40.222s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x8dc6130, duration=40.222s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x4b181dab, duration=40.222s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x6bfc0846, duration=40.222s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

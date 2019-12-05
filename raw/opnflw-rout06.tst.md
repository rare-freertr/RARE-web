# Example: openflow: mldp routing

## **Topology diagram**

![topology](/img/opnflw-rout06.tst.png)

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
 macaddr 005d.364e.152f
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 multicast mldp-enable
 ipv6 address 1234:1::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 no description
 mtu 1500
 macaddr 0079.383d.531d
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 multicast mldp-enable
 ipv6 address 1234:2::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 0003.2a6a.4879
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv4 multicast mldp-enable
 ipv6 address 1234:3::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 0005.4737.0910
 vrf forwarding v1
 ipv4 address 1.1.4.1 255.255.255.0
 ipv4 multicast mldp-enable
 ipv6 address 1234:4::1 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
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
 ipv4 multicast mldp-enable
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
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
 ipv4 multicast mldp-enable
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
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
 ipv4 multicast mldp-enable
 ipv6 address 1234:3::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
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
 ipv4 multicast mldp-enable
 ipv6 address 1234:4::2 ffff:ffff::
 ipv6 multicast mldp-enable
 mpls enable
 mpls ldp4
 mpls ldp6
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 40423 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=1052021032,type=all,bucket=actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,load:0xebf26->OXM_OF_MPLS_LABEL[],output:ens5,bucket=actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,load:0xc72f3->OXM_OF_MPLS_LABEL[],output:ens6,bucket=actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,load:0xf0028->OXM_OF_MPLS_LABEL[],output:ens7
 group_id=113692682,type=all,bucket=actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,load:0x6ca42->OXM_OF_MPLS_LABEL[],output:ens5,bucket=actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,load:0xc0629->OXM_OF_MPLS_LABEL[],output:ens6,bucket=actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,load:0x84cb->OXM_OF_MPLS_LABEL[],output:ens7
 cookie=0x6e387705, duration=19.967s, table=0, n_packets=86, n_bytes=8898, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x19cc7a88, duration=19.967s, table=0, n_packets=0, n_bytes=0, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x7cfdfc1, duration=19.967s, table=0, n_packets=83, n_bytes=10184, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x5b08c098, duration=19.967s, table=0, n_packets=10, n_bytes=1200, priority=1,mpls,in_port=ens4 actions=resubmit(,1)
 cookie=0x47420486, duration=19.966s, table=0, n_packets=87, n_bytes=9051, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x1fc41e40, duration=19.966s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x36744b10, duration=19.966s, table=0, n_packets=87, n_bytes=10835, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x317d4aa8, duration=19.966s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens5 actions=resubmit(,1)
 cookie=0x5f2f7e5f, duration=19.966s, table=0, n_packets=88, n_bytes=9111, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x16f832ae, duration=19.966s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x1599541c, duration=19.966s, table=0, n_packets=87, n_bytes=10839, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x5b4f2290, duration=19.966s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens6 actions=resubmit(,1)
 cookie=0x70fe6434, duration=19.966s, table=0, n_packets=85, n_bytes=8937, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0xcebfac3, duration=19.966s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x506e45cd, duration=19.966s, table=0, n_packets=87, n_bytes=10835, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0xbd54760, duration=19.966s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens7 actions=resubmit(,1)
 cookie=0x36ff7bca, duration=19.966s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x797602d9, duration=19.966s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x49fb4808, duration=19.966s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x7e420199, duration=19.966s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x1535699, duration=19.967s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x6b55abcf, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x8880fc2, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x200e301b, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=382059,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x5d743103, duration=19.965s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=729986,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x66342558, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=315594 actions=CONTROLLER:65535
 cookie=0xfe9fa, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=469853 actions=CONTROLLER:65535
 cookie=0x5580d372, duration=16.661s, table=1, n_packets=5, n_bytes=650, priority=1,mpls,mpls_label=46966 actions=group:1052021032
 cookie=0x1f6021d3, duration=13.040s, table=1, n_packets=5, n_bytes=550, priority=1,mpls,mpls_label=986040 actions=group:113692682
 cookie=0x44d67e4e, duration=19.966s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x32e026ca, duration=19.965s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:5d:36:4e:15:2f,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x1b443508, duration=19.965s, table=2, n_packets=16, n_bytes=1478, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x238124b3, duration=19.965s, table=2, n_packets=12, n_bytes=1101, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x11c0eada, duration=19.965s, table=2, n_packets=13, n_bytes=1161, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x4c9452f4, duration=19.965s, table=2, n_packets=10, n_bytes=987, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x55c3b876, duration=19.965s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x30d1eb4a, duration=19.965s, table=2, n_packets=45, n_bytes=4770, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:5d:36:4e:15:2f,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x107910dd, duration=19.953s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x2bc129b7, duration=19.965s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x508c6f8, duration=19.715s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x486a168b, duration=19.965s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x3ecd5d79, duration=17.249s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x6206cffc, duration=19.964s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x1ee5493a, duration=19.965s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x54ac9280, duration=19.965s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x248697a3, duration=19.965s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x21ef62c3, duration=19.965s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x31f15418, duration=19.965s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x7e448b2a, duration=19.964s, table=3, n_packets=12, n_bytes=1278, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x2d743080, duration=19.964s, table=3, n_packets=11, n_bytes=1299, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x30c0f7f0, duration=19.964s, table=3, n_packets=11, n_bytes=1303, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x385289c6, duration=19.964s, table=3, n_packets=11, n_bytes=1299, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x58d785ce, duration=19.964s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x5eb954d8, duration=19.964s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::203:2aff:fe6a:4879 actions=CONTROLLER:65535
 cookie=0x3228c41d, duration=19.964s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::205:47ff:fe37:910 actions=CONTROLLER:65535
 cookie=0xabff8f3, duration=19.964s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::25d:36ff:fe4e:152f actions=CONTROLLER:65535
 cookie=0x7c31486a, duration=19.964s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::279:38ff:fe3d:531d actions=CONTROLLER:65535
 cookie=0x15b9d53d, duration=19.280s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:5d:36:4e:15:2f,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x1280162f, duration=18.829s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0xfeb9a67, duration=18.671s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x57ac820f, duration=18.277s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:5d:36:4e:15:2f,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x781d581e, duration=19.964s, table=3, n_packets=45, n_bytes=5670, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:5d:36:4e:15:2f,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0xbbabb3f, duration=17.828s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x3c524cf1, duration=19.964s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:03:2a:6a:48:79,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x36d79ba1, duration=17.676s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x65acb1b3, duration=17.669s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x63b656d0, duration=19.964s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:79:38:3d:53:1d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x2d58e2ad, duration=16.673s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x4c2b3576, duration=19.964s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:05:47:37:09:10,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0xc823fb2, duration=19.964s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x34d923e6, duration=19.964s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x4ce7349f, duration=19.964s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x638992c6, duration=19.964s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x476db944, duration=19.964s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

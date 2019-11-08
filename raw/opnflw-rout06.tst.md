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
 macaddr 0012.160d.7d25
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
 macaddr 0026.1607.2861
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
 macaddr 0025.2610.210f
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
 macaddr 0079.193c.332a
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 52064 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=1313175679,type=all,bucket=actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,load:0xe3abe->OXM_OF_MPLS_LABEL[],output:ens5,bucket=actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,load:0x867a3->OXM_OF_MPLS_LABEL[],output:ens6,bucket=actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,load:0x7b3d6->OXM_OF_MPLS_LABEL[],output:ens7
 group_id=574663665,type=all,bucket=actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,load:0x8893b->OXM_OF_MPLS_LABEL[],output:ens5,bucket=actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,load:0xca0b5->OXM_OF_MPLS_LABEL[],output:ens6,bucket=actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,load:0x2d422->OXM_OF_MPLS_LABEL[],output:ens7
 cookie=0x44367008, duration=26.329s, table=0, n_packets=81, n_bytes=8414, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x2dfd16a7, duration=26.329s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x7e97a0dd, duration=26.329s, table=0, n_packets=84, n_bytes=10410, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x1e3159e5, duration=26.329s, table=0, n_packets=6, n_bytes=680, priority=1,mpls,in_port=ens4 actions=resubmit(,1)
 cookie=0x6d4c25d1, duration=26.329s, table=0, n_packets=87, n_bytes=9110, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x567a2e83, duration=26.329s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x382e2971, duration=26.329s, table=0, n_packets=82, n_bytes=10205, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x37ff913a, duration=26.328s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens5 actions=resubmit(,1)
 cookie=0x1865aad7, duration=26.328s, table=0, n_packets=85, n_bytes=8937, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x186f0651, duration=26.327s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x762ce8c4, duration=26.327s, table=0, n_packets=82, n_bytes=10205, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x7c8b230a, duration=26.327s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens6 actions=resubmit(,1)
 cookie=0x57f8459, duration=26.327s, table=0, n_packets=89, n_bytes=9361, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x7d8f6a15, duration=26.327s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x4d1f65f5, duration=26.327s, table=0, n_packets=81, n_bytes=10131, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x10b7f69d, duration=26.327s, table=0, n_packets=0, n_bytes=0, priority=1,mpls,in_port=ens7 actions=resubmit(,1)
 cookie=0x3bfbc001, duration=26.327s, table=0, n_packets=13, n_bytes=1190, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x58ab0edc, duration=26.327s, table=0, n_packets=13, n_bytes=1190, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x36157ed7, duration=26.327s, table=0, n_packets=13, n_bytes=1190, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x3388a2a8, duration=26.327s, table=0, n_packets=13, n_bytes=1190, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x1a7f2b5c, duration=26.329s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x6a2d95cc, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x1517abc, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x5b6c2ffc, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=162634,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x4dcab15d, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=655920,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x39308a5d, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=875552 actions=CONTROLLER:65535
 cookie=0x28276b31, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=941506 actions=CONTROLLER:65535
 cookie=0x5b1f785a, duration=19.802s, table=1, n_packets=1, n_bytes=130, priority=1,mpls,mpls_label=1025206 actions=group:1313175679
 cookie=0x33158559, duration=16.859s, table=1, n_packets=5, n_bytes=550, priority=1,mpls,mpls_label=401316 actions=group:574663665
 cookie=0x720fdcf3, duration=26.325s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x51c131c7, duration=26.324s, table=2, n_packets=11, n_bytes=994, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x477b4644, duration=26.324s, table=2, n_packets=12, n_bytes=1160, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x54bdffa6, duration=26.324s, table=2, n_packets=10, n_bytes=987, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x6c511d3a, duration=26.324s, table=2, n_packets=14, n_bytes=1411, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x58c72505, duration=26.324s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x7927894c, duration=25.457s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:12:16:0d:7d:25,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0xbbd2774, duration=26.324s, table=2, n_packets=45, n_bytes=4770, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:12:16:0d:7d:25,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x307699e0, duration=21.710s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x64428644, duration=26.324s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x11ed8462, duration=20.031s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x3296d91, duration=26.324s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x72b5b1d7, duration=19.056s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x23e0fb95, duration=26.324s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x609073d2, duration=26.324s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x65eb63d, duration=26.324s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x6815f514, duration=26.324s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x6326ac58, duration=26.324s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x5286cdc0, duration=26.325s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x410ddee9, duration=26.324s, table=3, n_packets=13, n_bytes=1504, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x4c0639fe, duration=26.323s, table=3, n_packets=11, n_bytes=1299, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x4313b849, duration=26.323s, table=3, n_packets=11, n_bytes=1299, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0xcedfd20, duration=26.323s, table=3, n_packets=10, n_bytes=1225, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x77dc55f0, duration=26.323s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x132b7369, duration=26.323s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::212:16ff:fe0d:7d25 actions=CONTROLLER:65535
 cookie=0x74826a40, duration=26.323s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::225:26ff:fe10:210f actions=CONTROLLER:65535
 cookie=0x34ce0746, duration=26.323s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::226:16ff:fe07:2861 actions=CONTROLLER:65535
 cookie=0x4f51d57d, duration=26.323s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::279:19ff:fe3c:332a actions=CONTROLLER:65535
 cookie=0x3885ee72, duration=23.255s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:12:16:0d:7d:25,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x1ecb04c, duration=26.323s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:12:16:0d:7d:25,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x5e636cf2, duration=22.255s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:12:16:0d:7d:25,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x517d6ec9, duration=21.809s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x35e08b77, duration=21.205s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x5837fb36, duration=20.824s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x218b86ba, duration=20.807s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0xf0c8a60, duration=26.323s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:79:19:3c:33:2a,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x1ccf3430, duration=20.202s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x2ec3972f, duration=26.323s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:26:16:07:28:61,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0xf2a21be, duration=19.823s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x1369a7cd, duration=26.323s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:25:26:10:21:0f,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x120c104, duration=26.324s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x7b73f95f, duration=26.323s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x1ac4a78, duration=26.323s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x2e22d073, duration=26.323s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x50a0d115, duration=26.324s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

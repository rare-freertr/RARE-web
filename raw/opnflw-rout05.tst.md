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
 macaddr 0005.394c.037a
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
 macaddr 0051.721a.2e7d
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
 macaddr 005c.6e3d.5e58
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
 macaddr 0068.2c41.3563
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 42833 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=366228468,type=all,bucket=actions=mod_dl_src:00:51:72:1a:2e:7d,output:ens5,bucket=actions=mod_dl_src:00:5c:6e:3d:5e:58,output:ens6,bucket=actions=mod_dl_src:00:68:2c:41:35:63,output:ens7
 group_id=1696664133,type=all,bucket=actions=mod_dl_src:00:51:72:1a:2e:7d,output:ens5,bucket=actions=mod_dl_src:00:5c:6e:3d:5e:58,output:ens6,bucket=actions=mod_dl_src:00:68:2c:41:35:63,output:ens7
 cookie=0x2bfa78df, duration=39.122s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x7a9ac2af, duration=39.122s, table=0, n_packets=0, n_bytes=0, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x6f50780, duration=39.122s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x6c990a, duration=39.122s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x28a7c0bc, duration=39.122s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x6e96466f, duration=39.122s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x7bf98aff, duration=39.122s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x7ed83242, duration=39.122s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x2df7b2b6, duration=39.122s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x68cd1a78, duration=39.122s, table=0, n_packets=84, n_bytes=8904, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0xd6f5c0a, duration=39.122s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x182cdc1f, duration=39.121s, table=0, n_packets=84, n_bytes=10544, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x775a5783, duration=39.121s, table=0, n_packets=5, n_bytes=530, priority=3,ip,in_port=ens4,nw_src=2.2.2.103,nw_dst=232.2.2.2 actions=group:1696664133
 cookie=0x5458ecdf, duration=39.121s, table=0, n_packets=5, n_bytes=630, priority=3,ipv6,in_port=ens4,ipv6_src=4321::103,ipv6_dst=ff06::1 actions=group:366228468
 cookie=0x7b8f6cb2, duration=39.121s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x2ed8b160, duration=39.121s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x6f98a666, duration=39.121s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0xcdd41a3, duration=39.121s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x449662d3, duration=39.122s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x252c8226, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x11d820d5, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x2a4b0bbb, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=267457,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x143627b9, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=828704,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x329df974, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=577323 actions=CONTROLLER:65535
 cookie=0x19ab6270, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=620809 actions=CONTROLLER:65535
 cookie=0x361ad3b0, duration=39.121s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x72dfb8b0, duration=39.121s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:05:39:4c:03:7a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x311d2ef5, duration=39.121s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x2a9e263b, duration=39.121s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x15d8298, duration=39.121s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x22cf7bec, duration=39.121s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x2c3ba017, duration=39.121s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x209d53a3, duration=39.121s, table=2, n_packets=45, n_bytes=4770, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:05:39:4c:03:7a,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x17cdb89d, duration=33.660s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:51:72:1a:2e:7d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x30990667, duration=39.121s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:51:72:1a:2e:7d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0xb8ae867, duration=27.858s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:5c:6e:3d:5e:58,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x38d66d56, duration=39.121s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:5c:6e:3d:5e:58,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x12779c46, duration=22.056s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:68:2c:41:35:63,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x79604fa8, duration=39.119s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:68:2c:41:35:63,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x22ef950c, duration=39.121s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x428a69ba, duration=39.121s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x7c016c8e, duration=39.121s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x7822acf1, duration=39.121s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x75c1577d, duration=39.121s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x55077fe1, duration=39.119s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x79a48882, duration=39.119s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x143a4fe4, duration=39.119s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x12047665, duration=39.119s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x23180a84, duration=39.119s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x437b5a8a, duration=39.119s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::205:39ff:fe4c:37a actions=CONTROLLER:65535
 cookie=0x30cbc8ad, duration=39.119s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::251:72ff:fe1a:2e7d actions=CONTROLLER:65535
 cookie=0x170b27a5, duration=39.119s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::25c:6eff:fe3d:5e58 actions=CONTROLLER:65535
 cookie=0x22ffaf87, duration=39.119s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::268:2cff:fe41:3563 actions=CONTROLLER:65535
 cookie=0x58d0905f, duration=37.062s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:05:39:4c:03:7a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0xa986b58, duration=39.119s, table=3, n_packets=45, n_bytes=5670, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:05:39:4c:03:7a,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x3e0a52fb, duration=36.061s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:05:39:4c:03:7a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x21b44842, duration=31.260s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:51:72:1a:2e:7d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x2ce324d7, duration=39.119s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:51:72:1a:2e:7d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x3d360cfe, duration=30.259s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:51:72:1a:2e:7d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x3c8099c5, duration=25.458s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:5c:6e:3d:5e:58,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x79ebc985, duration=39.119s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:5c:6e:3d:5e:58,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x6c02a593, duration=24.457s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:5c:6e:3d:5e:58,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x40838ec1, duration=19.655s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:68:2c:41:35:63,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x44ae87c6, duration=39.119s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:68:2c:41:35:63,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x6514db90, duration=18.654s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:68:2c:41:35:63,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x688f0898, duration=39.119s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x70ff7d47, duration=39.119s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x14fbd98a, duration=39.119s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x70861f19, duration=39.119s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x7be372ad, duration=39.119s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

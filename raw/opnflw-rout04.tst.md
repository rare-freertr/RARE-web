# Example: openflow: mpls routing

## **Topology diagram**

![topology](/img/opnflw-rout04.tst.png)

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
 label-mode per-prefix
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
 macaddr 0036.271d.676a
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234:1::1 ffff:ffff::
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
 macaddr 0048.6978.5072
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1234:2::1 ffff:ffff::
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
 macaddr 001d.771a.1a2f
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1234:3::1 ffff:ffff::
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
 macaddr 0049.282f.577c
 vrf forwarding v1
 ipv4 address 1.1.4.1 255.255.255.0
 ipv6 address 1234:4::1 ffff:ffff::
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
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv4 access-group-in test4
 ipv6 address 1234:1::2 ffff:ffff::
 ipv6 access-group-in test6
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
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv4 access-group-in test4
 ipv6 address 1234:2::2 ffff:ffff::
 ipv6 access-group-in test6
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
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv4 access-group-in test4
 ipv6 address 1234:3::2 ffff:ffff::
 ipv6 access-group-in test6
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
access-list test4
 sequence 10 deny 1 any all any all
 sequence 20 permit all any all any all
 exit
!
access-list test6
 sequence 10 deny all 4321:: ffff:: all 4321:: ffff:: all
 sequence 20 permit all any all any all
 exit
!
vrf definition v1
 rd 1:1
 label-mode per-prefix
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
 ipv4 access-group-in test4
 ipv6 address 1234:4::2 ffff:ffff::
 ipv6 access-group-in test6
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 60928 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 cookie=0xb865091, duration=25.182s, table=0, n_packets=31, n_bytes=3805, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x665fd98, duration=25.182s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x63164b99, duration=25.182s, table=0, n_packets=20, n_bytes=2392, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x4d2f92e7, duration=25.182s, table=0, n_packets=82, n_bytes=9820, priority=1,mpls,in_port=ens4 actions=resubmit(,1)
 cookie=0x108386eb, duration=25.181s, table=0, n_packets=26, n_bytes=3403, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x5f032f76, duration=25.181s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x4d0f836f, duration=25.181s, table=0, n_packets=19, n_bytes=2732, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x74d314eb, duration=25.181s, table=0, n_packets=81, n_bytes=9710, priority=1,mpls,in_port=ens5 actions=resubmit(,1)
 cookie=0x5c429222, duration=25.181s, table=0, n_packets=17, n_bytes=1727, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x54d65811, duration=25.181s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x1c76a75e, duration=25.181s, table=0, n_packets=19, n_bytes=2694, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x57bcaa29, duration=25.181s, table=0, n_packets=80, n_bytes=9600, priority=1,mpls,in_port=ens6 actions=resubmit(,1)
 cookie=0x50278279, duration=25.181s, table=0, n_packets=19, n_bytes=1829, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x2e329740, duration=25.181s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x3d38d17, duration=25.181s, table=0, n_packets=21, n_bytes=2538, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x3f18fc17, duration=25.181s, table=0, n_packets=80, n_bytes=9600, priority=1,mpls,in_port=ens7 actions=resubmit(,1)
 cookie=0xbc79dd8, duration=25.180s, table=0, n_packets=11, n_bytes=1006, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x57bb7863, duration=25.180s, table=0, n_packets=11, n_bytes=1006, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x75f856cf, duration=25.180s, table=0, n_packets=11, n_bytes=1006, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x7c339e29, duration=25.180s, table=0, n_packets=11, n_bytes=1006, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0xce62585, duration=25.182s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x24f3d9a7, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x109041a5, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x6a5f5ced, duration=25.179s, table=1, n_packets=43, n_bytes=4730, priority=2,mpls,mpls_label=56073,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x2f9ebad7, duration=25.179s, table=1, n_packets=40, n_bytes=5200, priority=2,mpls,mpls_label=322798,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0xf6fc781, duration=19.071s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=487976,mpls_bos=1 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,load:0x5fbd1->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0xbb97dc5, duration=23.247s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=541270,mpls_bos=1 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,load:0xd5114->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x14f9cb88, duration=21.147s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=918336,mpls_bos=1 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,load:0xbb710->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x3a9eb27b, duration=24.849s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=685060,mpls_bos=1 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,load:0x331c1->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x6dadd66f, duration=22.401s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=319721,mpls_bos=1 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,load:0x5729e->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x8852a40, duration=19.779s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=271015,mpls_bos=1 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,load:0xecaf8->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x1bd9bc98, duration=19.874s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=553217,mpls_bos=1 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,load:0x20509->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x1998d5c, duration=19.259s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=638917,mpls_bos=1 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,load:0xf78e2->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x6192dea7, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=296483 actions=CONTROLLER:65535
 cookie=0x3aaa2a29, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=925500 actions=CONTROLLER:65535
 cookie=0x12299ab9, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=487976 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,load:0x5fbd1->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x101a1a77, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=541270 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,load:0xd5114->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x72d24cd6, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=918336 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,load:0xbb710->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x20674d02, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=685060 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,load:0x331c1->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x7ff5fb9c, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=319721 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,load:0x5729e->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x6348815b, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=271015 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,load:0xecaf8->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x63dc8b02, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=553217 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,load:0x20509->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0xe899fde, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=638917 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,load:0xf78e2->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x6337f5a, duration=25.179s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x53fd2223, duration=25.178s, table=2, n_packets=24, n_bytes=2867, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x625af8fd, duration=25.178s, table=2, n_packets=22, n_bytes=2867, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x49804c5a, duration=25.178s, table=2, n_packets=17, n_bytes=1727, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x797ef0a2, duration=25.178s, table=2, n_packets=19, n_bytes=1829, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x41cbe28, duration=25.178s, table=2, n_packets=54, n_bytes=6032, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x1ec68af4, duration=24.847s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x731a731b, duration=23.247s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x63690e4c, duration=19.873s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x6b6fa898, duration=19.779s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x6c826f5e, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,push_mpls:0x8847,load:0xecaf8->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens6
 cookie=0x148246, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,push_mpls:0x8847,load:0xd5114->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens7
 cookie=0x12c29f6a, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,push_mpls:0x8847,load:0x331c1->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens4
 cookie=0x6ae1a436, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,push_mpls:0x8847,load:0x20509->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens5
 cookie=0x5169f6af, duration=25.180s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x455a0b04, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x2b9eb659, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x734f4eb6, duration=25.179s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x74886e2d, duration=25.180s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x3650b4b0, duration=25.179s, table=3, n_packets=19, n_bytes=2306, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x450077db, duration=25.178s, table=3, n_packets=18, n_bytes=2646, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x70831ff2, duration=25.178s, table=3, n_packets=18, n_bytes=2608, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x41af1bcd, duration=25.178s, table=3, n_packets=20, n_bytes=2452, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x26214b80, duration=25.178s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x2cc81fe8, duration=25.178s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::21d:77ff:fe1a:1a2f actions=CONTROLLER:65535
 cookie=0x5df07381, duration=25.178s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::236:27ff:fe1d:676a actions=CONTROLLER:65535
 cookie=0x6341aa94, duration=25.177s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::248:69ff:fe78:5072 actions=CONTROLLER:65535
 cookie=0x45bfa7d, duration=25.177s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::249:28ff:fe2f:577c actions=CONTROLLER:65535
 cookie=0x6ae6eefa, duration=23.404s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0xeb61be8, duration=22.401s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x1ecb1add, duration=22.150s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x4c2e5db3, duration=21.147s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x11275646, duration=20.261s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x433cad8e, duration=20.076s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x4dcd48d3, duration=19.259s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x2320c131, duration=19.072s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x7f040256, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:49:28:2f:57:7c,mod_dl_dst:00:00:00:00:66:66,push_mpls:0x8847,load:0x5fbd1->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens7
 cookie=0x119efeeb, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:36:27:1d:67:6a,mod_dl_dst:00:00:00:00:33:33,push_mpls:0x8847,load:0xbb710->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens4
 cookie=0x1f99c75c, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:1d:77:1a:1a:2f,mod_dl_dst:00:00:00:00:55:55,push_mpls:0x8847,load:0x5729e->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens6
 cookie=0x3db497, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:48:69:78:50:72,mod_dl_dst:00:00:00:00:44:44,push_mpls:0x8847,load:0xf78e2->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens5
 cookie=0x4ece0824, duration=25.179s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x6dc1945f, duration=25.179s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x7003abf2, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x1fe3752a, duration=25.178s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x59e8c28c, duration=25.179s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

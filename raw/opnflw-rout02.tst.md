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
 macaddr 003d.4062.506b
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn2
 no description
 mtu 1500
 macaddr 005b.5103.4922
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 0032.287b.322a
 bridge-group 1
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 007e.5d31.3617
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 43509 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 group_id=1750280183,type=all,bucket=actions=output:ens4,bucket=actions=output:ens5,bucket=actions=output:ens6
 cookie=0x1875eccd, duration=49.101s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x5f999af7, duration=49.101s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x657be2a1, duration=49.101s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x41bee8ff, duration=49.101s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x67482cc5, duration=49.101s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x3184b6f1, duration=49.100s, table=0, n_packets=3, n_bytes=258, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0xa302f5b, duration=49.100s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x5003f966, duration=49.101s, table=0, n_packets=39, n_bytes=4134, priority=2,ip,in_port=ens4,dl_dst=00:23:6e:55:05:4f actions=resubmit(,2)
 cookie=0x5e001b4f, duration=49.101s, table=0, n_packets=0, n_bytes=0, priority=2,arp,in_port=ens4,dl_dst=00:23:6e:55:05:4f actions=CONTROLLER:65535
 cookie=0x46badd4d, duration=49.101s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens4,dl_dst=00:23:6e:55:05:4f actions=resubmit(,3)
 cookie=0x2b2c19ec, duration=49.101s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens4,dl_dst=00:23:6e:55:05:4f actions=resubmit(,1)
 cookie=0x535db3cf, duration=49.100s, table=0, n_packets=39, n_bytes=4134, priority=2,ip,in_port=ens5,dl_dst=00:23:6e:55:05:4f actions=resubmit(,2)
 cookie=0x78eb5a32, duration=49.100s, table=0, n_packets=1, n_bytes=60, priority=2,arp,in_port=ens5,dl_dst=00:23:6e:55:05:4f actions=CONTROLLER:65535
 cookie=0x3f099e47, duration=49.100s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens5,dl_dst=00:23:6e:55:05:4f actions=resubmit(,3)
 cookie=0xb535ec7, duration=49.100s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens5,dl_dst=00:23:6e:55:05:4f actions=resubmit(,1)
 cookie=0x4f4ec3d9, duration=49.100s, table=0, n_packets=39, n_bytes=4134, priority=2,ip,in_port=ens6,dl_dst=00:23:6e:55:05:4f actions=resubmit(,2)
 cookie=0x3b475f2e, duration=49.100s, table=0, n_packets=1, n_bytes=60, priority=2,arp,in_port=ens6,dl_dst=00:23:6e:55:05:4f actions=CONTROLLER:65535
 cookie=0x6c2a375e, duration=49.100s, table=0, n_packets=39, n_bytes=4874, priority=2,ipv6,in_port=ens6,dl_dst=00:23:6e:55:05:4f actions=resubmit(,3)
 cookie=0x489e30b0, duration=49.100s, table=0, n_packets=0, n_bytes=0, priority=2,mpls,in_port=ens6,dl_dst=00:23:6e:55:05:4f actions=resubmit(,1)
 cookie=0x5e865a21, duration=49.101s, table=0, n_packets=90, n_bytes=10460, priority=1,in_port=ens4 actions=group:1750280183
 cookie=0x5ee7e961, duration=49.101s, table=0, n_packets=89, n_bytes=10334, priority=1,in_port=ens5 actions=group:1750280183
 cookie=0x46a5a0a5, duration=49.101s, table=0, n_packets=88, n_bytes=10208, priority=1,in_port=ens6 actions=group:1750280183
 cookie=0x4c8823e8, duration=49.101s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x13a62081, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x2e0828e0, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x228d44b4, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=284045,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x3a0db462, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=673150,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x1e32faee, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=386348 actions=CONTROLLER:65535
 cookie=0x5756fd33, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=499050 actions=CONTROLLER:65535
 cookie=0x12b2791f, duration=49.100s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x5358e944, duration=49.100s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:33:33,group:1750280183
 cookie=0x3e681170, duration=49.100s, table=2, n_packets=27, n_bytes=2862, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x459d471, duration=49.099s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x48cba302, duration=49.099s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x5f033c18, duration=49.099s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:33:33,dec_ttl,group:1750280183
 cookie=0x644cd543, duration=43.468s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.3 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:44:44,group:1750280183
 cookie=0x8da5fed, duration=49.099s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:44:44,dec_ttl,group:1750280183
 cookie=0x19c52b01, duration=37.666s, table=2, n_packets=10, n_bytes=1060, priority=300,ip,nw_dst=1.1.1.4 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:55:55,group:1750280183
 cookie=0x1d47c9df, duration=49.099s, table=2, n_packets=10, n_bytes=1060, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:55:55,dec_ttl,group:1750280183
 cookie=0x42e3df0f, duration=31.863s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:7e:5d:31:36:17,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x302cca23, duration=49.099s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:7e:5d:31:36:17,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x74a36b0c, duration=49.100s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x4c2dead8, duration=49.100s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x9fa255f, duration=49.100s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x72d7f8df, duration=49.098s, table=3, n_packets=24, n_bytes=3024, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x7891651b, duration=49.098s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x4309be5f, duration=49.098s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x6fc40e01, duration=49.098s, table=3, n_packets=3, n_bytes=258, priority=228,ipv6,ipv6_dst=fe80::223:6eff:fe55:54f actions=CONTROLLER:65535
 cookie=0x1d4fdf3c, duration=49.098s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::27e:5dff:fe31:3617 actions=CONTROLLER:65535
 cookie=0x620d4329, duration=46.868s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:33:33,group:1750280183
 cookie=0x18e05b0b, duration=49.098s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:33:33,dec_ttl,group:1750280183
 cookie=0x4ca97ee4, duration=45.867s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:33:33,group:1750280183
 cookie=0x74f009cd, duration=41.067s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::3 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:44:44,group:1750280183
 cookie=0x70da6121, duration=49.098s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:44:44,dec_ttl,group:1750280183
 cookie=0x371de7d0, duration=40.065s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:44:44,group:1750280183
 cookie=0x3f9a07ff, duration=35.264s, table=3, n_packets=10, n_bytes=1260, priority=300,ipv6,ipv6_dst=1234:1::4 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:55:55,group:1750280183
 cookie=0x7f4c265d, duration=49.098s, table=3, n_packets=10, n_bytes=1260, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:55:55,dec_ttl,group:1750280183
 cookie=0x5679302d, duration=34.263s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:23:6e:55:05:4f,mod_dl_dst:00:00:00:00:55:55,group:1750280183
 cookie=0x1b57c451, duration=29.462s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:7e:5d:31:36:17,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x24cba8b7, duration=49.098s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:7e:5d:31:36:17,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x69f2ce42, duration=28.461s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:7e:5d:31:36:17,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x24ff0b04, duration=49.098s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0xd3bd0da, duration=49.098s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x4feebda7, duration=49.099s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

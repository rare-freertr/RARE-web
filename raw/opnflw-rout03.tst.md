# Example: openflow: ip routing

## **Topology diagram**

![topology](/img/opnflw-rout03.tst.png)

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
 macaddr 0042.4100.1458
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
 macaddr 0019.5a54.7b0a
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv6 address 1234:2::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface sdn3
 no description
 mtu 1500
 macaddr 0027.6542.393c
 vrf forwarding v1
 ipv4 address 1.1.3.1 255.255.255.0
 ipv6 address 1234:3::1 ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface sdn4
 no description
 mtu 1500
 macaddr 0017.541d.3a3c
 vrf forwarding v1
 ipv4 address 1.1.4.1 255.255.255.0
 ipv6 address 1234:4::1 ffff:ffff::
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
 ipv6 address 1234:1::2 ffff:ffff::
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 34523 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 cookie=0x5f32a83f, duration=39.336s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x4894a02b, duration=39.336s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x1abbda8b, duration=39.336s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x1f5f4821, duration=39.336s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x2042e2cf, duration=39.336s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x4fe443bd, duration=39.336s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x24fd5853, duration=39.336s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x5c661f69, duration=39.336s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x25400387, duration=39.336s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0xc6ee8f, duration=39.336s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x5f8b7a66, duration=39.336s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x57e214f2, duration=39.336s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x356e94ca, duration=39.336s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x5b17eed9, duration=39.336s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x3677a342, duration=39.336s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x42453204, duration=39.336s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x1f909758, duration=39.336s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x727817b5, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x3e4160e9, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x5fff2faf, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=80531,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x4303afcb, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=146622,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x2e929b74, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=375018 actions=CONTROLLER:65535
 cookie=0x418dd2d7, duration=39.335s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=423977 actions=CONTROLLER:65535
 cookie=0x1bd17679, duration=39.336s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x6386b71, duration=39.335s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x2d456997, duration=39.334s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x2f8404b6, duration=39.334s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x7ccc3f7d, duration=39.334s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x68a6ea1d, duration=39.334s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x100eb688, duration=38.851s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:42:41:00:14:58,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x7d54805, duration=39.334s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:42:41:00:14:58,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x39d80ee9, duration=33.048s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:19:5a:54:7b:0a,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x25aefc48, duration=39.334s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:19:5a:54:7b:0a,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0xafc3e4b, duration=27.247s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:27:65:42:39:3c,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x20fe592, duration=39.334s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:27:65:42:39:3c,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x10d87736, duration=21.445s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:17:54:1d:3a:3c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x3c7325e1, duration=39.334s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:17:54:1d:3a:3c,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x4d783fc, duration=39.335s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x5657a12f, duration=39.335s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x313055f4, duration=39.334s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x633d95d9, duration=39.334s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x3f85487a, duration=39.335s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x33870b0d, duration=39.334s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x75c6cda1, duration=39.334s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x4c2bb7f8, duration=39.334s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x7b305746, duration=39.334s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x7cdf7838, duration=39.334s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x4813dbc4, duration=39.333s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::217:54ff:fe1d:3a3c actions=CONTROLLER:65535
 cookie=0x35cb2a0e, duration=39.333s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::219:5aff:fe54:7b0a actions=CONTROLLER:65535
 cookie=0x7fade74c, duration=39.333s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::227:65ff:fe42:393c actions=CONTROLLER:65535
 cookie=0x469d1362, duration=39.333s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::242:41ff:fe00:1458 actions=CONTROLLER:65535
 cookie=0x1e4490ad, duration=36.450s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:42:41:00:14:58,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x10fd1257, duration=39.334s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:42:41:00:14:58,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x4f383058, duration=35.449s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:42:41:00:14:58,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x17302e52, duration=30.649s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:19:5a:54:7b:0a,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x65aed3e6, duration=39.334s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:19:5a:54:7b:0a,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x64b87c10, duration=29.648s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:19:5a:54:7b:0a,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x7b882503, duration=24.846s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:27:65:42:39:3c,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x3a694c68, duration=39.334s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:27:65:42:39:3c,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x2946e31c, duration=23.845s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:27:65:42:39:3c,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x74172bc3, duration=19.044s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:17:54:1d:3a:3c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x2d736456, duration=39.333s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:17:54:1d:3a:3c,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x6d73f46a, duration=18.043s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:17:54:1d:3a:3c,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0xa40c79e, duration=39.334s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x3693bde0, duration=39.334s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x1c87150a, duration=39.334s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x6104dcd, duration=39.334s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x5c650eed, duration=39.334s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

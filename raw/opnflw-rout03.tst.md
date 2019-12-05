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
 macaddr 006f.7051.3200
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
 macaddr 003a.4446.171d
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
 macaddr 004c.7746.7213
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
 macaddr 0039.7d52.255d
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 34356 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 cookie=0x2162f35d, duration=39.155s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x61754258, duration=39.155s, table=0, n_packets=0, n_bytes=0, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x25ce8be, duration=39.155s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x32e01be0, duration=39.155s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x6d0c1f35, duration=39.155s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x6aff8b3e, duration=39.155s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x723fafe1, duration=39.155s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x6715582f, duration=39.155s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x2bb5ad81, duration=39.154s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0xc7926a4, duration=39.154s, table=0, n_packets=79, n_bytes=8374, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x108e27ce, duration=39.154s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x7cd3986b, duration=39.154s, table=0, n_packets=79, n_bytes=9914, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x7ab257fe, duration=39.154s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x6d5948fc, duration=39.154s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x4c4fb94, duration=39.154s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x32864f7, duration=39.154s, table=0, n_packets=1, n_bytes=86, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x41ca8f34, duration=39.155s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x2a690451, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x37ecfa8a, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0xcbae7d1, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=79354,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x55e775e8, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=434234,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x7aeebdc4, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=337644 actions=CONTROLLER:65535
 cookie=0x591ce1b6, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=1035858 actions=CONTROLLER:65535
 cookie=0x42acbdce, duration=39.154s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x68afbb24, duration=39.154s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:6f:70:51:32:00,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x328cef0, duration=39.154s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x743b554c, duration=39.154s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x5efb8df0, duration=39.154s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x4868b80c, duration=39.154s, table=2, n_packets=9, n_bytes=954, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x3e671a6a, duration=39.154s, table=2, n_packets=40, n_bytes=4240, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x7e0de4ac, duration=39.154s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:6f:70:51:32:00,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x631360e1, duration=33.674s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:3a:44:46:17:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x6315e62a, duration=39.154s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:3a:44:46:17:1d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x202e19bb, duration=27.872s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:4c:77:46:72:13,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x4465a7ed, duration=39.154s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:4c:77:46:72:13,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x6cc95c8d, duration=22.069s, table=2, n_packets=30, n_bytes=3180, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:39:7d:52:25:5d,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x76e6c9a1, duration=39.154s, table=2, n_packets=30, n_bytes=3180, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:39:7d:52:25:5d,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x221cbc10, duration=39.154s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x5b047928, duration=39.154s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x3432acff, duration=39.154s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x5f948169, duration=39.154s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x3be55d3e, duration=39.154s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0xfb41d8, duration=39.154s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x42aa4055, duration=39.152s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x7cbdeda4, duration=39.152s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x74ddb8bf, duration=39.152s, table=3, n_packets=8, n_bytes=1008, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x7c3545b0, duration=39.152s, table=3, n_packets=40, n_bytes=5040, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x26389623, duration=39.152s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::239:7dff:fe52:255d actions=CONTROLLER:65535
 cookie=0x55adf480, duration=39.152s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::23a:44ff:fe46:171d actions=CONTROLLER:65535
 cookie=0x7fcbc58, duration=39.152s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::24c:77ff:fe46:7213 actions=CONTROLLER:65535
 cookie=0x6e9ab98f, duration=39.152s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::26f:70ff:fe51:3200 actions=CONTROLLER:65535
 cookie=0x457c920c, duration=37.075s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:6f:70:51:32:00,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x48fea181, duration=39.152s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:6f:70:51:32:00,mod_dl_dst:00:00:00:00:33:33,dec_ttl,output:ens4
 cookie=0x7d878bdb, duration=36.074s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:6f:70:51:32:00,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x902b0de, duration=31.272s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:3a:44:46:17:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x53a0c203, duration=39.152s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:3a:44:46:17:1d,mod_dl_dst:00:00:00:00:44:44,dec_ttl,output:ens5
 cookie=0x205ebe4f, duration=30.272s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:3a:44:46:17:1d,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0xa1009, duration=25.470s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:4c:77:46:72:13,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x1c59a54d, duration=39.152s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:4c:77:46:72:13,mod_dl_dst:00:00:00:00:55:55,dec_ttl,output:ens6
 cookie=0x6bb8579, duration=24.469s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:4c:77:46:72:13,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x4140628, duration=19.668s, table=3, n_packets=30, n_bytes=3780, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:39:7d:52:25:5d,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x75e8cf1c, duration=39.152s, table=3, n_packets=30, n_bytes=3780, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:39:7d:52:25:5d,mod_dl_dst:00:00:00:00:66:66,dec_ttl,output:ens7
 cookie=0x4f664e9e, duration=18.666s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:39:7d:52:25:5d,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x3e5c1524, duration=39.154s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x7f507c5c, duration=39.152s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x65fcc63d, duration=39.152s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x4ae8bfe4, duration=39.152s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x6de3205e, duration=39.154s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

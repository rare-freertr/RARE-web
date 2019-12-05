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
 macaddr 0053.685a.745a
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
 macaddr 0077.052a.3018
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
 macaddr 0001.1601.4f49
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
 macaddr 0077.6f07.7550
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
info prt.prtTcp.connectionRcvd:prtTcp.java:730 got future acknowledge number telnet #10011 57274 -> 10.11.12.111 2323
tcl: - connecting to 10.11.12.111 2323
OFPST_GROUP_DESC reply (OF1.1) (xid=0x2):
 cookie=0x48422679, duration=19.022s, table=0, n_packets=21, n_bytes=2325, priority=1,ip,in_port=ens4 actions=resubmit(,2)
 cookie=0x3805a5d1, duration=19.022s, table=0, n_packets=0, n_bytes=0, priority=3,arp,in_port=ens4 actions=CONTROLLER:65535
 cookie=0x477274d5, duration=19.022s, table=0, n_packets=19, n_bytes=2314, priority=1,ipv6,in_port=ens4 actions=resubmit(,3)
 cookie=0x685ff6cc, duration=19.022s, table=0, n_packets=80, n_bytes=9600, priority=1,mpls,in_port=ens4 actions=resubmit(,1)
 cookie=0x1de2afec, duration=19.022s, table=0, n_packets=18, n_bytes=1849, priority=1,ip,in_port=ens5 actions=resubmit(,2)
 cookie=0x2714cf6f, duration=19.022s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens5 actions=CONTROLLER:65535
 cookie=0x11f8a63e, duration=19.022s, table=0, n_packets=17, n_bytes=2270, priority=1,ipv6,in_port=ens5 actions=resubmit(,3)
 cookie=0x32c2c94f, duration=19.022s, table=0, n_packets=84, n_bytes=10120, priority=1,mpls,in_port=ens5 actions=resubmit(,1)
 cookie=0x7cc9f657, duration=19.022s, table=0, n_packets=22, n_bytes=2009, priority=1,ip,in_port=ens6 actions=resubmit(,2)
 cookie=0x1539e4d1, duration=19.022s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens6 actions=CONTROLLER:65535
 cookie=0x39272f6d, duration=19.021s, table=0, n_packets=20, n_bytes=2588, priority=1,ipv6,in_port=ens6 actions=resubmit(,3)
 cookie=0x7f75d1e7, duration=19.021s, table=0, n_packets=80, n_bytes=9600, priority=1,mpls,in_port=ens6 actions=resubmit(,1)
 cookie=0x5d2228e, duration=19.021s, table=0, n_packets=19, n_bytes=1835, priority=1,ip,in_port=ens7 actions=resubmit(,2)
 cookie=0x5eeb405a, duration=19.021s, table=0, n_packets=1, n_bytes=60, priority=3,arp,in_port=ens7 actions=CONTROLLER:65535
 cookie=0x481f9de4, duration=19.021s, table=0, n_packets=20, n_bytes=2840, priority=1,ipv6,in_port=ens7 actions=resubmit(,3)
 cookie=0x26ef74ad, duration=19.021s, table=0, n_packets=80, n_bytes=9600, priority=1,mpls,in_port=ens7 actions=resubmit(,1)
 cookie=0x343f7d67, duration=19.021s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens4,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x580ec201, duration=19.021s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x1bedb808, duration=19.021s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens6,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x1ce96bd, duration=19.021s, table=0, n_packets=9, n_bytes=822, priority=2,in_port=ens7,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=CONTROLLER:65535
 cookie=0x783d8641, duration=19.022s, table=0, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x6c4d1598, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=0,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x9fb4abf, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=2,mpls,mpls_label=2,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x1b125fd7, duration=19.021s, table=1, n_packets=40, n_bytes=4400, priority=2,mpls,mpls_label=503890,mpls_bos=1 actions=pop_mpls:0x0800,resubmit(,2)
 cookie=0x4afc9f64, duration=19.021s, table=1, n_packets=44, n_bytes=5720, priority=2,mpls,mpls_label=766030,mpls_bos=1 actions=pop_mpls:0x86dd,resubmit(,3)
 cookie=0x3fd3a8f0, duration=16.217s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=282094,mpls_bos=1 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,load:0x4a499->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x4b7e7b5e, duration=16.328s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=421787,mpls_bos=1 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,load:0xaef85->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x322bfabc, duration=14.355s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=625830,mpls_bos=1 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,load:0x2abdf->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x4e02c9fb, duration=15.174s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=343046,mpls_bos=1 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,load:0x93586->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x4d3da32d, duration=16.498s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=621139,mpls_bos=1 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,load:0x5fbe7->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x1793f6eb, duration=19.021s, table=1, n_packets=30, n_bytes=3300, priority=2,mpls,mpls_label=59898,mpls_bos=1 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,load:0x13ba8->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x5af41e63, duration=17.395s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=324819,mpls_bos=1 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,load:0x6c73a->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x4b7236d1, duration=14.710s, table=1, n_packets=30, n_bytes=3900, priority=2,mpls,mpls_label=820095,mpls_bos=1 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,load:0x238ad->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x4e9d82e5, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=290786 actions=CONTROLLER:65535
 cookie=0xecc0209, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=615050 actions=CONTROLLER:65535
 cookie=0x2cf88abf, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=282094 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,load:0x4a499->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x35c6a9d6, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=421787 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,load:0xaef85->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x4d2c05cf, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=625830 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,load:0x2abdf->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens6
 cookie=0x6afafdfc, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=343046 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,load:0x93586->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x6e60e6c0, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=621139 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,load:0x5fbe7->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0xe8e8050, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=59898 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,load:0x13ba8->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens4
 cookie=0x5945b11, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=324819 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,load:0x6c73a->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens5
 cookie=0x5a77c722, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=1,mpls,mpls_label=820095 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,load:0x238ad->OXM_OF_MPLS_LABEL[],dec_mpls_ttl,output:ens7
 cookie=0x77f7e8d, duration=19.021s, table=1, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0xdfabec1, duration=19.021s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.1.2 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x714bf461, duration=19.021s, table=2, n_packets=16, n_bytes=1655, priority=228,ip,nw_dst=1.1.1.1 actions=CONTROLLER:65535
 cookie=0x3a2ba3d7, duration=19.020s, table=2, n_packets=18, n_bytes=1849, priority=228,ip,nw_dst=1.1.2.1 actions=CONTROLLER:65535
 cookie=0x13904b2f, duration=19.020s, table=2, n_packets=22, n_bytes=2009, priority=228,ip,nw_dst=1.1.3.1 actions=CONTROLLER:65535
 cookie=0x3a7eb247, duration=19.020s, table=2, n_packets=19, n_bytes=1835, priority=228,ip,nw_dst=1.1.4.1 actions=CONTROLLER:65535
 cookie=0x75a0386c, duration=19.020s, table=2, n_packets=45, n_bytes=4910, priority=228,ip,nw_dst=2.2.2.101 actions=CONTROLLER:65535
 cookie=0x4d196e0d, duration=16.498s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.2.2 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x4d11c888, duration=16.328s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.3.2 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x59259be, duration=15.174s, table=2, n_packets=0, n_bytes=0, priority=300,ip,nw_dst=1.1.4.2 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x4ef83f61, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.104 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,push_mpls:0x8847,load:0x5fbe7->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens5
 cookie=0x6b5ef06f, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.105 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,push_mpls:0x8847,load:0xaef85->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens6
 cookie=0x2ddfb377, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.106 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,push_mpls:0x8847,load:0x93586->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens7
 cookie=0x5b096fe8, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=228,ip,nw_dst=2.2.2.103 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,push_mpls:0x8847,load:0x13ba8->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens4
 cookie=0x2dd8b856, duration=19.021s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.1.0/24 actions=CONTROLLER:65535
 cookie=0x4ee197d8, duration=19.021s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.2.0/24 actions=CONTROLLER:65535
 cookie=0x5c8c3807, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.3.0/24 actions=CONTROLLER:65535
 cookie=0x4382e1ad, duration=19.020s, table=2, n_packets=0, n_bytes=0, priority=220,ip,nw_dst=1.1.4.0/24 actions=CONTROLLER:65535
 cookie=0x380d5b4e, duration=19.021s, table=2, n_packets=0, n_bytes=0, priority=0 actions=drop
 cookie=0x3be8c938, duration=19.020s, table=3, n_packets=18, n_bytes=2228, priority=228,ipv6,ipv6_dst=1234:1::1 actions=CONTROLLER:65535
 cookie=0x161c970, duration=19.020s, table=3, n_packets=15, n_bytes=2010, priority=228,ipv6,ipv6_dst=1234:2::1 actions=CONTROLLER:65535
 cookie=0x6880bd4c, duration=19.020s, table=3, n_packets=19, n_bytes=2502, priority=228,ipv6,ipv6_dst=1234:3::1 actions=CONTROLLER:65535
 cookie=0x73821bdc, duration=19.020s, table=3, n_packets=19, n_bytes=2754, priority=228,ipv6,ipv6_dst=1234:4::1 actions=CONTROLLER:65535
 cookie=0x5b0c301f, duration=19.020s, table=3, n_packets=45, n_bytes=5718, priority=228,ipv6,ipv6_dst=4321::101 actions=CONTROLLER:65535
 cookie=0x78b940ba, duration=19.020s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::201:16ff:fe01:4f49 actions=CONTROLLER:65535
 cookie=0x3eef536c, duration=19.020s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::253:68ff:fe5a:745a actions=CONTROLLER:65535
 cookie=0x4dae5a90, duration=19.020s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::277:5ff:fe2a:3018 actions=CONTROLLER:65535
 cookie=0x5a53e682, duration=19.020s, table=3, n_packets=1, n_bytes=86, priority=228,ipv6,ipv6_dst=fe80::277:6fff:fe07:7550 actions=CONTROLLER:65535
 cookie=0x5dd313a8, duration=18.398s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:4444 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x61e9d09d, duration=17.395s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:2::2 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,output:ens5
 cookie=0x3a9c3bf5, duration=17.218s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:3333 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0xc436d2a, duration=16.216s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:1::2 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,output:ens4
 cookie=0x376a2bbb, duration=15.712s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:6666 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x64905ab5, duration=15.357s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=fe80::200:ff:fe00:5555 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x79190ac6, duration=14.710s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:4::2 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,output:ens7
 cookie=0x3960a8cf, duration=14.354s, table=3, n_packets=0, n_bytes=0, priority=300,ipv6,ipv6_dst=1234:3::2 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,output:ens6
 cookie=0x236a20e3, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::103 actions=mod_dl_src:00:53:68:5a:74:5a,mod_dl_dst:00:00:00:00:33:33,push_mpls:0x8847,load:0x4a499->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens4
 cookie=0x68e5decd, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::106 actions=mod_dl_src:00:77:6f:07:75:50,mod_dl_dst:00:00:00:00:66:66,push_mpls:0x8847,load:0x238ad->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens7
 cookie=0x522384e1, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::105 actions=mod_dl_src:00:01:16:01:4f:49,mod_dl_dst:00:00:00:00:55:55,push_mpls:0x8847,load:0x2abdf->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens6
 cookie=0x13fb7d9e, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=228,ipv6,ipv6_dst=4321::104 actions=mod_dl_src:00:77:05:2a:30:18,mod_dl_dst:00:00:00:00:44:44,push_mpls:0x8847,load:0x6c73a->OXM_OF_MPLS_LABEL[],set_mpls_ttl(255),output:ens5
 cookie=0x6893fb9f, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:1::/32 actions=CONTROLLER:65535
 cookie=0x7ea39f92, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:2::/32 actions=CONTROLLER:65535
 cookie=0x54c6a0b8, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:3::/32 actions=CONTROLLER:65535
 cookie=0x7e67a7f9, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=132,ipv6,ipv6_dst=1234:4::/32 actions=CONTROLLER:65535
 cookie=0x6d0c23df, duration=19.020s, table=3, n_packets=0, n_bytes=0, priority=0 actions=drop
connection closed
```

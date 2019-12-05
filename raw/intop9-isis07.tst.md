# Example: interop9: isis sr

## **Topology diagram**

![topology](/img/intop9-isis07.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
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
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.1111.00
 traffeng-id 2.2.2.1
 is-type level2
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.1111.00
 traffeng-id 6.6.6.1
 is-type level2
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 segrout index 1
 router isis4 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 segrout index 2
 router isis6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv4 access-group-in test4
 mpls enable
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0009.3b1d.4e7b
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 pseudowire v1 loopback1 pweompls 2.2.2.3 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 0059.381c.283d
 vrf forwarding v1
 ipv4 address 3.3.3.5 255.255.255.252
 pseudowire v1 loopback2 pweompls 4321::3 1234
 no shutdown
 no log-link-change
 exit
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
end
```

**r2:**
```
hostname r2
set interfaces ge-0/0/0.0 family inet address 1.1.1.2/24
set interfaces ge-0/0/0.0 family iso
set interfaces ge-0/0/0.0 family mpls
set interfaces ge-0/0/1.0 family inet6
set interfaces ge-0/0/1.0 family iso
set interfaces ge-0/0/1.0 family mpls
set interfaces ge-0/0/2.0 family inet address 1.1.2.2/24
set interfaces ge-0/0/2.0 family iso
set interfaces ge-0/0/2.0 family mpls
set interfaces ge-0/0/3.0 family inet6
set interfaces ge-0/0/3.0 family iso
set interfaces ge-0/0/3.0 family mpls
set interfaces lo0.0 family inet address 2.2.2.2/32
set interfaces lo0.0 family inet6 address 4321::2/128
set interfaces lo0.0 family iso address 48.0000.0000.1234.00
set protocols mpls interface ge-0/0/0.0
set protocols mpls interface ge-0/0/1.0
set protocols mpls interface ge-0/0/2.0
set protocols mpls interface ge-0/0/3.0
set protocols isis interface ge-0/0/0.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/1.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/2.0 point-to-point hello-padding disable
set protocols isis interface ge-0/0/3.0 point-to-point hello-padding disable
set protocols isis interface lo0.0
set protocols isis source-packet-routing node-segment ipv4-index 3
set protocols isis source-packet-routing node-segment ipv6-index 4
commit
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
 exit
!
router isis4 1
 vrf v1
 net-id 48.4444.0000.3333.00
 traffeng-id 2.2.2.3
 is-type level2
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
router isis6 1
 vrf v1
 net-id 48.6666.0000.3333.00
 traffeng-id 6.6.6.3
 is-type level2
 segrout 10
 level2 segrout
 level1 segrout
 redistribute connected
 exit
!
interface loopback1
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.3 255.255.255.255
 router isis4 1 enable
 router isis4 1 circuit level2
 router isis4 1 segrout index 5
 router isis4 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface loopback2
 no description
 vrf forwarding v1
 ipv6 address 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 router isis6 1 enable
 router isis6 1 circuit level2
 router isis6 1 segrout index 6
 router isis6 1 segrout node
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.2.1 255.255.255.0
 ipv4 access-group-in test4
 mpls enable
 router isis4 1 enable
 router isis4 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface ethernet2
 no description
 vrf forwarding v1
 ipv6 address fe80::1 ffff::
 ipv6 access-group-in test6
 mpls enable
 router isis6 1 enable
 router isis6 1 circuit level2
 no shutdown
 no log-link-change
 exit
!
interface pwether1
 no description
 mtu 1500
 macaddr 0053.4954.4560
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 pseudowire v1 loopback1 pweompls 2.2.2.1 1234
 no shutdown
 no log-link-change
 exit
!
interface pwether2
 no description
 mtu 1500
 macaddr 0034.646f.2111
 vrf forwarding v1
 ipv4 address 3.3.3.6 255.255.255.252
 pseudowire v1 loopback2 pweompls 4321::1 1234
 no shutdown
 no log-link-change
 exit
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
end
```

# **Let's enable Multi Protocol Label Switching (MPLS)**

## 1 Overview
In [Let’s enable routing](004-igp.md) you learned how to create a routing domain and activated OSPF and OSPFv3 as IGP. In SP context, next step is to activate MPLS. This page is not an MPLS deep dive lesson and will put the focus on enabling MPLS in the entire routing domain with freeRtr.

In a nutshell, MPLS is a paradigm that will add encapsulation to the packet ingressing the SP MPLS domain. This encapsulation can be compared to a stack of labels. Each label position in the stack will have a different processing from MPLS routers within the network. A MPLS router can be a backbone router (aka P) or a provider egde router (aka PE). From the perspective of packet direction, ingress PE can proceed to label imposition (2 or more label in the stacks), the P router will simply proceed to MPLS label swap operation while the PHP or egress PE will pop the MPLS header.

When enabling MPLS, you have to remember that there is 2 main important points you need to care about:

- Label distribution: i.e how label will be allocated within the MPLS domain
- MPLS packet operation: i.e how MPLS encapsulated packet are processed

!!! note
    The above will guide you in understanding the below configuration steps.

In the present page, we will focus on the TOP MOST label in the MPLS stack, which is corresponds to MPLS forwarding operation.

## 2 freeRtr network example
### 2.1 Diagram
The demo implements a square topology:
- nodes are `r1`,`r2`,`r3`,`r4`
- edges are `e1[r1-r2]`,`e2[r2-r4]`,`e3[r3-r4]`,`e4[r1-r3]`
  `-` means is "connected to"
```
  r1----e1----r2
  |            |
  |            |
  e2          e2
  |            |
  |            |
  r3----e1----r4
```

We will consider the following assumption:

- LDP will be used to distribute label
- MPLS will be activated on all routers' core interface `eth1` and `eth2`
- Label distribution FECs are computed on a per IPv4 and IPv6 prefix basis

### 2.2 Nodes configuration
#### 2.2.1  **router** `r1`,`r2`,`r3`,`r4`

We will reuse `<*>-hw.txt` config file from previous articles [here](004-igp.md).
and add LDP configuration to `<*>-sw.txt` below:


`[r1|r2|r3|r4]-sw.txt`


```
show config-differences
interface ethernet2
 mpls enable
 mpls ldp4
 mpls ldp6
 exit
interface ethernet1
 mpls enable
 mpls ldp4
 mpls ldp6
 exit
vrf definition v1
 label-mode all-igp
 exit
```


## 3 Verification
### 3.1 Launch all nodes

Run `r1`,`r2`,`r3`,`r4` in different terminal windows:

`r1`
```
java -jar rtr.jar routersc r1-hw.txt r1-sw.txt
```
`r2`
```
java -jar rtr.jar routersc r2-hw.txt r2-sw.txt
```
`r3`
```
java -jar rtr.jar routersc r3-hw.txt r3-sw.txt
```
`r4`
```
java -jar rtr.jar routersc r4-hw.txt r4-sw.txt
```
### 3.2 Physical connectivity check
- **LLDP**

```
r1#sh lldp nei
interface  hostname  iface      ipv4     ipv6
ethernet1  r2        ethernet1  1.1.1.2  1234:1::2
ethernet2  r3        ethernet2  1.1.1.6  1234:2::2
```

- **MPLS interfaces**

```
r1#show mpls interfaces
interface  packet  secure  ldp4   ldp6   rsvp4  rsvp6
loopback0  false   false   false  false  false  false
ethernet1  true    false   true   true   false  false
ethernet2  true    false   true   true   false  false
ethernet3  false   false   false  false  false  false
```

- **interconnectivity reachability**

ping from `r1@eth1`

```
r1#ping 1.1.1.2 vrf v1
pinging 1.1.1.2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=1/2/5/12
```

```
r1#ping 1234:1::2 vrf v1
pinging 1234:1::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/0/3/16
```


ping from `r1@eth2`

```
r1#ping 1.1.1.6 vrf v1
pinging 1.1.1.6, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/2/10
```

```
r1#ping 1234:2::2 vrf v1
pinging 1234:2::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/4/16
r1#
```

### 3.3 LDP4 and LDP6 verification

- **LDP summary**

```
r1#show ipv4 ldp v1 summary
prefix         layer2         p2mp
learn  advert  learn  advert  learn  advert  neighbor  uptime
10     11      0      0       0      0       1.1.1.2   01:01:51
10     11      0      0       0      0       1.1.1.6   00:49:06
```

```
r1#show ipv6 ldp v1 summary
prefix         layer2         p2mp
learn  advert  learn  advert  learn  advert  neighbor   uptime
10     12      0      0       0      0       1234:1::2  01:01:54
10     12      0      0       0      0       1234:2::2  00:49:09
```

- **LDP neighbors**

```
r1#show ipv4 ldp v1 neighbor 1.1.1.2 status
peer = 1.1.1.2
transport = 1.1.1.2
lsrid = 1.1.1.2
local = 1.1.1.1
uptime = 01:03:13 ago, at 2021-09-07 09:46:50
hold time = 00:03:00
keepalive time = 00:01:00
prefix learned = 10
pwe learned = 0
p2mp learned = 0
advertise php = false
prefix advertised = 11 of 11
pwe advertised = 0 of 0
p2mp advertised = 0
connection = tx=1852(83) rx=1700(79) drp=0(0)

r1#show ipv4 ldp v1 neighbor 1.1.1.6 status
peer = 1.1.1.6
transport = 1.1.1.6
lsrid = 1.1.1.6
local = 1.1.1.5
uptime = 00:50:37 ago, at 2021-09-07 09:59:36
hold time = 00:03:00
keepalive time = 00:01:00
prefix learned = 10
pwe learned = 0
p2mp learned = 0
advertise php = false
prefix advertised = 11 of 11
pwe advertised = 0 of 0
p2mp advertised = 0
connection = tx=1618(70) rx=1466(66) drp=0(0)
```

```
r1#show ipv6 ldp v1 neighbor 1234:1::2 status
peer = 1234:1::2
transport = 1234:1::2
lsrid = 0.0.0.2
local = 1234:1::1
uptime = 01:04:01 ago, at 2021-09-07 09:46:52
hold time = 00:03:00
keepalive time = 00:01:00
prefix learned = 10
pwe learned = 0
p2mp learned = 0
advertise php = false
prefix advertised = 12 of 12
pwe advertised = 0 of 0
p2mp advertised = 0
connection = tx=2026(84) rx=1796(79) drp=0(0)

r1#show ipv6 ldp v1 neighbor 1234:2::2 status
peer = 1234:2::2
transport = 1234:2::2
lsrid = 0.0.0.2
local = 1234:2::1
uptime = 00:51:22 ago, at 2021-09-07 09:59:36
hold time = 00:03:00
keepalive time = 00:01:00
prefix learned = 10
pwe learned = 0
p2mp learned = 0
advertise php = false
prefix advertised = 12 of 12
pwe advertised = 0 of 0
p2mp advertised = 0
connection = tx=1810(72) rx=1580(67) drp=0(0)
```

- **LDP database**

```
r1#show ipv4 ldp v1 database
prefix       local   remote  hop
0.0.0.0/32   910946          null
1.1.1.0/30   910946          null
1.1.1.1/32   910946          null
1.1.1.4/30   910946          null
1.1.1.5/32   910946          null
1.1.1.8/30   129003  800494  1.1.1.2
1.1.1.12/30  521087  785657  1.1.1.6
2.2.2.1/32   910946          null
2.2.2.2/32   295827  800494  1.1.1.2
2.2.2.3/32   815108  785657  1.1.1.6
2.2.2.4/32   625208  452135  1.1.1.2
```

```
r1#show ipv6 ldp v1 database
prefix                     local    remote  hop
1234:1::/32                60611            null
1234:1::1/128              60611            null
1234:2::/32                60611            null
1234:2::1/128              60611            null
1234:3::/32                320237   596028  1234:1::2
1234:4::/32                370786   383223  1234:2::2
4321::1/128                60611            null
4321::2/128                363162   596028  1234:1::2
4321::3/128                1035264  383223  1234:2::2
4321::4/128                255927   739648  1234:1::2
fe80::/64                  60611            null
fe80::200:11ff:fe11:3/128  60611            null
```

- **show ip[v4|v6] route v1**

```
r1#sh ipv4 route v1
typ  prefix       metric  iface      hop      time
C    0.0.0.0/32   0/0     ethernet3  null     01:58:44
C    1.1.1.0/30   0/0     ethernet1  null     01:58:45
LOC  1.1.1.1/32   0/1     ethernet1  null     01:58:45
C    1.1.1.4/30   0/0     ethernet2  null     01:58:44
LOC  1.1.1.5/32   0/1     ethernet2  null     01:58:44
O    1.1.1.8/30   110/1   ethernet1  1.1.1.2  01:58:27
O    1.1.1.12/30  110/1   ethernet2  1.1.1.6  01:58:16
C    2.2.2.1/32   0/0     loopback0  null     01:58:45
O    2.2.2.2/32   110/1   ethernet1  1.1.1.2  01:58:27
O    2.2.2.3/32   110/1   ethernet2  1.1.1.6  01:58:16
O    2.2.2.4/32   110/2   ethernet1  1.1.1.2  01:58:10
```

```
r1#sh ipv6 route v1
typ  prefix                     metric  iface      hop        time
C    1234:1::/32                0/0     ethernet1  null       01:58:50
LOC  1234:1::1/128              0/1     ethernet1  null       01:58:50
C    1234:2::/32                0/0     ethernet2  null       01:58:50
LOC  1234:2::1/128              0/1     ethernet2  null       01:58:50
O    1234:3::/32                110/1   ethernet1  1234:1::2  01:58:32
O    1234:4::/32                110/1   ethernet2  1234:2::2  01:58:21
C    4321::1/128                0/0     loopback0  null       01:58:50
O    4321::2/128                110/1   ethernet1  1234:1::2  01:58:32
O    4321::3/128                110/1   ethernet2  1234:2::2  01:58:21
O    4321::4/128                110/2   ethernet1  1234:1::2  01:58:15
C    fe80::/64                  0/0     ethernet3  null       01:58:50
LOC  fe80::200:11ff:fe11:3/128  0/1     ethernet3  null       01:58:50
```

### 3.4 Loopback reachability verification using traceroute

- **loopback reachability from `r1@eth1`**

traceroute to `r1@lo0`

```
r1#traceroute 2.2.2.1 vrf v1
tracing 2.2.2.1, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 2.2.2.1 time=1
```

```
r1#traceroute 4321::1 vrf v1
tracing 4321::1, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 4321::1 time=0
```

traceroute to `r2@lo0`

```
traceroute 2.2.2.2 vrf v1

tracing 2.2.2.1, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 2.2.2.1 time=1
r1#traceroute 2.2.2.2 vrf v1
```

```
r1#traceroute 4321::2 vrf v1
tracing 4321::2, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1234:1::1 time=0
2 4321::2 time=1, mpls=596028
```

traceroute to `r3@lo0`

```
traceroute 2.2.2.3 vrf v1
tracing 2.2.2.3, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1.1.1.5 time=0
2 2.2.2.3 time=2, mpls=785657
```

```
r1#traceroute 4321::3 vrf v1
tracing 4321::3, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1234:2::1 time=0
2 4321::3 time=0, mpls=383223
```

traceroute to `r4@lo0`

```
r1#traceroute 2.2.2.4 vrf v1
tracing 2.2.2.4, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1.1.1.1 time=0
2 1.1.1.9 time=0, mpls=452135
3 2.2.2.4 time=1, mpls=539881
```

```
r1#traceroute 4321::4 vrf v1
tracing 4321::4, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1234:1::1 time=0
2 1234:3::1 time=1, mpls=739648
3 4321::4 time=1, mpls=1023984
```

From the traceroutes output you observe that LSP paths are used. (except for directly connected loopback of course)

!!! note
    `r2`,`r3` and `r4` verification is not displayed in order to avoid to clutter the article. But verification steps are obviously following the same path.

## 3 Conclusion
This section demonstrated:

- How to implement MPLS in our local square topology:
    - by configuring LDP for IPv4 and IPv6 address family
    - by explaining how to verify LDP operation
- How to verify connectivity
    - from each node of the topology
    - verify loopback reachability using traceroute and check MPLS LSP

You learned how to enable MPLS forwarding with LDP as label distribution protocol. You also verified that IPv4 and IPv6 network prefixes are considered as FEC from LDP perspective. Among these FEC you also checked that each router loopbacks are reachable using a MPLS LSP signalled by LDP. From SP perspective, we are now almost ready, this is still one configuration step before being able to implement MPLS service on top of the MLPS core you just created: configure iBGP between PE. But we will discuss this point in a subsequent article.

!!! note
    In this article, we used LDP with a `all-igp` label distribution mode. This mode is similar to Cisco default LDP behavior. freeRtr gives you the possibility to fine [tune label allocation](http://sources.nop.hu/cfg/mpls-ldp22.tst) which will help to save label space. it also feature a functionality that allows you to [control which label the router advertises](http://sources.nop.hu/cfg/mpls-ldp21.tst) to other ldp neighbors. Obviously the latter won't not contribute to label space saving. freeRtr also support [targeted LDP](http://sources.nop.hu/cfg/mpls-ldp17.tst) (Useful to to establish LDP session between non directly connected routers)

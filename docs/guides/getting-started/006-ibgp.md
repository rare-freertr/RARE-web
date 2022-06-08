# **BGP in service provider network**

## 1 Overview
In [Let’s enable MPLS](005-mpls.md) you learned how to enable MPLS forwarding on top of an IGP in the entire routing domain. From that point:

- Label reachability information is signalled between nodes using LDP relying on IGP database
- Effective traffic data path between any forwarding equivalent class (IPv4 and IPv6) is following a what we call a `MPLS LSP`

!!! note
    However, all of this is true only for internal IPv4 & IPv6 in the routing domain. In a SP environment, the backbone is interconnecting customer sites with dedicated CPE routers. CPEs can act as BGP peers advertising customer prefixes. These NLRI(s) is external to the SP domain and thus ~~should~~ must not be injected into the IGP.

This is where BGP comes into play. BGP is also assimilated as an Exterior Routing Protocol (EGP). In a nutshell, BGP is used to signal:

- From the perspective of an external packet entering the SP domain (i.e ingress Border SP router)
- The best exit point from the very same domain (i.e egress Border SP router)

Indifferently, you'll see in the litterature the terms `ingress PE` and `egress PE`.

Practically:

- `egress PE` is the BGP nexthop -
- for a packet sourced from customer `subnet A` in `site A`
- arriving at `ingress PE`
- in order to reach customer `subnet B` in `site B`

!!! note
    It is important to understand that, BGP does not provide any indication related to the path taken by the packet in order to reach the egress PE from the ingress PE. This forwarding is handled by the MPLS core you implemented in the last article. This means that BGP is needed only on border nodes (PE) connecting customer and not in the core (P) routers in the SP backbone.

Now you can use 3 techniques in order to enable iBGP in the core network:

- iBGP Full mesh
- BGP confederations
- BGP route reflector

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

- Route Reflection will be used
  - `r4` is the route reflector (RR)
  - `r1`,`r2`,`r3` are route reflector client (RRc)
- iBGP session will be established using `Loopback0`

### 2.2 Nodes configuration
#### 2.2.1  **router** `r1`,`r2`,`r3`,`r4`

We will reuse `<*>-hw.txt` config file from previous articles [here](004-igp.md).
and add BGP configuration to `<*>-sw.txt` below:

- RR

`r4-sw.txt`

```
object-group network RR-CLIENT-NET4
 description IPv4 RR client subnet
 sequence 10 2.2.2.0 255.255.255.0
 exit
object-group network RR-CLIENT-NET6
 description IPv6 RR client subnet
 sequence 10 4321:: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
 exit
access-list ACL-IPv4-RR-CLIENT
 sequence 10 permit all obj RR-CLIENT-NET4 all any all
 exit
access-list ACL-IPv6-RR-CLIENT
 sequence 10 permit all obj RR-CLIENT-NET6 all any all
 exit
route-policy NHT
 sequence 10 if distance 110
 sequence 20   pass
 sequence 30 else
 sequence 40   drop
 sequence 50 enif
 exit
router bgp4 1
 vrf v1
 local-as 65535
 router-id 2.2.2.4
 address-family unicast multicast flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 nexthop route-policy NHT
 template bgp4 remote-as 65535
 template bgp4 description rr clients
 template bgp4 local-as 65535
 template bgp4 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 template bgp4 distance 255
 template bgp4 connection-mode active
 template bgp4 compression both
 template bgp4 update-source loopback0
 template bgp4 hostname
 template bgp4 aigp
 template bgp4 traffeng
 template bgp4 pmsitun
 template bgp4 tunenc
 template bgp4 attribset
 template bgp4 segrout
 template bgp4 bier
 template bgp4 route-reflector-client
 template bgp4 next-hop-unchanged
 template bgp4 send-community all
 listen ACL-IPv4-RR-CLIENT bgp4
 exit
router bgp6 1
 vrf v1
 local-as 65535
 router-id 2.2.2.4
 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 nexthop route-policy NHT
 template bgp6 remote-as 65535
 template bgp6 description rr clients
 template bgp6 local-as 65535
 template bgp6 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 template bgp6 distance 255
 template bgp6 connection-mode active
 template bgp6 compression both
 template bgp6 update-source loopback0
 template bgp6 hostname
 template bgp6 aigp
 template bgp6 traffeng
 template bgp6 pmsitun
 template bgp6 tunenc
 template bgp6 attribset
 template bgp6 segrout
 template bgp6 bier
 template bgp6 route-reflector-client
 template bgp6 next-hop-unchanged
 template bgp6 send-community all
 listen ACL-IPv6-RR-CLIENT bgp6
 exit
```


- RR clients

`[r1|r2|r3]-sw.txt`


```
show config-differences
router bgp4 1
 vrf v1
 local-as 65535
 router-id 2.2.2.[1|2|3]
 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 neighbor 2.2.2.4 remote-as 65535
 neighbor 2.2.2.4 description RR[r4]
 neighbor 2.2.2.4 local-as 65535
 neighbor 2.2.2.4 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 neighbor 2.2.2.4 distance 200
 neighbor 2.2.2.4 update-source loopback0
 template 2.2.2.4 hostname
 template 2.2.2.4 aigp
 template 2.2.2.4 traffeng
 template 2.2.2.4 pmsitun
 template 2.2.2.4 tunenc
 template 2.2.2.4 attribset
 template 2.2.2.4 segrout
 template 2.2.2.4 bier
 template 2.2.2.4 send-community all
 exit
router bgp6 1
 vrf v1
 local-as 65535
 router-id 2.2.2.[1|2|3]
 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 neighbor 4321::4 remote-as 65535
 neighbor 4321::4 description RR[r4]
 neighbor 4321::4 local-as 65535
 neighbor 4321::4 address-family unicast multicast ouni omlt flowspec vpnuni vpnmlt vpnflw ovpnuni ovpnmlt ovpnflw vpls mspw evpn mdt srte mvpn omvpn
 neighbor 4321::4 distance 200
 neighbor 4321::4 update-source loopback0
 template 4321::4 hostname
 template 4321::4 aigp
 template 4321::4 traffeng
 template 4321::4 pmsitun
 template 4321::4 tunenc
 template 4321::4 attribset
 template 4321::4 segrout
 template 4321::4 bier
 template 4321::4 send-community all
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
### 3.2 Connectivity between RR and RR client `r1`
- **`r4` (RR) reachability from `r1`**

!!! note
    In order to avoid cluttering the page, verification will be done for IPv4 only. You can do IPv6 checks as an exercice.  :-)

**TL;DR**

```
r1#show ipv4 route v1 | i 2.2.2.4
O    2.2.2.4/32   110/2   ethernet1  1.1.1.2  01:18:47
```

!!! note
    Notice that the route has OSPF `O` tag


**Detailed ouput**

```
r1#show ipv4 route v1 2.2.2.4
vrf = v1:4
ipver = 4
rd = 0:0
prefix = 2.2.2.4/128
prefix network = 2.2.2.4
prefix broadcast = 2.2.2.4
prefix wildcard = ::
prefix netmask = ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
nlri = n/a
alternates = 1
alternate #0 attributes: ecmp=true best=true
type = ospf4 1
source = 2.2.2.4
validity = 0
segment routing index = 0
segment routing old base = 0
segment routing base = 0
segment routing size = 0
segment routing prefix = null
bier index = 0
bier old base = 0
bier base = 0
bier range = 0
bier size = 0-32
updated = 2021-09-09 08:24:18 (01:18:32 ago)
version = 0
distance = 110
metric = 2
ident = 0
hops = 2
interface = ethernet1
table = null
nexthop = 1.1.1.2
original nexthop = null
tag = 0
origin type = 109
local preference = 0
evpn label*16 = 0
attribute as = 0
attribute value = n/a
tunnel type = 0
tunnel value = n/a
link state = n/a
pmsi type = 0
pmsi label*16 = 0
pmsi tunnel = n/a
accumulated igp = 0
bandwidth = 0
atomic aggregator = false
aggregator as = 0
aggregator router = null
originator = null
cluster list =
as path (len=0) =
standard community =
extended community =
large community =
internal source = 0
local label = 471761
remote label = 527160
counter = null
hardware counter = null
```

!!! note
    Pay attention to MPLS `local label = 471761` and `remote label = 527160`, this is the first segment of the MPLS LSP path toward `r4`

```
r1#ping 2.2.2.4 vrf v1
pinging 2.2.2.4, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/0/1/7
```

```
r1#traceroute 2.2.2.4 vrf v1
tracing 2.2.2.4, src=null, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 1.1.1.1 time=0
2 1.1.1.9 time=1, mpls=527160
3 2.2.2.4 time=1, mpls=95859
```

!!! note
    Obviously, you observe that MPLS LSP is used and notice the second hop MPLS label: ` mpls=527160`

### Check from `r4` RR

- **BGP summary**

```
r4#show ipv4 bgp 1 summary
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   2.2.2.1   01:27:17
65535  0      0     true   2.2.2.2   01:27:15
65535  0      0     true   2.2.2.3   01:27:13
```

```
r4#show ipv6 bgp 1 summary
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   4321::1   01:27:20
65535  0      0     true   4321::2   01:27:19
65535  0      0     true   4321::3   01:27:18
```


- **BGP neighbor session with `r1`**

On a per address family

```
r4#show ipv4 bgp 1 neighbor 2.2.2.1 ?
  config    - peer configuration
  evpn      - address family to show
  flowspec  - address family to show
  labeled   - address family to show
  linkstate - address family to show
  mdt       - address family to show
  mspw      - address family to show
  multicast - address family to show
  mvpn      - address family to show
  oflw      - address family to show
  olab      - address family to show
  omlt      - address family to show
  omvpn     - address family to show
  osrt      - address family to show
  ouni      - address family to show
  ovpnflw   - address family to show
  ovpnmlt   - address family to show
  ovpnuni   - address family to show
  srte      - address family to show
  status    - peer status
  unicast   - address family to show
  vpls      - address family to show
  vpnflw    - address family to show
  vpnmlt    - address family to show
  vpnuni    - address family to show
```

```
r4#show ipv6 bgp 1 neighbor 4321::1 ?
  config    - peer configuration
  evpn      - address family to show
  flowspec  - address family to show
  labeled   - address family to show
  linkstate - address family to show
  mdt       - address family to show
  mspw      - address family to show
  multicast - address family to show
  mvpn      - address family to show
  oflw      - address family to show
  olab      - address family to show
  omlt      - address family to show
  omvpn     - address family to show
  osrt      - address family to show
  ouni      - address family to show
  ovpnflw   - address family to show
  ovpnmlt   - address family to show
  ovpnuni   - address family to show
  srte      - address family to show
  status    - peer status
  unicast   - address family to show
  vpls      - address family to show
  vpnflw    - address family to show
  vpnmlt    - address family to show
  vpnuni    - address family to show
```

- **BGP database**

```
r4#show ipv6 bgp 1 unicast database
prefix  hop  metric  aspath

```

```
r4#show ipv4 bgp 1 unicast database
prefix  hop  metric  aspath

```

??? info
    What ??!! BGP database is empty ! => Well this actually is normal as there is no external NLRI advertised for now. Remember, BGP is used to enable connectivity between netwosks external to the SP domain. As we don't have any customer for now this is normal to have BGP database empty.

- **show ip[v4|v6] route v1**

```
r4#show ipv4 route v1
typ  prefix       metric  iface      hop       time
O    1.1.1.0/30   110/1   ethernet2  1.1.1.9   01:33:39
O    1.1.1.4/30   110/1   ethernet1  1.1.1.13  01:33:39
C    1.1.1.8/30   0/0     ethernet2  null      01:33:42
LOC  1.1.1.10/32  0/1     ethernet2  null      01:33:42
C    1.1.1.12/30  0/0     ethernet1  null      01:33:43
LOC  1.1.1.14/32  0/1     ethernet1  null      01:33:43
O    2.2.2.1/32   110/2   ethernet2  1.1.1.9   01:33:39
O    2.2.2.2/32   110/1   ethernet2  1.1.1.9   01:33:39
O    2.2.2.3/32   110/1   ethernet1  1.1.1.13  01:33:39
C    2.2.2.4/32   0/0     loopback0  null      01:33:43
```

```
r4#show ipv6 route v1
typ  prefix         metric  iface      hop        time
O    1234:1::/32    110/2   ethernet1  1234:4::1  01:33:44
O    1234:2::/32    110/1   ethernet1  1234:4::1  01:33:44
C    1234:3::/32    0/0     ethernet2  null       01:33:47
LOC  1234:3::2/128  0/1     ethernet2  null       01:33:47
C    1234:4::/32    0/0     ethernet1  null       01:33:48
LOC  1234:4::2/128  0/1     ethernet1  null       01:33:48
O    4321::1/128    110/2   ethernet1  1234:4::1  01:33:44
O    4321::2/128    110/3   ethernet1  1234:4::1  01:33:44
O    4321::3/128    110/1   ethernet1  1234:4::1  01:33:44
C    4321::4/128    0/0     loopback0  null       01:33:48
```

!!! note
    Of course, there is no BGP routes in the SP routing table and this is what we want ! Imagine the burden you'll add to your IGP if you redistributed the entire Internet full routing table ...

### 3.4 RR `Loopback0` reachability verification from RR client

- **BGP loopback reachability from `r1@eth1`**

From **RR client**  `r1@lo0`

```
r1#sh ipv4 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   2.2.2.4   01:40:44

r1#traceroute 2.2.2.4 vrf v1
r1#traceroute 2.2.2.4 vrf v1 /interface lo0
tracing 2.2.2.4, src=2.2.2.1, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 2.2.2.1 time=0
2 1.1.1.9 time=3, mpls=527160
3 2.2.2.4 time=1, mpls=95859
```

```
r1#sh ipv6 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   4321::4   01:39:58

r1#traceroute 4321::4 vrf v1 /interface lo0
tracing 4321::4, src=4321::1, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 4321::1 time=0
2 1234:4::1 time=2, mpls=76040
3 4321::4 time=1, mpls=463804
```

From **RR client** `r2@lo0`

```
r2#show ipv4 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   2.2.2.4   01:41:33

r2#traceroute 2.2.2.4 vrf v1 /interface lo0
tracing 2.2.2.4, src=2.2.2.2, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 2.2.2.2 time=0
2 2.2.2.4 time=0, mpls=95859
```

```
r2#show ipv6 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   4321::4   01:44:26

r2#traceroute 4321::4 vrf v1
r2#traceroute 4321::4 vrf v1 /interface lo0
tracing 4321::4, src=4321::2, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 4321::2 time=0
2 1234:2::1 time=2, mpls=46041
3 1234:4::1 time=3, mpls=76040
4 4321::4 time=2, mpls=463804
```

From **RR client** `r3@lo0`

```
r3#show ipv4 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   2.2.2.4   01:42:54

r3#traceroute 2.2.2.4 vrf v1 /interface lo0
tracing 2.2.2.4, src=2.2.2.3, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 2.2.2.3 time=0
2 2.2.2.4 time=1, mpls=95859
```

```
r3#show ipv6 bgp 1 sum
as     learn  sent  ready  neighbor  uptime
65535  0      0     true   4321::4   01:46:06

r3#traceroute 4321::4 vrf v1 /interface lo0
tracing 4321::4, src=4321::3, vrf=v1, prt=0/33440, tim=1000, tos=0, len=64
1 4321::3 time=0
2 4321::4 time=1, mpls=463804
```
From **RR** `r4@lo0`

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

!!! note
    `r2`,`r3` and `r4` verification is not displayed in order to avoid to clutter the article. But verification steps are obviously following the same path.

## 3 Conclusion
This section demonstrated:

- How to implement iBGP on top of our local square topology:
    - by configuring BGP route reflection `r4` is RR and `r1`,`r2`,`r3` are RR clients
    - by configuring BGP for IPv4 and IPv6 address family and a gigantic list of SAFI
    - by explaining how to verify BGP operation
- How to verify connectivity
    - from each RR client of the topology
    - verify RR loopback reachability from all RR clients check MPLS LSP

You learned how to enable iBGP on top of the SP domain using RR paradigm. However, we saw that BGP database was empty. Which is totally normal as we don't have any customer yet. BGP is used to signal external networks reachability within the SP backbone between SP autonomous system border router. This will be discussed in a subsequent article.

!!! note
    Before jumping to next article, let's take 5 minutes and contemplate `rr4` BGP configuration. From this stanza, you notice nitty gritty details that demonstrates all the attention and craftmanship :-) that [mc36](http://mc36.nop.hu/) brought to [freeRtr](http://www.freertr.org/) CLI:

- `object-group` very useful to simplify access list writing/reading
- BGP `nexthop tracking` feature
- Using Route Policy Language (`rpl`)
- the impressive list of supported `SAFI` for for `AFI` IPv4 and IPv6 (incomplete list ...)
- Usage of the `template` keyword summoned via `listen` command
- `listen` CLI keyword. For those who configured RR back in 1998 can understand the convenience brought by this command. (Granted the fact that with have BGP `template`)

???+ info
    These features are usually found on high end commercial platform.

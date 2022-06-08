# ** freeRtr topology simulation **

## 1 Overview
In [Hello freeRtr !](001-hello-world.md) you learned how to implement one single freeRtr node that has 2 interfaces. In this page, you'll learn:

- how to implement a local topology by declaring 4 nodes
- each nodes has 2 interfaces (`eth1` and` eth2`)
- declare interconnection in the hardware definition file using the topology below.

## 2 freeRtr network example
In this section, we will use the demo example bundled into freeRtr tarball.
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
### 2.2 Nodes configuration
#### 2.2.1  **router** `r1`

`r1-hw.txt`
```
int eth1 eth 0000.1111.0001 127.0.0.1 1001 127.0.0.1 2001
int eth2 eth 0000.1111.0002 127.0.0.1 1002 127.0.0.1 3002
```
`r1-sw.txt`

```
hostname r1
!
vrf def v1
 rd 1:1
 exit
server telnet tel
 security protocol tel
 vrf v1
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 desc r1@eth1 -> r2@eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.252
 ipv6 addr 1234:1::1 ffff:ffff::
 exit
int eth2
 desc r1@eth2 -> r3@eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.5 255.255.255.252
 ipv6 addr 1234:2::1 ffff:ffff::
 exit
!
```
#### 2.2.2  **router** `r2`

`r2-hw.txt`
```
int eth1 eth 0000.2222.0001 127.0.0.1 2001 127.0.0.1 1001
int eth2 eth 0000.2222.0002 127.0.0.1 2002 127.0.0.1 4002
```
`r2-sw.txt`

```
hostname r2
!
vrf def v1
 rd 1:1
 exit
server telnet tel
 security protocol tel
 vrf v1
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.2 255.255.255.255
 ipv6 addr 4321::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 desc r2@eth1 -> r1@eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.2 255.255.255.252
 ipv6 addr 1234:1::2 ffff:ffff::
 exit
int eth2
 desc r2@eth2 -> r4@eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.9 255.255.255.252
 ipv6 addr 1234:3::1 ffff:ffff::
 exit
!
```

#### 2.2.3  **router** `r3`

`r3-hw.txt`
```
int eth1 eth 0000.3333.0001 127.0.0.1 3001 127.0.0.1 4001
int eth2 eth 0000.3333.0002 127.0.0.1 3002 127.0.0.1 1002
```
`r3-sw.txt`
```
hostname r3
!
vrf def v1
 rd 1:1
 exit
server telnet tel
 security protocol tel
 vrf v1
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.3 255.255.255.255
 ipv6 addr 4321::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 desc r3@eth1 -> r4@eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.13 255.255.255.252
 ipv6 addr 1234:4::1 ffff:ffff::
 exit
int eth2
 desc r3@eth2 -> r1@eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.6 255.255.255.252
 ipv6 addr 1234:2::2 ffff:ffff::
 exit
!
```

#### 2.2.4  **router** `r4`

`r4-hw.txt`
```
int eth1 eth 0000.4444.0001 127.0.0.1 4001 127.0.0.1 3001
int eth2 eth 0000.4444.0002 127.0.0.1 4002 127.0.0.1 2002
```
`r4-sw.txt`
```
hostname r4
!
vrf def v1
 rd 1:1
 exit
server telnet tel
 security protocol tel
 vrf v1
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.4 255.255.255.255
 ipv6 addr 4321::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
int eth1
 desc r4@eth1 -> r3@eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.14 255.255.255.252
 ipv6 addr 1234:4::2 ffff:ffff::
 exit
int eth2
 desc r4@eth2 -> r2@eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.10 255.255.255.252
 ipv6 addr 1234:3::2 ffff:ffff::
 exit
!
```
## 3 Explanation
### 3.1  **router** `r1`
`r1` has 2 interfaces:

- `r1@eth1` has socket `127.0.0.1 1001` and is conected to `127.0.0.1 2001`
- `r1@eth2` has socket `127.0.0.1 1002` and is conected to `127.0.0.1 3002`

if you look at subsequent declarations below:

- `127.0.0.1 2001` is `r2@eth1`
- `127.0.0.1 3002` is `r3@eth2`

### 3.2  **router** `r2`

- `r2@eth1` has socket `127.0.0.1 2001` and is conected to `127.0.0.1 1001`
- `r2@eth2` has socket `127.0.0.1 2002` and is conected to `127.0.0.1 4002`

if you look at subsequent declarations below:

- `127.0.0.1 1001` is `r1@eth1`
- `127.0.0.1 4002` is `r4@eth2`

### 3.3  **router** `r3`

- `r3@eth1` has socket `127.0.0.1 3001` and is conected to `127.0.0.1 4001`
- `r3@eth2` has socket `127.0.0.1 3002` and is conected to `127.0.0.1 1002`

if you look at subsequent declarations below:

- `127.0.0.1 4001` is `r4@eth1`
- `127.0.0.1 1002` is `r1@eth2`

### 3.4  **router** `r4`

## 4 Verification
### 4.1 Launch all nodes

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
### 4.2 Physical connectivity check

#### 4.2.1  **router** `r1`
```
r1#sh lldp nei
interface  hostname  iface      ipv4     ipv6
ethernet1  r2        ethernet1  1.1.1.2  1234:1::2
ethernet2  r3        ethernet2  1.1.1.6  1234:2::2
```
ping from `r1@eth1`
```
r1#ping 1.1.1.2 vrf v1
pinging 1.1.1.2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=1/2/5/12

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

r1#ping 1234:2::2 vrf v1
pinging 1234:2::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/4/16
r1#
```
#### 4.2.2  **router** `r2`
```
r2#sh lldp nei
interface  hostname  iface      ipv4      ipv6
ethernet1  r1        ethernet1  1.1.1.1   1234:1::1
ethernet2  r4        ethernet2  1.1.1.10  1234:3::2
```
ping from `r2@eth1`
```
r2#ping 1.1.1.1 vrf v1
pinging 1.1.1.1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/3/8

r2#ping 1234:1::1 vrf v1
pinging 1234:1::1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/8/22
```
ping from `r2@eth2`
```
r2#ping 1.1.1.10 vrf v1
pinging 1.1.1.10, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/3/6

r2#ping 1234:3::2 vrf v1
pinging 1234:3::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/2/4/14
r2#
```
#### 4.2.3  **router** `r3`
```
r3#sh lldp nei
interface  hostname  iface      ipv4      ipv6
ethernet1  r4        ethernet1  1.1.1.14  1234:4::2
ethernet2  r1        ethernet2  1.1.1.5   1234:2::1
```
ping from `r3@eth1`
```
r3#ping 1.1.1.14 vrf v1
pinging 1.1.1.14, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/5/10
r3#ping 1234:4::2 vrf v1
r3#ping 1234:4::2 vrf v1
pinging 1234:4::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/0/1/9
```
ping from `r3@eth2`
```
r3#ping 1.1.1.5 vrf v1
r3#ping 1.1.1.5 vrf v1
pinging 1.1.1.5, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/2/9/15
r3#ping 1234:2::1 vrf v1
r3#ping 1234:2::1 vrf v1
pinging 1234:2::1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/4/12
r3#
```

#### 4.2.4  **router** `r4`
```
r4#sh lldp nei
interface  hostname  iface      ipv4      ipv6
ethernet1  r3        ethernet1  1.1.1.13  1234:4::1
ethernet2  r2        ethernet2  1.1.1.9   1234:3::1
```
ping from `r4@eth1`

```
r4#ping 1.1.1.13 vrf v1
pinging 1.1.1.13, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/0/1/17

r4#ping 1234:4::1 vrf v1
pinging 1234:4::1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/4/17
```
ping from `r4@eth2`

```
r4#ping 1.1.1.9 vrf v1
pinging 1.1.1.9, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/0/1/5

r4#ping 1234:3::1 vrf v1
pinging 1234:3::1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=0/1/3/12
r4#
```

## 4 Conclusion
This section demonstrated:

- How to implement a local square topology:
    - by defining UNIX Socket pair
    - and lauching multiple freeRtr processes on the same host
- How to verify connectivity from each node of the topology
- This article demonstrated how freeRtr leverage UNIX UDP socket in order to forward packet

freeRtr in pure UNIX UDP socket mode is extremely useful when you want to simulate various topologies. In our example, `127.0.0.1` (localhost) was used, but of course any IP could have been used as long as the host somehow can reach the other IPs. With this mechanism, one can simulate an entire real service provider network. The only limitation is the inherent availability of hardware server resources such as CPU and RAM.
!!! Note
    One can says: "Simulation is great ! But what about effectively switch traffic IRL ?" And this is a fair comment ! In the next article we will see how to bind one freeRtr interface socket to a Linux network interface and start interacting with others hosts in the Local Area network. So stay tuned !

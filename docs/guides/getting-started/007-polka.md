# **Let’s enable PolKA**

## 1 Overview

Source routing (SR) is a prominent alternative to table-based routing for reducing the number of network states. In this approach, a source adds a route label in the packet header to provide deterministic paths for traffic engineering. The residue number system (RNS) is a promising way of executing fully stateless SR, in which forwarding decisions rely on a simple modulo operation over a route label. In this context, PolKA (Polynomial Key-based Architecture), explores binary polynomial arithmetic to propose a novel RNS-based SR. Herein, this tutorial shows how to enable PolKA in FreeRouter, create tunnels and migrate between different tunnels.


## 2 freeRtr network example
### 2.1 Diagram
The demo implements a square topology:
- core nodes are `r1`, `r2`, `r3`, `r4`
- edge nodes are `r5`, `r6`
```
r5----e3----r1----e1----r4
            |            |
            |            |
            e2          e2
            |            |
            |            |
r6----e3----r2----e1----r3
```
This topology presents two paths between r5 and r6, which will be used to create PolKA tunnels:
- A shortest path: `r1`- `r2`
- A longest path: `r1`- `r2`-`r3`-`r4`

### 2.1 Diagram

### 2.2 Core Nodes configuration
#### 2.2.1  **routers** `r1`, `r2`, `r3`, `r4`

`r1-hw.txt`

```
int eth1 eth 0000.1111.0001 127.0.0.1 16011 127.0.0.1 16021
int eth2 eth 0000.1111.0003 127.0.0.1 16013 127.0.0.1 16023
int eth3 eth 0000.1111.0005 127.0.0.1 16015 127.0.0.1 16025
tcp2vrf 2121 v1 23
```

`r1-sw.txt`

```
hostname R1
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.1.1.1
 segrout 20 1
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.1.1
 segrout 20 1
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 1 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R1
 vrf forwarding v1
 ipv4 address 20.20.20.1 255.255.255.255
 ipv6 address 2020::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R1@eth1 --> R4@eth1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1111:1::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet2
 description R1@eth2 --> R2@eth3
 vrf forwarding v1
 ipv4 address 2.2.2.2 255.255.255.252
 ipv6 address 2222::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet3
 description R1@eth3 --> R5@eth1
 vrf forwarding v1
 ipv4 address 11.11.11.2 255.255.255.252
 ipv6 address 1111::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec logging
 exec colorize prompt
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end
```

`r2-hw.txt`

```
int eth1 eth 0000.2222.0001 127.0.0.1 26011 127.0.0.1 26021
int eth2 eth 0000.2222.0002 127.0.0.1 26012 127.0.0.1 26022
int eth3 eth 0000.2222.0003 127.0.0.1 16023 127.0.0.1 16013
tcp2vrf 2222 v1 23
```

`r2-sw.txt`

```
hostname R2
!
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.2.2.2
 segrout 20 2
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.2.2
 segrout 20 2
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 2 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R2
 vrf forwarding v1
 ipv4 address 20.20.20.2 255.255.255.255
 ipv6 address 2020::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R2@eth1 --> R6@eth1
 vrf forwarding v1
 ipv4 address 7.7.7.2 255.255.255.252
 ipv6 address 7777::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet2
 description R2@eth2 --> R3eth1
 vrf forwarding v1
 ipv4 address 6.6.6.1 255.255.255.252
 ipv6 address 6666::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet3
 description R2@eth3 --> R1@eth2
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.252
 ipv6 address 2222::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec logging
 exec colorize prompt
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end
```


`r3-hw.txt`

```
int eth1 eth 0000.3333.0002 127.0.0.1 26022 127.0.0.1 26012
int eth2 eth 0000.3333.0003 127.0.0.1 46023 127.0.0.1 46013
tcp2vrf 2323 v1 23
```

`r3-sw.txt`

```
hostname R3
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.3.3.3
 segrout 20 3
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.3.3
 segrout 20 3
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 3 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R3
 vrf forwarding v1
 ipv4 address 20.20.20.3 255.255.255.255
 ipv6 address 2020::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R3@eth1 --> R2@eth2
 vrf forwarding v1
 ipv4 address 6.6.6.2 255.255.255.252
 ipv6 address 6666::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet2
 description R3@eth2 --> R4@eth2
 vrf forwarding v1
 ipv4 address 3.3.3.1 255.255.255.252
 ipv6 address 3333::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec logging
 exec colorize prompt
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end
```

`r4-hw.txt`

```
int eth1 eth 0000.4444.0001 127.0.0.1 16021 127.0.0.1 16011
int eth2 eth 0000.4444.0003 127.0.0.1 46013 127.0.0.1 46023
tcp2vrf 2424 v1 23
```

`r4-sw.txt`

```
hostname R4
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.4.4.4
 segrout 20 4
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.4.4
 segrout 20 4
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 4 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R4
 vrf forwarding v1
 ipv4 address 20.20.20.4 255.255.255.255
 ipv6 address 2020::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R4@eth1 --> R1@eth1
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.252
 ipv6 address 1111:1::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet2
 description R4@eth2 --> R3@eth2
 vrf forwarding v1
 ipv4 address 3.3.3.2 255.255.255.252
 ipv6 address 3333::2 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec logging
 exec colorize prompt
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end

```
#### 2.2.1  **Edge-Nodes-Routers** `r5`, `r6`

`r5-hw.txt`

```
int eth1 eth 0000.1111.0001 127.0.0.1 16025 127.0.0.1 16015
tcp2vrf 2525 v1 23
```

`r5-sw.txt`

```
hostname R5
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.11.11.11
 segrout 20 11
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.11.11
 segrout 20 11
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 11 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R5
 vrf forwarding v1
 ipv4 address 20.20.20.11 255.255.255.255
 ipv6 address 2020::11 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R5@eth1 --> R1@eth3
 vrf forwarding v1
 ipv4 address 11.11.11.1 255.255.255.252
 ipv6 address 1111::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface tunnel1
 description POLKA tunnel shortest ipv4 from R5 -> R6
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 20.20.20.7
 tunnel domain-name 20.20.20.1 20.20.20.2
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 30.30.30.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 description POLKA tunnel longuest ipv4 from R5 -> R6
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 20.20.20.7
 tunnel domain-name 20.20.20.1 20.20.20.4 20.20.20.3 20.20.20.2
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 40.40.40.1 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel3
 description POLKA tunnel shortest ipv6 from R5 -> R6
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2020::7
 tunnel domain-name 2020::1 2020::2
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 3030::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel4
 description POLKA tunnel longues ipv6 from R5 -> R6
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2020::7
 tunnel domain-name 2020::1 2020::4 2020::3 2020::2
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 4040::1 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec colorize prompt
 exec logging
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end
```
`r6-hw.txt`

```
int eth1 eth 0000.1717.0001 127.0.0.1 26021 127.0.0.1 26011
tcp2vrf 2626 v1 23
```

`r6-sw.txt`

```
hostname R6
!
vrf definition v1
 rd 1:1
 exit
!
router lsrp4 1
 vrf v1
 router-id 10.7.7.7
 segrout 20 7
 redistribute connected
 exit
!
router lsrp6 1
 vrf v1
 router-id 10.6.7.7
 segrout 20 7
 redistribute connected
 exit
!
interface template1
 no description
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic dynamic
 polka enable 7 65536 20
 mpls enable
 router lsrp4 1 enable
 shutdown
 no log-link-change
 exit
!
interface loopback0
 description lo R6
 vrf forwarding v1
 ipv4 address 20.20.20.7 255.255.255.255
 ipv6 address 2020::7 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface ethernet1
 description R6@eth1 -> R2@eth1
 vrf forwarding v1
 ipv4 address 7.7.7.1 255.255.255.252
 ipv6 address 7777::1 ffff:ffff:ffff:ffff::
 template template1
 router lsrp6 1 enable
 no shutdown
 exit
!
interface tunnel1
 description POLKA tunnel from R6 -> R5
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 20.20.20.11
 tunnel domain-name 20.20.20.2 20.20.20.1
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 30.30.30.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel2
 description POLKA tunnel longuest ipv4 from R6 -> R5
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 20.20.20.11
 tunnel domain-name 20.20.20.2 20.20.20.3 20.20.20.4 20.20.20.1
 tunnel mode polka
 vrf forwarding v1
 ipv4 address 40.40.40.2 255.255.255.252
 no shutdown
 no log-link-change
 exit
!
interface tunnel3
 description POLKA tunnel shortest ipv6 from R6 -> R5
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2020::11
 tunnel domain-name 2020::2 2020::1
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 3030::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
interface tunnel4
 description POLKA tunnel longues ipv6 from R6 -> R5
 tunnel vrf v1
 tunnel source loopback0
 tunnel destination 2020::11
 tunnel domain-name 2020::2 2020::3 2020::4 2020::1
 tunnel mode polka
 vrf forwarding v1
 ipv6 address 4040::2 ffff:ffff:ffff:ffff::
 no shutdown
 no log-link-change
 exit
!
server telnet tel
 security protocol telnet
 exec timeout 10000000
 exec logging
 exec colorize prompt
 no exec authorization
 no login authentication
 login logging
 vrf v1
 exit
!
end
```

## 3 Verification
### 3.1 Launch all nodes

Run `r1`, `r2`, `r3`,`r4`, `r5`, `r6` in different terminal windows:

- **Run** `r1`
`java -jar rtr.jar routersc r1-hw.txt r1-sw.txt`

- **Run** `r2`
`java -jar rtr.jar routersc r2-hw.txt r2-sw.txt`

- **Run** `r3`
`java -jar rtr.jar routersc r3-hw.txt r3-sw.txt`

- **Run** `r4`
`java -jar rtr.jar routersc r4-hw.txt r4-sw.txt`

- **Run** `r5`
`java -jar rtr.jar routersc r5-hw.txt r5-sw.txt`

- **Run** `r6`
`java -jar rtr.jar routersc r6-hw.txt r6-sw.txt`

### Or

Use `tmux` to run the entire topology in a single window.
To install it on a Linux Debian-based like Ubuntu, use `apt install -y tmux`.

Create a file
`vi start.sh`
```
#!/bin/bash

# Copyright [2019-2022] Universidade Federal do Espirito Santo
#                       Instituto Federal do Espirito Santo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

RTR=/<path freertr>/rtr.jar
HWSW=/<path configuration files>/

tmux new-session -d -s rare 'java -jar '$RTR' routersc '$HWSW'r1-hw.txt '$HWSW'r1-sw.txt'
tmux split-window -v -t 0 -p 50
tmux send 'java -jar '$RTR' routersc '$HWSW'r2-hw.txt '$HWSW'r2-sw.txt' ENTER;
tmux split-window -h -t 0 -p 50
tmux send 'java -jar '$RTR' routersc '$HWSW'r3-hw.txt '$HWSW'r3-sw.txt' ENTER;
tmux split-window -h -t 2 -p 50
tmux send 'java -jar '$RTR' routersc '$HWSW'r4-hw.txt '$HWSW'r4-sw.txt' ENTER;
tmux split-window -v -t 0 -p 50
tmux send 'java -jar '$RTR' routersc '$HWSW'r5-hw.txt '$HWSW'r5-sw.txt' ENTER;
tmux split-window -v -t 2 -p 50
tmux send 'java -jar '$RTR' routersc '$HWSW'r6-hw.txt '$HWSW'r6-sw.txt' ENTER;
tmux select-layout tiled
tmux a;
```

### 3.2 Access by Telnet

To access routers by telnet use `telnet <ip address> <port>`.

For Example:

`telnet 127.0.0.1 2525`


### 3.3 Verifying the tunnel is working on router r5

`R5# Show interfaces summary`

```
interface  state  tx     rx     drop
template1  admin  50     0      345
loopback0  up     3273   0      0
ethernet1  up     17231  32368  0
ethernet2  up     5760   0      0
tunnel1    up     330    0      0
tunnel2    up     0      0      0
tunnel3    up     460    0      0
tunnel4    up     230    0      0
```
If all tunnels are `up`, it's a good signal.

For verification on router `R6`, just connect and set the commands above.


### 3.3 Testing connectivity between `R5` to `R6` using PolKA

- **Shortest Path tunnel1 ipv4**

`R5#ping 30.30.30.2 vrf v1`
```
pinging 30.30.30.2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, sgt=0, flow=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/sum=0/0/3/8, ttl min/avg/max=255/255/255, tos min/avg/max=0/0/0
```
![Shortest Path](/img/upload_fc7ec37244d45d0fc56cf6e5477a1a47.png)

- **Longest Path tunnel2 ipv4**

`R5#ping 40.40.40.2 vrf v1`
```
pinging 40.40.40.2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, sgt=0, flow=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/sum=3/4/6/23, ttl min/avg/max=255/255/255, tos min/avg/max=0/0/0
```
![Longuest Path](/img/upload_964c33bf6e483c09d210eab98bcc59cc.png)


- **Shortest Path tunnel3 ipv6**

`R5#ping 3030::2 vrf v1`
```
pinging 3030::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, sgt=0, flow=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/sum=0/0/1/2, ttl min/avg/max=255/255/255, tos min/avg/max=0/0/0
```
![Shortest Path](/img/upload_6eb53de9dc87aa3f4143a4183903573b.png)

- **Longest Path tunnel4 ipv6**

`R5#ping 4040::2 vrf v1`

```
pinging 4040::2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, sgt=0, flow=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/sum=0/0/0/2, ttl min/avg/max=255/255/255, tos min/avg/max=0/0/0
```
![Longuest Path](/img/upload_c82ee2d30c8907e0ec60648e89cc10d0.png)


### 3.4 Visualizing route table

- **Route table ipv4**

`R5#show ipv4 route v1`

```
typ  prefix          metric  iface      hop         time
C    0.0.0.0/32      0/0     ethernet2  null        00:15:39
L    1.1.1.0/30      70/10   ethernet1  11.11.11.2  00:15:29
L    2.2.2.0/30      70/10   ethernet1  11.11.11.2  00:15:29
L    3.3.3.0/30      70/20   ethernet1  11.11.11.2  00:15:29
L    6.6.6.0/30      70/20   ethernet1  11.11.11.2  00:15:29
L    7.7.7.0/30      70/20   ethernet1  11.11.11.2  00:15:29
C    11.11.11.0/30   0/0     ethernet1  null        00:15:40
LOC  11.11.11.1/32   0/1     ethernet1  null        00:15:40
L    20.20.20.1/32   70/10   ethernet1  11.11.11.2  00:15:29
L    20.20.20.2/32   70/20   ethernet1  11.11.11.2  00:15:29
L    20.20.20.3/32   70/30   ethernet1  11.11.11.2  00:15:29
L    20.20.20.4/32   70/20   ethernet1  11.11.11.2  00:15:29
L    20.20.20.7/32   70/30   ethernet1  11.11.11.2  00:15:29
C    20.20.20.11/32  0/0     loopback0  null        00:15:42
C    30.30.30.0/30   0/0     tunnel1    null        00:15:29
LOC  30.30.30.1/32   0/1     tunnel1    null        00:15:29
C    40.40.40.0/30   0/0     tunnel2    null        00:15:29
LOC  40.40.40.1/32   0/1     tunnel2    null        00:15:29
```

- **Route table ipv6**

`R5#show ipv6 route v1`

```
typ  prefix        metric  iface      hop      time
C    1111::/64     0/0     ethernet1  null     00:18:17
LOC  1111::1/128   0/1     ethernet1  null     00:18:17
L    1111:1::/64   70/10   ethernet1  1111::2  00:18:05
L    2020::1/128   70/10   ethernet1  1111::2  00:18:05
L    2020::2/128   70/20   ethernet1  1111::2  00:18:05
L    2020::3/128   70/30   ethernet1  1111::2  00:18:05
L    2020::4/128   70/20   ethernet1  1111::2  00:18:05
L    2020::7/128   70/30   ethernet1  1111::2  00:18:05
C    2020::11/128  0/0     loopback0  null     00:18:19
L    2222::/64     70/10   ethernet1  1111::2  00:18:05
C    3030::/64     0/0     tunnel3    null     00:18:01
LOC  3030::1/128   0/1     tunnel3    null     00:18:01
L    3333::/64     70/20   ethernet1  1111::2  00:18:05
C    4040::/64     0/0     tunnel4    null     00:18:01
LOC  4040::1/128   0/1     tunnel4    null     00:18:01
L    6666::/64     70/20   ethernet1  1111::2  00:18:05
L    7777::/64     70/20   ethernet1  1111::2  00:18:05
```

### 3.4 Visualizing PolKA routeid

- **Routeid Tunnel 1**

`R5#show polka routeid tunnel1`

```
mode  routeid
hex   00 00 00 00 00 00 00 00 00 00 1c 59 b8 b1 a4 ea
poly  111000101100110111000101100011010010011101010
```

- **Routeid Tunnel 2**

`R5#show polka routeid tunnel2`

```
mode  routeid
hex   00 00 00 00 00 00 41 3b fd 39 6d 38 a0 07 71 39
poly  1000001001110111111110100111001011011010011100010100000000001110111000100111001
```
### 3.5 Tested on

These configurations have been tested on the following operating systems: MacOS Monterey 12.2 and Ubuntu 21.04

## 4 Conclusion
This section demonstrated:

- How to launch many automated routers with bash script using tmux
- How to use a template interface on freertr
- How to enable PolKA in a square topology
- How to create PolKA tunnels
- How to verify connectivity

You learned how to enable PolKA protocol using FreeRouter tunnels. You also learned how to use Link-state Routing Protocol (LSRP).

## 5 References:

https://ieeexplore.ieee.org/document/9165501

https://github.com/nerds-ufes/polka

http://www.freertr.org/

https://github.com/eversonscherrer/freertr/tree/main/polKa

https://github.com/eversonscherrer/dissector-polka

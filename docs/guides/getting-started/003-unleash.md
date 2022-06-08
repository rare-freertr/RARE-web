# **Unleash freeRtr to outside network !**

## 1 Overview
In [Hello freeRtr !](001-hello-world.md) and [Topology example](002-topology-example.md) we learned how to install freeRtr and create a 4 nodes topology. This is perfect in a network simulation use case, but this is basically useless as nodes are operating in an isolated environment.

In this article, we will learn how to bind freeRtr interfaces to existing Linux network host interfaces. freeRtr itself will become officially part of the existing network and will be able to communicate with any host in the local area network !

## 2 Installation
### 2.1 Pre-requisites
In order to illustrate this binding operation, I've added one new interfaces to my VirtualBox Debian guest OS.

```
ip a
...
4: enp0s9: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 08:00:27:25:43:31 brd ff:ff:ff:ff:ff:ff
...
```

As this interface is totally controlled by freeRtr we need to reset it:

```
ip addr flush dev enp0s9
```

In order to avoid future problem (disable TCP-offload)

```
cat <<EOF | sudo tee /root/tcp-offload-off.sh

#! /bin/bash

/sbin/ethtool -K $1 rx off
/sbin/ethtool -K $1 tx off
/sbin/ethtool -K $1 sg off
/sbin/ethtool -K $1 tso off
/sbin/ethtool -K $1 ufo off
/sbin/ethtool -K $1 gso off
/sbin/ethtool -K $1 gro off
/sbin/ethtool -K $1 lro off
/sbin/ethtool -K $1 rxvlan off
/sbin/ethtool -K $1 txvlan off
/sbin/ethtool -K $1 ntuple off
/sbin/ethtool -K $1 rxhash off

EOF
```
```
sudo chmod u+x /root/tcp-offload-off.sh
```
```
sudo /root/tcp-offload-off.sh enp0s9
```

Enable promiscuous mode and set MTU to 8192 as freeRtr is able to handle jumbo frames

```
ip link set enp9s9 up promisc on mtu 8192
```
Enable `enp0s9`

```
ip link set enp0s9 up
```


IPv6 will be handled by freeRtr, therefore we disable IPv6 from Linux perspective
```
echo 1 > /proc/sys/net/ipv6/conf/enp0s9/disable_ipv6
```

### 2.2 Additional freeRtr softwares
Let's add an additional interface definition `eth3`

- `eth3`, A-end:`127.0.0.1 1003` ---- B-end:`127.0.0.1 5003`

In this example B-end will be stitched to an existing Linux interface. `r1@eth3` which has socket `127.0.0.1 1003` will be bind to `enp0s9` Linux interface. In order to accomplish this,  we will use a simple tool called `pcapInt` part of freeRtr bundles

Let's first install freeRtr addtional tools bundle.

```
cd /rtr
wget freertr.org/rtr-x86_64.tar
tar xf rtr-x86_64.tar -C /rtr/
```
These tools are basically tools used to ensure freeRtr packet forwarding in different context and dataplane.


```
ls -1 *.bin
bundle.bin
hdlcInt.bin
mapInt.bin
modem.bin
p4dpdk.bin
p4emu.bin
p4pkt.bin
pcap2pcap.bin
pcapInt.bin
rawInt.bin
sender.bin
stdLin.bin
tapInt.bin
ttyLin.bin
vlan.bin
```

## 3 Configuration
### 3.1 freeRtr "hardware" file
We will re-use `r1` hardware definition file from previous articles and add `eth3`

```
int eth3 eth 0000.1111.0003 127.0.0.1 1003 127.0.0.1 5003
```

- `eth3` is identified by socket `127.0.0.1 1003` and remote end is `127.0.0.1 5003`

For learning sake, we will add a new keywords:

```
hwid MyDebianVM
tcp2vrf 2321 v1 23
```

- `hwid` is the hardware identifier shown usign the `show platform` command.
- `tcp2vrf` declare:
  -  a Linux host high port `2321`
  -  that is translated to port `23`
  -  into freeRtr VRF `v1` namespace

???+ info
     We will see the effect of these new keywords in the verification section.

### 3.2 freeRtr "configuration" file

```
hostname r1
!
vrf def v1
 rd 1:1
 exit
prefix-list p4
 sequence 10 permit 0.0.0.0/0 ge 0 le 0
 exit
prefix-list p6
 sequence 10 permit ::/0 ge 0 le 0
 exit
int eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.252
 ipv6 addr 1234:1::1 ffff:ffff::
 exit
int eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.5 255.255.255.252
 ipv6 addr 1234:2::1 ffff:ffff::
 exit
int eth3
 description r1@eth3[127.0.0.1 1003]->enp0s9[127.0.0.1 5003]
 lldp ena
 vrf for v1
 ipv4 address dynamic 255.255.255.0
 ipv4 gateway-prefix p4
 ipv4 dhcp-client enable
 ipv4 dhcp-client early
 ipv6 address dynamic ffff:ffff:ffff:ffff::
 ipv6 gateway-prefix p6
 ipv6 slaac
 no shutdown
 no log-link-change
 exit
!
```

- We are adding a telnet server configuration for OOBM from the Linux host VM:
  - port is `23`
  - vrf `v1`
  - `logging` will be applied
  - `exec logging` is logging all command executed from freeRtr cli prompt
  - `login logging` is logging all user access freeRtr cli

- `logging` feature is also configured
  - `logging buffered` is the memory buffer in lines
  - `logging file` is the log file in Linux filesytem
  - `logging rotate` declare a rotation of the log file when the log reach `X` size in bytes

```
!
logging buffered debug 10240
logging file debug /var/log/freertr.log
logging rotate 655360000 /var/log/freertr.old
!
server telnet v1
 security protocol telnet
 exec logging
 login logging
 vrf v1
 exit
!
```

???+ info
     We will to check these new features in the verification section.

### 3.3 Let's unleash freeRtr to the outside network !
Let's launch first `r1`
```
java -jar rtr.jar routersc r1-hw.txt r1-sw.txt


#######                         ##################
 ##  ##                                 ##
 ##   # ## ###   #####   #####  ## ###  ## ## ###
 ## #    ### ## ##   ## ##   ##  ### ## ##  ### ##
 ####    ##  ## ####### #######  ##  ## ##  ##  ##
 ## #    ##     ##      ##       ##     ##  ##
 ##      ##     ##   ## ##   ##  ##     ##  ##
####     ##      #####   #####   ##     ##  ##

freeRouter v21.8.21-cur, done by cs@nop.

place on the web: http://www.freertr.org/
license: http://creativecommons.org/licenses/by-sa/4.0/
quote1: make the world better
quote2: if a machine can learn the value of human life, maybe we can too
quote3: be liberal in what you accept, and conservative in what you send
quote4: the beer-ware license for selected group of people:
cs@nop wrote these files. as long as you retain this notice you
can do whatever you want with this stuff. if we meet some day, and
you think this stuff is worth it, you can buy me a beer in return

info cfg.cfgInit.doInit:cfgInit.java:660 booting
info cfg.cfgInit.doInit:cfgInit.java:802 initializing hardware
info cfg.cfgInit.doInit:cfgInit.java:808 applying defaults
info cfg.cfgInit.doInit:cfgInit.java:815 applying configuration
info cfg.cfgInit.doInit:cfgInit.java:845 boot completed
welcome
line ready
r1#
```
`r1` running-configuration
```
r1#sh run
hostname r1
buggy
!
!
vrf definition v1
 rd 1:1
 exit
!
int eth1
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.252
 ipv6 addr 1234:1::1 ffff:ffff::
 exit
int eth2
 lldp ena
 vrf for v1
 ipv4 addr 1.1.1.5 255.255.255.252
 ipv6 addr 1234:2::1 ffff:ffff::
 exit
interface ethernet3
 description r1@eth3[127.0.0.1 1003]->enp0s9[127.0.0.1 5003]
 lldp enable
 vrf forwarding v1
 ipv4 address dynamic 255.255.255.0
 ipv4 gateway-prefix p4
 ipv4 dhcp-client enable
 ipv4 dhcp-client early
 ipv6 address dynamic ffff:ffff:ffff:ffff::
 ipv6 gateway-prefix p6
 ipv6 slaac
 no shutdown
 no log-link-change
 exit
!
...
!
server telnet tel
 security protocol telnet
 no exec authorization
 no login authentication
 vrf v1
 exit
!
!
end

r1#
```

Now, it is time to bind  `r1@eth3` to `epn0s9`. First let's run `pcapInt` without any parameter.

```
./pcapInt.bin
using: ./pcapInt.bin <iface> <lport> <raddr> <rport> [laddr]
   or: ./pcapInt.bin <command>
commands: l=list interfaces
          v=version
          h=this help
```

Now, let's use `pcapInt` in order to bind `r1@eth1` to `epn0s9`.

- `r1@eth3` socket to `enp0s9` using socket `127.0.0.1 5003`

```
./pcapInt.bin enp0s9 5003 127.0.0.1 1003 127.0.0.1
binded to local port 127.0.0.1 5003.
will send to 127.0.0.1 1003.
pcap version: libpcap version 1.10.0 (with TPACKET_V3)
opening interface enp0s9
serving others
> d
iface counters:
                      packets                bytes
received                   24                 6104
sent                        0                    0

> h
commands:
h - this help
q - exit process
d - display counters
c - clear counters

> 
```

## 4 Verification
Port translation verification via tcp2vrf`2321` -> `23`

```
telnet 127.0.0.1 2321
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
welcome
line ready
r1#
```
Hardware information verification

```
r1#show platform
freeRouter v21.8.21-cur, done by cs@nop.

name: r1
hwid: MyDebianVM
uptime: since 2021-08-27 16:13:28, for 00:09:59
reload: -
hwcfg: r1-hw.txt
swcfg: r1-sw.txt
cpu: 1*amd64
mem: free=6452k, max=502m, used=32m
host: Linux v5.10.0-8-amd64
java: Debian v11.0.12 @ /usr/lib/jvm/java-11-openjdk-amd64
jspec: Oracle Corporation (Java Platform API Specification) v11
vm: Debian (OpenJDK 64-Bit Server VM) v11.0.12+7-post-Debian-2
vmspec: Oracle Corporation (Java Virtual Machine Specification) v11
class: v55.0 @ rtr.jar

r1#
```
`eth1` DHCP client verification

```
show ipv4 int                                                                                                               
interface  state  address         netmask
loopback0  up     2.2.2.1         255.255.255.255
ethernet1  up     1.1.1.1         255.255.255.252
ethernet2  up     1.1.1.5         255.255.255.252
ethernet3  up     192.168.136.67  255.255.255.0

r1#show ipv6 int                                                                                                               
interface  state  address                            netmask
loopback0  up     4321::1                            ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
ethernet1  up     1234:1::1                          ffff:ffff::
ethernet2  up     1234:2::1                          ffff:ffff::
ethernet3  up     2a01:e0a:159:2856:200:11ff:fe11:3  ffff:ffff:ffff:ffff::

r1#sh int eth3                                                                                                                 
ethernet3 is up (since 00:02:29, 1 changes)
 description: r1@eth3[127.0.0.1 1003]->enp0s9[127.0.0.1 5003]
 type is ethernet, hwaddr=0000.1111.0003, mtu=1500, bw=100mbps, vrf=v1
 ip4 address=192.168.136.67/24, netmask=255.255.255.0, ifcid=347805334
 ip6 address=2a01:e0a:159:2856:200:11ff:fe11:3/64, netmask=ffff:ffff:ffff:ffff::, ifcid=752263581
 received 3555 packets (810051 bytes) dropped 0 packets (0 bytes)
 transmitted 18 packets (2714 bytes) promisc=false macsec=false
```

External connectitivy verification (ping Cloudfarre DNS)

```
r1#ping 1.1.1.1 vrf v1
pinging 1.1.1.1, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
!!!!!
result=100%, recv/sent/lost/err=5/5/0/0, rtt min/avg/max/total=5/5/7/33
r1#
```

Check my LAN OpenWRT wifi router
```
r1#ping 192.168.136.2 vrf v1
pinging 192.168.136.2, src=null, vrf=v1, cnt=5, len=64, tim=1000, gap=0, ttl=255, tos=0, fill=0, sweep=false, multi=false, detail=false
.!!!!
result=80%, recv/sent/lost/err=4/5/1/0, rtt min/avg/max/total=0/1/2/1004
r1#
r1#ssh 192.168.136.2 /user root vrf v1
 - connecting to 192.168.136.2 22
password:

 - securing connection



BusyBox v1.30.1 () built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 19.07.4, r11208-ce6496d796
 -----------------------------------------------------
root@WTF-WIFI:~#
```

Congratulations ! You have successfully managed to insert freeRtr into your existing infrastructure.

## 5 Conclusion
This section demonstrated:

- How to complete freeRtr installation by installating freeRtr tools bundle
- How to reset an existing Linux interface so that it can be controlled by freeRtr
- Added a third interface to `r1`:
    - interface (`eth3` )
    - and its corresponding UNIX UDP sockets (`127.0.0.1 1003` )
- How bind a Linux interface through UDP socket `127.0.0.1 5003` using `pcapInt` tool included in the freeRtr addtional tools bundle.
- Configure `eth3` interface so that it could initiate IPv4 DHCP request and IPv6 SLAAC operation in order to get IPv4 and IPv6 address from local router acting as DHCP server and IPv6 SLAAC gateway.

!!! note
    The article demonstrated basic `ping` and `ssh` external connectivity. However, the real power of this setup is that from there, you can activate any IGP such as OSPF or ISIS on `eth3`. You can even push further connectivity extension by enabling multihop eBGP towards external system and start behaving as an ISP ... If you have the chance to have Service Provider able to provide you MPLS services, you'll get the possibility to extend MPLS service towards any of your internal host in your network. You have guessed it, you just got a hand on the most powerful open source network swiss army knife !
    In the next article, we will start implementing a small service provider with `r1`,`r2`,`r3`,`r4` so that the lab topology can appear as an external network. The first step will to implement an IGP !



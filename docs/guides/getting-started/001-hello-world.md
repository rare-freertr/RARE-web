# ** Hello freeRtr !**

## 1 Overview
As freeRtr's author mentions: "freeRouter is a free, open source router OS process, it speaks routing protocols, and (re)encapsulates packets on interfaces. it receives and sends packets through udp sockets".

Basically freeRtr is a control plane software that natively relies on UNIX UDP socket. Concretely, you can spawn an unlimited amount of router processes on the same host, and interconnect them via UNIX UDP sockets in order to implement a topology and simulate an entire network.

This is freeRtr in its simplest form running in default mode.
!!! Note
    Please note that this installation is meant to demonstrate freeRtr UNIX socket forwarding capability. If you are considering switching high traffic rate such as 10G, it is advised to run freeRtr alongside a DPDK or P4 hardware dataplane.

## 2 Installation
### 2.1 Operating system
Any Operating System architecture (amd64, x86, arm etc.) supporting Java platform. In the example below we will use Debian "buster".
```
lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster
```

### 2.2 Software dependency
freeRtr has been tested and working starting from Java 8. Of course it is recommended to use the latest and greatest Java runtime.
```
sudo apt-get install --no-install-recommends --no-install-suggests --yes default-jre-headless
```
### 2.4 Create freeRtr directory
For simplicity's sake we will use `/rtr` folder.
```
sudo mkdir /rtr
```
### 2.3 Download freeRtr binary
The freeRtr homepage is at `freertr.org`. Starting from this page, you'll find various resources such as source code (there is also a GitHub mirror), binaries, and other images that might be of your interest. From there we just download the freeRtr `jar` files.
```
cd /rtr
wget http://www.freertr.org/rtr.jar
```

## 3 Configuration
freeRtr needs two files in order to run properly:

- A hardware definition file
- A software configuration file
### 3.1 Hardware configuration file
This file encompasses definition of the router:

- platform information
- interfaces definition
- external port translation to freeRtr port namespace
- external process launched and watched by freeRtr
- ...

Let's give it the name `$hostname-hw.txt` (It can be of course any name)

- The router we will create is `r1` so the hardware file is:`r1-hw.txt`
- declare 2 interfaces for `r1`.

The format of interface declaration is:

```
int <intf_name> <intf_type> <intf_mac> <ip_socket_a> <port_socket_a> <ip_socket_b> <port_socket_b>
```
In its simplest form, `r1-hw.txt` is declaring 2 interfaces (`eth1`,`eth2`) of type `ethernet`

```
int eth1 eth 0000.1111.0001 127.0.0.1 1001 127.0.0.1 2001
int eth2 eth 0000.1111.0002 127.0.0.1 1002 127.0.0.1 3002
```

- `eth1` is identified by socket `127.0.0.1 1001` and remote end is `127.0.0.1 2001`
- `eth2` is identified by socket `127.0.0.1 1001` and remote end is `127.0.0.1 3002`


### 3.2 Software configuration file
This is basically `r1` freeRtr configuration similar to Cisco IOS `startup-config` file.
In the example below:

- you notice `eth1` and `eth2` that have been declared in the hardware file.
- These interface have `lldp` and an `ipv4` and `ipv6` addresses configured.
- In addition to that, we added a `lo0` that is of course not included in `r1-hw.txt` file as it is a logical interface.
- One peculiarity is that freeRtr enforces VRF usage. (in the example `vrf v1`) There is therefore no ambiguity related to the default VRF or VRF-aware features.

Let's give it the name `$hostname-sw.txt` (It can be of course any name)

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
!
```
### 3.3 Let's run our first freeRtr process !
Let's first try to launch freeRtr without any parameters:
```
java -jar /rtr/rtr.jar
java -jar /rtr/rtr.jar <parameters>
parameters:
  router <cfg>            - start router background, config url
  routerc <cfg>           - start router with console, config url
  routerw <cfg>           - start router with window, config url
  routercw <cfg>          - start router with console and window, config url
  routers <hwcfg> <swcfg> - start router from separate configs, config url, config url
  routera <swcfg>         - start router with sw config only, config url
  test <cmd>              - execute test command, command to execute
  show <cmd>              - execute show command, command to execute
  exec <cmd>              - execute exec command, command to execute
```
From the output above you observe some indications indicating how to launch freeRtr with various options. In our case we will then launch freeRtr with `r1-hw.txt` and `r1-sw.txt` and we also would like to have a CLI console access:

```
sudo java -jar rtr.jar routersc r1-hw.txt r1-sw.txt


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
`ri` running-configuration
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
interface loopback0
 no description
 vrf forwarding v1
 ipv4 address 2.2.2.1 255.255.255.255
 ipv6 address 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 no shutdown
 no log-link-change
 exit
!
interface ethernet1
 description r1@eth1 -> r2@eth1
 lldp enable
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.252
 ipv6 address 1234:1::1 ffff:ffff::
 no shutdown
  -=[more]=-
 no log-link-change
 exit
!
interface ethernet2
 description r1@eth2 -> r3@eth2
 lldp enable
 vrf forwarding v1
 ipv4 address 1.1.1.5 255.255.255.252
 ipv6 address 1234:2::1 ffff:ffff::
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
Congratulations! You have launched your first freeRtr router process using native UNIX UDP socket forwarding!

!!!+ info
     In the example above we spawned a freeRtr process with `sudo`, the reason for using it here is that freeRtr base directory is in `/rtr` and port below reserved port range. Other than that, freeRtr can be launched as a regular Unix user.

## 4 Conclusion
This section demonstrated:

- How to install and configure freeRtr on any OS able to run JVM
- How to create a freeRtr router process that has:
    - two interfaces (`eth1` and `eth2`)
    - `eth1` is UDP sockets `127.0.0.1 1001`, remote end is `127.0.0.1 2001`
    - `eth2` is UDP sockets `127.0.0.1 1002`, remote end is `127.0.0.1 3002`

- How to start freeRtr
!!! Note
    Most of you have probaly noticed that `r1` has both `eth1` and `eth2` interfaces connected to nowhere. And you are right ! We will see in the [next "getting started" article](002-topology-example.md) how to implement a entire local topology by interconnecting through UDP sockets 4 freeRtr router processes.




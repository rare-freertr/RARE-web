# **Basics**
## Configuration mode
RARE/freeRtr configuration is available via `configuration mode`.

It is denoted from the CLI by `rare(cfg)#` prompt.

```
rare#conf t
rare(cfg)#
```
## Save configuration

Configuration modifications are made persistent by writing it into the flash disk using the commands below:

```
rare(cfg)#exit
rare#write
% saving configuration
% success
rare#
```
or, if you're in configuration mode:

```
rare(cfg)#do write
% saving configuration
% success
rare(cfg)#exit
rare#
```
## Contextual help

 * `?` from CLI will let you access contextual help.


```
FREERTR#show ipv4 ospf ?                                                                                                       
  <num> - process id

FREERTR#show ipv4 ospf 1 ?                                                                                                     
  database        - list of lsas in area
  graph           - graph about last spf
  hostnames       - hostnames from database
  interface       - list of interfaces
  lnkinconsistent - inconsistent advertisements of metrics
  metric          - list of metrics
  neighbor        - list of neighbors
  nhinconsistent  - inconsistent advertisements of next hops
  originate       - list of routes originated locally
  othertopology   - topology of other node
  othertree       - tree of other node
  route           - list of routes in area
  spf             - information about last spf
  topology        - topology about last spf
  tree            - tree about last spf
```

```
FREERTR#conf t                                                                                                                 
FREERTR(cfg)#access-list MY_ACL_1                                                                                              
FREERTR(cfg-acl)#exit                                                                                                           
FREERTR(cfg)#access-list MY_ACL_2                                                                                              
FREERTR(cfg-acl)#exit                                                                                                          
FREERTR(cfg)#access-list ?                                                                                                     
  <name>               - name of access list
  MY_ACL_1             - name of access list
  MY_ACL_2             - name of access list

```

 * `<tab>` will provide you CLI contextual autocompletion 

!!! Note
    `<tab>` provides not only command autocompletion but also contextual object autocompletion among a list of object you might have created previously. In the example above try to type: `access-list MY_` + `<tab>` in configutation mode. 

## Dataplane configuration 
!!! IMPORTANT
    Dataplane parameters defined in RARE/FreeRtr control-plane are defined in `server p4lang` configuration stanza:

    * VRF: Enable VRF (L3) at the dataplane level
    * bridge: Enable bridge (L2) at the dataplane level
    * Interface: Enable interface at the dataplane level
    * Logical interfaces: Enable logical interface such as VLAN, Tunnel Hairpin etc. at the dataplane level   

They have to be exported in `server p4lang p4` such as the example below:
```
server p4lang p4
export-bridge 1000
export-bridge 1001
export-vrf switch_test 1
export-vrf switch_test_2 2
export-port sdn1 40 10 0 1 0
export-port sdn3 276 100 0 1 0
export-port sdn5 292 10 0 1 0
export-port sdn1.10 dynamic 100 0 1 0
export-port sdn1.20 dynamic 100 0 1 0
exit
```
In this example:

* `VRF(s)` have assigned the numbers `1` and `2` It can be arbitrary integer values.
* `Bridges` have assigned the numbers `1000` and `1001`. It can be arbitrary integer values. 

* Nevertheless, the `port-mapping` of the `interfaces` needs to be assigned using the [interface configuration document](/guides/installation/wedge100bf32/interface/).

* For the `VLAN sub-interfaces`, the mapping is configured using the keyword `dynamic` 

!!! Warning
    this section is by no means complete. RARE/freeRtr exposes an extensive list of CLI features. 
    
    Please refers to these blogs articles should you are "greedy" of more features:
    
    * ["conf t"](https://y.freertr.org/UL7TC)
    * ["show/view/watch/display/differ"](https://y.freertr.org/mL7TC)
    * ["Let's make you feel at home !"](https://y.freertr.org/Er-TC)
    * [""Saving private OpenWRT", thanks freeRouter's TFTP server !"](https://y.freertr.org/uw89CQ)

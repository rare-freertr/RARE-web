# **Bridge and Virtual Routing and Fording (VRF)**

In RARE/freeRtr you have 2 major constructs:

* bridge for L2
* VRF for L3

## Bridge [**_ (Wikipedia) _**](https://en.wikipedia.org/wiki/Network_bridge)
> A network bridge is a computer networking device that creates a single, aggregate network from multiple communication networks or network segments. This function is called network bridging.

In RARE/freeRtr, `bridge` in RARE/FreeRtr can be configured with the following command:

```
FREERTR(cfg)#bridge ?                                                                                                          
  <num> - number of bridge group

FREERTR(cfg)#bridge 1 ?                                                                                                        
  <cr>
```

!!! Warning
    Do not forget to export `bridge`(s) into `server p4lang` so that the dataplane will take it into account into its hardware forwarding operation

## Virtual routing forwarding [**_ (Wikipedia) _**](https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding)

> `Virtual Routing Forwarding (VRF)` is a technology included in `IP (Internet Protocol)` network routers that allows users to configure multiple routing table instances to simultaneously co-exist within the same router. `VRFs` are used for network isolation/virtualization at Layer 3 of the OSI model, the overlapping `IP addresses` can be used without conflicting because the multiple routing instances are independent and can select different outgoing interfaces. A `VRF` requires a `forwarding table` that designates the `next-hop` for each data packet, a list of devices that may be called upon to forward the packet and a set of rules and routing protocols that govern how the packets will be forwarded. These tables prevent traffic from being forwarded outside a specific `VRF path` and also keep out traffic that should remain outside the `VRF path`. Thus, the packets will be forwarded only between interfaces that `belongs to the same VRF`. 

In RARE/freeRtr, `vrf` in RARE/FreeRtr can be configured with the following command:

```
AMS0001(cfg)#vrf definition MY_?                                                                                               
type <name> to name of vrf

AMS0001(cfg)#vrf definition MY_VRF ?                                                                                           
  <cr>

AMS0001(cfg)#exit
```

!!! Warning
    Do not forget to export `vrf`(s) into `server p4lang` so that the dataplane will take it into account into its hardware forwarding operation
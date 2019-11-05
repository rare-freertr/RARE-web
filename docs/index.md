# Overview 

**RARE** (**R**outer for **A**cademia, **R**esearch & **E**ducation) is an ongoing effort under the [GÉANT 3rd programme](https://www.geant.org/Projects/GEANT_Project_GN4-3) which focus on determining if a routing software platform solution can fit **R&E** use cases. 
The project aims to integrate different pieces of software related to these building blocks:

* `control plane`: **RARE** uses **[FreerTr](http://freerouter.nop.hu/)** under the hood used as the control plane component
* `data plane`: **[P4](https://p4.org/)** is used to describe the behavioral model of **RARE** data plane 
* and `communication interface` between the control plane and data plane: Interface compliant to [P4Runtime](https://github.com/p4lang/p4runtime) specification ensure this function

A key part of the work consists in enabling a control plane software to pilot a data plane via a programmatic interface. 

**P4** is such a language proposing an interface that allows data plane programmability. 

!!! Note
    **P4** core language attempts to be as much as possible independent from the target or NPU processor architecture. 
    However architecture dependance is still prominent. Code adjustments followed by a target specific compilation is necessary if you want to run your p4 program on a specific architecture.


You'll in this page various guides that will help you deploy and use **RARE/FreerTr** router.

# Guides 

All the guides falls under 4 categories:

* `Network management` - features related to the network management plane  (i.e, SSH, TACACS, RADIUS, streaming telemetry)
* `Routing` - features related to the control plane. (i.e: OSPF, integrated IS-IS, LDP, Segment Routing, BGP) 
* `Network service` - features belonging to the sevice plane such as IPv4 and IPv6  L3VPN, point to point L2VPN.
* `FreerTr data plane` - **FreerTr** is a versatile control plane that supports various dataplane such as:
    * UNIX raw socket: multiple FreerTr instance can run on the same host in order to simulate a complete lab 
    * regular network UNIX device: You can bind FreerTr interfaces to UNIX network devices. 
        * A typical use case is to run FreerTa as pure BGP route reflector control plane in a Service Provider backbone
        * An other use case is to run FreerTR as a pure BGP route reflector control plane in order to ensure pod to pod communication in a Kubernetes cluster
    * OpenFlow 
    * Various P4 dataplane
        * p4lang: bmv2
        * BAREFOOT: TOFINO
        * P4 on FPGA: [<- under study] 


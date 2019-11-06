# **Overview** 

**RARE** (**R**outer for **A**cademia, **R**esearch & **E**ducation) is an ongoing effort under the [GÉANT 3rd programme](https://www.geant.org/Projects/GEANT_Project_GN4-3) which focus on determining if a routing software platform solution can fit **R&E** use cases. 
The project aims to integrate different pieces of software related to these building blocks:

* **control plane**: **RARE** uses **[FreerTr](http://freerouter.nop.hu/)** under the hood used as the control plane component
* **data plane**: **[P4](https://p4.org/)** is used to describe the behavioral model of **RARE** data plane 
* and **communication interface** between the control plane and data plane: Interface compliant to [P4Runtime](https://github.com/p4lang/p4runtime) specification ensure this function

A key part of the work consists in enabling a control plane software to pilot a data plane via a programmatic interface. 

**[P4](https://p4.org/)** is such a language proposing an interface that allows data plane programmability. 

!!! Note
    **[P4](https://p4.org/)** core language attempts to be as much as possible independent from the target or NPU processor architecture. 
    However architecture dependance is still prominent. Code adjustments followed by a target specific compilation is necessary if you want to run your p4 program on a specific architecture.


You'll find in this page various guides that will help you deploy and use **RARE/FreerTr** router.

## **Guides** 

Each guide falls under one of the 4 main categories listed below and is applicable to IPv4 and IPv6:

### **Network management**
 - features related to the network management plane  
    * Management
        * SSH, TELNET client/server
    * AAA security model
        * TACACS, RADIUS client/server
    * Accounting
        * Streaming telemetry
### **Routing**
 - features related to the control plane
    * IGP 
        * OSPF, integrated IS-IS, LSRP (FreerTr own IGP)
    * Label transport distribution 
        * LDP, IS-IS & OSPF Segment Routing extension
    * Internet protocol
        * BGP 
### **Network service**
 - features belonging to the sevice plane
    * MPLS L3VPN
        * VPNv4
        * 6VPE
    * MPLS L2VPN
        * Point to point L2VPN
        * VPLS
        * EVPN
    * SRv6 (<- on-going effort)
        * L3VPN function
        * L2VPN function
### **Dataplane**
 - **FreerTr** is a versatile control plane that supports various dataplane such as:
    * UNIX raw socket: 
        * multiple **FreerTr** instance can run on the same host in order to simulate a complete lab 
    * regular network UNIX device: 
        * You can bind FreerTr interfaces to UNIX network devices. 
        * A typical use case is to run **FreerTr** as pure BGP route reflector control plane in a Service Provider backbone
        * An other use case is to run **FreerTr** as a pure BGP route reflector control plane in order to ensure pod to pod communication in a Kubernetes cluster
    * OpenFlow 
    * Supported **[P4](https://p4.org/)** dataplane
        * **[p4lang](https://p4.org/)**: [bmv2](https://github.com/p4lang/behavioral-model)
        * **[INTEL/BAREFOOT](https://www.barefootnetworks.com/)**: [TOFINO](https://www.barefootnetworks.com/products/brief-tofino/)
        * **[P4](https://p4.org/)** on FPGA: [CESNET liberouter project](https://www.liberouter.org/technologies/p4/)[<- on-going effort study] 


# **RARE/freeRtr** home

## **Overview**
**RARE** (**R**outer for **A**cademia, **R**esearch & **E**ducation) is an ongoing effort under the [GÉANT 4th programme](https://www.geant.org/Projects/GEANT_Project_GN4-3) which focus on creating an Open Source routing software platform.
The project aims to integrate different pieces of software related to building blocks inherent to a routing stack:

### **Control plane**:
* **RARE** uses **[FreeRtr](http://freerouter.nop.hu/)** under the hood used as the control plane component
### **Programmable dataplane**
* **[P4](https://p4.org/)** , **[DPDK](https://www.dpdk.org/)** or **[TCPDUMP/libpcap](https://tcpdump.org)** are possible candidates
### **Communication interface**
* This is the interface between the control plane and data plane and it is specific to the target dataplane. For example, [BMv2](https://github.com/p4lang/behavioral-model), the open source P4 virtual switch developed by [p4.org](https://p4,org), uses [P4Runtime](https://github.com/p4lang/p4runtime) in order to expose internal P4 program's object to an external control plane

**[P4](https://p4.org/)** and **[NPL](https://nplang.org/)** are such languages that allows data plane programmability.

!!! Note
    **[P4](https://p4.org/)** and **[NPL](https://nplang.org/)** languages attempt to be as much as possible independent from the target or Programmable Ethernet ASIC architecture.
    However architecture dependance is still prominent. Code adjustments followed by a target specific compilation is necessary if you want to run your dataplane program on a specific architecture.

## **How to use this site**
You'll find in this page various guides that will help you deploy and use **RARE/FreerTr** router.

<!-- There are 3 categories of documentation:

### **Installation guides**
This section encompasses documents that would guide one to deploy **RARE/freeRtr** in various situation in which different dataplane is used. Each **RARE/freeRtr** flavour would play a different role depending on user requirement.

* If you want to deploy a powerful BGP Route Reflector, no need to run RARE/freeRtr with a **P4** or **DPDK** dataplane. A pure **freeRtr** native software dataplane is more than enough
* At the opposite, if you desire a router that act as a pure Label Switch router (MPLS P router ) able to switch 6.4 Tbps, your best bet is to run **RARE/freeRtr** with a **INTEL/TOFINO P4** dataplane.
* **RARE/freeRtr** with **DPDK** dataplane is a perfect fit for a SOHO router switching nx1GE,nx10GE or a couple of 100GE  line rate range
-->

### **Getting started**
This section will introduce you to [freeRtr](freertr.net) open source control plane. It will guide you in learning how to install, configure and run freeRtr in a basic scenario.

<!--
### **Reference guides**
This section will guide you in configuring freeRtr control plane. In essence, it is similar to [freeRtr test cases](http://www.freertr.net/tests.html). While the [freeRtr test cases](http://www.freertr.net/tests.html) is convenient as it provides an extensive list of all the features in one page, this section will provide a navigation structure that helps you to find your way among the incredible freeRtr feature list. You'll find the sub-categories below (by order of importance):

* Routing configuration reference guide
* MPLS configuration reference guide
* QoS services configuration reference guide
-->

<!--
### **Validated design guides**
You'll find here specific design document that have been deployed and validated in real/production environment. These use cases are [numerous](http://www.freertr.net/usage.html).
The list below is obviously not exhaustive, but you'll be able to learn how to:

* build a BGP Route Reflector for a Internet service provider backbone
* a high performance MPLS LSR/P router
* a high performance MPLS LER/P router
* how to create a small but versatile CPE on SOHO environment
* create a geographically distributed internet service provider backbone
* create a geographically distributed internet exchange point
* ... and more ! (your creativity is the limit ... )
-->

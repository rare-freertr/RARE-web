# ** RARE/freeRtr installation**

This section lists RARE/freeRtr routing platform possible installations. There multiple ways to achieve that. You can install every components in the same hardware similar to traditional router design, or even opt for a totally disaggregated model where all components are in different hardware and or virtual environment.

These components are:

* freeRtr control plane software
* target dataplane software
* RARE interface software

While the control plane software and RARE interface can be deployed using a VM or container, the dataplane software installation will be vendor dependant. For example, if you implement RARE/freeRtr platform instance on INTEL/TOFINO P4 switch you'd have to follow INTEL's hardware installation guide and perform the dataplane software installation on a platform powered by P4 TOFINO ASIC.

In order to guarantee the best user experience, we strongly feel that the first encounter with a software is critical. Thus this section will expose **ONLY** simple procedure in order to provide:

* an effortless installation
* the best Open source router experience

!!! note
    Should you need mode information regarding a distributed installation approach, don't hesitate to engage with us via RARE/freeRtr mailing. Contact infornation can be found [here](/contacts/)


[This article](http://y.freertr.org/X7nTC) and [this article](http://y.freertr.org/XIBbF) can also help you understand how RARE/freeRtr can be deployed via a complete disaggregated model.

!!! info
    As a result, the following instllation guide will be restricted to popular platform. However, RARE/freeRtr by nature aims to be available on a [variety of platform](http://y.freertr.org/DoC6Dg) in a long term perspective. Therefore, expect additonal guides !

Happy networking !


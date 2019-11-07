# Getting started: ACME Service Provider ![under-construction](/img/under-construction-small.png)

Let's get ambitious and build step by step a Service Provider network for a fictious ACME company.

## **Topology diagram**
![acme](/img/acme-sp.png)
## **Overview**

* ACME service provider routers are organized as follow:
    * `C2`, `C3`, `C4`, `C5` are pure MPLS Label Switch Router (`LSR`)
    * `C1`, `C7`, `C8` are MPLS Label Edge Router (`LER`)
    * `C9` is ACME core network:
        *  BGP route reflector 
        *  TACACS server 

* Protocols used are:
    * OSPF
    * LDP 
    * BGP with IPv4, IPv6, 6VPE, VPLS, EVPN address-family

* Management for all routers are possible using:
    * telnet: passwordless telnet for the lab purpose
    * SSH authentication: authenticated by `C9` acting a ACME TACACS server 

* `R10`,`R11`, `R12` are ACME CPEs and are configured to access network services provided by ACME `LER` routers. 

* Last but not least, we will deploy RARE/FreerTr with [`bmv2`](https://github.com/p4lang/behavioral-model) P4 dataplane

## **TL;DR**

* Set up a [p4lang p4](http://p4.org) environment: 
    * using [RARE p4 ppa in Launchpad](https://launchpad.net/~frederic-loui)
    * using [Andy Fingerhut scripts](https://github.com/jafingerhut/p4-guide) from his p4 guide.
* Clone RARE repository from GitHub:
```
git clone https://github.com/frederic-loui/RARE.git 
```

!!! warning
    **RARE** packages on Launchpad are daily built. It happens that changes applied to **p4** software `master` branches can prevent the packages to be build properly.
    While waiting for the packages build to be fixed, it is therefore reccommended to use p4-guides scripts or the manual method of your choice to set up a **p4** environement.
    Also note that RARE is using `p4runtime` in order to ensure communication between **FreerTr** and the p4 switch, so you'll need to build `bmv2` and enable `simple_switch_grpc` target.

* Launch the whole topology
```
cd RARE/02-PE-labs/0000-topology-B/
make
```

* Enjoy ACME network lab
    * Undertake end to end `ping` test from R10,R11,R12
    * Check BGP route reflection and use FreerTr CLI to verify BGP NLRI and adress-family session establishment
    * Check LDP and MPLS forwarding
    * Check VPLS and EVPN at LER level 
    * Check VPNv4 and 6VPE at LER level 
        * `any to any` VPN with 1 RT
        *  and a `many to one` wth 2 RT) 
    * etc.


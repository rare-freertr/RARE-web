# **RARE NOS profile**

RARE/freeRtr NOS on Wedge 100BF-32X has a concept of `profile`. It corresponds to a pre-compiled RARE/freeRtr P4 program with specific settings at the dataplane level. Each `profile` actually is optimized for specific use case. `P profilei` that corresponds to a core `label switch router` will favor more entry for IPv4/IPv6 and MPLS table, while SRv6 will include more entry for IPv6 table for example.

!!! Info
    In order to keep the installation guide synthetic, RARE/freeRtr `profile` will be describe in subsequent section of the documentation. This page focus on how to switch from one `profile` to another using RARE/freeRtr CLI.


## Profile list

This list is dependant from the software release.

``` linenums="0"
#tna-list-profiles
Current profile: GEANT_TESTBED
Available profiles: BNG, BRAS, CERN_FLOWLAB, CGNAT, CLEANER, CPE, FW, GEANT_TESTBED, GGSN, GRE, IPIP, KIFU_LNS, NFV, NOP_MCHOME, P, PE, RAWIP, RENATER_PEERING_L2, RENATER_PEERING_L3, SRV6, TOR, WLC
```

## Profile switch

There is a mechanism that prevent you to install non-exiting `profile`.

``` linenums="0"
FREERTR#tna-set-profile FOO
Invalid profile FOO, must be one of "BNG, BRAS, CERN_FLOWLAB, CGNAT, CLEANER, CPE, FW, GEANT_TESTBED, GGSN, GRE, IPIP, KIFU_LNS, NFV, NOP_MCHOME, P, PE, RAWIP, RENATER_PEERING_L2, RENATER_PEERING_L3, SRV6, TOR, WLC"
```

Pick one `profile` from the list and set the current `profile` in use

``` linenums="0"
FREERTR#tna-set-profile CERN_FLOWLAB
Changing P4 profile from GEANT_TESTBED to CERN_FLOWLAB, restarting data-plane processes
```

Check profile in currently in use

``` linenums="0"
FREERTR#tna-list-profiles
Current profile: CERN_FLOWLAB
Available profiles: BNG, BRAS, CERN_FLOWLAB, CGNAT, CLEANER, CPE, FW, GEANT_TESTBED, GGSN, GRE, IPIP, KIFU_LNS, NFV, NOP_MCHOME, P, PE, RAWIP, RENATER_PEERING_L2, RENATER_PEERING_L3, SRV6, TOR, WLC
```

!!! Warning
    If you want to make the `profile` switch persistent you would need to write the configuration beforehand.

    This will give you a safety mechanism if you need to fallback or switch to another `profile`.

    If you don't `write` the configuration, the switch will revert to the old `profile` used.


``` linenums="0"
FREERTR#reload warm
Connection closed by foreign host.
rare@par0001:~$
telnet 127.0.0.1 2323
 Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
welcome
line ready
FREERTR#tna-list-profiles
Current profile: GEANT_TESTBED
Available profiles: BNG, BRAS, CERN_FLOWLAB, CGNAT, CLEANER, CPE, FW, GEANT_TESTBED, GGSN, GRE, IPIP, KIFU_LNS, NFV, NOP_MCHOME, P, PE, RAWIP, RENATER_PEERING_L2, RENATER_PEERING_L3, SRV6, TOR, WLC
```

## Write the configuration

``` linenums="0"
FREERTR#wr
```

After a reboot:

``` linenums="0"
#tna-list-profiles
Current profile: CERN_FLOWLAB
Available profiles: BNG, BRAS, CERN_FLOWLAB, CGNAT, CLEANER, CPE, FW, GEANT_TESTBED, GGSN, GRE, IPIP, KIFU_LNS, NFV, NOP_MCHOME, P, PE, RAWIP, RENATER_PEERING_L2, RENATER_PEERING_L3, SRV6, TOR, WLC
```

The profile now currently in use is persitent even after a reboot.


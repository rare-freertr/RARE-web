# **Interface configuration on Wedge 100BF-32**

This section describes how to configure interface via RARE/freeRtr OS. Interfaces can be seen from 3 perspectives:

* Front panel
* INTEL/TOFINO ASIC
* freeRtr

# Front panel
On Wedge100bf32, all ports are accessible via the switch front panel. Actually, all QSFP28 ports are labelled and are visually identified by an index that belongs to [1..32] range. All ports are able to run at 10/25/40/100GE speeds. Each QSFP28 port has also 4 lanes. It is also possible for each port to provide 4x10GE, 4x25GE, and maybe 2x40GE interfaces using a breakout cable.

Therefore each port/lane will have the following identifier: **`$FRONT_PANEL_PORT/$LANE`**

For example, if you have a 4x25GE breakout cable inserted in `FRONT PANEL PORT 1`, the interfaces will be identified as follow:

`FRONT PANEL 15/0, 15/1,15/2, 15/3`.

# INTEL/TOFINO ASIC
Internally, INTEL/TOFINO ASIC allocates to each interface (i.e `$PORT/$LANE` pair) a specific identifier. The output from `bf_shell` utility below shows an example of interface mapping.

``` linenums="0"
-----+----+---+----+-------+----+--+--+---+---+---+--------+----------------+----------------+-
PORT |MAC |D_P|P/PT|SPEED  |FEC |AN|KR|RDY|ADM|OPR|LPBK    |FRAMES RX       |FRAMES TX       |E
-----+----+---+----+-------+----+--+--+---+---+---+--------+----------------+----------------+-
1/0  |23/0|132|3/ 4|10G    |NONE|Au|Au|YES|ENB|UP |  NONE  |           55055|           55154|
1/1  |23/1|133|3/ 5|-------|----|--|--|YES|---|---|--------|----------------|----------------|-
1/2  |23/2|134|3/ 6|-------|----|--|--|YES|---|---|--------|----------------|----------------|-
1/3  |23/3|135|3/ 7|-------|----|--|--|YES|---|---|--------|----------------|----------------|-
```

!!! Note
    The output above is just for information. Practically you would never have to run `bf_shell` in order to retrieve this mapping between front panel interface and TOFINO identifier

# freeRtr
freeRtr identifies dataplane port as `sdn<index>` interface. `<index>` is an integer.
!!! Note
    As a rule of thumb, when no breakout cable is used, `<index>` is the `front panel` port identifier: `<fp_port_id>`. If a breakout cable is used `<index>` can be the concatenation of [`<fp_port_id>` & `00` & `<lane_id>`]

For example, if a module is inserted into front panel port `1`, then freeRtr interface name is interface `sdn1`. If a 4x25GE breakout cable is plugged into port `1`, then interface name should be: interface `sdn1001`, `sdn1002`,`sdn1003`, `sdn1004`


# Interface configuration
In freeRtr philosophy, each interface belongs to either a `vrf` or a `bridge`. It is therefore mandatory:

* to configure a `vrf` or a `bridge`
``` linenums="0"
vrf definition <MY_VRF>
 exit
```
``` linenums="0"
bridge <BRIDGE_ID>
 mac-learn
 exit
```
* and bind each of them to an interface.
``` linenums="0"
conf t
interface sdn1
 vrf forwarding  <MY_VRF_ID>
 exit
end
```
``` linenums="0"
conf t
interface sdn2
 bridge-group <MY_BRIDGE_ID>
 exit
end
```

* Declare `vrf` or `bridge` and interfaces at the dataplane level
``` linenums="0"
server p4lang <SERVER_P4_ID>
 export-vrf <MY_VRF_ID> 1
 export-bridge <MY_BRIDGE_ID> 1
 export-port sdn1 132 100 0 0 0
 export-port sdn2 140 100 0 0 0
 exit
end
```

# Explanation
The above example describe the configuration of front panel port `1` and `2`.

* Front panel port `1` (sdn`1`) is bound to `vrf` `<MY_VRF_ID>`
* Front panel port `2` (sdn`2`) is bound to `bridge` `<MY_VRF_ID>`

The interesting part is `server p4lang p4` configuration stanza

* export-vrf `<MY_VRF_ID>` `<DATAPLANE_VRF_ID>`
    * `<MY_VRF_ID>` let's assign a value: `my_vrf`
    * `<DATAPLANE_VRF_ID>` let's assign a value: `1`

* export-bridge `<MY_BRIDGE_ID>` `DATAPLANE_BRIDGE_ID`
    * `<MY_BRIDGE_ID>` let's assign a value: `1`
    * `<DATAPLANE_BRIDGE_ID>` let's assign a value: `1`

* export-port `<FREERTR_INTF>` `<TOFINO_PORT_ID>` `<PORT_SPEED>` `<FEC>` `AUTONEG` `<FLOWCTRL>`
    * `<FREERTR_INTF>`: freeRtr `sdn` interface identifier
    * `<TOFINO_PORT_ID>`: INTEL/TOFINO ASIC port identifier
    * `<PORT_SPEED>`: Port speed `10`/`25`/`40`/`100` GE
    * `<FEC>`: Forwarding Error Correction in use [`0`=UNDEFINED, `1`=NONE, `2`=FC, `3`=RS]
    * `<AUTONEG>`: Autonegotiation [`0`=UNDEFINED, `1`=OFF, `2`=ON]
    * `<FLOWCTRL>`: Flow control type [`0`=UNDEFINED, `1`=NONE, `2`=PAUSE, `3`=PFC]

!!! Note
    In the above example `<TOFINO_PORT_ID>` for front panel port 1 has value `132`.

    How do we get this value without `bf_shell` ?

    * 2 possibilities:

    `-1-` `show p4lang <SERVER_P4_ID>`
    ``` linenums="0"
    FREERTR# show p4lang p4
    ...
    front  name
    ...
    132    frontpanel-1/0
    133    frontpanel-1/1
    134    frontpanel-1/2
    135    frontpanel-1/3
    ...
    140    frontpanel-2/0
    141    frontpanel-2/1
    142    frontpanel-2/2
    143    frontpanel-2/3
    ...
    ```
    `-2-` Use freeRtr configuration auto-completion
    ``` linenums="0"
    conf t
    FREERTR(cfg)#server p4lang p4
    FREERTR(cfg-server)#export-port sdn4 ?
      <num>           - port number
      dynamic         - dynamic port number
      frontpanel-1/0  - port number
      frontpanel-1/1  - port number
      frontpanel-1/2  - port number
      frontpanel-1/3  - port number
    ...
    ```
    If `-2-` is used then `frontpanel-1/0` will be translated to its corresponding TOFINO identifier (i.e `132`).

The final configuration is:

``` linenums="0"
conf t
!
vrf definition my_vrf
 exit
!
bridge 1
 mac-learn
 exit
!
interface sdn1
 vrf forwarding my_vrf
 exit
!
interface sdn2
 bridge-group 1
 exit
!
server p4lang p4
 export-vrf my_vrf 1
 export-bridge 1 1
 export-port sdn1 132 100 0 0 0
 export-port sdn2 140 100 0 0 0
 exit
!
end
```

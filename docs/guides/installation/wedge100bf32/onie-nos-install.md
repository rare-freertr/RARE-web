# **Installation on Wedge 100BF-32(X or QS)**

There are 3 major steps:

* Prerequisites
* Boot into ONIE environment
* RARE/freeRtr NOS image installation via ONIE

!!! info
    Assuming you are familiar with ONIE, the installation process should last 5 minutes

# Prerequisites
* Wedge 100BF-32 hardware with **ONIE partition pre-installed**
    * Wedge 100BF-32X
    * Wedge 100BF-32QS

!!! info
    Wedge 100BF-32X and Wedge 100BF-32QS are very similar platforms. They both have 32 QSFP28 ports able to run at 10/25/40/100GE line rate. The first is equipped with the Intel Tofino T32D ASIC model with two pipelines (or cores if it helps to picture the difference). The latter is powered by the Intel Tofino T32Q ASIC which has 4 pipelines. Each pipeline is able to handle 16 interface ports. The Wedge 100BF-32QS has 2 additional pipes that are not tied to specific front panel ports. They can be leveraged to provide additional stages for packet processing.

* DHCP server that serves IP addresses to
    * the [BMC](https://en.wikipedia.org/wiki/Baseboard_Management_Controller)
    * and the Main Board CPU (or MBC): Where the Network Operating System will be effectively installed

!!! note
    If you can access the BMC through the Wedge 100BF-32 serial console, the DHCP server and Internet connectivity are optional. However, the installation process requires at least IP connectivity and that you can get SSH access to Main Board CPU. Connectivity to MBC will have to be enabled from BMC.

* Wedge 100BF-32 BMC access either
    * via serial console port
    * or via BMC SSH

!!! note
    Please refer to [EdgeCore](https://www.edge-core.com/) documentation regarding BMC and MBC access procedure.

# Boot into ONIE environment

* Access to BMC via Serial or SSH
```
ssh root@<bmc_ip>
root@<bmc_ip>'s password:
Last login: Sun Mar  8 07:18:41 2020 from 172.16.11.11
root@bmc:~#
```
(use your favorite search engine in order to retrieve BMC default password)
* Power cycle MBC
```
wedge_power.sh reset
```

* Access to MBC from BMC
```
root@bmc:~# sol.sh
You are in SOL session.
Use ctrl-x to quit.
-----------------------

...
<BMC boot messages>
...
<wait for Grub menu to appear>
...
```

* Choose **`ONIE rescue mode`** from Grub menu

# RARE/freeRtr NOS image installation via ONIE
Now that you have rebooted MBC into **`ONIE rescue mode`**, there are 2 possible ways to install RARE/freeRtrt NOS

* Internet access is available from MBC
    * Launch RARE/freeRtr ONIE net-install
```
root@bmc:~# onie-nos-install http://hydra.nix.net.switch.ch/RARE/releases/1/onie-installer.bin
```

* WEDGE MBC air gapped installation
    * From a computer that has Internet connectivity
```
wget http://hydra.nix.net.switch.ch/RARE/releases/1/onie-installer.bin
```
    * Copy RARE/freeRtr ONIE installer to MBC
```
scp ./onie-installer.bin root@<mbc_ip>:~/
```
    * Log into the P4 switch either using BMC serial or SSH
```
ssh root@<mbc_ip>
```
    * Launch  RARE/freeRtr ONIE install from local file system
```
onie# onie-nos-install /root/onie-installer.bin
```
You should observe RARE/freeRtr installation work in progress. Once finished, the Wedge 100BF-32 will reboot.

And, «voilà !»

Congratulations, you have just installed RARE/freeRtr on your Wedge 100BF-32!

Happy networking!

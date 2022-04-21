# **Installation on Wedge100bf32(x or qs)**

There are 3 major steps:

* Prerequisites
* Boot into ONIE environment
* RARE/freeRtr NOS image installation via ONIE

!!! info
    Assuming you are familiar with ONIE, the installation process should last 5 minutes

# Prerequisites
* Wedge100bf32 hardware with **ONIE partition pre-installed**
    * Wedge100bf32x
    * Wedge100bf32qs

!!! info
    Wedge100bf32x and Wedge100bf32qs are almost similar platform. They both have 32 QSFP28 ports able to run at 10/25/40/100GE line rate. The first equipped with INTEL/TOFINO ASIC T32D model with two pipes or core if it helps to picture the difference. The latter is powered by INTEL/TOFINO ASIC T32Q which has 4 pipes. Each pipe is able to handle 16 interface ports. Wedge100bf32qs has 2 additional pipes that are not tied to specific front panel port. They can be leveraged to provide additional stages for packet processing.

* DHCP server
    * that serves IP addresses to [BMC](https://en.wikipedia.org/wiki/Baseboard_Management_Controller)
    * and Main Board CPU (or MBC): Where the Network Operating System will be effectively installed

!!! note
    If you have access to BMC through the Wedge100bf32 serial console, the DHCP server and Internet connectivity is optional. However, the installation process requires at least an IP connectivity and that you can get SSH access to Main Board CPU. Connectivity to MBC will have to be enabled from BMC.

* Wedge100bf32 BMC access either
    * via Serial console port
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
You should observe RARE/freeRtr installation work in progress. Once finished, the Wedge100bf32 will reboots.

And, "voilà !"

Congratulation you have just installed RARE/freeRtr on Wedge100bf32 !

Happy networking !

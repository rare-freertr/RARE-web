# Example: interop9: isis lsp md5 authentication

## **Topology diagram**

![topology](/img/intop9-isis12.tst.png)

## **Configuration**

**r1:**
```
hostname r1
logging file debug ../binTmp/zzz1r1-log.run
vrf definition tester
 exit
server telnet tester
 security protocol telnet
 vrf tester
 exit
vrf def v1
 rd 1:1
 exit
router isis4 1
 vrf v1
 net 48.4444.0000.1111.00
 both lsp-pass tester
 both authen-type md5
 red conn
 exit
router isis6 1
 vrf v1
 net 48.6666.0000.1111.00
 both lsp-pass tester
 both authen-type md5
 red conn
 exit
int eth1
 vrf for v1
 ipv4 addr 1.1.1.1 255.255.255.0
 router isis4 1 ena
 router isis4 1 password tester
 router isis4 1 authen-type md5
 exit
int eth2
 vrf for v1
 ipv6 addr fe80::1 ffff::
 router isis6 1 ena
 router isis6 1 password tester
 router isis6 1 authen-type md5
 exit
int lo0
 vrf for v1
 ipv4 addr 2.2.2.1 255.255.255.255
 ipv6 addr 4321::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 exit
```

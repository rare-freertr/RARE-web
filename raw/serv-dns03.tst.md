# Example: relaying dns server

## **Topology diagram**

![topology](/img/serv-dns03.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz-log-r1.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source ethernet1
 exit
!
!
!
!
!
!
!
!
!
!
!
!
!
!
server dns dns
 zone test.corp defttl 43200
 zone test.corp rr www.test.corp ip4a 1.1.1.1
 vrf v1
 exit
!
client proxy p1
client name-server 1234::2
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz-log-r2.run
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 no description
 vrf forwarding v1
 ipv4 address 1.1.1.2 255.255.255.0
 ipv6 address 1234::2 ffff::
 no shutdown
 no log-link-change
 exit
!
proxy-profile p1
 vrf v1
 source ethernet1
 exit
!
!
!
!
!
!
!
!
!
!
!
!
!
!
server dns dns
 resolver test.corp 1234::1
 vrf v1
 exit
!
client proxy p1
client name-server 1.1.1.1
!
end
```

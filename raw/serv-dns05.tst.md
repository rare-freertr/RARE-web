# Example: secondary dns server

## **Topology diagram**

![topology](/img/serv-dns05.tst.png)

## **Configuration**

**r1:**
```
hostname r1
buggy
!
logging file debug ../binTmp/zzz8r1-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
 vrf forwarding v1
 ipv4 address 1.1.1.1 255.255.255.0
 ipv6 address 1234::1 ffff::
 no shutdown
 no log-link-change
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
server dns dns
 zone test.corp defttl 43200
 zone test.corp axfr enable
 zone test.corp rr ip4a.test.corp ip4a 1.1.1.1
 zone test.corp rr ip4i.test.corp ip4i ethernet1
 zone test.corp rr test.corp soa ns.test.corp admin.test.corp 20100101 600 600 600000 30
 zone test.corp rr ip6a.test.corp ip6a 1234::1
 zone test.corp rr ip6i.test.corp ip6i ethernet1
 vrf v1
 exit
!
!
end
```

**r2:**
```
hostname r2
buggy
!
logging file debug ../binTmp/zzz8r2-log.run
!
vrf definition tester
 exit
!
vrf definition v1
 rd 1:1
 exit
!
interface ethernet1
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
server telnet tester
 security protocol telnet
 no exec authorization
 no login authentication
 vrf tester
 exit
!
server dns dns
 zone test.corp defttl 43200
 zone test.corp axfr enable
 vrf v1
 exit
!
client proxy p1
client name-server 1.1.1.2
!
end
```

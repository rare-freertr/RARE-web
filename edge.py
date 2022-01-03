#!/usr/bin/python3

from connector import *
import ipaddress,re
from pprint import pprint

class Edge:
    id = None
    tailEnd = None
    headEnd = None
    tailLabel = None
    headLabel = None
    tailTooltip = None
    headTooltip = None

    def __init__(self, id = None,
                       tailEnd = None, headEnd = None,
                       tailLabel = None, headLabel = None,
                       tailTooltip = None, headTooltip = {}):
       self.id = id
       self.tailEnd = tailEnd
       self.headEnd = headEnd
       self.tailLabel = tailLabel
       self.headLabel = headLabel
       self.tailTooltip = tailTooltip
       self.headTooltip = headTooltip

    def toString(self):
        return ('%s@%s -- %s@%s' ) % (self.tailEnd.node, self.tailEnd.intf,
                                      self.headEnd.node, self.headEnd.intf )
    def netMask2CIDR(self,netmask):
        bitCount = [0, 0x8000, 0xc000, 0xe000, 0xf000, 0xf800, 0xfc00, 0xfe00, 0xff00, 0xff80, 0xffc0, 0xffe0, 0xfff0, 0xfff8, 0xfffc, 0xfffe, 0xffff]

        count = 0
        try:
            for w in netmask.split(':'):
                if not w or int(w, 16) == 0: break
                count += bitCount.index(int(w, 16))
        except:
            raise SyntaxError('Bad NetMask')

        return count

    def get_host4(self, ipv4_address):
        host = re.findall(r'^.*?\..*?\..*?\.(.*)$', ipv4_address)
        if len(host) > 0:
            return host[0]
        else:
            return None

    def get_host6(self, ipv6_address):
        if len(ipv6_address.split(':')) > 0:
            return ipv6_address.split(':')[-1]
        else:
            return None

    def toDot(self):
        """
        'R1 -- R2 [
        taillabel="eth0[1]" headlabel="eth0[2]"
        label="1.1.12.0/24\r1234:12::/64"
        tailtooltip=".1\r::1/64" headtooltip=".2\r::2/64" ]`
        """
        ipv4_pfx = None
        ipv6_pfx = None

        if self.tailEnd.type == ConnType.ROUTED:
            edge_label ='INIT'
            if (self.tailEnd.ipv4 is not None):
                #if (self.tailEnd.ipv4 != 'dynamic'):
                ipv4_pfx = self.tailEnd.ipv4
                hostmask4 = self.tailEnd.hostmask4

            if (self.tailEnd.ipv6 is not None):
                ipv6_pfx = self.tailEnd.ipv6
                hostmask6 = self.tailEnd.hostmask6
                if (self.tailEnd.ipv6 != 'dynamic'):
                    #print('PREFIX_LEN: %s' % self.netMask2CIDR(hostmask6))
                    hostmask6 = self.netMask2CIDR(hostmask6)

            edge = '%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() )

            self.tailLabel = 'taillabel="%s"' % ( self.tailEnd.intf )

            if self.headEnd.type == ConnType.ROUTED:
                self.headLabel = 'headlabel="%s"' % ( self.headEnd.intf )

            #pprint('DEBUG edge: %s' % self.toString())
            #print('DEBUG ipv4_pfx: %s' % ipv4_pfx)
            #print('DEBUG hostmask4: %s' % hostmask4)
            if (ipv4_pfx is not None) and (ipv6_pfx is not None):
                #print("DEBUG IN EDGE: ipv4_pfx=%s,hostmask4=%s" % (ipv4_pfx,hostmask4))
                #print("DEBUG IN EDGE: ipv6_pfx=%s,hostmask6=%s" % (ipv6_pfx,hostmask6) )
                if  (self.tailEnd.ipv4 != 'dynamic') and (self.tailEnd.ipv6 != 'dynamic'):
                    ipaddr_ipv4 = ipaddress.ip_network('%s/%s' % (ipv4_pfx,hostmask4), strict=False )
                    ipaddr_ipv6 = ipaddress.ip_network('%s/%s' % (ipv6_pfx,hostmask6),strict=False )
                    edge_label = 'label="%s/%s\\n%s/%s"'  % ( ipaddr_ipv4.network_address,
                                                          ipaddr_ipv4.prefixlen,
                                                          ipaddr_ipv6.network_address,
                                                          ipaddr_ipv6.prefixlen )
                    self.tailLabel = 'taillabel="%s[%s]"' % ( self.tailEnd.intf, self.get_host4(ipv4_pfx) )
                else:
                    edge_label = 'label="%s/%s\\n%s/%s"'  % ( 'dynamic',
                                                              'dynamic',
                                                              'dynamic',
                                                              'dynamic' )

                    self.tailLabel = 'taillabel="%s"' % ( self.tailEnd.intf )
                #print('DEGUBG ipaddr_ipv4: %s' %  ipaddr_ipv4)
                #print('DEGUBG ipaddr_ipv6: %s' %  ipaddr_ipv6)
                #print('DEGUBG self.headEnd.node: %s@%s' %  (self.headEnd.node, self.headEnd.intf))
                #print('DEGUBG self.headEnd.ipv4: %s' %  self.headEnd.ipv4)
                #print('DEGUBG self.headEnd.ipv6: %s' %  self.headEnd.ipv6)

                if self.headEnd.type == ConnType.ROUTED:
                    if  (self.headEnd.ipv4 != 'dynamic') and (self.headEnd.ipv6 != 'dynamic'):
                        self.headLabel = 'headlabel="%s[%s]"' % ( self.headEnd.intf, self.get_host4(self.headEnd.ipv4) )
                    else:
                        self.headLabel = 'headlabel="%s"' % ( self.headEnd.intf )
                    self.headTooltip = 'headtooltip="%s\\n%s"' % ( self.headEnd.ipv4, self.headEnd.ipv6 )
                elif self.headEnd.type == ConnType.BRIDGED:
                    self.headLabel = 'headlabel="%s"' % ( self.headEnd.intf )
                    self.headTooltip = 'headtooltip="bridge %s"' % ( self.headEnd.bridge_id )

                self.tailTooltip = 'tailtooltip="%s\\n%s"' % ( self.tailEnd.ipv4, self.tailEnd.ipv6 )
            elif (ipv4_pfx is not None):
                if (self.tailEnd.ipv4 != 'dynamic'):
                    ipaddr_ipv4 = ipaddress.ip_network('%s/%s' % (ipv4_pfx,hostmask4), strict=False )
                    edge_label = 'label="%s/%s"'  % ( ipaddr_ipv4.network_address,
                                                  ipaddr_ipv4.prefixlen )
                    self.tailLabel = 'taillabel="%s[%s]"' % ( self.tailEnd.intf, self.get_host4(ipv4_pfx) )
                    edge_label = 'label="%s/%s"'  % ( 'dynamic',
                                                      'dynamic' )

                #print('DEBUG: %s' % self.headEnd.ipv4)
                if self.headEnd.type == ConnType.ROUTED:
                    self.headLabel = 'headlabel="%s[%s]"' % ( self.headEnd.intf, self.get_host4(self.headEnd.ipv4) )
                    self.headTooltip = 'headtooltip="%s"' % ( self.headEnd.ipv4 )
                self.tailTooltip = 'tailtooltip="%s"' % ( self.tailEnd.ipv4 )
            elif (ipv6_pfx is not None):
                ipaddr_ipv6 = ipaddress.ip_network('%s/%s' % (ipv6_pfx,hostmask6),strict=False )
                edge_label = 'label="%s/%s"'  % ( ipaddr_ipv6.network_address,
                                                  ipaddr_ipv6.prefixlen )
                self.tailLabel = 'taillabel="%s[%s]"' % ( self.tailEnd.intf, self.get_host6(ipv6_pfx) )
                if self.headEnd.type == ConnType.ROUTED:
                    self.headLabel = 'headlabel="%s[%s]"' % ( self.headEnd.intf, self.get_host6(self.headEnd.ipv6) )
                    self.headTooltip = 'headtooltip="%s"' % ( self.headEnd.ipv6 )
                self.tailTooltip = 'tailtooltip="%s"' % ( self.tailEnd.ipv6 )


        elif self.tailEnd.type == ConnType.BRIDGED:
            edge = '%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() )
            edge_label = ''
            #edge_label = 'label="%s/%s\\n%s/%s"'  % ( ipaddr_bvi4.network_address,
            #                                          ipaddr_bvi4.prefixlen,
            #                                          ipaddr_bvi6.network_address,
            #                                          ipaddr_bvi6.prefixlen )
            self.tailLabel = 'taillabel="%s"' % ( self.tailEnd.intf )
            self.headLabel = 'headlabel="%s"' % ( self.headEnd.intf )
            self.tailTooltip = 'tailtooltip="bridge %s"' % ( self.tailEnd.bridge_id )
            self.headTooltip = 'headtooltip="bridge %s"' % ( self.headEnd.bridge_id )
        else:
            edge = '%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() )
            edge_label = ''
            self.tailLabel = 'taillabel="%s"' % ( self.tailEnd.intf )
            self.headLabel = 'headlabel="%s"' % ( self.headEnd.intf )
            self.tailTooltip = 'tailtooltip="%s"' % ( self.tailEnd.intf )
            self.headTooltip = 'headtooltip="%s"' % ( self.headEnd.intf )

        #print('EDGE: %s' % edge)
        #print('EDGE_LABEL: %s' % edge_label)
        #print('TAIL_LABEL: %s' % self.tailLabel)
        #print('HEAD_LABEL: %s' % self.headLabel)
        #print('TAIL_TOOLTIP: %s' % self.tailTooltip)
        #print('HEAD_TOOLTIP: %s' % self.headTooltip)
        out = '%s [ %s %s %s %s %s ]' % (edge, edge_label,
                                         self.tailLabel,
                                         self.headLabel,
                                         self.tailTooltip,
                                         self.headTooltip )
        return out

    def toNext(self):
        """
        'R1 -- R2 [
        taillabel="eth0[1]" headlabel="eth0[2]"
        label="1.1.12.0/24\r1234:12::/64"
        tailtooltip=".1\r::1/64" headtooltip=".2\r::2/64" ]`
        """
        ipv4_pfx = None
        ipv6_pfx = None

        if self.tailEnd.type == ConnType.ROUTED:
            edge_label = {}
            if (self.tailEnd.ipv4 is not None):
                #if (self.tailEnd.ipv4 != 'dynamic'):
                ipv4_pfx = self.tailEnd.ipv4
                hostmask4 = self.tailEnd.hostmask4

            if (self.tailEnd.ipv6 is not None):
                ipv6_pfx = self.tailEnd.ipv6
                hostmask6 = self.tailEnd.hostmask6
                if (self.tailEnd.ipv6 != 'dynamic'):
                    #print('PREFIX_LEN: %s' % self.netMask2CIDR(hostmask6))
                    hostmask6 = self.netMask2CIDR(hostmask6)

            edge = { 'id': '%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() ) }

            self.tailLabel = {'taillabel': self.tailEnd.intf}

            if self.headEnd.type == ConnType.ROUTED:
                self.headLabel = {'headlabel': self.headEnd.intf}
            else:
                self.headLabel = {'headlabel': self.headEnd.intf}

            if (ipv4_pfx is not None) and (ipv6_pfx is not None):
                if  (self.tailEnd.ipv4 != 'dynamic') and (self.tailEnd.ipv6 != 'dynamic'):
                    ipaddr_ipv4 = ipaddress.ip_network('%s/%s' % (ipv4_pfx,hostmask4), strict=False )
                    ipaddr_ipv6 = ipaddress.ip_network('%s/%s' % (ipv6_pfx,hostmask6),strict=False )
                    edge_label = {'midlabel': '%s/%s - %s/%s' % ( ipaddr_ipv4.network_address,
                                                                  ipaddr_ipv4.prefixlen,
                                                                  ipaddr_ipv6.network_address,
                                                                  ipaddr_ipv6.prefixlen )}

                    self.tailLabel = {'taillabel': '%s[%s]' % ( self.tailEnd.intf, self.get_host4(ipv4_pfx) ) }
                else:
                    edge_label = {'midlabel': '%s/%s - %s/%s' % ( 'dynamic',
                                                                  'dynamic',
                                                                  'dynamic',
                                                                  'dynamic' )}
                    self.tailLabel = {'taillabel': '%s' % ( self.tailEnd.intf )}

                if self.headEnd.type == ConnType.ROUTED:
                    if  (self.headEnd.ipv4 != 'dynamic') and (self.headEnd.ipv6 != 'dynamic'):
                        self.headLabel = {'headlabel': '%s[%s]' % ( self.headEnd.intf, self.get_host4(self.headEnd.ipv4) ) }
                    else:
                        self.headLabel = {'headlabel': '%s' % ( self.headEnd.intf ) }
                    self.headTooltip = {'headtooltip': '%s - %s' % ( self.headEnd.ipv4, self.headEnd.ipv6 ) }
                elif self.headEnd.type == ConnType.BRIDGED:
                    self.headLabel = {'headlabel': '%s' % ( self.headEnd.intf ) }
                    self.headTooltip = { 'headtooltip': 'bridge %s' % ( self.headEnd.bridge_id ) }
                else:
                    self.headLabel = {'headlabel': '%s' % ( self.headEnd.intf ) }
                    self.headTooltip = { 'headtooltip': '' }

                self.tailTooltip = {'tailtooltip': '%s - %s' % ( self.tailEnd.ipv4, self.tailEnd.ipv6 ) }
            elif (ipv4_pfx is not None):
                if (self.tailEnd.ipv4 != 'dynamic'):
                    ipaddr_ipv4 = ipaddress.ip_network('%s/%s' % (ipv4_pfx,hostmask4), strict=False )
                    edge_label = {'midlabel': '%s/%s'  % ( ipaddr_ipv4.network_address,
                                                  ipaddr_ipv4.prefixlen )}
                    self.tailLabel = {'taillabel': '%s[%s]' % ( self.tailEnd.intf, self.get_host4(ipv4_pfx) ) }
                    edge_label = {'midlabel': '%s/%s'  % ( 'dynamic',
                                                      'dynamic' ) }

                if self.headEnd.type == ConnType.ROUTED:
                    self.headLabel = {'headlabel': '%s[%s]' % ( self.headEnd.intf, self.get_host4(self.headEnd.ipv4) ) }
                    self.headTooltip = {'headtooltip': '%s' % ( self.headEnd.ipv4 ) }

                self.tailTooltip = {'tailtooltip': '%s' % ( self.tailEnd.ipv4 ) }
            elif (ipv6_pfx is not None):
                ipaddr_ipv6 = ipaddress.ip_network('%s/%s' % (ipv6_pfx,hostmask6),strict=False )
                edge_label = { 'midlabel': '%s/%s'  % ( ipaddr_ipv6.network_address,
                                                  ipaddr_ipv6.prefixlen ) }
                self.tailLabel = { 'taillabel': '%s[%s]' % ( self.tailEnd.intf, self.get_host6(ipv6_pfx) ) }
                if self.headEnd.type == ConnType.ROUTED:
                    self.headLabel = {'headlabel': '%s[%s]' % ( self.headEnd.intf, self.get_host6(self.headEnd.ipv6) ) }
                    self.headTooltip = {'headtooltip': '%s' % ( self.headEnd.ipv6 ) }
                self.tailTooltip = {'tailtooltip': '%s' % ( self.tailEnd.ipv6 ) }


        elif self.tailEnd.type == ConnType.BRIDGED:
            edge = { 'id':'%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() ) }
            edge_label = {'midlabel': ''}
            self.tailLabel = {'taillabel': '%s' % ( self.tailEnd.intf )}
            self.headLabel = {'headlabel': '%s' % ( self.headEnd.intf )}
            self.tailTooltip = {'tailtooltip': 'bridge %s' % ( self.tailEnd.bridge_id )}
            self.headTooltip = {'headtooltip': 'bridge %s' % ( self.headEnd.bridge_id )}
        else:
            edge = { 'id': '%s -- %s' % ( self.tailEnd.node.upper(), self.headEnd.node.upper() ) }
            edge_label = {'midlabel': ''}
            self.tailLabel = {'taillabel': '%s' % ( self.tailEnd.intf ) }
            self.headLabel = {'headlabel': '%s' % ( self.headEnd.intf ) }
            self.tailTooltip = {'tailtooltip': '%s' % ( self.tailEnd.intf ) }
            self.headTooltip = {'headtooltip': '%s' % ( self.headEnd.intf ) }

        #print('EDGE: %s' % edge)
        #print('EDGE_LABEL: %s' % edge_label)
        #print('TAIL_LABEL: %s' % self.tailLabel)
        #print('HEAD_LABEL: %s' % self.headLabel)
        #print('TAIL_TOOLTIP: %s' % self.tailTooltip)
        #print('HEAD_TOOLTIP: %s' % self.headTooltip)
        #print('CONNTYPE: %s' % self.tailEnd.type)

        if self.tailTooltip is None:
            self.tailTooltip = {'tailtooltip':''}
        if self.headTooltip is None:
            self.headTooltip = {'headtooltip':''}
        if self.tailLabel is None:
            self.tailLabel = {'taillabel':''}
        if self.headLabel is None:
            self.headLabel = {'headlabel':''}
        out = edge | {'source':self.tailEnd.node.upper()} | {'target':self.headEnd.node.upper()} | edge_label | self.tailLabel | self.headLabel | self.tailTooltip | self.headTooltip
        return out


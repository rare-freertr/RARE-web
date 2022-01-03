#!/usr/bin/python3

from connector import *
from edge import *
from ipaddress import *
from ciscoconfparse import CiscoConfParse
import glob,re
from pprint import pprint
import os
import json

CONNS={}
EDGES={}
CONFIGS={}

topology_data = { 'nodes':[], 'links':[] }

NEXT_TEMPLATE="""
"""
def netMask2CIDR(netmask):
    bitCount = [0, 0x8000, 0xc000, 0xe000, 0xf000, 0xf800, 0xfc00, 0xfe00, 0xff00, 0xff80, 0xffc0, 0xffe0, 0xfff0, 0xfff8, 0xfffc, 0xfffe, 0xffff]

    count = 0
    try:
        for w in netmask.split(':'):
            if not w or int(w, 16) == 0: break
            count += bitCount.index(int(w, 16))
    except:
        raise SyntaxError('Bad NetMask')

    return count

def get_tst_list(tst_dir_path):
    tst_files = glob.glob("%s/*.tst" % tst_dir_path)
    tst_files.sort()
    return (sorted(tst_files))

def get_rtr_config(test_path):
    parse = CiscoConfParse(test_path, syntax='ios')
    routers = []
    rtr_intf_list = []
    nodes = []
    font_size = 8
    for intf_obj in parse.find_objects(r'^hostname'):
        routers.append("%s" % intf_obj.re_match_typed(r'^hostname\s+(\S+)', default=''))
    for rtr in routers:
        config = CiscoConfParse( parse.find_all_children('^hostname %s$' % rtr) )
        CONFIGS[rtr]=config
        rtr_intf_list = get_rtr_intf(CONFIGS[rtr])
        #print('INTF LIST: %s@%s' %  (rtr,rtr_intf_list) )
        if not rtr_intf_list:
            #print('DEBUG: %s HAS NO INTERFACE' % rtr)
            nodes.append('%s [ label="%s" ]' % ( rtr.upper(), rtr.upper() ) )
        else:
            xlabel = 'xlabel=< <font point-size="%s"> %s </font> >' % (font_size, " <br/> ".join(rtr_intf_list))
            nodes.append('%s [ label="%s" %s]' % ( rtr.upper(), rtr.upper(), xlabel ) )
    return "\n".join(nodes)


        #pprint('%s' %  CONFIGS[rtr].find_all_children('^hostname %s' % rtr))

def get_topology_nodes(test_path):
    parse = CiscoConfParse(test_path, syntax='ios')
    routers = []
    rtr_intf_list = []
    nodes = []
    font_size = 8
    i = 0
    for intf_obj in parse.find_objects(r'^hostname'):
        routers.append("%s" % intf_obj.re_match_typed(r'^hostname\s+(\S+)', default=''))
    for rtr in routers:
        config = CiscoConfParse( parse.find_all_children('^hostname %s$' % rtr) )
        CONFIGS[rtr]=config
        rtr_intf_list = get_rtr_intf(CONFIGS[rtr])
        #print('INTF LIST: %s@%s' %  (rtr,rtr_intf_list) )
        if not rtr_intf_list:
            #print('DEBUG: %s HAS NO INTERFACE' % rtr)
            #nodes.append('%s [ label="%s" ]' % ( rtr.upper(), rtr.upper() ) )
            nodes.append({
                'id': i,
                'name': rtr.upper(),
            })
        else:
            #xlabel = 'xlabel=< <font point-size="%s"> %s </font> >' % (font_size, " <br/> ".join(rtr_intf_list))
            #nodes.append('%s [ label="%s" %s]' % ( rtr.upper(), rtr.upper(), xlabel ) )
            node = {'id': i , 'name': rtr.upper()}
            xlabel = '%s' % (rtr_intf_list)
            for intf in rtr_intf_list:
                node = node | intf
            nodes.append(node)
            #nodes.append({
            #    'id': i,
            #    'name': rtr.upper(),
            #    'xlabel': xlabel,
            #})
        i = i + 1

    return (nodes)

def get_test_routers(test_path):
    parse = CiscoConfParse(test_path, syntax='ios')
    routers = []
    for intf_obj in parse.find_objects(r'^addrouter'):
        routers.append("%s" % intf_obj.re_match_typed(r'^addrouter\s+(\S+)', default=''))
    return routers

def get_intf_list(test_path,routers):
    parse = CiscoConfParse(test_path, syntax='ios')
    for rtr in routers:
        children = parse.find_children('^addrouter %s' % rtr)

def get_tst_connectors(test_path):
    parse = CiscoConfParse(test_path, syntax='ios')
    routers = []
    connectors = []
    conn_list = []
    for intf_obj in parse.find_objects(r'^addrouter'):
        routers.append("%s" % intf_obj.re_match_typed(r'^addrouter\s+(\S+)', default=''))

    for rtr in routers:
        EDGES = {}
        #print('RTR: %s' % (rtr) )
        children = parse.find_children('^addrouter %s' % rtr)
        #print('CHILDREN: %s' % children)
        conn_list = []
        for child in children:
            p = re.compile('^ int')
            if p.match(child):
                p_red = re.compile('^ int red')
                if not p_red.match(child):
                    conn_list.append(child)
        #connectors.append(children.pop(0))
        #parse_intfs (rtr, children)
        #print('CONN_LIST: %s' % conn_list)
        parse_intfs (rtr, conn_list)

def get_rtr_intf(p_config):
    logical_intfs = []

    loopbacks = p_config.find_objects(' int lo')
    for lo_obj in loopbacks:
        #print ('LO_OBJS: %s' % lo_obj.text)
        intf_label = None
        #print ('LOOPBACK=%s' % lo_obj.text )
        #print ('LOOPBACK=%s' % lo_obj.children )
        #intf_vrf = p_config.find_children_w_parents('%s' % lo.text,'  vrf for ')
        lo = lo_obj.re_match_typed(r'^\s+int\s+(lo\S+)$', default='')
        #print ('LO=%s' % lo)
        intf_vrf = p_config.find_children_w_parents('%s' % lo_obj.text,'vrf for')
        if len(intf_vrf) > 0:
            vrf = CiscoConfParse(intf_vrf).re_match_iter_typed(r'vrf\sfor\s(.*?)$')
        intf_ipv4 = p_config.find_children_w_parents('%s' % lo_obj.text,'ipv4')
        if len(intf_ipv4) > 0:
            ipaddr_ipv4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s(.*?)\s.*?$')
            hostmask4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s.*?\s(.*?)$')
            prefixlen4=IPv4Network('0.0.0.0/%s' % hostmask4).prefixlen
        intf_ipv6 = p_config.find_children_w_parents('%s' % lo_obj.text,'ipv6')
        if len(intf_ipv6) > 0:
            ipaddr_ipv6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s(.*?)\s.*?$')
            hostmask6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s.*?\s(.*?)$')
            prefixlen6=netMask2CIDR(hostmask6)

        if (len(intf_ipv4) > 0) and (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s - %s/%s]' % (lo,vrf,ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (lo,vrf)
            intf_ip = '%s/%s - %s/%s' %  (ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv4) > 0):
            #intf_label = '%s@%s[%s/%s]' % (lo,vrf,ipaddr_ipv4,prefixlen4)
            intf_vrf = '%s@%s' %  (lo,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv4,prefixlen4)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s]' % (lo,vrf,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (lo,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        else:
            intf_label = None
        if intf_label is not None:
            logical_intfs.append(intf_label)

    #print('LOGICAL_INTF AFTER LO: %s' % logical_intfs)


    bridge_intfs = p_config.find_objects(' int bvi')
    for bvi_obj in bridge_intfs:
        #print ('BVI_OBJS: %s' % bvi_obj.text)
        intf_label = None
        #print ('BVI=%s' % bvi_obj.text )
        #print ('BVI=%s' % bvi_obj.children )
        #intf_vrf = p_config.find_children_w_parents('%s' % lo.text,'  vrf for ')
        bvi = bvi_obj.re_match_typed(r'^\s+int\s+(bvi\S+)$', default='')
        #print ('BVI=%s' % bvi)
        intf_vrf = p_config.find_children_w_parents('%s' % bvi_obj.text,'vrf for')
        if len(intf_vrf) > 0:
            vrf = CiscoConfParse(intf_vrf).re_match_iter_typed(r'vrf\sfor\s(.*?)$')
        intf_ipv4 = p_config.find_children_w_parents('%s' % bvi_obj.text,'ipv4')
        if len(intf_ipv4) > 0:
            ipaddr_ipv4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s(.*?)\s.*?$')
            hostmask4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s.*?\s(.*?)$')
            prefixlen4=IPv4Network('0.0.0.0/%s' % hostmask4).prefixlen
        intf_ipv6 = p_config.find_children_w_parents('%s' % bvi_obj.text,'ipv6')
        if len(intf_ipv6) > 0:
            ipaddr_ipv6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s(.*?)\s.*?$')
            hostmask6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s.*?\s(.*?)$')
            prefixlen6=netMask2CIDR(hostmask6)
        #print('%s@%s[%s/%s - %s/%s]' % (bvi,vrf,ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)  )

        if (len(intf_ipv4) > 0) and (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s - %s/%s]' % (bvi,vrf,ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (bvi,vrf)
            intf_ip = '%s/%s - %s/%s' %  (ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv4) > 0):
            #intf_label = '%s@%s[%s/%s]' % (bvi,vrf,ipaddr_ipv4,prefixlen4)
            intf_vrf = '%s@%s' %  (bvi,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv4,prefixlen4)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s]' % (bvi,vrf,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (bvi,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        else:
            intf_label = None
        if intf_label is not None:
            logical_intfs.append(intf_label)

    #print('LOGICAL_INTF AFTER BVI: %s' % logical_intfs)

    tunnel_intfs = p_config.find_objects(' int tun')
    for tun_obj in tunnel_intfs:
        #print ('TUN_OBJS: %s' % tun_obj.text)
        intf_label = None
        #print ('BVI=%s' % bvi_obj.text )
        #print ('BVI=%s' % bvi_obj.children )
        #intf_vrf = p_config.find_children_w_parents('%s' % lo.text,'  vrf for ')
        tun = tun_obj.re_match_typed(r'^\s+int\s+(tun\S+)$', default='')
        #print ('TUN=%s' % tun)
        intf_vrf = p_config.find_children_w_parents('%s' % tun_obj.text,'vrf for')
        if len(intf_vrf) > 0:
            vrf = CiscoConfParse(intf_vrf).re_match_iter_typed(r'vrf\sfor\s(.*?)$')
        intf_ipv4 = p_config.find_children_w_parents('%s' % tun_obj.text,'ipv4')
        if len(intf_ipv4) > 0:
            ipaddr_ipv4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s(.*?)\s.*?$')
            hostmask4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s.*?\s(.*?)$')
            prefixlen4=IPv4Network('0.0.0.0/%s' % hostmask4).prefixlen
        intf_ipv6 = p_config.find_children_w_parents('%s' % tun_obj.text,'ipv6')
        if len(intf_ipv6) > 0:
            ipaddr_ipv6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s(.*?)\s.*?$')
            hostmask6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s.*?\s(.*?)$')
            prefixlen6=netMask2CIDR(hostmask6)
        #print('%s@%s[%s/%s - %s/%s]' % (tun,vrf,ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)  )

        if (len(intf_ipv4) > 0) and (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s - %s/%s]' % (tun,vrf,ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (tun,vrf)
            intf_ip = '%s/%s - %s/%s' %  (ipaddr_ipv4,prefixlen4,ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv4) > 0):
            #intf_label = '%s@%s[%s/%s]' % (tun,vrf,ipaddr_ipv4,prefixlen4)
            intf_vrf = '%s@%s' %  (tun,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv4,prefixlen4)
            intf_label = {intf_vrf:intf_ip}
        elif (len(intf_ipv6) > 0):
            #intf_label = '%s@%s[%s/%s]' % (tun,vrf,ipaddr_ipv6,prefixlen6)
            intf_vrf = '%s@%s' %  (tun,vrf)
            intf_ip = '%s/%s' %  (ipaddr_ipv6,prefixlen6)
            intf_label = {intf_vrf:intf_ip}
        else:
            intf_label = None
        if intf_label is not None:
            logical_intfs.append(intf_label)

    return logical_intfs

def parse_intfs(rtr, tst_intfs):
    for intf in tst_intfs:
        spl_intf = intf.split()
        #print('DEBUG CONN SPLIT: %s,%s,%s' % (spl_intf[4], rtr, spl_intf[1]))
        #print('spl_intf: %s' % (spl_intf) )
        #print('LENGTH: %s' % (len(spl_intf)) )
        conn = Connector(spl_intf[4], rtr, spl_intf[1] )
        CONNS[conn.id]=conn
        edge_key = "%s -- %s" % ( spl_intf[4],spl_intf[5] )
        reverse_edge_key = "%s -- %s" % ( spl_intf[5],spl_intf[4] )

        if (not (edge_key in EDGES)) and (not (reverse_edge_key in EDGES)):
            edge = Edge( id = "%s -- %s" % ( spl_intf[4],spl_intf[5] ))
            #print('DEBUG EDGE_ID: %s' % edge.id)
            EDGES[edge.id] = edge

def get_nodes():
    ipv4 = ''
    for node in CONNS:
        #print('CONN_ID: %s' % CONNS[node].id)
        #print('NODE_NAME: %s' % CONNS[node].node)
        p = CONFIGS[CONNS[node].node]
        #print('INTF: %s@%s' % (CONNS[node].node, CONNS[node].intf))
        #print (ccp.find_all_children('hostname %s' % CONNS[node].node))
        #print ('KEY:int %s' % CONNS[node].intf )
        #intf_ipv4 = p.find_children_w_parents('int %s\s+' % CONNS[node].intf,'ipv4')
        intf_ipv4 = p.find_children_w_parents('int %s$' % CONNS[node].intf,'ipv4')
        if len(intf_ipv4) > 0:
            CONNS[node].type=ConnType.ROUTED
            ipaddr_ipv4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s(.*?)\s.*?$')
            hostmask4 = CiscoConfParse(intf_ipv4).re_match_iter_typed(r'ipv4 addr\s.*?\s(.*?)$')
            #print('GET_NODE -> IPADDR_IPv4: %s' % ipaddr_ipv4)
            #print('GET_NODE -> HOSTMASK4: %s' % hostmask4)
            CONNS[node].ipv4 = ipaddr_ipv4
            CONNS[node].hostmask4 = hostmask4
        #intf_ipv6 = p.find_children_w_parents('int %s\s+' % CONNS[node].intf,'ipv6')
        intf_ipv6 = p.find_children_w_parents('int %s$' % CONNS[node].intf,'ipv6')
        if len(intf_ipv6) > 0:
            CONNS[node].type=ConnType.ROUTED
            ipaddr_ipv6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s(.*?)\s.*?$')
            hostmask6 = CiscoConfParse(intf_ipv6).re_match_iter_typed(r'ipv6 addr\s.*?\s(.*?)$')
            #print('GET_NODE -> IPADDR_IPv6: %s' % ipaddr_ipv6)
            #print('GET_NODE -> HOSTMASK6: %s' % hostmask6)
            #print('IPADDR_IPv6: %s' % ipaddr_ipv6)
            #print('HOSTMASK6: %s' % hostmask6)
            CONNS[node].ipv6 = ipaddr_ipv6
            CONNS[node].hostmask6 = hostmask6
        #intf_bridge = p.find_children_w_parents('int %s\s+' % CONNS[node].intf,'bridge')
        intf_bridge = p.find_children_w_parents('int %s$' % CONNS[node].intf,'bridge')
        if len(intf_bridge) > 0:
            CONNS[node].type=ConnType.BRIDGED
            CONNS[node].bridge_id = CiscoConfParse(intf_bridge).re_match_iter_typed(r'bridge-gr\s(.*?)$')

        #print (node)
        #print (CONNS[node].toDot())

def get_edges():
    edges = []
    for edge in EDGES:
        #print('GET_EDGES: %s' % edge )
        spl_edge = edge.split(" -- ")
        EDGES[edge].tailEnd = CONNS[spl_edge[0]]
        EDGES[edge].headEnd = CONNS[spl_edge[1]]
        EDGES[edge].tailLabel = CONNS[spl_edge[0]].intf
        EDGES[edge].headLabel = CONNS[spl_edge[1]].intf

        EDGES[edge].tailTooltip = CONNS[spl_edge[0]].ipv4
        EDGES[edge].headTooltip = CONNS[spl_edge[1]].ipv4
        #print(EDGES[edge].toDot())
        #edges.append(EDGES[edge].toDot())
        edges.append(EDGES[edge].toNext())

    return edges
    #return '\n'.join(edges)

def format_tst(tst_filepath):
   tst_file = open(tst_filepath,'r')
   tmp_file = open("%s.tmp" % tst_filepath ,'w')
   out_file = open("%s.tst2dot" % tst_filepath ,'w')
   lines = tst_file.readlines()
   p_add = re.compile('addrouter')
   p_end = re.compile('!')
   add = False
   output = ""
   cur_rtr = ""
   for line in lines:
       if add == True:
         #output = "  %s" % line.rstrip()
         output = " %s" % line
       else:
         #output = "%s" % line.rstrip()
         output = "%s" % line
       if p_add.match(line):
         cur_rtr = re.findall(r'^addrouter\s+(\S+)', line)[0]
         add = True
       if p_end.match(line):
         if add == True:
           output = line.rstrip()
           output = ""
           tmp_file.write("!\nhostname %s\n" % cur_rtr)
           add = False
       tmp_file.write("%s" % output)

   tst_file.close()
   tmp_file.close()


   tmp_file = open("%s.tmp" % tst_filepath,'r')

   lines = tmp_file.readlines()
   p_add = re.compile('hostname')
   p_end = re.compile('!')
   add = False
   output = ""

   for line in lines:
       if add == True:
         #output = "  %s" % line.rstrip()
         output = " %s" % line
       else:
         #output = "%s" % line.rstrip()
         output = "%s" % line
       if p_add.match(line):
         #cur_rtr = re.findall(r'^hostname\s+(\S+)', line)[0]
         add = True
       if p_end.match(line):
         if add == True:
           output = line.rstrip()
           #output = ""
           #out_file.write("!\nhostname %s\n" % cur_rtr)
           add = False

       out_file.write("%s" % output)

   tmp_file.close()
   out_file.close()


def tst2dot(tst_path):
    dot_node = []
    out_file = open("%s.dot" % (tst_path) ,'w')
    print(DOT_TEMPLATE)
    out_file.write(DOT_TEMPLATE)
    format_tst('%s' % tst_path)
    dot_node = get_rtr_config('%s.tst2dot' % tst_path)
    out_file.write(dot_node)
    print(dot_node)
    out_file.write('\n')
    get_tst_connectors('%s.tst2dot' % tst_path)
    get_nodes()
    out_file.write(get_edges())
    print(get_edges())
    out_file.write('\n}\n')
    out_file.close()
    print('}')

def tst2next(tst_path):
    dot_node = []
    out_file = open("%s.json" % (tst_path) ,'w')
    #print(DOT_TEMPLATE)
    #out_file.write(DOT_TEMPLATE)
    format_tst('%s' % tst_path)
    topology_data['nodes'] = get_topology_nodes('%s.tst2dot' % tst_path)
    get_tst_connectors('%s.tst2dot' % tst_path)
    get_nodes()
    topology_data['links'] = get_edges()
    out=json.dumps(topology_data, indent=4, sort_keys=False)
    print(out)
    out_file.write(out)
    out_file.write('\n')
    out_file.close()

# conn
# crypt
# mpls
# TBC: opnflw
# TBC: p4lang
# qos
# rout
# serv

#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/conn/'
#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/crypt/'
#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/mpls/'
#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/qos/'
#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/rout/'
#tst_dir_path = '/home/floui/nextcloud/all-tests/tst/serv/'
for tst in get_tst_list(tst_dir_path):
    print('--------------------------------------------------------------------')
    print(tst)
    print('--------------------------------------------------------------------')
    tst2next(tst)
    CONNS={}
    EDGES={}
    CONFIGS={}



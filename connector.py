#!/usr/bin/python3

from ipaddress import *
from enum import Enum

class ConnType(Enum):
   NONE = 0
   ROUTED = 1
   BRIDGED = 2

class Connector:
   id = None
   node = None
   intf = None
   type = ConnType.NONE
   ipv4 = None
   hostmask4 = None
   ipv6 = None
   hostmask6 = None
   bridge_id = None

   def __init__(self, id = None, node = None, intf = None, type = None,
                      ipv4 = None, hostmask4 = None,
                      ipv6 = None, hostmask6 = None, bridge_id = None):
      self.id = id
      self.node = node
      self.intf = intf
      self.type = type
      self.ipv4 = ipv4
      self.hostmask4 = hostmask4
      self.ipv6 = ipv6
      self.hostmask6 = hostmask6
      self.bridge_id = bridge_id

   def toString(self):
      return ("con[%s]=%s@%s" ) % (self.id, self.node, self.intf)

   def toDot(self):
      return ('%s [ label="%s" ]' % (self.node.upper(), self.node.upper()) )

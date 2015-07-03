# -*- coding: utf-8 -*-
"""
    avrodomain
    ~~~~~~~~~~

    Apache Avro domain.
"""

__version__ = "0.1"
# for this module's sphinx doc 
release = __version__
version = release.rsplit('.', 1)[0]

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField

avro_sig_regex = re.compile(
  r'''^
      ([^(]*?)       # type
      (\w+)          # name
      (?:\((.+?)\))? # args (optional)
      $
   ''', re.X)

class AvroObject(ObjectDescription):
  """Description of a general Avro object."""
  prefix = None
  
  def handle_signature(self,sig,signode):
    sig = sig.strip()
    type_name, name, arglist = avro_sig_regex.match(sig).groups()
    
    if self.prefix:
      signode += addnodes.desc_annotation(self.prefix+' ', self.prefix+' ')
    
    if type_name:
      signode += addnodes.desc_type(type_name, type_name)
    
    if name:
      signode += addnodes.desc_name(name,name)
    
    if arglist:
      paramlist = addnodes.desc_parameterlist()
      for arg in arglist.split(','):
        argtype, argname = arg.split(None,1)
        param = addnodes.desc_parameter(noemph=True)
        param += nodes.Text(argtype,argtype)
        param += nodes.emphasis(' '+argname,' '+argname)
        paramlist += param
      signode += paramlist
    
    return name

class AvroFixedField(AvroObject):
  prefix = 'fixed'
  doc_field_types = [
    Field('size', label=l_('Size'),
          names=('size',))
  ]

class AvroEnum(AvroObject):
  prefix = 'enum'
  doc_field_types = [
    Field('symbols', label=l_('Symbols'),
          names=('symbols',))
  ]

class AvroRecord(AvroObject):
  prefix = 'record'
  doc_field_types = [
    TypedField('fields', label=l_('Fields'),
               names=('field','member'),
               typenames=('type',),
               typerolename='record')
  ]

class AvroError(AvroRecord):
  prefix = 'error'

class AvroRPCMessage(AvroObject):
  doc_field_types = [
    TypedField('arguments', label=l_('Arguments'),
               names=('argument','arg','param'),
               typerolename='rpc'),
    GroupedField('errors', label=l_('Throws'),
                 names=('throws','throw'),
                 can_collapse=True),
    Field('returntype', label=l_('Returns'),
          names=('returns','return'))
  ]

class AvroDomain(Domain):
  name = "avro"
  label = "Apache Avro"
  
  object_types = {
    'fixed':  ObjType(l_('fixed'),  'fixed'),
    'enum':   ObjType(l_('enum'),   'enum'),
    'record': ObjType(l_('record'), 'record'),
    'error':  ObjType(l_('error'),  'error'),
    'rpc':    ObjType(l_('rpc'),    'rpc'),
  }
  
  directives = {
    'fixed':  AvroFixedField,
    'enum':   AvroEnum,
    'record': AvroRecord,
    'error':  AvroError,
    'rpc':    AvroRPCMessage
  }
  
  roles = {
    'fixed':  XRefRole(),
    'enum':   XRefRole(),
    'record': XRefRole(),
    'error':  XRefRole(),
    'rpc':    XRefRole()
  }
  
  initial_data = {
    'objects': {}
  }

def setup(app):
  app.add_domain(AvroDomain)

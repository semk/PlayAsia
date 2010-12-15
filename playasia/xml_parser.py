#! /usr/bin/env python
#
############################## Play-Asia api #################################
#
# The Play-Asia.com API is a set of functions that allow you to retrieve data 
# programmatically. Usage of the API is prohibited where you or your associates
# (in the loosest possible meaning) at any time
#   * act in competition to Play-Asia
#   * act against Play-Asia's interest
#   * let any third party gain knowledge of information retrieved through 
#     this API, other than in processed form*
# On request by Play-Asia, you will destroy all stored data you have retrieved 
# through this API. Play-Asia reserves the right to withdraw permission of 
# usage of any user without explanation or warning. Everything contained herein
# is confidential and you agree to give best efforts to keep confidentiality of 
# any aspect of the API and this agreement. 
#
# (*) Data retrieved through this API may not be accessible to anyone in raw 
# form (as-is). Where more information than the price and availability of items
# are displayed, you agree to put a clearly visible notice of the source of 
# data. (ex: Data-Feed: www.play-asia.com/paOS-00-3-api.html) Where product 
# descriptions are displayed you agree to display a copyright notice. 
# (ex: "Portions copyright (c) Play-Asia.com"). 

# In order to use the API, you have to agree to above terms.
#
###############################################################################
#
# @author: Sreejith K <http://foobarnbaz.com> <sreejithemk@gmail.com>
# Created On 13th Dec 2010
# Copyright (c) Play-Asia.com, 2010
#
## {{{ http://code.activestate.com/recipes/534109/ (r8)

import re
import xml.sax.handler

def xml2obj(src):
    """
    A simple function to converts XML data into native Python object.
    """

    non_id_char = re.compile('[^_0-9a-zA-Z]')

    def _name_mangle(name):
        return non_id_char.sub('_', name)

    class DataNode(object):
        def __init__(self):
            self._attrs = {}    # XML attributes and child elements
            self.data = None    # child text data

        def __len__(self):
            # treat single element as a list of 1
            return 1

        def __getitem__(self, key):
            if isinstance(key, basestring):
                return self._attrs.get(key,None)
            else:
                return [self][key]

        def __contains__(self, name):
            return self._attrs.has_key(name)

        def __nonzero__(self):
            return bool(self._attrs or self.data)

        def __getattr__(self, name):
            if name.startswith('__'):
                # need to do this for Python special methods???
                raise AttributeError(name)
            return self._attrs.get(name,None)

        def _add_xml_attr(self, name, value):
            if name in self._attrs:
                # multiple attribute of the same name are represented by a list
                children = self._attrs[name]
                if not isinstance(children, list):
                    children = [children]
                    self._attrs[name] = children
                children.append(value)
            else:
                self._attrs[name] = value

        def __str__(self):
            return self.data or repr(self._attrs)

        def __repr__(self):
            items = sorted(self._attrs.items())
            if self.data:
                items.append(('data', self.data))
            return u'{%s}' % ', '.join([u'%s:%s' % (k,repr(v)) for k,v in items])

    class TreeBuilder(xml.sax.handler.ContentHandler):
        def __init__(self):
            self.stack = []
            self.root = DataNode()
            self.current = self.root
            self.text_parts = []

        def startElement(self, name, attrs):
            self.stack.append((self.current, self.text_parts))
            self.current = DataNode()
            self.text_parts = []
            # xml attributes --> python attributes
            for k, v in attrs.items():
                self.current._add_xml_attr(_name_mangle(k), v)

        def endElement(self, name):
            text = ''.join(self.text_parts).strip()
            if text:
                self.current.data = text
            if self.current._attrs:
                obj = self.current
            else:
                # a text only node is simply represented by the string
                obj = text or ''
            self.current, self.text_parts = self.stack.pop()
            self.current._add_xml_attr(_name_mangle(name), obj)

        def characters(self, content):
            self.text_parts.append(content)

    builder = TreeBuilder()
    if isinstance(src,basestring):
        xml.sax.parseString(src, builder)
    else:
        xml.sax.parse(src, builder)
    return builder.root._attrs.values()[0]

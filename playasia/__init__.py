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

import sys
import urllib
from constants import *
from xml_parser import *

#FIXME Api key approved by PlayAsia.com
__api_key__ = 'YOUR-API-KEY-GOES-HERE'

#FIXME partner id provided by PlayAsia.com
__user_id__ = 0 # replace with your partner id

# Api url
__api_url__ = 'http://www.play-asia.com/__api__.php'


class InvalidArgumentError(Exception):
    """
    Raised when a given argument is invalid.
    """

class ArgumentMissingError(Exception):
    """
    Raised when a required argument is missing.
    """ 

class PlayAsia(object):
    
    def __init__(self, api_key=None, user_id=None):
        self.api_key = api_key or __api_key__
        self.user_id = user_id or __user_id__

    def _validate_keys(self, kwds, func):
        for key in kwds:
            #assert key in ALLOWED_KEYS[func]
            if key not in ALLOWED_KEYS[func]:
                raise InvalidArgumentError('Invalid argument \'%s\' for '\
                                            'function \'%s\'' %(key, func)) 
        for key in REQUIRED_KEYS[func]:
            #assert key in kwds
            if key not in kwds:
                raise ArgumentMissingError('\'%s\' is missing \'%s\' argument'\
                                            %(func, key))
        kwds[QUERY] = func
        xml = False
        if not kwds.get(QUICK, 1):
            xml = True
        if not kwds.get(KEY, None):
            kwds[KEY] = __api_key__
        if not kwds.get(USER, None):
            kwds[USER] = __user_id__
        return xml, kwds
    
    @classmethod
    def _build_query(cls, items):
        query = urllib.urlencode(items)
        return query

    def _parse_result(self, result):
        return xml2obj(result)

    def _fetch_result(self, data, parse=False):
        result = urllib.urlopen('%s?%s' %(__api_url__, data)).read()
        if parse:
            return self._parse_result(result)
        else:
            return result

    def test(self, **kwds):
        # pass the basic argument validation
        xml, kwds = self._validate_keys(kwds, 'test')
        query = self._build_query(kwds)
        result = self._fetch_result(query, xml)
        if xml:
            return result.content.item
        else:
            return result

    def info(self, **kwds):
        # pass the basic argument validation
        xml, kwds = self._validate_keys(kwds, 'info')
        query = self._build_query(kwds)
        result = self._fetch_result(query, xml)
        if xml:
            try:
                return result.content.item
            except:
                return result.status
        else:
            return result

    def paxfrombarcode(self, **kwds):
        # pass the basic argument validation
        xml, kwds = self._validate_keys(kwds, 'paxfrombarcode')
        query = self._build_query(kwds)
        result = self._fetch_result(query, xml)
        if xml:
            try:
                return result.content.item
            except:
                return result.status
        else:
            return result

    def paxfrommcode(self, **kwds):
        # pass the basic argument validation
        xml, kwds = self._validate_keys(kwds, 'paxfrommcode')
        query = self._build_query(kwds)
        result = self._fetch_result(query, xml)
        if xml:
            try:
                return result.content.item
            except:
                return result.status
        else:
            return result

    def listing(self, **kwds):
        #TODO: listing api
        xml, kwds = self._validate_keys(kwds, 'listing')
        query = self._build_query(kwds)
        return self._fetch_result(query, xml)

if __name__ == '__main__':
    p = PlayAsia()
    print p.test(quick=1)
    result = p.info(quick=0, pax='PAX0003120605', mask='pnl', fx='INR')
    print result
    result = p.paxfrombarcode(quick=0, bc='BLAS-50230')
    print result
    result = p.paxfrommcode(quick=0, code='BLAS-50230')
    print result
    #result = p.listing(quick=0, mask='pnl')
    #print result

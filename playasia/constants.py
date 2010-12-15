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

# Function keys
QUERY           = 'query'
QUICK           = 'quick'
KEY             = 'key'
USER            = 'user'
MASK            = 'mask'
PAX             = 'pax'
FX              = 'fx'
BC              = 'bc'
CODE            = 'code'
RESULTS         = 'results'
START           = 'start'
ONSALE          = 'onsale'
INSTOCK         = 'instock'
TYPE            = 'type'
COMPATIBLE      = 'compatible'
GENRE           = 'genre'
ENCODING        = 'encoding'
VERSION         = 'version'
SKIP_PREOWNED   = 'skip_preowned'
KEYWORD         = 'keyword'

# Allowed function keys
ALLOWED_KEYS = {
                'test'              : [QUICK, KEY, USER],
                'info'              : [QUICK, MASK, PAX, FX, KEY, USER],
                'paxfrombarcode'    : [QUICK, BC, KEY, USER],
                'paxfrommcode'      : [QUICK, CODE, KEY, USER],
                'listing'           : [QUICK, MASK, RESULTS, START, ONSALE, 
                                        INSTOCK,TYPE, COMPATIBLE, GENRE, 
                                        ENCODING, VERSION, SKIP_PREOWNED, 
                                        KEYWORD, KEY, USER]
                }

# Required function keys
REQUIRED_KEYS = {
                'test'              : [QUICK],
                'info'              : [QUICK, MASK, PAX, FX],
                'paxfrombarcode'    : [QUICK, BC],
                'paxfrommcode'      : [QUICK, CODE],
                'listing'           : [QUICK, MASK, RESULTS, START, ONSALE, 
                                        INSTOCK,TYPE, COMPATIBLE, GENRE, 
                                        ENCODING, VERSION, SKIP_PREOWNED, 
                                        KEYWORD]
                }

# Type list
GAME        = 1
ACCESSORY   = 2
CD          = 3
MOVIE       = 4
TOY         = 5	
BOOK        = 6
GROCERIES   = 7
APPAREL     = 8
ELECTRONICS = 9

#TODO Genre list

#TODO Compatible list

#TODO Encoding list

#TODO Version list

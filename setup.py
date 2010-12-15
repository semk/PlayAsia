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

import distutils.core
import sys

# Build the epoll extension for Linux systems with Python < 2.6
extensions = []
major, minor = sys.version_info[:2]
python_26 = (major > 2 or (major == 2 and minor >= 6))
if "linux" in sys.platform.lower() and not python_26:
    extensions.append(distutils.core.Extension(
        "tornado.epoll", ["tornado/epoll.c"]))

distutils.core.setup(
    name="playasia",
    version="0.1",
    packages = ["playasia"],
    author="Sreejith K",
    author_email="sreejithemk@gmail.com",
    url="http://www.foobarnbaz.com/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="PlayAsia.com api for Python",
)


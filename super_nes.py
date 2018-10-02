#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @name:    SuperNES - Super Nmap Easy Scanner
# @repo:    https://github.com/Sp1kes/SuperNES
# @author:  Roberto Mengibar (Sp1kes) sp1kes<at>protonmail.com
# @license: See the file 'LICENSE.txt'
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# This tool is only for Penetration Testing purposes. The author does not 
# assume any risk of the use of the tool, nor of the damages caused by it.
# Please, don't use the tool for illegal purposes.

import os
import sys
from subprocess import Popen, PIPE

# -- lib
from lib.utils.color import *
from lib.utils.banner import *
from lib.utils.checks import *
from lib.core.menus import *

# Definition of colors
r = lib.utils.color.colors().red(1)
e = lib.utils.color.colors().end()
b = lib.utils.color.colors().blue(1)
g = lib.utils.color.colors().green(1)
y = lib.utils.color.colors().yellow(1)
ny = lib.utils.color.colors().yellow(0)
w = lib.utils.color.colors().white(3)
bo = lib.utils.color.colors().bold(3)

#################################################################
## FUNCTIONS
#################################################################

def start():
	# Start P1
	print(g+"\n########################################"+e)
	print("")
	print(y+"         Single Player Mode"+e)
	print("")
	raw_input(bo+"   > PRESS ENTER BUTTON TO START <"+e)
	print("")
	print(g+"\n########################################"+e)

#################################################################
### MAIN
#################################################################

# Credits
#########
credits()

# Start
#######
start()

# Previous checks
#################
preChecks()

# Menu
######
# Parameter to continue in the loop "While" or exit(True for exit)
menuMainExit = False
menuMain(menuMainExit)

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
#import lib.utils.color
from lib.utils.color import *
from lib.utils.banner import * 

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

def check_Execs(*progs):
	# Check if the programs are installed, if not exit and report.
	for prog in progs:
		try:
			Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
		except	OSError:
			msgERR = r+" Error: "+e
			msg = '{0} program is necessary to run this script.'.format(prog)
			msgOut = "\n" + r+"        --- Game Over ---"+e + "\n\n"
			print(msgERR + msg)
			sys.exit(msgOut)
		else:
			msgOK = g+" Ok: "+e
			msg = '{0} is detected.'.format(prog)
			print(msgOK + msg)
	return
	
def preChecks():
	# Prerequisite checks
	print(ny+"\n............................"+e)
	print(ny+"Starting previous checks ..."+e)
	print(ny+"............................"+e)
	print(ny+"............................"+e + "\n")

	# Is nmap working
	check_Execs('nmap')

	# Is current user root
	isroot = os.getuid()
	if isroot == 0:
		print(g+" Ok: "+e + "Your current user is root.")
	else:
		print(r+" Error: "+e + "Your current user is NOT root.\n")
		sys.exit()
	
	# If directory not exist create directory
	print("\n" + b+" Info: "+e + "Current working directory is %s" % path)
	print(b+" Info: "+e + "Path of nmap results: " + nmapdir)
	
	if not os.path.exists(nmapdir):
		print("\n\t %s is not exist." % nmapdir)
		print("\tCreating directory ...")
		try:
			os.makedirs(nmapdir)
		except OSError:
			print("\n " + r+"Error: "+e + "Creation of the directory %s failed.\n" % nmapdir)
			sys.exit()
		else:
			print("\n " + g+"Ok: "+e + "Successfully created the directory %s " % nmapdir)
	else:
		print("\n " + g+"Ok: "+e + "%s exists." % nmapdir)

def menu1():
	# Menu
	# Set menuExit to False
	menuExit = False
	
	while not menuExit: # while menuExit is not True 

		print("\n-------------------------------------")
		print(g+"        ##################"+e)
		print(g+"        #"+e + bo+"      MENU:"+e + g+"     #"+e)
		print(g+"        ##################"+e)
		print("\t 1 - Ping scan.")
		print("\t 2 - Stealth scan.")
		print("\t 3 - Stealth & Detect versions scan.")
		print("\t 4 - OS version scan.")
		print("\t 5 - Complete scan.")
		print("\n\t 99 - Exit")
	
		# Ask for an option
		menuOption = raw_input("\n\t " + bo+"Select option: "+e)
		
		print("\n-------------------------------------")

		if menuOption == "1":
			option1()
		elif menuOption == "2":
			option2()
		elif menuOption == "3":
			option3()
		elif menuOption == "4":
			option4()
		elif menuOption == "5":
			option5()
		elif menuOption == "99":
			print("")
			print(r+"        --- Game Over ---"+e)
			print("")
			menuExit = True
		else:
			raw_input("\n\t" + bo+":( "+e + y+"Incorrect option.\n\n\t"+e + bo+"> press button to continue <"+e)
			menuExit = False

def option1():
	print("\n " + bo+"Ping scan"+e)
	print(g+" #########"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")

	print("\n" + ny+" Command: "+e + 'nmap -sn -oA %s/ping_scan %s' % (nmapdir,host))
	print("")
	os.system('nmap -sn -oA %s/ping_scan %s'% (nmapdir,host))
	os.system('xsltproc %s/ping_scan.xml -o %s/ping_scan.html'% (nmapdir,nmapdir))
	
	print("\n" + ny+"Result saved in: "+e + "%s/ping_scan.html"% (nmapdir))
	
def option2():
	print("\n " + bo+"Stealth scan"+e)
	print(g+" ############"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port (all: 1-65535): ")

	print("\n" + ny+" Command: "+e + 'nmap -sS -p%s -oA %s/stealth_scan %s'% (port,nmapdir,host))
	print("")
	os.system('nmap -sS -p%s -oA %s/stealth_scan %s'% (port,nmapdir,host))
	os.system('xsltproc %s/stealth_scan.xml -o %s/stealth_scan.html'% (nmapdir,nmapdir))
	
	print("\nResult saved in: %s/stealth_scan.html"% (nmapdir))
	
def option3():
	print("\n " + bo+"Stealth & Detect versions scan"+e)
	print(g+" #################################"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port (all: 1-65535): ")

	print("\n" + ny+" Command: "+e + 'nmap -sSV -O -p%s -oA %s/stealth_versions_scan %s'% (port,nmapdir,host))
	print("")
	os.system('nmap -sSV -O -p%s -oA %s/stealth_versions_scan %s'% (port,nmapdir,host))
	os.system('xsltproc %s/stealth_versions_scan.xml -o %s/stealth_versions_scan.html'% (nmapdir,nmapdir))
	
	print("\nResult saved in: %s/stealth_versions_scan.html"% (nmapdir))

def option4():
	print("\n " + bo+"OS version scan"+e)
	print(g+" ################"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")

	print("\n" + ny+" Command: "+e + 'nmap -O -oA %s/os_version_scan %s'% (nmapdir,host))
	print("")
	os.system('nmap -O -oA %s/os_version_scan %s'% (nmapdir,host))
	os.system('xsltproc %s/os_version_scan.xml -o %s/os_version_scan.html'% (nmapdir,nmapdir))
	
	print("\nResult saved in: %s/os_version_scan.html"% (nmapdir))
	
def option5():
	print("\n " + bo+"Complete scan"+e)
	print(g+" #############"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port(all: 1-65535): ")

	print("\n" + ny+" Command: "+e + 'nmap -sSV -A -T4 -p%s -oA %s/complete_scan %s'% (port,nmapdir,host))
	print("")
	os.system('nmap -sSV -A -T4 -p%s -oA %s/complete_scan %s'% (port,nmapdir,host))
	os.system('xsltproc %s/complete_scan.xml -o %s/complete_scan.html'% (nmapdir,nmapdir))
	
	print("\nResult saved in: %s/complete_scan.html"% (nmapdir))
	
#################################################################
### MAIN
#################################################################

# Previous tasks

# Detect the current working directory and print it
path = os.getcwd()
# Path of nmap results
nmapdir = path + "/results_SuperNES"

# Credits
credits()

# Start
start()

# Previous checks
preChecks()

# Menu
menu1()

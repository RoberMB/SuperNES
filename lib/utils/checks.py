#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
from subprocess import Popen, PIPE

# -- lib
import lib.utils.color
from lib.utils.color import *

# Global variables
global path
global nmapdir

# Detect the current working directory and print it
path = os.getcwd()
# Path of nmap results
nmapdir = path + "/results_SuperNES"

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

# Check executables
#################################################################
def checkExecs(*progs):
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
#################################################################

# Check Pre-requisites
#################################################################
def preChecks():
	# Prerequisite checks
	print(ny+"\n............................"+e)
	print(ny+"Starting previous checks ..."+e)
	print(ny+"............................"+e)
	print(ny+"............................"+e + "\n")

	# Is nmap working
	checkExecs('nmap')

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
#################################################################

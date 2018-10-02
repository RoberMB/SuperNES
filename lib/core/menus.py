#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys
from subprocess import Popen, PIPE

# -- lib
import lib.utils.color
from lib.utils.color import *
from lib.utils.checks import *

# Global variables
global path
global nmapdir
global custom

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

# MENU MAIN
#################################################################
def menuMain(menuMainExit):
	# Menu Main
	# Set menuMainExit to False
	#menuMainExit = False
		
	while not menuMainExit: # while menuMainExit is not True 

		print("\n-------------------------------------")
		print(g+"        ##################"+e)
		print(g+"        #"+e + bo+"      MENU:"+e + g+"     #"+e)
		print(g+"        ##################"+e)
		print("\t 1 - Discover.")
		print("\t 2 - Stealth scan.")
		print("\t 3 - Detect versions scan.")
		print("\t 4 - Full scan.")
		print("\t 5 - NSE Scripts.")
		print("\t 6 - Evasion.")
		print("\t 7 - Custom scan.")
		print("\n\t 99 - Exit")
		
		# Ask for an option
		menuOption = raw_input("\n\t " + bo+"Select option: "+e)
			
		print("\n-------------------------------------")

		if menuOption == "1":
			menu1()
		
		elif menuOption == "2":
			menu2()
		
		elif menuOption == "3":
			# Parameter to continue in the loop "While" or exit(True for exit)
			menu3Exit = False
			menu3(menu3Exit)
			
		elif menuOption == "4":
			menu4()
			
		elif menuOption == "5":
                        # Parameter to continue in the loop "while" or exit(True for exit)
                        menu5Exit = False
			menu5(menu5Exit)
			
		elif menuOption == "6":
			# Parameter to continue in the loop "While" or exit(True for exit)
			menu6Exit = False
			menu6(menu6Exit)
		
		elif menuOption == "7":
			menu7()
			
		elif menuOption == "99":
			print("")
			print(r+"        --- Game Over ---"+e)
			print("")
			menuMainExit = True
			break
		else:
			raw_input("\n\t" + bo+":( "+e + y+"Incorrect option.\n\n\t"+e + bo+"> press button to continue <"+e)
			menuMainExit = False

#################################################################

# MENU1
#################################################################
# 1 - Ping scan
def menu1():
	print("\n " + bo+"Ping scan"+e)
	print(g+" #########"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")

	print("\n" + ny+" Command: "+e + 'nmap -sn -oA %s/ping_scan %s' % (nmapdir,host))
	print("")
	os.system('nmap -sn -oA %s/ping_scan %s'% (nmapdir,host))
	os.system('xsltproc %s/ping_scan.xml -o %s/ping_scan.html'% (nmapdir,nmapdir))

	print("\n" + ny+"Result saved in: "+e + "%s/ping_scan.html"% (nmapdir))

#################################################################

# MENU2
#################################################################
# 2 - Stealth
def menu2():
	print("\n " + bo+"Stealth scan"+e)
	print(g+" ############"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port (all: 1-65535): ")

	print("\n" + ny+" Command: "+e + 'nmap -sS -p%s -oA %s/stealth_scan %s'% (port,nmapdir,host))
	print("")
	os.system('nmap -sS -p%s -oA %s/stealth_scan %s'% (port,nmapdir,host))
	os.system('xsltproc %s/stealth_scan.xml -o %s/stealth_scan.html'% (nmapdir,nmapdir))
			
	print("\n" + ny+"Result saved in: "+e + "%s/stealth_scan.html"% (nmapdir))

#################################################################

# MENU3
#################################################################
# 3 - Detect versions scan
def menu3(menu3Exit):
# Menu 3
	# Set menu3Exit to False
	#menu3Exit = False
	
	while not menu3Exit: # while menu3Exit is not True 

		print("\n-------------------------------------")
		print(g+"        ##################################"+e)
		print(g+"        #"+e + bo+"      Detect versions scan:"+e + g+"     #"+e)
		print(g+"        ##################################"+e)
		print("\t 1 - Stealth & Detect versions scan.")
		print("\t 2 - OS version scan.")
		print("\n\t 99 - Back")
		
		# Ask for an option
		menuOption = raw_input("\n\t " + bo+"Select option: "+e)
		
		print("\n-------------------------------------")

		if menuOption == "1":
			print("\n " + bo+"Stealth & Detect versions scan"+e)
			print(g+" #################################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sSV -O -p%s -oA %s/stealth_versions_scan %s'% (port,nmapdir,host))
			print("")
			os.system('nmap -sSV -O -p%s -oA %s/stealth_versions_scan %s'% (port,nmapdir,host))
			os.system('xsltproc %s/stealth_versions_scan.xml -o %s/stealth_versions_scan.html'% (nmapdir,nmapdir))
			print("\n" + ny+"Result saved in: "+e + "%s/stealth_versions_scan.html"% (nmapdir))
			
		elif menuOption == "2":
			print("\n " + bo+"OS version scan"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")

			print("\n" + ny+" Command: "+e + 'nmap -O -oA %s/os_version_scan %s'% (nmapdir,host))
			print("")
			os.system('nmap -O -oA %s/os_version_scan %s'% (nmapdir,host))
			os.system('xsltproc %s/os_version_scan.xml -o %s/os_version_scan.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/os_version_scan.html"% (nmapdir))
			
		elif menuOption == "99":
			menu3Exit = True
			menuMainExit = True
			menuMain(menuMainExit)
		else:
			raw_input("\n\t" + bo+":( "+e + y+"Incorrect option.\n\n\t"+e + bo+"> press button to continue <"+e)
			menu3Exit = False

#################################################################

# MENU4
#################################################################
# 4 - Full scan
def menu4():
	print("\n " + bo+"Full scan"+e)
	print(g+" #############"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port(all: 1-65535): ")

	print("\n" + ny+" Command: "+e + 'nmap -sSV -A -T4 -p%s -oA %s/complete_scan %s'% (port,nmapdir,host))
	print("")
	os.system('nmap -sSV -A -T4 -p%s -oA %s/complete_scan %s'% (port,nmapdir,host))
	os.system('xsltproc %s/complete_scan.xml -o %s/complete_scan.html'% (nmapdir,nmapdir))
	
	print("\n" + ny+"Result saved in: "+e + "%s/complete_scan.html"% (nmapdir))

#################################################################

# MENU5
#################################################################
# 5 - NSE Scripts
def menu5(menu5Exit):
	# Menu 5
	# Set menu5Exit to False
	menu5Exit = False
	
	while not menu5Exit: # while menu5Exit is not True 

		print("\n-------------------------------------")
		print(g+"        #########################"+e)
		print(g+"        #"+e + bo+"      NSE Scripts:"+e + g+"     #"+e)
		print(g+"        #########################"+e)
		print("\t 1 - Default scripts.")
		print("")
		print("\t 2 - Http Enumeration.")
		print("\t 3 - Http Brute-force.")
		print("\t 4 - Http Sitemap Generator.")
		print("\t 5 - Http Default Accounts.")
		print("")
		print("\t 6 - Whois Domain.")
		print("\t 7 - Traceroute Geolocation.")
		print("")
		print("\t 8 - Dns Brute-force.")
		print("\t 9 - Mysql Info.")
		print("\t10 - Smb OS Discovery.")
		print("\n\t 99 - Back")
		
		# Ask for an option
		menuOption = raw_input("\n\t " + bo+"Select option: "+e)
		
		print("\n-------------------------------------")

		if menuOption == "1":
			print("\n " + bo+"Default scripts"+e)
			print(g+" #################################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sC -p%s -oA %s/default_scripts %s'% (port,nmapdir,host))
			print("")
			os.system('nmap -sC -p%s -oA %s/default_scripts %s'% (port,nmapdir,host))
			os.system('xsltproc %s/default_scripts.xml -o %s/default_scripts.html'% (nmapdir,nmapdir))
			print("\n" + ny+"Result saved in: "+e + "%s/default_scripts.html"% (nmapdir))
			
		elif menuOption == "2":
			print("\n " + bo+"Http Enumeration"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")
			
			print("\n" + ny+" Command: "+e + 'nmap --script http-enum -p%s -oA %s/http-enum %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script http-enum -p%s -oA %s/http-enum %s'% (port,nmapdir,host))
			os.system('xsltproc %s/http-enum.xml -o %s/http-enum.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/http-enum.html"% (nmapdir))
			
		elif menuOption == "3":
			print("\n " + bo+"Http Brute-force"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --script http-brute -p%s -oA %s/http-brute %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script http-brute -p%s -oA %s/http-brute %s'% (port,nmapdir,host))
			os.system('xsltproc %s/http-brute.xml -o %s/http-brute.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/http-brute.html"% (nmapdir))
			
		elif menuOption == "4":
			print("\n " + bo+"Http Sitemap Generator"+e)
			print(g+" #######################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --script http-sitemap-generator -p%s -oA %s/http-sitemap-generator %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script http-sitemap-generator -p%s -oA %s/http-sitemap-generator %s'% (port,nmapdir,host))
			os.system('xsltproc %s/http-sitemap-generator.xml -o %s/http-sitemap-generator.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/http-sitemap-generator.html"% (nmapdir))
		
		elif menuOption == "5":
			print("\n " + bo+"Http Default Accounts"+e)
			print(g+" ######################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --script http-default-accounts -p%s -oA %s/http-default-accounts %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script http-default-accounts -p%s -oA %s/http-default-accounts %s'% (port,nmapdir,host))
			os.system('xsltproc %s/http-default-accounts.xml -o %s/http-default-accounts.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/http-default-accounts.html"% (nmapdir))
			
		elif menuOption == "6":
			print("\n " + bo+"Whois Domain"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host(domain.com): ")

			print("\n" + ny+" Command: "+e + 'nmap --script whois-domain -oA %s/whois-domain %s'% (nmapdir,host))
			print("")
			os.system('nmap --script whois-domain -oA %s/whois-domain %s'% (nmapdir,host))
			os.system('xsltproc %s/whois-domain.xml -o %s/whois-domain.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/whois-domain.html"% (nmapdir))
			
		elif menuOption == "7":
			print("\n " + bo+"Traceroute Geolocation"+e)
			print(g+" #######################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --traceroute --script traceroute-geolocation.nse -p%s -oA %s/traceroute-geolocation %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --traceroute --script traceroute-geolocation.nse -p%s -oA %s/traceroute-geolocation %s'% (port,nmapdir,host))
			os.system('xsltproc %s/traceroute-geolocation.xml -o %s/traceroute-geolocation.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/traceroute-geolocation.html"% (nmapdir))
		
		elif menuOption == "8":
			print("\n " + bo+"Dns Brute-force"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --script dns-brute -p%s -oA %s/dns-brute %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script dns-brute -p%s -oA %s/dns-brute %s'% (port,nmapdir,host))
			os.system('xsltproc %s/dns-brute.xml -o %s/dns-brute.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/dns-brute.html"% (nmapdir))
			
		elif menuOption == "9":
			print("\n " + bo+"Mysql Info"+e)
			print(g+" ############"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (80): ")

			print("\n" + ny+" Command: "+e + 'nmap --script mysql-info.nse -p%s -oA %s/mysql-info %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script mysql-info.nse -p%s -oA %s/mysql-info %s'% (port,nmapdir,host))
			os.system('xsltproc %s/mysql-info.xml -o %s/mysql-info.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/mysql-info.html"% (nmapdir))
			
		elif menuOption == "10":
			print("\n " + bo+"Smb OS Discovery"+e)
			print(g+" ################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (445): ")

			print("\n" + ny+" Command: "+e + 'nmap --script smb-os-discovery -p%s -oA %s/smb-os-discovery %s'% (port,nmapdir,host))
			print("")
			os.system('nmap --script smb-os-discovery -p%s -oA %s/smb-os-discovery %s'% (port,nmapdir,host))
			os.system('xsltproc %s/smb-os-discovery.xml -o %s/smb-os-discovery.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/smb-os-discovery.html"% (nmapdir))
			
		elif menuOption == "99":
			menu5Exit = True
			menuMainExit = True
			menuMain(menuMainExit)
		else:
			raw_input("\n\t" + bo+":( "+e + y+"Incorrect option.\n\n\t"+e + bo+"> press button to continue <"+e)
			menu5Exit = False

#################################################################

# MENU6
#################################################################
# 6 - Evasion
def menu6(menu6Exit):
# Menu 6
	# Set menu6Exit to False
	#menu6Exit = False
	
	while not menu6Exit: # while menu6Exit is not True 

		print("\n-------------------------------------")
		print(g+"        #####################"+e)
		print(g+"        #"+e + bo+"      Evasion:"+e + g+"     #"+e)
		print(g+"        #####################"+e)
		print("\t 1 - IP Spoofing.")
		print("\t 2 - Fragmentation.")
		print("\t 3 - Fragmentation choosing mtu.")
		print("\t 4 - Decoy.")
		print("\t 5 - MAC Spoofing.")
		print("\t 6 - Time Control.")
		print("\n\t 99 - Back")
		
		# Ask for an option
		menuOption = raw_input("\n\t " + bo+"Select option: "+e)
		
		print("\n-------------------------------------")
		
                if menuOption == "1":
			print("\n " + bo+"IP Spoofing"+e)
			print(g+" #################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
			mac = raw_input(" - MAC (the fake MAC of attacker): ")
			srcIP = raw_input(" - Source IP (10.10.10.2): ")
			srcPort = raw_input(" - Source Port (80): ")
			interface = raw_input(" - Interface (eth0): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -Pn --spoof-mac %s --source-port %s -n -e %s -S %s -p%s -oA %s/ping_ip_spoofing %s'% (mac,srcPort,interface,srcIP,port,nmapdir,host))
			print("")
			os.system('nmap -Pn --spoof-mac %s --source-port %s -n -e %s -S %s -p%s -oA %s/ping_ip_spoofing %s'% (mac,srcPort,interface,srcIP,port,nmapdir,host))
			os.system('xsltproc %s/ping_ip_spoofing.xml -o %s/ping_ip_spoofing.html'% (nmapdir,nmapdir))
			
			print("\n" + ny+"Result saved in: "+e + "%s/ping_ip_spoofing.html"% (nmapdir))

		elif menuOption == "2":
			print("\n " + bo+"Fragmentation"+e)
			print(g+" #########################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sS -f -p%s -oA %s/fragmentation %s'% (port,nmapdir,host))
			print("")
			os.system('nmap -sS -f -p%s -oA %s/fragmentation %s'% (port,nmapdir,host))
			os.system('xsltproc %s/fragmentation.xml -o %s/fragmentation.html'% (nmapdir,nmapdir))
			
			print("\n" + ny+"Result saved in: "+e + "%s/fragmentation.html"% (nmapdir))
			
		elif menuOption == "3":
			print("\n " + bo+"Fragmentation choosing mtu"+e)
			print(g+" #################################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
			mtu = raw_input(" - mtu (8): ")

			print("\n" + ny+" Command: "+e + 'nmap -sS -f --mtu %s -p%s -oA %s/fragmentation_mtu %s'% (mtu,port,nmapdir,host))
			print("")
			os.system('nmap -sS -f --mtu %s -p%s -oA %s/fragmentation_mtu %s'% (mtu,port,nmapdir,host))
			os.system('xsltproc %s/fragmentation_mtu.xml -o %s/fragmentation_mtu.html'% (nmapdir,nmapdir))

			print("\n" + ny+"Result saved in: "+e + "%s/fragmentation_mtu.html"% (nmapdir))
			
		elif menuOption == "4":
			print("\n " + bo+"Decoy"+e)
			print(g+" #######"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
			decoy = raw_input(" - Decoy (192.168.1.2,192.168.1.3,...): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sS -D %s,RND:10,ME -p%s -oA %s/decoy %s'% (decoy,port,nmapdir,host))
			print("")
			os.system('nmap -sS -D %s,RND:10,ME -p%s -oA %s/decoy %s'% (decoy,port,nmapdir,host))
			os.system('xsltproc %s/decoy.xml -o %s/decoy.html'% (nmapdir,nmapdir))
			
			print("\n" + ny+"Result saved in: "+e + "%s/decoy.html"% (nmapdir))
		
		elif menuOption == "5":
			print("\n " + bo+"MAC Spoofing"+e)
			print(g+" ###############"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
			mac = raw_input(" - MAC (the fake MAC of attacker): ")
			srcPort = raw_input(" - Source Port (80): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sS --spoof-mac %s --source-port %s -p%s -oA %s/fragmentation %s'% (mac,srcPort,port,nmapdir,host))
			print("")
			os.system('nmap -sS --spoof-mac %s --source-port %s -p%s -oA %s/fragmentation %s'% (mac,srcPort,port,nmapdir,host))
			os.system('xsltproc %s/fragmentation.xml -o %s/fragmentation.html'% (nmapdir,nmapdir))
			
			print("\n" + ny+"Result saved in: "+e + "%s/fragmentation.html"% (nmapdir))
			
		elif menuOption == "6":
			print("\n " + bo+"Time Control"+e) #nmap -T2 -sS --packet-trace -D [DECOY],RND:10,ME [TARGET]
			print(g+" #################################"+e)
			host = raw_input("\n - Host or Network(10.10.10.0/24): ")
			port = raw_input(" - Port (all: 1-65535): ")
			timeCtr = raw_input(" - Time control (T1-T5, where T1 is slower): ")
		
			print("\n" + ny+" Command: "+e + 'nmap -sS -%s -p%s -oA %s/time_control %s'% (timeCtr,port,nmapdir,host))
			print("")
			os.system('nmap -sS -%s -p%s -oA %s/time_control %s'% (timeCtr,port,nmapdir,host))
			os.system('xsltproc %s/time_control.xml -o %s/time_control.html'% (nmapdir,nmapdir))
			
			print("\n" + ny+"Result saved in: "+e + "%s/time_control.html"% (nmapdir))
			
		elif menuOption == "99":
			menu6Exit = True
			menuMainExit = True
			menuMain(menuMainExit)
		else:
			raw_input("\n\t" + bo+":( "+e + y+"Incorrect option.\n\n\t"+e + bo+"> press button to continue <"+e)
			menu6Exit = False

#################################################################

# MENU7
#################################################################
# 7 - Custom scan
def menu7():
	print("\n " + bo+"Custom scan"+e)
	print(g+" ###########"+e)
	host = raw_input("\n - Host or Network(10.10.10.0/24): ")
	port = raw_input(" - Port (all: 1-65535): ")
	custom = raw_input(" - Custom options (-sSV -v -T4 ...): ")

	print("\n" + ny+" Command: "+e + 'nmap %s -p%s -oA %s/custom_scan %s'% (custom,port,nmapdir,host))
	print("")
	os.system('nmap %s -p%s -oA %s/custom_scan %s'% (custom,port,nmapdir,host))
	os.system('xsltproc %s/custom_scan.xml -o %s/custom_scan.html'% (nmapdir,nmapdir))
	
	print("\n" + ny+"Result saved in: "+e + "%s/custom_scan.html"% (nmapdir))

#################################################################

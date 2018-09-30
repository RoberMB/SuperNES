#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# -- lib
import lib.utils.color

# Definition of colors
r = lib.utils.color.colors().red(1)
e = lib.utils.color.colors().end()
b = lib.utils.color.colors().blue(1)
g = lib.utils.color.colors().green(1)
y = lib.utils.color.colors().yellow(1)
ny = lib.utils.color.colors().yellow(0)
w = lib.utils.color.colors().white(3)
bo = lib.utils.color.colors().bold(3)

def credits():
    #This function clean screen and show the menu again.
    os.system('clear') # NOTE: for Windows system you must change 'clear' for 'cls'. For Linux system: 'clear'
    print(r+"  ____                         _   _ _____ ____  "+e)
    print(r+" / ___| _   _ _ __   ___ _ __ | \ | | ____/ ___| "+e)
    print(r+" \___ \| | | | '_ \ / _ \ '__||  \| |  _| \___ \ "+e)
    print(r+"  ___) | |_| | |_) |  __/ |   | |\  | |___ ___) |"+e)
    print(r+" |____/ \__,_| .__/ \___|_|   |_| \_|_____|____/ "+e)
    print(r+"             |_|                                  "+e)
    print(b+"                          Super Nmap Easy Scanner"+e)
    print("                                          v0.1 beta")
    
    print(g+"______██████████████"+e)
    print(g+"-____██▓▓▓▓▓▓▓▓▓ M ▓████"+e)
    print(g+"-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██"+e)
    print(g+"-__██████░░░░██░░██████"+e)
    print(g+"██░░░░████░░██░░░░░░░░██"+e)
    print(g+"██░░░░████░░░░██░░░░░░██"+e)
    print(g+"-__████░░░░░░██████████"+e)
    print(g+"-__██░░░░░░░░░░░░░██"+e)
    print(g+"_____██░░░░░░░░░██"+e)
    print(g+"-______██░░░░░░██"+e)
    print(g+"-____██▓▓████▓▓▓█"+e)
    print(g+"-_██▓▓▓▓▓▓████▓▓█"+e)
    print(g+"██▓▓▓▓▓▓███░░███░"+e)
    print(g+"-__██░░░░░░███████"+e)
    print(g+"-____██░░░░███████"+e)
    print(g+"-______██████████"+e)
    print(g+"-_____██▓▓▓▓▓▓▓▓▓██"+e)
    print(g+"-_____█████████████ "+e)

    print(g+"\n########################################"+e)
    print("|| " + b+"SuperNES - Super Nmap Easy Scanner "+e)
    
    print("\n|| Author: Roberto Mengibar " + r+"(Sp1kes)"+e)
    print("|| GitHub: https://github.com/RoberMB ")
    print(g+"\n########################################"+e)
    print("\n||| This tool is only for Penetration Testing purposes.")
    print("||| The author does not assume any risk of the use of the")
    print("    tool, nor of the damages caused by it. Please, don't use") 
    print("    the tool for illegal purposes.")

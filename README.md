SuperNES - Super Nmap Easy Scanner
========

SuperNES(__Super__Nmap__Easy__Scanner__) is a python open source security scanner that automates the process of scanning hosts and networks with the most used options of nmap. The main purpose of SuperNES is to makes scans easy and generate html reports of their results.   

SuperNES is built on python2.7 and can run on Linux platform which has a Python environment and nmap installed on it. And it needs to be executed as root.

This tool is designed for someone with no experience, with little experience or lazy with nmap :) and their most used options during a Penetration Testing for example in boxes of HackTheBox, iHacklabs, etc ... Always in controlled environments.

The author does not assume any risk of the use of the tool, nor of the damages caused by it. Please, don't use the tool for illegal purposes.

![screen_main](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_main.png)
![screen_prev_checks](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_prev_checks.png)
![screen_menu](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_menu.png)

Installation
========

You can download the latest version of SuperNES by cloning the GitHub repository:

- $ git clone https://github.com/RoberMB/SuperNES.git SuperNES
- $ cd SuperNES
- $ python super_nes.py

|||	|||	|||	|||	|||	|||

Features
========

v0.1 beta

**Ping Scan**
- nmap -sn -oA ./results_SuperNES/ping_scan [IP or Network]
- At the end of the scan generates html report.

**Stealth Scan**
- nmap -sS -p[PORT] -oA ./results_SuperNES/stealth_scan [IP or Network]
- At the end of the scan generates html report.

**Stealth & Detect versions scan**
- nmap -sSV -O -p[PORT] -oA ./results_SuperNES/stealth_versions_scan [IP or Network]
- At the end of the scan generates html report.

**OS version scan**
- nmap -O -oA ./results_SuperNES/os_version_scan [IP or Network]
- At the end of the scan generates html report.

**Complete Scan**
- nmap -sSV -A -T4 -p[PORT] -oA ./results_SuperNES/complete_scan [IP or Network]
- At the end of the scan generates html report.

|||	|||	|||	|||	|||	|||

Usage
========

	SuperNES - Super Nmap Easy Scanner
	Author: Roberto Mengibar (Sp1kes) sp1kes<at>protonmail.com
	
	Usage:	$ python super_nes.py

	Suggestions:	$ cd /boxes/box1
			$ python /tools/super_nes.py

	 1 - Ping scan.
	 2 - Stealth scan.
	 3 - Stealth & Detect versions scan.
	 4 - OS version scan.
	 5 - Complete scan.

**Ping Scan:
-------
Option 1

![screen_ping_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_ping_scan1.png)
![screen_ping_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_ping_scan2.png)

![screen_ping_scan_report](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_ping_scan_report.png)


**Stealth Scan:
-------
Option 2

![screen_stealth_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_stealth_scan.png)

![screen_stealth_scan_report](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_stealth_scan_report.png)


**Stealth & Detect versions scan:
-------
Option 3

![screen_stealth_detect_ver_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_stealth_detect_ver_scan.png)

![screen_stealth_detect_ver_report](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_stealth_detect_ver_report.png)


**OS version scan:
-------
Option 4

![screen_os_version_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_os_version_scan.png)

![screen_os_version_scan_report](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_os_version_scan_report.png)


**Complete Scan:
-------
Option 5

![screen_complete_scan](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_complete_scan.png)

![screen_complete_scan_report](https://raw.githubusercontent.com/RoberMB/SuperNES/master/screen/screen_complete_scan_report.png)

|||	|||	|||	|||	|||	|||

Advanced Usage
========

Coming soon ...

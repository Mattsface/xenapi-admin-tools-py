#!/usr/bin/python
# lsvdis.py
# Display VDIs and their parameters
#
# Date: 12/20/2013 
# Ver. 0.0.1
# Author: Matthew Spah

import XenAPI
import sys, getopt

def syntax():
	print "lsvdis version 0.1.1"
	print ""
	print "Syntax: lshosts [options]"
	print "-h This help text"
	print " -u - shows VDI UUID, Size, SR UUID, SR type, VM UUID and VM device"
	print "	-n - shows VDI Name, Size, SR Name, SR type, VM Name and VM device"
    print "	-m - shows VDI UUID, Size, SR Name, SR type, VM Name and VM device"
	print " -o <value> - change sort order by column, value can be vdi, size, sr, vm or device"
	print "	-s <host> - remote poolmaster host"
    print "	-p <password> - remote poolmaster password"
	print " -s <host> - remote poolmaster host"
	print "-w - number of whitespaces between columns"


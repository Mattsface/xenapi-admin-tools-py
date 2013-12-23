#!/usr/bin/python
# lsvdis.py
# Display VDIs and their parameters
#
# Date: 12/20/2013 
# Ver. 0.0.1
# Author: Matthew Spah

import XenAPI
import sys, getopt
from XAPIlib import *

def syntax():
	print "lsvdis version 0.1.1"
	print ""
	print "Syntax: lshosts [options]"
	print "-h This help text"
	print " -u - shows VDI UUID, Size, SR UUID, SR type, VM UUID and VM device"
	print "	-n - shows VDI Name, Size, SR Name, SR type, VM Name and VM device"
	print "	-m - shows VDI UUID, Size, SR Name, SR type, VM Name and VM device"
	print " -c --csv output CSV"
	print " -o <value> - change sort order by column, value can be vdi, size, sr, vm or device"
	print "	-s <host> - remote poolmaster host"
	print "	-p <password> - remote poolmaster password"
	print " -s <host> - remote poolmaster host"
	print "- w - number of whitespaces between columns"
	
	
def getvdidata(session):
	vdis = session.xenapi.VDI.get_all_records()
	SRs = session.xenapi.SR.get_all_records()
	vbds = session.xenapi.VBD.get_all_records()
	
	
	vdiArray = []
	
	for vdi in vdis:
		
		
		
		data = {
			"UUID":		vdis[vdi]['uuid'],
			"Size":		vdis[vdi]['virtual_size'],
			
		
		
		
		}
	

def main():
	try:
		myopts, args = getopt.getopt(sys.argv[1:], "hunmw:",["help", "uuid", "name", "mix", "wspace"])
	except getopt.GetoptError:
		print "Unknown options"
		syntax()
		sys.exit(1)
	minspace = 4
	CSV = False
	mode = "name"
	for opt, arg in myopts:
		if opt in ("-h", "--help"):
			syntax()
			sys.exit(1)
		elif opt in ("-u", "--uuid"):
			mode = "uuid"
		elif opt in ("-n", "--name"):
			mode = "name"
		elif opt in ("-m", "--mix"):
			mode = "mix"
		elif opt in ("-c", "--csv"):
			CSV = True
		elif opt in ("-w", "--wspace"):
			minspace = int(arg)
	
	session = XenAPI.xapi_local()
	
	session.xenapi.login_with_password("", "")

	vdidata = getvdidata(session)
	
	print vdidata


main()

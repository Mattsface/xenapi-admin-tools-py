#!/usr/bin/python
# lshosts.py
# Display all hosts and parameters in a xenserver pool
#
# Date: 12/10/2013 
# Ver. 0.0.1
# Author: Matthew Spah
# Date: 12/19/2013
# Ver. 0.1.0
# Desc: Added formatarray() and made modifications to gethostdata()
# Ver. 0.1.1
# Desc: Added Tot mem and Free mem

import XenAPI
import sys, getopt	


def syntax():
	print "lshost version 0.0.1"
	print ""
	print "Syntax: lshosts [options]"
	print "-h This help text"
	print "-u Show UUIDs"
	print "-n Show Names (default)"
	print "-c output CSV"
	print ""
	
def gethostdata(session):		
	
	records = session.xenapi.host.get_all_records()
	metrics = session.xenapi.host_metrics.get_all_records()
	
	hArray = []
	for x in records:
		
		metobjuuid = records[x]['metrics']
		totmem = round(float(metrics[metobjuuid]['memory_total']) / 1024 ** 3, 2)
		freemem = round(float(metrics[metobjuuid]['memory_free']) / 1024 ** 3, 2)
		
		data = {
			"UUID":			records[x]['uuid'],
			"Name-label":	records[x]['name_label'],
			"Active-VMs":	len(records[x]['resident_VMs']),
			"CPU-Model":	records[x]['cpu_info']['modelname'],
			"CPUs":			len(records[x]['host_CPUs']),
			'Tot Mem':		str(totmem) + "GB",
			'Free Mem':		str(freemem) + "GB",
			"Ver":			records[x]['software_version']['platform_version'],
			"Network":		records[x]['software_version']['network_backend'],
		}
		hArray.append(data)
		
	return hArray	

def formatdarray(data, order, minspace=4, CSV=False):
	
	string_data = [[str(row[col]) for col in order] for row in data]
	
	string_data.insert(0, [name for name in order])
	
	if CSV:
		
		formatstr = (',').join(string for string in row for row in string_data)
		
		return formatstr
		
	else:
	
		colwidths = [max(len(row[col]) for row in string_data) for col in range(len(order))]
	
		formatstr = (' ' * minspace).join('%%-%ds' % width for width in colwidths)
	
		return '\n'.join(formatstr % tuple(line) for line in string_data)

def defineheadings(mode):

	if mode == "name":
		headings = ('Name-label', 'Active-VMs', 'CPU-Model', 'CPUs', 'Tot Mem', 'Free Mem', 'Ver', 'Network')
	elif mode == "uuid":
		headings = ('UUID', 'Active-VMs', 'CPU-Model', 'CPUs', 'Tot Mem', 'Free Mem', 'Ver', 'Network')
	
	return headings

def main():
	try:
		myopts, args = getopt.getopt(sys.argv[1:], "hunc",["help", "uuid", "name", "csv"])
	except getopt.GetoptError:
		print "Unknown options"
		syntax()
		sys.exit(1) 
	minspace = 4
	csv = False
	mode = "name"
	for opt, arg in myopts:
		if opt in ("-h", "--help"):
			syntax()
			sys.exit(1)
		elif opt in ("-u", "--uuid"):
			mode = "uuid"			
		elif opt in ("-n", "--name"):
			mode = "name"
		elif opt in ("-c", "--csv"):
			CSV = True 
	
	session = XenAPI.xapi_local()
	
	session.xenapi.login_with_password("root", "Chopper1man")
	
	hosts = gethostdata(session)
	
	headings = defineheadings(mode)
	
	print formatdarray(hosts, headings, minspace, CSV)
	
main()

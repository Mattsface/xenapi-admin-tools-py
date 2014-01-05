#!/usr/bin/python
# lsvms.py
# Display VMs and their parameters
#
# Date: 1/2/2014 
# Ver. 0.0.1
# Author: Matthew Spah

import XenAPI
import sys, getopt
from XAPIlib import *

def syntax():
    print ""
    print "	Syntax: $(basename $0) [options]"
    print "	Options:"
    print "	-d - shell debugging"
    print "	-c - output comma seperated values"
    print "	-u - shows VM UUID, Status, Host UUID"
    print "	-b - shows VM Name, Status, VMUUID, Host Name and Host UUID"
    print "	-n - shows VM Name, Status and Hostname"
    print "	-m - shows VM Name, Status, VM UUID and Hostname"
    print "	-o <value> - changes sort order by column, value can be vmname, hostname, vmuuid, hostuud"
    print "	-r - use local config files for remote poolmasters"
    print "	-s <host> - remote poolmaster host"
    print "	-p <password> - remote poolmaster password"
    print "	-h - this help text"
    print "	-w - number of whitespaces between columns"
    print ""


def getvmdata(session):
    vmArray = []   
    vms = session.xenapi.VM.get_all()
    for vm in vms:
        if session.xenapi.VM.get_is_a_template(vm):
            continue
        elif session.xenapi.VM.get_is_control_domain(vm):
            continue
        elif session.xenapi.VM.get_is_a_snapshot(vm):
            continue
        else:
            vmhostref = session.xenapi.VM.get_resident_on(vm)

            data = {
                'UUID' = session.xenapi.VM.get_uuid(vm),
                'Name' = session.xenapi.VM.get_name_label(vm),
                'Host UUID' = session.xenapi.host.get_uuid(vmhostref), # fix this
                'Host Name' = session.xenapi.host.get_name_label(vmhostref),
                'Dom ID' = session.xenapi.VM.get_domid(vm), # finish this
                'Status' = session.xenapi.VM.get_power_state(vm)   
            }
    return vmArray
                
def main():
	session = XenAPI.xapi_local()
	session.xenapi.login_with_password("", "")

	vmdata = getvmdata(session)

	print vmdata
	

main()
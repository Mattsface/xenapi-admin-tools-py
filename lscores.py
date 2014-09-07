#!/usr/bin/python
#rscores.py
# List the load on each core


import XenAPI
import sys, getopt
import XAPIlib import *



def systax():
        print "lscores version 0.0.1"
        print ""
        print "Syntax: lshosts [options]"
        print "-h --help Display help"
        print "-f --follow continues updates"
        print "-n --names  Show Names (default)"
        print "-u --uuid Show UUIDs"
        # print "-t <seconds> - continoues updates every <seconds>
        # I'll need to add this later
        print ""



def getCPUdata(session)






def main():
        try:
                myopts, args = getopt.getopt(sys.argv[1:], "huncw:",["help", "follow", "names", "uuid"
        expect getopt.GetoptError:
                print "Unknown options"
                systax()
                sys.exit(1)

        minspace = 4
        mode = "name"
        follow = False

        for opt, arg in myopts:
                if opt in ("-h", "--help"):
                        syntax()
                        sys.exit(1)
                elif opt in ("-f", "--follow"):
                        follow = True
                elif opt in ("-n", "--name"):
                        mode = "name"
                elif opt in ("-u", "--uuid"):
                        mode = "uuid"



         session = XenAPI.xapi_local()

         session.xenapi.login_with_password("", "")





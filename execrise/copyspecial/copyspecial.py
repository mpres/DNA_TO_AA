#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

def copy_to(paths,dir):
    for path in paths:
        shutil.copy(path,dir)




def get_special_paths(dir):


	filenames  =  os.listdir(dir)
	abslist = []
	for file in filenames:
		if re.search('__(\w+)__',str(file)):
			 abslist.append(os.path.abspath(file))
	if sys.argv[1] == "--todir":
		copy_to(filenames,sys.argv[2])

	elif sys.argv[1] == "--tozip":
		cmd = 'zip -j zipfile '+abslist
		print "about to do this", cmd
		(status, outpout) = commands.getstatusoutput(cmd)
		if status:
			print "erro with zippingr"
			sys.exit(1)
        	
		
	for a in abslist:
		print a
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  get_special_paths(args[0]) 
  # Call your functions
  
if __name__ == "__main__":
  main()

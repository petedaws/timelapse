#!/usr/bin/env python
import glob
import os
import sys
import shutil
import re

def rename_file(startnum,firstnum,prefix,extension):
	for filename in os.listdir('.'):
		mo = re.match(r'(%s)(\d*)(\.%s)'% (prefix,extension),filename)
		if mo is not None:
			numname = (int(mo.group(2)) - startnum + firstnum)
			if numname >= 0:
				newname = 'image-%08d.jpeg' % (numname)
				os.rename(filename,newname) 

if __name__ == "__main__":
	if len(sys.argv) > 1:
		rename_file(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4])
	else:
		print "rename_file.py <startnum> <firstnum> <prefix> <extension>"

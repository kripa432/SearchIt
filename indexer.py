#! /usr/local/bin/python3
import math
import re



def index(str,file,dict):
	print file
	list=re.split(r'[ ;:_.,/\*\\\-<>@\(\)\n0-9$]',str)
	list=filter(None,list)
	#print list
	for i in list:
		print i
		
		dict[i]=dict[i]+[file]

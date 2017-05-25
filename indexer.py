#! /usr/local/bin/python3
import math
import re

def index(str,file,dict):
	#spliting the string into words removing special character and numbers
	list=re.split(r'[ ;:_.,/\*\\\-<>@\(\)\n0-9$]',str)
	#removing empty words
	list=filter(None,list)
	#inserting location of file into index
	for i in list:
		try:
			dict[i]=dict[i]+[file]
		except:
			dict[i]=[file]

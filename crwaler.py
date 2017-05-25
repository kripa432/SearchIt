#! /usr/local/bin/python2
import PyPDF2
import docx
import os
import glob
import csv
import re
import textract
import json
from indexer import *

os.chdir("./data") #change the current working directory


class init(dict):
	def __missing__(self,key):
		return []

dict=init()
#crawling the directories and sub directories for files
for root,directories,filenames in os.walk("."):
	# os.walk returns 3-tuple (directory path, dirctory names, filenames)
	for filename in filenames:
		#compiled string to be generated to be passed to indexer
		cstr=''
		#obtaining full path of file
		file= os.path.join(root,filename)
		#extracting of the file using textract library function
		cstr+=textract.process(file, encoding='ascii')

		if len(cstr)!=0:
			# Calling  the indexing function
			index(cstr,file,dict)
			cstr=''
#dumping the data of dictionary to a database file
json.dump(dict,open("../database.txt","w"))




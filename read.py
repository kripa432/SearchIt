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


#sample for extracting text from first page of file
#f=open("../data/gandhinagar.pdf","rb")
#print PyPDF2.PdfFileReader(f).getPage(0).extractText()


os.chdir("./data")

#pdffiles=[]
#for file in os.listdir('../data/'):
#	if file.endswith(".pdf"):
#		pdffiles+=[file]
#		f=open("../data/"+file,"rb")
#		pdf=PyPDF2.PdfFileReader(f)
#		n=pdf.numPages
#		for i in range(n):
#			print pdf.getPage(i).extractText().encode("utf8")

class init(dict):
	def __missing__(self,key):
		return []

dict=init()

for root,directories,filenames in os.walk("."):
	for filename in filenames:
		cstr=''
		file= os.path.join(root,filename)
		cstr+=textract.process(file, encoding='ascii')

		if len(cstr)!=0:
			# Call the indexing function
			index(cstr,file,dict)
			cstr=''

json.dump(dict,open("../database.txt","w"))




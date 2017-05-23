#! /usr/local/bin/python2
import PyPDF2
import os
import glob

#sample for extracting text from first page of file
#f=open("../data/gandhinagar.pdf","rb")
#print PyPDF2.PdfFileReader(f).getPage(0).extractText()


os.chdir("../data/")

#pdffiles=[]
#for file in os.listdir('../data/'):
#	if file.endswith(".pdf"):
#		pdffiles+=[file]
#		f=open("../data/"+file,"rb")
#		pdf=PyPDF2.PdfFileReader(f)
#		n=pdf.numPages
#		for i in range(n):
#			print pdf.getPage(i).extractText().encode("utf8")

for root,directories,filenames in os.walk("."):
	for directory in directories:
		print os.path.join(root,directory)
	for filename in filenames:
		file= os.path.join(root,filename)
		if file.endswith(".pdf"):
			f=open(file,"rb")
			pdf=PyPDF2.PdfFileReader(f)
			n=pdf.numPages
			for i in range(n):
				print pdf.getPage(i).extractText().encode("utf8")
		elif file.endswith(".docx"):
			print "doc file stub"
		elif file.endswith(".csv"):
			print "csv file stub"
		elif file.endswith(".txt"):
			print "txt file stub"




#! /usr/local/bin/python3
import json
import os
import webbrowser
dict=json.load(open("database.txt"))

os.chdir("./data")


query=raw_input().split()
lis=[]
for i in query:
	try:
		lis+=dict[i]
	except:
		pass
c=1;
for i in lis:
	print str(c)+' '+str(i)
	c+=1

print "enter file no to open"
i=raw_input()
webbrowser.open(lis[int(i)-1])

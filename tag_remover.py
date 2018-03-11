# remove special character and remove stop words
import re
import fileinput
import os, sys
import shutil


directoris = ["L_the_patient", "U_Patient", "U_The_patient"]
genders = ["female", "male", "universal"]


for dir_index in directoris:
	for gender_index in genders:
		dir = "letters/"+dir_index+"/"+gender_index+"/"
		path = os.fsencode(dir)

		for file in os.listdir(path):
			filename = os.fsdecode(file)
			print(filename)
			if filename != ".DS_Store":
				f = open(dir+filename,'r')
				filedata = f.read()
				f.close()
				
				cleanr = re.compile("<.*?>")
				newdata = re.sub(cleanr, '', filedata)

				f = open(dir+filename,'w')
				f.write(newdata)
				f.close()
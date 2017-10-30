#Declaring libraries

import os
import sys
import urllib
import time
#import pdb for debugging

#Opening and Reading the file to "urlfile" list
with open(sys.argv[1]) as f:
	urlfile = f.read().splitlines()
	
#creting a folder to store downloaded files
os.mkdir("Downloaded")

#using count to iterate through the list index as well as declaring a path list
count = 0
path = []

#downloadiing the files to the created folder and recording their url link, size, and time(ms) inside the url list. 
for line in urlfile:
	time_start = time.clock()
	urllib.urlretrieve(line,"Downloaded/"+str(count)+".jpg")
	elapsedtime = (time.clock() - time_start)*1000
	statinfo = os.stat("Downloaded/"+str(count)+".jpg")
	urlfile[count] = [urlfile[count], statinfo.st_size, int(elapsedtime)]
	path.append(["Downloaded/"+str(count)+".jpg", int(elapsedtime)])
	count += 1



#sorting my lists by the time index
urlfile.sort(key=lambda x: x[2])
path.sort(key=lambda x: x[1])

#making folders to put Fast and slow downloaded files
os.mkdir("Downloaded/FastDownloaded")
os.mkdir("Downloaded/SlowDownloaded")

#interating through path list in order to moves files to the correct folder
count = 0
for item in path:
	if(count < (len(path)/2)):
		os.rename(path[count][0], "Downloaded/FastDownloaded/"+str(count)+".jpg")
	else:
		os.rename(path[count][0], "Downloaded/SlowDownloaded/"+str(count)+".jpg")
	count += 1 

#pdb.set_trace() for debugging

# printing the report
print "Fast Downdloaded files"
print "URL, Size(bytes), Time(ms)\n"

for yolo in urlfile[0:5]:
	print yolo
			
print "\n\n\n---------------------\n\n\n"
print "Slow Downloaded files"
print "URL, Size(bytes), Time(ms)\n"

for yoyo in urlfile[5:]:
	print yoyo

